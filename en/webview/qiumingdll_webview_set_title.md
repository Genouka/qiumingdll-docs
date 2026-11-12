# qiumingdll_webview_set_title(webviewId, title)

Set the text displayed in the title bar of the specified WebView window.

## Signature

```gml
qiumingdll_webview_set_title(webviewId, title)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | yes | WebView id, range 1 ~ 16 |
| title | String | yes | Window title text; Chinese is supported (converted to UTF-8 internally); limited by the internal 512-wide-character buffer, longer strings are truncated |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Call failed: invalid id, or there is no active WebView with that id |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Precondition: the WebView has been created. Does not require readiness.
- Only affects the title bar text of **standalone windows** (created with create); the title bar may also be overwritten by the page's own `document.title` (Chromium rewrites the window title when a page loads). To keep a fixed title, set it again after the page has loaded, or keep the page title empty.
- **Child windows have no title bar**; calling this function has no visible effect (it still executes internally and returns 1).
- An empty string clears the title.
- The title is for display only; when you need to identify a window, use the webviewId you recorded yourself.

## Example

```gml
/// Create event (obj_webview_news)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(100, 100, 640, 480);
qiumingdll_webview_set_title(webviewId, "News");

/// Step event
// Fix the title again once the page is ready (to prevent it from being overwritten by document.title)
if (qiumingdll_webview_get_is_active(webviewId) == 1 && !titleFixed)
{
    titleFixed = true;
    qiumingdll_webview_set_title(webviewId, "News - In-Game");
}

/// Room end event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_set_titlebar](qiumingdll_webview_set_titlebar.md)
- [qiumingdll_webview_create](qiumingdll_webview_create.md)
- [qiumingdll_webview_get_is_active](qiumingdll_webview_get_is_active.md)
