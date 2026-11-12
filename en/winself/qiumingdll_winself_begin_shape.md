# qiumingdll_winself_begin_shape()

Start recording a custom polygon shape for the game's own window: clears the shape point buffer, then add vertices one by one with `qiumingdll_winself_add_shape_point` and generate the shape with `qiumingdll_winself_end_shape`.

## Signature

```gml
qiumingdll_winself_begin_shape()
```

> The window handle is taken internally from `window_handle()`; it does not need to be passed explicitly.

## Parameters

No parameters.

## Returns

| Value | Description |
|----|------|
| `1` | Recording started successfully |
| `0` | Failure: invalid window handle; on non-Windows platforms the wrapper returns `0` directly |

## Usage

- Prerequisite: call on Windows with the game window already present. The function automatically uses `window_handle()` as the target window.
- Shape point coordinates use the window's **client area** (client rect) coordinate system, with the origin at the top-left corner of the client area.
- You must call begin → add_shape_point (at least 3 points) → end in that order before the window shape actually changes.
- The vertex order determines the polygon winding direction; it is recommended to add points continuously in clockwise or counter-clockwise order.
- Areas outside the polygon become transparent, and mouse clicks on transparent areas pass through to the desktop.

## Example

```gml
// Create a triangular game window (within client area 0,0 - 800,600)
qiumingdll_winself_begin_shape();
qiumingdll_winself_add_shape_point(400, 0);
qiumingdll_winself_add_shape_point(800, 600);
qiumingdll_winself_add_shape_point(0, 600);
qiumingdll_winself_end_shape();
```

## Related functions

- [qiumingdll_winself_add_shape_point](qiumingdll_winself_add_shape_point.md)
- [qiumingdll_winself_end_shape](qiumingdll_winself_end_shape.md)
- [qiumingdll_winself_clear_shape](qiumingdll_winself_clear_shape.md)
