# qiumingdll_net_get_players_json()

获取房间内玩家名单（JSON 数组字符串）。

## 函数签名

```gml
qiumingdll_net_get_players_json()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数 |

## 返回值

| 端 | 返回值 |
|----|--------|
| host | `[{"id":0,"name":"host"},{"id":1,"name":"Alice"},...]`（按加入顺序） |
| client | host 广播的名单；名字到达前返回仅含自己的数组 |
| 未连接 | `"[]"` |

> 返回字符串使用内部静态缓冲区，**在下一次调用本函数前有效**；需要跨帧保存请立即 `json_parse` 或复制。

## 使用说明

- host 的名单第一项固定是 host 自身（`id=0`，名字 `"host"`）；client 的名单包含 host 与所有 client。
- 名单在有人加入/离开时由 host 全量广播，client 侧是“最后一份快照”，不是增量。
- 玩家的昵称来自 `client_connect` 的 `player_name`，允许重名；请用 `id` 作为唯一键。
- 掉线检测：client 进程异常退出时，host 约 5 秒心跳超时后才会从名单中移除。
- 昵称经过 JSON 转义，含引号/反斜杠也不会破坏结构。

## 示例

```gml
var _players = json_parse(qiumingdll_net_get_players_json());
for (var i = 0; i < array_length(_players); i++)
{
    var _p = _players[i];
    show_debug_message("Player #" + string(_p.id) + ": " + _p.name);
}

// 找到自己的名字
var _myId = qiumingdll_net_get_player_id();
var _myName = "";
for (var i = 0; i < array_length(_players); i++)
{
    if (_players[i].id == _myId) { _myName = _players[i].name; break; }
}
```

## 相关函数

- [qiumingdll_net_get_player_count](qiumingdll_net_get_player_count.md)
- [qiumingdll_net_get_player_id](qiumingdll_net_get_player_id.md)
- [qiumingdll_net_get_shared_vars_json](qiumingdll_net_get_shared_vars_json.md)
- [qiumingdll_net_poll_json](qiumingdll_net_poll_json.md)
