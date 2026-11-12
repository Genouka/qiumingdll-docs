# qiumingdll_winsplit_batch_clear(splitId)

Stops the batch animation playing on the given split window, clears all of its recorded commands and leaves recording mode.

## Signature

```gml
qiumingdll_winsplit_batch_clear(splitId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window number, starting from 1, maximum 16 |

## Returns

| Value | Description |
|----|------|
| 1 | Cleared successfully |
| 0 | Invalid splitId (the split window does not exist); or non-Windows platform (fallback return value of the GML wrapper) |

## Usage

- Prerequisite: initialize the module and create a split window first (qiumingdll_winsplit_init / qiumingdll_winsplit_create).
- Platform support: Windows only; on other platforms the GML wrapper returns 0 directly.
- Effect: if playback is running it stops immediately (including the internal timer); the command count is reset to zero; recording state is left (recording = false).
- The window stays at its current position/size; it does not move or jump.
- Difference from batch_stop: stop only stops playback and keeps the commands; clear also deletes all commands.
- After clearing, call batch_begin again to record a new sequence.

## Example

```gml
// Key event: clear the old batch and record a brand-new sequence
if (keyboard_check_pressed(vk_r))
{
    qiumingdll_winsplit_batch_clear(global.splitId);  // stop playback + clear commands
    qiumingdll_winsplit_batch_begin(global.splitId);
    qiumingdll_winsplit_batch_add_region(global.splitId, 200, 150, 640, 480, 600);
    qiumingdll_winsplit_batch_add_wait(global.splitId, 400);
    qiumingdll_winsplit_batch_add_region(global.splitId, 100, 100, 320, 240, 600);
    qiumingdll_winsplit_batch_end(global.splitId);
    qiumingdll_winsplit_batch_play(global.splitId, 1);
}
```

## Related functions

- [qiumingdll_winsplit_batch_begin](qiumingdll_winsplit_batch_begin.md)
- [qiumingdll_winsplit_batch_end](qiumingdll_winsplit_batch_end.md)
- [qiumingdll_winsplit_batch_stop](qiumingdll_winsplit_batch_stop.md)
- [qiumingdll_winsplit_batch_play](qiumingdll_winsplit_batch_play.md)
