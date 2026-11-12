# qiumingdll_volume_stop()

Stop microphone recording and release the capture device, resetting the volume state to zero while keeping the configured parameters (silence threshold, smoothing factor).

## Signature

```gml
qiumingdll_volume_stop()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 0 | Recording stopped and the device released. The GML wrapper likewise returns 0 directly on **non-Windows platforms** |

## Usage

- Precondition: start does not need to have been called; even when recording is not running the call is safe (no side effects).
- Platform limit: Windows only (on non-Windows platforms the wrapper returns 0 directly and does nothing).
- Difference from cleanup: stop only stops recording, releases the microphone and zeroes the volume values; it does **not** change the parameters set with qiumingdll_volume_set_silence_threshold() and qiumingdll_volume_set_smoothing(). After stop, calling qiumingdll_volume_start() again starts the volume accumulating from zero.
- State of the Get functions after stopping: get_rms and get_peak return 0, get_db returns -96, get_level returns 0 and is_active returns 0.
- Call it when the game exits, scenes change or the microphone is no longer needed, so the device resources are released promptly and other programs that need the microphone are not affected.
- This module is independent of the pitch module; this function only affects the volume module and not pitch detection.
- Note: after stop all Get functions return their "not started" values (rms/peak/level are 0, db is -96); if the UI still shows a volume bar, hide or clear it as well to avoid misleading players.

## Example

```gml
/// Keyboard event (Enter)
// Press Enter to stop recording, emulating a "mute switch"
if (qiumingdll_volume_is_active() == 1)
{
    qiumingdll_volume_stop(); // The microphone is released after stopping
    micOn = false;
}
else
{
    qiumingdll_volume_start(48000, 10); // Start recording again
    micOn = true;
}

/// Room End event
if (qiumingdll_volume_is_active() == 1)
{
    qiumingdll_volume_stop(); // Stop recording before leaving the room
}
```

## Related functions

- [qiumingdll_volume_start](qiumingdll_volume_start.md)
- [qiumingdll_volume_is_active](qiumingdll_volume_is_active.md)
- [qiumingdll_volume_cleanup](qiumingdll_volume_cleanup.md)
