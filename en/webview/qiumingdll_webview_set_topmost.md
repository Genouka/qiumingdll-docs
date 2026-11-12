# qiumingdll_webview_set_topmost(webviewId, topmost)

Set whether the specified WebView **standalone window** stays on top (above all other windows).

## Signature

```gml
qiumingdll_webview_set_topmost(webviewId, topmost)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | yes | WebView id, range 1 ~ 16 |
| topmost | Real | yes | Boolean switch: 1 (or any non-zero value) = always on top, 0 = cancel topmost (default) |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Call failed: invalid id, or there is no active WebView with that id |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Precondition: the WebView has been created (normally used with standalone windows created by create).
- When topmost, the window is always displayed above other normal windows (including the game's main window), which suits "announcement pop-ups", "forced prompts", "recording subtitles" and similar scenarios.
- Pass 0 to cancel topmost and restore the normal level.
- **No effect on child windows**: child windows are embedded in the main window's client area, so this setting is meaningless for them.
- Topmost is guaranteed by the system; when another application switches to fullscreen it may be restricted by system policy, which is normal behavior.

## Example

```gml
/// Create event (obj_webview_alert)
qiumingdll_webview_init();
alertId = qiumingdll_webview_create(400, 200, 480, 260);
qiumingdll_webview_navigate_to_string(alertId,
    "<html><body style='padding:40px;text-align:center'>" +
    "<h2>System Notice</h2><p>Maintenance starts in 5 minutes</p></body></html>");
isTopmost = false;

/// Step event
// Press T to toggle the topmost state
if (keyboard_check_pressed(ord("T")))
{
    isTopmost = !isTopmost;
    qiumingdll_webview_set_topmost(alertId, isTopmost ? 1 : 0);
}

/// Room end event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_create](qiumingdll_webview_create.md)
- [qiumingdll_webview_set_draggable](qiumingdll_webview_set_draggable.md)
- [qiumingdll_webview_set_closable](qiumingdll_webview_set_closable.md)
