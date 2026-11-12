# qiumingdll_pitch_is_active()

Queries whether the pitch module is currently detecting pitch; returns 1 while detecting and 0 when not started.

## Signature

```gml
qiumingdll_pitch_is_active()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 1 | Detecting: qiumingdll_pitch_start() succeeded and has not been stopped |
| 0 | Not detecting: start has not been called or has failed, or qiumingdll_pitch_stop() / qiumingdll_pitch_cleanup() has been called. The GML wrapper on **non-Windows platforms** also returns 0 directly |

## Usage

- Prerequisite: none; safe to call at any time.
- Platform support: Windows only (on other platforms the GML wrapper returns 0 directly).
- Purpose: use it as a guard before reading get_frequency / get_note, to avoid confusing "not started" with "no pitch detected" (get_note also returns -1 when not started).
- Behavior: after start returns 0 successfully, is_active immediately becomes 1; after stop or cleanup is called it immediately returns to 0. Repeated calls to start do not affect this state (it stays 1).
- Note: is_active being 1 only means "the detection flow is running"; it does not mean a pitch has necessarily been detected. Whether there is a pitch depends on whether get_frequency / get_note return valid values.

## Example

```gml
/// Step Event (obj_pitch_controller)
// Automatically restart if detection stops unexpectedly
if (wantDetect && qiumingdll_pitch_is_active() == 0)
{
    qiumingdll_pitch_start(22050, 10); // resume detection (a lower sample rate is better for low notes)
}

/// Draw Event
// Show detection status and the current note
if (qiumingdll_pitch_is_active() == 1)
{
    var note = qiumingdll_pitch_get_note();
    if (note == -1)
        draw_text(10, 10, "Detecting... (no pitch)");
    else
        draw_text(10, 10, "Detecting, note = " + string(note));
}
else
{
    draw_text(10, 10, "Not started");
}
```

## Related functions

- [qiumingdll_pitch_start](qiumingdll_pitch_start.md)
- [qiumingdll_pitch_stop](qiumingdll_pitch_stop.md)
- [qiumingdll_pitch_cleanup](qiumingdll_pitch_cleanup.md)
