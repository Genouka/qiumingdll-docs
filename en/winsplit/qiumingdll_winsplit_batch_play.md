# qiumingdll_winsplit_batch_play(splitId, conflictMode)

Plays the recorded batch animation sequence of the given split window; driven by an internal 16ms timer, independent of the game frame rate.

## Signature

```gml
qiumingdll_winsplit_batch_play(splitId, conflictMode)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window number, starting from 1, maximum 16 |
| conflictMode | Real | yes | How to handle a conflict with a batch that is already playing, range 0~3, see the table below |

Conflict mode enum:

| Value | Name | Description |
|----|------|------|
| 0 | stack | Queue and wait: the currently playing batch is not stopped; this request is handled right after it |
| 1 | interrupt | Interrupt immediately: stop the currently playing batch and play this sequence from the beginning |
| 2 | rollback | Roll back and replay: first roll the window back to the state "before the last playback started", then play this sequence from the beginning |
| 3 | fastforward | Fast forward: first advance the window directly to the "end of the last batch" state, then play this sequence from the beginning |

## Returns

| Value | Description |
|----|------|
| 1 | Playback started (or queued/rolled back/fast-forwarded and then started) |
| 0 | Playback failed: invalid splitId, command count is 0, or still recording (batch_end not called); or non-Windows platform (fallback return value of the GML wrapper) |

## Usage

- Prerequisite: the recording flow must be complete first: batch_begin → batch_add_* → batch_end, with a command count greater than 0.
- Platform support: Windows only; on other platforms the GML wrapper returns 0 directly.
- The playback interval is fixed at 16ms (about a 60fps pace); the accumulated command durations determine the total playback time.
- While a batch plays, normal animations of that window are ignored (the batch takes priority); use batch_stop to stop it midway.
- When exact synchronization with the game frame rate is required, use batch_play_frame_sync + batch_step driven every frame instead.
- Commands are kept after playback ends and can be played again; use batch_clear to clear them.
- If you want strictly "queued" semantics, waiting for the previous batch to finish, it is recommended to poll batch_is_playing first and call this function once playback has ended.

## Example

```gml
// Key event: record and play a "fly in - stay - fly out" sequence
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_batch_begin(global.splitId);
    qiumingdll_winsplit_batch_add_position(global.splitId, 400, 300, 500);
    qiumingdll_winsplit_batch_add_wait(global.splitId, 500);
    qiumingdll_winsplit_batch_add_position(global.splitId, 800, 600, 500);
    qiumingdll_winsplit_batch_end(global.splitId);
    qiumingdll_winsplit_batch_play(global.splitId, 1);  // interrupt: play from the beginning immediately
}
```

## Related functions

- [qiumingdll_winsplit_batch_begin](qiumingdll_winsplit_batch_begin.md)
- [qiumingdll_winsplit_batch_end](qiumingdll_winsplit_batch_end.md)
- [qiumingdll_winsplit_batch_play_frame_sync](qiumingdll_winsplit_batch_play_frame_sync.md)
- [qiumingdll_winsplit_batch_stop](qiumingdll_winsplit_batch_stop.md)
- [qiumingdll_winsplit_batch_is_playing](qiumingdll_winsplit_batch_is_playing.md)
