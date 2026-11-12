# qiumingdll_ime_input_draw()

Draws the complete IME input box: background + border + confirmed text + composition text + underline + cursor + candidate box.

## Signature

```gml
qiumingdll_ime_input_draw()
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| (none) | - | - | This function takes no parameters |

## Returns

No return value (this function does not return anything).

## Usage

- Precondition: `qiumingdll_ime_input_create` must be called first to create the input box.
- Call once per frame in the object's Draw event (or Draw GUI, depending on the coordinate system you use), usually after `qiumingdll_ime_input_step`.
- When `ime_focused` is false, this function exits immediately and draws nothing.
- What is drawn (appearance controlled by the `ime_color_*` and `ime_font` variables):
  1. Background: a solid rectangle filled with `ime_color_bg` (at ime_x, ime_y, size ime_w, ime_h);
  2. Border: a rectangle border in a 1:1 mix of `ime_color_text` and gray;
  3. Confirmed text: drawn with `ime_color_text`, starting at ime_x+6, vertically centered;
  4. Composition text (when composing and non-empty): `ime_color_comp` immediately after the confirmed text, with an underline drawn beneath it;
  5. Composition cursor: a vertical line drawn within the composition text according to `ime_comp_cursor` (`ime_color_cursor`);
  6. When not composing: a blinking cursor is drawn (visible for the first 30 frames of `ime_cursor_blink`, hidden afterwards);
  7. Candidate list (when non-empty): the candidate box is drawn at the default position (ime_x + 6 + confirmed text width, ime_y + ime_h + 4), numbered from 1 (format "1. candidate one"), with the selected item shown with a highlighted background + highlighted text color; the candidate box width is the maximum text width over all candidates + 16, minimum 100.
- For custom layouts (such as a candidate box appearing next to the mouse, or text that is not vertically centered), use the `qiumingdll_ime_input_draw_text` + `qiumingdll_ime_input_draw_candidates` combination instead.
- This function modifies the current drawing color/font/alpha settings; save them yourself (`draw_get_color` etc.) if you need to restore them afterwards.

## Example

```gml
// Draw event: draw the complete input box directly
qiumingdll_ime_input_draw();
```

```gml
// Example: complete usage of the input box (all four events: Create / Step / Draw / Clean Up)
// Create:  qiumingdll_ime_input_create(50, 300, 400, 36);
// Step:    qiumingdll_ime_input_step();
// Draw:    qiumingdll_ime_input_draw();
// Clean Up: qiumingdll_ime_input_cleanup();
```

## Related functions

- [qiumingdll_ime_input_draw_text](qiumingdll_ime_input_draw_text.md)
- [qiumingdll_ime_input_draw_candidates](qiumingdll_ime_input_draw_candidates.md)
- [qiumingdll_ime_input_create](qiumingdll_ime_input_create.md)
