# qiumingdll_wineffect_get_state()

Queries the current state of window effects and returns a bitmask.

## Signature

```gml
qiumingdll_wineffect_get_state()
```

## Parameters

None.

## Returns

| Bit | Value | Description |
|----|----|------|
| 0 | 1 | Enabled (`set_enabled(1)` succeeded) |
| 1 | 2 | Shake strength > 0 |
| 2 | 4 | Distortion strength > 0 |
| 3 | 8 | Tear strength > 0 |
| 4 | 16 | Currently active (timer installed, not paused due to focus loss / minimization / invisibility) |

For example, a return value of `19` (1+2+16) means enabled, shake on, and currently drawing.

## Usage

- Use `&` directly to test a bit, e.g. `if (state & 16)` to check whether the effect is currently visible.
- Returns 0 when not initialized.
- When enabled but all three strengths are 0, only bit 0 is returned.
- While the window is unfocused/minimized, bit 4 is temporarily cleared, but the strengths and enabled state are retained.

## Example

```gml
var st = qiumingdll_wineffect_get_state();
if (st & 16) {
    draw_text(8, 8, "Window effects running");
}
if (st & 8) {
    draw_text(8, 24, "Tear enabled");
}
```

## Related functions

- [qiumingdll_wineffect_set_enabled](qiumingdll_wineffect_set_enabled.md)
- [qiumingdll_wineffect_stop](qiumingdll_wineffect_stop.md)
