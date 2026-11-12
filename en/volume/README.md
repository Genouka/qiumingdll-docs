# volume module

Microphone volume detection: read the peak, the RMS and the decibel value, with an adjustable silence threshold and smoothing factor.

10 functions in total.

## Function index

| Function | Description |
|------|------|
| [qiumingdll_volume_cleanup](qiumingdll_volume_cleanup.md) | Fully clean up the volume module: stop recording, release the microphone device and every internal resource, and reset all state (including volume values and parameter settings) to zero. |
| [qiumingdll_volume_get_db](qiumingdll_volume_get_db.md) | Return the decibel value (dB) of the current volume, roughly -96 ~ 0; it stays at -96 in silence, which makes it suitable for a professional level-meter display. |
| [qiumingdll_volume_get_level](qiumingdll_volume_get_level.md) | Return the discrete level of the current volume, 0~5, derived from threshold bands of the smoothed RMS; ideal for a simple "bars" style volume indicator. |
| [qiumingdll_volume_get_peak](qiumingdll_volume_get_peak.md) | Return the peak value of the current microphone volume, 0~1; the value is smoothed as well and reflects the instantaneous strength of the sound. |
| [qiumingdll_volume_get_rms](qiumingdll_volume_get_rms.md) | Return the root-mean-square (RMS) value of the current microphone volume, 0~1; the value is already smoothed by the smoothing factor, which makes it suitable for driving a volume bar. |
| [qiumingdll_volume_is_active](qiumingdll_volume_is_active.md) | Query whether the volume module is currently recording: 1 means recording, 0 means not started. |
| [qiumingdll_volume_set_silence_threshold](qiumingdll_volume_set_silence_threshold.md) | Set the silence threshold: audio whose smoothed RMS is below this value counts as silence (get_level returns 0). Default 0.01. |
| [qiumingdll_volume_set_smoothing](qiumingdll_volume_set_smoothing.md) | Set the volume smoothing factor, which controls how strongly get_rms and get_peak are smoothed. Default 0.3; a larger factor is more responsive, a smaller one is smoother. |
| [qiumingdll_volume_start](qiumingdll_volume_start.md) | Open the system default microphone and start collecting volume data; a return value of 0 means recording started successfully. |
| [qiumingdll_volume_stop](qiumingdll_volume_stop.md) | Stop microphone recording and release the capture device, resetting the volume state to zero while keeping the configured parameters (silence threshold, smoothing factor). |

[Back to the documentation home](../README.md)
