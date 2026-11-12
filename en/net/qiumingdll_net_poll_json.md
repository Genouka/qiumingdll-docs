# qiumingdll_net_poll_json()

Dequeue and clear the event queue, returning a JSON array string. This is the networking module's **only event outlet**.

## Signature

```gml
qiumingdll_net_poll_json()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| JSON array string | All events accumulated since the previous call; `"[]"` when there are none |

> The returned string uses an internal static buffer and is **valid only until the next `poll_json` call**. If you need it across frames, `json_parse` or copy it immediately.

## Event types

| kind | Fields | When it appears |
|------|------|----------|
| `var` | `name`(string), `value`(any JSON), `peer`(number) | Shared variable changed; `peer=0` means it was set by the host |
| `instance` | `id`(number), `type`(string), `state`(JSON or `null`), `op`(`"create"`/`"update"`/`"destroy"`) | Instance created/updated/destroyed; `state` is `null` for `destroy` |
| `event` | `name`(string), `payload`(JSON), `target`(number), `peer`(number) | Custom event; `target=0` means broadcast, `peer` is the originator id (0 when sent by the host) |
| `connect` | `peer`(number), `name`(string) | A client joined (only produced on the host) |
| `disconnect` | `peer`(number), `name`(string), `reason`(string) | Disconnect. `reason` values: `"goodbye"` (the other side disconnected voluntarily), `"closed"` (connection closed/process exited), `"timeout"` (heartbeat timeout, about 5 seconds), `"error"` (network error) |

## Usage

- Call it once per frame (Step event) and process the result immediately to avoid queue buildup.
- Calling it clears the queue: **do not call it from several places**, otherwise later callers miss earlier events. Poll in one place and dispatch from there.
- Event order matches arrival order (TCP is ordered).
- Instances and custom events originated by the host, and shared variables set by the host, are also queued (`peer=0`), so both sides can share the same consumption logic.
- Calling `qiumingdll_net_disconnect()` locally does not produce a `disconnect` event for yourself.

## Example

```gml
// Step event: unified dispatch
var _events = json_parse(qiumingdll_net_poll_json());

for (var i = 0; i < array_length(_events); i++)
{
    var _e = _events[i];
    switch (_e.kind)
    {
        case "connect":
            show_debug_message("Player joined: " + _e.name + " (id " + string(_e.peer) + ")");
            break;

        case "disconnect":
            show_debug_message("Player left: " + _e.name + " (" + _e.reason + ")");
            break;

        case "var":
            if (_e.name == "score") global.score = _e.value;
            break;

        case "instance":
            switch (_e.op)
            {
                case "create":  net_spawn(_e.id, _e.type, _e.state); break;
                case "update":  net_apply_state(_e.id, _e.state);    break;
                case "destroy": net_despawn(_e.id);                  break;
            }
            break;

        case "event":
            net_handle_custom(_e.name, _e.payload, _e.peer);
            break;
    }
}
```

## Related functions

- [qiumingdll_net_get_status](qiumingdll_net_get_status.md)
- [qiumingdll_net_get_players_json](qiumingdll_net_get_players_json.md)
- [qiumingdll_net_get_shared_vars_json](qiumingdll_net_get_shared_vars_json.md)
- [qiumingdll_net_fire_event](qiumingdll_net_fire_event.md)
