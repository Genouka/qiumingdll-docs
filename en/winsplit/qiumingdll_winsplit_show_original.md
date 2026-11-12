# qiumingdll_winsplit_show_original()

Restore and show the hidden original game window, at the same position as before it was hidden; used as a pair with `hide_original`.

## Signature

```gml
qiumingdll_winsplit_show_original()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters; it acts on the game's main window recorded at `init` time |

## Returns

| Value | Description |
|----|------|
| 1 | Call succeeded (if the original window was not hidden, 1 is also returned with no side effects) |
| 0 | The original game window handle is invalid (in theory this only happens if the main window was destroyed after `init`); on non-Windows platforms the wrapper returns `0` directly |

## Usage

- Prerequisite: `qiumingdll_winsplit_init()` has been called successfully.
- Used as a pair with `qiumingdll_winsplit_hide_original()`; after restoring, the original window becomes visible again with the same position, size, and style as before it was hidden.
- Can be called repeatedly: calling it while not hidden causes no change.
- Restoring does not affect split windows; they can continue to be displayed.
- Under the Windows 7 "move off-screen" approach, this function moves the window back to the position recorded before hiding.
- Recommended to call when the game exits or when switching back to "normal single-window mode" (the cleanup routine also restores it automatically).

## Example

```gml
// In the controller object's Step event: space toggles between "split mode" and "single-window mode"
if (keyboard_check_pressed(vk_space))
{
    global.split_mode = !global.split_mode;
    if (global.split_mode)
    {
        // Enter split mode: hide the original window and show only the split windows
        qiumingdll_winsplit_hide_original();
    }
    else
    {
        // Leave split mode: restore the original window
        qiumingdll_winsplit_show_original();
    }
}
```

## Related functions

- [qiumingdll_winsplit_hide_original](qiumingdll_winsplit_hide_original.md)
- [qiumingdll_winsplit_cleanup](qiumingdll_winsplit_cleanup.md)
- [qiumingdll_winsplit_destroy_all](qiumingdll_winsplit_destroy_all.md)
