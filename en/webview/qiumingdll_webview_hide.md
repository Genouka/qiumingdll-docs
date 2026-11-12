# qiumingdll_webview_hide(webviewId)

Hide the given WebView window (page and script state are preserved).

## Signature

```gml
qiumingdll_webview_hide(webviewId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | real | yes | WebView id, range 1 ~ 16 |

## Returns

| Value | Description |
|----|------|
| `1` | Hidden successfully |
| `0` | Failure: invalid id, or no active WebView for that id |
| `0` | Non-Windows platforms: the GML wrapper returns 0 directly |

## Usage

- Prerequisite: the WebView has been created (create / create_child).
- Hiding only makes the window invisible: page content, JS state and browsing history are all preserved, and show can restore it at any time.
- While hidden, the page may still run in the background (timers, requests, etc.); to stop it completely, use stop or navigate to something like `about:blank`.
- Works for both standalone windows and child windows; after a child window is hidden, the corresponding area of the game no longer displays page content.
- Hiding does not destroy the window: `exists(id)` still returns 1 and `get_count()` does not change.

## Example

```gml
/// Create event (obj_browser)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create_child(50, 50, 500, 300);
isVisible = true;

/// Key press event (keyboard H)
if (keyboard_check_pressed(ord("H")))
{
    if (isVisible)
    {
        qiumingdll_webview_hide(webviewId);
        isVisible = false;
        show_debug_message("Browser hidden (page is still alive)");
    }
    else
    {
        qiumingdll_webview_show(webviewId);
        isVisible = true;
    }
}

/// Room end event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_show](qiumingdll_webview_show.md)
- [qiumingdll_webview_destroy](qiumingdll_webview_destroy.md)
- [qiumingdll_webview_set_opacity](qiumingdll_webview_set_opacity.md)
