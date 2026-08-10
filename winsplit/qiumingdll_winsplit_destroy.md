# qiumingdll_winsplit_destroy(splitId)

销毁指定的分裂窗口：关闭窗口、释放其占用的槽位和形状资源，窗口 ID 随后可被新建的分裂窗口复用。

## 函数签名

```gml
qiumingdll_winsplit_destroy(splitId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 要销毁的分裂窗口 ID，取值 1 ~ 16，必须是 qiumingdll_winsplit_create 返回且仍存在的 ID |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 销毁成功（或该窗口已被销毁但 ID 曾有效） |
| 0 | 销毁失败：splitId 无效（不在 1~16 范围，或该槽位本就不活跃）；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用，且 splitId 对应的分裂窗口存在。
- 销毁后该 ID 立即失效，`qiumingdll_winsplit_exists` 返回 0；不要再对已销毁的 ID 调用任何函数。
- 销毁时若有进行中的动画（位置/尺寸动画、路径动画、批处理动画），会自动停止并清除。
- 销毁不会影响其他分裂窗口，也不会影响原游戏窗口。
- 这是程序化的销毁通道：即使用户关闭了分裂窗口的标题栏 X（触发自身销毁和可能的联动关闭），内部槽位也会被释放，之后同样可复用。

## 示例

```gml
// 在控制对象的 Step 事件中：按 Backspace 销毁 1 号分裂窗口
if (keyboard_check_pressed(vk_backspace))
{
    if (global.split_1 > 0)
    {
        if (qiumingdll_winsplit_destroy(global.split_1) == 1)
        {
            global.split_1 = 0; // 置 0 避免后续误用
            show_debug_message("1 号分裂窗口已销毁");
        }
    }
}
```

## 相关函数

- [qiumingdll_winsplit_create](qiumingdll_winsplit_create.md)
- [qiumingdll_winsplit_destroy_all](qiumingdll_winsplit_destroy_all.md)
- [qiumingdll_winsplit_exists](qiumingdll_winsplit_exists.md)
- [qiumingdll_winsplit_get_count](qiumingdll_winsplit_get_count.md)