# qiumingdll_winsplit_create(srcX, srcY, srcW, srcH, dstX, dstY, dstW, dstH)

Create a split window: display a specified pixel region (source region) of the original game window's client area in real time in a new top-level window, and return the split window's ID.

## Signature

```gml
qiumingdll_winsplit_create(srcX, srcY, srcW, srcH, dstX, dstY, dstW, dstH)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| srcX | Real | yes | X of the source region's top-left corner, in pixels, relative to the original game window's client area (the client area's top-left corner is 0,0), value 0 ~ client area width |
| srcY | Real | yes | Y of the source region's top-left corner, in pixels, relative to the original game window's client area, value 0 ~ client area height |
| srcW | Real | yes | Source region width, in pixels, must be greater than 0; recommended not to exceed the right edge of the original client area |
| srcH | Real | yes | Source region height, in pixels, must be greater than 0; recommended not to exceed the bottom edge of the original client area |
| dstX | Real | yes | X of the split window's top-left corner on screen, in pixels, screen coordinates (the primary monitor's top-left corner is 0,0) |
| dstY | Real | yes | Y of the split window's top-left corner on screen, in pixels, screen coordinates |
| dstW | Real | yes | Split window client area width, in pixels (excluding the title bar and other borders; borders extend outward additionally) |
| dstH | Real | yes | Split window client area height, in pixels (excluding the title bar and other borders) |

The source region (srcX/srcY/srcW/srcH) lies within the original game window's client area and determines "what is displayed"; the destination region (dstX/dstY/dstW/dstH) is on screen and determines "where it is displayed and how large". Source content is stretched to the destination size.

## Returns

| Value | Description |
|----|------|
| 1 ~ 16 | Creation succeeded; returns the split window's ID (splitId), used as a parameter by all subsequent operations |
| 0 | Creation failed: module not initialized, window slots full (at most 16 at a time), or system window creation failed; on non-Windows platforms the wrapper returns 0 directly |

## Usage

- Precondition: `qiumingdll_winsplit_init()` must have been called successfully (returned 0).
- splitIds start at 1, not 0; at most 16 split windows can exist at the same time. Destroyed slots are reused automatically by later creations, so IDs are not guaranteed to increase consecutively.
- Created visible; no need to call show.
- Default properties at creation: draggable `draggable=false`, has title bar `hasTitleBar=true`, closable `closable=true`, closing also closes the main window `closeTriggersMain=true`. All can be changed with the corresponding set functions.
- srcW/srcH may overlap the source region (multiple split windows can display the same region).
- If the source region exceeds the original window's client area, the exceeding part has no image content and the split window shows blank/black.
- After hiding the original window the split windows still render normally; the two do not affect each other.

## Example

```gml
// In the controller object's Create event: divide the main window's client area into four equal parts, each displayed independently
if (global.winsplit_ready == true)
{
    var _cw = window_get_width();   // Main window client area width
    var _ch = window_get_height();  // Main window client area height
    var _hw = _cw div 2;
    var _hh = _ch div 2;

    // Top-left part: displayed above-right of the main window
    global.split_1 = qiumingdll_winsplit_create(0, 0, _hw, _hh, _cw + 20, 50, _hw, _hh);
    // Top-right part: displayed below-right of the main window
    global.split_2 = qiumingdll_winsplit_create(_hw, 0, _cw - _hw, _hh, _cw + 20, 50 + _hh + 30, _hw, _hh);
    // Bottom-left part: displayed on the secondary monitor (if present)
    global.split_3 = qiumingdll_winsplit_create(0, _hh, _hw, _ch - _hh, 0, 0, _hw, _hh);

    if (global.split_1 == 0)
        show_debug_message("Failed to create split window: slots may be full or the module is not initialized");
}
```

## Related functions

- [qiumingdll_winsplit_init](qiumingdll_winsplit_init.md)
- [qiumingdll_winsplit_destroy](qiumingdll_winsplit_destroy.md)
- [qiumingdll_winsplit_destroy_all](qiumingdll_winsplit_destroy_all.md)
- [qiumingdll_winsplit_set_source_region](qiumingdll_winsplit_set_source_region.md)
- [qiumingdll_winsplit_set_region](qiumingdll_winsplit_set_region.md)
- [qiumingdll_winsplit_hide_original](qiumingdll_winsplit_hide_original.md)
