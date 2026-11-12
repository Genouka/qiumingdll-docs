# qiumingdll_free()

Releases the qiumingdll extension: unloads the DLL and undoes the initialization state, making all other qiumingdll functions unusable.

## Signature

```gml
qiumingdll_free()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| no return value | This function returns nothing |

## Usage

- Prerequisite: it is recommended to have called `qiumingdll_init()` first; if it was never initialized, this function still skips automatically on Windows because the global variable does not exist, and does not raise an error.
- Platform limit: Windows only (`os_type == os_windows`); calling it on other platforms does nothing.
- Behavior: on Windows it calls `external_free("qiumingdll.dll")` to unload the DLL and sets the global variable `__qiumingdll_initialized` back to `false`, i.e. returns to the uninitialized state.
- Note: after releasing, all other `qiumingdll_*` functions stop working — some do not execute because they cannot find the bound variables, and some return default values (for example, the version number returns 0). `qiumingdll_init()` must be called again before they can be used.
- Use cases: cleaning up when the game exits, hot-reloading the DLL, or releasing resources when the extension is no longer needed mid-run. Usually the game only needs to init once for its whole lifetime, so this function is not needed.
- Unlike the idempotent `qiumingdll_init()`, this function completes the release on the first call; subsequent calls (without re-initializing) skip automatically.

## Example

```gml
// Release the extension when the game exits
qiumingdll_init();
qiumingdll_fixflash();

// When it needs to be released...
qiumingdll_free();

// Other functions no longer work after release (this returns 0)
var v = qiumingdll_get_version();
show_debug_message("Version after release: " + string(v));

// To use it again, it must be re-initialized first
qiumingdll_init();
```

## Related functions

- [qiumingdll_init](qiumingdll_init.md)
- [qiumingdll_get_version](qiumingdll_get_version.md)
