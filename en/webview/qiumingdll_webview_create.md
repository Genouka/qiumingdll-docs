# qiumingdll_webview_create(x, y, w, h)

Creates a standalone browser window (with a system title bar, movable and closable) and returns the window's webviewId.

## Signature

```gml
qiumingdll_webview_create(x, y, w, h)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| x | Real | Yes | Screen-coordinate X of the window's top-left corner, in pixels (screen coordinate system, origin at the top-left of the screen) |
| y | Real | Yes | Screen-coordinate Y of the window's top-left corner, in pixels |
| w | Real | Yes | Client-area width of the window, in pixels (`w` and `h` refer to the content area size; the actual window additionally includes the title bar area) |
| h | Real | Yes | Client-area height of the window, in pixels |

## Returns

| Value | Description |
|----|------|
| 1 ~ 16 | Creation succeeded; returns the WebView id (webviewId), allocated from 1 upward; ids are reused after everything has been destroyed |
| 0 | Creation failed. Possible reasons: qiumingdll_webview_init() has not been called, initialization failed, 16 WebViews already exist, insufficient system resources |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Precondition: qiumingdll_webview_init() must be called first and return 0.
- Platform support: Windows only; requires the installed WebView2 Runtime (usually bundled with Win10 / Win11).
- At most **16** WebViews can exist at the same time; beyond that, create returns 0.
- This function creates a **standalone top-level window** with its own title bar, system menu and close button:
  - Closable by default (use `set_closable(id, 0)` to disable closing).
  - By default, closing affects only itself and does **not** close the main game window; use `set_close_triggers_main(id, 1)` to also close the main window.
  - Not draggable by default; use `set_draggable(id, 1)` to enable "drag by holding anywhere on the window".
- **Page loading is asynchronous**: immediately after create returns, the WebView is not yet ready internally; calling navigate / execute_script / reload etc. then returns 0 (failure). Poll with `get_is_active(id)` (returns 1 = ready) or `get_info(id, 4)` until ready, then operate.
- New windows are visible by default (CreateWindowEx includes WS_VISIBLE); show / hide can also be used.
- When a window created by this function is closed during the game, wm_close is handled by the DLL, so GML does not need to handle the close event.
- **Standalone** windows are not destroyed automatically when the main window is destroyed; clean them up with destroy / destroy_all / cleanup before the game exits.

## Example

```gml
/// Create event (obj_browser_manager)
if (qiumingdll_webview_init() != 0)
{
    exit;  // Initialization failed; this object should not run
}

// Create an 800x600 standalone browser window, left of screen center
webviewId = qiumingdll_webview_create(200, 100, 800, 600);
if (webviewId == 0)
{
    show_debug_message("Failed to create WebView");
    exit;
}

// Set the title and open a URL once ready
qiumingdll_webview_set_title(webviewId, "In-game browser");
state = "waiting_ready";

/// Step event
if (state == "waiting_ready")
{
    if (qiumingdll_webview_get_is_active(webviewId) == 1)
    {
        state = "waiting_ready_done";
        qiumingdll_webview_navigate(webviewId, "https://example.com");
    }
}
else
{
    // Once the page has loaded, script execution etc. can begin
    if (qiumingdll_webview_get_info(webviewId, 4) == 1)
    {
        // For example, change the title text in the page
        qiumingdll_webview_execute_script(webviewId, "document.body.style.background='#222'");
    }
}

/// Room End event
qiumingdll_webview_destroy(webviewId);  // Destroy this window before the game exits
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_init](qiumingdll_webview_init.md)
- [qiumingdll_webview_create_child](qiumingdll_webview_create_child.md)
- [qiumingdll_webview_destroy](qiumingdll_webview_destroy.md)
- [qiumingdll_webview_get_is_active](qiumingdll_webview_get_is_active.md)
- [qiumingdll_webview_navigate](qiumingdll_webview_navigate.md)
