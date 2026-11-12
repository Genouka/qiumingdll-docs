# qiumingdll_disable_system_menu()

Disables the game window's system menu and window operations so players cannot interfere with the game through the system menu.

## Signature

```gml
qiumingdll_disable_system_menu()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters. It obtains the current game window handle (`window_handle()`) internally |

## Returns

| Value | Description |
|----|------|
| 1 | Disabled successfully (the window handle is valid and the intercepting subclass is installed) |
| 0 | Invalid window: the handle obtained is not a valid window |
| (no return value) | Called on a non-Windows platform: no operation, no return value |

## Usage

- Prerequisite: call `qiumingdll_init()` first on Windows.
- Platform limit: Windows only; no effect on other platforms.
- Behavior: installs a window subclass on the game window that intercepts and swallows a series of system operations, including:
  - `Alt+Space` opening the window system menu, and Enter triggering the system menu;
  - the system menu opened by right-clicking the title bar;
  - the taskbar context menu (SC_TASKLIST);
  - dragging the title bar with the mouse to move the window;
  - double-clicking the title bar to maximize / restore;
  - right-click / middle-click menus in the non-client area (title bar, borders).
  The window itself is not changed to borderless; only these system interactions are blocked.
- Use together with `qiumingdll_restore_system_menu()`: after calling the restore function, all of the above system interactions are restored.
- Note: the effect applies to the current game window; the subclass is removed automatically when the window is destroyed, so no manual cleanup is needed.
- Recommended together with `qiumingdll_fixflash()` at startup for a "clean" game window experience.

## Example

```gml
// Lock the window after a fullscreen game starts: no dragging, no system menu
qiumingdll_init();
qiumingdll_fixflash();

var r = qiumingdll_disable_system_menu();
if (r == 1)
{
    show_debug_message("System menu disabled");
}
```

## Related functions

- [qiumingdll_restore_system_menu](qiumingdll_restore_system_menu.md)
- [qiumingdll_fixflash](qiumingdll_fixflash.md)
- [qiumingdll_init](qiumingdll_init.md)
