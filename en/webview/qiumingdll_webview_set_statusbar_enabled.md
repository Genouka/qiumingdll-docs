# qiumingdll_webview_set_statusbar_enabled(webviewId, enabled)

Enable or disable the status bar at the bottom of the specified WebView page (showing link targets, load progress, etc.).

## Signature

```gml
qiumingdll_webview_set_statusbar_enabled(webviewId, enabled)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | yes | WebView id, range 1 ~ 16 |
| enabled | Real | yes | Boolean switch: 1 (non-zero) = show the status bar, 0 = hide the status bar |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Call failed: invalid id, the WebView does not exist, or it is not ready yet (this function requires readiness) |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Precondition: the WebView has been created and is ready.
- **Off by default**: the status bar is not shown after create.
- Once enabled, a status bar area appears at the bottom of the browser window (showing the target address when hovering a link, load progress while the page loads, etc.), matching the experience of a normal browser.
- Off is the recommended state: the status bar takes up space at the bottom of the page and weakens the "embedded app" look; enable it when you want a "browser feel" (e.g. a built-in browser feature page).
- Affects a single WebView only.

## Example

```gml
/// Create event (obj_webview_browser)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(150, 100, 900, 640);

/// Step event
if (qiumingdll_webview_get_is_active(webviewId) == 1 && !configured)
{
    configured = true;
    // This window emulates a "built-in browser": enable the status bar + context menu + DevTools
    qiumingdll_webview_set_statusbar_enabled(webviewId, 1);
    qiumingdll_webview_set_default_context_menus_enabled(webviewId, 1);
    qiumingdll_webview_navigate(webviewId, "https://example.com");
}

/// Room end event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_set_devtools_enabled](qiumingdll_webview_set_devtools_enabled.md)
- [qiumingdll_webview_set_default_context_menus_enabled](qiumingdll_webview_set_default_context_menus_enabled.md)
- [qiumingdll_webview_set_script_enabled](qiumingdll_webview_set_script_enabled.md)
