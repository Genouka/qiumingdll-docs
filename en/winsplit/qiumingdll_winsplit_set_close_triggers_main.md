# qiumingdll_winsplit_set_close_triggers_main(splitId, triggers)

Sets whether the user closing this split window also closes the original game main window (linked close).

## Signature

```gml
qiumingdll_winsplit_set_close_triggers_main(splitId, triggers)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window ID, value 1 ~ 16, must exist |
| triggers | Real/Bool | yes | Whether to link: non-zero (true) = closing this split window also closes the main window (default), 0 (false) = close only the split window without affecting the main window |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Failed: splitId is invalid or does not exist; on non-Windows platforms the wrapper returns 0 directly |

## Usage

- Prerequisite: `qiumingdll_winsplit_init()` has been called successfully and the split window for splitId exists.
- The default at creation is `closeTriggersMain = true` (closing the split window closes the main window as well).
- The linkage is triggered only on the "user close" path (titlebar X, system menu close); programmatic calls to destroy / destroy_all / cleanup do not trigger it.
- When the user clicks close on a split window, the split window is destroyed first and a close request is then sent to the main game window — which usually means the game exits. If the game defines a "close confirmation / save prompt", the prompt appears as usual.
- Recommendation for scenes with multiple split windows: keep at least one "exit entry" (the linked one) and set the others to false, so that the user cannot quit the game by accident.
- Together with `qiumingdll_winsplit_set_closable`: with closable=false the linkage logic is never reached.

## Example

```gml
// In the Create event of a controller object, configure the close linkage after creating the split windows:
// Window 1 acts as the "exit gate" (keeps the default linkage); closing window 2 does not close the main window
if (global.split_2 > 0)
    qiumingdll_winsplit_set_close_triggers_main(global.split_2, false);
```

```gml
// In the Step event of a controller object: press E to toggle the close linkage of split window 1
if (keyboard_check_pressed(ord("E")))
{
    global.split_link_main = !global.split_link_main;
    qiumingdll_winsplit_set_close_triggers_main(global.split_1, global.split_link_main);
}
```

## Related functions

- [qiumingdll_winsplit_set_closable](qiumingdll_winsplit_set_closable.md)
- [qiumingdll_winsplit_set_titlebar](qiumingdll_winsplit_set_titlebar.md)
- [qiumingdll_winsplit_destroy](qiumingdll_winsplit_destroy.md)
