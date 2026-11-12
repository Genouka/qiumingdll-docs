# qiumingdll_wineffect_stop()

Immediately stops window effects, zeroes the shake/distortion/tear strengths, and restores the window position and original region.

## Signature

```gml
qiumingdll_wineffect_stop()
```

## Parameters

None.

## Returns

| Value | Description |
|----|------|
| 1 | Stopped and restored |

## Usage

- Difference from `set_enabled(0)`: this function also zeroes all three strengths, suitable for "ending the sequence for good".
- The window binding is retained after stopping; you can set strengths again and call `set_enabled(1)` once more.
- If the module has not been initialized, calling this function is still safe (it returns 1 directly).

## Example

```gml
/// Force-stop all window effects
qiumingdll_wineffect_stop();
```

## Related functions

- [qiumingdll_wineffect_set_enabled](qiumingdll_wineffect_set_enabled.md)
- [qiumingdll_wineffect_cleanup](qiumingdll_wineffect_cleanup.md)
- [qiumingdll_wineffect_get_state](qiumingdll_wineffect_get_state.md)
