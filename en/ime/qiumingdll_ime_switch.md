# qiumingdll_ime_switch(action)

Switches the current input method: switches to English/Chinese mode, or cycles among the input methods installed on the system.

## Signature

```gml
qiumingdll_ime_switch(action)
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| action | Real | Yes | Action to perform: 0=switch to English mode; 1=switch to Chinese mode; 2=switch to the next input method; 3=switch to the previous input method |

## Returns

| Value | Description |
|-------|-------------|
| 0 | Success: the mode was switched or another input method was activated |
| 1 | No target window: no valid foreground window or recorded window could be found. Always returned on non-Windows platforms |
| 2 | No IME context: the window is valid, but its IME context could not be obtained (or created) |
| 3 | Invalid action: the action passed is outside the 0~3 range |

## Usage

- Platform limit: Windows only; always returns 1 on other platforms.
- action 0/1: directly changes the IME's Chinese/English conversion state. action 1 (switch to Chinese) is equivalent to putting the IME into the "Chinese input" state (this may require a Chinese IME to be installed and enabled); action 0 (switch to English) turns off native Chinese conversion.
- action 2/3: switches via the system keyboard layout (next/previous input method). Switching releases the current IME context and re-activates the keyboard layout; this is system-level behavior and does not affect the player/game window itself.
- Target window: prefers the window recorded by `qiumingdll_ime_fix_conflict` or `qiumingdll_ime_set_inline_position`; if none is recorded, the current foreground window is used.
- If the user is in the middle of composing (typing) when the input method is switched, the current composition may be interrupted; call it at an appropriate moment.
- Switching the input method may trigger system IME-switch hints (such as a taskbar icon change); this is normal system behavior.

## Example

```gml
// Force Chinese mode when the input box gains focus
if (box_focused) {
    if (qiumingdll_ime_get_mode() != 1) {
        qiumingdll_ime_switch(1); // switch to Chinese
    }
}

// Cycle input methods when the user presses Tab
if (keyboard_check_pressed(vk_tab)) {
    qiumingdll_ime_switch(2); // next input method
}
```

## Related functions

- [qiumingdll_ime_get_mode](qiumingdll_ime_get_mode.md)
- [qiumingdll_ime_fix_conflict](qiumingdll_ime_fix_conflict.md)
- [qiumingdll_ime_get_state](qiumingdll_ime_get_state.md)
