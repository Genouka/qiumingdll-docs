# qiumingdll_pitch_start(sampleRate, bufferMs)

Opens the system default microphone and starts fundamental-frequency detection; returns 0 when detection has started successfully.

## Signature

```gml
qiumingdll_pitch_start(sampleRate, bufferMs)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| sampleRate | Real | yes | Sample rate (in Hz). Range 8000 ~ 192000; out-of-range values are clamped to the boundary automatically. 48000 (CD quality) is recommended; a higher sample rate improves the detectable pitch range and accuracy but costs more CPU |
| bufferMs | Real | yes | Buffer duration (in milliseconds). Range 5 ~ 100; out-of-range values are clamped to the boundary automatically. A shorter buffer updates detection faster (lower latency); a longer buffer saves resources but makes pitch refresh slower. Around 10 is usually sufficient |

## Returns

| Value | Description |
|----|------|
| 0 | Success: the microphone is open and pitch data starts updating |
| 1 | Failure: no microphone is detected by the system, the device is exclusively held by another program, or internal resource allocation fails. The GML wrapper on **non-Windows platforms** also returns 1 directly |

## Usage

- Prerequisite: the extension's global initialization flow must have completed so that `global.__qiumingdll_pitch_start` points to the DLL function; otherwise the wrapper returns 1 directly.
- Platform support: Windows only. Internally it opens the system **default** microphone via WAVE_MAPPER and captures mono 16-bit PCM; a specific input device cannot be selected.
- Detection principle: the YIN algorithm performs fundamental-frequency detection on the captured audio, and results are read through get_frequency / get_note.
- Repeated calls: if detection is already running, calling again automatically stops the previous session first, then restarts with the new parameters.
- Parameter relationship: sampleRate and bufferMs together determine the capture buffer size for each pass (about sampleRate × bufferMs ÷ 1000 samples, minimum 64 samples); the pitch analysis window is about 2048 samples, so a higher sample rate means the window covers a shorter time span, which is less favorable for low notes (e.g. bass voices). To favor low-note detection, use a lower sample rate (e.g. 22050).
- This module shares the system microphone with the volume module; the Get functions of this module return valid values only after start succeeds.
- Typical uses: singing pitch display, instrument tuners, rhythm-game judging.

## Example

```gml
/// Create Event (obj_voice_pitch)
// Start pitch detection at a 48 kHz sample rate with a 10 ms buffer
var err = qiumingdll_pitch_start(48000, 10);
if (err == 0)
{
    pitchActive = true; // detection started; pitch can be read in Step
}
else
{
    pitchActive = false;
    show_debug_message("Failed to start pitch detection");
}

/// Room End Event
if (pitchActive)
{
    qiumingdll_pitch_stop(); // stop detection and release the microphone
}
```

## Related functions

- [qiumingdll_pitch_stop](qiumingdll_pitch_stop.md)
- [qiumingdll_pitch_get_frequency](qiumingdll_pitch_get_frequency.md)
- [qiumingdll_pitch_get_note](qiumingdll_pitch_get_note.md)
- [qiumingdll_pitch_cleanup](qiumingdll_pitch_cleanup.md)
