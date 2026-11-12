# qiumingdll_volume_start(sampleRate, bufferMs)

Open the system default microphone and start collecting volume data; a return value of 0 means recording started successfully.

## Signature

```gml
qiumingdll_volume_start(sampleRate, bufferMs)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| sampleRate | Real | yes | Sample rate (unit Hz). Range 8000~192000; out-of-range values are clamped to the nearest bound. 48000 (CD quality) is recommended; a higher sample rate gives better precision but also uses more memory and CPU |
| bufferMs | Real | yes | Buffer duration (unit milliseconds). Range 5~100; out-of-range values are clamped to the nearest bound. A shorter buffer refreshes the volume faster (lower latency), a longer buffer uses fewer resources but reacts more slowly; around 10 is usually enough |

## Returns

| Value | Description |
|----|------|
| 0 | Success: the microphone is open and volume data starts updating |
| 1 | Failure: the system cannot find a microphone, the device is exclusively held by another program, or internal resource allocation failed. The GML wrapper also returns 1 directly on **non-Windows platforms** |

## Usage

- Precondition: the extension's global initialization routine must have run so that `global.__qiumingdll_volume_start` points at the DLL function; otherwise the wrapper returns 1 directly.
- Platform limit: Windows only. The underlying code opens the system **default** microphone via WAVE_MAPPER and captures mono 16-bit PCM, so a specific input device cannot be selected.
- Repeated calls: if recording is already running, calling again first stops the previous session automatically and then restarts with the new parameters; there is no need to call stop manually first.
- Parameter interaction: sampleRate and bufferMs together determine the buffer size of each capture (about sampleRate × bufferMs ÷ 1000 samples, minimum 64 samples), so both should be given reasonable values and extreme combinations avoided.
- After a successful call, always call qiumingdll_volume_stop() or qiumingdll_volume_cleanup() when the game exits or the microphone is no longer needed, otherwise other programs will never be able to use the microphone.
- This module shares the system microphone with the pitch module; the Get functions of this module only return valid values after start has succeeded.
- Typical uses: microphone volume meters, voice detection, karaoke volume bars.

## Example

```gml
/// Create event (obj_mic_volume)
// Open the system default microphone at a 48kHz sample rate with a 10ms buffer
var err = qiumingdll_volume_start(48000, 10);
if (err == 0)
{
    volumeActive = true;  // Recording started; the volume can be read in the Step event
}
else
{
    volumeActive = false; // No microphone or it is occupied; fall back gracefully
    show_debug_message("Failed to open the microphone");
}

/// Room End event
if (volumeActive)
{
    qiumingdll_volume_stop(); // Stop recording and release the microphone
}
```

## Related functions

- [qiumingdll_volume_stop](qiumingdll_volume_stop.md)
- [qiumingdll_volume_get_rms](qiumingdll_volume_get_rms.md)
- [qiumingdll_volume_get_level](qiumingdll_volume_get_level.md)
- [qiumingdll_volume_cleanup](qiumingdll_volume_cleanup.md)
