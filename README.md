# qiumingdll 文档

qiumingdll 扩展（Windows 专用 GameMaker 扩展）的完整函数参考文档。

## 模块导航

| 模块 | 目录 | 文档数 | 说明 |
|------|------|--------|------|
| 核心 | [system](system/) | 15 | `qiumingdll_init` / `free` / 版本 / 系统菜单 / 程序执行等 |
| 进程检测 | [procdetect](procdetect/) | 4 | 检测 Cheat Engine、直播软件、多开、任意进程 |
| JSON5 | [json5](json5/) | 2 | JSON5 格式的编码 / 解码 |
| 窗口分屏 | [winsplit](winsplit/) | 61 | 多窗口分屏显示、形状裁剪、批量动画 |
| WebView | [webview](webview/) | 37 | 内置浏览器窗口（独立 / 子窗口） |
| 输入法 | [ime](ime/) | 23 | 输入法候选、拼音、内嵌编辑、轮询 |
| 麦克风音量 | [volume](volume/) | 10 | 音量峰值 / RMS / dB 检测与阈值 |
| 音高检测 | [pitch](pitch/) | 8 | 麦克风输入的音高 / 音符检测 |
| 保活 | [keeplive](keeplive/) | 3 | 防止系统进入休眠 / 屏幕关闭 |

共 163 篇函数文档（覆盖 `gml/` 目录下全部 157 个 GML 包装函数，其中 webview/set_region 等多态函数拆分多篇）。

## 文档格式

每篇函数文档均遵循 [doc-template.md](doc-template.md)：

- 函数签名与参数说明
- 返回值对照表
- 使用说明（前置条件、平台限制、注意事项）
- GML 示例代码
- 相关函数链接

## 快速上手

```gml
qiumingdll_init();              // 1. 初始化（仅 Windows 生效）
qiumingdll_fixflash();          // 2. 可选：修复 Flash 控件
show_debug_message(qiumingdll_get_version());  // 3. 校验扩展版本
```

详见 [system/qiumingdll_init.md](system/qiumingdll_init.md)。