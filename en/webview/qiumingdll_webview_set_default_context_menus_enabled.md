# qiumingdll_webview_set_default_context_menus_enabled(webviewId, enabled)

Enable or disable the default context menu of the specified WebView page.

## Signature

```gml
qiumingdll_webview_set_default_context_menus_enabled(webviewId, enabled)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | yes | WebView id, range 1 ~ 16 |
| enabled | Real | yes | Boolean switch: 1 (non-zero) = show the default context menu (**enabled by default**), 0 = disable the default context menu |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Call failed: invalid id, the WebView does not exist, or it is not ready yet (this function requires readiness) |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Precondition: the WebView has been created and is ready.
- **Enabled by default**. Once disabled, right-clicking the page no longer pops up the browser's "Back/Reload/Inspect" menus.
- Note: this disables the **built-in** menu; a page's own contextmenu event (a right-click menu implemented by the page itself) still works.
- Purpose:
  - Create an "app" feel rather than a "browser" feel;
  - Prevent players from opening DevTools, viewing the source or saving images through the context menu;
  - Prevent accidental clicks from interrupting game input.
- Affects only a single WebView.

## Example

```gml
/// Create event (obj_webview_app)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(100, 100, 800, 600);
// Disable the default context menu, blocking browser operations
qiumingdll_webview_set_default_context_menus_enabled(webviewId, 0);

/// Step event
// Load the game client main screen once ready
if (qiumingdll_webview_get_is_active(webviewId) == 1 && !loaded)
{
    loaded = true;
    qiumingdll_webview_navigate_to_string(webviewId,
        "<html><body style='background:#111;color:#fff;text-align:center;padding-top:40%'>" +
        "Context menu disabled<br>(press C to toggle)</body></html>");
}

// Press C to toggle the context menu (demo)
if (keyboard_check_pressed(ord("C")))
{
    ctxOn = !ctxOn;
    qiumingdll_webview_set_default_context_menus_enabled(webviewId, ctxOn ? 1 : 0);
}

/// Room end event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_set_devtools_enabled](qiumingdll_webview_set_devtools_enabled.md)
- [qiumingdll_webview_set_script_enabled](qiumingdll_webview_set_script_enabled.md)
- [qiumingdll_webview_set_statusbar_enabled](qiumingdll_webview_set_statusbar_enabled.md)
