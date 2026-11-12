# qiumingdll_webview_destroy(webviewId)

Destroys the specified WebView window and releases its internal resources; the id is immediately freed for reuse.

## Signature

```gml
qiumingdll_webview_destroy(webviewId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | Yes | WebView id to destroy, range 1 ~ 16; must be a valid id returned by create / create_child |

## Returns

| Value | Description |
|----|------|
| 1 | Destruction succeeded (valid id and the window exists) |
| 0 | Destruction failed: invalid id (outside 1~16), no active WebView under that id, or the module was not initialized before the call |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Precondition: the WebView must have been created by create / create_child and not yet destroyed.
- Destroys **one** WebView only: after destroy the id is immediately invalid, `exists(id)` returns 0, `get_is_active(id)` returns 0; a later create may reuse that id.
- Destroying a child window behaves the same as destroying a standalone window; when the main window is destroyed its child windows are destroyed automatically, so nothing needs to be (or should be) done manually.
- Destruction is immediate; no waiting is required. Do not call any other function with that id afterwards (they will all return 0 / -1).
- When the game exits and all windows are handled uniformly, destroy_all or cleanup is more convenient.

## Example

```gml
/// Global WebView manager object (obj_webview_manager)

/// Create event
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(600, 200, 480, 360);
webviewBusy = true;  // Prevents double destruction

/// Step event
// If the browser is closed by test mode: closing standalone windows is already handled by the DLL on Windows,
// this shows conditionally destroying it explicitly
if (keyboard_check_pressed(vk_f1) && webviewBusy)
{
    // Close the page before destroying (reload/stop before destroy is optional and does not affect destruction)
    var result = qiumingdll_webview_destroy(webviewId);
    webviewBusy = false;
    show_debug_message("destroy result = " + string(result));
    // Confirm destruction
    if (qiumingdll_webview_exists(webviewId) == 0)
    {
        show_debug_message("WebView destroyed, id released");
    }
}

/// Room End event
qiumingdll_webview_cleanup();  // Safety net: release all resources
```

## Related functions

- [qiumingdll_webview_create](qiumingdll_webview_create.md)
- [qiumingdll_webview_create_child](qiumingdll_webview_create_child.md)
- [qiumingdll_webview_destroy_all](qiumingdll_webview_destroy_all.md)
- [qiumingdll_webview_exists](qiumingdll_webview_exists.md)
- [qiumingdll_webview_cleanup](qiumingdll_webview_cleanup.md)
