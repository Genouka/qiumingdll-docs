# json5 模块

JSON5 编解码模块。支持 JSON5 格式与标准 JSON 格式之间的转换。

## JSON5 特性

- 单引号字符串
- 未加引号的键名
- 注释（`//` 和 `/* */`）
- 尾随逗号
- 十六进制数字
- `Infinity`、`-Infinity`、`NaN`
- 多行字符串

## API

### qmJson5Decode

```c
QM_EXPORT QM_String qmJson5Decode(QM_String json5Str);
```

**参数：**
- `json5Str` - JSON5 格式字符串

**返回值：** 标准 JSON 格式字符串，解析失败返回空字符串

**转换示例：**
```json5
// 输入 (JSON5)
{
  name: 'test',
  value: 123,
  // 这是注释
  list: [1, 2, 3,],
}

// 输出 (JSON)
{"name":"test","value":123,"list":[1,2,3]}
```

---

### qmJson5Encode

```c
QM_EXPORT QM_String qmJson5Encode(QM_String jsonStr);
```

**参数：**
- `jsonStr` - 标准 JSON 格式字符串

**返回值：** JSON5 格式字符串（美化输出），编码失败返回空字符串

**转换示例：**
```json
// 输入 (JSON)
{"name":"test","value":123,"list":[1,2,3]}

// 输出 (JSON5)
{
  name: 'test',
  value: 123,
  list: [
    1,
    2,
    3
  ]
}
```

## 使用示例

```c
// 解码 JSON5
const char* json5 = "{ name: 'test', value: 42 }";
const char* json = qmJson5Decode(json5);
// json 现在是 {"name":"test","value":42}

// 编码为 JSON5
const char* jsonInput = "{\"key\":\"value\"}";
const char* json5Output = qmJson5Encode(jsonInput);
// json5Output 是美化后的 JSON5 格式
```

## 注意事项

- 返回的字符串指针指向内部缓冲区，下次调用时会被覆盖
- 解析错误时返回空字符串
- NaN 会被转换为 null
- Infinity 会被转换为 1e999
