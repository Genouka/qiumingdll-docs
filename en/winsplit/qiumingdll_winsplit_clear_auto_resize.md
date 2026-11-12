# qiumingdll_winsplit_clear_auto_resize(splitId)

Cancel the 9-Patch auto-follow of the split window. Afterwards the split window keeps its current position, size and source region, and no longer adjusts automatically when the main window is resized/moved.

## Signature

```gml
qiumingdll_winsplit_clear_auto_resize(splitId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window ID, value range 1 ~ 16 |

## Returns

| Value | Description |
|----|------|
| 1 | Call succeeded (returns 1 even if the window never enabled auto-follow; this function is idempotent) |
| 0 | Call failed: invalid ID or the split window does not exist |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Does not stop a playing animation; after the animation ends the window stays at the animation result and main-window resizing no longer intervenes.
- After cancelling you can re-enable at any time with `qiumingdll_winsplit_set_auto_resize_9patch` (using the client area at the time of the call as the new design size).
- On destroy / cleanup the follow state is destroyed together with the window.

## Example

```gml
/// The player turns off the "screen copy" feature
qiumingdll_winsplit_clear_auto_resize(splitId);
qiumingdll_winsplit_set_region(splitId, 100, 100, 400, 225);
```

## Related functions

- [qiumingdll_winsplit_set_auto_resize_9patch](qiumingdll_winsplit_set_auto_resize_9patch.md)
- [qiumingdll_winsplit_set_region](qiumingdll_winsplit_set_region.md)
