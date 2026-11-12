# qiumingdll_webview_set_zoom_factor(webviewId, zoomFactor)

Set the zoom factor of the specified WebView page.

## Signature

```gml
qiumingdll_webview_set_zoom_factor(webviewId, zoomFactor)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | yes | WebView id, range 1 ~ 16 |
| zoomFactor | Real | yes | Page zoom factor, **1.0 = 100%** normal size; 0.5 = shrunk to 50%, 2.0 = enlarged to 200%. Positive values are recommended (at 0 or a negative value the page becomes invisible). The actual allowed range is decided by WebView2 (roughly 0.25 ~ 5.0); out-of-range values are clamped by the system |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Call failed: invalid id, the WebView does not exist, or the controller has not been created yet (wait until ready) |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Precondition: the WebView has been created and the controller is ready (wait for `get_is_active(id) == 1`).
- Zoom affects page rendering (equivalent to Ctrl+wheel zoom in a browser) and does not affect the window size.
- Effective timing: applies to the current page content immediately, including pages reloaded after zooming.
- Layout impact: zooming in reduces the page's visible area (equivalently, more/less content is visible inside a fixed window), so it is often adjusted together with the window size.
- Valid range: WebView2 supports values roughly between 0.25 and 5.0; common presets between 0.5 and 2.0 are recommended.

## Example

```gml
/// Create event (obj_webview_read)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(100, 100, 800, 600);
zoom = 1.0;

/// Step event
// Load a long document once ready
if (qiumingdll_webview_get_is_active(webviewId) == 1 && !loaded)
{
    loaded = true;
    qiumingdll_webview_navigate_to_string(webviewId,
        "<html><body style='max-width:720px;margin:auto;padding:24px;font-size:16px'>" +
        "<h1>Chapter 1</h1>" + string_repeat("<p>Body paragraph...</p>", 40) +
        "</body></html>");
}

// Zoom control: + / - to adjust, R to reset
if (keyboard_check_pressed(vk_add) || keyboard_check_pressed(vk_numpadadd))
{
    zoom = min(2.0, zoom + 0.25);
    qiumingdll_webview_set_zoom_factor(webviewId, zoom);
}
if (keyboard_check_pressed(vk_subtract) || keyboard_check_pressed(vk_numpadsub))
{
    zoom = max(0.5, zoom - 0.25);
    qiumingdll_webview_set_zoom_factor(webviewId, zoom);
}
if (keyboard_check_pressed(ord("R")))
{
    zoom = 1.0;
    qiumingdll_webview_set_zoom_factor(webviewId, 1.0);
}

/// Room end event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_set_size](qiumingdll_webview_set_size.md)
- [qiumingdll_webview_get_is_active](qiumingdll_webview_get_is_active.md)
- [qiumingdll_webview_navigate_to_string](qiumingdll_webview_navigate_to_string.md)
