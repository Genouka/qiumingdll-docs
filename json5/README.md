# json5 模块

JSON5 格式的编解码，支持注释、单引号字符串、未加引号键名、尾随逗号、十六进制数字等标准 JSON 之外的扩展语法。

共 2 个函数。

## 函数索引

| 函数 | 说明 |
|------|------|
| [qiumingdll_json5_decode](qiumingdll_json5_decode.md) | 将 JSON5 格式的字符串解析为 GameMaker 数据结构（DS Map / Array / 基础类型），在 Windows 平台优先调用 DLL 中的 JSON5 解析器，… |
| [qiumingdll_json5_encode](qiumingdll_json5_encode.md) | 将 GameMaker 数据结构（DS Map / Array / 基础类型）序列化为 JSON5 格式字符串，在 Windows 平台优先调用 DLL 实现，非 Windows … |

[返回文档首页](../README.md)