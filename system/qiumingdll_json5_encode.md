# qiumingdll_json5_encode(value)

把 GML 值编码为紧凑易读的 JSON5 风格字符串（键不加引号、字符串用单引号、带缩进）。

## 函数签名

```gml
qiumingdll_json5_encode(value)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| value | Any | 是 | 任意可被 `json_encode` 序列化的 GML 值：struct、ds_map、array、String、Real、Bool、undefined/null 等均可 |

## 返回值

| 值 | 说明 |
|----|------|
| String | 编码后的 JSON5 风格字符串。示例效果：`{ name: 'Kris', level: 42, items: ['apple', 'pear'] }` |
| 空字符串 `""` | 传入的值无法序列化或序列化过程失败时返回 |

## 使用说明

- 前置条件：Windows 上需先调用 `qiumingdll_init()`。
- 平台限制：Windows 上先把 GML 值经 `json_encode` 转为标准 JSON 字符串，再由 DLL 转成 JSON5 风格并支持缩进美化；非 Windows 平台直接返回 `json_encode(value)`（即输出标准 JSON，不带 JSON5 美化）。
- 行为细节（Windows 平台）：
  - 对象键：合法的标识符键不加引号（以字母、`_`、`$` 开头，仅含字母、数字、`_`、`$`，且不是 JS 保留字）；其余键保留双引号；
  - 字符串：一律改用单引号输出（内部字符串内容中的单引号会被转义为 `\'`）；
  - 缩进：嵌套的对象与数组按 2 空格缩进换行，便于人眼阅读。
- 注意：`json_encode` 对循环引用或含非序列化内容的 struct 会失败，此时本函数在 Windows 可能返回空字符串；调用后建议做判空处理。
- 典型用途：把存档、设置等数据导出为人类可读、可手改的配置文件，再配合 `qiumingdll_json5_decode()` 读回。
- 输出为多行带缩进文本，若需要单行紧凑输出，可自行用 GML 字符串处理去除换行与缩进。

## 示例

```gml
// 把游戏配置保存为 JSON5 风格字符串
qiumingdll_init();

var config =
{
    name: "Kris",
    level: 42,
    inventory: ["apple", "pear", "sword"],
    settings:
    {
        sound: true,
        fullscreen: false,
    }
};

var json5Text = qiumingdll_json5_encode(config);
show_debug_message(json5Text);
// 输出效果：
// {
//   name: 'Kris',
//   level: 42,
//   inventory: ['apple', 'pear', 'sword'],
//   settings: {
//     sound: true,
//     fullscreen: false
//   }
// }

// 保存到文件，之后可用 qiumingdll_json5_decode 读回
// file_text_write_string(file_text_open_write("config.json5"), json5Text);
```

## 相关函数

- [qiumingdll_json5_decode](qiumingdll_json5_decode.md)
- [qiumingdll_init](qiumingdll_init.md)