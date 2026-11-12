# qiumingdll_winsplit_batch_play_frame_sync(splitId, conflictMode)

Plays the batch animation of the given split window in "frame-sync" mode: no internal timer is created, the caller must call batch_step every frame to advance it, so progress matches the game frame rate exactly.

## Signature

```gml
qiumingdll_winsplit_batch_play_frame_sync(splitId, conflictMode)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window number, starting from 1, maximum 16 |
| conflictMode | Real | yes | How to handle a conflict with a batch that is already playing, with the same values as batch_play: 0=stack queue and wait, 1=interrupt stop immediately, 2=rollback roll back to the state before the last playback, 3=fastforward advance to the end state of the last playback |

## Returns

| Value | Description |
|----|------|
| 1 | Playback started |
| 0 | Playback failed: invalid splitId, command count is 0, or still recording (batch_end not called); or non-Windows platform (fallback return value of the GML wrapper) |

## Usage

- Prerequisite: the recording flow must be complete first (batch_begin → batch_add_* → batch_end).
- Platform support: Windows only; on other platforms the GML wrapper returns 0 directly.
- Difference from batch_play: this function starts no timer. If the caller does not call qiumingdll_winsplit_batch_step every frame, the batch stays on the first frame and never advances by itself.
- Recommended usage: call batch_step every frame in the Step event until it returns 0 (playback finished).
- Command durations are still in milliseconds and progress is interpolated by system time; the higher the frame rate, the smaller the interpolation step per frame.
- All other behavior (conflict modes, command order, source region follow, end state computation) matches batch_play.

## Example

```gml
// Key event: start playback in frame-sync mode
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_batch_begin(global.splitId);
    qiumingdll_winsplit_batch_add_position(global.splitId, 400, 300, 600);
    qiumingdll_winsplit_batch_add_wait(global.splitId, 400);
    qiumingdll_winsplit_batch_add_position(global.splitId, 100, 100, 600);
    qiumingdll_winsplit_batch_end(global.splitId);
    qiumingdll_winsplit_batch_play_frame_sync(global.splitId, 1);  // no timer is started
}

// Step event: advance the batch every frame; a return of 0 means playback has finished
if (qiumingdll_winsplit_batch_step(global.splitId) == 0)
{
    // playback finished (or was not playing); follow-up logic can be triggered here
}
```

## Related functions

- [qiumingdll_winsplit_batch_step](qiumingdll_winsplit_batch_step.md)
- [qiumingdll_winsplit_batch_play](qiumingdll_winsplit_batch_play.md)
- [qiumingdll_winsplit_batch_stop](qiumingdll_winsplit_batch_stop.md)
- [qiumingdll_winsplit_batch_is_playing](qiumingdll_winsplit_batch_is_playing.md)
