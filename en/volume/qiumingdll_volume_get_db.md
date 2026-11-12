# qiumingdll_volume_get_db()

Return the decibel value (dB) of the current volume, roughly -96 ~ 0. In silence it stays at -96, which makes it suitable for a professional level-meter display.

## Signature

```gml
qiumingdll_volume_get_db()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| -96 ~ 0 | Decibel value of the current volume (unit dB), converted from the smoothed RMS (20 × log10(RMS)). 0 dB is a 16-bit full-scale signal |
| -96 | Returned in silence (RMS below the threshold); this is the lower bound of the decibel conversion. The same value is returned when recording has not been started |
| 0 | The GML wrapper returns 0 directly on **non-Windows platforms** (note the difference from -96 in silence) |

## Usage

- Precondition: qiumingdll_volume_start() must have succeeded; calling before start returns -96.
- Platform limit: Windows only.
- Relationship with the other Get functions: get_db is converted from the smoothed result of get_rms, so the two values are fully in sync and only the display unit differs; the decibel scale better matches professional audio equipment (e.g. anything below -60 dB counts as silence).
- Freshness: it only refreshes while recording is running; valid values start to appear a few tens of milliseconds after start.
- Tip: human speech usually sits between -40 and -10 dB; if it often stays below -50 dB, the microphone input is too quiet and the system input gain should be increased.
- Conversion: 0 dB corresponds to RMS=1 (16-bit full scale), -6 dB to RMS≈0.5, and -20 dB to RMS≈0.1; the larger the decibel value, the louder the sound.
- Display tip: read it directly in the Draw GUI event; the value is already smoothed, so no extra interpolation animation is needed.

## Example

```gml
/// Draw event (obj_audio_meter)
// Professional-style decibel meter: map -96~0 dB onto a height of 0~300 pixels
var db = qiumingdll_volume_get_db();
var h = (db + 96) / 96 * 300; // -96dB maps to 0px, 0dB maps to 300px
draw_set_color(c_orange);
draw_rectangle(200, 400, 220, 400 - h, false);

// Show the value with 1 decimal place
draw_set_color(c_white);
draw_text(230, 380, string_format(db, 1, 1) + " dB");
```

## Related functions

- [qiumingdll_volume_start](qiumingdll_volume_start.md)
- [qiumingdll_volume_get_rms](qiumingdll_volume_get_rms.md)
- [qiumingdll_volume_get_level](qiumingdll_volume_get_level.md)
