# qiumingdll_winsplit_batch_step(splitId)

Advances the "frame-sync" batch animation of the given split window by one frame (only effective for playback started by batch_play_frame_sync) and returns whether playback is still running.

## Signature

```gml
qiumingdll_winsplit_batch_step(splitId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window number, starting from 1, maximum 16 |

## Returns

| Value | Description |
|----|------|
| 1 | The batch is still playing; this function must be called again on the next frame |
| 0 | The batch has finished playing; or no frame-sync batch is currently playing on this window (including timer mode started with batch_play); or invalid splitId; or non-Windows platform (fallback return value of the GML wrapper) |

## Usage

- Prerequisite: frame-sync playback must have been started first with qiumingdll_winsplit_batch_play_frame_sync.
- Platform support: Windows only; on other platforms the GML wrapper returns 0 directly.
- Calling it once per frame is enough; interpolation progress is computed internally from system time, so the call frequency determines smoothness (calling it every frame in the Step event is recommended).
- This function only works in frameSync mode: calling it for timer playback started with batch_play returns 0.
- It returns 0 once playback has finished, so no further calls are needed; commands are kept and can be played again.
- Note: if this function stops being called midway, the batch "freezes" at the current progress and does not finish by itself.

## Example

```gml
// Create event: initialize and create a split window
qiumingdll_winsplit_init();
global.splitId = qiumingdll_winsplit_create(0, 0, 640, 480, 100, 100, 320, 240);

// Key event: record and play in frame-sync mode
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_batch_begin(global.splitId);
    qiumingdll_winsplit_batch_add_size(global.splitId, 640, 480, 800);
    qiumingdll_winsplit_batch_add_position(global.splitId, 400, 300, 800);
    qiumingdll_winsplit_batch_end(global.splitId);
    qiumingdll_winsplit_batch_play_frame_sync(global.splitId, 1);
}

// Step event: advance the frame-sync batch every frame
if (qiumingdll_winsplit_batch_step(global.splitId) == 0)
{
    show_debug_message("Frame-sync batch has finished");
}
```

## Related functions

- [qiumingdll_winsplit_batch_play_frame_sync](qiumingdll_winsplit_batch_play_frame_sync.md)
- [qiumingdll_winsplit_batch_is_playing](qiumingdll_winsplit_batch_is_playing.md)
- [qiumingdll_winsplit_batch_stop](qiumingdll_winsplit_batch_stop.md)
