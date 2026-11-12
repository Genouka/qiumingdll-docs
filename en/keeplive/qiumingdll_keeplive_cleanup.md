# qiumingdll_keeplive_cleanup()

Uninstall the window keep-alive message hook, stop keep-alive protection for the target window, and clear the internally recorded target-window state.

## Signature

```gml
qiumingdll_keeplive_cleanup()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| (no return value) | This function returns no numeric value; there is nothing to handle after the call. **Non-Windows platforms**: the wrapper returns immediately and has no effect |

## Usage

- Prerequisite: none. Calling this function is safe even if qiumingdll_keeplive_init() was never called (no hook installed).
- Platform limitation: Windows only (on non-Windows platforms the wrapper function returns immediately and does nothing).
- Relation to init: every hook installed by init is uninstalled by this function; after uninstalling, qiumingdll_keeplive_is_active() returns 0.
- When to call: recommended before the game exits, when switching window mode (fullscreen ↔ windowed), or when switching to a scene that does not need keep-alive protection.
- Behavior details: after uninstalling, close requests to the target window (titlebar ×, Alt+F4 and other system commands) are handled normally again; the window no longer enjoys the "not responding" exemption either.
- Safe to call repeatedly: uninstalling again does not raise an error; there are simply no more hooks to remove.
- The global cleanup routine normally calls this function automatically; when calling it manually, take care not to run it twice together with the global cleanup.
- Debugging tip: after uninstalling, use qiumingdll_keeplive_is_active() to verify that it is back to 0; if it still returns 1 after cleanup, another keep-alive instance is still running — check whether init was called more than once.

## Example

```gml
/// Room End event (obj_keeplive_manager)
// Disable keep-alive before switching scenes so the hook does not affect other window logic
qiumingdll_keeplive_cleanup();

/// Game End event
// Final cleanup before the game exits
qiumingdll_keeplive_cleanup();

/// Enable again
// Reinstall when keep-alive is needed
if (needKeepAlive)
{
    qiumingdll_keeplive_init();
}
```

## Related functions

- [qiumingdll_keeplive_init](qiumingdll_keeplive_init.md)
- [qiumingdll_keeplive_is_active](qiumingdll_keeplive_is_active.md)
