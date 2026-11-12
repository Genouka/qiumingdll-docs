# qiumingdll_winsplit_set_closable(splitId, closable)

Sets whether the given split window may be closed by the user (through the X button in the titlebar or "Close" in the system menu).

## Signature

```gml
qiumingdll_winsplit_set_closable(splitId, closable)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window ID, value 1 ~ 16, must exist |
| closable | Real/Bool | yes | Whether the user may close it: non-zero (true) = closable (default), 0 (false) = not closable |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Failed: splitId is invalid or does not exist; on non-Windows platforms the wrapper returns 0 directly |

## Usage

- Prerequisite: `qiumingdll_winsplit_init()` has been called successfully and the split window for splitId exists.
- The default at creation is `closable = true` (the user can close it).
- With closable = false: clicking the titlebar X does nothing; the "Close" item in the system menu (Alt+Space) is grayed out and cannot be clicked. When a titlebar is present, the close item of the system menu is grayed out accordingly.
- This function only intercepts "user close": programmatic calls to `qiumingdll_winsplit_destroy` / `destroy_all` are unaffected and can still destroy the window.
- Relationship with `qiumingdll_winsplit_set_close_triggers_main`: the close_triggers_main linkage is triggered only when an actual "user close" action occurs.
- If the window has no titlebar (`set_titlebar(splitId, false)`), the system-menu close entry has already been removed, and closable still applies to the other close paths (such as the WM_CLOSE message).

## Example

```gml
// In the Step event of a controller object: press L to lock/unlock closing of split window 1
if (keyboard_check_pressed(ord("L")))
{
    global.split_locked = !global.split_locked;
    qiumingdll_winsplit_set_closable(global.split_1, !global.split_locked);

    if (global.split_locked)
        show_debug_message("Split window locked: the user cannot close it (the program can still destroy it)");
}
```

## Related functions

- [qiumingdll_winsplit_set_close_triggers_main](qiumingdll_winsplit_set_close_triggers_main.md)
- [qiumingdll_winsplit_set_titlebar](qiumingdll_winsplit_set_titlebar.md)
- [qiumingdll_winsplit_destroy](qiumingdll_winsplit_destroy.md)
