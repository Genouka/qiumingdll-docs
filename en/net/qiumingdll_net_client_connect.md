# qiumingdll_net_client_connect()

Connects to the host as a client and joins the room.

## Signature

```gml
qiumingdll_net_client_connect(host_ip, port, player_name)
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| host_ip | string | yes | The host's IPv4 address (use `"127.0.0.1"` when testing on the same machine) |
| port | real | yes | The host's listening port (1~65535); must match `host_start` |
| player_name | string | yes | Player nickname, shown in the roster on the host and other clients; may be an empty string |

## Returns

| Value | Description |
|-------|-------------|
| `> 0` | Connected successfully; returns the playerId assigned by the host. `qiumingdll_net_get_status()` now returns `2` |
| `0` | Connection failed or timed out (no WELCOME frame from the host within 5 seconds) |

## Usage

- Precondition: `qiumingdll_init()` must have been called and the host must already be listening.
- **This function is synchronous and blocking**: it waits for the host's WELCOME for up to about 5 seconds. Call it from a loading screen or a dedicated step, not every frame.
- If a connection already exists, it is closed automatically first.
- At the moment the connection succeeds, the host queues its current shared variables and all instances as the WELCOME snapshot, so the first `poll_json` already returns them.
- The roster (ROSTER) follows WELCOME immediately, so right after connecting `get_players_json()` may contain only yourself; the full roster arrives within about a frame.
- Nicknames are not deduplicated and duplicates are allowed; use playerId to tell players apart.

## Example

```gml
// Create event: join the room
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

## Related functions

- [qiumingdll_net_host_start](qiumingdll_net_host_start.md)
- [qiumingdll_net_disconnect](qiumingdll_net_disconnect.md)
- [qiumingdll_net_poll_json](qiumingdll_net_poll_json.md)
- [qiumingdll_net_get_player_id](qiumingdll_net_get_player_id.md)
- [qiumingdll_net_get_status](qiumingdll_net_get_status.md)
