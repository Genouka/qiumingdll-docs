# qiumingdll_ime_get_candidate_selection()

Get the index of the selected candidate in the current candidate list.

## Signature

```gml
qiumingdll_ime_get_candidate_selection()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| Real | The currently selected candidate index (starting at 0, using the same index scheme as `qiumingdll_ime_get_candidate`) |
| -1 | No candidate is currently selected (e.g. the candidate list is empty, or no candidate has been selected) |

Non-Windows platforms always return -1.

## Usage

- Platform limit: Windows only; other platforms always return -1.
- Precondition: the call is meaningful while the candidate list is valid (read after status bit 0x04); it returns -1 when there are no candidates.
- The return value can be combined with `qiumingdll_ime_get_candidate_count`: the selected index is always smaller than the candidate count (-1 when nothing is selected).
- When the user presses ←/→ or the number keys to switch candidates, the selected index updates accordingly; polling is required to reflect the latest selection.
- Typical uses: highlight the currently selected item while drawing the candidate box (together with `qiumingdll_ime_get_candidate`), or commit the candidate matching the number key pressed.

## Example

```gml
// Draw the candidate box and highlight the selected item
var n = qiumingdll_ime_get_candidate_count();
var sel = qiumingdll_ime_get_candidate_selection();
for (var i = 0; i < n; i++) {
    var label = string(i + 1) + ". " + qiumingdll_ime_get_candidate(i);
    if (i == sel) {
        draw_set_color(c_yellow); // Highlight the selected item
    } else {
        draw_set_color(c_white);
    }
    draw_text(cand_x, cand_y + i * 20, label);
}
```

## Related functions

- [qiumingdll_ime_get_candidate](qiumingdll_ime_get_candidate.md)
- [qiumingdll_ime_get_candidate_count](qiumingdll_ime_get_candidate_count.md)
- [qiumingdll_ime_get_state](qiumingdll_ime_get_state.md)
