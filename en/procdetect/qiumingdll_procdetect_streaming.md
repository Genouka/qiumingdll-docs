# qiumingdll_procdetect_streaming()

Detects whether common streaming/recording software processes (such as OBS, Streamlabs, etc.) are present on the system, to determine whether the game is being streamed or recorded.

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
| 1 | A streaming/recording software process is running |
| 0 | Not detected, or a non-Windows platform / not initialized (returns 0 in that case) |

## Usage

- Preconditions: on Windows, call `qiumingdll_init()` first.
- Platform limits: Windows only.
- Behavior: matches against a preset list of common streaming/recording software process names; can be used, for example, to adjust on-screen content during a live stream (hide easter eggs, swap textures).
- Note: this function can only match known process names and cannot guarantee coverage of every third-party streaming tool; the result only represents the state at the moment of the call.
- Async mode: by default it reads from the background cache, so the result can lag by up to about 0.5 seconds; safe to call every frame from the Step event without stuttering.

## Example

```gml
/// Step event
if (qiumingdll_procdetect_streaming())
{
    // Live streaming: hide unreleased content
    surprise_content.visible = false;
}
else
{
    surprise_content.visible = true;
}
```

## Related functions

- [qiumingdll_procdetect_cheatengine](qiumingdll_procdetect_cheatengine.md)
- [qiumingdll_procdetect_multiinstance](qiumingdll_procdetect_multiinstance.md)
- [qiumingdll_procdetect_process](qiumingdll_procdetect_process.md)
