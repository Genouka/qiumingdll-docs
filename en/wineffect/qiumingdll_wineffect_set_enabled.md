# qiumingdll_wineffect_set_enabled(enable)

Master switch: enables or stops window effects. Stopping restores the window position and window region immediately.

## Signature

```gml
qiumingdll_wineffect_set_enabled(enable)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| enable | Real | Yes | Non-zero = enable; 0 = stop and restore the window |

## Returns

| Value | Description |
|----|------|
| 1 | Operation succeeded |
| 0 | Failure: `qiumingdll_wineffect_init()` has not been called, or the window is invalid, or subclass/timer installation failed |

## Usage

- Prerequisite: `qiumingdll_wineffect_init()` must be called first.
- Enabling installs the window subclass and the 16ms timer; with all strengths at 0 there is no visible effect, but the state bit still reports "enabled".
- Stopping (enable=0) restores the window position and the original window region saved at enable time; the three strength values are retained and take effect again when re-enabled.
- When the window is minimized, invisible or loses the foreground, effects pause automatically and restore; they resume automatically once back in the foreground.
- A maximized window cannot be moved: shake and tear jumps are skipped, while distortion/tear region effects still apply.

## Example

```gml
/// Enable when entering the glitch room
qiumingdll_wineffect_set_shake(0.6);
qiumingdll_wineffect_set_enabled(1);

/// Stop and restore when leaving the room
qiumingdll_wineffect_set_enabled(0);
```

## Related functions

- [qiumingdll_wineffect_init](qiumingdll_wineffect_init.md)
- [qiumingdll_wineffect_stop](qiumingdll_wineffect_stop.md)
- [qiumingdll_wineffect_get_state](qiumingdll_wineffect_get_state.md)
