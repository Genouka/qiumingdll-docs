# qiumingdll_webview_get_count()

Returns the number of WebView windows that currently exist (not yet destroyed).

## Signature

```gml
qiumingdll_webview_get_count()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 0 ~ 16 | Number of currently active WebViews (standalone + child windows combined). Destroying one decreases the count; 16 is the simultaneous limit |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Precondition: no init required (when uninitialized the window count is 0 and this function can still be called safely).
- Use cases: determine whether windows still need cleaning up, whether you are close to the 16 limit (another create would return 0), and count resource usage while debugging.
- Only counts "active" windows: destroyed ones (via destroy / destroy_all / automatic destruction from main-window destruction) are excluded.
- Note: returns 0 when initialized but no window has ever been created; also returns 0 after everything is destroyed.

## Example

```gml
/// Create event (obj_webview_debug)
qiumingdll_webview_init();

/// Step event
// Refresh debug info every 60 frames
if (frame % 60 == 0)
{
    var n = qiumingdll_webview_get_count();
    show_debug_message("Current WebView count = " + string(n) + " / 16");
}

// Demo: do not create new windows when nearing the limit
if (keyboard_check_pressed(ord("N")))
{
    if (qiumingdll_webview_get_count() >= 16)
    {
        show_debug_message("16 limit reached, creation failed");
    }
    else
    {
        var id = qiumingdll_webview_create(100 + irandom(800), 100 + irandom(400), 320, 240);
        show_debug_message("Created id = " + string(id));
    }
}

/// Room End event
qiumingdll_webview_destroy_all();
show_debug_message("Count after destruction = " + string(qiumingdll_webview_get_count()));
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_exists](qiumingdll_webview_exists.md)
- [qiumingdll_webview_destroy_all](qiumingdll_webview_destroy_all.md)
- [qiumingdll_webview_create](qiumingdll_webview_create.md)
