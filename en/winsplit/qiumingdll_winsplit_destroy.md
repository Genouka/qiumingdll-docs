# qiumingdll_winsplit_destroy(splitId)

Destroy the specified split window: close the window, release its slot and shape resources, and the window ID can then be reused by a newly created split window.

## Signature

```gml
qiumingdll_winsplit_destroy(splitId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | ID of the split window to destroy, value 1 ~ 16, must be an ID returned by qiumingdll_winsplit_create that still exists |

## Returns

| Value | Description |
|----|------|
| 1 | Destruction succeeded (or the window was already destroyed but the ID was once valid) |
| 0 | Destruction failed: splitId is invalid (outside 1~16, or the slot was never active); on non-Windows platforms the wrapper returns 0 directly |

## Usage

- Precondition: `qiumingdll_winsplit_init()` has been called successfully, and the split window for splitId exists.
- After destruction the ID becomes invalid immediately and `qiumingdll_winsplit_exists` returns 0; do not call any function on a destroyed ID again.
- If animations are in progress (position/size animation, path animation, batch animation) they are stopped and cleared automatically on destruction.
- Destruction does not affect other split windows, nor the original game window.
- This is the programmatic destruction path: even if the user closes the split window via its title-bar X (triggering self-destruction and possibly a linked close), the internal slot is still released and can be reused afterwards.

## Example

```gml
// In the controller object's Step event: press Backspace to destroy split window 1
if (keyboard_check_pressed(vk_backspace))
{
    if (global.split_1 > 0)
    {
        if (qiumingdll_winsplit_destroy(global.split_1) == 1)
        {
            global.split_1 = 0; // Set to 0 to avoid later misuse
            show_debug_message("Split window 1 destroyed");
        }
    }
}
```

## Related functions

- [qiumingdll_winsplit_create](qiumingdll_winsplit_create.md)
- [qiumingdll_winsplit_destroy_all](qiumingdll_winsplit_destroy_all.md)
- [qiumingdll_winsplit_exists](qiumingdll_winsplit_exists.md)
- [qiumingdll_winsplit_get_count](qiumingdll_winsplit_get_count.md)
