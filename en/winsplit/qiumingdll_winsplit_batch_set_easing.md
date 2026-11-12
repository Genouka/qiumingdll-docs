# qiumingdll_winsplit_batch_set_easing(splitId, easing)

Sets the easing curve used by subsequent commands (batch_add_*) in the batch recording of the given split window.

## Signature

```gml
qiumingdll_winsplit_batch_set_easing(splitId, easing)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window number, starting from 1, maximum 16 |
| easing | Real | yes | Easing curve enum, range 0~11, sharing the same enum as qiumingdll_winsplit_set_easing_curve (0=linear, 1=ease-in, 2=ease-out, 3=ease-in-out, 4=in-cubic, 5=out-cubic, 6=in-out-cubic, 7=in-back, 8=out-back, 9=in-out-back, 10=bounce-out, 11=elastic-out) |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Invalid splitId (the split window does not exist); or non-Windows platform (fallback return value of the GML wrapper) |

## Usage

- Prerequisite: initialize the module and create a split window first (qiumingdll_winsplit_init / qiumingdll_winsplit_create); normally called between qiumingdll_winsplit_batch_begin and qiumingdll_winsplit_batch_end.
- Platform support: Windows only; on other platforms the GML wrapper returns 0 directly.
- Each batch_add_* command "snapshots" the easing curve at the time it is added, so different easings can be switched at different points of the same recording, producing combined effects such as "constant speed first, bouncing at the end".
- Calling it outside recording also changes the current easing, but does not affect commands already added.
- At the start of recording the initial value is the current curve of the window's normal animation (ease-in-out by default); it usually needs no extra setup.

## Example

```gml
// Key event: record an entrance animation sequence that starts slowly and bounces at the end
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_batch_begin(global.splitId);
    qiumingdll_winsplit_batch_set_easing(global.splitId, 1);    // ease-in, slow start
    qiumingdll_winsplit_batch_add_position(global.splitId, 400, 300, 600);
    qiumingdll_winsplit_batch_set_easing(global.splitId, 10);   // bounce-out, bouncing finish
    qiumingdll_winsplit_batch_add_size(global.splitId, 640, 480, 600);
    qiumingdll_winsplit_batch_end(global.splitId);
    qiumingdll_winsplit_batch_play(global.splitId, 1);
}
```

## Related functions

- [qiumingdll_winsplit_batch_begin](qiumingdll_winsplit_batch_begin.md)
- [qiumingdll_winsplit_set_easing_curve](qiumingdll_winsplit_set_easing_curve.md)
- [qiumingdll_winsplit_batch_add_position](qiumingdll_winsplit_batch_add_position.md)
- [qiumingdll_winsplit_batch_add_size](qiumingdll_winsplit_batch_add_size.md)
- [qiumingdll_winsplit_batch_end](qiumingdll_winsplit_batch_end.md)
