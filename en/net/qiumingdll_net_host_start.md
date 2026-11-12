# qiumingdll_net_host_start()

Start a TCP listener as host, waiting for other players to join the room as clients.

## Signature

```gml
qiumingdll_net_host_start(bind_ip, port, max_players)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| bind_ip | string | yes | Listen address. `"0.0.0.0"` means all network adapters (use this for LAN play); `"127.0.0.1"` is local machine only; a specific IPv4 address is also accepted |
| port | real | yes | Listen port (1~65535) |
| max_players | real | yes | Total room capacity, **including the host itself**; values below 1 are treated as 1. Client limit = `max_players - 1` |

## Returns

| Value | Description |
|----|------|
| `1` | Started successfully; `qiumingdll_net_get_status()` now returns `1` |
| `0` | Start failed (Winsock unavailable, socket/bind/listen failure, port already in use, etc.) |

## Usage

- Prerequisite: `qiumingdll_init()` must be called first (`external_define` is done during init).
- If a connection already exists (host or client), this function disconnects it automatically before listening.
- This function does not block: accept and heartbeat are handled by background threads, so it can be called directly in the Create event.
- Player ids are assigned incrementally from `1` and are **not reused** after a disconnect; the host itself always has id `0` and is shown in the player list under the name `"host"`.
- When each client joins: it first receives the WELCOME snapshot (current shared variables + all instances, queued as poll events), then the full player list.
- All network events (connect, variables, instances, custom events, disconnect) are consumed uniformly by polling `qiumingdll_net_poll_json()`.
- The same port cannot be listened on by two processes at once; when testing LAN play, remember to allow the port in the firewall.

## Example

```gml
// Create event: open the room as host
if (qiumingdll_net_host_start("0.0.0.0", 25565, 4))
{
    show_debug_message("Room opened, max 3 clients");
}
else
{
    show_debug_message("Failed to open room");
}
```

## Related functions

- [qiumingdll_net_client_connect](qiumingdll_net_client_connect.md)
- [qiumingdll_net_disconnect](qiumingdll_net_disconnect.md)
- [qiumingdll_net_poll_json](qiumingdll_net_poll_json.md)
- [qiumingdll_net_get_status](qiumingdll_net_get_status.md)
- [qiumingdll_net_get_player_count](qiumingdll_net_get_player_count.md)
