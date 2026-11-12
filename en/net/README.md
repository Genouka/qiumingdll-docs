# net module

TCP multiplayer (one host, multiple clients): a single host listens and multiple clients join. Provides shared variable sync, shared instances (host arbitration), custom event propagation, disconnect notifications and a player roster. All network events are consumed uniformly by polling `poll_json`.

15 functions in total.

## Function index

### Connection management

| Function | Description |
|----------|-------------|
| [qiumingdll_net_host_start](qiumingdll_net_host_start.md) | Starts TCP listening as host; `maxPlayers` includes the host itself. |
| [qiumingdll_net_client_connect](qiumingdll_net_client_connect.md) | Connects to the host as a client (synchronous and blocking, about 5 seconds max); returns the playerId on success. |
| [qiumingdll_net_disconnect](qiumingdll_net_disconnect.md) | Disconnects the current connection (works for both host and client). |

### Shared variables (host authoritative)

| Function | Description |
|----------|-------------|
| [qiumingdll_net_register_shared_var](qiumingdll_net_register_shared_var.md) | The host declares a variable name that needs to be synchronized. |
| [qiumingdll_net_set_shared_var](qiumingdll_net_set_shared_var.md) | The host sets a variable value (JSON literal) and broadcasts it immediately. |

### Shared instances (host arbitration)

| Function | Description |
|----------|-------------|
| [qiumingdll_net_instance_create](qiumingdll_net_instance_create.md) | Creates an instance; the host returns the new id, a client returns 1 (asynchronous; take the id from the event). |
| [qiumingdll_net_instance_update](qiumingdll_net_instance_update.md) | Updates instance state (whole-state replacement, last write wins). |
| [qiumingdll_net_instance_destroy](qiumingdll_net_instance_destroy.md) | Destroys an instance and broadcasts it (the event `state` is `null`). |

### Events and queries

| Function | Description |
|----------|-------------|
| [qiumingdll_net_fire_event](qiumingdll_net_fire_event.md) | Fires a named event; `targetId=0` broadcasts, any other value targets a single player. |
| [qiumingdll_net_poll_json](qiumingdll_net_poll_json.md) | Drains the event queue and returns a JSON array (the only event outlet). |
| [qiumingdll_net_get_status](qiumingdll_net_get_status.md) | 0 = not connected, 1 = host listening, 2 = client connected. |
| [qiumingdll_net_get_player_id](qiumingdll_net_get_player_id.md) | This machine's playerId (host = 0, client > 0, not connected = 0). |
| [qiumingdll_net_get_player_count](qiumingdll_net_get_player_count.md) | Number of players in the room (the host's count includes itself; a client's count comes from the roster broadcast). |
| [qiumingdll_net_get_players_json](qiumingdll_net_get_players_json.md) | Player roster `[{"id":N,"name":"..."},...]`. |
| [qiumingdll_net_get_shared_vars_json](qiumingdll_net_get_shared_vars_json.md) | Shared variable snapshot `[{"name":"...","value":...},...]`. |

## Typical usage

host:

```gml
// Create event
qiumingdll_net_host_start("0.0.0.0", 25565, 4);
qiumingdll_net_register_shared_var("score");
qiumingdll_net_set_shared_var("score", "0");

// Step event
var _events = json_parse(qiumingdll_net_poll_json());
// …dispatch connect / disconnect / var / instance / event…

// When the state changes
qiumingdll_net_set_shared_var("score", string(global.score));
```

client:

```gml
// Create event
global.myId = qiumingdll_net_client_connect("192.168.1.10", 25565, "Alice");

// Step event
var _events = json_parse(qiumingdll_net_poll_json());
// …dispatch events…

// Cleanup event
qiumingdll_net_disconnect();
```

## Protocol and limits

- Frame format: `[magic:4B="QMn1"][type:1B][payloadLen:4B network order][payload]`; a single frame payload is capped at 1 MiB.
- The host is authoritative: shared variables can only be written by the host; instance ids are allocated by the host (starting at 1, never reused), and updates use "last write wins".
- Heartbeat: a client sends one every 2 seconds; the host declares `timeout` after 5 seconds without one. The `reason` of a `disconnect` event is `goodbye` / `closed` / `timeout` / `error`.
- All string return values use an internal static buffer and are valid until the next call.
- Windows only; on non-Windows platforms every function returns `0` / an empty string / `"[]"`.

## Platform limits

All functions are Windows-only.

[Back to documentation home](../README.md)
