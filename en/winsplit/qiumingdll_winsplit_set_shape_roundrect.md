# qiumingdll_winsplit_set_shape_roundrect(splitId, cornerW, cornerH)

Set the specified split window to a rounded-rectangle shape (the four corners are cut off using the given radii). This is the usual shape for a borderless rounded panel.

## Signature

```gml
qiumingdll_winsplit_set_shape_roundrect(splitId, cornerW, cornerH)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | real | yes | Split window ID, in the range 1 ~ 16; the window must exist |
| cornerW | real | yes | Horizontal radius of the rounded corners (corner width), in pixels, from 0 to the client width; 0 means no rounding |
| cornerH | real | yes | Vertical radius of the rounded corners (corner height), in pixels, from 0 to the client height; 0 means no rounding |

## Returns

| Value | Description |
|----|------|
| `1` | The rounded-rectangle shape was applied successfully |
| `0` | Failure: `splitId` is invalid or does not exist; on non-Windows platforms the wrapper returns `0` directly |

## Usage

- Prerequisite: `qiumingdll_winsplit_init()` has been called successfully, and the split window identified by `splitId` exists.
- `cornerW` / `cornerH` are the semi-axis lengths of the corner ellipses: for example, `(20, 20)` gives 20-pixel rounded corners. Passing 0 for both is equivalent to a rectangle with no rounding (indistinguishable from a rectangular window).
- The four corner areas outside the rounded corners are transparent, and mouse clicks pass through them.
- The shape does not update automatically when the window size changes. After changing the window size with `set_size`, call this function again.
- This shape replaces any previously set shape; `qiumingdll_winsplit_clear_shape` restores the rectangle.

## Example

```gml
// In the Step event of a controller object: press U to turn split window 1 into a rounded panel
if (keyboard_check_pressed(ord("U")))
{
    // Window style with 20-pixel rounded corners
    qiumingdll_winsplit_set_shape_roundrect(global.split_1, 20, 20);
}

// Press 9 for a "capsule" shape (very large vertical rounding), press 0 to restore the rectangle
if (keyboard_check_pressed(ord("9")))
    qiumingdll_winsplit_set_shape_roundrect(global.split_1, 200, 200);

if (keyboard_check_pressed(ord("0")))
    qiumingdll_winsplit_clear_shape(global.split_1);
```

## Related functions

- [qiumingdll_winsplit_set_shape_ellipse](qiumingdll_winsplit_set_shape_ellipse.md)
- [qiumingdll_winsplit_set_shape_from_bitmap](qiumingdll_winsplit_set_shape_from_bitmap.md)
- [qiumingdll_winsplit_clear_shape](qiumingdll_winsplit_clear_shape.md)
