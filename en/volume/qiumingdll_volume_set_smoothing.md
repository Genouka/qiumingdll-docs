# qiumingdll_volume_set_smoothing(smoothing)

Set the volume smoothing factor, which controls how strongly get_rms and get_peak are smoothed. Default 0.3; a larger factor is more responsive, a smaller one is smoother.

## Signature

```gml
qiumingdll_volume_set_smoothing(smoothing)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| smoothing | Real | yes | Smoothing factor (unitless). Range 0~1; out-of-range values are clamped to the nearest bound. Default 0.3. Larger values give new data more weight (more sensitive to sound changes, the value jumps more); smaller values give historical data more weight (smoother, rounder values that react more slowly) |

## Returns

| Value | Description |
|----|------|
| 0 | Set successfully (the factor is stored and takes effect immediately). The GML wrapper also returns 0 directly on **non-Windows platforms** |

## Usage

- Precondition: none. It can be called before or after start, and changes made while recording take effect immediately (starting from the next analysis update).
- Platform limit: Windows only (on non-Windows platforms the wrapper returns 0 directly and has no effect).
- Scope: it affects the smoothing of both get_rms() and get_peak(), which share the same factor; get_db is converted from the smoothed RMS and is therefore affected indirectly, and get_level is banded from the smoothed RMS and is indirectly affected as well.
- Behaviour details: with a factor of 1 the value is barely smoothed at all (it follows the instantaneous value completely); with 0 the value almost stops changing (it keeps its initial value), so 0 is generally not recommended.
- Persistence: the parameter survives stop() until this function is called again, or until the global cleanup routine resets it to the default.
- Usage tips: around 0.3 feels natural for volume bar animation; increase it for fast response (lip sync, audio visualization) and decrease it for stable readings (voice detection logic).
- Relationship with the volume: smoothing is exponential weighting (new data × factor + old value × (1 - factor)), so the value always "chases" the current volume instead of jumping instantly. There is no absolutely correct value between over-responsive and over-smoothed; tune it to the feel of your gameplay.
- Evaluation method: expose a slider in the settings UI that calls this function in real time, then sing along and watch the volume bar to find the right feel quickly.

## Example

```gml
/// Create event (obj_mic_volume)
qiumingdll_volume_start(48000, 10);

/// Step event
// Adjust the smoothing factor dynamically from the player's setting (0.1 smooth ~ 0.9 responsive)
qiumingdll_volume_set_smoothing(ui_smoothSliderValue); // assume the slider value is between 0.1 and 0.9

// Smoothed volume for the draw event
smoothedRms = qiumingdll_volume_get_rms();

/// Draw event
// Draw the main volume bar with the more strongly smoothed reading to avoid frantic jitter
draw_set_color(c_lime);
draw_rectangle(50, 50, 50 + smoothedRms * 300, 60, false);
```

## Related functions

- [qiumingdll_volume_get_rms](qiumingdll_volume_get_rms.md)
- [qiumingdll_volume_get_peak](qiumingdll_volume_get_peak.md)
- [qiumingdll_volume_start](qiumingdll_volume_start.md)
