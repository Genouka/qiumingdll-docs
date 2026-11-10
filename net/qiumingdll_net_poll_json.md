# qiumingdll_net_poll_json()

取出并清空事件队列，返回 JSON 数组字符串。这是联机模块**唯一的事件出口**。

## 函数签名

```gml
qiumingdll_net_poll_json()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| JSON 数组字符串 | 自上次调用以来累积的全部事件；无事件时为 `"[]"` |

> 返回字符串使用内部静态缓冲区，**在下一次调用 `poll_json` 前有效**。需要跨帧保存时请立即 `json_parse` 或复制。

## 事件类型

| kind | 字段 | 出现时机 |
|------|------|----------|
| `var` | `name`(string), `value`(任意 JSON), `peer`(number) | 共享变量变更；`peer=0` 表示由 host 设置 |
| `instance` | `id`(number), `type`(string), `state`(JSON 或 `null`), `op`(`"create"`/`"update"`/`"destroy"`) | 实例创建/更新/销毁；`destroy` 的 `state` 为 `null` |
| `event` | `name`(string), `payload`(JSON), `target`(number), `peer`(number) | 自定义事件；`target=0` 表示广播，`peer` 为发起者 id（host 发起的为 0） |
| `connect` | `peer`(number), `name`(string) | 有 client 加入（仅 host 产生） |
| `disconnect` | `peer`(number), `name`(string), `reason`(string) | 掉线。`reason` 取值：`"goodbye"`（对方主动断开）、`"closed"`（连接被关闭/进程退出）、`"timeout"`（心跳超时，约 5 秒）、`"error"`（网络错误） |

## 使用说明

- 建议每帧（Step 事件）调用一次并立即处理，避免队列堆积。
- 调用即清空：**不要在多处重复调用**，否则后调用者拿不到前面的事件。推荐统一在一处轮询后分发。
- 事件顺序与到达顺序一致（TCP 有序）。
- host 自己发起的实例与自定义事件、以及自己设置的共享变量也会入队（`peer=0`），因此两端可以共用同一套消费逻辑。
- 本地主动调用 `qiumingdll_net_disconnect()` 不会给自己产生 `disconnect` 事件。

## 示例

```gml
// Step 事件：统一分发
var _events = json_parse(qiumingdll_net_poll_json());

for (var i = 0; i < array_length(_events); i++)
{
    var _e = _events[i];
    switch (_e.kind)
    {
        case "connect":
            show_debug_message("Player joined: " + _e.name + " (id " + string(_e.peer) + ")");
            break;

        case "disconnect":
            show_debug_message("Player left: " + _e.name + " (" + _e.reason + ")");
            break;

        case "var":
            if (_e.name == "score") global.score = _e.value;
            break;

        case "instance":
            switch (_e.op)
            {
                case "create":  net_spawn(_e.id, _e.type, _e.state); break;
                case "update":  net_apply_state(_e.id, _e.state);    break;
                case "destroy": net_despawn(_e.id);                  break;
            }
            break;

        case "event":
            net_handle_custom(_e.name, _e.payload, _e.peer);
            break;
    }
}
```

## 相关函数

- [qiumingdll_net_get_status](qiumingdll_net_get_status.md)
- [qiumingdll_net_get_players_json](qiumingdll_net_get_players_json.md)
- [qiumingdll_net_get_shared_vars_json](qiumingdll_net_get_shared_vars_json.md)
- [qiumingdll_net_fire_event](qiumingdll_net_fire_event.md)
