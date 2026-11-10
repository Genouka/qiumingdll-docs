# winself 模块

游戏自身窗口外观控制：整体透明度调整（分层窗口），以及异型窗口（SetWindowRgn）的形状裁剪。作用于游戏主窗口本身（函数内部自动取 `window_handle()`），区别于 winsplit 的分屏子窗口。

共 8 个函数。

## 函数索引

| 函数 | 说明 |
|------|------|
| [qiumingdll_winself_set_opacity](qiumingdll_winself_set_opacity.md) | 设置游戏自身窗口的整体透明度（0 = 完全透明，255 = 完全不透明）。 |
| [qiumingdll_winself_begin_shape](qiumingdll_winself_begin_shape.md) | 开始为游戏窗口录制自定义多边形形状（begin → add_shape_point*N → end）。 |
| [qiumingdll_winself_add_shape_point](qiumingdll_winself_add_shape_point.md) | 在形状录制过程中向多边形添加一个顶点（客户区坐标）。 |
| [qiumingdll_winself_end_shape](qiumingdll_winself_end_shape.md) | 结束形状录制并把收集的多边形顶点应用到游戏窗口。 |
| [qiumingdll_winself_set_shape_ellipse](qiumingdll_winself_set_shape_ellipse.md) | 把游戏窗口裁成内切于客户区的椭圆形。 |
| [qiumingdll_winself_set_shape_roundrect](qiumingdll_winself_set_shape_roundrect.md) | 把游戏窗口裁成圆角矩形（四角按指定圆角半径裁掉）。 |
| [qiumingdll_winself_set_shape_from_bitmap](qiumingdll_winself_set_shape_from_bitmap.md) | 用一张 BMP 位图作为形状模板：与 transColor 同色的像素成洞，其余保留。 |
| [qiumingdll_winself_clear_shape](qiumingdll_winself_clear_shape.md) | 清除游戏窗口的形状区域，恢复为完整矩形。 |



[返回文档首页](../README.md)
