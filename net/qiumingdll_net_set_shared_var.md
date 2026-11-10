# qiumingdll_net_set_shared_var()

host 设置共享变量的值（JSON 字面量），并立即广播给所有 client。

## 函数签名

```gml
qiumingdll_net_set_shared_var(name, json_value)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| name | string | 是 | 变量名（区分大小写） |
| json_value | string | 是 | 变量值的 **JSON 字面量文本**，会原样广播 |

`json_value` 是 JSON 而不是 GML 值，注意引号：

| 想要的值 | 应传的字符串 |
|----------|--------------|
| 数字 123 | `"123"` |
| 字符串 "abc" | `"\"abc\""` |
| 布尔真 | `"true"` |
| 对象 | `"{\"hp\":10,\"mp\":5}"` |
| 数组 | `"[1,2,3]"` |

## 返回值

| 值 | 说明 |
|----|------|
| `1` | 设置并广播成功（host） |
| `0` | 失败：当前不是 host（client/未连接），或 name 为空 |

## 使用说明

- **仅 host 有效**。client 调用恒定返回 `0`，共享变量由 host 权威决定。
- 未注册过的名字会自动注册（等效于隐式 `register_shared_var`），因此不注册也能用。
- 每次设置都会：更新 host 本地快照 → 广播给所有 client → 给 host 自己入队一条 `kind="var"` 事件（`peer=0`）。
- client 收到后缓存并在 `get_shared_vars_json()` 中反映，同时入队 `kind="var"` 事件（`peer=0`）。
- **请务必传入合法 JSON**：本模块不做校验，非法文本会原样进入事件 JSON，导致 `poll_json()` 输出无法解析。
- 广播是“最后写入胜出”，不做确认与回滚；高频更新建议自行合并（例如每帧最多同步一次）。

## 示例

```gml
// host：分数变化时同步
global.score += 10;
qiumingdll_net_set_shared_var("score", string(global.score));

// 同步一个对象
qiumingdll_net_set_shared_var("gameState", "{\"round\":3,\"phase\":\"battle\"}");

// 同步字符串（注意转义）
qiumingdll_net_set_shared_var("hostName", "\"Alice\"");
```

client 侧读取：

```gml
var _vars = json_parse(qiumingdll_net_get_shared_vars_json());
for (var i = 0; i < array_length(_vars); i++)
{
    if (_vars[i].name == "score") global.score = _vars[i].value;
}
```

## 相关函数

- [qiumingdll_net_register_shared_var](qiumingdll_net_register_shared_var.md)
- [qiumingdll_net_get_shared_vars_json](qiumingdll_net_get_shared_vars_json.md)
- [qiumingdll_net_poll_json](qiumingdll_net_poll_json.md)
