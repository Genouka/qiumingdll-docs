# qiumingdll_net_host_start()

以 host（主机）身份启动 TCP 监听，等待其他玩家以 client 身份加入房间。

## 函数签名

```gml
qiumingdll_net_host_start(bind_ip, port, max_players)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| bind_ip | string | 是 | 监听地址。`"0.0.0.0"` 表示所有网卡（局域网联机用这个）；`"127.0.0.1"` 仅本机；也接受具体 IPv4 地址 |
| port | real | 是 | 监听端口（1~65535） |
| max_players | real | 是 | 房间总人数上限，**含 host 自身**；小于 1 时按 1 处理。client 上限 = `max_players - 1` |

## 返回值

| 值 | 说明 |
|----|------|
| `1` | 启动成功，此时 `qiumingdll_net_get_status()` 返回 `1` |
| `0` | 启动失败（Winsock 不可用、socket/bind/listen 失败、端口被占用等） |

## 使用说明

- 前置条件：需先调用 `qiumingdll_init()`（`external_define` 在 init 中完成）。
- 若当前已有连接（host 或 client），本函数会先自动断开，再进入监听。
- 本函数不阻塞：accept 与心跳由后台线程处理，创建事件里直接调用即可。
- 玩家 id 从 `1` 开始递增分配，断开后**不复用**；host 自身 id 恒为 `0`，在玩家名单中显示名为 `"host"`。
- 每个 client 加入时：先收到 WELCOME 快照（当前共享变量 + 全部实例，以 poll 事件形式入队），随后收到全量玩家名单。
- 所有网络事件（连接、变量、实例、自定义事件、掉线）统一通过 `qiumingdll_net_poll_json()` 轮询消费。
- 同一端口不能同时被两个进程监听；测试局域网联机时记得在防火墙放行该端口。

## 示例

```gml
// Create 事件：作为主机开启房间
if (qiumingdll_net_host_start("0.0.0.0", 25565, 4))
{
    show_debug_message("Room opened, max 3 clients");
}
else
{
    show_debug_message("Failed to open room");
}
```

## 相关函数

- [qiumingdll_net_client_connect](qiumingdll_net_client_connect.md)
- [qiumingdll_net_disconnect](qiumingdll_net_disconnect.md)
- [qiumingdll_net_poll_json](qiumingdll_net_poll_json.md)
- [qiumingdll_net_get_status](qiumingdll_net_get_status.md)
- [qiumingdll_net_get_player_count](qiumingdll_net_get_player_count.md)
