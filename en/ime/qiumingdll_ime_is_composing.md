# qiumingdll_ime_is_composing()

Queries whether composition input is in progress.

## Signature

```gml
qiumingdll_ime_is_composing()
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|-------|-------------|
| 1 | Composition input is in progress (the user is in the middle of pinyin/stroke input) |
| 0 | Not composing |

Always returns 0 on non-Windows platforms.

## Usage

- Platform limit: Windows only; always returns 0 on other platforms.
- Has the same meaning as bit 0x01 of the `qiumingdll_ime_get_state` state, but this function does not consume one-shot flags (0x02/0x04/0x08), which is cleaner when you only want to test the composition state.
- During composition the system composition window is inline/hidden, and the composition text is drawn by the game itself (see `qiumingdll_ime_get_composition_text`).
- Determining "composing" vs "composition finished": returns 1 from the start of composition until the text is confirmed and entered (or cancelled); returns 0 after confirmation (commit) or cancellation.
- Typical use: disable backspace deletion of confirmed text while composing (to avoid accidental deletion), and restore it after composition ends.

## Example

```gml
// Step event: do not delete confirmed text with backspace while composing
if (keyboard_check_pressed(vk_back)) {
    if (!qiumingdll_ime_is_composing()) {
        if (string_length(text) > 0) {
            text = string_copy(text, 1, string_length(text) - 1);
        }
    }
}
```

## Related functions

- [qiumingdll_ime_get_composition_text](qiumingdll_ime_get_composition_text.md)
- [qiumingdll_ime_get_state](qiumingdll_ime_get_state.md)
- [qiumingdll_ime_input_step](qiumingdll_ime_input_step.md)
