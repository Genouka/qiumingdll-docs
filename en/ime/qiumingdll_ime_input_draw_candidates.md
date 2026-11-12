# qiumingdll_ime_input_draw_candidates(x, y)

Draws only the candidate list (candidate box background + border + candidates + selection highlight), optionally at a specified position.

## Signature

```gml
qiumingdll_ime_input_draw_candidates(x, y)
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| x | Real | No | X coordinate of the candidate box's top-left corner; when omitted, the default position is used (ime_x + 6 + confirmed text width) |
| y | Real | No | Y coordinate of the candidate box's top-left corner; when omitted, the default position is used (ime_y + ime_h + 4) |

## Returns

No return value (this function does not return anything).

## Usage

- Precondition: `qiumingdll_ime_input_create` must be called first to create the input box.
- x/y are optional parameters: **when omitted, the default position is used** (identical to the candidate box position built into `qiumingdll_ime_input_draw`); when both are passed, the box is drawn at the given position.
- When the candidate list is empty (`ime_cand_list` size is 0), the function returns immediately and draws nothing.
- What is drawn:
  1. Background: a semi-transparent (alpha 0.9) solid rectangle in `ime_color_cand_bg`;
  2. Border: a 3:7 mix of `ime_color_cand_bg` and white;
  3. Candidates: formatted as "index. text" (index starts at 1, i.e. "1. candidate one"), each row height = line height + 6 pixels; color `ime_color_cand_text`;
  4. Selected item (index equal to `ime_cand_sel`): shown with the `ime_color_cand_sel_bg` highlighted background + the `ime_color_cand_sel_text` highlighted text color.
- Candidate box width: the maximum width of all "index. text" entries + 16, minimum 100 pixels.
- Usually combined with `qiumingdll_ime_input_draw_text` for fully customized input box rendering; the default position is designed to appear directly below the input box.
- Should be called after `qiumingdll_ime_input_step` (so that `ime_cand_list` holds the latest data).
- This function modifies the current color/alpha/font settings.

## Example

```gml
// Draw the candidate box at the default position (same effect as the complete input box)
qiumingdll_ime_input_draw_candidates();
```

```gml
// Custom position: make the candidate box follow the mouse
var endX = qiumingdll_ime_input_draw_text();
qiumingdll_ime_input_draw_candidates(mouse_x, mouse_y);
```

## Related functions

- [qiumingdll_ime_input_draw_text](qiumingdll_ime_input_draw_text.md)
- [qiumingdll_ime_input_draw](qiumingdll_ime_input_draw.md)
- [qiumingdll_ime_input_step](qiumingdll_ime_input_step.md)
