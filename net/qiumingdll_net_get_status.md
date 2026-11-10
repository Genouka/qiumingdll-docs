# qiumingdll_net_get_status()

查询当前联机状态。

## 函数签名

```gml
qiumingdll_net_get_status()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| `0` | 未连接（未启动监听，也未作为 client 连上） |
| `1` | host：已在监听 |
| `2` | client：已连接 host |

## 使用说明

- 该值由 host/client 的后台线程在断线时自动回写为 `0`，可放心用于 UI 显示与逻辑判断。
- 远程掉线（对端关闭、心跳超时）后，状态会自行归零；但建议仍以 `poll_json` 的 `disconnect` 事件作为“玩家离开”的业务触发点。
- 未调用 `qiumingdll_init()` 之前调用本函数没有意义（DLL 未加载）。

## 示例

```gml
switch (qiumingdll_net_get_status())
{
    case 0: draw_text(16, 16, "Offline");            break;
    case 1: draw_text(16, 16, "Hosting");            break;
    case 2: draw_text(16, 16, "Connected as client"); break;
}
```

## 相关函数

- [qiumingdll_net_host_start](qiumingdll_net_host_start.md)
- [qiumingdll_net_client_connect](qiumingdll_net_client_connect.md)
- [qiumingdll_net_disconnect](qiumingdll_net_disconnect.md)
- [qiumingdll_net_get_player_id](qiumingdll_net_get_player_id.md)
