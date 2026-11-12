# qiumingdll_webview_set_size(webviewId, w, h)

Set the client area size of the specified WebView window (without changing its position).

## Signature

```gml
qiumingdll_webview_set_size(webviewId, w, h)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | yes | WebView id, range 1 ~ 16 |
| w | Real | yes | Client area width in pixels (the actual width of the content area) |
| h | Real | yes | Client area height in pixels |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Call failed: invalid id, or there is no active WebView with that id |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Precondition: the WebView has been created. Does not require the WebView to be ready.
- The passed w / h refer to the **client area** (page content area) size; standalone windows also have a title bar, so the actual outer window is slightly larger (the title bar height is decided by the system; the outer frame size is converted internally).
- Child windows have no title bar, so w / h are exactly the window size.
- Page content reflows as the window is resized (equivalent to stretching a browser window).
- Changes size only, not position: the position stays unchanged; to set both position and size, use set_region.
- A size of 0 or a negative value makes the window invisible/abnormal; pass reasonable positive values.

## Example

```gml
/// Create event (obj_video_player)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(100, 100, 640, 360);

/// Step event
// Demo: press 1/2/3 to switch the display size
if (keyboard_check_pressed(ord("1")))
    qiumingdll_webview_set_size(webviewId, 640, 360);
else if (keyboard_check_pressed(ord("2")))
    qiumingdll_webview_set_size(webviewId, 1280, 720);
else if (keyboard_check_pressed(ord("3")))
    qiumingdll_webview_set_size(webviewId, 320, 180);

// Read the current client area size
if (keyboard_check_pressed(ord("S")))
{
    var w = qiumingdll_webview_get_info(webviewId, 2);  // client area width
    var h = qiumingdll_webview_get_info(webviewId, 3);  // client area height
    show_debug_message("Current client area: " + string(w) + " x " + string(h));
}

/// Room end event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_set_position](qiumingdll_webview_set_position.md)
- [qiumingdll_webview_set_region](qiumingdll_webview_set_region.md)
- [qiumingdll_webview_get_info](qiumingdll_webview_get_info.md)
