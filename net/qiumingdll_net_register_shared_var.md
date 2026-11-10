# qiumingdll_net_register_shared_var()

host 声明一个需要同步给所有 client 的共享变量名。

## 函数签名

```gml
qiumingdll_net_register_shared_var(name)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| name | string | 是 | 变量名（区分大小写），例如 `"score"`、`"round"`、`"gameState"` |

## 返回值

| 值 | 说明 |
|----|------|
| `1` | 注册成功；同名变量已注册时同样返回 `1`，且不会重置其当前值 |
| `0` | 失败：当前不是 host（client 或未连接），或 name 为空 |

## 使用说明

- **仅 host 有效**。共享变量是 host 权威的：client 只能读取，不能写入。
- 注册只是“声明名字”，初始值为 `0`；真正写入值请调用 `qiumingdll_net_set_shared_var()`。
- 未注册的名字在 `set_shared_var` 时也会被自动注册，因此注册主要用于提前声明与让新加入的 client 在 WELCOME 中收到初始值。
- 新 client 加入时，WELCOME 快照会带上所有已注册变量的当前值，并以 `kind="var"` 事件入队。
- 变量值可以是任意合法 JSON（数字、字符串、布尔、对象、数组），由调用方自行约定含义。

## 示例

```gml
// host 的 Create 事件
qiumingdll_net_host_start("0.0.0.0", 25565, 4);
qiumingdll_net_register_shared_var("score");
qiumingdll_net_register_shared_var("round");
qiumingdll_net_register_shared_var("gameState");
```

## 相关函数

- [qiumingdll_net_set_shared_var](qiumingdll_net_set_shared_var.md)
- [qiumingdll_net_get_shared_vars_json](qiumingdll_net_get_shared_vars_json.md)
- [qiumingdll_net_host_start](qiumingdll_net_host_start.md)
- [qiumingdll_net_poll_json](qiumingdll_net_poll_json.md)
