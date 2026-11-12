# qiumingdll_net_disconnect()

Disconnects the current connection (can be called by either host or client).

## Signature

```gml
qiumingdll_net_disconnect()
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|-------|-------------|
| `1` | Disconnection complete; also returns `1` when there was no connection at all (idempotent) |

## Usage

- **Called by a client**: sends GOODBYE to the host first, then closes the connection. The host receives an event with `kind="disconnect"` and `reason="goodbye"`.
- **Called by the host**: first broadcasts GOODBYE to every online client (clients receive `reason="goodbye"` and automatically switch to the disconnected state), then stops listening and closes all connections.
- An intentional local disconnect does **not** generate a disconnect event for the caller itself (avoiding a false "I kicked myself" reading); it only affects the peer's events.
- After disconnecting, `qiumingdll_net_get_status()` returns `0`.
- The function waits for the background thread to exit and normally returns within a few hundred milliseconds; calling it from the Cleanup event is recommended.
- After the host disconnects, previously assigned player ids are not recycled or reused.

## Example

```gml
// Cleanup event
qiumingdll_net_disconnect();

// Or: the player clicks the "leave room" button
if (qiumingdll_net_disconnect() == 1)
{
    room_goto(rm_menu);
}
```

## Related functions

- [qiumingdll_net_host_start](qiumingdll_net_host_start.md)
- [qiumingdll_net_client_connect](qiumingdll_net_client_connect.md)
- [qiumingdll_net_get_status](qiumingdll_net_get_status.md)
- [qiumingdll_net_poll_json](qiumingdll_net_poll_json.md)
