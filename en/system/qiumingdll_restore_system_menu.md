# qiumingdll_restore_system_menu()

Restores the game window's system menu and window operations, undoing the interception installed earlier by `qiumingdll_disable_system_menu()`.

## Signature

```gml
qiumingdll_restore_system_menu()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters. It obtains the current game window handle (`window_handle()`) internally |

## Returns

| Value | Description |
|----|------|
| 1 | Restored successfully (the window handle is valid and the intercepting subclass has been removed) |
| 0 | Invalid window, or no intercepting subclass is currently installed |
| (no return value) | Called on a non-Windows platform: no operation, no return value |

## Usage

- Prerequisite: call `qiumingdll_init()` first on Windows.
- Platform support: Windows only; no effect on other platforms.
- Behavior: internally removes from the game window the window subclass installed by `qiumingdll_disable_system_menu()`, after which all of the following are restored:
  - `Alt+Space` opening the system menu, and Enter triggering the system menu;
  - right-clicking the title bar, and the taskbar context menu;
  - dragging the title bar with the mouse to move the window;
  - double-clicking the title bar to maximize / restore;
  - right-click / middle-click menus in the non-client area.
- Calling this function without having called `qiumingdll_disable_system_menu()` first is a safe no-op: it returns 0 and has no effect.
- Use case: the game switches between a locked-window mode and a draggable mode (for example a "lock window" toggle in the settings screen).
- Note: the interception stops working automatically when the game window is destroyed, so this function neither needs nor should be called then.

## Example

```gml
// The "lock window" toggle in the settings screen
qiumingdll_init();

window_locked = false;

if (keyboard_check_pressed(vk_f9))
{
    if (window_locked)
    {
        // Unlock: restore the system menu and window operations
        qiumingdll_restore_system_menu();
        window_locked = false;
    }
    else
    {
        // Lock: disable the system menu and window operations
        qiumingdll_disable_system_menu();
        window_locked = true;
    }
}
```

## Related functions

- [qiumingdll_disable_system_menu](qiumingdll_disable_system_menu.md)
- [qiumingdll_init](qiumingdll_init.md)
