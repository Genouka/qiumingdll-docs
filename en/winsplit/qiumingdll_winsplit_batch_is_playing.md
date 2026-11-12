# qiumingdll_winsplit_batch_is_playing(splitId)

Queries whether the given split window is currently playing a batch animation (both timer mode and frame-sync mode count).

## Signature

```gml
qiumingdll_winsplit_batch_is_playing(splitId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window number, starting from 1, maximum 16 |

## Returns

| Value | Description |
|----|------|
| 1 | A batch is playing |
| 0 | No batch is playing; or invalid splitId; or non-Windows platform (fallback return value of the GML wrapper) |

## Usage

- Prerequisite: initialize the module and create a split window first (qiumingdll_winsplit_init / qiumingdll_winsplit_create).
- Platform support: Windows only; on other platforms the GML wrapper returns 0 directly (indistinguishable from "not playing").
- Both ways of starting playback report 1: batch_play (timer driven) and batch_play_frame_sync (frame-sync driven) are both reflected in this state.
- It returns to 0 after playback finishes naturally, is stopped by batch_stop, or is cleared by batch_clear.
- It only reflects batch state, not normal animations; use qiumingdll_winsplit_is_animating for normal animations.

## Example

```gml
// Key event: start a new playback only when no batch is playing (to avoid conflicts)
if (keyboard_check_pressed(vk_enter))
{
    if (qiumingdll_winsplit_batch_is_playing(global.splitId) == 0)
    {
        qiumingdll_winsplit_batch_begin(global.splitId);
        qiumingdll_winsplit_batch_add_position(global.splitId, 400, 300, 800);
        qiumingdll_winsplit_batch_end(global.splitId);
        qiumingdll_winsplit_batch_play(global.splitId, 1);
    }
    else
    {
        show_debug_message("Batch is playing, ignoring this request");
    }
}
```

## Related functions

- [qiumingdll_winsplit_batch_play](qiumingdll_winsplit_batch_play.md)
- [qiumingdll_winsplit_batch_play_frame_sync](qiumingdll_winsplit_batch_play_frame_sync.md)
- [qiumingdll_winsplit_batch_stop](qiumingdll_winsplit_batch_stop.md)
- [qiumingdll_winsplit_is_animating](qiumingdll_winsplit_is_animating.md)
