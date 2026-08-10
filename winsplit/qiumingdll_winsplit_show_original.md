# qiumingdll_winsplit_show_original()

恢复显示被隐藏的原游戏窗口，恢复位置与隐藏前一致；与 hide_original 成对使用。

## 函数签名

```gml
qiumingdll_winsplit_show_original()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数，作用于 init 时记录的游戏主窗口 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 调用成功（若原窗口本就未隐藏，也返回 1，无副作用） |
| 0 | 原游戏窗口句柄无效（理论上仅当 init 后主窗口被销毁时发生）；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用。
- 与 `qiumingdll_winsplit_hide_original()` 成对使用，恢复后原窗口重新可见，其位置、尺寸、样式与隐藏前一致。
- 可以重复调用：未隐藏时调用不产生任何变化。
- 恢复显示不会影响分裂窗口，分裂窗口可以继续显示。
- 在 Win7 的"移到屏幕外"方案下，本函数会把窗口移回隐藏前记录的位置。
- 建议在游戏退出、或需要切换回"正常单窗口模式"时调用（清理流程也会自动恢复）。

## 示例

```gml
// 在控制对象的 Step 事件中：空格键在"分裂模式"与"单窗口模式"之间切换
if (keyboard_check_pressed(vk_space))
{
    global.split_mode = !global.split_mode;
    if (global.split_mode)
    {
        // 进入分裂模式：隐藏原窗口，只显示分裂窗口
        qiumingdll_winsplit_hide_original();
    }
    else
    {
        // 退出分裂模式：恢复原窗口显示
        qiumingdll_winsplit_show_original();
    }
}
```

## 相关函数

- [qiumingdll_winsplit_hide_original](qiumingdll_winsplit_hide_original.md)
- [qiumingdll_winsplit_cleanup](qiumingdll_winsplit_cleanup.md)
- [qiumingdll_winsplit_destroy_all](qiumingdll_winsplit_destroy_all.md)