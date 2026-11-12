# qiumingdll_webview_navigate_to_string(webviewId, html)

Render a page in the given WebView directly from an HTML string (similar to the effect of `data:text/html`), with no network or local file required.

## Signature

```gml
qiumingdll_webview_navigate_to_string(webviewId, html)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | real | yes | WebView id, range 1 ~ 16 |
| html | string | yes | Complete HTML document string (may start with `<!DOCTYPE html>`); Chinese and UTF-8 are supported. Note that double quotes inside a GML string must be escaped or handled by using single quotes |

## Returns

| Value | Description |
|----|------|
| `1` | HTML render request submitted successfully |
| `0` | Failure: invalid id, WebView does not exist, not ready yet, or converting the HTML string to wide characters failed |
| `0` | Non-Windows platforms: the GML wrapper returns 0 directly |

## Usage

- Prerequisite: the WebView must be created and ready (`get_is_active(id) == 1`; page creation is asynchronous).
- Difference from navigate: navigate requires a real, reachable URL; this function renders the HTML **directly as content**, which suits in-game help pages, leaderboards, dialog boxes and other pure static or pure-JS dynamic pages.
- Relative resource paths inside the HTML cannot be resolved (there is no real URL base); for images/styles, inline them with `data:` URIs or base64 where possible.
- The HTML string may be very long (the buffer is allocated dynamically with no fixed limit, but extremely long documents should be split up or trimmed).
- Rendering is asynchronous too: after the call, give the WebView some time to parse and render before running page scripts.
- execute_script can be used to interact with the rendered page, e.g. read user input or update the UI with JS.

## Example

```gml
/// Create event (obj_webview_help)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create_child(100, 100, 600, 400);
state = "waiting";

/// Step event
if (state == "waiting")
{
    // First wait for the WebView to become ready
    if (qiumingdll_webview_get_info(webviewId, 4) == 1)
    {
        state = "done";
        var html = "<!DOCTYPE html><html><head><meta charset='utf-8'>" +
            "<style>body{font-family:sans-serif;background:#1e1e2e;color:#cdd6f4;padding:20px}" +
            "button{background:#89b4fa;color:#111;border:none;padding:8px 16px;cursor:pointer}</style>" +
            "</head><body><h1>Game Help</h1><p>This is the embedded help document.</p>" +
            "<button id='btn' onclick='count++'>Click me</button>" +
            "<p id='out'>0</p><script>var count=0;" +
            "document.getElementById('btn').onclick=function(){" +
            "document.getElementById('out').textContent=count;}</script></body></html>";
        qiumingdll_webview_navigate_to_string(webviewId, html);
    }
}

/// Step event (a separate loop demonstrating periodic communication with page scripts)
// Note: execute_script has no return-value callback; this only demonstrates sending commands to the page
if (state == "done")
{
    if (keyboard_check_pressed(vk_space))
    {
        qiumingdll_webview_execute_script(webviewId,
            "document.body.style.background = '#2a2a3e';");
    }
}

/// Room end event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_navigate](qiumingdll_webview_navigate.md)
- [qiumingdll_webview_get_is_active](qiumingdll_webview_get_is_active.md)
- [qiumingdll_webview_execute_script](qiumingdll_webview_execute_script.md)
- [qiumingdll_webview_create_child](qiumingdll_webview_create_child.md)
