# qiumingdll_winsplit_set_stretch_mode(mode)

Set the GDI stretch mode used when the split window picture and the window size do not match (affects only image quality during scaled rendering; global setting).

## Signature

```gml
qiumingdll_winsplit_set_stretch_mode(mode)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| mode | Real | yes | Stretch mode, value range 0~1, meanings in the table below |

| Value | Name | Description |
|----|------|------|
| 0 | COLORONCOLOR | Fast stretching (default). Better performance, but edges may show aliasing when enlarged |
| 1 | HALFTONE | High-quality stretching. Smoother picture, but higher performance cost |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | The platform is not Windows (fallback return value of the GML wrapper) |

## Usage

- Prerequisite: recommended to call after `qiumingdll_winsplit_init` and before creating split windows (it is a global setting and takes effect whenever called).
- Platform limit: Windows only; on other platforms the GML wrapper returns `0` directly.
- This function is still valid (not a deprecated API): when the split window's source region size differs from the window's client area size (i.e. a StretchBlt scaling occurs), it determines the GDI stretch algorithm used for scaling.
- Global setting; affects all split windows.
- Note: negative values are clamped to 0; any value other than 1 is treated as 0 (COLORONCOLOR).
- When the source region size equals the window size no scaling occurs, and this setting has no effect.

## Example

```gml
// Create event: enable high-quality stretching and create the split window
qiumingdll_winsplit_init();
qiumingdll_winsplit_set_stretch_mode(1);  // HALFTONE high-quality stretching

// Source region 320x240, window 640x480; smooth stretching is used when the picture is enlarged
global.splitId = qiumingdll_winsplit_create(0, 0, 320, 240, 100, 100, 640, 480);
```

## Related functions

- [qiumingdll_winsplit_set_capture_mode](qiumingdll_winsplit_set_capture_mode.md) (deprecated)
- [qiumingdll_winsplit_set_render_during_drag](qiumingdll_winsplit_set_render_during_drag.md)
- [qiumingdll_winsplit_set_position_animate](qiumingdll_winsplit_set_position_animate.md)
