# qiumingdll_winsplit_enable_transparent_color(splitId, enable)

Enable or disable the transparent color key feature of the specified split window without changing the already-set color key value. The color key must first be set with `qiumingdll_winsplit_set_transparent_color`; this function then decides whether that color key takes effect.

## Signature

```gml
qiumingdll_winsplit_enable_transparent_color(splitId, enable)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window ID, value 1 ~ 16, must exist |
| enable | Real | yes | Whether to enable the transparent color key: non-zero = on, 0 = off; usually pass `true` / `false` |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully (state toggled) |
| 0 | Failure: splitId is invalid or does not exist; on non-Windows platforms the wrapper returns 0 directly |

## Usage

- Precondition: `qiumingdll_winsplit_init()` has been called successfully, and the split window for splitId exists.
- This function only toggles the "transparent color key switch" and does not affect the color key value set by `qiumingdll_winsplit_set_transparent_color`; after disabling, the color key cache remains, and re-enabling uses the last set color.
- If `set_transparent_color` has never been called, `useColorKey` in the window defaults to off; only after enabling with this function does the default color key (0, i.e. pure black) take effect.
- The transparent color key is based on the layered window's `LWA_COLORKEY`: when enabled, pixels of the corresponding color become transparent; when disabled, rendering returns to normal opaque (the system automatically removes the layered window style, for the best performance).
- Can be combined with overall opacity (`set_opacity`).

## Example

```gml
// First set the color to key out (e.g. pure red COLORREF 0x000000FF), then enable
qiumingdll_winsplit_set_transparent_color(global.split_1, 0x000000FF);
qiumingdll_winsplit_enable_transparent_color(global.split_1, true);

// Toggle according to the switch state in the game
if (global.use_mask)
{
    qiumingdll_winsplit_enable_transparent_color(global.split_1, true);
}
else
{
    qiumingdll_winsplit_enable_transparent_color(global.split_1, false);
}
```

## Related functions

- [qiumingdll_winsplit_set_transparent_color](qiumingdll_winsplit_set_transparent_color.md)
- [qiumingdll_winsplit_set_opacity](qiumingdll_winsplit_set_opacity.md)
- [qiumingdll_winsplit_set_shape_from_bitmap](qiumingdll_winsplit_set_shape_from_bitmap.md)
