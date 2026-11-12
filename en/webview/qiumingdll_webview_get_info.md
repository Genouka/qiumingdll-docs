# qiumingdll_webview_get_info(webviewId, infoType)

Queries runtime information about the specified WebView by type (position, size, ready state, window type).

## Signature

```gml
qiumingdll_webview_get_info(webviewId, infoType)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | Yes | WebView id, range 1 ~ 16 |
| infoType | Real | Yes | Query type: 0 = window X coordinate; 1 = window Y coordinate; 2 = client-area width; 3 = client-area height; 4 = ready (1/0); 5 = is child window (1/0); any other value is invalid |

## Returns

| Value | Description |
|----|------|
| (coordinate value) | When infoType = 0 or 1: returns the window position. **Child windows** return coordinates relative to the main window client area (converted automatically); **standalone windows** return screen coordinates. Unit: pixels |
| (size value) | When infoType = 2 or 3: returns the client-area width / height, in pixels |
| 1 / 0 | When infoType = 4: 1 = core ready (navigate / execute_script possible), 0 = not yet ready |
| 1 / 0 | When infoType = 5: 1 = child window (created by create_child), 0 = standalone window (created by create) |
| -1 | Query failed: invalid webviewId / no active WebView under that id, or infoType is not one of 0~5 |
| -1 | Non-Windows platform: the GML wrapper returns -1 directly |

## Usage

- Precondition: the WebView has been created (when querying position/size/type); infoType=4 can be queried without readiness.
- The position is the **real window position queried live**; it may differ slightly from the target values set by set_position / set_region due to system adjustments (e.g. after dragging).
- Standalone windows' X/Y are screen coordinates; child windows' X/Y are automatically converted to coordinates relative to the main window client area, convenient for direct use in the game.
- infoType = 4 is the second way to check readiness (equivalent to get_is_active).
- Common combinations: read the client-area width/height with 2/3 for UI layout logic against the window size; use 4 in a state machine to wait.

## Example

```gml
/// Create event (obj_webview_layout)
qiumingdll_webview_init();
childId = qiumingdll_webview_create_child(50, 40, 400, 300);
standId = qiumingdll_webview_create(800, 200, 500, 400);

/// Step event
if (keyboard_check_pressed(ord("I")))
{
    // Child window positions are client-area coordinates
    var cx = qiumingdll_webview_get_info(childId, 0);
    var cy = qiumingdll_webview_get_info(childId, 1);
    var cw = qiumingdll_webview_get_info(childId, 2);
    var ch = qiumingdll_webview_get_info(childId, 3);
    show_debug_message("Child window: (" + string(cx) + "," + string(cy) + ") " +
                       string(cw) + "x" + string(ch));

    // Standalone window values are screen coordinates
    var sx = qiumingdll_webview_get_info(standId, 0);
    show_debug_message("Standalone window screen X = " + string(sx));

    // Ready state and type
    if (qiumingdll_webview_get_info(childId, 4) == 1)
        show_debug_message("Child window is ready");
    show_debug_message("childId is child = " + string(qiumingdll_webview_get_info(childId, 5)));
}

/// Room End event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_get_is_active](qiumingdll_webview_get_is_active.md)
- [qiumingdll_webview_is_child](qiumingdll_webview_is_child.md)
- [qiumingdll_webview_set_position](qiumingdll_webview_set_position.md)
- [qiumingdll_webview_set_region](qiumingdll_webview_set_region.md)
