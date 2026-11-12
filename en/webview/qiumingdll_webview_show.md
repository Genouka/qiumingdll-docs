# qiumingdll_webview_show(webviewId)

Show the specified WebView window (undo the hidden state).

## Signature

```gml
qiumingdll_webview_show(webviewId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | yes | WebView id, range 1 ~ 16 |

## Returns

| Value | Description |
|----|------|
| 1 | Shown successfully |
| 0 | Call failed: invalid id, or there is no active WebView with that id |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Precondition: the WebView has been created (create / create_child).
- Used as a pair with hide: after hiding, call this function to show the window again; page content and JS state **are not lost** (hiding only makes it invisible).
- Newly created windows are shown by default; only call show to restore a window that was previously hidden with hide (or hidden by other means).
- Works for both standalone windows and child windows.
- Showing/hiding affects visibility only, not page loading or script execution (while hidden the page keeps running in the background and can still be navigated).

## Example

```gml
/// Create event (obj_browser)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(200, 100, 640, 480);
qiumingdll_webview_navigate(webviewId, "https://example.com");
visible = true;

/// Key press event (keyboard F1)
if (keyboard_check_pressed(vk_f1))
{
    if (visible)
    {
        qiumingdll_webview_hide(webviewId);   // Hide the browser
        visible = false;
    }
    else
    {
        qiumingdll_webview_show(webviewId);   // Show it again; the page is still there
        visible = true;
    }
}

/// Room end event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_hide](qiumingdll_webview_hide.md)
- [qiumingdll_webview_create](qiumingdll_webview_create.md)
- [qiumingdll_webview_create_child](qiumingdll_webview_create_child.md)
