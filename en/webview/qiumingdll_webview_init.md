# qiumingdll_webview_init()

Initialize the WebView module: register the window class, load WebView2Loader.dll, initialize COM and create the WebView2 environment. This is the first prerequisite for every WebView feature.

## Signature

```gml
qiumingdll_webview_init()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | No GML parameters. The wrapper automatically passes the main game window handle `window_handle()` to the DLL, which is later used to create child browser windows and to receive parent window resize events |

## Returns

| Value | Description |
|----|------|
| `0` | Initialization succeeded; create / create_child and the other functions can now be called |
| `1` | Window class registration failed (or the supplied window handle is invalid); no browser window can be created |
| `2` | WebView2Loader.dll could not be loaded (the DLL was not shipped with the program, or loading its entry point failed) |
| `3` | COM initialization failed |
| `4` | Memory allocation failed for the WebView2 environment creation callback |
| `5` | WebView2 environment creation failed (WebView2 Runtime is not installed, or the OS version is too old) |
| `1` | **Non-Windows platforms**: the GML wrapper returns 1 directly |

## Usage

- Prerequisite: this function must be called **before** any other function in the module (create, navigate, etc.), and you must confirm that it returned 0.
- Platform limitation: Windows only. It is built on the Microsoft Edge WebView2 runtime, so the system must have the WebView2 Runtime installed (Windows 10 / 11 normally ship with it; if missing, install the Evergreen Standalone runtime, or ship WebView2Loader.dll next to the exe).
- This function takes no arguments: the main window handle is obtained automatically by the wrapper and cannot (and need not) be passed manually.
- Whether initialization succeeds determines whether all later functions are usable; if it fails, the create functions return 0.
- Call `qiumingdll_webview_cleanup()` before exiting the game to release the environment; after cleanup, call this function again if you need to use the module.
- User data (cookies, cache, etc.) is stored in the WebView2Data folder next to the game exe.

## Example

```gml
/// Create event (obj_webview_manager)
// Initialize the WebView module when the game starts
initResult = qiumingdll_webview_init();
if (initResult != 0)
{
    // Initialization failed; log the error code and skip WebView features
    show_debug_message("WebView init failed: " + string(initResult));
    webviewEnabled = false;
}
else
{
    webviewEnabled = true;
}

/// Room end event
qiumingdll_webview_cleanup();  // Release all WebView resources before the game exits
```

## Related functions

- [qiumingdll_webview_create](qiumingdll_webview_create.md)
- [qiumingdll_webview_create_child](qiumingdll_webview_create_child.md)
- [qiumingdll_webview_cleanup](qiumingdll_webview_cleanup.md)
