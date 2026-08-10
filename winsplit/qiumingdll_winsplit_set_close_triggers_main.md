# qiumingdll_winsplit_set_close_triggers_main(splitId, triggers)

设置当用户关闭该分裂窗口时，是否连带关闭原游戏主窗口（联动关闭）。

## 函数签名

```gml
qiumingdll_winsplit_set_close_triggers_main(splitId, triggers)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口 ID，取值 1 ~ 16，必须存在 |
| triggers | Real/Bool | 是 | 是否联动：非 0（true）= 用户关闭该分裂窗口时主窗口一同关闭（默认），0（false）= 只关分裂窗口，不影响主窗口 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 失败：splitId 无效或不存在；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用，且 splitId 对应的分裂窗口存在。
- 创建时默认 `closeTriggersMain = true`（关闭分裂窗口会连主窗口一起关）。
- 联动只在"用户关闭"路径触发（标题栏 X、系统菜单关闭）；程序调用 destroy / destroy_all / cleanup 不会触发联动。
- 用户在分裂窗口点击关闭时，分裂窗口先销毁，随后向主游戏窗口发送关闭请求——这通常意味着游戏退出。若游戏设置了"关闭确认/存档提示"，提示会照常出现。
- 多分裂窗口场景建议：至少保留一个"退出入口"（触发的那个），其余设为 false，避免用户手滑直接退出游戏。
- 与 `qiumingdll_winsplit_set_closable` 配合：closable=false 时根本不会走到联动逻辑。

## 示例

```gml
// 在控制对象的 Create 事件中建立分裂窗口后配置联动行为：
// 1 号窗口作为"退出闸口"（保留默认联动），2 号窗口关闭时不联动
if (global.split_2 > 0)
    qiumingdll_winsplit_set_close_triggers_main(global.split_2, false);
```

```gml
// 在控制对象的 Step 事件中：按 E 切换 1 号分裂窗口的联动开关
if (keyboard_check_pressed(ord("E")))
{
    global.split_link_main = !global.split_link_main;
    qiumingdll_winsplit_set_close_triggers_main(global.split_1, global.split_link_main);
}
```

## 相关函数

- [qiumingdll_winsplit_set_closable](qiumingdll_winsplit_set_closable.md)
- [qiumingdll_winsplit_set_titlebar](qiumingdll_winsplit_set_titlebar.md)
- [qiumingdll_winsplit_destroy](qiumingdll_winsplit_destroy.md)