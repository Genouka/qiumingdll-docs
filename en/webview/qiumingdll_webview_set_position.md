# qiumingdll_webview_set_position(webviewId, x, y)

Set the position of the specified WebView window (without changing its size).

## Signature

```gml
qiumingdll_webview_set_position(webviewId, x, y)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | yes | WebView id, range 1 ~ 16 |
| x | Real | yes | Target X coordinate in pixels. **Standalone window**: screen coordinates (origin at the top-left of the screen); **child window**: relative to the main window's client area (origin at the top-left of the main window's client area) |
| y | Real | yes | Target Y coordinate in pixels, same coordinate system as above |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Call failed: invalid id, or there is no active WebView with that id |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Precondition: the WebView has been created. This function does not require the WebView to be ready (the window can be moved whether it is ready or not).
- Changes position only, not size; to change both position and size, use set_region.
- Coordinates are rounded (Reals are truncated to integer pixels).
- Standalone window: coordinates are screen coordinates; read the current screen position back with `get_info(id, 0/1)`.
- Child window: coordinates are relative to the main window's client area; child windows follow automatically when the main window moves, so no manual reset is normally needed after setting them.
- Also works while a page is still loading; moving does not interrupt navigation.

## Example

```gml
/// Create event (obj_webview_ui)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create_child(0, 0, 400, 300);
// Place the login UI on the right side of the client area
qiumingdll_webview_set_position(webviewId, 400, 100);

/// Step event
// Demo: fine-tune the position with the arrow keys
if (keyboard_check(vk_right)) qiumingdll_webview_set_position(webviewId, pos_x + 2, pos_y);
if (keyboard_check(vk_left))  qiumingdll_webview_set_position(webviewId, pos_x - 2, pos_y);

/// Room end event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_set_size](qiumingdll_webview_set_size.md)
- [qiumingdll_webview_set_region](qiumingdll_webview_set_region.md)
- [qiumingdll_webview_get_info](qiumingdll_webview_get_info.md)
- [qiumingdll_webview_create](qiumingdll_webview_create.md)
