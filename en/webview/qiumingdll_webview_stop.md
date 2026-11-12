# qiumingdll_webview_stop(webviewId)

Stop the page load currently in progress in the specified WebView.

## Signature

```gml
qiumingdll_webview_stop(webviewId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | yes | WebView id, range 1 ~ 16 |

## Returns

| Value | Description |
|----|------|
| 1 | Stop request submitted |
| 0 | Call failed: invalid id, the WebView does not exist, or it is not ready yet |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Precondition: the WebView is ready.
- Equivalent to the browser's "stop loading" (Esc): aborts the current navigation request and the page stays at the previously loaded content; if the first load is stopped, the page shows blank or an error page.
- Common uses: the user skips loading, load timeout protection (together with a timer), cleaning up network resources.
- To start loading again after stopping, navigate again with navigate (reload reloads the current document).
- Asynchronous: a return value of 1 only means the request was submitted.

## Example

```gml
/// Create event (obj_webview_timeout)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(100, 100, 800, 600);
loadingTicks = 0;
loadStarted = false;

/// Step event
// Start loading a test page once ready
if (qiumingdll_webview_get_is_active(webviewId) == 1 && !loadStarted)
{
    loadStarted = true;
    qiumingdll_webview_navigate(webviewId, "https://example.com/slow_page");
}

// Load timeout protection: stop if completion is not confirmed after 300 frames (5 seconds)
if (loadStarted && loadingTicks < 900)
{
    loadingTicks++;
    if (loadingTicks == 300)
    {
        qiumingdll_webview_stop(webviewId);
        show_debug_message("Load timed out, stopped");
        qiumingdll_webview_navigate_to_string(webviewId,
            "<html><body style='text-align:center;padding-top:40%'>Load timed out, please try again</body></html>");
        loadingTicks = 900;  // Do not trigger again
    }
}

/// Room end event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_reload](qiumingdll_webview_reload.md)
- [qiumingdll_webview_navigate](qiumingdll_webview_navigate.md)
- [qiumingdll_webview_go_back](qiumingdll_webview_go_back.md)
