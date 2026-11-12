# qiumingdll_procdetect_streaming()

Detects whether screen recording and streaming software exists among system processes, for protecting story content or reporting recording status.

## Signature

```gml
qiumingdll_procdetect_streaming()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 1 | At least one screen recording/streaming software process is running |
| 0 | No target process detected, or called on a non-Windows platform |

## Usage

- Prerequisite: call `qiumingdll_init()` first on Windows.
- Platform support: Windows only; other platforms always return 0.
- Behavior: internally walks a snapshot of system processes and compares each process name (case-insensitive, exact exe file name) against a built-in list, returning 1 on the first hit. The built-in list includes:
  - Streaming tools: OBS Studio (obs64.exe, obs32.exe, obs.exe), XSplit (xsplit.core.exe, xsplit.gamecaster.exe), Streamlabs OBS (streamlabs obs.exe, streamlabsobs.exe, sl.exe), vMix (vmix64.exe, vMix.exe), Wirecast (wirecast.exe), etc.;
  - Screen recorders: Bandicam (bandicam.exe), Fraps (fraps.exe), Mirillis Action (action.exe, action!.exe, mirillis_action.exe), ShareX (sharex.exe), Camtasia (camtasia.exe, camrec.exe), Dxtory (dxtory.exe), ocam (ocam.exe, ocam_capture.exe), etc.;
  - GPU capture: NVIDIA ShadowPlay / GeForce Experience (shadowplay.exe, nvidia share.exe, gamecapture.exe, nvcontainer.exe), etc.;
  - Stream relay/connection tools: livestreamer.exe, streamlink.exe, mediasourcehelper.exe, etc.
- Detection works by "comparing process names against a list", so it only works for the **default executable file names** of the listed software; renamed software may go undetected, and processes sharing a name may cause false positives.
- Note: this function performs no blocking action, it only returns the detection result.
- Typical use: story-driven games pausing unpublished content when recording is detected, showing a "do not record" notice, or adjusting video output as needed.

## Example

```gml
// Check for recording before a key story segment
qiumingdll_init();

if (qiumingdll_procdetect_streaming() == 1)
{
    // Someone is recording/streaming: pause the story and notify
    show_message("Screen recording or streaming software detected; please close it before continuing this story segment");
    // ...... suspend the story logic
}
else
{
    // Environment clean, play the story normally
}
```

## Related functions

- [qiumingdll_procdetect_cheatengine](qiumingdll_procdetect_cheatengine.md)
- [qiumingdll_procdetect_process](qiumingdll_procdetect_process.md)
- [qiumingdll_init](qiumingdll_init.md)
