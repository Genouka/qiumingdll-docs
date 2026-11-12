# qiumingdll_winself_add_shape_point(x, y)

Between `qiumingdll_winself_begin_shape` and `qiumingdll_winself_end_shape`, add one vertex to the polygon shape currently being recorded.

## Signature

```gml
qiumingdll_winself_add_shape_point(x, y)
```

> The window handle is taken internally from `window_handle()`; it does not need to be passed explicitly.

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| x | real | yes | Vertex X coordinate (window client-area coordinate system) |
| y | real | yes | Vertex Y coordinate (window client-area coordinate system) |

## Returns

| Value | Description |
|----|------|
| `1` | Vertex added successfully |
| `0` | Failure: invalid window handle, `begin_shape` not called yet, or the vertex limit (256) has been reached; on non-Windows platforms the wrapper returns `0` directly |

## Usage

- Prerequisite: `qiumingdll_winself_begin_shape` must already have been called on the game window.
- Coordinates are based on the window client area (client rect) coordinate system; the origin is the top-left corner of the client area.
- At least 3 vertices are required; the polygon takes effect only after `qiumingdll_winself_end_shape` is called.
- A single recording holds at most 256 vertices.

## Example

```gml
// Add one vertex between begin and end
qiumingdll_winself_add_shape_point(400, 300);
```

## Related functions

- [qiumingdll_winself_begin_shape](qiumingdll_winself_begin_shape.md)
- [qiumingdll_winself_end_shape](qiumingdll_winself_end_shape.md)
