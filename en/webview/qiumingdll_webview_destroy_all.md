# qiumingdll_webview_destroy_all()

Destroys **all** currently existing WebView window instances (both standalone and child windows) and frees every id.

## Signature

```gml
qiumingdll_webview_destroy_all()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 1 | Executed successfully (returns 1 even when there are no WebViews at all) |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Difference from cleanup: **destroy_all only destroys the window instances**; the WebView2 environment, COM and other underlying resources are kept, so **you can continue** to call create / create_child after destroying, without re-initializing.
- Equivalent to calling destroy on each existing id one by one.
- Use case: clearing all browser windows when switching levels / modes while keeping the environment for quick rebuilding.
- Note that it does not free the memory occupied by the WebView2 environment; use cleanup before the game fully exits to release all resources.

## Example

```gml
/// Create event (obj_webview_manager)
qiumingdll_webview_init();

/// Step event
// Demo: press F2 to clear all browser windows, then immediately rebuild one
if (keyboard_check_pressed(vk_f2))
{
    qiumingdll_webview_destroy_all();
    show_debug_message("WebViews left after destruction = " + string(qiumingdll_webview_get_count()));

    // cleanup is not required to release the environment, so a new window can be created directly
    newId = qiumingdll_webview_create(300, 150, 640, 480);
    show_debug_message("New WebView id = " + string(newId));
}

/// Room End event
// Clear all windows, then release the environment
qiumingdll_webview_destroy_all();
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_destroy](qiumingdll_webview_destroy.md)
- [qiumingdll_webview_cleanup](qiumingdll_webview_cleanup.md)
- [qiumingdll_webview_get_count](qiumingdll_webview_get_count.md)
- [qiumingdll_webview_create](qiumingdll_webview_create.md)
