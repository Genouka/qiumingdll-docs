# qiumingdll_volume_is_active()

Query whether the volume module is currently recording: 1 means recording, 0 means not started.

## Signature

```gml
qiumingdll_volume_is_active()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 1 | Recording: qiumingdll_volume_start() has succeeded and has not been stopped since |
| 0 | Not recording: start was never called or has failed, or qiumingdll_volume_stop()/qiumingdll_volume_cleanup() has been called. The GML wrapper also returns 0 directly on **non-Windows platforms** |

## Usage

- Precondition: none; it is safe to call at any time.
- Platform limit: Windows only (on non-Windows platforms the wrapper returns 0 directly).
- Purpose: use it as a guard before calling the Get functions, so invalid data is not read while the module is stopped; it can also drive a runtime "microphone on/off" status display.
- Behaviour details: once start returns 0, is_active becomes 1 immediately; after stop or cleanup is called it returns to 0 immediately. Calling start repeatedly does not change this state (it stays 1).
- Tip: is_active being 1 only means "the device is open and capturing", not that sound has actually been detected; for that, look at get_rms / get_level.

## Example

```gml
/// Step event (obj_mic_controller)
// Check the recording state every frame and recover automatically after an unexpected stop
if (micWanted && qiumingdll_volume_is_active() == 0)
{
    // Recording stopped unexpectedly (e.g. by a stop call); restart it as needed
    qiumingdll_volume_start(48000, 10);
}

/// Draw GUI event
// Show the current state as text
if (qiumingdll_volume_is_active() == 1)
{
    draw_text(10, 10, "Microphone: recording");
}
else
{
    draw_text(10, 10, "Microphone: not started");
}
```

## Related functions

- [qiumingdll_volume_start](qiumingdll_volume_start.md)
- [qiumingdll_volume_stop](qiumingdll_volume_stop.md)
- [qiumingdll_volume_cleanup](qiumingdll_volume_cleanup.md)
