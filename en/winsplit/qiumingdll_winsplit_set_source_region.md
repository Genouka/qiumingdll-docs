# qiumingdll_winsplit_set_source_region(splitId, srcX, srcY, srcW, srcH)

Change the source region of the specified split window: the area of the original game window's client area that the split window captures (i.e. "which part is shown").

## Signature

```gml
qiumingdll_winsplit_set_source_region(splitId, srcX, srcY, srcW, srcH)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | real | yes | Split window ID, in the range 1 ~ 16; the window must exist |
| srcX | real | yes | X coordinate of the source region's top-left corner, in pixels, relative to the original game window's client area (client-area top-left is 0,0) |
| srcY | real | yes | Y coordinate of the source region's top-left corner, in pixels, relative to the original game window's client area |
| srcW | real | yes | Source region width in pixels; must be greater than 0 |
| srcH | real | yes | Source region height in pixels; must be greater than 0 |

## Returns

| Value | Description |
|----|------|
| `1` | Set successfully |
| `0` | Failure: `splitId` is invalid or does not exist; on non-Windows platforms the wrapper returns `0` directly |

## Usage

- Prerequisite: `qiumingdll_winsplit_init()` has been called successfully, and the split window identified by `splitId` exists.
- The source region is a "camera view" over the screen: the split window behaves like a camera that refreshes in real time with the game picture, and this function moves or zooms that camera's viewfinder.
- Changing the source region does not affect the split window's position or size (the destination region is unchanged); the captured picture is stretched to the split window's client-area size.
- The part of the source region outside the original window's client area has no picture content and is shown as blank.
- Combined with animation or scripts, this enables "look-around" effects: for example, continuously shifting the source region lets the split window display different parts of the game picture.
- At creation time the source region is determined by `srcX` / `srcY` / `srcW` / `srcH` passed to `create`; this function can change it freely afterward.

## Example

```gml
// In the Step event of a controller object: use the arrow keys to move split window 1's "viewfinder" around the main window
var _cw = window_get_width();
var _ch = window_get_height();
var _sw = 400; // Viewfinder width (source region width)
var _sh = 225; // Viewfinder height

global.cam_x = clamp(global.cam_x + keyboard_check(vk_right) * 8 - keyboard_check(vk_left) * 8, 0, _cw - _sw);
global.cam_y = clamp(global.cam_y + keyboard_check(vk_down) * 8 - keyboard_check(vk_up) * 8, 0, _ch - _sh);

// Apply the viewfinder position to the split window
qiumingdll_winsplit_set_source_region(global.split_1, global.cam_x, global.cam_y, _sw, _sh);
```

## Related functions

- [qiumingdll_winsplit_create](qiumingdll_winsplit_create.md)
- [qiumingdll_winsplit_get_info](qiumingdll_winsplit_get_info.md)
- [qiumingdll_winsplit_set_region](qiumingdll_winsplit_set_region.md)
