# Cursor module

Global cursor inversion: once enabled, the system cursor moves in the opposite direction to the physical mouse movement (for example, moving the mouse right moves the cursor left). Suited to pranks, trick levels, hidden easter eggs and similar scenarios.

- Implementation: a `WH_MOUSE_LL` global low-level mouse hook plus `SetCursorPos` to rewrite the cursor position in reverse; when the cursor reaches a screen edge it wraps around to the other side and keeps moving in reverse, so it never gets stuck.
- Cancellation: `qmCursorSetInvert(0)`, pressing **F12 eight times within 1.5 seconds** while the effect is active (a global hotkey; the game does not need focus), or automatic restoration when the DLL is unloaded / the game exits.
- Restoration behavior: disabling the effect puts the cursor back where it was before enabling and immediately restores normal mouse movement, leaving no system-level changes behind.

2 functions in total.

## Function index

| Function | Description |
|----------|-------------|
| [qiumingdll_cursor_set_invert](qiumingdll_cursor_set_invert.md) | Enable / disable the "cursor moves opposite to the mouse" effect. |
| [qiumingdll_cursor_get_invert](qiumingdll_cursor_get_invert.md) | Query whether cursor inversion is currently active. |

[Back to documentation home](../README.md)
