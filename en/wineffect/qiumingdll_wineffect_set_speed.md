# qiumingdll_wineffect_set_speed(speed)

Sets the animation speed multiplier for window effects. All three effects share the same speed.

## Signature

```gml
qiumingdll_wineffect_set_speed(speed)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| speed | Real | Yes | 0.0 ~ 8.0; out-of-range values are clamped automatically. Default 1.0; 0 = freeze the animation (keep the current pose) |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Failure: no window bound (call `qiumingdll_wineffect_init()` first) |

## Usage

- Prerequisite: call `qiumingdll_wineffect_init()` first.
- speed affects the phase advance rate of shake/distortion as well as the refresh interval of the tear layout.
- With speed = 0 the animation freezes: the window keeps its current displacement and current region shape until a non-zero speed is set again or the effect is stopped.
- Changing the speed while running is smooth and does not reset the current phase.

## Example

```gml
// Slow-motion glitch
qiumingdll_wineffect_set_speed(0.35);
qiumingdll_wineffect_set_enabled(1);

// Back to normal speed
qiumingdll_wineffect_set_speed(1.0);
```

## Related functions

- [qiumingdll_wineffect_set_shake](qiumingdll_wineffect_set_shake.md)
- [qiumingdll_wineffect_set_distort](qiumingdll_wineffect_set_distort.md)
- [qiumingdll_wineffect_set_tear](qiumingdll_wineffect_set_tear.md)
