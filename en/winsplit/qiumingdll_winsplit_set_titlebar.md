# qiumingdll_winsplit_set_titlebar(splitId, hasTitleBar)

Set whether the specified split window has a title bar (including the window border and system buttons). When toggled, the window's client area size stays the same, while the outer frame size and top-left corner adjust accordingly.

## Signature

```gml
qiumingdll_winsplit_set_titlebar(splitId, hasTitleBar)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window ID, value 1 ~ 16, must exist |
| hasTitleBar | Real/Bool | yes | Whether to have a title bar: non-zero (true) = has a title bar (default), 0 (false) = borderless, no title bar |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Failed: `splitId` is invalid or does not exist; on non-Windows platforms the wrapper returns `0` directly |

## Usage

- Prerequisite: `qiumingdll_winsplit_init()` has been called successfully, and the split window corresponding to `splitId` exists.
- Default at creation is `hasTitleBar = true` (has a title bar).
- If the requested value equals the current value (e.g. already borderless and setting false again), returns 1 directly without doing anything.
- Toggling rebuilds the window style: the client area (the picture display area) size stays the same, so the outer frame's overall size increases or decreases accordingly, and to keep the client area's top-left corner aligned, the window's top-left position is adjusted slightly (query the new position with `get_info` 0/1).
- A window without a title bar (false) is cleaner and suitable for "picture-only" uses; however there is no visible close button and the system menu's close entry disappears too. If you need to keep the ability to close it, pair it with the close-related behavior (`closable` still controls the WM_CLOSE response, and the program can still destroy it with `destroy`).
- With a title bar you can use `qiumingdll_winsplit_set_title` to show a custom title, and `qiumingdll_winsplit_set_closable` to control whether the X button is enabled.

## Example

```gml
// In the controller object's Step event: press N to toggle the title bar of split window 1
if (keyboard_check_pressed(ord("N")))
{
    global.split_has_title = !global.split_has_title;
    qiumingdll_winsplit_set_titlebar(global.split_1, global.split_has_title);

    if (global.split_has_title)
        qiumingdll_winsplit_set_title(global.split_1, "Preview window");
}
```

## Related functions

- [qiumingdll_winsplit_set_title](qiumingdll_winsplit_set_title.md)
- [qiumingdll_winsplit_set_closable](qiumingdll_winsplit_set_closable.md)
- [qiumingdll_winsplit_set_draggable](qiumingdll_winsplit_set_draggable.md)
- [qiumingdll_winsplit_get_info](qiumingdll_winsplit_get_info.md)
