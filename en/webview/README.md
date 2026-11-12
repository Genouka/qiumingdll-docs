# webview module

WebView2-based built-in browser windows: supports standalone windows and child windows, navigation, script execution, and appearance controls such as shape / opacity / topmost.

41 functions in total.

## Function index

| Function | Description |
|------|------|
| [qiumingdll_webview_cleanup](qiumingdll_webview_cleanup.md) | Destroys all WebView windows and **releases the entire WebView environment** (including the WebView2 Environment, the loaded DLL, COM, and all other underlying resources). |
| [qiumingdll_webview_clear_resize_to_parent](qiumingdll_webview_clear_resize_to_parent.md) | Cancels the auto-fill effect of `resize_to_parent`, keeps the current size, and the window no longer follows main window resizing afterwards. |
| [qiumingdll_webview_clear_auto_resize_9patch](qiumingdll_webview_clear_auto_resize_9patch.md) | Cancels 9-Patch auto-follow, keeps the current geometry, and the window no longer follows main window resizing afterwards. |
| [qiumingdll_webview_create](qiumingdll_webview_create.md) | Creates a standalone browser window (with a system title bar, movable and closable) and returns its webviewId. |
| [qiumingdll_webview_create_child](qiumingdll_webview_create_child.md) | Creates an embedded child-window browser (no title bar) inside the game main window's client area and returns the WebView's id. |
| [qiumingdll_webview_destroy](qiumingdll_webview_destroy.md) | Destroys the specified WebView window and releases its internal resources; the id is immediately freed for reuse. |
| [qiumingdll_webview_destroy_all](qiumingdll_webview_destroy_all.md) | Destroys **all** currently existing WebView window instances (both standalone and child windows) and frees every id. |
| [qiumingdll_webview_end_shape](qiumingdll_webview_end_shape.md) | Ends the irregular-shape editing of the WebView window, applying the shape region previously set via `qiumingdll_webview_set_region`. |
| [qiumingdll_webview_execute_script](qiumingdll_webview_execute_script.md) | Executes a piece of JavaScript code in the specified WebView's current page. |
| [qiumingdll_webview_exists](qiumingdll_webview_exists.md) | Queries whether the given webviewId currently corresponds to an active (not yet destroyed) WebView window. |
| [qiumingdll_webview_get_count](qiumingdll_webview_get_count.md) | Returns the number of WebView windows that currently exist (not yet destroyed). |
| [qiumingdll_webview_get_info](qiumingdll_webview_get_info.md) | Queries runtime information of the specified WebView by type (position, size, ready state, window type). |
| [qiumingdll_webview_get_is_active](qiumingdll_webview_get_is_active.md) | Queries whether the specified WebView has been created and is **internally ready** (controller created; navigate / execute_script etc. can be used). |
| [qiumingdll_webview_go_back](qiumingdll_webview_go_back.md) | Makes the specified WebView go back to the previous page in the browsing history (like the browser's back button). |
| [qiumingdll_webview_go_forward](qiumingdll_webview_go_forward.md) | Makes the specified WebView go forward to the next page in the browsing history (like the browser's forward button). |
| [qiumingdll_webview_hide](qiumingdll_webview_hide.md) | Hides the specified WebView window (page and script state are preserved). |
| [qiumingdll_webview_init](qiumingdll_webview_init.md) | Initializes the WebView module: registers the window class, loads WebView2Loader.dll, initializes COM and creates the WebView2 environment — the first prerequisite step for all WebView functionality. |
| [qiumingdll_webview_is_child](qiumingdll_webview_is_child.md) | Queries whether the specified WebView is a child window (created by create_child) or a standalone window (created by create). |
| [qiumingdll_webview_navigate](qiumingdll_webview_navigate.md) | Makes the specified WebView navigate to the given URL, loading the page asynchronously. |
| [qiumingdll_webview_navigate_to_string](qiumingdll_webview_navigate_to_string.md) | Renders a page in the specified WebView directly from an HTML string (similar to `data:text/html`), without network or local files. |
| [qiumingdll_webview_reload](qiumingdll_webview_reload.md) | Reloads the specified WebView's current page (like the browser's refresh). |
| [qiumingdll_webview_resize_to_parent](qiumingdll_webview_resize_to_parent.md) | Makes the specified **child-window** browser automatically fill the game main window's entire client area and follow main window size changes. |
| [qiumingdll_webview_resize](qiumingdll_webview_resize.md) | Cancels all auto-following and scales to a custom rectangle (position + size) in one call. |
| [qiumingdll_webview_set_closable](qiumingdll_webview_set_closable.md) | Controls whether the specified standalone WebView window may be closed by the user (via the title bar close button / Alt+F4). |
| [qiumingdll_webview_set_auto_resize_9patch](qiumingdll_webview_set_auto_resize_9patch.md) | Uses a 9-Patch grid plus a rectangle-diagonal two-coordinate scheme so a child window automatically follows main window resizing. |
| [qiumingdll_webview_set_close_triggers_main](qiumingdll_webview_set_close_triggers_main.md) | Sets whether closing this standalone WebView window by the user also closes the game main window. |
| [qiumingdll_webview_set_default_context_menus_enabled](qiumingdll_webview_set_default_context_menus_enabled.md) | Enables or disables the default right-click context menu of the specified WebView's page. |
| [qiumingdll_webview_set_devtools_enabled](qiumingdll_webview_set_devtools_enabled.md) | Enables or disables DevTools (F12) support for the specified WebView. |
| [qiumingdll_webview_set_draggable](qiumingdll_webview_set_draggable.md) | Sets whether the specified WebView window can be dragged by holding its content area. |
| [qiumingdll_webview_set_opacity](qiumingdll_webview_set_opacity.md) | Sets the overall opacity of the specified WebView window. |
| [qiumingdll_webview_set_position](qiumingdll_webview_set_position.md) | Sets the position of the specified WebView window (size unchanged). |
| [qiumingdll_webview_set_region](qiumingdll_webview_set_region.md) | Sets both position and size of the specified WebView window. |
| [qiumingdll_webview_set_script_enabled](qiumingdll_webview_set_script_enabled.md) | Enables or disables JavaScript execution in the specified WebView's page. |
| [qiumingdll_webview_set_size](qiumingdll_webview_set_size.md) | Sets the client-area size of the specified WebView window (position unchanged). |
| [qiumingdll_webview_set_statusbar_enabled](qiumingdll_webview_set_statusbar_enabled.md) | Enables or disables the status bar at the bottom of the specified WebView's page (showing link targets, load progress, etc.). |
| [qiumingdll_webview_set_title](qiumingdll_webview_set_title.md) | Sets the text shown in the title bar of the specified WebView window. |
| [qiumingdll_webview_set_titlebar](qiumingdll_webview_set_titlebar.md) | Toggles whether the specified WebView window has a system title bar (a "borderless" mode for standalone windows). |
| [qiumingdll_webview_set_topmost](qiumingdll_webview_set_topmost.md) | Sets whether the specified **standalone** WebView window stays on top (above all other windows). |
| [qiumingdll_webview_set_zoom_factor](qiumingdll_webview_set_zoom_factor.md) | Sets the zoom factor of the specified WebView's page. |
| [qiumingdll_webview_show](qiumingdll_webview_show.md) | Shows the specified WebView window (cancels the hidden state). |
| [qiumingdll_webview_stop](qiumingdll_webview_stop.md) | Stops the specified WebView's current page load. |

[Back to documentation home](../README.md)
