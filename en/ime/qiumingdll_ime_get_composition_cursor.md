# qiumingdll_ime_get_composition_cursor()

Get the cursor position within the composition text (character offset, starting at 0).

## Signature

```gml
qiumingdll_ime_get_composition_cursor()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| Real | The cursor position within the composition text (character offset, starting at 0); usually 0 when not composing |

Non-Windows platforms always return 0.

## Usage

- Platform limit: Windows only; other platforms always return 0.
- Precondition: use it alongside the composition text; confirm that the `qiumingdll_ime_get_state` status bits contain 0x01 before calling.
- The value is a **character offset**, not a byte offset. For example, with the composition text "nihao", a cursor after the 3rd character returns 3, which can be fed directly into `string_copy(comp, 1, cursor)` to take the part before the cursor.
- While composing, the value updates as the user moves the cursor with ←/→, so continuous polling is required.
- Typical uses: drawing the caret line at the correct position inside the composition text, and splitting the composition underline into segments.
- The return value never exceeds the character count of the current composition text.

## Example

```gml
// Draw the caret line inside the composition text
var state = qiumingdll_ime_get_state();
if (state & 1) {
    var comp  = qiumingdll_ime_get_composition_text();
    var cur   = qiumingdll_ime_get_composition_cursor();
    var baseX = input_x + string_width(input_text);
    // Width of the text before the cursor determines the caret position
    var curX  = baseX + string_width(string_copy(comp, 1, cur));
    draw_line(curX, input_y, curX, input_y + string_height(comp));
}
```

## Related functions

- [qiumingdll_ime_get_composition_text](qiumingdll_ime_get_composition_text.md)
- [qiumingdll_ime_get_state](qiumingdll_ime_get_state.md)
- [qiumingdll_ime_input_draw_text](qiumingdll_ime_input_draw_text.md)
