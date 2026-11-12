# qiumingdll_winsplit_set_topmost(splitId, topmost)

Set whether the specified split window is always on top (always floating above other windows, including the game's main window and other applications' windows).

## Signature

```gml
qiumingdll_winsplit_set_topmost(splitId, topmost)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window ID, value 1 ~ 16, must exist |
| topmost | Real/Bool | yes | Whether to stay on top: non-zero (true) = on top, 0 (false) = cancel topmost |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Failed: `splitId` is invalid or does not exist; on non-Windows platforms the wrapper returns `0` directly |

## Usage

- Prerequisite: `qiumingdll_winsplit_init()` has been called successfully, and the split window corresponding to `splitId` exists.
- Split windows are created with the topmost style (`WS_EX_TOPMOST`) by default, i.e. the default behavior is already "always on top"; usually there is no need to call this function.
- `topmost = 1` makes the window float above all windows; `topmost = 0` cancels topmost, and the window takes part in the normal stacking order (it can be covered by other windows).
- Canceling topmost only affects the z-order; it does not affect the window's position, size, or content.
- Topmost works in multi-monitor setups too: a topmost window always floats above the workspace.
- Consistent with the OS's intuitive "always on top" behavior: suitable for windows that must stay visible, such as minimaps, floating panels, and consoles.

## Example

```gml
// In the controller object's Step event: press T to toggle the topmost state of split window 1
if (keyboard_check_pressed(ord("T")))
{
    global.split_topmost = !global.split_topmost;
    qiumingdll_winsplit_set_topmost(global.split_1, global.split_topmost);
}
```

```gml
// Ensure the floating toolbar window is always on top
qiumingdll_winsplit_set_topmost(global.split_toolbar, true);
```

## Related functions

- [qiumingdll_winsplit_create](qiumingdll_winsplit_create.md)
- [qiumingdll_winsplit_set_opacity](qiumingdll_winsplit_set_opacity.md)
- [qiumingdll_winsplit_set_draggable](qiumingdll_winsplit_set_draggable.md)
