# GML 绑定使用教程

> 本文档基于 QiumingDLL v1.8.0+，介绍如何在 GameMaker 中使用 QiumingDLL 的 GML 绑定。

## 一、快速开始

### 1. 复制 DLL

32 位 DLL 用于 32 位 GameMaker 游戏，64 位 DLL 用于 64 位 GameMaker 游戏。

把对应版本的 `qiumingdll.dll` 放到游戏目录（跟 `data.win` 同目录）。

### 2. 初始化

在游戏开始时（如创建事件）调用一次：

```gml
qiumingdll_init();  // 定义 DLL 中所有可用的外部函数
```

### 3. 释放（可选）

游戏结束时释放：

```gml
qiumingdll_free();
```

---

## 二、功能速查表

| 功能 | 使用方法 |
|------|----------|
| **修复闪屏** | `qiumingdll_fixflash()` |
| **窗口保活** | `qiumingdll_keeplive_init()` / `qiumingdll_keeplive_cleanup()` |
| **错误对话框** | `qiuming_show_error("错误描述")` |
| **禁用系统菜单** | `qiumingdll_disable_system_menu()` / `qiumingdll_restore_system_menu()` |
| **执行外部程序** | `qiuming_execute_program("路径")` / `qiuming_execute_program_async("路径")` |
| **获取版本号** | `qiuming_get_version()` |
| **窗口分裂** | 见下方详细说明 |
| **音高检测** | `qiumingdll_pitch_start(48000, 10)` 等 |
| **音量检测** | `qiumingdll_volume_start(48000, 10)` 等 |
| **WebView2** | `qiumingdll_webview_init()` 等 |
| **进程检测** | `qiumingdll_procdetect_cheatengine()` 等 |
| **JSON5** | `qiumingdll_json5_decode()` / `qiumingdll_json5_encode()` |
| **输入法控制** | `qiumingdll_ime_fix_conflict()` 等 |

---

## 三、窗口分裂 API

### 初始化与清理

```gml
qiumingdll_winsplit_init();       // 初始化
qiumingdll_winsplit_cleanup();    // 清理所有资源
```

### 创建与销毁

```gml
// create(srcX, srcY, srcW, srcH, dstX, dstY, dstW, dstH)
id = qiumingdll_winsplit_create(0, 0, 400, 300, 100, 100, 400, 300);

qiumingdll_winsplit_destroy(id);       // 销毁单个
qiumingdll_winsplit_destroy_all();     // 销毁所有
```

### 窗口操作

```gml
qiumingdll_winsplit_show(id);
qiumingdll_winsplit_hide(id);
qiumingdll_winsplit_set_position(id, x, y);
qiumingdll_winsplit_set_size(id, w, h);
qiumingdll_winsplit_set_region(id, x, y, w, h);  // 同时设置位置和大小
qiumingdll_winsplit_set_opacity(id, 0~255);
qiumingdll_winsplit_set_topmost(id, 1/0);
qiumingdll_winsplit_set_draggable(id, 1/0);
qiumingdll_winsplit_set_titlebar(id, 1/0);
qiumingdll_winsplit_set_title(id, "标题文本");
qiumingdll_winsplit_set_closable(id, 1/0);
qiumingdll_winsplit_set_close_triggers_main(id, 1/0);
```

### 查询信息

```gml
count = qiumingdll_winsplit_get_count();      // 活跃分屏数量
exists = qiumingdll_winsplit_exists(id);      // 是否存在

// get_info(id, infoType)  infoType: 0=X, 1=Y, 2=宽, 3=高
wx = qiumingdll_winsplit_get_info(id, 0);
```

### 原窗口控制

```gml
qiumingdll_winsplit_hide_original();    // 隐藏原窗口（DWM Cloak）
qiumingdll_winsplit_show_original();    // 恢复显示
```

### 动画

```gml
// 缓动曲线（在动画函数前设置）
// 0=线性, 1=ease-in, 2=ease-out, 3=ease-in-out(默认)
// 4~6=cubic, 7~9=back, 10=bounce, 11=elastic
qiumingdll_winsplit_set_easing_curve(id, 3);

// 位置动画
qiumingdll_winsplit_set_position_animate(id, x, y, 500, 16);

// 大小动画
qiumingdll_winsplit_set_size_animate(id, w, h, 500, 16);

// 区域动画
qiumingdll_winsplit_set_region_animate(id, x, y, w, h, 500, 16);

// 停止/查询
qiumingdll_winsplit_stop_animation(id);
isAnimating = qiumingdll_winsplit_is_animating(id);
```

### 批量动画

```gml
// 录制
qiumingdll_winsplit_batch_begin(id);
qiumingdll_winsplit_batch_set_easing(id, 3);
qiumingdll_winsplit_batch_add_position(id, 300, 200, 500);
qiumingdll_winsplit_batch_add_wait(id, 200);
qiumingdll_winsplit_batch_add_size(id, 400, 300, 500);
qiumingdll_winsplit_batch_end(id);

// 播放
qiumingdll_winsplit_batch_play(id, 1);  // conflictMode: 0=叠加, 1=打断, 2=回退, 3=快进

// 控制
qiumingdll_winsplit_batch_stop(id);
isPlaying = qiumingdll_winsplit_batch_is_playing(id);
qiumingdll_winsplit_batch_clear(id);
```

