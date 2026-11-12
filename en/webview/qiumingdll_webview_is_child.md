# qiumingdll_webview_is_child(webviewId)

Query whether the given WebView is a child window (created by create_child) or a standalone window (created by create).

## Signature

```gml
qiumingdll_webview_is_child(webviewId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | real | yes | WebView id, range 1 ~ 16 |

## Returns

| Value | Description |
|----|------|
| `1` | The id refers to a child browser window (created by create_child, embedded in the main window's client area) |
| `0` | The id refers to a standalone window (created by create) |
| `0` | The id does not exist (invalid, never created, or already destroyed) — returns 0 just like a standalone window; use exists to tell them apart |
| `0` | Non-Windows platforms: the GML wrapper returns 0 directly |

## Usage

- Prerequisite: the WebView has been created (returns 0 if not).
- The most direct way to determine the type of a single window; `get_info(id, 5)` provides the same information.
- How the two types differ:
  - Child window: coordinates are client-area coordinates; it cannot be dragged/closed/made topmost; it is destroyed automatically when the main window is destroyed; resize_to_parent is available;
  - Standalone window: screen coordinates; can be dragged/closed/made topmost; must be destroyed explicitly.
- Useful for branching in unified multi-window management logic.

## Example

```gml
/// Create event (obj_webview_manager)
qiumingdll_webview_init();
widgets[0] = qiumingdll_webview_create_child(20, 20, 300, 200);  // In-game UI
widgets[1] = qiumingdll_webview_create(600, 150, 400, 300);      // Standalone popup

/// Step event
// Iterate over all windows and run type-specific logic
for (var i = 0; i < 2; i++)
{
    var id = widgets[i];
    if (qiumingdll_webview_is_child(id) == 1)
    {
        // Child window: keep its client-area coordinates in bounds
        var x = qiumingdll_webview_get_info(id, 0);
        if (x < 0) qiumingdll_webview_set_position(id, 0, 20);
    }
    else
    {
        // Standalone window: make sure the topmost state matches requirements
        qiumingdll_webview_set_topmost(id, 1);
    }
}

/// Room end event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_create_child](qiumingdll_webview_create_child.md)
- [qiumingdll_webview_create](qiumingdll_webview_create.md)
- [qiumingdll_webview_get_info](qiumingdll_webview_get_info.md)
- [qiumingdll_webview_resize_to_parent](qiumingdll_webview_resize_to_parent.md)
