# qiumingdll_webview_cleanup()

Destroys all WebView windows and **releases the entire WebView environment** (including the WebView2 Environment, the loaded DLL, COM, and all other underlying resources).

## Signature

```gml
qiumingdll_webview_cleanup()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 1 | Cleanup executed successfully |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Call it before the game exits (Room End / Game End / closing the main window) to avoid leftover browser processes holding resources.
- **After cleanup the module returns to the uninitialized state**: to use WebView functionality again you must call qiumingdll_webview_init() again.
- Comparison with destroy_all:
  - destroy_all: only destroys the window instances; the environment is kept, so new windows can be created directly afterwards;
  - cleanup: destroys the windows **and releases the environment**; you must init again before using WebView.
- Internal flow: destroy all windows → stop intercepting main-window messages → release the WebView2 environment → unload the DLL → uninitialize COM.
- Calling cleanup repeatedly is safe (subsequent calls are effectively no-ops).
- Child windows do not need to be destroyed separately: they are destroyed automatically when the main window is destroyed.

## Example

```gml
/// Create event (obj_webview_manager)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(100, 100, 640, 480);

/// Room End event (the game is about to exit)
if (qiumingdll_webview_cleanup() == 1)
{
    show_debug_message("WebView environment fully released");
}

/// Game End event (safety net for abnormal exit paths)
qiumingdll_webview_cleanup();  // Repeated calls are safe
```

## Related functions

- [qiumingdll_webview_init](qiumingdll_webview_init.md)
- [qiumingdll_webview_destroy_all](qiumingdll_webview_destroy_all.md)
- [qiumingdll_webview_destroy](qiumingdll_webview_destroy.md)
