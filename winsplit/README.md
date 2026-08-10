# winsplit 模块

多窗口分屏显示：将一个窗口的内容同时呈现在多个屏幕上，支持形状裁剪、源区域缩放、批量动画控制。

共 61 个函数。

## 函数索引

| 函数 | 说明 |
|------|------|
| [qiumingdll_winsplit_add_path_point](qiumingdll_winsplit_add_path_point.md) | 向指定分裂窗口的路径列表累积添加一个路径点（屏幕坐标），路径点随后可通过 move_path / move_path_animate 使用。 |
| [qiumingdll_winsplit_add_shape_point](qiumingdll_winsplit_add_shape_point.md) | 在 begin_shape 与 end_shape 之间，向当前正在录制的多边形形状添加一个顶点。 |
| [qiumingdll_winsplit_batch_add_position](qiumingdll_winsplit_batch_add_position.md) | 在批处理录制中添加一条"位置移动"命令：播放时窗口在 durationMs 毫秒内从当前插值移动到目标位置 (x, y)。 |
| [qiumingdll_winsplit_batch_add_region](qiumingdll_winsplit_batch_add_region.md) | 在批处理录制中添加一条"区域变换"命令：播放时窗口在 durationMs 毫秒内同时移动到目标位置并缩放到目标尺寸（源区域按当时的源动画模式联动）。 |
| [qiumingdll_winsplit_batch_add_size](qiumingdll_winsplit_batch_add_size.md) | 在批处理录制中添加一条"尺寸缩放"命令：播放时窗口在 durationMs 毫秒内从当前尺寸缩放到目标尺寸 (w, h)（源区域按当时的源动画模式联动）。 |
| [qiumingdll_winsplit_batch_add_src_region](qiumingdll_winsplit_batch_add_src_region.md) | 在批处理录制中添加一条"源区域变换"命令：播放时在 durationMs 毫秒内把源区域（主窗口上截取的图像区域）从当前值插值到目标区域。 |
| [qiumingdll_winsplit_batch_add_wait](qiumingdll_winsplit_batch_add_wait.md) | 在批处理录制中添加一条"原地等待"命令：播放时窗口在 durationMs 毫秒内保持当前状态不变，之后继续执行下一条命令。 |
| [qiumingdll_winsplit_batch_begin](qiumingdll_winsplit_batch_begin.md) | 开始录制指定分裂窗口的批处理动画序列；之后的 batch_add_* 命令将以此为基础按顺序累积。 |
| [qiumingdll_winsplit_batch_clear](qiumingdll_winsplit_batch_clear.md) | 停止指定分裂窗口正在播放的批处理，并清空其所有已录制的命令，解除录制状态。 |
| [qiumingdll_winsplit_batch_end](qiumingdll_winsplit_batch_end.md) | 结束指定分裂窗口的批处理录制状态，之后才能调用 batch_play / batch_play_frame_sync 播放。 |
| [qiumingdll_winsplit_batch_is_playing](qiumingdll_winsplit_batch_is_playing.md) | 查询指定分裂窗口当前是否正在播放批处理动画（定时器模式与帧同步模式均计入）。 |
| [qiumingdll_winsplit_batch_play](qiumingdll_winsplit_batch_play.md) | 播放指定分裂窗口已录制好的批处理动画序列；由内部 16ms 定时器驱动，与游戏帧率无关。 |
| [qiumingdll_winsplit_batch_play_frame_sync](qiumingdll_winsplit_batch_play_frame_sync.md) | 以"帧同步"方式播放指定分裂窗口的批处理动画：不创建内部定时器，必须由调用方每帧调用 batch_step 推进，进度与游戏帧率完全一致。 |
| [qiumingdll_winsplit_batch_set_easing](qiumingdll_winsplit_batch_set_easing.md) | 设置指定分裂窗口批处理录制中后续命令（batch_add_*）所使用的缓动曲线。 |
| [qiumingdll_winsplit_batch_set_src_anim_mode](qiumingdll_winsplit_batch_set_src_anim_mode.md) | 设置指定分裂窗口批处理录制中后续尺寸类命令（batch_add_size / batch_add_region）所使用的源动画模式。 |
| [qiumingdll_winsplit_batch_step](qiumingdll_winsplit_batch_step.md) | 推进指定分裂窗口的"帧同步"批处理动画一帧（仅对 batch_play_frame_sync 启动的播放有效），并返回播放是否仍在进行。 |
| [qiumingdll_winsplit_batch_stop](qiumingdll_winsplit_batch_stop.md) | 中途停止指定分裂窗口正在播放的批处理动画，窗口停留在被停止时的状态。 |
| [qiumingdll_winsplit_begin_shape](qiumingdll_winsplit_begin_shape.md) | 开始为指定的分裂窗口录制自定义多边形形状：清空该窗口的形状点缓冲，后续用 add_shape_point 依次添点、用 end_shape 生成形状。 |
| [qiumingdll_winsplit_cleanup](qiumingdll_winsplit_cleanup.md) | 整体清理窗口分裂模块：销毁所有分裂窗口、恢复原游戏窗口显示、卸载捕获与消息钩子。用于游戏退出或彻底停用分裂功能。 |
| [qiumingdll_winsplit_clear_path](qiumingdll_winsplit_clear_path.md) | 停止指定分裂窗口正在播放的动画，并清空其所有已添加的路径点。 |
| [qiumingdll_winsplit_clear_shape](qiumingdll_winsplit_clear_shape.md) | 清除指定分裂窗口的形状区域，恢复为完整矩形（显示整个客户区画面）。 |
| [qiumingdll_winsplit_create](qiumingdll_winsplit_create.md) | 创建一个分裂窗口：把原游戏窗口客户区内指定的一块像素区域（源区域）实时显示在一个新的顶层窗口中，并返回该分裂窗口的 ID。 |
| [qiumingdll_winsplit_destroy](qiumingdll_winsplit_destroy.md) | 销毁指定的分裂窗口：关闭窗口、释放其占用的槽位和形状资源，窗口 ID 随后可被新建的分裂窗口复用。 |
| [qiumingdll_winsplit_destroy_all](qiumingdll_winsplit_destroy_all.md) | 一次性销毁当前存在的所有分裂窗口，常用于场景切换、返回标题画面等需要"清屏"的场合。 |
| [qiumingdll_winsplit_end_shape](qiumingdll_winsplit_end_shape.md) | 结束形状录制并把已收集的多边形顶点应用到分裂窗口：窗口立即变为该多边形的形状，多边形之外的区域不再显示。 |
| [qiumingdll_winsplit_exists](qiumingdll_winsplit_exists.md) | 判断指定的分裂窗口 ID 是否有效（是否已创建且尚未销毁）。 |
| [qiumingdll_winsplit_get_count](qiumingdll_winsplit_get_count.md) | 返回当前存在的分裂窗口总数（0 ~ 16），用于槽位管理、UI 显示等。 |
| [qiumingdll_winsplit_get_info](qiumingdll_winsplit_get_info.md) | 查询指定分裂窗口的运行状态：窗口位置、客户区尺寸、源区域数值。一次只能查询一项，由 infoType 指定。 |
| [qiumingdll_winsplit_hide](qiumingdll_winsplit_hide.md) | 隐藏指定的分裂窗口，不影响其内部状态；之后可以随时用 show 重新显示。 |
| [qiumingdll_winsplit_hide_original](qiumingdll_winsplit_hide_original.md) | 隐藏原游戏窗口（保留分裂窗口继续显示画面），用于"只让分裂窗口显示、主窗口不露脸"的典型窗口分裂用法。 |
| [qiumingdll_winsplit_init](qiumingdll_winsplit_init.md) | 初始化窗口分裂模块：记录当前游戏窗口、注册分裂窗口类并安装画面捕获钩子，是所有窗口分裂功能的前置条件。 |
| [qiumingdll_winsplit_is_animating](qiumingdll_winsplit_is_animating.md) | 查询指定分裂窗口当前是否正在播放普通动画（位置/尺寸/区域/路径动画）。 |
| [qiumingdll_winsplit_move_path](qiumingdll_winsplit_move_path.md) | 不带动画，将指定分裂窗口立即移动到当前路径的最后一个路径点，并清空路径点列表。 |
| [qiumingdll_winsplit_move_path_animate](qiumingdll_winsplit_move_path_animate.md) | 让指定分裂窗口沿已录制的路径逐段平滑移动，动画结束后停留在路径的最后一个点。 |
| [qiumingdll_winsplit_set_capture_mode](qiumingdll_winsplit_set_capture_mode.md) | 设置分裂窗口的捕获方式。**已弃用**：新方案总是从 GPU 直接读取 backbuffer，调用本函数不会产生任何效果（返回值固定为 1）。 |
| [qiumingdll_winsplit_set_closable](qiumingdll_winsplit_set_closable.md) | 设置指定分裂窗口是否允许被用户关闭（通过标题栏的 X 按钮或系统菜单的"关闭"）。 |
| [qiumingdll_winsplit_set_close_triggers_main](qiumingdll_winsplit_set_close_triggers_main.md) | 设置当用户关闭该分裂窗口时，是否连带关闭原游戏主窗口（联动关闭）。 |
| [qiumingdll_winsplit_set_draggable](qiumingdll_winsplit_set_draggable.md) | 设置指定分裂窗口是否允许被鼠标拖动移动位置。开启后用户可直接用鼠标拖动窗口。 |
| [qiumingdll_winsplit_set_dwm_thumbnail_mode](qiumingdll_winsplit_set_dwm_thumbnail_mode.md) | 启用/禁用 DWM 缩略图作为分裂窗口内容来源。**已弃用**：新方案使用 GPU Hook 捕获 backbuffer，调用本函数不会产生任何效果。 |
| [qiumingdll_winsplit_set_easing_curve](qiumingdll_winsplit_set_easing_curve.md) | 设置指定分裂窗口的缓动曲线，该曲线将应用于该窗口后续所有普通动画（位置/尺寸/区域/路径动画）。 |
| [qiumingdll_winsplit_set_opacity](qiumingdll_winsplit_set_opacity.md) | 设置指定分裂窗口的整体透明度（0 = 完全透明，255 = 完全不透明）。越界值会被自动钳制。 |
| [qiumingdll_winsplit_set_position](qiumingdll_winsplit_set_position.md) | 移动指定的分裂窗口到屏幕上的新位置：只改变位置，不改变大小、源区域和其他属性。 |
| [qiumingdll_winsplit_set_position_animate](qiumingdll_winsplit_set_position_animate.md) | 将分裂窗口从当前位置平滑移动到指定屏幕坐标，动画由内部定时器驱动，结束后停留在目标位置。 |
| [qiumingdll_winsplit_set_region](qiumingdll_winsplit_set_region.md) | 一次性设置指定分裂窗口的位置和尺寸（合并 set_position 与 set_size 的操作）。 |
| [qiumingdll_winsplit_set_region_animate](qiumingdll_winsplit_set_region_animate.md) | 将分裂窗口从当前位置与尺寸平滑移动到目标位置与尺寸（位置+尺寸组合动画），动画结束后停留在目标状态。 |
| [qiumingdll_winsplit_set_render_during_drag](qiumingdll_winsplit_set_render_during_drag.md) | 设置拖拽分裂窗口的过程中是否持续渲染窗口内容（全局设置，默认开启）。 |
| [qiumingdll_winsplit_set_render_interval](qiumingdll_winsplit_set_render_interval.md) | 设置分裂窗口的渲染刷新间隔。**已弃用**：新方案每帧随游戏 Present 同步渲染，本函数不再限制任何渲染频率（调用无任何效果，返回值固定为 1）。 |
| [qiumingdll_winsplit_set_shape_ellipse](qiumingdll_winsplit_set_shape_ellipse.md) | 把指定的分裂窗口设置为椭圆形（内切于其客户区的椭圆），窗口四角变透明，适合做成圆形小地图、圆形头像窗等。 |
| [qiumingdll_winsplit_set_shape_from_bitmap](qiumingdll_winsplit_set_shape_from_bitmap.md) | 用一张位图（BMP）作为分裂窗口的形状模板：图中颜色等于 transColor 的像素在窗口上变透明（成洞），其余像素保留显示。 |
| [qiumingdll_winsplit_set_shape_roundrect](qiumingdll_winsplit_set_shape_roundrect.md) | 把指定的分裂窗口设置为圆角矩形形状（四个角按指定圆角半径裁掉），是"无边框圆角面板"的常用形状。 |
| [qiumingdll_winsplit_set_size](qiumingdll_winsplit_set_size.md) | 改变指定分裂窗口的显示尺寸：只改变大小，不改变位置、源区域和其他属性。 |
| [qiumingdll_winsplit_set_size_animate](qiumingdll_winsplit_set_size_animate.md) | 将分裂窗口从当前尺寸平滑缩放到指定尺寸，源区域可按源动画模式联动，动画结束后停留在目标尺寸。 |
| [qiumingdll_winsplit_set_source_region](qiumingdll_winsplit_set_source_region.md) | 修改指定分裂窗口的源区域，即分裂窗口从原游戏窗口客户区中截取的画面范围（"显示哪一块"）。 |
| [qiumingdll_winsplit_set_src_anim_mode](qiumingdll_winsplit_set_src_anim_mode.md) | 设置指定分裂窗口在尺寸/区域动画期间源区域（主窗口上的截图区域）的联动方式：保持不变、等比拉伸或按锚点裁剪。 |
| [qiumingdll_winsplit_set_stretch_mode](qiumingdll_winsplit_set_stretch_mode.md) | 设置分裂窗口画面与窗口尺寸不一致时的 GDI 拉伸模式（仅影响缩放渲染时的画质，全局设置）。 |
| [qiumingdll_winsplit_set_title](qiumingdll_winsplit_set_title.md) | 设置指定分裂窗口标题栏上显示的标题文字（仅在有标题栏时可见）。 |
| [qiumingdll_winsplit_set_titlebar](qiumingdll_winsplit_set_titlebar.md) | 设置指定分裂窗口是否有标题栏（含窗口边框与系统按钮）。切换时窗口客户区尺寸保持不变，外框大小和左上角会相应调整。 |
| [qiumingdll_winsplit_set_topmost](qiumingdll_winsplit_set_topmost.md) | 设置指定分裂窗口是否置顶显示（始终浮在其它窗口之上，包括游戏主窗口和其它程序窗口）。 |
| [qiumingdll_winsplit_show](qiumingdll_winsplit_show.md) | 显示指定的分裂窗口（若之前被隐藏），不激活它、不抢焦点。 |
| [qiumingdll_winsplit_show_original](qiumingdll_winsplit_show_original.md) | 恢复显示被隐藏的原游戏窗口，恢复位置与隐藏前一致；与 hide_original 成对使用。 |
| [qiumingdll_winsplit_stop_animation](qiumingdll_winsplit_stop_animation.md) | 中途停止指定分裂窗口正在播放的普通动画（位置/尺寸/区域/路径动画），窗口停留在被停止时的位置。 |

[返回文档首页](../README.md)