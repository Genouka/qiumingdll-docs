# qiumingdll_ime_get_candidate(index)

Get the candidate text at the specified index.

## Signature

```gml
qiumingdll_ime_get_candidate(index)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| index | Real | yes | Candidate index, starting at 0; the valid range is 0 ~ `qiumingdll_ime_get_candidate_count()-1` |

## Returns

| Value | Description |
|----|------|
| String | The candidate text at the given index (UTF-8) |
| "" | The index is invalid (out of range) or there is no candidate list at the moment |

Non-Windows platforms always return "".

## Usage

- Platform limit: Windows only; other platforms always return "".
- Out-of-range indices do not raise an error; the function returns an empty string "" instead, so you can safely iterate by count without worrying about overrunning the list.
- The candidate list changes in real time as composition input proceeds (read the latest list after status bit 0x04).
- The text is UTF-8 encoded and can be drawn or concatenated directly.
- Typical use: iterate over all candidates to draw a candidate box, and use `qiumingdll_ime_get_candidate_selection` to highlight the selected item.

## Example

```gml
// Iterate over and draw the candidates (one per line)
var n = qiumingdll_ime_get_candidate_count();
for (var i = 0; i < n; i++) {
    var cand = qiumingdll_ime_get_candidate(i);
    if (cand == "") break; // Defensive: stop when the index is invalid
    var label = string(i + 1) + ". " + cand;
    draw_text(cand_x, cand_y + i * 20, label);
}
```

## Related functions

- [qiumingdll_ime_get_candidate_count](qiumingdll_ime_get_candidate_count.md)
- [qiumingdll_ime_get_candidate_selection](qiumingdll_ime_get_candidate_selection.md)
- [qiumingdll_ime_get_state](qiumingdll_ime_get_state.md)
