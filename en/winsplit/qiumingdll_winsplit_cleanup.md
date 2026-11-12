# qiumingdll_winsplit_cleanup()

Clean up the window splitting module as a whole: destroy all split windows, restore the original game window, and uninstall the capture and message hooks. Use it when the game exits or splitting is disabled entirely.

## Signature

```gml
qiumingdll_winsplit_cleanup()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 1 | Cleanup succeeded; on non-Windows platforms the wrapper returns 0 directly |

## Usage

- Precondition: `qiumingdll_winsplit_init()` has been called successfully (calling it when uninitialized is harmless and idempotent).
- This cleanup performs in order: destroy all split windows → restore the original window if it was hidden → remove the frame capture hook and the message hook.
- After cleanup all split window IDs become invalid and `get_count` returns 0; if you use splitting again afterwards you must call `qiumingdll_winsplit_init()` again.
- Recommended in the game exit event (e.g. Game End / before the main loop ends) so the original window and system state are fully restored; not calling it will not crash, but hidden state and hooks may be left behind.
- To destroy a single split window use `qiumingdll_winsplit_destroy` or `qiumingdll_winsplit_destroy_all`; this function is "module-level" cleanup.

## Example

```gml
// Perform module cleanup in the controller object's Game End event (or Clean Up event)
qiumingdll_winsplit_cleanup();
```

```gml
// Provide a "disable split mode" switch in the game: clean up first, then re-init when needed later
// Controller object Step event
if (keyboard_check_pressed(ord("Q")))
{
    qiumingdll_winsplit_cleanup();
    global.winsplit_ready = false; // Mark the module as disabled; re-init before next use
}
```

## Related functions

- [qiumingdll_winsplit_init](qiumingdll_winsplit_init.md)
- [qiumingdll_winsplit_destroy_all](qiumingdll_winsplit_destroy_all.md)
- [qiumingdll_winsplit_show_original](qiumingdll_winsplit_show_original.md)
