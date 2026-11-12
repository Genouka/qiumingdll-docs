# qiumingdll_winself_set_opacity(opacity)

Set the overall opacity of the game's own window (0 = fully transparent, 255 = fully opaque). Out-of-range values are clamped automatically.

## Signature

```gml
qiumingdll_winself_set_opacity(opacity)
```

> The window handle is taken internally from `window_handle()`; it does not need to be passed explicitly.

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| opacity | real | yes | Opacity as an integer from 0 to 255: 0 = fully transparent (invisible but still responsive), 255 = fully opaque; values below 0 are treated as 0 and values above 255 as 255 |

## Returns

| Value | Description |
|----|------|
| `1` | Set successfully |
| `0` | Failure: invalid window handle; on non-Windows platforms the wrapper returns `0` directly |

## Usage

- Prerequisite: call on Windows with the game window already created. The function automatically uses `window_handle()` as the target window.
- Opacity is applied at the "window level": the rendered content, the titlebar and everything else are all made transparent by the same ratio.
- With opacity = 255 the window returns to normal opaque rendering and the system removes the layered-window style automatically (best performance).
- With 0 < opacity < 255 the window switches to layered rendering; alpha blending is done at the system level, and performance and blending quality vary by GPU/OS.
- A fully transparent (0) window still "exists" and still responds to mouse and other events; it is only invisible.
- Opacity and the shape functions do not conflict: you can clip the shape first and then adjust opacity.

## Example

```gml
// Adjust the game window opacity in real time with the mouse wheel (in the Step event)
var _wheel = mouse_wheel_up() - mouse_wheel_down();
if (_wheel != 0)
{
    global.game_alpha = clamp(global.game_alpha + _wheel * 16, 0, 255);
    qiumingdll_winself_set_opacity(global.game_alpha);
}
```

```gml
// Fade the whole game window out/in with the [ and ] keys
if (keyboard_check_pressed(vk_lbracket))
{
    global.game_alpha = max(global.game_alpha - 32, 0);
    qiumingdll_winself_set_opacity(global.game_alpha);
}
if (keyboard_check_pressed(vk_rbracket))
{
    global.game_alpha = min(global.game_alpha + 32, 255);
    qiumingdll_winself_set_opacity(global.game_alpha);
}
```

## Related functions

- [qiumingdll_winself_set_shape_ellipse](qiumingdll_winself_set_shape_ellipse.md)
- [qiumingdll_winself_set_shape_roundrect](qiumingdll_winself_set_shape_roundrect.md)
- [qiumingdll_winself_clear_shape](qiumingdll_winself_clear_shape.md)
