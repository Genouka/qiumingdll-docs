# IME module

IME integration: composition text, candidates, inline editing and polling; the input drawing functions must be called in a draw event to display the candidate area.

23 functions in total.

## Function index

| Function | Description |
|------|------|
| [qiumingdll_ime_fix_conflict](qiumingdll_ime_fix_conflict.md) | Fix IME conflicts: move the system IME composition window to an invisible position so the IME candidate box no longer covers the game screen. |
| [qiumingdll_ime_get_candidate](qiumingdll_ime_get_candidate.md) | Get the candidate text at the specified index. |
| [qiumingdll_ime_get_candidate_count](qiumingdll_ime_get_candidate_count.md) | Get the number of candidates in the current candidate list. |
| [qiumingdll_ime_get_candidate_selection](qiumingdll_ime_get_candidate_selection.md) | Get the index of the selected candidate in the current candidate list. |
| [qiumingdll_ime_get_commit](qiumingdll_ime_get_commit.md) | Simplified commit-text retrieval: checks status bit 0x02 internally, returning the commit text when there is one and an empty string otherwise. |
| [qiumingdll_ime_get_commit_text](qiumingdll_ime_get_commit_text.md) | Get the commit text confirmed for this input; the text is cleared after being read. |
| [qiumingdll_ime_get_composition_cursor](qiumingdll_ime_get_composition_cursor.md) | Get the cursor position within the composition text (character offset, starting at 0). |
| [qiumingdll_ime_get_composition_text](qiumingdll_ime_get_composition_text.md) | Get the current IME composition text (the string, such as pinyin or strokes, that has not yet been confirmed). |
| [qiumingdll_ime_get_mode](qiumingdll_ime_get_mode.md) | Get the IME's current input mode (English/Chinese). |
| [qiumingdll_ime_get_state](qiumingdll_ime_get_state.md) | Return the IME state-change flags (bitmask) used to decide which data to read next. |
| [qiumingdll_ime_input_cleanup](qiumingdll_ime_input_cleanup.md) | Clean up input-box resources: destroy the candidate list ds_list and leave inline mode in DLL mode. |
| [qiumingdll_ime_input_create](qiumingdll_ime_input_create.md) | One-stop "IME input box" solution: initialize the input box and create every `ime_`-prefixed instance variable. |
| [qiumingdll_ime_input_draw](qiumingdll_ime_input_draw.md) | Draw the complete IME input box: background + border + confirmed text + composition text + underline + caret + candidate box. |
| [qiumingdll_ime_input_draw_candidates](qiumingdll_ime_input_draw_candidates.md) | Draw only the candidate list (candidate box background + border + candidates + selection highlight) at a specified position. |
| [qiumingdll_ime_input_draw_text](qiumingdll_ime_input_draw_text.md) | Draw only the text portion of the input box (confirmed text + composition text + underline + caret), without the background or candidate list; suited to custom rendering. |
| [qiumingdll_ime_input_step](qiumingdll_ime_input_step.md) | Poll IME state in the Step event and update the input box's internal data (text, composition, candidates, callbacks). |
| [qiumingdll_ime_is_composing](qiumingdll_ime_is_composing.md) | Query whether a composition is currently in progress. |
| [qiumingdll_ime_poll](qiumingdll_ime_poll.md) | Poll all IME state at once, parse it into a GML ds_map and return it. |
| [qiumingdll_ime_poll_destroy](qiumingdll_ime_poll_destroy.md) | Destroy the ds_map returned by `qiumingdll_ime_poll()`, along with the candidate-list ds_list it contains. |
| [qiumingdll_ime_poll_json](qiumingdll_ime_poll_json.md) | Poll all IME state at once and return a JSON string. |
| [qiumingdll_ime_reset_inline](qiumingdll_ime_reset_inline.md) | Leave inline mode, restore the default behavior of the system IME windows and clear all IME state. |
| [qiumingdll_ime_set_inline_position](qiumingdll_ime_set_inline_position.md) | Inline the IME composition and candidate windows at a specified position in the game window's client area and enable inline mode. |
| [qiumingdll_ime_switch](qiumingdll_ime_switch.md) | Switch the current IME: switch to English/Chinese mode, or cycle through the IMEs installed on the system. |

[Back to documentation home](../README.md)
