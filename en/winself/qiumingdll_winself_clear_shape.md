# qiumingdll_winself_clear_shape()

Clear the shape region of the game's own window and restore the full rectangle (the whole client area is displayed).

## Signature

```gml
qiumingdll_winself_clear_shape()
```

> The window handle is taken internally from `window_handle()`; it does not need to be passed explicitly.

## Parameters

No parameters.

## Returns

| Value | Description |
|----|------|
| `1` | Cleared successfully (already restored to the full rectangle) |
| `0` | Failure: invalid window handle; on non-Windows platforms the wrapper returns `0` directly |

## Usage

- Prerequisite: call on Windows with the game window already present. The function automatically uses `window_handle()` as the target window.
- After the call the window returns to a normal rectangular window; any irregular shape previously set through ellipse / roundrect / polygon / bitmap is removed.
- Does not conflict with the opacity API: clearing the shape does not affect the opacity already set on the window.

## Example

```gml
// Restore the game window to a rectangle
qiumingdll_winself_clear_shape();
```

## Related functions

- [qiumingdll_winself_set_shape_ellipse](qiumingdll_winself_set_shape_ellipse.md)
- [qiumingdll_winself_set_shape_roundrect](qiumingdll_winself_set_shape_roundrect.md)
- [qiumingdll_winself_begin_shape](qiumingdll_winself_begin_shape.md)
