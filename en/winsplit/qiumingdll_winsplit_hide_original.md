# qiumingdll_winsplit_hide_original()

Hide the original game window (keeping split windows displaying the image), for the typical window-splitting use case where "only the split windows are shown and the main window stays out of sight".

## Signature

```gml
qiumingdll_winsplit_hide_original()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters and acts on the game main window recorded at init |

## Returns

| Value | Description |
|----|------|
| 1 | Call succeeded (also returns 1 if the original window is unavailable or already hidden, with no side effects) |
| 0 | The original game window handle is invalid (in theory only when the main window was destroyed after init); on non-Windows platforms the wrapper returns 0 directly |

## Usage

- Precondition: `qiumingdll_winsplit_init()` has been called successfully.
- The hiding method depends on the system:
  - Windows 8 and later: hidden using DWM window cloak; the window stays in place and keeps rendering, split window images update as usual, and performance is unaffected;
  - Windows 7: DWM Cloak is unavailable, so the window is moved off-screen (-32000,-32000).
- After hiding, the game main window visually disappears, but the game keeps running and still responds to keyboard and other input (mouse events on split windows are also forwarded to the main window).
- Can be called repeatedly: calling it again while hidden does not error or record the state twice.
- Use `qiumingdll_winsplit_show_original()` to restore the original window; after restoring, its position is the same as before hiding.
- If you forget to restore before exiting the game, `qiumingdll_winsplit_cleanup()` restores the original window automatically.

## Example

```gml
// In the controller object's Step event: press F9 to hide the original window, F10 to restore
if (keyboard_check_pressed(vk_f9))
    qiumingdll_winsplit_hide_original();

if (keyboard_check_pressed(vk_f10))
    qiumingdll_winsplit_show_original();
```

```gml
// Typical usage: hide the original window right after creating a split window, so only the split image is on screen
if (global.split_1 > 0)
    qiumingdll_winsplit_hide_original();
```

## Related functions

- [qiumingdll_winsplit_show_original](qiumingdll_winsplit_show_original.md)
- [qiumingdll_winsplit_create](qiumingdll_winsplit_create.md)
- [qiumingdll_winsplit_cleanup](qiumingdll_winsplit_cleanup.md)
