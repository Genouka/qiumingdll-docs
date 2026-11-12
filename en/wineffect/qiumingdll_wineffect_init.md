# qiumingdll_wineffect_init()

Binds the game window and prepares window effects. It only records the target window; no effect is started.

## Signature

```gml
qiumingdll_wineffect_init()
```

> The window handle is passed in automatically by the wrapper via `window_handle()`; it does not need to be supplied explicitly.

## Parameters

None.

## Returns

| Value | Description |
|----|------|
| 1 | Bound successfully |
| 0 | Failure: invalid window handle (or non-Windows platform) |

## Usage

- Prerequisite: call `qiumingdll_init()` first, and call this after the game window has been created.
- This function only binds; you still need to call `qiumingdll_wineffect_set_enabled(1)` for anything to start running.
- If effects are already enabled and this function is called again with a different window, the old window is stopped and restored first, then the new window is bound; the new window needs `set_enabled(1)` again.
- Re-binding the same window is safe and does not interrupt running effects.
- The module does not modify window styles or create background threads; the animation is driven by the window's own `WM_TIMER`.

## Example

```gml
/// Create event
qiumingdll_init();
qiumingdll_wineffect_init();
```

## Related functions

- [qiumingdll_wineffect_set_enabled](qiumingdll_wineffect_set_enabled.md)
- [qiumingdll_wineffect_cleanup](qiumingdll_wineffect_cleanup.md)
