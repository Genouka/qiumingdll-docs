# qiumingdll_webview_get_is_active(webviewId)

Queries whether the specified WebView has been created and is **internally ready** (the controller has been created, so navigate / execute_script etc. can be used).

## Signature

```gml
qiumingdll_webview_get_is_active(webviewId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | Yes | WebView id, range 1 ~ 16 |

## Returns

| Value | Description |
|----|------|
| 1 | The WebView exists and is ready; navigation, script execution and similar operations can be performed |
| 0 | The WebView does not exist (invalid id, destroyed, or never created), or exists but is **not yet ready** (common right after create) |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- **This is the most important function for deciding "when operations can start"**: after create / create_child returns, the WebView's core creation is asynchronous; only once this function returns 1 (or `get_info(id, 4)` returns 1) do readiness-dependent functions such as navigate, navigate_to_string, execute_script, reload, stop, go_back, go_forward succeed; otherwise they all return 0.
- Poll this function in the GML Step event and perform the initial setup (title, switches, first navigation) once ready.
- Difference from exists: exists only checks "whether the window exists" (1 immediately after create); this function additionally checks whether the core is ready.
- Once ready, it never reverts to not-ready while running; after destruction it returns 0 (consistent with exists).

## Example

```gml
/// Create event (obj_browser_launcher)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(150, 100, 900, 600);
started = false;

/// Step event
// Poll until ready, then complete initialization in one go
if (!started && qiumingdll_webview_get_is_active(webviewId) == 1)
{
    started = true;
    show_debug_message("WebView ready, starting initialization");
    qiumingdll_webview_set_devtools_enabled(webviewId, 1);
    qiumingdll_webview_set_title(webviewId, "Home");
    qiumingdll_webview_navigate(webviewId, "https://example.com");
}

// While waiting, if the page is not ready yet, demonstrate attempting navigation (it fails; for teaching only)
if (!started)
{
    var r = qiumingdll_webview_navigate(webviewId, "https://example.com");
    if (r == 0) show_debug_message("Not ready yet, navigate failed (expected behavior)");
}

/// Room End event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_get_info](qiumingdll_webview_get_info.md)
- [qiumingdll_webview_exists](qiumingdll_webview_exists.md)
- [qiumingdll_webview_create](qiumingdll_webview_create.md)
- [qiumingdll_webview_navigate](qiumingdll_webview_navigate.md)
