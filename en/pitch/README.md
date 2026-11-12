# pitch Module

Microphone input pitch detection: get the current frequency, note name and volume; suitable for singing games and similar gameplay.

8 functions in total.

## Function index

| Function | Description |
|------|------|
| [qiumingdll_pitch_cleanup](qiumingdll_pitch_cleanup.md) | Fully cleans up the pitch module: stops pitch detection, releases the microphone device and all internal resources, and resets all state (including detection results and threshold parameters) to zero. |
| [qiumingdll_pitch_get_frequency](qiumingdll_pitch_get_frequency.md) | Returns the fundamental frequency (in Hz) of the currently detected sound, range 20 ~ 20000; returns 0 when no valid pitch is detected. |
| [qiumingdll_pitch_get_note](qiumingdll_pitch_get_note.md) | Returns the MIDI note number corresponding to the currently detected pitch, where 60 is middle C and 69 is middle A (440 Hz); returns -1 when nothing is detected. |
| [qiumingdll_pitch_get_volume](qiumingdll_pitch_get_volume.md) | Returns the input volume (RMS) within the pitch module's current analysis window, range 0 ~ 1, used to determine whether the sound is loud enough for pitch detection. |
| [qiumingdll_pitch_is_active](qiumingdll_pitch_is_active.md) | Queries whether the pitch module is currently detecting pitch; returns 1 while detecting and 0 when not started. |
| [qiumingdll_pitch_set_threshold](qiumingdll_pitch_set_threshold.md) | Sets the threshold of the YIN fundamental-frequency detection algorithm, controlling pitch detection sensitivity. Default is 0.15. |
| [qiumingdll_pitch_start](qiumingdll_pitch_start.md) | Opens the system default microphone and starts fundamental-frequency detection; returns 0 when detection has started successfully. |
| [qiumingdll_pitch_stop](qiumingdll_pitch_stop.md) | Stops fundamental-frequency detection and releases the capture device, clearing the detection results but keeping the configured YIN threshold parameter. |

[Back to documentation home](../README.md)
