# qiumingdll_ime_poll()

Polls all IME state at once, parses it into a GML ds_map, and returns it.

## Signature

```gml
qiumingdll_ime_poll()
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| (none) | - | - | This function takes no parameters |

## Returns

| Key | Type | Description |
|-----|------|-------------|
| "composing" | Real | Whether composition input is in progress (0/1) |
| "compText" | String | Current composition text |
| "compCursor" | Real | Cursor position within the composition text (character offset) |
| "commitText" | String | Committed text (one-shot, cleared after being read) |
| "candidates" | ds_list | Candidate word list, elements are String |
| "candidateSel" | Real | Index of the currently selected candidate (-1 = none selected) |
| "inputMode" | Real | Input mode: 0=English, 1=Chinese |
| "stateFlags" | Real | Bitmask of state-change flags |

- On non-Windows platforms or when the extension is not initialized: returns an empty ds_map (no keys at all).
- When JSON parsing fails, an empty ds_map is returned as well.

## Usage

- Platform limit: only Windows returns complete data; other platforms return an empty ds_map (you can safely use `ds_map_size` to check that it is empty).
- **Memory management (important)**: the returned ds_map must be destroyed with `qiumingdll_ime_poll_destroy(map)` after use (that method also destroys the internal candidates ds_list); otherwise calling it every frame leaks memory.
- The "candidates" key is always present: even with no candidates it is an empty ds_list, so you can use `ds_list_size` / `ds_list_find_value` directly without checking for emptiness.
- commitText is one-shot data: it is cleared as soon as it is read in the current frame, and the same committed text is not returned again on the next frame.
- Relationship with `qiumingdll_ime_poll_json`: this function internally calls poll_json and then parses the result, making it the more convenient GML-side wrapper.
- The ime_input wrapper family uses this function internally, so there is no need to call it manually.

## Example

```gml
// Step event: poll and handle all state
var m = qiumingdll_ime_poll();

// Enter the committed text
var commit = ds_map_find_value(m, "commitText");
if (commit != "") {
    input_text += commit;
}

// Composition state
if (ds_map_find_value(m, "composing")) {
    var comp = ds_map_find_value(m, "compText");
    var cur  = ds_map_find_value(m, "compCursor");
    // Draw the composition text and cursor ...
}

// Candidate list
var candList = ds_map_find_value(m, "candidates");
var candCount = ds_list_size(candList);
for (var i = 0; i < candCount; i++) {
    show_debug_message(string(i) + ": " + ds_list_find_value(candList, i));
}

// Must be destroyed after use to prevent memory leaks
qiumingdll_ime_poll_destroy(m);
```

## Related functions

- [qiumingdll_ime_poll_destroy](qiumingdll_ime_poll_destroy.md)
- [qiumingdll_ime_poll_json](qiumingdll_ime_poll_json.md)
- [qiumingdll_ime_input_step](qiumingdll_ime_input_step.md)
