# qiumingdll_net_get_player_count()

查询房间内的玩家数量。

## 函数签名

```gml
qiumingdll_net_get_player_count()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| host | 当前在线人数，**含 host 自身**（最小为 `1`） |
| client | host 广播的玩家名单人数；名单尚未到达时为 `0` |
| `0` | 未连接 |

## 使用说明

- host 的计数基于“仍在线的 peer”，掉线后立即减少（心跳超时约 5 秒后才判定）。
- client 的数据来自 host 的名单广播（ROSTER）：WELCOME 之后紧接着到达，因此刚连上的第一帧可能还是 `0`，下一帧左右恢复正常。需要精确判断时请以 `get_players_json()` 是否包含自己为准。
- 人数上限由 `host_start` 的 `max_players` 决定（含 host 自身），超出后新连接会被 host 直接关闭。
- 与 `get_players_json()` 的长度保持一致（client 在名单到达前两者分别为 `0` 与“仅自己”，属正常瞬态）。

## 示例

```gml
var _count = qiumingdll_net_get_player_count();
draw_text(16, 48, "Players: " + string(_count));
```

## 相关函数

- [qiumingdll_net_get_players_json](qiumingdll_net_get_players_json.md)
- [qiumingdll_net_get_player_id](qiumingdll_net_get_player_id.md)
- [qiumingdll_net_host_start](qiumingdll_net_host_start.md)
- [qiumingdll_net_poll_json](qiumingdll_net_poll_json.md)
