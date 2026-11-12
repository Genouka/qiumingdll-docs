# qiumingdll_ime_input_draw_text()

Draws only the text part of the input box (confirmed text + composition text + underline + cursor), without the background or candidate list, for custom rendering.

## Signature

```gml
qiumingdll_ime_input_draw_text()
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|-------|-------------|
| Real | X coordinate of the end of the text: where the cursor sits after the confirmed text and composition text have been drawn (returns `ime_x` when not focused), so you can continue drawing other content after it |

## Usage

- Precondition: `qiumingdll_ime_input_create` must be called first to create the input box.
- The drawing origin is (ime_x, ime_y) (top-left aligned, no vertical centering, unlike `qiumingdll_ime_input_draw`).
- When `ime_focused` is false, it returns `ime_x` immediately and draws nothing.
- What is drawn:
  1. Confirmed text: `ime_color_text`, starting at (ime_x, ime_y);
  2. Composition text (when composing and non-empty): `ime_color_comp` immediately after the confirmed text, with an underline drawn beneath (same color as the composition text color, baseline at ime_y + line height);
  3. Composition cursor: a vertical line drawn according to `ime_comp_cursor` (`ime_color_cursor`);
  4. When not composing: a blinking cursor is drawn (same rhythm as `ime_cursor_blink`).
- Return value computation: confirmed text width + composition text width (i.e. it returns `ime_x + string_width(ime_text)`, or that plus the composition text width).
- Typical usage: when customizing the input box background/position, use this function to draw the text and pass the returned X to other drawing (such as icons and buttons); the candidate box can be drawn separately with `qiumingdll_ime_input_draw_candidates`.
- This function modifies the current font/color settings.

## Example

```gml
// Draw event: custom rendering -- text + trailing icon + candidate box
var endX = qiumingdll_ime_input_draw_text();
// Draw a decorative icon at the end of the text
draw_sprite(spr_input_icon, 0, endX + 6, ime_y);
// Draw the candidate box below the icon
qiumingdll_ime_input_draw_candidates(endX + 6, ime_y + string_height("A") + 12);
```

## Related functions

- [qiumingdll_ime_input_draw](qiumingdll_ime_input_draw.md)
- [qiumingdll_ime_input_draw_candidates](qiumingdll_ime_input_draw_candidates.md)
- [qiumingdll_ime_input_create](qiumingdll_ime_input_create.md)
