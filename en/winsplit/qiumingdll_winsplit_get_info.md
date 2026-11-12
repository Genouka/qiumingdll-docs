# qiumingdll_winsplit_get_info(splitId, infoType)

Query the running state of the specified split window: window position, client area size, source region values. Only one item can be queried per call, selected by infoType.

## Signature

```gml
qiumingdll_winsplit_get_info(splitId, infoType)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window ID, value 1 ~ 16, must exist |
| infoType | Real | yes | Item to query, value 0 ~ 7, meaning see the table below |

infoType values:

| infoType | Meaning | Coordinate system/unit |
|----------|------|------------|
| 0 | Window top-left X | Screen pixel coordinates |
| 1 | Window top-left Y | Screen pixel coordinates |
| 2 | Client area width | Pixels |
| 3 | Client area height | Pixels |
| 4 | Source region srcX | Original game window client area pixels |
| 5 | Source region srcY | Original game window client area pixels |
| 6 | Source region srcW | Pixels |
| 7 | Source region srcH | Pixels |

## Returns

| Value | Description |
|----|------|
| ≥ 0 | Query result; its meaning depends on infoType (window coordinates, size or source region values) |
| -1 | Query failed: splitId is invalid/does not exist, or infoType is outside 0~7; on non-Windows platforms the wrapper returns -1 directly |

## Usage

- Precondition: `qiumingdll_winsplit_init()` has been called successfully, and the split window for splitId exists.
- 0/1 read the real-time screen coordinates of the window frame's top-left corner (including the title bar); after the user drags the window, the values read match the new position.
- 2/3 read the actual size of the client area (the image display area), corresponding to the w/h passed to set_size/set_region.
- 4~7 read the internally recorded source region values, consistent with the most recent create or set_source_region setting.
- If you only need to check whether a window exists, `qiumingdll_winsplit_exists` is more direct.

## Example

```gml
// In the controller object's Step event: press F1 to print all state of split window 1
if (keyboard_check_pressed(vk_f1))
{
    var _x  = qiumingdll_winsplit_get_info(global.split_1, 0);
    var _y  = qiumingdll_winsplit_get_info(global.split_1, 1);
    var _w  = qiumingdll_winsplit_get_info(global.split_1, 2);
    var _h  = qiumingdll_winsplit_get_info(global.split_1, 3);
    var _sx = qiumingdll_winsplit_get_info(global.split_1, 4);
    var _sy = qiumingdll_winsplit_get_info(global.split_1, 5);
    var _sw = qiumingdll_winsplit_get_info(global.split_1, 6);
    var _sh = qiumingdll_winsplit_get_info(global.split_1, 7);

    show_debug_message("Window position: (" + string(_x) + ", " + string(_y) + ")");
    show_debug_message("Client area size: " + string(_w) + " x " + string(_h));
    show_debug_message("Source region: (" + string(_sx) + ", " + string(_sy) + ") " + string(_sw) + " x " + string(_sh));
}
```

## Related functions

- [qiumingdll_winsplit_exists](qiumingdll_winsplit_exists.md)
- [qiumingdll_winsplit_get_count](qiumingdll_winsplit_get_count.md)
- [qiumingdll_winsplit_set_position](qiumingdll_winsplit_set_position.md)
- [qiumingdll_winsplit_set_source_region](qiumingdll_winsplit_set_source_region.md)
