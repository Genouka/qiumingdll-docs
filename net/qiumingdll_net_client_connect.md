# qiumingdll_net_client_connect()

以 client（从机）身份连接 host，加入房间。

## 函数签名

```gml
qiumingdll_net_client_connect(host_ip, port, player_name)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| host_ip | string | 是 | host 的 IPv4 地址（同一台机器测试用 `"127.0.0.1"`） |
| port | real | 是 | host 的监听端口（1~65535），需与 `host_start` 一致 |
| player_name | string | 是 | 玩家昵称，会出现在 host 与其他 client 的玩家名单中；可为空字符串 |

## 返回值

| 值 | 说明 |
|----|------|
| `> 0` | 连接成功，返回 host 分配的 playerId；此时 `qiumingdll_net_get_status()` 返回 `2` |
| `0` | 连接失败或超时（5 秒内未收到 host 的 WELCOME 帧） |

## 使用说明

- 前置条件：需先调用 `qiumingdll_init()`，且 host 已启动监听。
- **本函数是同步阻塞的**：会一直等到 host 返回 WELCOME，最长约 5 秒。建议在 loading 界面或单独的步骤中调用，不要每帧调用。
- 连接前若已有连接，会先自动断开。
- 成功的同一时刻，host 会把当前共享变量与全部实例作为 WELCOME 快照入队，第一次 `poll_json` 即可拿到。
- 玩家名单（ROSTER）紧随 WELCOME 到达，因此刚连上时 `get_players_json()` 可能只包含自己，下一帧左右即可拿到完整名单。
- 昵称不做去重，允许重名；需要区分玩家请用 playerId。

## 示例

```gml
// Create 事件：加入房间
var _pid = qiumingdll_net_client_connect("192.168.1.10", 25565, "Alice");
if (_pid > 0)
{
    show_debug_message("Joined as player " + string(_pid));
}
else
{
    show_debug_message("Connect failed or timed out");
}
```

## 相关函数

- [qiumingdll_net_host_start](qiumingdll_net_host_start.md)
- [qiumingdll_net_disconnect](qiumingdll_net_disconnect.md)
- [qiumingdll_net_poll_json](qiumingdll_net_poll_json.md)
- [qiumingdll_net_get_player_id](qiumingdll_net_get_player_id.md)
- [qiumingdll_net_get_status](qiumingdll_net_get_status.md)
