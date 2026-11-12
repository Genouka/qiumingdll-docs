# qiumingdll_webview_clear_resize_to_parent(webviewId)

Cancels the "automatically fill the main window's client area" effect set by `qiumingdll_webview_resize_to_parent`. After cancelling, the child window keeps its current position and size and no longer follows when the main window is stretched/resized.

## Signature

```gml
qiumingdll_webview_clear_resize_to_parent(webviewId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | Yes | WebView id, range 1 ~ 16 |

## Returns

| Value | Description |
|----|------|
| 1 | Call succeeded (returns 1 even if this WebView never had auto-fill enabled; the function is idempotent) |
| 0 | Call failed: invalid id or the WebView does not exist |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Only affects the `resize_to_parent` follow flag; it **does not change** the child window's current position or size.
- If you afterwards want to keep following with a custom rectangle, use `qiumingdll_webview_set_auto_resize_9patch`.
- To do "cancel following + move to a given rectangle" in one step, call `qiumingdll_webview_resize` directly.
- The follow capability is released automatically on cleanup / main-window destruction, so you do not need to call this function manually.

## Example

```gml
/// The player presses ESC to leave "fullscreen embedded" mode and switch to a fixed small window
if (fullscreen_mode && keyboard_check_pressed(vk_escape))
{
    qiumingdll_webview_clear_resize_to_parent(webviewId);
    qiumingdll_webview_set_region(webviewId, 40, 40, 480, 320);
    fullscreen_mode = false;
}
```

## Related functions

- [qiumingdll_webview_resize_to_parent](qiumingdll_webview_resize_to_parent.md)
- [qiumingdll_webview_resize](qiumingdll_webview_resize.md)
- [qiumingdll_webview_set_auto_resize_9patch](qiumingdll_webview_set_auto_resize_9patch.md)
