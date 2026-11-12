# qiumingdll_wineffect_cleanup()

Unbinds the window: stops effects, removes the window subclass and timer, restores the window position/region, and frees the saved original region.

## Signature

```gml
qiumingdll_wineffect_cleanup()
```

## Parameters

None.

## Returns

| Value | Description |
|----|------|
| 1 | Cleaned up |

## Usage

- Recommended in the game-end / room-cleanup event, especially before switching windows or reloading the DLL.
- The window remains usable after cleanup; using the module again requires calling `qiumingdll_wineffect_init()` again.
- Repeated calls are safe.
- If the window has already been destroyed, the function still returns safely without accessing an invalid handle.

## Example

```gml
/// Cleanup event
qiumingdll_wineffect_cleanup();
```

## Related functions

- [qiumingdll_wineffect_init](qiumingdll_wineffect_init.md)
- [qiumingdll_wineffect_stop](qiumingdll_wineffect_stop.md)
