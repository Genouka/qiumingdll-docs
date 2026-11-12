# qiumingdll_pitch_get_note()

Returns the MIDI note number corresponding to the currently detected pitch, where 60 is middle C and 69 is middle A (440 Hz); returns -1 when nothing is detected.

## Signature

```gml
qiumingdll_pitch_get_note()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 12 ~ 135 | The detected MIDI note number (converted from the fundamental frequency by 69 + 12 × log2(f / 440)). Common references: 60 = middle C (C4, about 261.6 Hz), 69 = A4 (440 Hz), 72 = C5 (high C); each increment of 1 is one semitone up |
| -1 | No valid pitch detected (silence, noise, no stable periodic signal), or detection has not been started. The GML wrapper on **non-Windows platforms** also returns -1 directly |
| Other | The theoretical range from frequency conversion is about 12 ~ 135, but a note number is only produced when detection succeeds (get_frequency is between 20 and 20000 Hz) |

## Usage

- Prerequisite: qiumingdll_pitch_start() must have been called successfully; calling before start returns -1.
- Platform support: Windows only (on other platforms the GML wrapper returns -1 directly).
- Usage: use -1 to tell "whether a pitch was detected"; compare the number with the target chart note for equality or near-equality to implement rhythm-game / karaoke judging. Slight detuning within the same note does not change the number; for fine detuning judgments, use get_frequency to compute the cent deviation instead.
- Conversion to note names: MIDI number modulo 12 gives the note name (0=C, 1=C#, 2=D, ... 11=B), and the number divided by 12 (integer division) minus 1 gives the octave (e.g. 60 → note name C, octave 4, i.e. C4 middle C).
- Update timing: updated synchronously with get_frequency within the same analysis cycle; returns to -1 immediately after detection stops.

## Example

```gml
/// Step Event (obj_piano_lesson)
// Read the current note number and compare it with the target chart note
var targetNote = 60; // target: middle C
var note = qiumingdll_pitch_get_note();
if (note == -1)
{
    statusText = "Waiting for sound...";
}
else if (note == targetNote)
{
    statusText = "Correct! Middle C";
    score += 1;
}
else if (note > targetNote)
{
    statusText = "Too high by " + string(note - targetNote) + " semitones";
}
else
{
    statusText = "Too low by " + string(targetNote - note) + " semitones";
}

/// Draw GUI Event
draw_set_color(c_white);
draw_text(10, 10, statusText);
draw_text(10, 30, "Note number: " + string(note));
```

## Related functions

- [qiumingdll_pitch_get_frequency](qiumingdll_pitch_get_frequency.md)
- [qiumingdll_pitch_start](qiumingdll_pitch_start.md)
- [qiumingdll_pitch_is_active](qiumingdll_pitch_is_active.md)
