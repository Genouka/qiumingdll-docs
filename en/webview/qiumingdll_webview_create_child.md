# qiumingdll_webview_create_child(x, y, w, h)

Creates an embedded child-window browser (no title bar) inside the game main window's client area and returns the WebView's id.

## Signature

```gml
qiumingdll_webview_create_child(x, y, w, h)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| x | Real | Yes | X coordinate of the child window's top-left corner relative to the **main window client area** (client-area coordinate system, origin at the main window client area's top-left corner; negative offsets are allowed), in pixels |
| y | Real | Yes | Y coordinate of the child window's top-left corner relative to the main window client area, in pixels |
| w | Real | Yes | Child window client-area width, in pixels |
| h | Real | Yes | Child window client-area height, in pixels |

## Returns

| Value | Description |
|----|------|
| 1 ~ 16 | Creation succeeded; returns webviewId (allocated from 1 upward, reusable) |
| 0 | Creation failed. Possible reasons: not initialized, initialization failed, invalid main window handle, the 16-WebView limit reached, insufficient system resources |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Precondition: qiumingdll_webview_init() must be called first and return 0; the child window is embedded in the main game window's client area recorded at init time.
- Platform support: Windows only; requires the installed WebView2 Runtime.
- Difference from create: the child window **has no title bar**, therefore:
  - It cannot be closed via the system menu (closable is fixed at false); only the game can destroy it with destroy / destroy_all;
  - It is not topmost (topmost has no effect);
  - It is not draggable (draggable is always false; set_draggable has no effect on it);
  - It moves and resizes together with the game main window: when the main window moves, the child window follows automatically; when the main window is destroyed, the child window is destroyed automatically too.
- Coordinates are always relative to the main window client area: the x, y passed to create_child / set_position / set_region are client-area coordinates; positions queried with `get_info(id, 0/1)` are also converted to client-area coordinates.
- Page loading is likewise asynchronous: after create, wait until `get_is_active(id) == 1` (or `get_info(id, 4) == 1`) before calling navigate and similar functions.
- To make the child window automatically fill the game client area and adjust as the window size changes, call `resize_to_parent(id)`.

## Example

```gml
/// Create event (obj_ingame_browser)
qiumingdll_webview_init();  // Assume it returns 0

// Embed a browser in the game view, starting at 400x300
webviewId = qiumingdll_webview_create_child(40, 200, 400, 300);
if (webviewId > 0)
{
    qiumingdll_webview_set_title(webviewId, "");  // Child windows have no title bar; this call has no effect
    state = "waiting";
}

/// Step event
if (state == "waiting" && qiumingdll_webview_get_is_active(webviewId) == 1)
{
    state = "loaded";
    // Render a local page directly from an HTML string
    qiumingdll_webview_navigate_to_string(webviewId, "<h1>Hello, WebView</h1><p>This is a browser embedded in the game window.</p>");
    // Fill the whole game client area and adjust automatically as the window size changes
    qiumingdll_webview_resize_to_parent(webviewId);
}

/// Key press event (ESC)
if (keyboard_check_pressed(vk_escape))
{
    qiumingdll_webview_hide(webviewId);       // Hide the browser (not destroyed; can be shown again)
}

/// Room End event
qiumingdll_webview_destroy_all();   // The main window cleans up automatically; destroying explicitly here is safer
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_init](qiumingdll_webview_init.md)
- [qiumingdll_webview_create](qiumingdll_webview_create.md)
- [qiumingdll_webview_resize_to_parent](qiumingdll_webview_resize_to_parent.md)
- [qiumingdll_webview_is_child](qiumingdll_webview_is_child.md)
- [qiumingdll_webview_navigate_to_string](qiumingdll_webview_navigate_to_string.md)
