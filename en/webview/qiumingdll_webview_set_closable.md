# qiumingdll_webview_set_closable(webviewId, closable)

Control whether the specified WebView standalone window may be closed by the user (via the titlebar close button / Alt+F4).

## Signature

```gml
qiumingdll_webview_set_closable(webviewId, closable)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | yes | WebView id, range 1 ~ 16 |
| closable | Real | yes | Boolean switch: 1 (non-zero) = the user may close it (default), 0 = the user may not close it |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Call failed: invalid id, or there is no active WebView with that id |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Precondition: the WebView has been created; mainly affects standalone windows (created by create).
- The two ways to close:
  - The X button in the system menu / titlebar: disabled when `closable=0` (the system menu item is greyed out) and WM_CLOSE is intercepted;
  - `destroy(id)` / `destroy_all()`: **unaffected by this setting**; the game can always destroy the window.
- With `closable=0`, Alt+F4 has no effect either (prevents accidentally closing the window/game).
- Meaningless for child windows: a child window can never be closed by the user, only destroyed by the game.
- Works together with set_close_triggers_main: with closable=1, whether the user closing the window also closes the game main window is decided by close_triggers_main.

## Example

```gml
/// Create event (obj_webview_lock)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(400, 200, 480, 320);
qiumingdll_webview_navigate(webviewId, "https://example.com");

// Closable by default; pressing L locks it so the user cannot click X to close
locked = false;

/// Step event
if (keyboard_check_pressed(ord("L")))
{
    locked = !locked;
    qiumingdll_webview_set_closable(webviewId, locked ? 0 : 1);
    show_debug_message(locked ? "Window locked (cannot close)" : "Window unlocked");
}

/// Room end event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_set_close_triggers_main](qiumingdll_webview_set_close_triggers_main.md)
- [qiumingdll_webview_destroy](qiumingdll_webview_destroy.md)
- [qiumingdll_webview_set_titlebar](qiumingdll_webview_set_titlebar.md)
