# qiumingdll_pitch_cleanup()

Fully cleans up the pitch module: stops pitch detection, releases the microphone device and all internal resources, and resets all state (including detection results and threshold parameters) to zero.

## Signature

```gml
qiumingdll_pitch_cleanup()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 0 | Cleanup complete. The GML wrapper on **non-Windows platforms** also returns 0 directly |

## Usage

- Prerequisite: none. It is safe to call even when detection has not been started.
- Platform support: Windows only (on other platforms the GML wrapper returns 0 directly and has no effect).
- Difference from stop: stop only stops detection and keeps the parameters; cleanup also **resets the YIN threshold** (back to the default 0.15) and fully reinitializes the internal data structures. If the module is needed again after cleanup, you must call qiumingdll_pitch_start() again and re-set any required threshold.
- Recommended before the game fully exits, to ensure the microphone is released and avoid a crash or leftover device occupation when the DLL unloads while the device is still in use.
- The extension's global cleanup routine normally calls this function automatically; when calling it manually, take care not to duplicate the global cleanup (repeated calls are safe but redundant).
- Note: cleanup only affects the pitch module; if the volume module has no separate cleanup, its recording is not stopped by this function.
- Debugging tip: after calling it in the room end event, if you return to the detection screen, go through the full start → set threshold flow again instead of reading the Get functions directly in the "cleaned up" state (they will return the not-started values).

## Example

```gml
/// Room End Event (obj_voice_pitch)
// Fully release pitch module resources when leaving the detection scene
qiumingdll_pitch_cleanup();
pitchActive = false;

/// Game End Event
// Final cleanup before the game exits
qiumingdll_pitch_cleanup();

/// Re-enable (e.g. re-entering the tuning room)
// After cleanup the module must be fully re-initialized
var err = qiumingdll_pitch_start(48000, 10);
if (err == 0)
{
    qiumingdll_pitch_set_threshold(0.15); // restore the required threshold
    pitchActive = true;
}
```

## Related functions

- [qiumingdll_pitch_start](qiumingdll_pitch_start.md)
- [qiumingdll_pitch_stop](qiumingdll_pitch_stop.md)
- [qiumingdll_pitch_set_threshold](qiumingdll_pitch_set_threshold.md)
