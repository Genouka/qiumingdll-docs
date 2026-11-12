# qiumingdll_winsplit_get_count()

Return the total number of currently existing split windows (0 ~ 16), used for slot management, UI display, etc.

## Signature

```gml
qiumingdll_winsplit_get_count()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 0 ~ 16 | Number of currently active (not destroyed) split windows; on non-Windows platforms the wrapper returns 0 directly |

## Usage

- Precondition: `qiumingdll_winsplit_init()` has been called successfully (returns 0 when uninitialized).
- Like the get_info/get_count family of query functions, this function is a read-only query with no side effects.
- The maximum is 16: when the return value reaches 16, calling `qiumingdll_winsplit_create` will inevitably return 0 (slots exhausted). You must destroy some windows before creating more.
- Hidden windows (hide) still count toward the number; only destroyed (destroy) windows no longer count.

## Example

```gml
// In the controller object's Step event: press C to create a minimap split window, but check for a free slot first
if (keyboard_check_pressed(ord("C")))
{
    if (qiumingdll_winsplit_get_count() < 16)
    {
        global.split_minimap = qiumingdll_winsplit_create(0, 0, 400, 300, 50, 50, 400, 300);
    }
    else
    {
        show_debug_message("Split window limit reached (16); cannot create more");
    }
}

// Display the count in the Draw GUI event
draw_text(10, 10, "Split windows: " + string(qiumingdll_winsplit_get_count()) + "/16");
```

## Related functions

- [qiumingdll_winsplit_create](qiumingdll_winsplit_create.md)
- [qiumingdll_winsplit_destroy](qiumingdll_winsplit_destroy.md)
- [qiumingdll_winsplit_destroy_all](qiumingdll_winsplit_destroy_all.md)
- [qiumingdll_winsplit_exists](qiumingdll_winsplit_exists.md)
