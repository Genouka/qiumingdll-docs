# qiumingdll_winself_set_shape_from_bitmap(bitmapPath, transColor)

Use a bitmap (BMP) as the shape template for the game's own window: pixels whose color equals `transColor` become transparent (holes) on the window, while all other pixels remain visible. This clips the window precisely to any figure (such as a character silhouette, circle or star).

## Signature

```gml
qiumingdll_winself_set_shape_from_bitmap(bitmapPath, transColor)
```

> The window handle is taken internally from `window_handle()`; it does not need to be passed explicitly.

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| bitmapPath | string | yes | Path to the BMP file (ideally the same size as the window client area, 32bpp preferred) |
| transColor | real | yes | Color value treated as the "transparent color", BGR packed into an integer (e.g. 0x00BBGGRR); pixels in the bitmap equal to this color are punched out |

## Returns

| Value | Description |
|----|------|
| `1` | Bitmap shape applied successfully |
| `0` | Failure: invalid window handle, empty path, or bitmap load failure; on non-Windows platforms the wrapper returns `0` directly |

## Usage

- Prerequisite: call on Windows with the game window already present; the BMP file must be readable by the process with `LR_LOADFROMFILE` (mind the working directory and permissions).
- The bitmap's pixel dimensions determine the effective display region of the window; it is recommended that the bitmap match the window client-area size, otherwise the transparent region is applied using bitmap pixel coordinates (client-area coordinate system).
- Color comparison uses 24-bit color (alpha is ignored); pass `transColor` in 0x00BBGGRR form.
- This shape replaces any shape set previously; `qiumingdll_winself_clear_shape` restores the rectangle.

## Example

```gml
// Punch holes for pixels colored white (0x00FFFFFF) in circle_mask.bmp and keep the rest
qiumingdll_winself_set_shape_from_bitmap("circle_mask.bmp", 0x00FFFFFF);
```

## Related functions

- [qiumingdll_winself_set_shape_ellipse](qiumingdll_winself_set_shape_ellipse.md)
- [qiumingdll_winself_set_shape_roundrect](qiumingdll_winself_set_shape_roundrect.md)
- [qiumingdll_winself_clear_shape](qiumingdll_winself_clear_shape.md)
