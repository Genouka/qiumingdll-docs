# qiumingdll_webview_navigate(webviewId, url)

Navigate the given WebView to the specified URL, loading the page asynchronously.

## Signature

```gml
qiumingdll_webview_navigate(webviewId, url)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | real | yes | WebView id, range 1 ~ 16 |
| url | string | yes | URL to open; it **must include a protocol prefix**, e.g. `"https://example.com"`, `"http://127.0.0.1:8080/page"`, `"file:///C:/..."`. A URL without a protocol (such as `"example.com"`) cannot be resolved correctly |

## Returns

| Value | Description |
|----|------|
| `1` | Navigation request submitted successfully (note: whether the page actually finished loading must be observed separately; the DLL provides no load-completion notification) |
| `0` | Failure: invalid id, the WebView does not exist, or the WebView is not ready yet (most likely right after create) |
| `0` | Non-Windows platforms: the GML wrapper returns 0 directly |

## Usage

- Prerequisite: the WebView must be created and **ready**. Page creation is asynchronous: after create / create_child returns you must wait until `get_is_active(id) == 1` (or `get_info(id, 4) == 1`) before navigate can succeed, otherwise it returns 0.
- URL length is capped at roughly 2000 characters (fixed internal buffer).
- URLs may contain non-ASCII characters such as Chinese (converted to UTF-8 internally).
- Navigation is asynchronous: a return value of 1 only means the request was issued. Whether the page finishes loading, and whether it succeeds, **cannot** be observed through any callback; if needed, poll the page state with a script, e.g. `execute_script(id, "document.readyState")` (note that it returns no result), or periodically check WebView readiness with `get_info(id, 4)`.
- Only after the page has finished loading can execute_script reliably manipulate the DOM; running it too early does nothing because the page is not loaded yet.
- Repeated navigate calls replace the current page and add new browsing history entries (usable by go_back / go_forward).

## Example

```gml
/// Create event (obj_browser)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(100, 100, 800, 600);
state = "waiting";

/// Step event
switch (state)
{
case "waiting":
    // Wait for the WebView to become ready
    if (qiumingdll_webview_get_is_active(webviewId) == 1)
    {
        state = "navigating";
        var ok = qiumingdll_webview_navigate(webviewId, "https://example.com");
        show_debug_message("navigate submit result = " + string(ok));
        tick = 0;
    }
    break;

case "navigating":
    // For simplicity, wait a fixed time for the page to load (a real project could poll via execute_script)
    tick++;
    if (tick > 120)
    {
        state = "loaded";
        // Run a script after the page has loaded
        qiumingdll_webview_execute_script(webviewId,
            "document.title = 'Loaded'; document.body.style.background = '#333';");
    }
    break;
}

/// Room end event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_navigate_to_string](qiumingdll_webview_navigate_to_string.md)
- [qiumingdll_webview_get_is_active](qiumingdll_webview_get_is_active.md)
- [qiumingdll_webview_execute_script](qiumingdll_webview_execute_script.md)
- [qiumingdll_webview_reload](qiumingdll_webview_reload.md)
- [qiumingdll_webview_stop](qiumingdll_webview_stop.md)
