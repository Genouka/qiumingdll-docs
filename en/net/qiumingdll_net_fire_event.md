# qiumingdll_net_fire_event()

Fires a named custom event, either broadcast to the room or sent to a specific peer.

## Signature

```gml
qiumingdll_net_fire_event(name, payload_json, target_id)
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| name | string | yes | Event name, user-defined, e.g. `"explosion"`, `"chat"` |
| payload_json | string | yes | The event payload as a **JSON literal**, e.g. `"{\"x\":10,\"dmg\":5}"`; pass `"{}"` when there is no payload |
| target_id | real | yes | `0` = broadcast to all clients; non-zero = send only to that playerId |

## Returns

| Value | Description |
|-------|-------------|
| host: `1` | Broadcast succeeded, or the targeted player is online and the event was delivered |
| host: `0` | The targeted player is offline / sending failed; or not connected |
| client: `1` | The request was handed to the host (the host does the routing); returns `0` when not connected |

## Usage

- **Host side**: with `target_id = 0` the event is broadcast to all clients; with `target_id != 0` it is delivered only to that peer. In both cases the host also queues the event for itself (`peer=0`) for uniform local bookkeeping; the host itself cannot be a targeted recipient (id 0 is reserved for "broadcast").
- **Client side**: whether broadcasting or targeting, the event is sent to the host first and the host routes it:
  - `target_id = 0` → the host broadcasts to all clients (the sender also receives this broadcast, i.e. a loopback);
  - `target_id = N` → sent only to player N (if N is yourself, it comes back to you);
  - returns `1` as soon as the send succeeds; whether the target is online is decided by the host (the host always sees the event in its own poll with `peer` set to the sender's id).
- Events are fire-and-forget: no queued retries and no reliability guarantee beyond ordering (TCP is ordered, but nothing is replayed after a reconnect).
- Pass valid JSON as the payload.

## Example

```gml
// host: broadcast an explosion event
qiumingdll_net_fire_event("explosion", "{\"x\":320,\"y\":180,\"dmg\":5}", 0);

// host: notify only player 2
qiumingdll_net_fire_event("privateTip", "{\"text\":\"You are the traitor\"}", 2);

// client: report chat, broadcast to everyone
qiumingdll_net_fire_event("chat", "{\"text\":\"gg\"}", 0);

// receiving end
var _events = json_parse(qiumingdll_net_poll_json());
for (var i = 0; i < array_length(_events); i++)
{
    var _e = _events[i];
    if (_e.kind == "event" && _e.name == "explosion")
    {
        net_play_explosion(_e.payload.x, _e.payload.y);
    }
}
```

## Related functions

- [qiumingdll_net_poll_json](qiumingdll_net_poll_json.md)
- [qiumingdll_net_get_players_json](qiumingdll_net_get_players_json.md)
- [qiumingdll_net_instance_create](qiumingdll_net_instance_create.md)
