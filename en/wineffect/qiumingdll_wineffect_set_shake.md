# qiumingdll_wineffect_set_shake(intensity)

Sets the window shake strength. The window moves rapidly across the screen along a superimposed sinusoidal path.

## Signature

```gml
qiumingdll_wineffect_set_shake(intensity)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| intensity | Real | Yes | 0.0 ~ 1.0; out-of-range values are clamped automatically. 0 = shake off. At 1.0 the max displacement is about 24 pixels |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Failure: no window bound (call `qiumingdll_wineffect_init()` first) |

## Usage

- Prerequisite: call `qiumingdll_wineffect_init()` first; may be set before or after `set_enabled(1)`.
- The target is the **real window position**, not the window content; the non-client area, title bar and shadow move along with it.
- A maximized window cannot be moved and this effect is skipped; restore the window first.
- If the game moves the window itself while effects are running (e.g. dragging), the effect follows; on stop the window returns to the last detected base position.
- On stop (`set_enabled(0)` / `stop()` / `cleanup()`) the window returns exactly to the base position.

## Example

```gml
/// Shake on hit
qiumingdll_wineffect_set_shake(1.0);
qiumingdll_wineffect_set_enabled(1);
alarm[0] = 12;   // turn off after 0.2 seconds

/// Alarm 0
qiumingdll_wineffect_set_shake(0);
```

## Related functions

- [qiumingdll_wineffect_set_distort](qiumingdll_wineffect_set_distort.md)
- [qiumingdll_wineffect_set_tear](qiumingdll_wineffect_set_tear.md)
- [qiumingdll_wineffect_set_speed](qiumingdll_wineffect_set_speed.md)
