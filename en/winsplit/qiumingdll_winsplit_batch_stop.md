# qiumingdll_winsplit_batch_stop(splitId)

Stop the batch animation currently playing on the specified split window midway; the window stays in the state it was in when stopped.

## Signature

```gml
qiumingdll_winsplit_batch_stop(splitId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window ID, starting from 1, maximum 16 |

## Returns

| Value | Description |
|----|------|
| 1 | Call succeeded (regardless of whether it was playing before) |
| 0 | Invalid splitId (the split window does not exist); or non-Windows platform (fallback return value of the GML wrapper) |

## Usage

- Preconditions: you must first initialize and create a split window (`qiumingdll_winsplit_init` / `qiumingdll_winsplit_create`).
- Platform limit: Windows only; on other platforms this GML wrapper returns 0 directly.
- After stopping, the window stays at the current interpolated position/size and does not jump to the final state of the batch.
- Timer-mode playback (`batch_play`) also stops its internal timer; after frame-sync playback (`batch_play_frame_sync`) is stopped, further calls to `batch_step` return 0.
- Only affects batch animations; use `qiumingdll_winsplit_stop_animation` to stop normal animations.
- Stopping does not clear the recorded commands; afterwards you can call `batch_play` again to play from the beginning.
- To discard the batch entirely, use `qiumingdll_winsplit_batch_clear`.

## Example

```gml
// Key event: start playing a 10-second long sequence
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_batch_begin(global.splitId);
    qiumingdll_winsplit_batch_add_position(global.splitId, 400, 300, 5000);
    qiumingdll_winsplit_batch_add_position(global.splitId, 100, 100, 5000);
    qiumingdll_winsplit_batch_end(global.splitId);
    qiumingdll_winsplit_batch_play(global.splitId, 1);
}

// Key event: stop midway
if (keyboard_check_pressed(vk_x))
{
    qiumingdll_winsplit_batch_stop(global.splitId);
}
```

## Related functions

- [qiumingdll_winsplit_batch_play](qiumingdll_winsplit_batch_play.md)
- [qiumingdll_winsplit_batch_play_frame_sync](qiumingdll_winsplit_batch_play_frame_sync.md)
- [qiumingdll_winsplit_batch_is_playing](qiumingdll_winsplit_batch_is_playing.md)
- [qiumingdll_winsplit_batch_clear](qiumingdll_winsplit_batch_clear.md)
- [qiumingdll_winsplit_stop_animation](qiumingdll_winsplit_stop_animation.md)
