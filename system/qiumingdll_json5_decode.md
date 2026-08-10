# qiumingdll_json5_decode(json5Text)

解析 JSON5 格式文本（带注释、单引号、无引号键等扩展语法），返回对应的 GML 数据结构。

## 函数签名

```gml
qiumingdll_json5_decode(json5Text)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| json5Text | String | 是 | JSON5 格式的文本。支持标准 JSON 之外的大量扩展语法（见下方说明） |

## 返回值

| 值 | 说明 |
|----|------|
| struct / array / ds_map | 解析成功时返回与内容对应的 GML 数据结构（由内部 `json_decode` 决定具体类型：对象解析为 struct 或 ds_map，数组解析为 array） |
| `json_decode("")` 的结果 | 解析失败时返回（即对空字符串解码的结果，通常为某种空数据表示，不会抛出异常） |

## 使用说明

- 前置条件：Windows 上需先调用 `qiumingdll_init()`。
- 平台限制：Windows 上 DLL 先把 JSON5 转换为标准 JSON，再交给 GML 的 `json_decode` 解析；非 Windows 平台直接调用 `json_decode(json5Text)`（即不支持 JSON5 扩展语法，仅接受标准 JSON）。
- 支持的 JSON5 扩展语法（Windows 平台）：
  - 注释：`// 行注释` 与 `/* 块注释 */`；
  - 字符串：单引号 `'...'` 与双引号 `"..."` 均可用，支持 `\x41`、`\u0041` 等转义；
  - 键：对象键可不加引号（裸标识符，如 `{ name: "A" }`），键中支持 `\n`、`\uXXXX` 等转义；
  - 尾逗号：对象与数组最后一个元素后允许多余的逗号；
  - 数字：十六进制（`0xFF`）、正负 `Infinity`、`NaN`（解码结果为 null / 极限大数）、小数点开头（`.5`）等；
  - 布尔与空值：`true`、`false`、`null`。
- 失败行为：文本格式错误（如括号不闭合、键缺失冒号、残留多余字符）时视为解析失败，返回 `json_decode("")` 的结果，不会崩溃。建议调用后校验返回内容。
- 注意：解析出的对象最终是 struct 还是 ds_map 取决于 GML 运行时的 `json_decode` 行为；如需确保得到 ds_map，可在调用前设置相应的 json 选项（`json_*` 相关缓冲/格式设置由项目自行决定）。
- 典型用途：读取人类手写的、带注释的配置文件。

## 示例

```gml
// 读取带注释与单引号的 JSON5 配置
qiumingdll_init();

var json5Text = @"
{
  // 玩家配置
  name: 'Kris',          // 单引号字符串 + 无引号键
  level: 0x2A,           // 十六进制数字（= 42）
  items: ['apple', 'pear',],
  boss: {
    hp: Infinity,
  }
}";

var cfg = qiumingdll_json5_decode(json5Text);
if (is_struct(cfg) || is_ds_map(cfg))
{
    show_debug_message("玩家名: " + string(cfg.name));   // 访问方式视返回类型而定
}
```

## 相关函数

- [qiumingdll_json5_encode](qiumingdll_json5_encode.md)
- [qiumingdll_init](qiumingdll_init.md)