# qiumingdll_winsplit_batch_add_wait(splitId, durationMs)

Adds a "wait in place" command to the batch recording: during playback the window keeps its current state unchanged for durationMs milliseconds, then continues with the next command.

## Signature

```gml
qiumingdll_winsplit_batch_add_wait(splitId, durationMs)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window number, starting from 1, maximum 16 |
| durationMs | Real | yes | Wait duration, in milliseconds; pass 0 for no wait and move on to the next command immediately |

## Returns

| Value | Description |
|----|------|
| 1 | Command added successfully |
| 0 | Add failed: invalid splitId, not recording, or the command count has reached the limit of 32; or non-Windows platform (fallback return value of the GML wrapper) |

## Usage

- Prerequisite: `qiumingdll_winsplit_batch_begin` must have been called to enter recording state, and `qiumingdll_winsplit_batch_end` must not have been called yet.
- Platform support: Windows only; on other platforms the GML wrapper returns 0 directly.
- During the wait the window position, size and source region all stay unchanged (no interpolation at all).
- A wait command does not change the end state of the window; the "end state" computation (used for the fastforward conflict mode) skips wait commands.
- Useful for inserting a pause between two animations so the viewer can see the intermediate state.

## Example

```gml
// Key event: record a complete "move in -> wait 1 second -> move out" sequence
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_batch_begin(global.splitId);
    qiumingdll_winsplit_batch_add_position(global.splitId, 400, 300, 500);  // move in within 500ms
    qiumingdll_winsplit_batch_add_wait(global.splitId, 1000);               // wait in place for 1 second
    qiumingdll_winsplit_batch_add_position(global.splitId, 100, 100, 500);  // move out within 500ms
    qiumingdll_winsplit_batch_end(global.splitId);
    qiumingdll_winsplit_batch_play(global.splitId, 1);
}
```

## Related functions

- [qiumingdll_winsplit_batch_begin](qiumingdll_winsplit_batch_begin.md)
- [qiumingdll_winsplit_batch_add_position](qiumingdll_winsplit_batch_add_position.md)
- [qiumingdll_winsplit_batch_add_region](qiumingdll_winsplit_batch_add_region.md)
- [qiumingdll_winsplit_batch_end](qiumingdll_winsplit_batch_end.md)
