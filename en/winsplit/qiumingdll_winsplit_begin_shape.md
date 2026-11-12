# qiumingdll_winsplit_begin_shape(splitId)

Start recording a custom polygon shape for the specified split window: clear that window's shape point buffer, then add points one by one with add_shape_point and generate the shape with end_shape.

## Signature

```gml
qiumingdll_winsplit_begin_shape(splitId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window ID, value 1 ~ 16, must exist |

## Returns

| Value | Description |
|----|------|
| 1 | Successfully entered shape recording state |
| 0 | Failure: splitId is invalid or does not exist; on non-Windows platforms the wrapper returns 0 directly |

## Usage

- Precondition: `qiumingdll_winsplit_init()` has been called successfully, and the split window for splitId exists.
- Must be used as a group with `qiumingdll_winsplit_add_shape_point` and `qiumingdll_winsplit_end_shape`; all three must use the same splitId.
- The shape point buffer is shared at module level: only one window's shape can be recorded at a time. After begin on one window and before end, do not begin another window (doing so invalidates the former recording).
- This only starts recording and does not change the window's appearance; the actual shape takes effect only at `qiumingdll_winsplit_end_shape`.
- To abandon midway, simply stop calling any shape functions (the next begin clears the old point buffer automatically).

## Example

```gml
// In the Step event of a controller object: press P to start recording an "east-west-north-south diamond" polygon shape
if (keyboard_check_pressed(ord("P")))
{
    // Start recording shape points for split window 1
    qiumingdll_winsplit_begin_shape(global.split_1);
    // ...then call add_shape_point in order to add at least 3 points...
}
```

## Related functions

- [qiumingdll_winsplit_add_shape_point](qiumingdll_winsplit_add_shape_point.md)
- [qiumingdll_winsplit_end_shape](qiumingdll_winsplit_end_shape.md)
- [qiumingdll_winsplit_clear_shape](qiumingdll_winsplit_clear_shape.md)
- [qiumingdll_winsplit_set_shape_ellipse](qiumingdll_winsplit_set_shape_ellipse.md)
