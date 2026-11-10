# qiumingdll_net_get_player_id()

查询本机在房间中的 playerId。

## 函数签名

```gml
qiumingdll_net_get_player_id()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| `0` | 本机是 host；或未连接 |
| `> 0` | client 的玩家 id（host 分配） |

## 使用说明

- host 的 id 固定为 `0`，这是协议约定（`target_id=0` 表示广播，因此 host 不作为定向目标）。
- client 连接成功后 id 立即有效；远程掉线后状态归零，本函数返回 `0`，直到重新连接。
- 该 id 在本次连接内稳定；重连会分配新 id（旧 id 不复用）。
- 判断“我是 host 还是 client”请用 `get_status()`，不要用 `get_player_id() == 0`（未连接时也为 0）。

## 示例

```gml
var _pid = qiumingdll_net_get_player_id();
var _is_host = (qiumingdll_net_get_status() == 1);

if (!_is_host && _pid > 0)
{
    draw_text(16, 32, "You are player #" + string(_pid));
}
```

## 相关函数

- [qiumingdll_net_get_status](qiumingdll_net_get_status.md)
- [qiumingdll_net_get_players_json](qiumingdll_net_get_players_json.md)
- [qiumingdll_net_client_connect](qiumingdll_net_client_connect.md)
