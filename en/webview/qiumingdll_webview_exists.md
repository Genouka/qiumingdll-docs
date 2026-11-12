# qiumingdll_webview_exists(webviewId)

Queries whether the given webviewId currently corresponds to an active (not yet destroyed) WebView window.

## Signature

```gml
qiumingdll_webview_exists(webviewId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | Yes | WebView id, range 1 ~ 16 |

## Returns

| Value | Description |
|----|------|
| 1 | An active WebView window exists under this id |
| 0 | Does not exist: invalid id (outside 1~16), never created, or already destroyed |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Only checks "whether the window was created and not destroyed"; it does **not** check whether the core is ready. Use get_is_active or get_info(id, 4) for readiness.
- Right after create returns, this function is already 1 (earlier than core readiness).
- Use cases: validate that an id is still legal before calling other functions (operating after destroy yields 0 / -1; checking exists first is clearer); detect dangling ids when managing a multi-window list.
- A child window destroyed together with the main window also makes this function return 0.

## Example

```gml
/// Create event (obj_webview_keeper)
qiumingdll_webview_init();
idA = qiumingdll_webview_create(100, 100, 400, 300);
idB = qiumingdll_webview_create_child(20, 20, 300, 200);
idC = 99;  // Example of an invalid id

/// Step event
// Press D to destroy idA, then check the state of each id
if (keyboard_check_pressed(ord("D")))
{
    qiumingdll_webview_destroy(idA);
    show_debug_message("idA exists? " + string(qiumingdll_webview_exists(idA)));
    show_debug_message("idB exists? " + string(qiumingdll_webview_exists(idB)) + "  ready? " +
                       string(qiumingdll_webview_get_is_active(idB)));
    show_debug_message("idC exists? " + string(qiumingdll_webview_exists(idC)));
}

// Demo: validate before calling, to avoid operating on destroyed ids
if (keyboard_check_pressed(ord("X")))
{
    if (qiumingdll_webview_exists(idA))
    {
        qiumingdll_webview_hide(idA);
    }
}

/// Room End event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_get_is_active](qiumingdll_webview_get_is_active.md)
- [qiumingdll_webview_get_count](qiumingdll_webview_get_count.md)
- [qiumingdll_webview_destroy](qiumingdll_webview_destroy.md)
- [qiumingdll_webview_is_child](qiumingdll_webview_is_child.md)
