# qiumingdll_winsplit_destroy_all()

一次性销毁当前存在的所有分裂窗口，常用于场景切换、返回标题画面等需要"清屏"的场合。

## 函数签名

```gml
qiumingdll_winsplit_destroy_all()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 调用成功（无论当时有多少个分裂窗口；没有分裂窗口时也是 1） |
| 0 | 非 Windows 平台，包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用；未初始化时调用本函数不影响原窗口。
- 作用等价于对所有现存分裂窗口逐个调用 `qiumingdll_winsplit_destroy`。
- 销毁完成后 `qiumingdll_winsplit_get_count()` 返回 0；所有 splitId 均失效，`qiumingdll_winsplit_exists` 全部返回 0。
- 注意：本函数只销毁分裂窗口，不恢复原游戏窗口。若原窗口此前被隐藏，需要另行调用 `qiumingdll_winsplit_show_original()` 恢复显示。
- 销毁窗口不会发送关闭消息给主窗口（不触发 closeTriggersMain 联动）。

## 示例

```gml
// 在控制对象的 Step 事件中：按 Delete 清空全部分裂窗口
if (keyboard_check_pressed(vk_delete))
{
    qiumingdll_winsplit_destroy_all();

    // 清空本地记录的 ID，避免误用
    global.split_1 = 0;
    global.split_2 = 0;
    global.split_3 = 0;

    // 如果原窗口之前被隐藏，现在恢复显示
    qiumingdll_winsplit_show_original();
}
```

## 相关函数

- [qiumingdll_winsplit_destroy](qiumingdll_winsplit_destroy.md)
- [qiumingdll_winsplit_create](qiumingdll_winsplit_create.md)
- [qiumingdll_winsplit_get_count](qiumingdll_winsplit_get_count.md)
- [qiumingdll_winsplit_show_original](qiumingdll_winsplit_show_original.md)