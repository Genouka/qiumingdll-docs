# qiumingdll_wineffect_set_tear(intensity)

Sets the window tearing strength. The window is cut into misaligned horizontal strips, with notches, vertical cracks and slight jumps appearing at random.

## Signature

```gml
qiumingdll_wineffect_set_tear(intensity)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| intensity | Real | Yes | 0.0 ~ 1.0; out-of-range values are clamped automatically. 0 = tear off. At 1.0 the max misalignment is about 120 pixels |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Failure: no window bound (call `qiumingdll_wineffect_init()` first) |

## Usage

- Prerequisite: call `qiumingdll_wineffect_init()` first.
- Generates a window region with notches/cracks via `SetWindowRgn`; the clipped-away parts expose the desktop or underlying windows.
- The tear layout is re-randomized every ~60–140ms, combined with slight window position jumps, to produce the feeling of a "window being torn open".
- When enabled together with `set_distort()`, the tear misalignment is layered on top of the distorted outline.
- Higher intensity means: more slices, larger misalignment, more visible notches/cracks, stronger jumps.
- On stop the original window region and position are restored.
- Note: while tearing, clipped-away window areas no longer participate in mouse hit-testing, so clicks fall through to underlying windows; this is normal shaped-window behavior.

## Example

```gml
/// Heavy glitch: tearing + slight shaking
qiumingdll_wineffect_set_tear(0.8);
qiumingdll_wineffect_set_shake(0.2);
qiumingdll_wineffect_set_enabled(1);

/// Back to normal
qiumingdll_wineffect_set_tear(0);
qiumingdll_wineffect_set_shake(0);
```

## Related functions

- [qiumingdll_wineffect_set_distort](qiumingdll_wineffect_set_distort.md)
- [qiumingdll_wineffect_set_shake](qiumingdll_wineffect_set_shake.md)
- [qiumingdll_wineffect_set_speed](qiumingdll_wineffect_set_speed.md)
