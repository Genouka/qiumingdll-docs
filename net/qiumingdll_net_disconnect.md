# qiumingdll_net_disconnect()

断开当前连接（host 或 client 均可调用）。

## 函数签名

```gml
qiumingdll_net_disconnect()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| `1` | 断开完成；当前本来就没有连接时也返回 `1`（幂等） |

## 使用说明

- **client 调用**：先向 host 发送 GOODBYE，再关闭连接。host 会收到一条 `kind="disconnect"` 且 `reason="goodbye"` 的事件。
- **host 调用**：先向所有在线 client 广播 GOODBYE（client 侧收到 `reason="goodbye"` 并自动转为未连接状态），然后停止监听并关闭所有连接。
- 本地主动断开**不会**给自己产生 disconnect 事件（避免“自己把自己踢掉”的误判）；只影响对端事件。
- 断开后 `qiumingdll_net_get_status()` 返回 `0`。
- 该函数会等待后台线程退出，正常在几百毫秒内返回；建议在 Cleanup 事件中调用。
- host 断开后，之前分配的玩家 id 不会回收复用。

## 示例

```gml
// Cleanup 事件
qiumingdll_net_disconnect();

// 或：玩家点击“退出房间”按钮
if (qiumingdll_net_disconnect() == 1)
{
    room_goto(rm_menu);
}
```

## 相关函数

- [qiumingdll_net_host_start](qiumingdll_net_host_start.md)
- [qiumingdll_net_client_connect](qiumingdll_net_client_connect.md)
- [qiumingdll_net_get_status](qiumingdll_net_get_status.md)
- [qiumingdll_net_poll_json](qiumingdll_net_poll_json.md)
