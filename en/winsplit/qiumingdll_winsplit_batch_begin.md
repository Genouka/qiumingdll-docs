# qiumingdll_winsplit_batch_begin(splitId)

Starts recording a batch animation sequence for the given split window; subsequent batch_add_* commands accumulate in order on top of it.

## Signature

```gml
qiumingdll_winsplit_batch_begin(splitId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window number, starting from 1, maximum 16 |

## Returns

| Value | Description |
|----|------|
| 1 | Recording started |
| 0 | Invalid splitId (the split window does not exist); or non-Windows platform (fallback return value of the GML wrapper) |

## Usage

- Prerequisite: initialize the module and create a split window first (qiumingdll_winsplit_init / qiumingdll_winsplit_create).
- Platform support: Windows only; on other platforms the GML wrapper returns 0 directly.
- After the call the window enters "recording" state: existing commands are cleared (at most 32) and any batch playback currently running is stopped.
- batch_play cannot be called while recording (it returns 0); batch_end must come first.
- When recording starts, the initial batch easing curve is taken from the current normal animation curve of that window (ease-in-out by default), and the initial source animation mode is reset to 0 (none); both can be changed during recording with batch_set_easing / batch_set_src_anim_mode.
- Typical full flow: batch_begin → batch_add_* (several) → batch_end → batch_play (or batch_play_frame_sync + batch_step every frame).

## Example

```gml
// Key event: record a complete batch animation sequence
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_batch_begin(global.splitId);               // 1. start recording
    qiumingdll_winsplit_batch_add_position(global.splitId, 400, 200, 400);  // move in
    qiumingdll_winsplit_batch_add_size(global.splitId, 640, 480, 400);      // zoom up
    qiumingdll_winsplit_batch_add_wait(global.splitId, 500);                 // stay
    qiumingdll_winsplit_batch_add_position(global.splitId, 100, 100, 400);  // move out
    qiumingdll_winsplit_batch_end(global.splitId);                 // 2. end recording
    qiumingdll_winsplit_batch_play(global.splitId, 1);             // 3. play (interrupt mode)
}
```

## Related functions

- [qiumingdll_winsplit_batch_set_easing](qiumingdll_winsplit_batch_set_easing.md)
- [qiumingdll_winsplit_batch_set_src_anim_mode](qiumingdll_winsplit_batch_set_src_anim_mode.md)
- [qiumingdll_winsplit_batch_add_position](qiumingdll_winsplit_batch_add_position.md)
- [qiumingdll_winsplit_batch_end](qiumingdll_winsplit_batch_end.md)
- [qiumingdll_winsplit_batch_play](qiumingdll_winsplit_batch_play.md)
- [qiumingdll_winsplit_batch_clear](qiumingdll_winsplit_batch_clear.md)
