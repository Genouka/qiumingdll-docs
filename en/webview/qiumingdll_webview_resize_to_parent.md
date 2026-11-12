# qiumingdll_webview_resize_to_parent(webviewId)

Make the specified **child window** browser fill the entire client area of the game main window, and follow automatically when the main window size changes.

## Signature

```gml
qiumingdll_webview_resize_to_parent(webviewId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | yes | WebView id, range 1 ~ 16 (must be a child window created by create_child) |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully: the child window fills the main window client area and follows main window size changes automatically |
| 0 | Call failed: invalid id, the WebView does not exist, it is **not a child window** (calling on a standalone window has no effect), or the main window handle is invalid |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- **Child windows only**: only windows created by create_child can call this; calling it on a standalone window created by create returns 0.
- After the call the child window position is reset to (0, 0) (top-left of the client area) and its width/height fill the whole main window client area.
- **Automatic following**: once enabled, when the main window is stretched/scaled (including the user resizing the window and resolution changes), the child window refills the client area automatically; no resize event handling is needed on the GML side.
- This following behaviour is removed automatically on cleanup / main window destruction; no manual disabling required.
- Suited to a "fullscreen embedded page": the game screen becomes the browser page, and the window goes fullscreen with the main window size.
- If you later need to control position and size manually, call set_position / set_region / set_size before changing the layout (those calls do not cancel automatic following; later main window changes still refill).

## Example

```gml
/// Create event (obj_fullscreen_browser)
qiumingdll_webview_init();
if (qiumingdll_webview_create_child(0, 0, 320, 240) > 0)
{
    webviewId = qiumingdll_webview_create_child(0, 0, 320, 240);
    started = false;
}

/// Step event
// Once ready, fill the whole game window and load the page
if (!started && qiumingdll_webview_get_is_active(webviewId) == 1)
{
    started = true;
    qiumingdll_webview_resize_to_parent(webviewId);   // Fullscreen embed, follows window resizing automatically
    qiumingdll_webview_navigate(webviewId, "https://example.com");
    // When the player stretches the game window, the page scales along with it; no extra code needed
}

/// Room end event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_create_child](qiumingdll_webview_create_child.md)
- [qiumingdll_webview_is_child](qiumingdll_webview_is_child.md)
- [qiumingdll_webview_set_region](qiumingdll_webview_set_region.md)
- [qiumingdll_webview_set_size](qiumingdll_webview_set_size.md)
