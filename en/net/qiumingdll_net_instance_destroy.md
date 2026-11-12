# qiumingdll_net_instance_destroy()

Destroy a shared instance and synchronize it to every peer in the room.

## Signature

```gml
qiumingdll_net_instance_destroy(id)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| id | real | yes | Id of the instance to destroy |

## Returns

| Value | Description |
|----|------|
| host: `1` | The instance existed, was deleted and broadcast |
| host: `0` | The instance does not exist (destroyed twice or never created), nothing was broadcast |
| client: `1` | Request sent to the host (asynchronous) |
| client: `0` | Send failed or not connected |

## Usage

- The host deletes the instance from its instance table, broadcasts, and queues an `op="destroy"` event for itself (`peer=0`).
- The `state` field of a destroy event is always `null`, and `type` is the instance's original type, so receivers can distinguish the kind without a lookup.
- Instance ids are never reassigned after destruction.
- Repeated destruction is safe: the host returns `0` the second time and no duplicate event is produced.
- When a player leaves the room, instances they created but did not destroy are **not cleaned up automatically**; if you want "monsters vanish with their owner", destroy them on the host after receiving that peer's disconnect event (record an owner on the instance, or keep your own mapping).

## Example

```gml
var _events = json_parse(qiumingdll_net_poll_json());
for (var i = 0; i < array_length(_events); i++)
{
    var _e = _events[i];
    if (_e.kind == "instance" && _e.op == "destroy")
    {
        var _inst = net_find_instance(_e.id);
        if (_inst != noone) instance_destroy(_inst);
    }
}

// Local destroy (callable by both host and client)
if (qiumingdll_net_instance_destroy(_inst.netId))
{
    instance_destroy(_inst);  // Also clear locally right away; if a duplicate destroy event arrives, it is ignored because the id is not found
}
```

## Related functions

- [qiumingdll_net_instance_create](qiumingdll_net_instance_create.md)
- [qiumingdll_net_instance_update](qiumingdll_net_instance_update.md)
- [qiumingdll_net_poll_json](qiumingdll_net_poll_json.md)
