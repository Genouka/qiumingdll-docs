# qiumingdll_pitch_get_volume()

Returns the input volume (RMS) within the pitch module's current analysis window, range 0 ~ 1, used to determine whether the sound is loud enough for pitch detection.

## Signature

```gml
qiumingdll_pitch_get_volume()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 0 ~ 1 | Root-mean-square volume (RMS) within the current analysis window. 1 means the signal reaches 16-bit full scale; normal singing is usually between 0.05 and 0.5 |
| 0 | Returns 0 when detection has not been started; the GML wrapper on **non-Windows platforms** also returns 0 directly |

## Usage

- Prerequisite: qiumingdll_pitch_start() must have been called successfully; calling before start returns 0.
- Platform support: Windows only (on other platforms the GML wrapper returns 0 directly).
- Difference from the volume module: the volume module has its own smoothing and silence threshold settings, whereas this function's volume is the RMS computed directly within each pitch analysis window (about 2048 samples) without smoothing, reflecting the input level at the moment of detection.
- Relationship to detection results: when the volume is below the internal gate (about 0.01), detection is skipped and get_frequency returns 0 while get_note returns -1; this function therefore tells you whether "returning 0 is because there is no sound or because there is no pitch".
- Typical uses: determine whether the player is really vocalizing (avoid misjudging pitch during quiet passages), control the hint blinking in the tuning UI.

## Example

```gml
/// Step Event (obj_singing_game)
// Combined check: first whether the volume is high enough, then the pitch
var vol = qiumingdll_pitch_get_volume();
if (vol < 0.05)
{
    // Volume too low: prompt the player to move closer to the microphone
    hintText = "Too quiet, please sing louder!";
}
else
{
    var f = qiumingdll_pitch_get_frequency();
    if (f > 0)
    {
        hintText = "Detecting pitch: " + string(f) + " Hz";
    }
    else
    {
        hintText = "There is sound but no stable pitch (try a sustained note)";
    }
}
```

## Related functions

- [qiumingdll_pitch_get_frequency](qiumingdll_pitch_get_frequency.md)
- [qiumingdll_pitch_start](qiumingdll_pitch_start.md)
- [qiumingdll_pitch_set_threshold](qiumingdll_pitch_set_threshold.md)
