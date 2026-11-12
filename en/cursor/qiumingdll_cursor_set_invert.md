# qiumingdll_cursor_set_invert(enable)

Enables or disables the "cursor moves opposite to the mouse" effect. Once enabled, the cursor moves in the direction opposite to the physical mouse movement across the entire system, not just the game window.

## Signature

```gml
qiumingdll_cursor_set_invert(enable)
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| enable | Real | Yes | Non-zero = enable the effect; 0 = disable the effect and restore |

## Returns

| Value | Description |
|-------|-------------|
| 1 | The effect is enabled after the call |
| 0 | The effect is disabled after the call (either disabled successfully or failed to enable — for example, the system refused to install the global hook) |

## Usage

- Precondition: on Windows, `qiumingdll_init()` must be called first.
- Platform limit: Windows only.
- Behavior details:
  - Enabling records the current cursor position as the "restore point"; disabling the effect (or automatic restoration) puts the cursor back at that position.
  - Implemented with a `WH_MOUSE_LL` global hook, so it affects the whole system, including other programs. Do not leave it enabled for long periods without the player's knowledge.
  - When the cursor reaches a screen edge it **wraps around** to the other side and keeps moving in reverse, so it never gets stuck at the edge.
  - In-game `mouse_x` / `mouse_y` also report the inverted position; programs that read hardware movement directly through Raw Input are unaffected.
- Cancellation (any one of):
  - call `qiumingdll_cursor_set_invert(0)` again;
  - while the effect is active, press **F12 eight times within 1.5 seconds** (a global hotkey; the game window does not need focus, and the count restarts if the interval between two presses exceeds 1.5 seconds);
  - when the DLL is unloaded (`qiumingdll_free()`) or the game process exits, the effect is **restored automatically**, leaving no system-level changes behind.
- Note: this function affects the real system cursor. Use it only when the player has been clearly informed or as a controllable easter egg; the F12 safety valve cannot be disabled by game code.

## Example

```gml
/// Prank trap: invert for 5 seconds after stepping on a mine
if (place_meeting(x, y, obj_trap)) {
    qiumingdll_cursor_set_invert(1);   // returns 1, now enabled
    alarm[0] = room_speed * 5;
}

/// (Alarm 0 event)
qiumingdll_cursor_set_invert(0);       // restore the cursor position
show_message("Your movement is back to normal!");
```

```gml
// Players can always rescue themselves: press F12 8 times quickly while the effect is active to cancel it
if (qiumingdll_cursor_get_invert()) {
    draw_text(8, 8, "Hint: press F12 8 times to cancel inverted movement");
}
```

## Related functions

- [qiumingdll_cursor_get_invert](qiumingdll_cursor_get_invert.md)
