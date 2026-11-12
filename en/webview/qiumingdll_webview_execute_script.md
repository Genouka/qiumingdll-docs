# qiumingdll_webview_execute_script(webviewId, script)

Executes a piece of JavaScript code in the specified WebView's current page.

## Signature

```gml
qiumingdll_webview_execute_script(webviewId, script)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | Yes | WebView id, range 1 ~ 16 |
| script | String | Yes | JavaScript source code string to execute; multiple statements and Chinese text are supported; note that quotes and backslashes inside GML strings must be escaped (converted to UTF-8 internally and passed to Chromium) |

## Returns

| Value | Description |
|----|------|
| 1 | The script was submitted to the page for execution (successful submission does not mean the script ran without JS errors; errors thrown by the script itself are not reported back) |
| 0 | Call failed: invalid id, WebView does not exist, not yet ready, or the script string conversion failed |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Precondition: the WebView must be created and ready, and **the page must have loaded** (ideally wait a moment after navigate / navigate_to_string); executing scripts while a page is loading usually fails or acts on a half-loaded page.
- **No return value**: this function does not return the script's execution result, only whether submission succeeded. For two-way communication between page and game, the page can write data into the DOM (e.g. an input's value, an element's textContent) and the game side uses execute_script to write or read it.
- Depends on the JavaScript switch: `set_script_enabled(id, 1)` must stay enabled (**enabled by default**); once disabled, execute_script has no effect.
- It runs in the global scope of the page's current document: global variables can be read/modified, page functions called, and DOM events triggered.
- Execution is asynchronous: after returning 1 the script runs on the page thread, so querying page state immediately afterwards may not yet reflect it.
- Works with DevTools: with DevTools enabled you can debug page scripts directly in the developer tools Console (`set_devtools_enabled(id, 1)`, disabled by default).

## Example

```gml
/// Create event (obj_webview_hud)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create_child(0, 0, 640, 100);
pageReady = false;

/// Step event
// 1) Wait until ready and load the page
if (!ready_started && qiumingdll_webview_get_is_active(webviewId) == 1)
{
    ready_started = true;
    qiumingdll_webview_navigate_to_string(webviewId,
        "<html><body><div id='hud'>HP: 0/0</div></body></html>");
    loadTick = 0;
}
if (ready_started && !pageReady)
{
    loadTick++;
    if (loadTick > 10)
    {
        pageReady = true;  // Simple delay to let the page render
    }
}

// 2) Once the page is ready, inject game HUD data into it
if (pageReady && hp != lastHp)
{
    lastHp = hp;
    var code = "document.getElementById('hud').textContent = 'HP: " +
               string(hp) + "/" + string(hpMax) + "';";
    qiumingdll_webview_execute_script(webviewId, code);
}

// 3) Demo of reading page content (write into the DOM, read back by a later script, or convert to an image for processing)
if (keyboard_check_pressed(vk_f5))
{
    // Have the page write data back into some DOM field, to be retrieved later by other means
    qiumingdll_webview_execute_script(webviewId,
        "localStorage.setItem('last_ts', String(Date.now()));");
}

/// Room End event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_navigate](qiumingdll_webview_navigate.md)
- [qiumingdll_webview_navigate_to_string](qiumingdll_webview_navigate_to_string.md)
- [qiumingdll_webview_set_script_enabled](qiumingdll_webview_set_script_enabled.md)
- [qiumingdll_webview_get_is_active](qiumingdll_webview_get_is_active.md)
