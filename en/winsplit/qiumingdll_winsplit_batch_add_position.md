# qiumingdll_winsplit_batch_add_position(splitId, x, y, durationMs)

Adds a "move position" command to the batch recording: during playback the window interpolates from its current position to the target position (x, y) within durationMs milliseconds.

## Signature

```gml
qiumingdll_winsplit_batch_add_position(splitId, x, y, durationMs)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window number, starting from 1, maximum 16 |
| x | Real | yes | Target X coordinate (screen coordinate system, in pixels), where the top-left corner of the window should move to |
| y | Real | yes | Target Y coordinate (screen coordinate system, in pixels) |
| durationMs | Real | yes | Duration of this animation segment, in milliseconds; pass 0 to skip the transition and snap into place when the command starts |

## Returns

| Value | Description |
|----|------|
| 1 | Command added successfully |
| 0 | Add failed: invalid splitId, not recording, or the command count has reached the limit of 32; or non-Windows platform (fallback return value of the GML wrapper) |

## Usage

- Prerequisite: `qiumingdll_winsplit_batch_begin` must have been called to enter recording state, and `qiumingdll_winsplit_batch_end` must not have been called yet.
- Platform support: Windows only; on other platforms the GML wrapper returns 0 directly.
- This command does not change the window size or the source region, it only moves the position.
- The start state of a command is the window state at the moment the command begins (i.e. the end state of the previous command), so commands join end to end in order.
- Easing is taken from the batch easing curve set when the command was added (see qiumingdll_winsplit_batch_set_easing).
- Each command snapshots the mode and easing at the time it is added; changes made during recording do not affect commands already added.
- During playback the commands run in order; a whole recording holds at most 32 commands.

## Example

```gml
// Key event: record a complete "move - wait - move" sequence (this function provides the two move commands)
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_batch_begin(global.splitId);
    qiumingdll_winsplit_batch_add_position(global.splitId, 400, 200, 400);  // move to (400,200) within 400ms
    qiumingdll_winsplit_batch_add_wait(global.splitId, 300);                // wait in place for 300ms
    qiumingdll_winsplit_batch_add_position(global.splitId, 100, 100, 400);  // move to (100,100) within 400ms
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
