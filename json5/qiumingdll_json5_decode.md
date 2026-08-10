# qiumingdll_json5_decode(json5_string)

将 JSON5 格式的字符串解析为 GameMaker 数据结构（DS Map / Array / 基础类型），在 Windows 平台优先调用 DLL 中的 JSON5 解析器，非 Windows 平台回退为 `json_decode`。

## 函数签名

```gml
qiumingdll_json5_decode(json5_string)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| json5_string | String | 是 | JSON5 格式的文本。JSON5 是 JSON 的超集，支持注释（`//`、`/* */`）、不加引号的键名、单引号字符串、尾随逗号、十六进制数字等 |

## 返回值

| 值 | 说明 |
|----|------|
| DS Map / Array / Real / String | 解析成功：根据内容返回 GameMaker 原生数据结构（对象/数组会映射为 DS Map 与 Array）。返回的结构需要自行用 `ds_map_destroy` 等释放 |
| 无效值 | 解析失败（例如字符串为空或格式完全非法），此时可对结构再次进行 `json_decode` 等兜底处理 |

## 使用说明

- 前置条件：Windows 平台需先调用 `qiumingdll_init()`；未初始化或非 Windows 平台时自动回退为内建的 `json_decode(argument0)`。
- 平台限制：DLL 路径仅在 Windows 平台可用；回退模式只支持标准 JSON，不支持注释、单引号等 JSON5 扩展语法。
- 行为细节：与标准 `json_decode` 的区别在于解析器本身接受 JSON5 语法；函数内部将 GML 字符串传给 DLL，再把 DLL 返回的 JSON 文本用 `json_decode` 转为结构。
- 注意：解析出来的 DS Map 需要手动销毁，避免内存泄漏。

## 示例

```gml
// 带注释和未加引号键名的 JSON5 文本
var str = "{ name: 'qiuming', // 单引号 + 注释" +
          "  version: 0x2a,  // 十六进制" +
          "  tags: [a, b, c,], }";

var data = qiumingdll_json5_decode(str);
if (is_struct(data))
{
    show_debug_message(string(data.name));
    ds_map_destroy(data);
}
```

## 相关函数

- [qiumingdll_json5_encode](qiumingdll_json5_encode.md)