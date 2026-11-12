# qiumingdll_winsplit_set_region(splitId, x, y, w, h)

Sets the position and size of the given split window in one call (combines set_position and set_size).

## Signature

```gml
qiumingdll_winsplit_set_region(splitId, x, y, w, h)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window ID, value 1 ~ 16, must exist |
| x | Real | yes | New top-left X of the window, pixels, screen coordinates |
| y | Real | yes | New top-left Y of the window, pixels, screen coordinates |
| w | Real | yes | New client-area width in pixels, must be greater than 0 |
| h | Real | yes | New client-area height in pixels, must be greater than 0 |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Failed: splitId is invalid or does not exist; on non-Windows platforms the wrapper returns 0 directly |

## Usage

- Prerequisite: `qiumingdll_winsplit_init()` has been called successfully and the split window for splitId exists.
- Equivalent to calling `set_position(splitId, x, y)` followed by `set_size(splitId, w, h)`, but done in one step with no intermediate state.
- Coordinate system and units: x/y are screen pixel coordinates; w/h are client-area (rendered area) pixel sizes, so the window frame is slightly larger due to the titlebar/border.
- Suitable for the initial layout or for switching between whole placement schemes (for example from a "2-screen layout" to a "4-screen layout").
- If the split window is playing an animation, calling this function conflicts with it; stop the animation first.

## Example

```gml
// Define two layouts in the Create event of a controller object and switch them with Tab in the Step event
// Layout 1: the split window occupies a band on the right side of the main window
if (global.layout_tab == 0)
    qiumingdll_winsplit_set_region(global.split_1, 1280, 100, 400, 300);
else
    // Layout 2: the split window occupies the area directly below the main window
    qiumingdll_winsplit_set_region(global.split_1, 400, 900, 800, 450);
```

```gml
// Switch layouts in the Step event of a controller object
if (keyboard_check_pressed(vk_tab))
    global.layout_tab = !global.layout_tab;
```

## Related functions

- [qiumingdll_winsplit_set_position](qiumingdll_winsplit_set_position.md)
- [qiumingdll_winsplit_set_size](qiumingdll_winsplit_set_size.md)
- [qiumingdll_winsplit_get_info](qiumingdll_winsplit_get_info.md)
- [qiumingdll_winsplit_create](qiumingdll_winsplit_create.md)
