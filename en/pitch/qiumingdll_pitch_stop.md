# qiumingdll_pitch_stop()

Stops fundamental-frequency detection and releases the capture device, clearing the detection results but keeping the configured YIN threshold parameter.

## Signature

```gml
qiumingdll_pitch_stop()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 0 | Detection stopped and the device released. The GML wrapper on **non-Windows platforms** also returns 0 directly |

## Usage

- Prerequisite: start does not need to have been called first; calling it while not detecting is safe (no side effects).
- Platform support: Windows only (on other platforms the GML wrapper returns 0 directly and does nothing).
- Difference from cleanup: stop only stops detection, releases the microphone and clears the detection results; it does **not** change the YIN threshold set via qiumingdll_pitch_set_threshold(). After stop, calling qiumingdll_pitch_start() again reuses the previous threshold value.
- State after stopping: get_frequency returns 0, get_volume returns 0, get_note returns -1, is_active returns 0.
- Recommended when the game exits, scenes change, or pitch detection is no longer needed, to release the device resources promptly.
- This module is independent of the volume module; this function affects only the pitch module and does not affect volume-module recording.
- Note: after stop, all Get functions return their "not started" values (frequency 0, volume 0, note -1); if the UI is still displaying a pitch, clear or hide it as well, to avoid mistaking the "stopped state" for "no pitch detected".

## Example

```gml
/// Keyboard Event (Space)
// Toggle pitch detection with the space key
if (qiumingdll_pitch_is_active() == 1)
{
    qiumingdll_pitch_stop(); // turn detection off
    detectOn = false;
}
else
{
    qiumingdll_pitch_start(48000, 10); // turn it back on
    detectOn = true;
}

/// Room End Event
if (qiumingdll_pitch_is_active() == 1)
{
    qiumingdll_pitch_stop(); // stop detection before leaving the room
}
```

## Related functions

- [qiumingdll_pitch_start](qiumingdll_pitch_start.md)
- [qiumingdll_pitch_is_active](qiumingdll_pitch_is_active.md)
- [qiumingdll_pitch_cleanup](qiumingdll_pitch_cleanup.md)
