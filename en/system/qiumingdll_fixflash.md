# qiumingdll_fixflash()

Fixes game window flicker by clearing the background brush of the window class, eliminating flicker during window repaints.

## Signature

```gml
qiumingdll_fixflash()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters. It obtains the current game window handle (`window_handle()`) internally, so the window cannot and need not be specified manually |

## Returns

| Value | Description |
|----|------|
| 0 | Fixed successfully (the window handle is valid and the background brush has been cleared) |
| 1 | Invalid window: the handle obtained is not a valid window, and nothing was changed |
| (no return value) | Called on a non-Windows platform: no operation, no return value |

## Usage

- Prerequisite: call `qiumingdll_init()` first on Windows.
- Platform limit: Windows only; no effect on other platforms.
- Behavior: internally clears the background brush (`GCLP_HBRBACKGROUND`) of the window class the game window belongs to, so Windows no longer paints a gray background before drawing the game frame, eliminating flicker when switching windows, resizing, and similar cases.
- Note: the change applies to the whole window class and stays in effect for the lifetime of the game; since a GameMaker game normally has exactly one instance of its window class, restoring it is generally unnecessary.
- Call it once after the game window has been created (e.g. in the `game_start` event); calling it repeatedly brings no additional benefit.
- It does not conflict with other system functions and can be used together with `qiumingdll_disable_system_menu()` and similar functions.

## Example

```gml
// Fix window flicker when the game starts
qiumingdll_init();

var r = qiumingdll_fixflash();
if (r == 0)
{
    show_debug_message("Window flicker fixed");
}
else
{
    show_debug_message("Fix failed: invalid window (returned 1)");
}
```

## Related functions

- [qiumingdll_init](qiumingdll_init.md)
- [qiumingdll_disable_system_menu](qiumingdll_disable_system_menu.md)
- [qiumingdll_restore_system_menu](qiumingdll_restore_system_menu.md)
