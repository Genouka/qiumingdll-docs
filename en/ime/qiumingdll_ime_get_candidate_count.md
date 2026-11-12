# qiumingdll_ime_get_candidate_count()

Get the number of candidates in the current candidate list.

## Signature

```gml
qiumingdll_ime_get_candidate_count()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| Real | The current number of candidates; 0 means there is no candidate list at the moment |

Non-Windows platforms always return 0.

## Usage

- Platform limit: Windows only; other platforms always return 0.
- Precondition: reads related to the candidate list should be done after the `qiumingdll_ime_get_state` status bits contain 0x04 (candidate list changed); however, this function still returns the current count even when nothing has changed.
- The candidate list is tied to the current composition input: candidates change frequently while composing; after composition ends or the candidate box closes the count is 0.
- The underlying layer keeps at most 50 candidates (anything beyond that is truncated), so the return value is at most 50.
- Commonly combined with `qiumingdll_ime_get_candidate(index)` to iterate over and draw the candidate box.

## Example

```gml
// Print every candidate when the candidate list changes
var state = qiumingdll_ime_get_state();
if (state & 4) {
    var n = qiumingdll_ime_get_candidate_count();
    show_debug_message("Candidate count: " + string(n));
    for (var i = 0; i < n; i++) {
        show_debug_message(string(i) + ": " + qiumingdll_ime_get_candidate(i));
    }
}
```

## Related functions

- [qiumingdll_ime_get_candidate](qiumingdll_ime_get_candidate.md)
- [qiumingdll_ime_get_candidate_selection](qiumingdll_ime_get_candidate_selection.md)
- [qiumingdll_ime_get_state](qiumingdll_ime_get_state.md)
