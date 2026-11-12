# qiumingdll_ime_get_mode()

Get the IME's current input mode (English/Chinese).

## Signature

```gml
qiumingdll_ime_get_mode()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 0 | English mode (the IME's Chinese conversion is disabled) |
| 1 | Chinese mode (the IME's Chinese conversion is enabled) |
| -1 | Retrieval failed: the target window could not be found or the IME context could not be obtained. Non-Windows platforms always return this value |

## Usage

- Platform limit: Windows only; other platforms always return -1.
- This function is a read-only query; it does not modify any IME state.
- Target window: the recorded window (set by `qiumingdll_ime_fix_conflict` / `qiumingdll_ime_set_inline_position`) is used with priority; otherwise the current foreground window is used.
- Usage: poll it every frame to display a mode label, or use status bit 0x08 (input mode changed, see `qiumingdll_ime_get_state`) to read it only when the mode changes, avoiding frequent calls.
- Actual meaning: Chinese mode means the IME conversion state contains the "native Chinese" flag (e.g. the Chinese state of a Chinese IME); in English mode, keyboard input produces English characters directly.
- The result may match what the system IME tray icon shows; if no Chinese IME is enabled on the system, it usually returns 0.

## Example

```gml
// Display the current input mode every frame
var mode = qiumingdll_ime_get_mode();
if (mode == -1) {
    draw_text(10, 10, "IME: unknown");
} else if (mode == 0) {
    draw_text(10, 10, "IME: EN");
} else {
    draw_text(10, 10, "IME: CN");
}
```

## Related functions

- [qiumingdll_ime_switch](qiumingdll_ime_switch.md)
- [qiumingdll_ime_get_state](qiumingdll_ime_get_state.md)
- [qiumingdll_ime_poll_json](qiumingdll_ime_poll_json.md)
