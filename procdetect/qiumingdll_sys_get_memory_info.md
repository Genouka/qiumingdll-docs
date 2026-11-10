# qiumingdll_sys_get_memory_info()

获取系统物理内存使用情况，返回 JSON 字符串。

## 函数签名

```gml
qiumingdll_sys_get_memory_info()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数 |

## 返回值

返回 JSON 字符串：`{ "total": 总物理内存字节数, "used": 已用字节数, "free": 可用字节数, "percent": 已用百分比 }`。

| 字段 | 类型 | 说明 |
|------|------|------|
| total | Real | 系统安装的物理内存总量（字节） |
| used | Real | 当前已使用的物理内存（total - free，字节） |
| free | Real | 当前可用的物理内存（字节） |
| percent | Real | 已用百分比，保留两位小数（0.00 ~ 100.00） |

调用失败（非 Windows）时返回 `{}`。

## 使用说明

- 前置条件：Windows 上需先调用 `qiumingdll_init()`。
- 平台限制：仅 Windows 生效；基于 `GlobalMemoryStatusEx` 读取物理内存。
- 行为细节：每次调用实时读取，无需像 CPU/GPU 那样做差值采样，可随时调用。
- 解析返回的 JSON 可使用 `qiumingdll_json5_decode()`。
- 典型用途：在设置界面显示内存占用、在内存不足时提示玩家关闭其他程序。

## 示例

```gml
qiumingdll_init();

var json = qiumingdll_sys_get_memory_info();
var mem = qiumingdll_json5_decode(json);
if (is_array(mem))
{
    var totalMB = mem[? "total"] / (1024 * 1024);
    var usedMB = mem[? "used"] / (1024 * 1024);
    var pct = mem[? "percent"];
    show_debug_message("内存: " + string(usedMB) + " / " + string(totalMB) + " MB (" + string(pct) + "%)");
}
```

## 相关函数

- [qiumingdll_sys_get_cpu_usage](qiumingdll_sys_get_cpu_usage.md)
- [qiumingdll_sys_get_gpu_usage](qiumingdll_sys_get_gpu_usage.md)
- [qiumingdll_json5_decode](../json5/qiumingdll_json5_decode.md)
- [qiumingdll_init](qiumingdll_init.md)
