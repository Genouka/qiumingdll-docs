# qiumingdll_get_version()

获取 qiumingdll 扩展的版本号整数，可用于运行时判断扩展能力。

## 函数签名

```gml
qiumingdll_get_version()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 10900（当前版本 1.9.0） | 版本号整数，编码格式为 `主版本*10000 + 次版本*100 + 修订号`。例如 1.9.0 → 1×10000 + 9×100 + 0 = 10900；2.3.4 → 20304 |
| 0 | 非 Windows 平台调用，或 DLL 未初始化（已 `qiumingdll_free()`）时返回 |

## 使用说明

- 前置条件：Windows 上需先调用 `qiumingdll_init()`，否则找不到绑定的外部函数，返回 0。
- 平台限制：仅在 Windows 平台返回真实版本号；其他平台固定返回 0。
- 行为细节：版本号由 DLL 内部编译期常量计算得出，每次构建扩展后版本会变化，本函数返回的是扩展自身的版本，与游戏版本无关。
- 用途：可用于版本兼容性判断——当游戏依赖的某个 qiumingdll 功能在特定版本才引入时，先检查版本号再决定是否调用相关函数。
- 注意：`qiumingdll_free()` 之后调用本函数同样返回 0。

## 示例

```gml
// 检查扩展版本
qiumingdll_init();

var ver = qiumingdll_get_version();
show_debug_message("qiumingdll version code: " + string(ver));

// 按版本判断是否支持某项功能（假设该功能从 2.0.0 起可用）
if (ver >= 20000)
{
    // 使用较新版本才有的能力
}
else
{
    show_message("检测到旧版 qiumingdll 扩展，请更新");
}
```

## 相关函数

- [qiumingdll_init](qiumingdll_init.md)
- [qiumingdll_free](qiumingdll_free.md)