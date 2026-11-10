# qiumingdll_net_get_shared_vars_json()

获取当前共享变量的快照（JSON 数组字符串）。

## 函数签名

```gml
qiumingdll_net_get_shared_vars_json()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数 |

## 返回值

| 端 | 返回值 |
|----|--------|
| host | `[{"name":"score","value":123},{"name":"round","value":3},...]`（注册顺序） |
| client | host 同步过来的最近一次快照（WELCOME + 后续增量） |
| 未连接 | `"[]"` |

> 返回字符串使用内部静态缓冲区，**在下一次调用本函数前有效**；需要跨帧保存请立即 `json_parse` 或复制。

## 使用说明

- 数组元素的 `value` 是**任意 JSON 值**（数字/字符串/布尔/对象/数组），由 host 写入时决定类型；读取时按业务约定使用。
- client 端缓存随 WELCOME 初始化，随后由每条变量广播增量更新，因此该函数始终反映“最新已知值”。
- 这是拉取式快照；事件式获取请用 `poll_json()` 的 `kind="var"` 事件（两者数据一致，选择一种消费方式即可）。
- 该函数只读，不会清空任何状态；未注册的变量为空数组。
- 值由 host 以 JSON 文本原样广播，本模块不做类型转换；请确保写入时是合法 JSON。

## 示例

```gml
var _vars = json_parse(qiumingdll_net_get_shared_vars_json());
var _map = {};

for (var i = 0; i < array_length(_vars); i++)
{
    _map[$ _vars[i].name] = _vars[i].value;
}

if (variable_struct_exists(_map, "score"))
{
    global.score = _map.score;
}

// 同步一个对象变量
if (variable_struct_exists(_map, "gameState"))
{
    global.round = _map.gameState.round;
    global.phase = _map.gameState.phase;
}
```

## 相关函数

- [qiumingdll_net_register_shared_var](qiumingdll_net_register_shared_var.md)
- [qiumingdll_net_set_shared_var](qiumingdll_net_set_shared_var.md)
- [qiumingdll_net_poll_json](qiumingdll_net_poll_json.md)
