# qiumingdll_net_get_player_id()

Returns this machine's playerId in the room.

## Signature

```gml
qiumingdll_net_get_player_id()
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|-------|-------------|
| `0` | This machine is the host; or it is not connected |
| `> 0` | The client's player id (assigned by the host) |

## Usage

- The host's id is always `0`; this is part of the protocol (`target_id=0` means broadcast, so the host is never a targeted recipient).
- A client's id is valid immediately after connecting; when the remote side drops, the state resets and this function returns `0` until it reconnects.
- The id is stable for the lifetime of the connection; reconnecting assigns a new id (old ids are never reused).
- To decide "am I host or client", use `get_status()`, not `get_player_id() == 0` (which is also 0 when not connected).

## Example

```gml
var _pid = qiumingdll_net_get_player_id();
var _is_host = (qiumingdll_net_get_status() == 1);

if (!_is_host && _pid > 0)
{
    draw_text(16, 32, "You are player #" + string(_pid));
}
```

## Related functions

- [qiumingdll_net_get_status](qiumingdll_net_get_status.md)
- [qiumingdll_net_get_players_json](qiumingdll_net_get_players_json.md)
- [qiumingdll_net_client_connect](qiumingdll_net_client_connect.md)
