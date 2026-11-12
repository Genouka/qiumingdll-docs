# qiumingdll_winsplit_set_opacity(splitId, opacity)

Sets the overall opacity of the given split window (0 = fully transparent, 255 = fully opaque). Out-of-range values are clamped automatically.

## Signature

```gml
qiumingdll_winsplit_set_opacity(splitId, opacity)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window ID, value 1 ~ 16, must exist |
| opacity | Real | yes | Opacity, integer 0 ~ 255: 0 = fully transparent (invisible but still responsive), 255 = fully opaque; values below 0 are treated as 0 and values above 255 as 255 |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Failed: splitId is invalid or does not exist; on non-Windows platforms the wrapper returns 0 directly |

## Usage

- Prerequisite: `qiumingdll_winsplit_init()` has been called successfully and the split window for splitId exists.
- Opacity is a "window-level" overlay: the rendered content, titlebar and so on all become transparent by the same ratio.
- With opacity = 255 the window returns to normal opaque rendering and the system removes the layered window style automatically (best performance).
- With 0 < opacity < 255 the window switches to layered rendering, so the alpha blending is done at the system level; note that performance and blending quality vary with GPU and OS. For the best visual result, prefer common values such as 128 or 192.
- A fully transparent (0) window still "exists": it still occupies a slot and still responds to mouse events, it is just invisible.
- Opacity and the shape feature do not conflict: you can clip the shape first and then adjust opacity.

## Example

```gml
// In the Step event of a controller object: press [ and ] to fade out/fade in split window 1
if (keyboard_check_pressed(vk_lbracket))
{
    global.split_alpha -= 32;   // fade out a little
    qiumingdll_winsplit_set_opacity(global.split_1, global.split_alpha);
}

if (keyboard_check_pressed(vk_rbracket))
{
    global.split_alpha += 32;   // fade in a little
    qiumingdll_winsplit_set_opacity(global.split_1, global.split_alpha);
}
```

```gml
// Adjust opacity in real time with the mouse wheel (in the Step event)
var _wheel = mouse_wheel_up() - mouse_wheel_down();
if (_wheel != 0)
{
    global.split_alpha = clamp(global.split_alpha + _wheel * 16, 0, 255);
    qiumingdll_winsplit_set_opacity(global.split_1, global.split_alpha);
}
```

## Related functions

- [qiumingdll_winsplit_set_topmost](qiumingdll_winsplit_set_topmost.md)
- [qiumingdll_winsplit_set_shape_ellipse](qiumingdll_winsplit_set_shape_ellipse.md)
- [qiumingdll_winsplit_set_titlebar](qiumingdll_winsplit_set_titlebar.md)
