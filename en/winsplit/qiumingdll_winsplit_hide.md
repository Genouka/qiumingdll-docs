# qiumingdll_winsplit_hide(splitId)

Hide the specified split window without affecting its internal state; it can be shown again at any time with show.

## Signature

```gml
qiumingdll_winsplit_hide(splitId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window ID, value 1 ~ 16, must exist |

## Returns

| Value | Description |
|----|------|
| 1 | Hidden successfully |
| 0 | Failure: splitId is invalid or does not exist; on non-Windows platforms the wrapper returns 0 directly |

## Usage

- Precondition: `qiumingdll_winsplit_init()` has been called successfully, and the split window for splitId exists.
- Hiding only stops displaying; the window is still "alive": `qiumingdll_winsplit_exists` still returns 1, and it does not count as a reusable slot; position, size, source region, shape and all other settings are preserved.
- Difference from destroy: hide is reversible, destroy is irreversible and frees the slot.
- Hiding does not hide the original game window; the two are independent.

## Example

```gml
// Hide all split windows during a story sequence and show them again when it ends
// (e.g. in a script of the scene manager object)

// Hide
qiumingdll_winsplit_hide(global.split_1);
qiumingdll_winsplit_hide(global.split_2);

// ...a few seconds later, the sequence ends: restore all split windows
qiumingdll_winsplit_show(global.split_1);
qiumingdll_winsplit_show(global.split_2);
```

## Related functions

- [qiumingdll_winsplit_show](qiumingdll_winsplit_show.md)
- [qiumingdll_winsplit_destroy](qiumingdll_winsplit_destroy.md)
- [qiumingdll_winsplit_hide_original](qiumingdll_winsplit_hide_original.md)
