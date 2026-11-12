# qiumingdll_volume_get_rms()

Return the root-mean-square (RMS) value of the current microphone volume, 0~1. The value is already smoothed by the smoothing factor, which makes it suitable for driving a volume bar.

## Signature

```gml
qiumingdll_volume_get_rms()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 0 ~ 1 | Smoothed root-mean-square volume. 0 means silence, 1 means full scale (the input signal reaches 16-bit full scale). In a quiet environment the value falls back over time and settles close to 0 |
| 0 | Returned when recording has not been started; the GML wrapper also returns 0 directly on **non-Windows platforms** |

## Usage

- Precondition: qiumingdll_volume_start() must have succeeded; calling before start always returns 0.
- Platform limit: Windows only (on non-Windows platforms the wrapper returns 0 directly).
- Smoothing behaviour: the return value is affected by the smoothing factor set with qiumingdll_volume_set_smoothing(); a larger factor is more sensitive to instantaneous sound (the value jumps more), a smaller factor is smoother.
- Freshness: about a few tens of milliseconds (a few buffer periods) are needed after start before valid values accumulate; the volume values only refresh while recording is running.
- Typical uses: use it directly as the width/height ratio of a volume bar (multiply by the target pixel count), or as input for voice detection.
- Tip: get_peak() reflects the instantaneous peak while get_rms() reflects average loudness; rms is usually the more stable choice when deciding "is someone speaking".
- Performance: this function only reads one internal number, so the call cost is negligible; it can be called every frame in Step or Draw events without hurting game performance.

## Example

```gml
/// Draw event (obj_mic_volume)
// Draw the RMS volume as a horizontal volume bar
var rms = qiumingdll_volume_get_rms();
var barW = rms * 200; // 0~200 pixels
draw_set_color(c_lime);
draw_rectangle(50, 50, 50 + barW, 60, false);

// Also print the number for debugging
draw_set_color(c_white);
draw_text(50, 70, "RMS: " + string(rms));
```

## Related functions

- [qiumingdll_volume_start](qiumingdll_volume_start.md)
- [qiumingdll_volume_get_peak](qiumingdll_volume_get_peak.md)
- [qiumingdll_volume_set_smoothing](qiumingdll_volume_set_smoothing.md)
