# qiumingdll_keeplive_is_active()

查询窗口保活钩子当前是否已安装，返回 1 表示保活生效中、0 表示未安装。

## 函数签名

```gml
qiumingdll_keeplive_is_active()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 保活钩子已安装：qiumingdll_keeplive_init() 已成功调用且尚未调用 cleanup 卸载 |
| 0 | 钩子未安装：init 未调用、init 失败，或已调用 qiumingdll_keeplive_cleanup()。**非 Windows 平台**的 GML 包装函数也直接返回 0 |

## 使用说明

- 前置条件：无，任何时刻都可安全调用。
- 平台限制：仅 Windows 有效（非 Windows 平台包装函数直接返回 0）。
- 用途：在 UI 上显示保活状态（如"防未响应：已开启"）、调试时确认 init 是否真正生效、以及避免重复调用 init。
- 行为细节：init 成功返回 0 后，is_active 立即变为 1；cleanup 调用后立即变回 0。若保活的某个内部钩子因异常被自动移除，为 0 时表示保护已不完整，应重新 init。
- 提示：is_active 为 1 只代表钩子在位，并非"窗口一定不会无响应"；它只是通过拦截消息降低被系统强制关闭的风险。

## 示例

```gml
/// Step 事件 (obj_keeplive_manager)
// 每帧检查保活状态，意外失效时自动重装
if (wantKeepAlive && qiumingdll_keeplive_is_active() == 0)
{
    qiumingdll_keeplive_init();
}

/// Draw GUI 事件
// 状态显示
if (qiumingdll_keeplive_is_active() == 1)
{
    draw_set_color(c_lime);
    draw_text(10, 10, "保活钩子：已安装");
}
else
{
    draw_set_color(c_red);
    draw_text(10, 10, "保活钩子：未安装");
}
```

## 相关函数

- [qiumingdll_keeplive_init](qiumingdll_keeplive_init.md)
- [qiumingdll_keeplive_cleanup](qiumingdll_keeplive_cleanup.md)