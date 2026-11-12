# qiumingdll_ime_fix_conflict()

Fix IME conflicts: move the system IME composition window to an invisible position so the IME candidate box no longer covers the game screen.

## Signature

```gml
qiumingdll_ime_fix_conflict()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters. The window handle is obtained automatically by the wrapper layer (on Windows the handle of the current game window is passed in automatically) |

## Returns

| Value | Description |
|----|------|
| 0 | Success: the composition window has been moved to an invisible position, and the target window is recorded internally for subsequent IME functions to use |
| 1 | Invalid window: no valid game window handle could be obtained. Non-Windows platforms always return this value |
| 2 | Unable to obtain the IME context: the window is valid, but its IME context could not be retrieved (or created) |

## Usage

- Platform limit: Windows only; other platforms such as macOS, Linux, HTML5 and UWP always return 1.
- Purpose: fixes the "IME conflict". The candidate/composition windows that Chinese IMEs (such as Microsoft Pinyin or Sogou Pinyin) pop up while typing can cover the game screen; after calling this function the system composition window is placed at an invisible position, so the screen is no longer covered.
- Behavior details: on success the current window handle is saved internally, and subsequent functions such as `qiumingdll_ime_switch`, `qiumingdll_ime_get_mode` and `qiumingdll_ime_set_inline_position` operate on that window first (falling back to the foreground window only when the recorded window cannot be found).
- Calling it once at game startup is usually enough; you may also call it again when entering a scene that needs Chinese input.
- This function only hides the system composition window; it does not enable inline mode. If you need to draw the candidate box yourself inside the game, use it together with `qiumingdll_ime_set_inline_position`.
- It can be called without initialization; however, if the DLL extension has not been initialized yet (the wrapper layer cannot find the external functions), it returns 1 directly.
- Calling it on non-Windows platforms has no side effects, so cross-platform code can call it without a platform check.

## Example

```gml
// Call once at game startup to stop the IME candidate box from covering the screen
if (os_type == os_windows) {
    var result = qiumingdll_ime_fix_conflict();
    if (result == 0) {
        show_debug_message("IME conflict fixed successfully");
    } else {
        show_debug_message("Failed to fix IME conflict: " + string(result));
    }
}
```

## Related functions

- [qiumingdll_ime_set_inline_position](qiumingdll_ime_set_inline_position.md)
- [qiumingdll_ime_reset_inline](qiumingdll_ime_reset_inline.md)
- [qiumingdll_ime_input_create](qiumingdll_ime_input_create.md)
