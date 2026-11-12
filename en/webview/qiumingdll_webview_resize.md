# qiumingdll_webview_resize(webviewId, x, y, w, h)

Cancel all automatic following for the WebView (`resize_to_parent` and `set_auto_resize_9patch`) and resize the window to a custom rectangle in one shot. Later changes to the main window will no longer adjust it automatically.

## Signature

```gml
qiumingdll_webview_resize(webviewId, x, y, w, h)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | yes | WebView id, range 1 ~ 16 |
| x | Real | yes | New X position. Child windows use client-area coordinates; standalone windows use screen coordinates |
| y | Real | yes | New Y position. Child windows use client-area coordinates; standalone windows use screen coordinates |
| w | Real | yes | New client area width (values below 1 are clamped to 1) |
| h | Real | yes | New client area height (values below 1 are clamped to 1) |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully: automatic following cancelled and the new rectangle applied |
| 0 | Call failed: invalid id, or the WebView does not exist |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Difference from `set_region`: this function **also cancels** `resize_to_parent` / 9-patch automatic following, which suits switching from a fullscreen embed to a fixed layout; `set_region` does not cancel following.
- For standalone windows, x/y are screen coordinates and the size is the client area (titlebar and border are compensated automatically).

## Example

```gml
/// Switch from a fullscreen embed to a fixed-size panel in the bottom-right corner
qiumingdll_webview_resize(webviewId,
    window_get_width() - 420, window_get_height() - 280,
    400, 260);
```

## Related functions

- [qiumingdll_webview_set_region](qiumingdll_webview_set_region.md)
- [qiumingdll_webview_clear_resize_to_parent](qiumingdll_webview_clear_resize_to_parent.md)
- [qiumingdll_webview_set_auto_resize_9patch](qiumingdll_webview_set_auto_resize_9patch.md)
