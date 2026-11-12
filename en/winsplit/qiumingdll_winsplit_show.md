# qiumingdll_winsplit_show(splitId)

Show the specified split window (if it was previously hidden) without activating it or stealing focus.

## Signature

```gml
qiumingdll_winsplit_show(splitId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window ID, value 1 ~ 16, must exist |

## Returns

| Value | Description |
|----|------|
| 1 | Shown successfully |
| 0 | Failed: `splitId` is invalid or does not exist; on non-Windows platforms the wrapper returns `0` directly |

## Usage

- Prerequisite: `qiumingdll_winsplit_init()` has been called successfully, and the split window corresponding to `splitId` exists.
- Used as a pair with `qiumingdll_winsplit_hide`; windows are visible by default at creation, so if `hide` was never called there is no need to call this function.
- The window is shown without activation (`SW_SHOWNA`), so it does not take focus away from the game window; suitable for multi-window game scenarios.
- A hidden split window is not displayed, but its internal state (position, size, source region) is preserved and restored when it is shown again.

## Example

```gml
// In the controller object's Step event: press 0 to toggle show/hide of split window 1
if (keyboard_check_pressed(ord("0")))
{
    global.split_visible = !global.split_visible;
    if (global.split_visible)
        qiumingdll_winsplit_show(global.split_1);
    else
        qiumingdll_winsplit_hide(global.split_1);
}
```

## Related functions

- [qiumingdll_winsplit_hide](qiumingdll_winsplit_hide.md)
- [qiumingdll_winsplit_create](qiumingdll_winsplit_create.md)
- [qiumingdll_winsplit_hide_original](qiumingdll_winsplit_hide_original.md)
