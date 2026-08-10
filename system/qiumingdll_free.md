# qiumingdll_free()

释放 qiumingdll 扩展：卸载 DLL 并撤销初始化状态，使其余所有 qiumingdll 函数失效。

## 函数签名

```gml
qiumingdll_free()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 无返回值 | 本函数不返回任何值 |

## 使用说明

- 前置条件：建议先调用过 `qiumingdll_init()`；若从未初始化，本函数在 Windows 上也会因全局变量不存在而自动跳过，不会报错。
- 平台限制：仅在 Windows 平台（`os_type == os_windows`）生效；其他平台调用时无操作。
- 行为细节：Windows 上会调用 `external_free("qiumingdll.dll")` 卸载 DLL，并将全局变量 `__qiumingdll_initialized` 置回 `false`，即回到未初始化状态。
- 注意：释放之后，其他所有 `qiumingdll_*` 函数都将失效——部分函数会因找不到绑定变量而不执行，部分会返回默认值（如版本号返回 0）。必须重新调用 `qiumingdll_init()` 才能再次使用。
- 适用场景：游戏退出清理、热重载 DLL、或运行中途不再需要扩展功能时释放资源。通常游戏全程只需 init 一次，无需调用本函数。
- 与 `qiumingdll_init()` 的幂等不同，本函数执行一次即完成释放；再次调用（未重新 init 时）自动跳过。

## 示例

```gml
// 游戏退出清理时释放扩展
qiumingdll_init();
qiumingdll_fixflash();

// 需要释放时……
qiumingdll_free();

// 释放后其他函数不再生效（此处返回 0）
var v = qiumingdll_get_version();
show_debug_message("释放后的版本号: " + string(v));

// 想继续使用必须先重新初始化
qiumingdll_init();
```

## 相关函数

- [qiumingdll_init](qiumingdll_init.md)
- [qiumingdll_get_version](qiumingdll_get_version.md)