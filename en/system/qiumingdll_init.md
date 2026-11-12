# qiumingdll_init()

Initializes the qiumingdll extension: loads the DLL on Windows and binds all external functions. This is the prerequisite for every other qiumingdll function.

## Signature

```gml
qiumingdll_init()
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

- Prerequisite: none. This function must be called first, however, before any other `qiumingdll_*` function can be called safely.
- Platform limit: Windows only (`os_type == os_windows`); on other platforms it returns immediately and does nothing.
- Behavior: during initialization it defines the global variable `__qiumingdll_initialized` (set to `true`) and uses `external_define` to bind all functions in the DLL, storing the results in the `global.__qiumingdll_*` global variables. The DLL is loaded lazily: the actual load happens on the first call to a bound function.
- Repeated calls: this function is idempotent. If it has already been initialized (the global variable `__qiumingdll_initialized` exists), repeated calls skip automatically — nothing is bound twice and no error is raised.
- Note: after `qiumingdll_free()` the effect of this function is undone (`__qiumingdll_initialized` is set back to `false`); at that point all other functions fail or return default values, and this function must be called again to restore them.
- It is recommended to call it once as early as possible during the game's first load (e.g. in the `game_start` event or the Create event of a global manager object).

## Example

```gml
// Call in the Create event of the global object at game start
qiumingdll_init();

// Other functions can then be used safely
qiumingdll_fixflash();
var v = qiumingdll_get_version();
show_debug_message("qiumingdll version: " + string(v));

// Repeated calls have no side effects
qiumingdll_init();
```

## Related functions

- [qiumingdll_free](qiumingdll_free.md)
- [qiumingdll_get_version](qiumingdll_get_version.md)
- [qiumingdll_fixflash](qiumingdll_fixflash.md)
