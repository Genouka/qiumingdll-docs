# qiumingdll_winsplit_destroy_all()

Destroy all currently existing split windows at once; commonly used when switching scenes, returning to the title screen, or other situations that need to "clear the screen".

## Signature

```gml
qiumingdll_winsplit_destroy_all()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 1 | Call succeeded (regardless of how many split windows existed; also 1 when there are none) |
| 0 | Non-Windows platform; the wrapper returns 0 directly |

## Usage

- Precondition: `qiumingdll_winsplit_init()` has been called successfully; calling this function when uninitialized does not affect the original window.
- Equivalent to calling `qiumingdll_winsplit_destroy` on every existing split window one by one.
- After destruction `qiumingdll_winsplit_get_count()` returns 0; all splitIds become invalid and `qiumingdll_winsplit_exists` returns 0 for all of them.
- Note: this function only destroys split windows and does not restore the original game window. If the original window was hidden before, call `qiumingdll_winsplit_show_original()` separately to restore it.
- Destroying windows does not send a close message to the main window (does not trigger the closeTriggersMain link).

## Example

```gml
// In the controller object's Step event: press Delete to clear all split windows
if (keyboard_check_pressed(vk_delete))
{
    qiumingdll_winsplit_destroy_all();

    // Clear the locally recorded IDs to avoid misuse
    global.split_1 = 0;
    global.split_2 = 0;
    global.split_3 = 0;

    // If the original window was hidden before, restore it now
    qiumingdll_winsplit_show_original();
}
```

## Related functions

- [qiumingdll_winsplit_destroy](qiumingdll_winsplit_destroy.md)
- [qiumingdll_winsplit_create](qiumingdll_winsplit_create.md)
- [qiumingdll_winsplit_get_count](qiumingdll_winsplit_get_count.md)
- [qiumingdll_winsplit_show_original](qiumingdll_winsplit_show_original.md)
