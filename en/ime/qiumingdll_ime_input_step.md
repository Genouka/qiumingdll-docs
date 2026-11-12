# qiumingdll_ime_input_step()

Polls the IME state in the Step event and updates the input box's internal data (text, composition, candidates, callbacks).

## Signature

```gml
qiumingdll_ime_input_step()
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| (none) | - | - | This function takes no parameters |

## Returns

No return value (this function does not return anything).

## Usage

- Precondition: `qiumingdll_ime_input_create` must be called first to create the input box (this function depends on the `ime_*` variables it creates).
- Call once per frame in the object's Step event (or End Step).
- When `ime_focused` is false, this function exits immediately and does nothing (incidentally: `ime_focused` can be used to stop the input box from receiving input after it loses focus).
- Internal flow in DLL mode (`ime_use_dll == true`):
  1. Update the cursor blink timer (`ime_cursor_blink`, cycling 0~59);
  2. Every frame, automatically call `qiumingdll_ime_set_inline_position(ime_x + 6 + string_width(ime_text), ime_y + 4)` so the system composition window follows the end of the text;
  3. Call `qiumingdll_ime_poll` to poll all state at once;
  4. Handle committed text: append it to `ime_text`, subject to `ime_max_length` (0 = unlimited); when the limit is exceeded, nothing is appended and no callback is fired;
  5. Update composition state: write `ime_composing` / `ime_comp_text` / `ime_comp_cursor`; fire the composition-change callback when the composition state or text changes;
  6. Copy the candidate list into `ime_cand_list` (a ds_list copy) and update `ime_cand_sel`;
  7. When the input mode changes, update `ime_input_mode` and fire the mode-change callback;
  8. Call `qiumingdll_ime_poll_destroy` to destroy the ds_map returned by the poll;
  9. In DLL mode the backspace key must be handled manually: when no composition is in progress, pressing backspace deletes the last character of `ime_text`.
- Internal flow in fallback mode (`ime_use_dll == false`, non-Windows):
  1. Compare `keyboard_string` with the `ime_kb_string` cache, append the new characters to `ime_text` (also subject to the maximum length), and fire the commit callback;
  2. The backspace key synchronously deletes from both the text and keyboard_string;
  3. Composition- and candidate-related variables are reset (composition text cleared, candidates cleared).
- Callback script parameters (corresponding to the `ime_on_*` variables, -1 means unused):
  - `ime_on_commit(commit_text)`: each piece of text successfully entered;
  - `ime_on_compose_change(composing, comp_text, comp_cursor)`: when composition starts/ends or the composition text changes;
  - `ime_on_mode_change(mode)`: when the IME mode changes (0=English, 1=Chinese).
- Callbacks may take a script asset index or a method variable (executed internally with `script_execute`).

## Example

```gml
// Step event
qiumingdll_ime_input_step();
```

```gml
// Register a method-variable callback in the Create event (requires GameMaker 2022.2+)
qiumingdll_ime_input_create(100, 200, 320, 32);
ime_on_commit = method(self, function(_text) {
    chat_log += _text; // record every entered segment in the chat log
});
```

## Related functions

- [qiumingdll_ime_input_create](qiumingdll_ime_input_create.md)
- [qiumingdll_ime_input_draw](qiumingdll_ime_input_draw.md)
- [qiumingdll_ime_poll](qiumingdll_ime_poll.md)
- [qiumingdll_ime_set_inline_position](qiumingdll_ime_set_inline_position.md)
