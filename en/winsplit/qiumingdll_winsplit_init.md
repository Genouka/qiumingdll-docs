# qiumingdll_winsplit_init()

Initialize the window splitting module: record the current game window, register the split window class and install the frame capture hook. This is a precondition for all window splitting features.

## Signature

```gml
qiumingdll_winsplit_init()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no GML parameters. The wrapper automatically passes the current game window handle (`window_handle()`) to the DLL; the caller does not need to provide it |

## Returns

| Value | Description |
|----|------|
| 0 | Initialization succeeded, the module is ready and split windows can be created |
| 1 | Initialization failed (e.g. invalid window handle, window class registration failed); on non-Windows platforms the GML wrapper returns 1 directly without calling the DLL |

## Usage

- Precondition: you must first call `qiumingdll_init()` to complete the overall extension initialization (that function registers global function handles such as `__qiumingdll_winsplit_*`); otherwise the wrapper cannot detect the handles and returns the failure value directly.
- Platform limit: Windows only; macOS / Linux and other non-Windows platforms return 1 directly.
- Should be called only once during the game lifecycle; to reinitialize, call `qiumingdll_winsplit_cleanup()` first, then call this function.
- This module depends on D3D11 rendering capture to display split images, so the game must use D3D11 rendering (GameMaker's default).
- After successful initialization, it is recommended to record the result in a global variable and check it before creating split windows, avoiding further calls in a failed environment.
- After successful initialization no split windows are created and the original window is not hidden by default; call the creation and hiding functions as needed.

## Example

```gml
// Initialize the window splitting module in the controller object's Create event
if (os_type == os_windows)
{
    // First complete the overall extension initialization (register DLL function handles)
    qiumingdll_init();

    // Initialize the window splitting module
    var _ret = qiumingdll_winsplit_init();
    if (_ret == 0)
    {
        global.winsplit_ready = true;
        show_debug_message("Window splitting module initialized");
    }
    else
    {
        global.winsplit_ready = false;
        show_debug_message("Window splitting module initialization failed");
    }
}
```

## Related functions

- [qiumingdll_winsplit_create](qiumingdll_winsplit_create.md)
- [qiumingdll_winsplit_cleanup](qiumingdll_winsplit_cleanup.md)
- [qiumingdll_winsplit_hide_original](qiumingdll_winsplit_hide_original.md)
