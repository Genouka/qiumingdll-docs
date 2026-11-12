# qiumingdll_ime_input_cleanup()

Clean up input-box resources: destroy the candidate list ds_list and leave inline mode in DLL mode.

## Signature

```gml
qiumingdll_ime_input_cleanup()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

No return value (this function does not return anything).

## Usage

- Call it in the object's Clean Up event (Destroy event), paired with `qiumingdll_ime_input_create`; every instance that has created an input box should call it when destroyed, to prevent ds_list leaks.
- Internal behavior:
  1. destroys `ime_cand_list` (the ds_list);
  2. in DLL mode (`ime_use_dll == true`), automatically calls `qiumingdll_ime_reset_inline()` to leave inline mode, restore the system's default IME behavior and clear all IME state.
- Safe to call repeatedly: `ime_cand_list` is checked with `ds_exists` before being destroyed; normal usage is still to call it only once.
- Callback scripts (`ime_on_*`) need no extra release (script resources are managed by the engine; method variables passed in do not need to be freed either).
- It must also be called on non-Windows platforms (the fallback mode creates a ds_list too).
- Note: if you want to keep the contents of `ime_text` before destroying the instance, save it elsewhere first; this function does not save the text.

## Example

```gml
// Clean Up event: release the input-box resources
qiumingdll_ime_input_cleanup();
```

```gml
// Manual teardown: when the input box is no longer needed
// Take the text out first (if you still need it)
saved_text = ime_text;
qiumingdll_ime_input_cleanup();
instance_destroy();
```

## Related functions

- [qiumingdll_ime_input_create](qiumingdll_ime_input_create.md)
- [qiumingdll_ime_reset_inline](qiumingdll_ime_reset_inline.md)
- [qiumingdll_ime_poll_destroy](qiumingdll_ime_poll_destroy.md)
