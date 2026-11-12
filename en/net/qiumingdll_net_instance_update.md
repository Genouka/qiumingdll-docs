# qiumingdll_net_instance_update()

Update the state of a shared instance (whole-state replacement) and synchronize it to every peer in the room.

## Signature

```gml
qiumingdll_net_instance_update(id, state_json)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| id | real | yes | Target instance id (the id assigned by the host, or the `id` from a poll event) |
| state_json | string | yes | New state as a **JSON literal**, e.g. `"{\"x\":120,\"y\":64}"` |

## Returns

| Value | Description |
|----|------|
| host: `1` | The instance exists, was updated and broadcast |
| host: `0` | The instance does not exist (possibly already destroyed), nothing was broadcast |
| client: `1` | Request sent to the host (asynchronous); the host broadcasts an update event once it accepts |
| client: `0` | Send failed or not connected |

## Usage

- The state is **replaced as a whole**, not merged field by field: the `state_json` from this call is the instance's new state, and any field not included is regarded as absent. Assemble the complete state locally if you need merging.
- Uses a "last write wins" policy, with no conflict detection or frame synchronization; for high-frequency updates (e.g. coordinates every frame), reduce the send rate (for example once every 2~4 frames) or interpolate yourself.
- After updating, the host queues an `op="update"` event for itself (`peer=0`), and every client receives the same broadcast.
- Updating a non-existent id: the host returns `0`; the client still returns `1` (because the send succeeded), so rely on whether an update event actually arrives.
- The received `state` is `null` in destroy events and a JSON object in all other events.

## Example

```gml
// host: authoritative update of an instance position
qiumingdll_net_instance_update(_inst.netId, "{\"x\":" + string(_inst.x) + ",\"y\":" + string(_inst.y) + "}");

// client: report its own input/position (the host decides whether to accept)
qiumingdll_net_instance_update(myNetId, "{\"inputX\":1,\"inputY\":0}");

// Receiving end
var _events = json_parse(qiumingdll_net_poll_json());
for (var i = 0; i < array_length(_events); i++)
{
    var _e = _events[i];
    if (_e.kind == "instance" && _e.op == "update")
    {
        var _inst = net_find_instance(_e.id);
        if (_inst != noone) net_apply_state(_inst, _e.state);
    }
}
```

## Related functions

- [qiumingdll_net_instance_create](qiumingdll_net_instance_create.md)
- [qiumingdll_net_instance_destroy](qiumingdll_net_instance_destroy.md)
- [qiumingdll_net_poll_json](qiumingdll_net_poll_json.md)
