# qiumingdll_winsplit_set_position(splitId, x, y)

Moves the given split window to a new position on screen: only the position changes, not the size, source region or other properties.

## Signature

```gml
qiumingdll_winsplit_set_position(splitId, x, y)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window ID, value 1 ~ 16, must exist |
| x | Real | yes | New top-left X of the window, pixels, screen coordinates (top-left of the primary display is 0,0); may be negative or outside the screen |
| y | Real | yes | New top-left Y of the window, pixels, screen coordinates; may be negative or outside the screen |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Failed: splitId is invalid or does not exist; on non-Windows platforms the wrapper returns 0 directly |

## Usage

- Prerequisite: `qiumingdll_winsplit_init()` has been called successfully and the split window for splitId exists.
- Coordinate system: x/y are screen pixel coordinates (physical display coordinates), consistent with GameMaker's display coordinates; they are not game-window client-area coordinates.
- What moves is the top-left corner of the window frame (including the titlebar when present), so the rendered area (client area) shifts along with it.
- The move takes effect immediately; for smooth movement see the animation functions.
- If the split window is playing a position animation, calling this function conflicts with the animation; stop the animation first.

## Example

```gml
// In the Step event of a controller object: press 1/2/3 to move split window 1 to different preview positions
if (keyboard_check_pressed(ord("1")))
    qiumingdll_winsplit_set_position(global.split_1, 50, 50);

if (keyboard_check_pressed(ord("2")))
    qiumingdll_winsplit_set_position(global.split_1, 800, 50);

if (keyboard_check_pressed(ord("3")))
    qiumingdll_winsplit_set_position(global.split_1, 800, 500);
```

## Related functions

- [qiumingdll_winsplit_set_size](qiumingdll_winsplit_set_size.md)
- [qiumingdll_winsplit_set_region](qiumingdll_winsplit_set_region.md)
- [qiumingdll_winsplit_get_info](qiumingdll_winsplit_get_info.md)
- [qiumingdll_winsplit_set_draggable](qiumingdll_winsplit_set_draggable.md)
