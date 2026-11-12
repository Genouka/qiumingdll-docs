# qiumingdll_net_get_shared_vars_json()

Returns a snapshot of the current shared variables (as a JSON array string).

## Signature

```gml
qiumingdll_net_get_shared_vars_json()
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| (none) | - | - | This function takes no parameters |

## Returns

| Side | Return value |
|------|--------------|
| host | `[{"name":"score","value":123},{"name":"round","value":3},...]` (registration order) |
| client | The latest snapshot synchronized from the host (WELCOME plus subsequent deltas) |
| not connected | `"[]"` |

> The returned string uses an internal static buffer and is **valid until the next call to this function**; to keep it across frames, `json_parse` or copy it immediately.

## Usage

- The `value` of each array element is **any JSON value** (number, string, boolean, object or array); its type is decided by whatever the host wrote, and you interpret it according to your own conventions.
- The client-side cache is initialized by WELCOME and then updated by each variable broadcast delta, so this function always reflects the "latest known value".
- This is a pull-style snapshot; for event-style access use the `kind="var"` events from `poll_json()` (both expose the same data, so pick one way of consuming it).
- The function is read-only and clears no state; variables that were never registered yield an empty array.
- Values are broadcast by the host as raw JSON text; this module performs no type conversion, so make sure what you write is valid JSON.

## Example

```gml
var _vars = json_parse(qiumingdll_net_get_shared_vars_json());
var _map = {};

for (var i = 0; i < array_length(_vars); i++)
{
    _map[$ _vars[i].name] = _vars[i].value;
}

if (variable_struct_exists(_map, "score"))
{
    global.score = _map.score;
}

// Synchronize an object variable
if (variable_struct_exists(_map, "gameState"))
{
    global.round = _map.gameState.round;
    global.phase = _map.gameState.phase;
}
```

## Related functions

- [qiumingdll_net_register_shared_var](qiumingdll_net_register_shared_var.md)
- [qiumingdll_net_set_shared_var](qiumingdll_net_set_shared_var.md)
- [qiumingdll_net_poll_json](qiumingdll_net_poll_json.md)
