# qiumingdll_winsplit_exists(splitId)

Check whether the specified split window ID is valid (has been created and not yet destroyed).

## Signature

```gml
qiumingdll_winsplit_exists(splitId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window ID to check, value 1 ~ 16 |

## Returns

| Value | Description |
|----|------|
| 1 | splitId is valid: within 1~16 and the split window exists (including hidden windows) |
| 0 | splitId is invalid: outside 1~16, or that slot currently has no active window; on non-Windows platforms the wrapper returns 0 directly |

## Usage

- Precondition: none (safely returns 0 even when uninitialized).
- Unlike `qiumingdll_winsplit_get_count`, this function checks whether "a specific ID is usable" and is suitable for defensive checks before calling other functions.
- A hidden window (hidden via hide) still returns 1; it returns 0 only after destruction.
- Slots are reused: if split_1 is destroyed and a newly created window happens to take slot number 1, exists(1) returns 1 again, but it now refers to the new window.

## Example

```gml
// In the controller object's Step event: check before operating on a split window that no longer exists
if (keyboard_check_pressed(ord("S")))
{
    // Make sure the window still exists before adjusting its position
    if (qiumingdll_winsplit_exists(global.split_1))
    {
        qiumingdll_winsplit_set_position(global.split_1, mouse_x, mouse_y);
    }
    else
    {
        show_debug_message("Split window does not exist; create it first");
    }
}
```

## Related functions

- [qiumingdll_winsplit_get_count](qiumingdll_winsplit_get_count.md)
- [qiumingdll_winsplit_destroy](qiumingdll_winsplit_destroy.md)
- [qiumingdll_winsplit_create](qiumingdll_winsplit_create.md)
- [qiumingdll_winsplit_get_info](qiumingdll_winsplit_get_info.md)
