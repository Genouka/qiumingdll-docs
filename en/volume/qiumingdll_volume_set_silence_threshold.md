# qiumingdll_volume_set_silence_threshold(threshold)

Set the silence threshold: audio whose smoothed RMS is below this value counts as silence (get_level returns 0). Default 0.01.

## Signature

```gml
qiumingdll_volume_set_silence_threshold(threshold)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| threshold | Real | yes | Silence threshold (unitless, corresponds to the normalized RMS volume in 0~1). Range 0~0.5; out-of-range values are clamped to the nearest bound. Default 0.01. Larger values make silence easier to detect (less sensitive to faint ambient noise), smaller values are more sensitive |

## Returns

| Value | Description |
|----|------|
| 0 | Set successfully (the threshold is stored and takes effect immediately). The GML wrapper also returns 0 directly on **non-Windows platforms** |

## Usage

- Precondition: none. It can be called before or after start, and changes made while recording take effect immediately.
- Platform limit: Windows only (on non-Windows platforms the wrapper returns 0 directly and has no effect).
- Scope: it only affects the level-0 decision of get_level() (RMS below the threshold = level 0); get_rms / get_peak / get_db are unaffected.
- Parameter interaction: if the silence threshold is set above 0.05, sounds that would otherwise be classed as level 1 are all counted as level 0 (silence).
- Persistence: the parameter survives stop() until this function is called again, or until the global cleanup routine resets it to the default.
- Recommended use: raise it moderately in noisy environments (e.g. 0.02~0.05) and lower it (e.g. 0.005) when very quiet sounds must be captured.
- Interaction reminder for get_level: this threshold only affects the level-0 decision of get_level, and if the silence threshold is set above 0.05 level 1 will never appear.
- Debugging tip: after Start, observe the ambient noise floor with get_rms, then set the threshold to 1.5~2 times that value for a reasonably good silence decision.

## Example

```gml
/// Create event (obj_voice_detect)
// Set the silence threshold dynamically for different environments
qiumingdll_volume_set_silence_threshold(0.01); // quiet environment, default value
micSensitivity = 0.5; // 0~1 sensitivity slider for the player

/// Step event
// Map the sensitivity slider to a threshold: 0 = most sensitive (0.0) ~ 1 = least sensitive (0.3)
var t = lerp(0.0, 0.3, micSensitivity);
qiumingdll_volume_set_silence_threshold(t);

// Decide whether someone is talking (ignoring faint background noise)
var talking = qiumingdll_volume_get_level() > 0;
```

## Related functions

- [qiumingdll_volume_get_level](qiumingdll_volume_get_level.md)
- [qiumingdll_volume_start](qiumingdll_volume_start.md)
- [qiumingdll_volume_set_smoothing](qiumingdll_volume_set_smoothing.md)
