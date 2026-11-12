# qiumingdll_ime_poll_destroy(map)

Destroys the ds_map returned by `qiumingdll_ime_poll()`, together with the candidate list ds_list inside it.

## Signature

```gml
qiumingdll_ime_poll_destroy(map)
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| map | ds_map | Yes | The ds_map returned by `qiumingdll_ime_poll()` |

## Returns

No return value (this function does not return anything).

## Usage

- Platform limit: available on all platforms (on non-Windows, `qiumingdll_ime_poll` returns an empty ds_map, which must be destroyed with this function as well).
- Must be used in pairs with `qiumingdll_ime_poll`: every ds_map returned by poll must be released with this function once it is no longer needed, otherwise memory keeps leaking (at two levels: the ds_map and the ds_list inside it).
- Internal behavior: if the map contains a "candidates" key, the corresponding ds_list is destroyed first, then the ds_map itself; calling it on a map that does not exist (`ds_map_exists` is false) is safely ignored.
- Only destroy maps returned by `qiumingdll_ime_poll`; for similar structures from other sources (such as `json_parse`), use the corresponding normal destruction method.
- Do not destroy the same map twice, and do not keep using the ds_list reference after destruction.

## Example

```gml
var m = qiumingdll_ime_poll();

// ... use the data in m ...

qiumingdll_ime_poll_destroy(m); // remember to destroy it to prevent memory leaks
```

```gml
// Standard pattern for per-frame polling
repeat (2) { // demo: correct usage inside a loop
    var m = qiumingdll_ime_poll();
    // read data ...
    qiumingdll_ime_poll_destroy(m);
}
```

## Related functions

- [qiumingdll_ime_poll](qiumingdll_ime_poll.md)
- [qiumingdll_ime_poll_json](qiumingdll_ime_poll_json.md)
