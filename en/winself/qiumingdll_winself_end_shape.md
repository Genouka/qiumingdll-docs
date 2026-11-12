# qiumingdll_winself_end_shape()

Finish shape recording and apply the collected polygon vertices to the game's own window: the window immediately becomes that polygon's shape, and areas outside the polygon are no longer displayed.

## Signature

```gml
qiumingdll_winself_end_shape()
```

> The window handle is taken internally from `window_handle()`; it does not need to be passed explicitly.

## Parameters

No parameters.

## Returns

| Value | Description |
|----|------|
| `1` | Shape applied successfully |
| `0` | Failure: invalid window handle, `begin_shape` not called, or fewer than 3 vertices; on non-Windows platforms the wrapper returns `0` directly |

## Usage

- Prerequisite: `qiumingdll_winself_begin_shape` has already been called on the game window and at least 3 vertices have been added.
- If there are fewer than 3 vertices, the current recording is discarded and no shape change occurs.
- This shape replaces any shape set previously; `qiumingdll_winself_clear_shape` restores the full rectangle.
- The window shape region is based on the window's client-area coordinates and does not update automatically when the window is resized: if you change the window size later, call this function again to refresh the shape.

## Example

```gml
// Finish after begin + several add_shape_point calls
qiumingdll_winself_end_shape();
```

## Related functions

- [qiumingdll_winself_begin_shape](qiumingdll_winself_begin_shape.md)
- [qiumingdll_winself_add_shape_point](qiumingdll_winself_add_shape_point.md)
- [qiumingdll_winself_clear_shape](qiumingdll_winself_clear_shape.md)
