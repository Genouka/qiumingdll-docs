# qiumingdll_webview_reload(webviewId)

Reload the current page of the given WebView (equivalent to the browser's refresh).

## Signature

```gml
qiumingdll_webview_reload(webviewId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | real | yes | WebView id, range 1 ~ 16 |

## Returns

| Value | Description |
|----|------|
| `1` | Reload request submitted |
| `0` | Failure: invalid id, WebView does not exist, or **not ready yet** |
| `0` | Non-Windows platforms: the GML wrapper returns 0 directly |

## Usage

- Prerequisite: the WebView is ready (after create, wait until `get_is_active(id) == 1`).
- Reloads the current page: same behavior as F5 in a browser; the page is loaded again (HTTP cache policy is decided by Chromium and cached content may be used).
- If the current page was rendered by navigate_to_string, reloading renders the same HTML again.
- Reloading is asynchronous; a return value of 1 only means the request was issued, and completion depends on the network/page complexity.
- To reopen a page after loading was stopped by stop, use this function (or navigate again).

## Example

```gml
/// Create event (obj_webview_news)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(100, 100, 700, 500);

/// Step event
// Load the news page once ready
if (qiumingdll_webview_get_is_active(webviewId) == 1 && !loaded)
{
    loaded = true;
    qiumingdll_webview_navigate(webviewId, "https://example.com/news");
}

// Press R to reload / S to stop loading
if (keyboard_check_pressed(ord("R")))
    qiumingdll_webview_reload(webviewId);

if (keyboard_check_pressed(ord("S")))
    qiumingdll_webview_stop(webviewId);   // Stop the current load

/// Room end event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_stop](qiumingdll_webview_stop.md)
- [qiumingdll_webview_navigate](qiumingdll_webview_navigate.md)
- [qiumingdll_webview_go_back](qiumingdll_webview_go_back.md)
- [qiumingdll_webview_go_forward](qiumingdll_webview_go_forward.md)
