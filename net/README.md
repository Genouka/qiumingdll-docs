# net 模块

TCP 联机（一主多从）：一个 host 监听，多个 client 加入。提供共享变量同步、共享实例（host 仲裁）、自定义事件传播、掉线通知与玩家名单。所有网络事件统一通过 `poll_json` 轮询消费。

共 15 个函数。

## 函数索引

### 连接管理

| 函数 | 说明 |
|------|------|
| [qiumingdll_net_host_start](qiumingdll_net_host_start.md) | 以 host 身份启动 TCP 监听，`maxPlayers` 含 host 自身。 |
| [qiumingdll_net_client_connect](qiumingdll_net_client_connect.md) | 以 client 身份连接 host（同步阻塞，最多约 5 秒），成功返回 playerId。 |
| [qiumingdll_net_disconnect](qiumingdll_net_disconnect.md) | 断开当前连接（host / client 均可）。 |

### 共享变量（host 权威）

| 函数 | 说明 |
|------|------|
| [qiumingdll_net_register_shared_var](qiumingdll_net_register_shared_var.md) | host 声明需要同步的变量名。 |
| [qiumingdll_net_set_shared_var](qiumingdll_net_set_shared_var.md) | host 设置变量值（JSON 字面量）并立即广播。 |

### 共享实例（host 仲裁）

| 函数 | 说明 |
|------|------|
| [qiumingdll_net_instance_create](qiumingdll_net_instance_create.md) | 创建实例；host 返回新 id，client 返回 1（异步，id 从事件取）。 |
| [qiumingdll_net_instance_update](qiumingdll_net_instance_update.md) | 更新实例状态（整体替换，最后写入胜出）。 |
| [qiumingdll_net_instance_destroy](qiumingdll_net_instance_destroy.md) | 销毁实例并广播（事件 `state` 为 `null`）。 |

### 事件与查询

| 函数 | 说明 |
|------|------|
| [qiumingdll_net_fire_event](qiumingdll_net_fire_event.md) | 发起命名事件，`targetId=0` 广播，非 0 定向。 |
| [qiumingdll_net_poll_json](qiumingdll_net_poll_json.md) | 取出并清空事件队列，返回 JSON 数组（唯一事件出口）。 |
| [qiumingdll_net_get_status](qiumingdll_net_get_status.md) | 0=未连接，1=host 监听中，2=client 已连接。 |
| [qiumingdll_net_get_player_id](qiumingdll_net_get_player_id.md) | 本机 playerId（host=0，client>0，未连接=0）。 |
| [qiumingdll_net_get_player_count](qiumingdll_net_get_player_count.md) | 房间人数（host 含自身；client 来自名单广播）。 |
| [qiumingdll_net_get_players_json](qiumingdll_net_get_players_json.md) | 玩家名单 `[{"id":N,"name":"..."},...]`。 |
| [qiumingdll_net_get_shared_vars_json](qiumingdll_net_get_shared_vars_json.md) | 共享变量快照 `[{"name":"...","value":...},...]`。 |

## 典型用法

host：

```gml
// Create 事件
qiumingdll_net_host_start("0.0.0.0", 25565, 4);
qiumingdll_net_register_shared_var("score");
qiumingdll_net_set_shared_var("score", "0");

// Step 事件
var _events = json_parse(qiumingdll_net_poll_json());
// …分发 connect / disconnect / var / instance / event…

// 状态变化时
qiumingdll_net_set_shared_var("score", string(global.score));
```

client：

```gml
// Create 事件
global.myId = qiumingdll_net_client_connect("192.168.1.10", 25565, "Alice");

// Step 事件
var _events = json_parse(qiumingdll_net_poll_json());
// …分发事件…

// Cleanup 事件
qiumingdll_net_disconnect();
```

## 协议与限制

- 帧格式：`[magic:4B="QMn1"][type:1B][payloadLen:4B 网络序][payload]`，单帧负载上限 1 MiB。
- host 为权威端：共享变量只能由 host 写；实例 id 由 host 分配（从 1 开始，不复用），更新采用“最后写入胜出”。
- 心跳：client 每 2 秒发送一次，host 5 秒未收到即判定 `timeout`；`disconnect` 事件的 `reason` 为 `goodbye` / `closed` / `timeout` / `error`。
- 所有字符串返回值使用内部静态缓冲区，下一次调用前有效。
- 仅 Windows 平台有效；非 Windows 下所有函数返回 `0` / 空字符串 / `"[]"`。

## 平台限制

全部函数仅 Windows 有效。

[返回文档首页](../README.md)
