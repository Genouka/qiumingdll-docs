# qiumingdll_ime_set_inline_position(x, y)

Inlines the IME composition window and candidate window into the specified position of the game window's client area, and enables inline mode.

## Signature

```gml
qiumingdll_ime_set_inline_position(x, y)
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| x | Real | Yes | X pixel coordinate of the inline position within the game window's client area (used as an integer) |
| y | Real | Yes | Y pixel coordinate of the inline position within the game window's client area (used as an integer) |

## Returns

| Value | Description |
|-------|-------------|
| 0 | Success: the inline position is set and inline mode is enabled |
| 1 | No target window: no valid window could be found. Always returned on non-Windows platforms |
| 2 | No IME context: the window is valid, but its IME context could not be obtained |

## Usage

- Platform limit: Windows only; always returns 1 on other platforms.
- Precondition: it is recommended to call `qiumingdll_ime_fix_conflict` first to record the target window; if it was not called, this function automatically finds and uses the foreground window.
- Purpose: enables "inline IME" mode — the system composition window and candidate window are hidden (no longer drawn by the system) and are pinned at the client-area coordinates you specify; underneath, window message handling is hooked so that composition text, committed text, candidate lists and other information is recorded in internal state, to be read by the state-polling APIs (`qiumingdll_ime_get_state`, `qiumingdll_ime_poll`, etc.).
- Relative position of the composition box and the candidate box: both are placed by the underlying layer near the given coordinates (the candidate window appears about 20 pixels below the composition position); the game does not need to care about the exact pixel offsets.
- Coordinate system: x/y are game window **client area** coordinates (neither screen coordinates nor room coordinates). If the game window moves or is resized, call this function again to update the position.
- Typical usage: call once per frame (Step event) to move the position along with the current input caret / end of the text, so the composition window "sticks" to the input position.
- Every call updates the internally recorded position; during composition, the position set most recently is also used to reposition the boxes.
- Corresponding cancel operation: call `qiumingdll_ime_reset_inline` to restore the system default behavior.

## Example

```gml
// Step event: make the system composition window follow the end of the text
var posX = input_x + 6 + string_width(text);
qiumingdll_ime_set_inline_position(posX, input_y + 4);
```

```gml
// Simple case: pin it to the center of the screen
qiumingdll_ime_set_inline_position(room_width / 2, room_height / 2);
```

## Related functions

- [qiumingdll_ime_reset_inline](qiumingdll_ime_reset_inline.md)
- [qiumingdll_ime_fix_conflict](qiumingdll_ime_fix_conflict.md)
- [qiumingdll_ime_get_state](qiumingdll_ime_get_state.md)
- [qiumingdll_ime_input_step](qiumingdll_ime_input_step.md)
