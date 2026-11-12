# qiumingdll_net_register_shared_var()

The host declares the name of a shared variable that must be synchronized to all clients.

## Signature

```gml
qiumingdll_net_register_shared_var(name)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| name | string | yes | Variable name (case-sensitive), e.g. `"score"`, `"round"`, `"gameState"` |

## Returns

| Value | Description |
|----|------|
| `1` | Registered successfully; also returns `1` when a variable with the same name is already registered, without resetting its current value |
| `0` | Failure: not the host (client or not connected), or name is empty |

## Usage

- **Host only**. Shared variables are host-authoritative: clients can only read, not write.
- Registration merely "declares the name"; the initial value is `0`. To actually write a value, call `qiumingdll_net_set_shared_var()`.
- Unregistered names are also registered automatically by `set_shared_var`, so registration is mainly for declaring names in advance and letting new clients receive the initial value in WELCOME.
- When a new client joins, the WELCOME snapshot carries the current values of all registered variables and queues them as `kind="var"` events.
- Variable values can be any valid JSON (number, string, boolean, object, array); the caller defines the meaning.

## Example

```gml
// host's Create event
qiumingdll_net_host_start("0.0.0.0", 25565, 4);
qiumingdll_net_register_shared_var("score");
qiumingdll_net_register_shared_var("round");
qiumingdll_net_register_shared_var("gameState");
```

## Related functions

- [qiumingdll_net_set_shared_var](qiumingdll_net_set_shared_var.md)
- [qiumingdll_net_get_shared_vars_json](qiumingdll_net_get_shared_vars_json.md)
- [qiumingdll_net_host_start](qiumingdll_net_host_start.md)
- [qiumingdll_net_poll_json](qiumingdll_net_poll_json.md)
