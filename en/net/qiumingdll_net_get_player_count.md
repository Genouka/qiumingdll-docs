# qiumingdll_net_get_player_count()

Returns the number of players in the room.

## Signature

```gml
qiumingdll_net_get_player_count()
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|-------|-------------|
| host | Current online player count, **including the host itself** (minimum `1`) |
| client | The player count from the roster broadcast by the host; `0` until the roster arrives |
| `0` | Not connected |

## Usage

- The host's count is based on peers that are still online, so it drops as soon as a peer disconnects (only after the heartbeat times out, about 5 seconds).
- A client's data comes from the host's roster broadcast (ROSTER): it arrives right after WELCOME, so the first frame after connecting may still be `0` and it recovers within about a frame. When you need an exact answer, check whether `get_players_json()` contains yourself.
- The player cap is set by `max_players` in `host_start` (including the host itself); new connections beyond it are closed by the host immediately.
- It stays consistent with the length of `get_players_json()` (before the roster arrives a client reports `0` here and "only yourself" there, which is a normal transient state).

## Example

```gml
var _count = qiumingdll_net_get_player_count();
draw_text(16, 48, "Players: " + string(_count));
```

## Related functions

- [qiumingdll_net_get_players_json](qiumingdll_net_get_players_json.md)
- [qiumingdll_net_get_player_id](qiumingdll_net_get_player_id.md)
- [qiumingdll_net_host_start](qiumingdll_net_host_start.md)
- [qiumingdll_net_poll_json](qiumingdll_net_poll_json.md)
