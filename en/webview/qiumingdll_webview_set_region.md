# qiumingdll_webview_set_region(webviewId, x, y, w, h)

Set the position and size of the specified WebView window at the same time.

## Signature

```gml
qiumingdll_webview_set_region(webviewId, x, y, w, h)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | yes | WebView id, range 1 ~ 16 |
| x | Real | yes | Target X coordinate in pixels. For **standalone windows** it is a screen coordinate; for **child windows** it is relative to the main window's client area |
| y | Real | yes | Target Y coordinate in pixels, same coordinate system as x |
| w | Real | yes | Client area width in pixels |
| h | Real | yes | Client area height in pixels |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Call failed: invalid id, or there is no active WebView with that id |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Equivalent to calling set_position(id, x, y) and then set_size(id, w, h), but both take effect in a single call (no intermediate state).
- Precondition: the WebView has been created. Does not require the WebView to be ready.
- For standalone windows, w / h are the client area size; the actual outer frame automatically adds the title bar size. For child windows, w / h are exactly the window size.
- Suited to whole-layout adjustments (e.g. adapting to resolution changes, popping up small windows).
- Pass reasonable positive sizes; otherwise the window may become invisible or misbehave.

## Example

```gml
/// Create event (obj_webview_popup)
qiumingdll_webview_init();
mainId = qiumingdll_webview_create_child(0, 0, 800, 600);
popupId = qiumingdll_webview_create(500, 300, 300, 200);
popupVisible = true;

/// Step event
// Demo: press P to pop the animated "small window" out in the center, press P again to tuck it back into the bottom-right corner
if (keyboard_check_pressed(ord("P")))
{
    if (popupVisible)
    {
        // Tuck it into the bottom-right corner of the screen and shrink it
        qiumingdll_webview_set_region(popupId, 1200, 700, 300, 200);
    }
    else
    {
        // Move it to the center of the screen and enlarge it
        qiumingdll_webview_set_region(popupId, 400, 200, 640, 480);
    }
    popupVisible = !popupVisible;
}

/// Room end event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_set_position](qiumingdll_webview_set_position.md)
- [qiumingdll_webview_set_size](qiumingdll_webview_set_size.md)
- [qiumingdll_webview_resize_to_parent](qiumingdll_webview_resize_to_parent.md)
