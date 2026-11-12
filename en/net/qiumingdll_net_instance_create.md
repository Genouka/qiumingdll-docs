# qiumingdll_net_instance_create()

Create a "shared instance" (synchronized object) and synchronize it to every peer in the room.

## Signature

```gml
qiumingdll_net_instance_create(type, state_json)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| type | string | yes | Instance type name, user-defined, e.g. `"enemy"`, `"bullet"`; used by the receiving end to distinguish object kinds |
| state_json | string | yes | Initial state as a **JSON literal**, e.g. `"{\"x\":10,\"y\":20}"` |

## Returns

| Value | Description |
|----|------|
| host: `> 0` | New instance id (increments from 1, **not reused** after disconnect/destroy) |
| client: `1` | Request sent (**asynchronous**): the real id must be taken from the `op="create"` event of `poll_json()` |
| `0` | Failure: not connected, or send failed |

## Usage

- Instances are arbitrated by the host: a client's create request is first sent to the host, which allocates the id uniformly and broadcasts to **all** peers (including the originator).
- Therefore clients must not use the return value as an id; integrate as follows:
  1. Call `instance_create` and remember that "I initiated a create";
  2. On the next frame, take the event from `poll_json()` with `kind="instance"`, `op="create"` and matching type/state, and use its `id` as the real object id.
- When the host calls it, besides broadcasting, the same create event is queued for itself (`peer=0`), consumed exactly like on a client.
- When a new client joins, the WELCOME snapshot queues one `op="create"` event for every existing instance, so "sync on join" needs no extra code.
- Instances are not destroyed automatically; when leaving the room or changing scenes, call `instance_destroy` yourself or let the host clean them up centrally.

## Example

```gml
// Step event: handle instance creation events
var _events = json_parse(qiumingdll_net_poll_json());
for (var i = 0; i < array_length(_events); i++)
{
    var _e = _events[i];
    if (_e.kind == "instance" && _e.op == "create")
    {
        var _obj = instance_create_depth(_e.state.x, _e.state.y, 0, obj_remote_actor);
        _obj.netId = _e.id;
        _obj.netType = _e.type;
    }
}

// Local creation (callable by both host and client)
qiumingdll_net_instance_create("enemy", "{\"x\":100,\"y\":64}");
```

## Related functions

- [qiumingdll_net_instance_update](qiumingdll_net_instance_update.md)
- [qiumingdll_net_instance_destroy](qiumingdll_net_instance_destroy.md)
- [qiumingdll_net_poll_json](qiumingdll_net_poll_json.md)
- [qiumingdll_net_fire_event](qiumingdll_net_fire_event.md)