### 异形窗口

```gml
// 椭圆
qiumingdll_winsplit_set_shape_ellipse(id);

// 圆角矩形
qiumingdll_winsplit_set_shape_roundrect(id, cornerW, cornerH);

// 多边形
qiumingdll_winsplit_begin_shape(id);
qiumingdll_winsplit_add_shape_point(id, 0, 0);
qiumingdll_winsplit_add_shape_point(id, 200, 0);
qiumingdll_winsplit_add_shape_point(id, 100, 150);
qiumingdll_winsplit_end_shape(id);

// 位图遮罩
qiumingdll_winsplit_set_shape_from_bitmap(id, "mask.bmp", 0x00FF00);

// 恢复矩形
qiumingdll_winsplit_clear_shape(id);
```

---

## 四、麦克风音高检测 API

```gml
// 启动（sampleRate: 8000~192000, bufferMs: 5~100）
qiumingdll_pitch_start(48000, 10);

// 查询
freq = qiumingdll_pitch_get_frequency();   // Hz，0=未检测到
vol = qiumingdll_pitch_get_volume();       // 0~1
note = qiumingdll_pitch_get_note();        // MIDI 编号，-1=无
active = qiumingdll_pitch_is_active();     // 0/1

// 参数
qiumingdll_pitch_set_threshold(0.15);     // 0.01~0.99

// 停止/清理
qiumingdll_pitch_stop();
qiumingdll_pitch_cleanup();
```

### MIDI 音符速查

| MIDI | 音名 | 频率 |
|------|------|------|
| 60 | C4 (中央C) | 261.63 Hz |
| 69 | A4 | 440.00 Hz |
| 72 | C5 | 523.25 Hz |

---

## 五、麦克风音量检测 API

```gml
// 启动
qiumingdll_volume_start(48000, 10);

// 查询
rms = qiumingdll_volume_get_rms();       // 0~1
peak = qiumingdll_volume_get_peak();     // 0~1
db = qiumingdll_volume_get_db();         // -96~0 dB
level = qiumingdll_volume_get_level();   // 0~5
active = qiumingdll_volume_is_active();  // 0/1

// 参数
qiumingdll_volume_set_silence_threshold(0.01);  // 0~0.5
qiumingdll_volume_set_smoothing(0.3);            // 0~1

// 停止/清理
qiumingdll_volume_stop();
qiumingdll_volume_cleanup();
```

### 音量等级

| 等级 | RMS 范围 | 含义 |
|------|----------|------|
| 0 | < 静音阈值 | 静音 |
| 1 | 0.01~0.05 | 很轻 |
| 2 | 0.05~0.15 | 轻 |
| 3 | 0.15~0.35 | 中等 |
| 4 | 0.35~0.60 | 响 |
| 5 | > 0.60 | 很响 |

---

## 六、WebView2 API

### 前置要求

- 将 `WebView2Loader.dll` 放到游戏可执行文件同目录
- 系统需安装 Edge WebView2 Runtime（Win10/11 已预装）

### 初始化与清理

```gml
qiumingdll_webview_init();       // 初始化
qiumingdll_webview_cleanup();    // 清理
```

### 创建与销毁

```gml
// 独立窗口
id = qiumingdll_webview_create(x, y, w, h);

// 子窗口（嵌入游戏窗口）
id = qiumingdll_webview_create_child(x, y, w, h);

qiumingdll_webview_destroy(id);
qiumingdll_webview_destroy_all();
```

### 导航

```gml
qiumingdll_webview_navigate(id, "https://example.com");
qiumingdll_webview_navigate_to_string(id, "<h1>Hello</h1>");
qiumingdll_webview_reload(id);
qiumingdll_webview_stop(id);
qiumingdll_webview_go_back(id);
qiumingdll_webview_go_forward(id);
```

### 执行 JavaScript

```gml
qiumingdll_webview_execute_script(id, "document.title = 'Hello'");
```

### 窗口操作

```gml
qiumingdll_webview_show(id);
qiumingdll_webview_hide(id);
qiumingdll_webview_set_position(id, x, y);
qiumingdll_webview_set_size(id, w, h);
qiumingdll_webview_set_opacity(id, 0~255);
qiumingdll_webview_set_topmost(id, 1/0);
qiumingdll_webview_set_title(id, "标题");
qiumingdll_webview_set_titlebar(id, 1/0);
qiumingdll_webview_set_closable(id, 1/0);
qiumingdll_webview_set_draggable(id, 1/0);
qiumingdll_webview_set_zoom_factor(id, 1.0);
```

### 查询

```gml
active = qiumingdll_webview_get_is_active(id);
count = qiumingdll_webview_get_count();
exists = qiumingdll_webview_exists(id);
isChild = qiumingdll_webview_is_child(id);
qiumingdll_webview_resize_to_parent(id);  // 自动跟随父窗口
```

