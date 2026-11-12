# qiumingdll_net_get_status()

Query the current networking status.

## Signature

```gml
qiumingdll_net_get_status()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| `0` | Not connected (neither listening started nor connected as client) |
| `1` | host: listening |
| `2` | client: connected to host |

## Usage

- The host/client background thread automatically writes this value back to `0` on disconnect, so it is safe to use for UI display and logic checks.
- After a remote disconnect (peer closed, heartbeat timeout) the status resets to zero by itself; it is still recommended to treat the `disconnect` event from `poll_json` as the business trigger for "player left".
- Calling this function before `qiumingdll_init()` is meaningless (the DLL is not loaded).

## Example

```gml
switch (qiumingdll_net_get_status())
{
    case 0: draw_text(16, 16, "Offline");            break;
    case 1: draw_text(16, 16, "Hosting");            break;
    case 2: draw_text(16, 16, "Connected as client"); break;
}
```

## Related functions

- [qiumingdll_net_host_start](qiumingdll_net_host_start.md)
- [qiumingdll_net_client_connect](qiumingdll_net_client_connect.md)
- [qiumingdll_net_disconnect](qiumingdll_net_disconnect.md)
- [qiumingdll_net_get_player_id](qiumingdll_net_get_player_id.md)
