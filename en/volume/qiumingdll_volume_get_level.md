# qiumingdll_volume_get_level()

Return the discrete level of the current volume, 0~5, derived from threshold bands of the smoothed RMS; ideal for a simple "bars" style volume indicator.

## Signature

```gml
qiumingdll_volume_get_level()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 0 | Silence: smoothed RMS below the silence threshold (default 0.01, adjustable with qiumingdll_volume_set_silence_threshold) |
| 1 | RMS not below the silence threshold and below 0.05: extremely quiet sound |
| 2 | RMS between 0.05 and 0.15: soft speech |
| 3 | RMS between 0.15 and 0.35: normal speaking volume |
| 4 | RMS between 0.35 and 0.6: fairly loud |
| 5 | RMS at 0.6 or above: maximum level |
| 0 | Returned when recording has not been started; the GML wrapper also returns 0 directly on **non-Windows platforms** |

## Usage

- Precondition: qiumingdll_volume_start() must have succeeded; calling before start returns 0.
- Platform limit: Windows only (on non-Windows platforms the wrapper returns 0 directly).
- Threshold bands: the level is derived from the smoothed RMS of each analysis window (about 1024 samples), banded as follows — below the silence threshold = 0; < 0.05 = 1; < 0.15 = 2; < 0.35 = 3; < 0.6 = 4; everything else = 5.
- Interaction with the silence threshold: after raising the threshold with qiumingdll_volume_set_silence_threshold(), quiet sounds that used to return 1 become 0 (silence).
- Typical uses: phone-call style volume bars, karaoke accompaniment sing-along indicators, voice activity detection.

## Example

```gml
/// Draw event (obj_level_meter)
// Show the volume level (0~5) as a 5-segment colour bar
var lvl = qiumingdll_volume_get_level();
for (var i = 0; i < 5; i++)
{
    // Light up segment i
    if (i < lvl)
    {
        draw_set_color(lvl >= 5 ? c_red : c_yellow);
        draw_rectangle(50 + i * 26, 200, 70 + i * 26, 220, false);
    }
    else
    {
        draw_set_color(c_gray);
        draw_rectangle(50 + i * 26, 200, 70 + i * 26, 220, true);
    }
}

/// Step event
// Level = 0 while recording means "nobody is speaking"
if (qiumingdll_volume_is_active() == 1 && qiumingdll_volume_get_level() == 0)
{
    silenceFrames += 1;
}
else
{
    silenceFrames = 0;
}
```

## Related functions

- [qiumingdll_volume_get_rms](qiumingdll_volume_get_rms.md)
- [qiumingdll_volume_set_silence_threshold](qiumingdll_volume_set_silence_threshold.md)
- [qiumingdll_volume_start](qiumingdll_volume_start.md)
