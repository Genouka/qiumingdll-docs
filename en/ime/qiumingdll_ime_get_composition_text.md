# qiumingdll_ime_get_composition_text()

Get the current IME composition text (the string, such as pinyin or strokes, that has not yet been confirmed).

## Signature

```gml
qiumingdll_ime_get_composition_text()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| String | The current composition text; returns an empty string "" when not composing |

Non-Windows platforms always return "".

## Usage

- Platform limit: Windows only; other platforms always return "".
- Precondition: the call is meaningful after `qiumingdll_ime_get_state` confirms that the status bits contain 0x01 (composing); it returns "" when not composing.
- The composition text changes in real time as the user types (every pinyin letter updates it), so continuous polling is required to get the latest content.
- The text is UTF-8 encoded; GML strings can concatenate, compare and draw it directly, and Chinese characters need no extra conversion.
- This function is read-only; it neither clears nor modifies the composition state.
- After composition ends (pressing space / committing a candidate) the composition text becomes "", at which point you should stop drawing it.
- If you only need to know "whether a composition is in progress", `qiumingdll_ime_is_composing` is more direct (and does not disturb the state flags).

## Example

```gml
// Check and draw the composition text every frame
var state = qiumingdll_ime_get_state();
if (state & 1) { // Composing
    var comp = qiumingdll_ime_get_composition_text();
    if (comp != "") {
        draw_set_color(c_blue);
        draw_text(input_x + string_width(input_text), input_y, comp);
    }
}
```

## Related functions

- [qiumingdll_ime_get_composition_cursor](qiumingdll_ime_get_composition_cursor.md)
- [qiumingdll_ime_get_state](qiumingdll_ime_get_state.md)
- [qiumingdll_ime_is_composing](qiumingdll_ime_is_composing.md)
