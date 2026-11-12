# qiumingdll_keeplive_init()

Install the "window keep-alive" message hook so the target window is not judged "not responding" by the system and closed or cleaned up; used for fullscreen / not-responding protection in web games.

## Signature

```gml
qiumingdll_keeplive_init()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no GML parameters. The wrapper automatically passes the main game window handle `window_handle()` to the DLL, so the target window is the game's main window |

## Returns

| Value | Description |
|----|------|
| `0` | Success: the keep-alive hook has been installed for the target window |
| `1` | Failure: the window handle passed in is invalid, or the thread owning the target window cannot be obtained. **Non-Windows platforms**: the wrapper returns immediately and has no effect (in practice no valid value is returned; handle Windows scenarios only) |

## Usage

- Prerequisite: none; it only takes effect on Windows, and it is usually recommended to call it after the game's main window has been created (for example in an object's Create event or a Room Start event).
- Platform limitation: Windows only. The hook is bound to the thread owning the game's main window and processes that window's message pump.
- Keep-alive mechanism: the hook intercepts some messages of the target window (such as WM_PAINT, WM_ERASEBKGND, WM_SETCURSOR) for special handling and swallows the system menu / titlebar close command (WM_SYSCOMMAND SC_CLOSE), preventing the window from being judged "not responding" and terminated because it has not responded to user actions for a long time. Typical scenario: a web game (with WebView) entering fullscreen, staying idle for a long time, or the main thread being busy — prevents Windows from showing the "not responding" prompt and closing it.
- Repeated calls: calling again reinstalls the hook (installing repeatedly on the same window is safe, but calling cleanup before init is preferred).
- Call qiumingdll_keeplive_cleanup() to uninstall the hook before exiting the game; when the game is closed, the hook becomes invalid automatically after the window is destroyed.
- Side effect: while keep-alive is active, close requests sent by the system to the target window may be swallowed, so when the player uses Alt+F4 / the titlebar to close the game, make sure your game logic provides its own exit path.

## Example

```gml
/// Create event (obj_keeplive_manager)
// Enable keep-alive after the game's main window is created
var r = qiumingdll_keeplive_init();
if (r == 0)
{
    keepliveOn = true; // Keep-alive hook installed
}

/// Room End event
// Uninstall the hook before leaving the room or exiting the game
if (keepliveOn)
{
    qiumingdll_keeplive_cleanup();
    keepliveOn = false;
}

/// Draw GUI event (debug display)
if (qiumingdll_keeplive_is_active() == 1)
{
    draw_text(10, 10, "Window keep-alive: enabled");
}
else
{
    draw_text(10, 10, "Window keep-alive: disabled");
}
```

## Related functions

- [qiumingdll_keeplive_cleanup](qiumingdll_keeplive_cleanup.md)
- [qiumingdll_keeplive_is_active](qiumingdll_keeplive_is_active.md)
