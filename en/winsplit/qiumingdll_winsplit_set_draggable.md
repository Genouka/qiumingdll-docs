# qiumingdll_winsplit_set_draggable(splitId, draggable)

Sets whether the given split window may be moved by dragging with the mouse. When enabled, the user can drag the window directly.

## Signature

```gml
qiumingdll_winsplit_set_draggable(splitId, draggable)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window ID, value 1 ~ 16, must exist |
| draggable | Real/Bool | yes | Whether it can be dragged: non-zero (true) = draggable, 0 (false) = not draggable |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Failed: splitId is invalid or does not exist; on non-Windows platforms the wrapper returns 0 directly |

## Usage

- Prerequisite: `qiumingdll_winsplit_init()` has been called successfully and the split window for splitId exists.
- The default at creation is `draggable = false` (not draggable).
- With a titlebar, hold the titlebar to drag the window; without a titlebar, hold any point of the window to drag it.
- Dragging only moves the window position; it does not affect the window size, source region, shape or other properties. The new position can be read with `qiumingdll_winsplit_get_info(splitId, 0/1)`.
- Important behavioral difference: once dragging is enabled, mouse events inside the split window (clicks, movement, wheel, etc.) are no longer forwarded to the original game window. If the split window serves as an interactive game view (for example clicking game buttons inside it), keep it non-draggable so the game receives your clicks.
- Compared with animated positions, dragging is a user action and the two do not interfere (after an animation ends the window stays at the animation's end point).

## Example

```gml
// In the Step event of a controller object: press G to toggle the "draggable" switch of split window 1
if (keyboard_check_pressed(ord("G")))
{
    global.split_draggable = !global.split_draggable;
    qiumingdll_winsplit_set_draggable(global.split_1, global.split_draggable);

    if (global.split_draggable)
        show_debug_message("Split window dragging enabled (mouse events are no longer forwarded to the game)");
    else
        show_debug_message("Split window locked (clicks are forwarded to the game)");
}
```

## Related functions

- [qiumingdll_winsplit_set_titlebar](qiumingdll_winsplit_set_titlebar.md)
- [qiumingdll_winsplit_set_position](qiumingdll_winsplit_set_position.md)
- [qiumingdll_winsplit_get_info](qiumingdll_winsplit_get_info.md)
- [qiumingdll_winsplit_create](qiumingdll_winsplit_create.md)
