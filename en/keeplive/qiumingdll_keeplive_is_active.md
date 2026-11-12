# qiumingdll_keeplive_is_active()

Query whether the window keep-alive hook is currently installed; returns 1 when keep-alive is active and 0 when it is not installed.

## Signature

```gml
qiumingdll_keeplive_is_active()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| `1` | Keep-alive hook installed: qiumingdll_keeplive_init() has been called successfully and cleanup has not uninstalled it yet |
| `0` | Hook not installed: init was never called, init failed, or qiumingdll_keeplive_cleanup() has been called. The GML wrapper function on **non-Windows platforms** also returns 0 directly |

## Usage

- Prerequisite: none; it can be called safely at any time.
- Platform limitation: Windows only (on non-Windows platforms the wrapper function returns 0 directly).
- Purpose: display the keep-alive state in the UI (for example "Prevent not-responding: on"), confirm during debugging whether init actually took effect, and avoid calling init repeatedly.
- Behavior details: after init returns 0 successfully, is_active becomes 1 immediately; after cleanup is called it returns to 0 immediately. If one of the internal keep-alive hooks is removed automatically due to an exception, a value of 0 means protection is incomplete and init should be called again.
- Tip: is_active being 1 only means the hook is in place, not that "the window will definitely never stop responding"; it merely reduces the risk of being force-closed by the system by intercepting messages.

## Example

```gml
/// Step event (obj_keeplive_manager)
// Check keep-alive state every frame and reinstall automatically if it fails unexpectedly
if (wantKeepAlive && qiumingdll_keeplive_is_active() == 0)
{
    qiumingdll_keeplive_init();
}

/// Draw GUI event
// Status display
if (qiumingdll_keeplive_is_active() == 1)
{
    draw_set_color(c_lime);
    draw_text(10, 10, "Keep-alive hook: installed");
}
else
{
    draw_set_color(c_red);
    draw_text(10, 10, "Keep-alive hook: not installed");
}
```

## Related functions

- [qiumingdll_keeplive_init](qiumingdll_keeplive_init.md)
- [qiumingdll_keeplive_cleanup](qiumingdll_keeplive_cleanup.md)
