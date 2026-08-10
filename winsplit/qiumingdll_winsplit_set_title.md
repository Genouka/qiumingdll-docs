# qiumingdll_winsplit_set_title(splitId, title)

设置指定分裂窗口标题栏上显示的标题文字（仅在有标题栏时可见）。

## 函数签名

```gml
qiumingdll_winsplit_set_title(splitId, title)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口 ID，取值 1 ~ 16，必须存在 |
| title | String | 是 | 要显示的标题文字，UTF-8 编码，支持中文；长度建议不超过几百字符 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 失败：splitId 无效或不存在；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用，且 splitId 对应的分裂窗口存在。
- 标题只在标题栏显示；若窗口当前无标题栏（`set_titlebar(splitId, false)`），设置标题不会有可见效果（内部仍会保存，重新开启标题栏后可见）。
- 设置后立即生效，标题栏会实时重绘。
- 创建时分裂窗口的默认标题为空字符串，不设置就没有标题。
- 中文可直接传入，无需转码（包装层按 UTF-8 传给 DLL）。
- 标题不影响任何逻辑行为（不参与关闭、拖动判断等），纯粹是显示用途。

## 示例

```gml
// 在控制对象的 Create 事件中创建分裂窗口后，立刻给它起个好记的名字
if (global.split_2 > 0)
{
    qiumingdll_winsplit_set_title(global.split_2, "副屏小地图");
    qiumingdll_winsplit_set_title(global.split_1, "第一视角画面");
}
```

```gml
// 随时改名，例如显示当前游戏场景名
qiumingdll_winsplit_set_title(global.split_1, "当前场景: " + room_get_name(room));
```

## 相关函数

- [qiumingdll_winsplit_set_titlebar](qiumingdll_winsplit_set_titlebar.md)
- [qiumingdll_winsplit_create](qiumingdll_winsplit_create.md)
- [qiumingdll_winsplit_set_closable](qiumingdll_winsplit_set_closable.md)