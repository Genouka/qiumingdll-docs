# qiumingdll_ime_get_state()

Return the IME state-change flags (bitmask) used to decide which data to read next.

## Signature

```gml
qiumingdll_ime_get_state()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 0 | No state change at all |
| 0x01 (1) | A composition is in progress. **Persistent state**: stays set for the whole composition, is not cleared by reading, and disappears only when the composition ends |
| 0x02 (2) | There is new commit text. **One-shot flag**: cleared after being read |
| 0x04 (4) | The candidate list has changed. **One-shot flag**: cleared after being read |
| 0x08 (8) | The input mode has changed. **One-shot flag**: cleared after being read |
| Other combinations | Bitwise OR of the flags above, e.g. 5 = 0x01 \| 0x04, 7 = 0x01 \| 0x02 \| 0x04, etc. |

Non-Windows platforms always return 0.

## Usage

- Platform limit: Windows only; other platforms always return 0.
- Polling-style API: IME events do not notify GML proactively, so you must call this function every frame (or at high frequency) to catch changes.
- Standard read flow (check the flags first, then read the data):
  - contains 0x01 → read the composition data: `qiumingdll_ime_get_composition_text` / `qiumingdll_ime_get_composition_cursor` (or simply query `qiumingdll_ime_is_composing`);
  - contains 0x02 → read the commit text: `qiumingdll_ime_get_commit_text` (or use the simplified `qiumingdll_ime_get_commit`);
  - contains 0x04 → read the candidate list: `qiumingdll_ime_get_candidate_count` / `qiumingdll_ime_get_candidate` / `qiumingdll_ime_get_candidate_selection`;
  - contains 0x08 → the input mode has changed; query the new mode with `qiumingdll_ime_get_mode` (the inputMode field of `qiumingdll_ime_poll_json` works too).
- One-shot flags (0x02/0x04/0x08) are cleared immediately after being read and will not appear again in the next frame; the persistent flag (0x01) is unaffected.
- The end of a composition (including committing with a confirm key) also sets 0x01 so you can notice it; at that moment the composition text is an empty string.
- If reading each item individually feels cumbersome, use `qiumingdll_ime_poll_json` / `qiumingdll_ime_poll` to fetch all the state at once.

## Example

```gml
// Step event: read the corresponding data according to the status bits
var state = qiumingdll_ime_get_state();

if (state & 2) { // There is new commit text
    var commit = qiumingdll_ime_get_commit_text();
    total_text += commit;
}

if (state & 1) { // Composing
    var comp = qiumingdll_ime_get_composition_text();
    var cur  = qiumingdll_ime_get_composition_cursor();
    // Draw the composition text and caret ...
}

if (state & 4) { // The candidate list changed
    var n = qiumingdll_ime_get_candidate_count();
    for (var i = 0; i < n; i++) {
        show_debug_message("Candidate " + string(i) + ": " + qiumingdll_ime_get_candidate(i));
    }
}

if (state & 8) { // The input mode changed
    show_debug_message("Input mode: " + string(qiumingdll_ime_get_mode()));
}
```

## Related functions

- [qiumingdll_ime_get_commit_text](qiumingdll_ime_get_commit_text.md)
- [qiumingdll_ime_get_composition_text](qiumingdll_ime_get_composition_text.md)
- [qiumingdll_ime_get_candidate_count](qiumingdll_ime_get_candidate_count.md)
- [qiumingdll_ime_poll_json](qiumingdll_ime_poll_json.md)
