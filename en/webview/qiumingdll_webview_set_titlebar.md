# qiumingdll_webview_set_titlebar(webviewId, hasTitleBar)

Toggle whether the specified WebView window has a system title bar (used for the "borderless" mode of standalone windows).

## Signature

```gml
qiumingdll_webview_set_titlebar(webviewId, hasTitleBar)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | yes | WebView id, range 1 ~ 16 |
| hasTitleBar | Real | yes | Boolean switch: 1 (non-zero) = show the title bar, 0 = hide the title bar (borderless) |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully (also returns 1 if the state did not change) |
| 0 | Call failed: invalid id, or there is no active WebView with that id |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Precondition: the WebView has been created; mainly used for standalone windows created with create.
- After hiding the title bar the window becomes a borderless "content window"; combined with `set_draggable(id, 1)` you can build a custom-looking window (e.g. a game-drawn border plus drag bar).
- Toggling the title bar **rebuilds the window style and adjusts the outer frame size**: the client area size stays unchanged, but the outer window changes; the window position stays at the screen position corresponding to the top-left of the client area (visually the top-left corner does not move).
- Without a title bar the system menu and close button disappear. To close, use `set_closable` together with an in-game button/hotkey that calls destroy, or call `destroy(id)` directly.
- Meaningless for child windows (child windows never have a title bar); the call returns 1 but has no effect.

## Example

```gml
/// Create event (obj_custom_win)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(300, 150, 500, 400);
borderless = false;

// First load a page that draws its own "border"
// (once ready):
/// Step event
if (!borderless && qiumingdll_webview_get_is_active(webviewId) == 1)
{
    borderless = true;
    // Hide the system title bar to become a borderless window
    qiumingdll_webview_set_titlebar(webviewId, 0);
    // Allow dragging by holding anywhere in the window
    qiumingdll_webview_set_draggable(webviewId, 1);
    qiumingdll_webview_navigate_to_string(webviewId,
        "<html><body style='margin:0;background:#2b2b2b'>" +
        "<div id='bar' style='height:32px;background:#444;color:#fff;line-height:32px;text-align:center'>" +
        "Custom window</div></body></html>");
}

/// Room end event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_set_title](qiumingdll_webview_set_title.md)
- [qiumingdll_webview_set_draggable](qiumingdll_webview_set_draggable.md)
- [qiumingdll_webview_set_closable](qiumingdll_webview_set_closable.md)
