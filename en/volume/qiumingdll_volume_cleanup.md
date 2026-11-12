# qiumingdll_volume_cleanup()

Fully clean up the volume module: stop recording, release the microphone device and every internal resource, and reset all state (including volume values and parameter settings) to zero.

## Signature

```gml
qiumingdll_volume_cleanup()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 0 | Cleanup complete. The GML wrapper also returns 0 directly on **non-Windows platforms** |

## Usage

- Precondition: none. Calling it when recording was never started is safe.
- Platform limit: Windows only (on non-Windows platforms the wrapper returns 0 directly and has no effect).
- Difference from stop: stop only stops recording and keeps the parameters (silence threshold, smoothing factor); cleanup zeroes **the parameters as well** and fully resets the internal data structures. If you want to keep using the module after cleanup, you must call qiumingdll_volume_start() again and set the parameters you need again (the threshold and smoothing factor fall back to their defaults, 0.01 / 0.3).
- It is recommended to call this before the game exits completely, so the microphone is released and the device cannot remain occupied while the DLL unloads, which would cause a crash or leave resources behind.
- The extension's global cleanup routine normally calls this function automatically; when calling it manually, take care not to duplicate the global cleanup (calling it twice is safe but redundant).

## Example

```gml
/// Room End event (obj_mic_volume)
// Fully release the Volume module resources when changing scenes or closing the game
qiumingdll_volume_cleanup();
volumeActive = false;

/// Game End event
// Final cleanup before the game exits
qiumingdll_volume_cleanup();

/// Enabling it again (e.g. re-entering the recording room)
// After cleanup the module must be fully re-initialized
var err = qiumingdll_volume_start(48000, 10);
if (err == 0)
{
    qiumingdll_volume_set_silence_threshold(0.01); // restore the parameters you need
    qiumingdll_volume_set_smoothing(0.3);
    volumeActive = true;
}
```

## Related functions

- [qiumingdll_volume_start](qiumingdll_volume_start.md)
- [qiumingdll_volume_stop](qiumingdll_volume_stop.md)
- [qiumingdll_volume_set_silence_threshold](qiumingdll_volume_set_silence_threshold.md)
- [qiumingdll_volume_set_smoothing](qiumingdll_volume_set_smoothing.md)
