# winself Module

Appearance control for the game's own window: overall opacity adjustment (layered window) plus irregular-window shape clipping (SetWindowRgn). It acts on the game main window itself (the functions obtain `window_handle()` internally), unlike winsplit's split-screen child windows.

8 functions in total.

## Function index

| Function | Description |
|------|------|
| [qiumingdll_winself_set_opacity](qiumingdll_winself_set_opacity.md) | Set the overall opacity of the game's own window (0 = fully transparent, 255 = fully opaque). |
| [qiumingdll_winself_begin_shape](qiumingdll_winself_begin_shape.md) | Start recording a custom polygon shape for the game window (begin → add_shape_point*N → end). |
| [qiumingdll_winself_add_shape_point](qiumingdll_winself_add_shape_point.md) | Add one vertex to the polygon while a shape is being recorded (client-area coordinates). |
| [qiumingdll_winself_end_shape](qiumingdll_winself_end_shape.md) | Finish shape recording and apply the collected polygon vertices to the game window. |
| [qiumingdll_winself_set_shape_ellipse](qiumingdll_winself_set_shape_ellipse.md) | Clip the game window to an ellipse inscribed in the client area. |
| [qiumingdll_winself_set_shape_roundrect](qiumingdll_winself_set_shape_roundrect.md) | Clip the game window to a rounded rectangle (each corner cut with the specified corner radius). |
| [qiumingdll_winself_set_shape_from_bitmap](qiumingdll_winself_set_shape_from_bitmap.md) | Use a BMP bitmap as the shape template: pixels matching transColor become holes, all others are kept. |
| [qiumingdll_winself_clear_shape](qiumingdll_winself_clear_shape.md) | Clear the game window's shape region and restore the full rectangle. |

[Back to documentation home](../README.md)
