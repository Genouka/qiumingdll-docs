# qiumingdll_ime_poll_json()

Polls all IME state at once and returns a JSON string.

## Signature

```gml
qiumingdll_ime_poll_json()
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|-------|-------------|
| String | JSON string containing all IME state (keys listed below) |

Always returns "{}" on non-Windows platforms.

JSON keys:

| Key | Type | Description |
|-----|------|-------------|
| composing | Boolean | Whether composition input is in progress |
| compText | String | Current composition text |
| compCursor | Real | Cursor position within the composition text (character offset) |
| commitText | String | Committed text (one-shot, cleared after being read, never appears again) |
| candidates | Array | Array of candidate word strings |
| candidateSel | Real | Index of the currently selected candidate (-1 = none selected) |
| inputMode | Real | Input mode: 0=English, 1=Chinese |
| stateFlags | Real | Bitmask of state-change flags (bitwise OR of 0x01/0x02/0x04/0x08) |

## Usage

- Platform limit: Windows only; always returns "{}" on other platforms.
- Difference from polling item by item (`qiumingdll_ime_get_state` + the individual get_* functions): a single call returns all state without first checking flags; the cost is that you need to parse JSON.
- Side effects: after the call the one-shot flags (0x02/0x04/0x08) and the committed text are cleared; `commitText` is only returned once, in the current frame.
- All text is UTF-8 and can be parsed directly.
- Recommended parsing: `json_parse` to get a ds_map + ds_list, or use the convenience wrapper `qiumingdll_ime_poll` directly (returns a ds_map, performs the parsing internally and guarantees that candidates exists).
- Performance: the underlying implementation builds a single string, so the per-frame cost is tiny; it is safe to poll every frame.

## Example

```gml
// Poll and parse every frame
var json = qiumingdll_ime_poll_json();
if (json != "{}") {
    var map = json_parse(json);
    if (map != undefined) {
        var commit = ds_map_find_value(map, "commitText");
        if (commit != "") {
            input_text += commit;
        }
        var composing = ds_map_find_value(map, "composing");
        if (composing) {
            var comp = ds_map_find_value(map, "compText");
            // draw the composition text yourself
        }
        json_destroy(map); // release the parse result
    }
}
```

## Related functions

- [qiumingdll_ime_poll](qiumingdll_ime_poll.md)
- [qiumingdll_ime_poll_destroy](qiumingdll_ime_poll_destroy.md)
- [qiumingdll_ime_get_state](qiumingdll_ime_get_state.md)
