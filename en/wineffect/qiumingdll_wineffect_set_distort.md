# qiumingdll_wineffect_set_distort(intensity)

Sets the window outline distortion strength. The left and right window edges shrink row by row following a sine wave, producing a wavy outline.

## Signature

```gml
qiumingdll_wineffect_set_distort(intensity)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| intensity | Real | Yes | 0.0 ~ 1.0; out-of-range values are clamped automatically. 0 = distortion off. At 1.0 the max edge shrink is about 48 pixels |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Failure: no window bound (call `qiumingdll_wineffect_init()` first) |

## Usage

- Prerequisite: call `qiumingdll_wineffect_init()` first.
- Modifies the **window region** via `SetWindowRgn`: the part of the window outside the wavy edge is clipped away, exposing the desktop / underlying windows.
- This is a window outline distortion, not image resampling; the window content is not scaled or translated, only clipped.
- Can be enabled together with `set_tear()`; both are merged into a single window region.
- Still takes effect when the window is maximized.
- On stop the original window region saved at enable time is restored; if the window had no region, it is restored to the full rectangle.

## Example

```gml
/// Glitch sequence: window edges start rippling
qiumingdll_wineffect_set_distort(0.5);
qiumingdll_wineffect_set_enabled(1);

/// Sequence ends
qiumingdll_wineffect_set_distort(0);
```

## Related functions

- [qiumingdll_wineffect_set_tear](qiumingdll_wineffect_set_tear.md)
- [qiumingdll_wineffect_set_shake](qiumingdll_wineffect_set_shake.md)
- [qiumingdll_wineffect_set_speed](qiumingdll_wineffect_set_speed.md)
