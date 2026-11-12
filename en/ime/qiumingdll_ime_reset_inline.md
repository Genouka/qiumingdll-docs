# qiumingdll_ime_reset_inline()

Cancels inline mode, restores the default behavior of the system IME windows, and clears all IME state.

## Signature

```gml
qiumingdll_ime_reset_inline()
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|-------|-------------|
| 0 | Success: inline mode is cancelled and all IME state is cleared |
| 1 | No target window: no valid window could be found. Always returned on non-Windows platforms |

## Usage

- Platform limit: Windows only; always returns 1 on other platforms.
- Purpose: undoes every effect of `qiumingdll_ime_set_inline_position`:
  - The composition window and candidate window return to the system default style and position (the system may pop the candidate box up again near the cursor / at the bottom of the screen);
  - Window message handling is uninstalled (IME messages are no longer intercepted);
  - All internal state is cleared: composition text, composition cursor, committed text, candidate list, selected candidate, state flags, etc.
- When to use: call it when the input box is closed, the window is switched, or the game exits, so that leftover inline state does not affect other interfaces.
- Difference from `qiumingdll_ime_fix_conflict`: this function restores the system default behavior (including the composition window that was hidden before the fix); if the game still needs to hide the system candidate box, call `qiumingdll_ime_fix_conflict` again.
- In the ime_input wrapper family, `qiumingdll_ime_input_cleanup` calls this function automatically in DLL mode, so there is no need to call it again manually.

## Example

```gml
// Cancel inline mode when the input box is closed
if (input_box_closed) {
    qiumingdll_ime_reset_inline();
}
```

```gml
// Reset first, then re-apply inline mode when moving the input box
qiumingdll_ime_reset_inline();
qiumingdll_ime_set_inline_position(100, 200);
```

## Related functions

- [qiumingdll_ime_set_inline_position](qiumingdll_ime_set_inline_position.md)
- [qiumingdll_ime_fix_conflict](qiumingdll_ime_fix_conflict.md)
- [qiumingdll_ime_input_cleanup](qiumingdll_ime_input_cleanup.md)
