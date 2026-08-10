# qiumingdll_winsplit_set_closable(splitId, closable)

设置指定分裂窗口是否允许被用户关闭（通过标题栏的 X 按钮或系统菜单的"关闭"）。

## 函数签名

```gml
qiumingdll_winsplit_set_closable(splitId, closable)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口 ID，取值 1 ~ 16，必须存在 |
| closable | Real/Bool | 是 | 是否可被用户关闭：非 0（true）= 允许关闭（默认），0（false）= 禁止关闭 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 失败：splitId 无效或不存在；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用，且 splitId 对应的分裂窗口存在。
- 创建时默认 `closable = true`（用户可关闭）。
- closable = false 时：点击标题栏 X 无反应；系统菜单（Alt+空格）中的"关闭"项变灰不可点。有标题栏时系统菜单的关闭项会同步置灰。
- 本函数只拦截"用户关闭"：程序调用 `qiumingdll_winsplit_destroy` / `destroy_all` 不受影响，仍然可以销毁。
- 与 `qiumingdll_winsplit_set_close_triggers_main` 的联动关系：只有真正发生"用户关闭"动作时，才会触发 close_triggers_main 的联动。
- 若窗口无标题栏（`set_titlebar(splitId, false)`），系统菜单关闭入口已被移除，closable 依然生效于其它关闭路径（如 WM_CLOSE 消息）。

## 示例

```gml
// 在控制对象的 Step 事件中：按 L 锁定/解锁 1 号分裂窗口的关闭按钮
if (keyboard_check_pressed(ord("L")))
{
    global.split_locked = !global.split_locked;
    qiumingdll_winsplit_set_closable(global.split_1, !global.split_locked);

    if (global.split_locked)
        show_debug_message("分裂窗口已锁定：用户无法关闭（程序仍可 destroy）");
}
```

## 相关函数

- [qiumingdll_winsplit_set_close_triggers_main](qiumingdll_winsplit_set_close_triggers_main.md)
- [qiumingdll_winsplit_set_titlebar](qiumingdll_winsplit_set_titlebar.md)
- [qiumingdll_winsplit_destroy](qiumingdll_winsplit_destroy.md)