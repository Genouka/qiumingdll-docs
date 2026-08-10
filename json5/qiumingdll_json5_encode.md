# qiumingdll_json5_encode(value)

将 GameMaker 数据结构（DS Map / Array / 基础类型）序列化为 JSON5 格式字符串，在 Windows 平台优先调用 DLL 实现，非 Windows 平台回退为 `json_encode`。

## 函数签名

```gml
qiumingdll_json5_encode(value)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| value | DS Map / Array / Real / String | 是 | 需要序列化的数据。DS Map 中可嵌套 Array、DS Map、Real、String、Bool |

## 返回值

| 值 | 说明 |
|----|------|
| String | 序列化得到 JSON5 文本。Windows + 已初始化时由 DLL 生成；否则回退为标准 `json_encode` 的输出 |

## 使用说明

- 前置条件：Windows 平台需先调用 `qiumingdll_init()`；未初始化或非 Windows 平台时回退为 `json_encode(argument0)`。
- 平台限制：DLL 路径仅在 Windows 平台可用。
- 行为细节：函数先把 GML 数据用 `json_encode` 转换为标准 JSON 文本传给 DLL，DLL 再输出最终结果；
- 可用于和 `qiumingdll_json5_decode` 配合做带注释数据的存取。

## 示例

```gml
var data = ds_map_create();
ds_map_add(data, "name", "qiuming");
ds_map_add(data, "version", 42);
ds_map_add_list(data, "tags", list);

var str = qiumingdll_json5_encode(data);
show_debug_message(str);
ds_map_destroy(data);
```

## 相关函数

- [qiumingdll_json5_decode](qiumingdll_json5_decode.md)