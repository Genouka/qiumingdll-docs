# qiumingdll_winsplit_batch_add_src_region(splitId, srcX, srcY, srcW, srcH, durationMs)

Adds a "source region transform" command to the batch recording: during playback the source region (the image area captured from the main window) is interpolated from its current value to the target region within durationMs milliseconds.

## Signature

```gml
qiumingdll_winsplit_batch_add_src_region(splitId, srcX, srcY, srcW, srcH, durationMs)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window number, starting from 1, maximum 16 |
| srcX | Real | yes | X coordinate of the top-left corner of the target source region (main window client area coordinate system, in pixels) |
| srcY | Real | yes | Y coordinate of the top-left corner of the target source region (main window client area coordinate system, in pixels) |
| srcW | Real | yes | Width of the target source region (in pixels) |
| srcH | Real | yes | Height of the target source region (in pixels) |
| durationMs | Real | yes | Duration of this animation segment, in milliseconds; pass 0 to skip the transition and snap into place when the command starts |

## Returns

| Value | Description |
|----|------|
| 1 | Command added successfully |
| 0 | Add failed: invalid splitId, not recording, or the command count has reached the limit of 32; or non-Windows platform (fallback return value of the GML wrapper) |

## Usage

- Prerequisite: `qiumingdll_winsplit_batch_begin` must have been called to enter recording state, and `qiumingdll_winsplit_batch_end` must not have been called yet.
- Platform support: Windows only; on other platforms the GML wrapper returns 0 directly.
- This command only changes the source region (the picture content is "panned/scaled" in the frame), not the window position or size; the effect is similar to panning the viewfinder across a camera picture.
- The source animation mode is not used (the mode has no effect on this command), and no other state outside the window is consumed.
- Easing is taken from the batch easing curve set when the command was added.
- The start state of a command is the source region at the moment the command begins; commands join end to end in order.

## Example

```gml
// Key event: record a "viewfinder pans right, then back to center" sequence
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_batch_begin(global.splitId);
    // the main window client area is 640x480; first move the viewfinder to the right side
    qiumingdll_winsplit_batch_add_src_region(global.splitId, 320, 0, 320, 480, 500);
    qiumingdll_winsplit_batch_add_wait(global.splitId, 300);
    // viewfinder back to center
    qiumingdll_winsplit_batch_add_src_region(global.splitId, 160, 0, 320, 480, 500);
    qiumingdll_winsplit_batch_end(global.splitId);
    qiumingdll_winsplit_batch_play(global.splitId, 1);
}
```

## Related functions

- [qiumingdll_winsplit_batch_begin](qiumingdll_winsplit_batch_begin.md)
- [qiumingdll_winsplit_batch_set_easing](qiumingdll_winsplit_batch_set_easing.md)
- [qiumingdll_winsplit_batch_add_size](qiumingdll_winsplit_batch_add_size.md)
- [qiumingdll_winsplit_batch_add_wait](qiumingdll_winsplit_batch_add_wait.md)
- [qiumingdll_winsplit_batch_end](qiumingdll_winsplit_batch_end.md)
