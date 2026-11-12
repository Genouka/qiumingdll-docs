# qiumingdll_webview_clear_auto_resize_9patch(webviewId)

Cancels the 9-Patch auto-follow set by `qiumingdll_webview_set_auto_resize_9patch`. After cancelling, the child window keeps its current position and size and no longer adjusts automatically when the main window is resized.

## Signature

```gml
qiumingdll_webview_clear_auto_resize_9patch(webviewId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | Yes | WebView id, range 1 ~ 16 |

## Returns

| Value | Description |
|----|------|
| 1 | Call succeeded (returns 1 even if this WebView never had 9-Patch following enabled; the function is idempotent) |
| 0 | Call failed: invalid id or the WebView does not exist |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Only clears the 9-Patch follow flag; it does not change the window's current position or size.
- Difference from `qiumingdll_webview_clear_resize_to_parent`: the latter only cancels the "fill the client area" following; this function only cancels 9-Patch following. The two are mutually exclusive — at most one can be active at a time.
- After cancelling you can call `qiumingdll_webview_set_auto_resize_9patch` again at any time to establish a new layout baseline.
- If you want to "cancel following and immediately move/resize to a given rectangle" in one step, use `qiumingdll_webview_resize` directly.

## Example

```gml
/// Leave the adaptive layout and stay fixed at the current position
qiumingdll_webview_clear_auto_resize_9patch(webviewId);
```

## Related functions

- [qiumingdll_webview_set_auto_resize_9patch](qiumingdll_webview_set_auto_resize_9patch.md)
- [qiumingdll_webview_resize](qiumingdll_webview_resize.md)
- [qiumingdll_webview_clear_resize_to_parent](qiumingdll_webview_clear_resize_to_parent.md)
