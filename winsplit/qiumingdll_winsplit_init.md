# qiumingdll_winsplit_init()

初始化窗口分裂模块：记录当前游戏窗口、注册分裂窗口类并安装画面捕获钩子，是所有窗口分裂功能的前置条件。

## 函数签名

```gml
qiumingdll_winsplit_init()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何 GML 参数。包装层会自动把当前游戏的窗口句柄（`window_handle()`）传给 DLL，调用方无需提供 |

## 返回值

| 值 | 说明 |
|----|------|
| 0 | 初始化成功，模块已就绪，可以创建分裂窗口 |
| 1 | 初始化失败（如窗口句柄无效、窗口类注册失败）；在非 Windows 平台上，GML 包装层直接返回 1，不会调用 DLL |

## 使用说明

- 前置条件：必须先调用 `qiumingdll_init()` 完成扩展整体初始化（该函数注册 `__qiumingdll_winsplit_*` 等全局函数句柄）；否则包装层检测不到句柄，会直接返回失败值。
- 平台限制：仅 Windows 可用；macOS / Linux 等非 Windows 平台直接返回 1。
- 在游戏生命周期内应只调用一次；若需要重新初始化，请先调用 `qiumingdll_winsplit_cleanup()` 清理后再调用本函数。
- 本模块依赖 D3D11 渲染捕获才能显示分裂画面，游戏需使用 D3D11 渲染（GameMaker 默认即是）。
- 初始化成功建议用全局变量记录结果，后续创建分裂窗口前先检查，避免在失败环境下继续调用。
- 初始化成功后默认不创建任何分裂窗口，不隐藏原窗口；需要再调用创建和隐藏相关函数。

## 示例

```gml
// 在控制对象的 Create 事件中初始化窗口分裂模块
if (os_type == os_windows)
{
    // 先完成扩展整体初始化（注册 DLL 函数句柄）
    qiumingdll_init();

    // 初始化窗口分裂模块
    var _ret = qiumingdll_winsplit_init();
    if (_ret == 0)
    {
        global.winsplit_ready = true;
        show_debug_message("窗口分裂模块初始化成功");
    }
    else
    {
        global.winsplit_ready = false;
        show_debug_message("窗口分裂模块初始化失败");
    }
}
```

## 相关函数

- [qiumingdll_winsplit_create](qiumingdll_winsplit_create.md)
- [qiumingdll_winsplit_cleanup](qiumingdll_winsplit_cleanup.md)
- [qiumingdll_winsplit_hide_original](qiumingdll_winsplit_hide_original.md)