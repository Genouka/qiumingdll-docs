# qiumingdll_winsplit_set_src_anim_mode(splitId, mode)

Set how the source region (the captured area of the main window) follows the split window during size/region animations: keep it unchanged, stretch it proportionally, or crop it against an anchor point.

## Signature

```gml
qiumingdll_winsplit_set_src_anim_mode(splitId, mode)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window number, starting from 1, maximum 16 |
| mode | Real | yes | Source animation mode enum, value range 0~10, meanings in the table below |

Source animation mode enum (shared with `qiumingdll_winsplit_batch_set_src_anim_mode`):

| Value | Name | Description |
|----|------|------|
| 0 | None | The source region stays unchanged (default) |
| 1 | Stretch | The source region scales with the window proportionally: source coordinates and source size are scaled by the ratio "target size / current size" |
| 2 | Crop - top-left (TL) | The anchor is fixed at the top-left corner; the source region expands/contracts toward the bottom-right |
| 3 | Crop - top-center (TC) | The anchor is fixed at the top edge's midpoint; expands left/right and downward |
| 4 | Crop - top-right (TR) | The anchor is fixed at the top-right corner; expands/contracts toward the bottom-left |
| 5 | Crop - middle-left (ML) | The anchor is fixed at the left edge's midpoint; expands right and up/down |
| 6 | Crop - middle-center (MC) | The anchor is fixed at the center; expands symmetrically in all directions |
| 7 | Crop - middle-right (MR) | The anchor is fixed at the right edge's midpoint; expands left and up/down |
| 8 | Crop - bottom-left (BL) | The anchor is fixed at the bottom-left corner; expands/contracts toward the top-right |
| 9 | Crop - bottom-center (BC) | The anchor is fixed at the bottom edge's midpoint; expands upward and left/right |
| 10 | Crop - bottom-right (BR) | The anchor is fixed at the bottom-right corner; expands/contracts toward the top-left |

Crop mode semantics: if the window size change is dW / dH, the source region changes by the same amount (source width = original source width + dW, source height = original source height + dH); the anchor determines the direction of expansion/contraction.

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | `splitId` is invalid (the split window does not exist), or the platform is not Windows (fallback return value of the GML wrapper) |

## Usage

- Prerequisite: the library must be initialized and the split window created first (`qiumingdll_winsplit_init` / `qiumingdll_winsplit_create`).
- Platform limit: Windows only; on other platforms the GML wrapper returns `0` directly.
- Only affects "size" animations: `set_size_animate`, `set_region_animate`; it has no effect on pure position animations (`set_position_animate` forces mode 0 internally).
- The default mode is 0 (the source region stays fixed).
- This setting is persistent state; set it once before the animation starts.
- Crop modes interpolate relative to the source region at the moment the animation starts; set the initial source region first with `qiumingdll_winsplit_set_source_region`.

## Example

```gml
// Create event: create the split window and enable the "stretch" source animation mode
qiumingdll_winsplit_init();

global.splitId = qiumingdll_winsplit_create(0, 0, 640, 480, 100, 100, 320, 240);
if (global.splitId > 0)
{
    // Stretch mode: when the window grows, the source region scales proportionally, i.e. the picture zooms in sync
    qiumingdll_winsplit_set_src_anim_mode(global.splitId, 1);
}

// Key event: enlarge the window to full screen; the source region stretches in sync
if (keyboard_check_pressed(vk_space))
{
    qiumingdll_winsplit_set_size_animate(global.splitId, 640, 480, 1000, 16);
}
```

## Related functions

- [qiumingdll_winsplit_set_easing_curve](qiumingdll_winsplit_set_easing_curve.md)
- [qiumingdll_winsplit_set_size_animate](qiumingdll_winsplit_set_size_animate.md)
- [qiumingdll_winsplit_set_region_animate](qiumingdll_winsplit_set_region_animate.md)
- [qiumingdll_winsplit_batch_set_src_anim_mode](qiumingdll_winsplit_batch_set_src_anim_mode.md)
- [qiumingdll_winsplit_batch_add_size](qiumingdll_winsplit_batch_add_size.md)
