# qiumingdll_net_set_shared_var()

The host sets the value of a shared variable (a JSON literal) and broadcasts it to all clients immediately.

## Signature

```gml
qiumingdll_net_set_shared_var(name, json_value)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| name | string | yes | Variable name (case-sensitive) |
| json_value | string | yes | The variable value as **JSON literal text**, broadcast verbatim |

`json_value` is JSON, not a GML value, so watch the quotes:

| Desired value | String to pass |
|----------|--------------|
| number 123 | `"123"` |
| string "abc" | `"\"abc\""` |
| boolean true | `"true"` |
| object | `"{\"hp\":10,\"mp\":5}"` |
| array | `"[1,2,3]"` |

## Returns

| Value | Description |
|----|------|
| `1` | Set and broadcast successfully (host) |
| `0` | Failure: not the host (client/not connected), or name is empty |

## Usage

- **Host only**. Client calls always return `0`; shared variables are decided authoritatively by the host.
- Names that were never registered are registered automatically (equivalent to an implicit `register_shared_var`), so registration is optional.
- Each set does the following: updates the host's local snapshot → broadcasts to all clients → queues a `kind="var"` event for the host itself (`peer=0`).
- Clients cache the value and reflect it in `get_shared_vars_json()`, while also queueing a `kind="var"` event (`peer=0`).
- **Always pass valid JSON**: this module does no validation, and invalid text enters the event JSON verbatim, making `poll_json()` output unparsable.
- Broadcasting is "last write wins", with no acknowledgement or rollback; for high-frequency updates, merge them yourself (for example synchronize at most once per frame).

## Example

```gml
// host: synchronize when the score changes
global.score += 10;
qiumingdll_net_set_shared_var("score", string(global.score));

// Synchronize an object
qiumingdll_net_set_shared_var("gameState", "{\"round\":3,\"phase\":\"battle\"}");

// Synchronize a string (note the escaping)
qiumingdll_net_set_shared_var("hostName", "\"Alice\"");
```

Reading on the client side:

```gml
var _vars = json_parse(qiumingdll_net_get_shared_vars_json());
for (var i = 0; i < array_length(_vars); i++)
{
    if (_vars[i].name == "score") global.score = _vars[i].value;
}
```

## Related functions

- [qiumingdll_net_register_shared_var](qiumingdll_net_register_shared_var.md)
- [qiumingdll_net_get_shared_vars_json](qiumingdll_net_get_shared_vars_json.md)
- [qiumingdll_net_poll_json](qiumingdll_net_poll_json.md)
