# qiumingdll_winsplit_set_transparent_color(splitId, color)

Set the transparent color key of the specified split window: pixels in the window picture whose color equals this value become fully transparent (punched through), while all other pixels display normally. Can be combined with overall opacity (`set_opacity`).

## Signature

```gml
qiumingdll_winsplit_set_transparent_color(splitId, color)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window ID, value 1 ~ 16, must exist |
| color | Real | yes | Color value of the transparent key, interpreted as a 24-bit COLORREF in `0x00BBGGRR` form (the high byte is ignored; only the low 24 bits `0x00FFFFFF` are used); you may pass a color produced by `make_color_rgb(r, g, b)` directly (GML colors are `0xRRGGBB`; after passing in, the low 24 bits are used internally, and the blue and red components are interpreted in COLORREF order — see the usage notes below) |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully (the color key is enabled and takes effect immediately) |
| 0 | Failed: `splitId` is invalid or does not exist; on non-Windows platforms the wrapper returns `0` directly |

## Usage

- Prerequisite: `qiumingdll_winsplit_init()` has been called successfully, and the split window corresponding to `splitId` exists.
- The color key is implemented via the layered window's `LWA_COLORKEY`: only pixels "equal to" that color are transparent, others are opaque; it is a pixel-exact color removal, and is a separate capability from `set_opacity`'s overall alpha blending — the two do not affect each other.
- Color order convention: Windows `COLORREF` is `0x00BBGGRR` (blue, green, red). This function uses `color & 0x00FFFFFF` internally as the color key. If you pass a value from GML's `make_color_rgb(r, g, b)` (whose value is `0xRRGGBB`) directly, the red and blue components are interpreted in COLORREF's `BGR` order — that is, the color actually removed is `(b, g, r)` rather than `(r, g, b)`. When you need to match a specific pixel color exactly, construct the value yourself in `0x00BBGGRR` form (e.g. to remove pure red, pass `0x000000FF`).
- Calling this function also turns on the window's "transparent color key switch"; if you want to temporarily disable it while keeping the color value, use `qiumingdll_winsplit_enable_transparent_color(splitId, false)`.
- The transparent color key and overall opacity can take effect simultaneously: first use `set_transparent_color` to remove specific colors, then `set_opacity` for overall translucency; the two stack.
- After canceling the transparent color key the window returns to normal opaque rendering (the system automatically removes the layered window style, for the best performance).

## Example

```gml
// Punch out "pure black" in split window 1 (0x000000FF = pure red in COLORREF; note the BGR order)
// as transparent, achieving a shaped display that "uses black as a mask"
qiumingdll_winsplit_set_transparent_color(global.split_1, 0x000000FF);
```

```gml
// Construct a true pure-blue (RGB 0,0,255) color key: BGR = 0xFF0000
var _key = 0x00FF0000;  // In COLORREF 0x00BBGGRR => B=FF,G=00,R=00 => pure blue
qiumingdll_winsplit_set_transparent_color(global.split_1, _key);

// Temporarily disable the color key (the color value is kept; it can be re-enabled directly next time)
qiumingdll_winsplit_enable_transparent_color(global.split_1, false);

// Re-enable
qiumingdll_winsplit_enable_transparent_color(global.split_1, true);
```

## Related functions

- [qiumingdll_winsplit_enable_transparent_color](qiumingdll_winsplit_enable_transparent_color.md)
- [qiumingdll_winsplit_set_opacity](qiumingdll_winsplit_set_opacity.md)
- [qiumingdll_winsplit_set_shape_from_bitmap](qiumingdll_winsplit_set_shape_from_bitmap.md)
