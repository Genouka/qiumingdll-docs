# qiumingdll_winsplit_set_dwm_thumbnail_mode(enable)

Enables/disables DWM thumbnails as the content source of split windows. **Deprecated**: the new implementation captures the backbuffer with a GPU hook, so calling this function has no effect.

## Signature

```gml
qiumingdll_winsplit_set_dwm_thumbnail_mode(enable)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| enable | Real | yes | Toggle of the old implementation (0 = off, non-zero = on). It is ignored in the new implementation and any value is accepted (0 is recommended) |

## Returns

| Value | Description |
|----|------|
| (none) | The GML wrapper script of this function has no return statement, so the return value is undefined; do not rely on it to determine the outcome |

## Usage

- **Deprecated, calling it has no effect**: the new implementation reads the backbuffer directly from the GPU through a D3D11 Present hook and no longer uses DWM thumbnails.
- **Caveats (unlike other wrappers)**:
  - This wrapper has no `variable_global_exists` check; if the DLL is not loaded (the `__qiumingdll_winsplit_set_dwm_thumbnail_mode` global does not exist), calling it raises a script error, so check it yourself first;
  - The wrapper references the variable name `enable` instead of `argument0` and does not use the usual argument passing, so compatibility is limited;
  - On non-Windows platforms there is no return value either (it does not return 0).
- Global setting with no splitId parameter.
- The API is kept only for compatibility with legacy callers; new code should not call this function.

## Example

```gml
// Legacy-code migration example: check that the global exists before calling to avoid a script error
if (variable_global_exists("__qiumingdll_winsplit_set_dwm_thumbnail_mode"))
{
    qiumingdll_winsplit_set_dwm_thumbnail_mode(0);  // no effect in the new implementation; can safely be deleted
}
```

## Related functions

- [qiumingdll_winsplit_set_capture_mode](qiumingdll_winsplit_set_capture_mode.md)
- [qiumingdll_winsplit_set_render_interval](qiumingdll_winsplit_set_render_interval.md)
- [qiumingdll_winsplit_set_stretch_mode](qiumingdll_winsplit_set_stretch_mode.md)
