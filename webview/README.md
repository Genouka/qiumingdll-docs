# webview 模块

基于 WebView2 的内置浏览器窗口：支持独立窗口与子窗口、导航、脚本执行、形状/透明度/置顶等外观控制。

共 37 个函数。

## 函数索引

| 函数 | 说明 |
|------|------|
| [qiumingdll_webview_cleanup](qiumingdll_webview_cleanup.md) | 销毁所有 WebView 窗口并**释放整个 WebView 环境**（包括 WebView2 Environment、加载的 DLL、COM 等全部底层资源）。 |
| [qiumingdll_webview_create](qiumingdll_webview_create.md) | 创建一个独立的浏览器窗口（带系统标题栏，可移动、可关闭），返回该窗口的 webviewId。 |
| [qiumingdll_webview_create_child](qiumingdll_webview_create_child.md) | 在游戏主窗口的客户区内创建一个嵌入式的子窗口浏览器（无标题栏），返回该 WebView 的编号。 |
| [qiumingdll_webview_destroy](qiumingdll_webview_destroy.md) | 销毁指定的 WebView 窗口并释放其内部资源，该编号随即被释放可复用。 |
| [qiumingdll_webview_destroy_all](qiumingdll_webview_destroy_all.md) | 销毁当前存在的**所有** WebView 窗口实例（包括独立窗口和子窗口），并把全部编号释放。 |
| [qiumingdll_webview_end_shape](qiumingdll_webview_end_shape.md) | 结束 WebView 窗口的不规则形状编辑，使之前通过 `qiumingdll_webview_set_region` 设置的形状区域生效。 |
| [qiumingdll_webview_execute_script](qiumingdll_webview_execute_script.md) | 在指定 WebView 当前页面中执行一段 JavaScript 代码。 |
| [qiumingdll_webview_exists](qiumingdll_webview_exists.md) | 查询指定的 webviewId 当前是否对应一个活动的（尚未销毁的）WebView 窗口。 |
| [qiumingdll_webview_get_count](qiumingdll_webview_get_count.md) | 返回当前同时存在的（尚未销毁的）WebView 窗口数量。 |
| [qiumingdll_webview_get_info](qiumingdll_webview_get_info.md) | 按类型查询指定 WebView 的运行时信息（位置、尺寸、就绪状态、窗口类型）。 |
| [qiumingdll_webview_get_is_active](qiumingdll_webview_get_is_active.md) | 查询指定的 WebView 是否已创建并且**内部已就绪**（控制器创建完成，可以执行 navigate / execute_script 等操作）。 |
| [qiumingdll_webview_go_back](qiumingdll_webview_go_back.md) | 让指定 WebView 后退到浏览历史中的上一个页面（相当于浏览器的后退按钮）。 |
| [qiumingdll_webview_go_forward](qiumingdll_webview_go_forward.md) | 让指定 WebView 前进到浏览历史中的下一个页面（相当于浏览器的前进按钮）。 |
| [qiumingdll_webview_hide](qiumingdll_webview_hide.md) | 隐藏指定的 WebView 窗口（页面与脚本状态保留）。 |
| [qiumingdll_webview_init](qiumingdll_webview_init.md) | 初始化 WebView 模块：注册窗口类、加载 WebView2Loader.dll、初始化 COM 并创建 WebView2 环境，是所有 WebView 功能的第一道前置步骤。 |
| [qiumingdll_webview_is_child](qiumingdll_webview_is_child.md) | 查询指定的 WebView 是子窗口（create_child 创建）还是独立窗口（create 创建）。 |
| [qiumingdll_webview_navigate](qiumingdll_webview_navigate.md) | 让指定的 WebView 导航到给定的网址，异步加载网页。 |
| [qiumingdll_webview_navigate_to_string](qiumingdll_webview_navigate_to_string.md) | 用一段 HTML 字符串直接在指定 WebView 中渲染页面（类似 `data:text/html` 的效果），无需网络和本地文件。 |
| [qiumingdll_webview_reload](qiumingdll_webview_reload.md) | 重新加载指定 WebView 当前页面（相当于浏览器的刷新）。 |
| [qiumingdll_webview_resize_to_parent](qiumingdll_webview_resize_to_parent.md) | 让指定的**子窗口**浏览器自动铺满游戏主窗口的整个客户区，并在主窗口尺寸变化时自动跟随。 |
| [qiumingdll_webview_set_closable](qiumingdll_webview_set_closable.md) | 控制指定的 WebView 独立窗口是否允许被用户关闭（通过标题栏关闭按钮 / Alt+F4）。 |
| [qiumingdll_webview_set_close_triggers_main](qiumingdll_webview_set_close_triggers_main.md) | 设置当用户关闭该 WebView 独立窗口时，是否连带关闭游戏主窗口。 |
| [qiumingdll_webview_set_default_context_menus_enabled](qiumingdll_webview_set_default_context_menus_enabled.md) | 开启或关闭指定 WebView 页面的默认右键菜单。 |
| [qiumingdll_webview_set_devtools_enabled](qiumingdll_webview_set_devtools_enabled.md) | 开启或关闭指定 WebView 的开发者工具（F12 DevTools）支持。 |
| [qiumingdll_webview_set_draggable](qiumingdll_webview_set_draggable.md) | 设置指定的 WebView 窗口是否可以通过按住窗口内容区域拖动窗口。 |
| [qiumingdll_webview_set_opacity](qiumingdll_webview_set_opacity.md) | 设置指定 WebView 窗口的整体透明度。 |
| [qiumingdll_webview_set_position](qiumingdll_webview_set_position.md) | 设置指定 WebView 窗口的位置（不改变大小）。 |
| [qiumingdll_webview_set_region](qiumingdll_webview_set_region.md) | 同时设置指定 WebView 窗口的位置和大小。 |
| [qiumingdll_webview_set_script_enabled](qiumingdll_webview_set_script_enabled.md) | 开启或关闭指定 WebView 页面中 JavaScript 的执行能力。 |
| [qiumingdll_webview_set_size](qiumingdll_webview_set_size.md) | 设置指定 WebView 窗口的客户区大小（不改变位置）。 |
| [qiumingdll_webview_set_statusbar_enabled](qiumingdll_webview_set_statusbar_enabled.md) | 开启或关闭指定 WebView 页面底部的状态栏（显示链接地址、加载进度等）。 |
| [qiumingdll_webview_set_title](qiumingdll_webview_set_title.md) | 设置指定 WebView 窗口标题栏中显示的文本。 |
| [qiumingdll_webview_set_titlebar](qiumingdll_webview_set_titlebar.md) | 切换指定 WebView 窗口是否带有系统标题栏（用于独立窗口的"无边框"模式）。 |
| [qiumingdll_webview_set_topmost](qiumingdll_webview_set_topmost.md) | 设置指定 WebView **独立窗口**是否置顶（保持在所有窗口之上）。 |
| [qiumingdll_webview_set_zoom_factor](qiumingdll_webview_set_zoom_factor.md) | 设置指定 WebView 页面的缩放比例（Zoom）。 |
| [qiumingdll_webview_show](qiumingdll_webview_show.md) | 显示指定的 WebView 窗口（取消隐藏状态）。 |
| [qiumingdll_webview_stop](qiumingdll_webview_stop.md) | 停止指定 WebView 当前正在进行的页面加载。 |

[返回文档首页](../README.md)