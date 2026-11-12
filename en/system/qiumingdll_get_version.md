# qiumingdll_get_version()

Returns the qiumingdll extension version as an integer, which can be used at runtime to determine the extension's capabilities.

## Signature

```gml
qiumingdll_get_version()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 11400 (current version 1.14.0) | Version number as an integer, encoded as `major*10000 + minor*100 + patch`. For example 1.14.0 → 1×10000 + 14×100 + 0 = 11400; 2.3.4 → 20304 |
| 0 | Returned when called on a non-Windows platform, or when the DLL is not initialized (after `qiumingdll_free()`) |

## Usage

- Prerequisite: call `qiumingdll_init()` first on Windows, otherwise the bound external function cannot be found and 0 is returned.
- Platform limit: only Windows returns the real version number; other platforms always return 0.
- Behavior: the version number is computed from a compile-time constant inside the DLL, so it changes with every build of the extension. This function returns the extension's own version, unrelated to the game version.
- Purpose: version compatibility checks — when the game relies on a qiumingdll feature introduced in a particular version, check the version number first and then decide whether to call the related functions.
- Note: calling this function after `qiumingdll_free()` likewise returns 0.

## Example

```gml
// Check the extension version
qiumingdll_init();

var ver = qiumingdll_get_version();
show_debug_message("qiumingdll version code: " + string(ver));

// Decide by version whether a feature is supported (assuming it is available from 2.0.0)
if (ver >= 20000)
{
    // Use capabilities only available in newer versions
}
else
{
    show_message("An older qiumingdll extension was detected, please update");
}
```

## Related functions

- [qiumingdll_init](qiumingdll_init.md)
- [qiumingdll_free](qiumingdll_free.md)
