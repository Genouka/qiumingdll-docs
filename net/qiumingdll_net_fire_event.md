# qiumingdll_net_fire_event()

发起一个命名自定义事件，广播或定向发送给房间内其他端。

## 函数签名

```gml
qiumingdll_net_fire_event(name, payload_json, target_id)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| name | string | 是 | 事件名，自定义，例如 `"explosion"`、`"chat"` |
| payload_json | string | 是 | 事件负载的 **JSON 字面量**，例如 `"{\"x\":10,\"dmg\":5}"`；无负载可传 `"{}"` |
| target_id | real | 是 | `0` = 广播给所有 client；非 0 = 定向发送给该 playerId |

## 返回值

| 值 | 说明 |
|----|------|
| host：`1` | 广播成功，或定向目标在线且已投递 |
| host：`0` | 定向目标不在线 / 发送失败；未连接 |
| client：`1` | 请求已交给 host（host 负责路由）；未连接返回 `0` |

## 使用说明

- **host 侧**：`target_id = 0` 时广播给所有 client；`target_id != 0` 时只投递给该 peer。两种情况 host 都会给自己入队一条事件（`peer=0`），便于本地统一记录；host 自身不作为定向目标（id 0 已被约定为“广播”）。
- **client 侧**：无论广播还是定向，都先发给 host 由 host 路由：
  - `target_id = 0` → host 广播给所有 client（发起者也会收到这条广播，即“回环”）；
  - `target_id = N` → 只发给玩家 N（若 N 就是自己，会回到自己）；
  - 发送成功即返回 `1`，目标是否在线由 host 判断（host 一定会在自己的 poll 中看到该事件，`peer` 为发起者 id）。
- 事件是“即发即忘”的：不排队重发、不保证顺序之外的可靠性（TCP 本身有序，但重连后不会补发）。
- 负载请传合法 JSON。

## 示例

```gml
// host：广播爆炸事件
qiumingdll_net_fire_event("explosion", "{\"x\":320,\"y\":180,\"dmg\":5}", 0);

// host：只通知玩家 2
qiumingdll_net_fire_event("privateTip", "{\"text\":\"You are the traitor\"}", 2);

// client：上报聊天，广播给所有人
qiumingdll_net_fire_event("chat", "{\"text\":\"gg\"}", 0);

// 接收端
var _events = json_parse(qiumingdll_net_poll_json());
for (var i = 0; i < array_length(_events); i++)
{
    var _e = _events[i];
    if (_e.kind == "event" && _e.name == "explosion")
    {
        net_play_explosion(_e.payload.x, _e.payload.y);
    }
}
```

## 相关函数

- [qiumingdll_net_poll_json](qiumingdll_net_poll_json.md)
- [qiumingdll_net_get_players_json](qiumingdll_net_get_players_json.md)
- [qiumingdll_net_instance_create](qiumingdll_net_instance_create.md)
