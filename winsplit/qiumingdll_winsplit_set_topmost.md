# qiumingdll_winsplit_set_topmost(splitId, topmost)

设置指定分裂窗口是否置顶显示（始终浮在其它窗口之上，包括游戏主窗口和其它程序窗口）。

## 函数签名

```gml
qiumingdll_winsplit_set_topmost(splitId, topmost)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口 ID，取值 1 ~ 16，必须存在 |
| topmost | Real/Bool | 是 | 是否置顶：非 0（true）= 置顶，0（false）= 取消置顶 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 失败：splitId 无效或不存在；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用，且 splitId 对应的分裂窗口存在。
- 分裂窗口创建时默认就带置顶样式（WS_EX_TOPMOST），即默认行为即"置顶"；通常无需额外调用本函数。
- topmost = 1 使窗口浮在所有窗口之上；topmost = 0 取消置顶，窗口参与普通层叠顺序（可被其他窗口盖住）。
- 取消置顶只影响 z 序，不影响窗口本身的位置、尺寸、内容。
- 置顶对多屏场景同样有效：置顶窗口始终浮在工作区最上方。
- 与操作系统的"窗口置顶"直觉一致：适合小地图、悬浮面板、控制台等需要始终可见的窗口。

## 示例

```gml
// 在控制对象的 Step 事件中：按 T 切换 1 号分裂窗口的置顶状态
if (keyboard_check_pressed(ord("T")))
{
    global.split_topmost = !global.split_topmost;
    qiumingdll_winsplit_set_topmost(global.split_1, global.split_topmost);
}
```

```gml
// 保证悬浮工具栏窗口永远在最上面
qiumingdll_winsplit_set_topmost(global.split_toolbar, true);
```

## 相关函数

- [qiumingdll_winsplit_create](qiumingdll_winsplit_create.md)
- [qiumingdll_winsplit_set_opacity](qiumingdll_winsplit_set_opacity.md)
- [qiumingdll_winsplit_set_draggable](qiumingdll_winsplit_set_draggable.md)