# qiumingdll_winsplit_set_size(splitId, w, h)

Change the display size of the specified split window. Only the size changes; the position, source region, and other properties are left untouched.

## Signature

```gml
qiumingdll_winsplit_set_size(splitId, w, h)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | real | yes | Split window ID, in the range 1 ~ 16; the window must exist |
| w | real | yes | New client-area width in pixels; must be greater than 0. The outer window width is this value plus the border (and title bar, if present) |
| h | real | yes | New client-area height in pixels; must be greater than 0. The outer window height is this value plus the border (and title bar, if present) |

## Returns

| Value | Description |
|----|------|
| `1` | Set successfully |
| `0` | Failure: `splitId` is invalid or does not exist; on non-Windows platforms the wrapper returns `0` directly |

## Usage

- Prerequisite: `qiumingdll_winsplit_init()` has been called successfully, and the split window identified by `splitId` exists.
- `w` / `h` are the dimensions of the split window's client area (the rendered picture area); `dstW` / `dstH` at creation time have the same meaning. Because of the title bar and border, the actual outer window is slightly larger than `w` / `h`.
- After resizing, the source-region content is stretched to fit the new client area (the default stretch mode scales it; content is not cropped).
- The position (top-left corner) stays fixed, so the window grows or shrinks toward the bottom-right.
- If the split window is currently playing a size animation, calling this function directly conflicts with the animation; stop the animation first.

## Example

```gml
// In the Step event of a controller object: press = to enlarge split window 1 to 960x540, press - to shrink it back to 640x360
if (keyboard_check_pressed(vk_add) || keyboard_check_pressed(vk_equals))
    qiumingdll_winsplit_set_size(global.split_1, 960, 540);

if (keyboard_check_pressed(vk_subtract) || keyboard_check_pressed(vk_minus))
    qiumingdll_winsplit_set_size(global.split_1, 640, 360);
```

## Related functions

- [qiumingdll_winsplit_set_position](qiumingdll_winsplit_set_position.md)
- [qiumingdll_winsplit_set_region](qiumingdll_winsplit_set_region.md)
- [qiumingdll_winsplit_get_info](qiumingdll_winsplit_get_info.md)
- [qiumingdll_winsplit_set_titlebar](qiumingdll_winsplit_set_titlebar.md)
