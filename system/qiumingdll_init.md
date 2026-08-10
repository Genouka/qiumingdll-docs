# qiumingdll_init()

初始化 qiumingdll 扩展：在 Windows 平台加载 DLL 并绑定全部外部函数，是所有其他 qiumingdll 函数可用的前提。

## 函数签名

```gml
qiumingdll_init()
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

- 前置条件：无。但必须先调用本函数，之后才能安全调用其他所有 `qiumingdll_*` 函数。
- 平台限制：仅在 Windows 平台（`os_type == os_windows`）生效；其他平台调用时直接跳过，不做任何事。
- 行为细节：初始化时会定义全局变量 `__qiumingdll_initialized`（置为 `true`），并利用 `external_define` 绑定 DLL 中的全部函数，绑定结果保存在 `global.__qiumingdll_*` 系列全局变量中。DLL 的加载是惰性的，真正的加载发生在第一次调用绑定函数时。
- 重复调用：本函数幂等。已经初始化过（全局变量 `__qiumingdll_initialized` 存在）时重复调用会自动跳过，不会重复绑定、也不会报错。
- 注意：调用 `qiumingdll_free()` 之后本函数的作用被撤销（`__qiumingdll_initialized` 置回 `false`），此时其余函数全部失效或返回默认值，必须再次调用本函数才能恢复。
- 建议在游戏首次加载（如 `game_start` 事件或某个全局管理对象的 Create 事件）中尽早调用一次。

## 示例

```gml
// 在游戏开始的全局对象 Create 事件中调用
qiumingdll_init();

// 之后可安全使用其他函数
qiumingdll_fixflash();
var v = qiumingdll_get_version();
show_debug_message("qiumingdll 版本: " + string(v));

// 重复调用不会产生副作用
qiumingdll_init();
```

## 相关函数

- [qiumingdll_free](qiumingdll_free.md)
- [qiumingdll_get_version](qiumingdll_get_version.md)
- [qiumingdll_fixflash](qiumingdll_fixflash.md)