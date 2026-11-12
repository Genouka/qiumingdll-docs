# qiumingdll_webview_go_back(webviewId)

Navigate the given WebView back to the previous page in its browsing history (equivalent to the browser's Back button).

## Signature

```gml
qiumingdll_webview_go_back(webviewId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | real | yes | WebView id, range 1 ~ 16 |

## Returns

| Value | Description |
|----|------|
| `1` | Back request submitted (note: this does not guarantee that the history actually moved back) |
| `0` | Failure: invalid id, WebView does not exist, or not ready yet |
| `0` | Non-Windows platforms: the GML wrapper returns 0 directly |

## Usage

- Prerequisite: the WebView is ready.
- **Depends on browsing history**: going back only has a visible effect when the WebView has a "previous page" (for example after several navigates, or after following a link inside the page); with no history the call returns 1 but the page stays unchanged.
- History is maintained per WebView and is unrelated to other game windows.
- Content rendered by navigate_to_string also counts toward history.
- Combining back/forward with reload gives a complete "toolbar" logic (together with go_forward).
- Asynchronous: a return value of 1 only means the request was issued.

## Example

```gml
/// Create event (obj_webview_wiki)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(100, 100, 800, 600);

/// Step event
// Open the first page once ready
if (qiumingdll_webview_get_is_active(webviewId) == 1 && !loaded)
{
    loaded = true;
    qiumingdll_webview_navigate(webviewId, "https://example.com/page1");
}

// Browser-style back/forward buttons
if (keyboard_check_pressed(vk_left))   // Left arrow = back
    qiumingdll_webview_go_back(webviewId);

if (keyboard_check_pressed(vk_right))  // Right arrow = forward
    qiumingdll_webview_go_forward(webviewId);

if (keyboard_check_pressed(vk_f5))     // F5 = reload
    qiumingdll_webview_reload(webviewId);

/// Room end event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_go_forward](qiumingdll_webview_go_forward.md)
- [qiumingdll_webview_reload](qiumingdll_webview_reload.md)
- [qiumingdll_webview_navigate](qiumingdll_webview_navigate.md)
