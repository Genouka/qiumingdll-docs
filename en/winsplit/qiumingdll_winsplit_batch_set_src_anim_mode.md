# qiumingdll_winsplit_batch_set_src_anim_mode(splitId, mode)

Sets the source animation mode used by subsequent size-related commands (batch_add_size / batch_add_region) in the batch recording of the given split window.

## Signature

```gml
qiumingdll_winsplit_batch_set_src_anim_mode(splitId, mode)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window number, starting from 1, maximum 16 |
| mode | Real | yes | Source animation mode enum, range 0~10, shared with qiumingdll_winsplit_set_src_anim_mode (0=none, 1=stretch, 2~10=crop anchor: 2=top-left TL, 3=top-center TC, 4=top-right TR, 5=middle-left ML, 6=middle-center MC, 7=middle-right MR, 8=bottom-left BL, 9=bottom-center BC, 10=bottom-right BR) |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Invalid splitId (the split window does not exist); or non-Windows platform (fallback return value of the GML wrapper) |

## Usage

- Prerequisite: initialize the module and create a split window first (qiumingdll_winsplit_init / qiumingdll_winsplit_create); normally called between qiumingdll_winsplit_batch_begin and qiumingdll_winsplit_batch_end.
- Platform support: Windows only; on other platforms the GML wrapper returns 0 directly.
- It only affects size-related commands added afterwards: batch_add_size and batch_add_region; position commands (batch_add_position) and source region commands (batch_add_src_region) do not use this mode.
- Each command "snapshots" the mode at the time it is added, so it can be switched at different points of the same recording.
- At the start of recording the initial value is 0 (none).
- Stretch mode: the source region scales proportionally with the window (the picture content zooms in/out); crop mode: the source region expands/shrinks together with the window size in the anchor direction.

## Example

```gml
// Key event: record a sequence where "the picture zooms together as the window zooms"
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_batch_begin(global.splitId);
    qiumingdll_winsplit_batch_set_src_anim_mode(global.splitId, 1);  // stretch
    qiumingdll_winsplit_batch_add_size(global.splitId, 640, 480, 800);
    qiumingdll_winsplit_batch_set_src_anim_mode(global.splitId, 0);  // back to no follow
    qiumingdll_winsplit_batch_add_position(global.splitId, 200, 200, 400);
    qiumingdll_winsplit_batch_end(global.splitId);
    qiumingdll_winsplit_batch_play(global.splitId, 1);
}
```

## Related functions

- [qiumingdll_winsplit_batch_begin](qiumingdll_winsplit_batch_begin.md)
- [qiumingdll_winsplit_set_src_anim_mode](qiumingdll_winsplit_set_src_anim_mode.md)
- [qiumingdll_winsplit_batch_add_size](qiumingdll_winsplit_batch_add_size.md)
- [qiumingdll_winsplit_batch_add_region](qiumingdll_winsplit_batch_add_region.md)
- [qiumingdll_winsplit_batch_end](qiumingdll_winsplit_batch_end.md)
