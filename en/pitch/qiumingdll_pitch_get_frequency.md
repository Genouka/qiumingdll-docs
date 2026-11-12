# qiumingdll_pitch_get_frequency()

Returns the fundamental frequency (in Hz) of the currently detected sound, range 20 ~ 20000; returns 0 when no valid pitch is detected.

## Signature

```gml
qiumingdll_pitch_get_frequency()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 20 ~ 20000 | The currently detected fundamental frequency (in Hz). Human singing is usually in the 80 ~ 1100 Hz range; the A4 reference pitch is 440 Hz, and middle C (C4) is about 261.6 Hz |
| 0 | No valid pitch detected: no stable periodic signal (silence, noise, a sound that is too quiet), or detection has not been started. The GML wrapper on **non-Windows platforms** also returns 0 directly |

## Usage

- Prerequisite: qiumingdll_pitch_start() must have been called successfully; calling before start returns 0.
- Platform support: Windows only (on other platforms the GML wrapper returns 0 directly).
- Detection condition: fundamental-frequency analysis is performed only when the input volume (RMS) is at or above the internal volume gate; under silence or ambient noise it returns 0. Use qiumingdll_pitch_set_threshold() to adjust the sensitivity of the YIN algorithm.
- Update timing: refreshed continuously only while detection is running; after start it takes roughly tens of milliseconds (to accumulate enough samples for the analysis window) before the first valid result appears.
- Relationship to get_note: get_frequency is the raw frequency before conversion to a MIDI note; both are updated synchronously within the same analysis cycle. Prefer the note number (get_note) for "in tune or not" decisions, and use the frequency to draw pitch curves.
- Typical uses: singing pitch meters, instrument tuners, pitch-training games.

## Example

```gml
/// Step Event (obj_tuner)
// Read the current fundamental frequency and convert it to the deviation (in cents) from the target pitch
var f = qiumingdll_pitch_get_frequency();
if (f > 0)
{
    // Target pitch A4 = 440Hz; calculate the deviation in cents (cents)
    var cents = 1200 * log2(f / 440.0);
    // A deviation within ±20 cents counts as "in tune"
    inTune = abs(cents) < 20;
}
else
{
    inTune = false; // no pitch detected
}

/// Draw GUI Event
if (f > 0 && inTune)
{
    draw_set_color(c_lime);
    draw_text(10, 10, "A4 in tune! Current frequency: " + string(f) + " Hz");
}
else
{
    draw_set_color(c_white);
    draw_text(10, 10, "Please sing A4 (440Hz) into the microphone...");
}
```

## Related functions

- [qiumingdll_pitch_start](qiumingdll_pitch_start.md)
- [qiumingdll_pitch_get_note](qiumingdll_pitch_get_note.md)
- [qiumingdll_pitch_get_volume](qiumingdll_pitch_get_volume.md)
