# QiumingDLL API Documentation

> Version 1.9.0

QiumingDLL 是一个 Windows 扩展动态链接库，为游戏开发提供多种功能模块。采用模块化架构，支持热插拔式功能扩展。

## 概述

QiumingDLL 通过 `DllMain` 自动加载所有内置模块，在 DLL 加载时初始化，卸载时清理。所有导出函数使用 `QM_Real`（double）作为返回类型，字符串参数使用 `QM_String`（char*）。

## 类型定义

| 类型 | 定义 | 说明 |
|------|------|------|
| `QM_Real` | `double` | 数值类型，用于所有数值参数和返回值 |
| `QM_String` | `char*` | 字符串类型，UTF-8 编码 |

## 版本信息

```c
QM_VERSION_MAJOR  1
QM_VERSION_MINOR  9
QM_VERSION_PATCH  0
```

## 通用 API

| 函数 | 返回值 | 说明 |
|------|--------|------|
| `qmGetVersion()` | `QM_Real` | 获取 DLL 版本号（major*10000 + minor*100 + patch） |
| `qmGetModuleCount()` | `QM_Real` | 获取已注册模块数量 |
| `qmGetModuleInfo(index)` | `QM_Real` | 获取模块初始化状态（0=未初始化，1=已初始化，-1=无效索引） |

## 模块列表

| 模块名 | 功能 | 文档链接 |
|--------|------|----------|
| fixflash | 修复窗口闪烁问题 | [查看文档](fixflash.md) |
| keeplive | 窗口保活（防止被关闭） | [查看文档](keeplive.md) |
| specmessage | 自定义错误对话框 | [查看文档](specmessage.md) |
| spectitle | 禁用/恢复系统菜单 | [查看文档](spectitle.md) |
| winsplit | 窗口分裂（GPU D3D11 钩子方案） | [查看文档](winsplit.md) |
| pitch | 音高检测（麦克风输入） | [查看文档](pitch.md) |
| volume | 音量检测（麦克风输入） | [查看文档](volume.md) |
| webview | WebView2 浏览器嵌入 | [查看文档](webview.md) |
| procdetect | 进程检测 | [查看文档](procdetect.md) |
| json5 | JSON5 编解码 | [查看文档](json5.md) |
| ime | 输入法管理 | [查看文档](ime.md) |

## 工具函数

| 函数 | 返回值 | 说明 |
|------|--------|------|
| `qmExecuteProgram(programPath)` | `QM_Real` | 同步执行外部程序，返回退出码（-1=失败） |
| `qmExecuteProgramAsync(programPath)` | `QM_Real` | 异步执行外部程序，返回 BOOL 结果 |

## 使用说明

1. 将 `qiumingdll.dll` 放置在游戏目录或系统 PATH 中
2. DLL 加载时自动初始化所有模块
3. 通过导出函数调用各模块功能
4. DLL 卸载时自动清理所有模块
