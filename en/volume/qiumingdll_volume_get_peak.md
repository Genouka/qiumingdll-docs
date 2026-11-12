# qiumingdll_volume_get_peak()

Return the peak value of the current microphone volume, 0~1. The value is smoothed as well and reflects the instantaneous strength of the sound.

## Signature

```gml
qiumingdll_volume_get_peak()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 0 ~ 1 | Smoothed peak volume. 0 means silence, 1 means the signal reaches 16-bit full scale. Short, loud transients such as hand claps or knocks make the peak clearly higher than the RMS at the same moment |
| 0 | Returned when recording has not been started; the GML wrapper also returns 0 directly on **non-Windows platforms** |

## Usage

- Precondition: qiumingdll_volume_start() must have succeeded; calling before start always returns 0.
- Platform limit: Windows only (on non-Windows platforms the wrapper returns 0 directly).
- Smoothing behaviour: the return value is also affected by the smoothing factor set with qiumingdll_volume_set_smoothing(), and it shares that factor with the RMS.
- Relationship with get_rms: for the same audio, peak is generally greater than or equal to rms; the peak reflects sudden loudness faster, while the RMS better represents sustained loudness. Karaoke-style bars commonly use peak for the "flicker" effect.
- Freshness: it only refreshes while recording is running; valid values start to appear a few tens of milliseconds after start.
- Performance: this function only reads one internal number, so the call cost is negligible and it can be called every frame without worry; reading it together with get_rms makes the classic two-bar (green = RMS, yellow = Peak) level meter easy.
- Tip: if you want an "instantaneous peak hold" effect, record the maximum of this frame's peak on the GML side and let it decay slowly over time.

## Example

```gml
/// Step event (obj_voice_detect)
// Use the peak to detect "suddenly loud" moments and raise a warning
var peak = qiumingdll_volume_get_peak();
if (peak > 0.8)
{
    // Volume too high warning
    draw_loudWarning = 1;
}

/// Draw event
// Overlay the peak bar (red) on the RMS bar (green) for comparison
var p = qiumingdll_volume_get_peak();
var r = qiumingdll_volume_get_rms();
draw_set_color(c_red);
draw_rectangle(50, 100, 50 + p * 200, 110, false);
draw_set_color(c_green);
draw_rectangle(50, 115, 50 + r * 200, 125, false);
```

## Related functions

- [qiumingdll_volume_start](qiumingdll_volume_start.md)
- [qiumingdll_volume_get_rms](qiumingdll_volume_get_rms.md)
- [qiumingdll_volume_set_smoothing](qiumingdll_volume_set_smoothing.md)