---

## 七、进程检测 API

无需初始化，直接调用：

```gml
// 检测作弊/调试工具
if (qiumingdll_procdetect_cheatengine()) {
    show_debug_message("检测到作弊工具！");
}

// 检测直播/录屏软件
if (qiumingdll_procdetect_streaming()) {
    show_debug_message("检测到录屏软件！");
}

// 检测多开
var instances = qiumingdll_procdetect_multiinstance();
if (instances >= 2) {
    show_debug_message("游戏多开了！");
}

// 检测指定进程
if (qiumingdll_procdetect_process("notepad.exe")) {
    show_debug_message("记事本运行中");
}
```

---

## 八、JSON5 API

无需初始化，直接调用：

```gml
// JSON5 → JSON
var json = qiumingdll_json5_decode('{ name: "hello", age: 18, }');
// 返回: {"name":"hello","age":18}

// JSON → JSON5
var json5 = qiumingdll_json5_encode('{"name":"hello","age":18}');
// 返回格式化的 JSON5
```

---

## 九、输入法 API

### 基础功能

```gml
// 修复输入法冲突
qiumingdll_ime_fix_conflict();

// 切换输入法
qiumingdll_ime_switch(0);  // 0=英文, 1=中文, 2=下一个, 3=上一个

// 获取模式
mode = qiumingdll_ime_get_mode();  // 0=英文, 1=中文, -1=失败
```

### 内联模式

```gml
// 设置候选框位置
qiumingdll_ime_set_inline_position(x, y);

// 取消内联
qiumingdll_ime_reset_inline();
```

### 状态轮询

```gml
// 获取状态标志
state = qiumingdll_ime_get_state();
// 0x01=组合中, 0x02=有提交, 0x04=候选变化, 0x08=模式变化

// 获取组合文本
compText = qiumingdll_ime_get_composition_text();
cursor = qiumingdll_ime_get_composition_cursor();

// 获取提交文本（读取后清空）
commitText = qiumingdll_ime_get_commit_text();

// 候选列表
count = qiumingdll_ime_get_candidate_count();
cand = qiumingdll_ime_get_candidate(index);
sel = qiumingdll_ime_get_candidate_selection();
```

### 便捷 API

```gml
// 一次性轮询所有状态
var map = qiumingdll_ime_poll();
// ds_map 包含: composing, compText, compCursor, commitText, candidates, candidateSel, inputMode, stateFlags
qiumingdll_ime_poll_destroy(map);

// 简化获取提交文本
var commit = qiumingdll_ime_get_commit();
```

---

## 十、完整示例

### 示例：双屏显示

```gml
// 创建事件
qiumingdll_init();
qiumingdll_winsplit_init();

var ww = window_get_width();
var hh = window_get_height();

var left = qiumingdll_winsplit_create(0, 0, ww/2, hh, 0, 0, ww/2, hh);
var right = qiumingdll_winsplit_create(ww/2, 0, ww/2, hh, ww/2, 0, ww/2, hh);

qiumingdll_winsplit_hide_original();
qiumingdll_winsplit_set_topmost(left, 1);
qiumingdll_winsplit_set_topmost(right, 1);

// 清理事件
qiumingdll_winsplit_show_original();
qiumingdll_winsplit_cleanup();
```

### 示例：音高检测显示

```gml
// 创建事件
qiumingdll_pitch_start(48000, 10);

// Step 事件
var freq = qiumingdll_pitch_get_frequency();
var vol = qiumingdll_pitch_get_volume();

if (freq > 0) {
    var note = qiumingdll_pitch_get_note();
    show_debug_message("音高: " + string(freq) + "Hz");
}

// 清理事件
qiumingdll_pitch_stop();
qiumingdll_pitch_cleanup();
```

### 示例：WebView2 内嵌网页

```gml
// 创建事件
qiumingdll_webview_init();
var wv = qiumingdll_webview_create_child(10, 10, 400, 300);
qiumingdll_webview_resize_to_parent(wv);
qiumingdll_webview_navigate(wv, "https://example.com");

// 清理事件
qiumingdll_webview_cleanup();
```

---

## 十一、开发者扩展指南

1. 在 `src/` 下创建 `qm_xxx.h` 和 `qm_xxx.cpp`
   - 实现 `bool qm_xxx_init()` 和 `void qm_xxx_cleanup()`
   - 用 `QM_EXPORT` 修饰导出函数

2. 修改 `src/qiumingdll.cpp`：
   - 添加 `#include "qm_xxx.h"`
   - 在 `DllMain` 中添加 `qm_register_module("xxx", qm_xxx_init, qm_xxx_cleanup);`

3. 在 `gml/` 下添加对应的 GML 脚本
   - 在 `qiumingdll_init.gml` 中添加 `external_define`

4. 重新编译

---

## 十二、编译指南

1. 安装 Visual Studio 2019/2022（带"C++ 桌面开发"工作负载）
2. 双击 `compile.bat`，自动编译 x32 和 x64 两个版本
3. 编译产物在 `output/x32/qiumingdll.dll` 和 `output/x64/qiumingdll.dll`
