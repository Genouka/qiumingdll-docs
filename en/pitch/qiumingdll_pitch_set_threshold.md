# qiumingdll_pitch_set_threshold(threshold)

Sets the threshold of the YIN fundamental-frequency detection algorithm, controlling pitch detection sensitivity. Default is 0.15.

## Signature

```gml
qiumingdll_pitch_set_threshold(threshold)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| threshold | Real | yes | YIN detection threshold (unitless). Range 0.01 ~ 0.99; out-of-range values are clamped to the boundary automatically; default 0.15. A smaller threshold is pickier about "non-periodic signals" (harder to misjudge, but weak signals may not be detected); a larger threshold makes it easier to lock onto a period (more likely to produce a result for noisy or ambiguous signals, but may misjudge the pitch) |

## Returns

| Value | Description |
|----|------|
| 0 | Set successfully (the threshold is saved and takes effect immediately). The GML wrapper on **non-Windows platforms** also returns 0 directly |

## Usage

- Prerequisite: none. May be called before or after start; changes made during detection take effect in the next analysis.
- Platform support: Windows only (on other platforms the GML wrapper returns 0 directly and has no effect).
- Scope: affects only the YIN algorithm decisions of the pitch module; the volume module is unaffected — its silence threshold is set via qiumingdll_volume_set_silence_threshold().
- Behavior: the YIN threshold determines how low the "cumulative mean normalized difference" must be for a period to be considered found. If the threshold is too low, slightly distorted input causes detection to fail (get_frequency returns 0); if it is too high, noise may be treated as pitch.
- Persistence: the parameter survives stop() until this function modifies it again, or the global cleanup routine resets it to the default 0.15.
- Recommendations: clean instrument signals can use 0.1 ~ 0.15; noisy environments or singing can use somewhat higher values (0.2 ~ 0.3); when only clear notes should count, use lower values (0.05 ~ 0.1).
- Relationship to input volume: this threshold only affects whether a period is considered trustworthy; regardless of the threshold, detection is skipped when the input volume is too low (get_frequency returns 0). The two are not substitutes for each other.
- Debugging tip: have the player sing a steady sustained note into the microphone, raise the threshold gradually until wrong pitches occasionally appear, then back off a little; that is the suitable value for the current environment.

## Example

```gml
/// Create Event (obj_tuner)
qiumingdll_pitch_start(48000, 10);
qiumingdll_pitch_set_threshold(0.15); // default sensitivity

/// Step Event
// Adjust detection sensitivity in real time from a UI slider (0 ~ 1)
// Slider 0 → strictest (0.05), slider 1 → loosest (0.3)
var t = lerp(0.05, 0.30, sensitivitySlider);
qiumingdll_pitch_set_threshold(t);

// When sensitivity is low, "no result" is common; give the player feedback
if (qiumingdll_pitch_get_frequency() == 0 && qiumingdll_pitch_get_volume() > 0.1)
{
    drawHint = "Didn't catch that; please sing more clearly or raise the sensitivity";
}
```

## Related functions

- [qiumingdll_pitch_start](qiumingdll_pitch_start.md)
- [qiumingdll_pitch_get_frequency](qiumingdll_pitch_get_frequency.md)
- [qiumingdll_pitch_cleanup](qiumingdll_pitch_cleanup.md)
