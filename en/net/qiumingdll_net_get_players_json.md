# qiumingdll_net_get_players_json()

Returns the player roster of the room (as a JSON array string).

## Signature

```gml
qiumingdll_net_get_players_json()
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| (none) | - | - | This function takes no parameters |

## Returns

| Side | Return value |
|------|--------------|
| host | `[{"id":0,"name":"host"},{"id":1,"name":"Alice"},...]` (in join order) |
| client | The roster broadcast by the host; before it arrives, an array containing only yourself |
| not connected | `"[]"` |

> The returned string uses an internal static buffer and is **valid until the next call to this function**; to keep it across frames, `json_parse` or copy it immediately.

## Usage

- The host's roster always starts with the host itself (`id=0`, name `"host"`); a client's roster contains the host and every client.
- The host broadcasts the full roster whenever someone joins or leaves; on the client side it is the "last snapshot", not an incremental update.
- Player nicknames come from `player_name` in `client_connect` and duplicates are allowed; use `id` as the unique key.
- Disconnect detection: when a client process exits abnormally, the host only removes it from the roster after its heartbeat times out (about 5 seconds).
- Nicknames are JSON-escaped, so quotes or backslashes do not break the structure.

## Example

```gml
var _players = json_parse(qiumingdll_net_get_players_json());
for (var i = 0; i < array_length(_players); i++)
{
    var _p = _players[i];
    show_debug_message("Player #" + string(_p.id) + ": " + _p.name);
}

// Find your own name
var _myId = qiumingdll_net_get_player_id();
var _myName = "";
for (var i = 0; i < array_length(_players); i++)
{
    if (_players[i].id == _myId) { _myName = _players[i].name; break; }
}
```

## Related functions

- [qiumingdll_net_get_player_count](qiumingdll_net_get_player_count.md)
- [qiumingdll_net_get_player_id](qiumingdll_net_get_player_id.md)
- [qiumingdll_net_get_shared_vars_json](qiumingdll_net_get_shared_vars_json.md)
- [qiumingdll_net_poll_json](qiumingdll_net_poll_json.md)
