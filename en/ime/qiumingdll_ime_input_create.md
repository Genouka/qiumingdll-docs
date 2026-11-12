# qiumingdll_ime_input_create(x, y, w, h, [font])

Creates a one-stop "IME input box" solution: initializes the input box and creates all instance variables with the `ime_` prefix.

## Signature

```gml
qiumingdll_ime_input_create(x, y, w, h, [font])
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| x | Real | Yes | X coordinate of the input box's top-left corner |
| y | Real | Yes | Y coordinate of the input box's top-left corner |
| w | Real | Yes | Input box width (pixels) |
| h | Real | Yes | Input box height (pixels) |
| font | Font Asset | No | Font asset to use; when omitted, -1 (default font) is used |

## Returns

No return value (this function does not return anything).

## Usage

- Call once in the object's Create event. After calling it you must also use: `qiumingdll_ime_input_step()` in the Step event, `qiumingdll_ime_input_draw()` in the Draw event (or draw_text + draw_candidates), and `qiumingdll_ime_input_cleanup()` in the Clean Up event.
- Automatic platform detection: Windows with the DLL extension initialized → `ime_use_dll = true`, and `qiumingdll_ime_fix_conflict()` is called automatically to fix IME conflicts; other platforms or an uninitialized extension → `ime_use_dll = false`, falling back to the `keyboard_string` approach (no composition text and no candidate list).
- After the call the instance owns the following variables (which can be read and written directly for customization):

| Variable | Default | Description |
|----------|---------|-------------|
| ime_x / ime_y / ime_w / ime_h | Passed-in values | Input box position and size |
| ime_text | "" | Confirmed text |
| ime_max_length | 0 | Maximum character count, 0 = unlimited |
| ime_focused | true | Whether the box has focus (step/draw do nothing when false) |
| ime_composing | false | Whether composition input is in progress |
| ime_comp_text | "" | Current composition text |
| ime_comp_cursor | 0 | Cursor position within the composition text |
| ime_cand_list | ds_list | Candidate list (ds_list, do not destroy manually) |
| ime_cand_sel | -1 | Index of the currently selected candidate |
| ime_input_mode | 0 | Input mode (0=English, 1=Chinese) |
| ime_use_dll | Automatic | Whether the DLL approach is used (result of platform detection) |
| ime_kb_string | "" | keyboard_string cache in fallback mode |
| ime_cursor_blink | 0 | Cursor blink timer (cycles 0~59) |
| ime_on_commit | -1 | Commit callback script index (-1 = unused) |
| ime_on_compose_change | -1 | Composition-change callback script index (-1 = unused) |
| ime_on_mode_change | -1 | Input-mode-change callback script index (-1 = unused) |
| ime_color_bg / ime_color_text / ime_color_comp / ime_color_cursor | white/black/blue/red | Background, text, composition text and cursor colors |
| ime_color_cand_bg / ime_color_cand_text | black/white | Candidate box background and candidate text colors |
| ime_color_cand_sel_bg / ime_color_cand_sel_text | navy/yellow | Selected candidate background and text colors |
| ime_font | -1 | Font (-1 = default font) |

- Callback scripts may also be method variables when they are not script assets (invoked internally with `script_execute`).
- It is recommended to set the needed `ime_*` variables (such as colors, font and callbacks) immediately after creation, then start input.

## Example

```gml
// Create event: create the input box and register callbacks
qiumingdll_ime_input_create(100, 200, 320, 32);
ime_max_length = 30;                       // at most 30 characters
ime_font = fnt_chat;                       // custom font
ime_color_bg = c_silver;                   // custom background
ime_on_commit = scr_on_ime_commit;         // register commit callback
ime_on_compose_change = scr_on_ime_compose;// register composition-change callback
ime_on_mode_change = scr_on_ime_mode;      // register mode-change callback
```

```gml
// Callback script scr_on_ime_commit(commit_text) -- the committed text is entered
show_debug_message("Commit: " + commit_text);
```

```gml
// Callback script scr_on_ime_compose(composing, comp_text, comp_cursor)
show_debug_message("Composing: " + string(composing) + " " + comp_text + " cursor@" + string(comp_cursor));
```

```gml
// Callback script scr_on_ime_mode(mode) -- 0=English 1=Chinese
show_debug_message("Input mode: " + (mode == 1 ? "Chinese" : "English"));
```

## Related functions

- [qiumingdll_ime_input_step](qiumingdll_ime_input_step.md)
- [qiumingdll_ime_input_draw](qiumingdll_ime_input_draw.md)
- [qiumingdll_ime_input_cleanup](qiumingdll_ime_input_cleanup.md)
- [qiumingdll_ime_fix_conflict](qiumingdll_ime_fix_conflict.md)
