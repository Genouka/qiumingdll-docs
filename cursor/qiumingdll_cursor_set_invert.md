# qiumingdll_cursor_set_invert(enable)

开启或关闭"光标与鼠标移动相反"效果。开启后，整个系统（不止游戏窗口）中的光标都会朝鼠标物理移动的相反方向移动。

## 函数签名

```gml
qiumingdll_cursor_set_invert(enable)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| enable | Real | 是 | 非 0 = 开启效果；0 = 关闭效果并还原 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 调用后效果处于开启状态 |
| 0 | 调用后效果处于关闭状态（关闭成功，或开启失败——例如系统拒绝了全局钩子安装） |

## 使用说明

- 前置条件：Windows 平台需先调用 `qiumingdll_init()`。
- 平台限制：仅 Windows。
- 行为细节：
  - 开启瞬间会记录当前光标位置作为"还原点"；关闭效果（或自动还原）时光标会被放回该位置。
  - 通过 `WH_MOUSE_LL` 全局钩子实现，作用范围是整个系统，包括其他程序；请勿在玩家不知情的情况下长时间开启。
  - 光标移动到屏幕边缘时会**环绕**到另一侧继续反向移动，避免光标卡死在边缘。
  - 游戏内通过 `mouse_x` / `mouse_y` 读取到的也是反向后的位置；使用 Raw Input 直读硬件位移的程序不受影响。
- 取消方式（任选其一）：
  - 再次调用 `qiumingdll_cursor_set_invert(0)`；
  - 效果生效期间，在 **1.5 秒内连按 8 次 F12**（全局热键，无需游戏窗口获得焦点，两次按键间隔超过 1.5 秒则重新计数）；
  - DLL 被卸载（`qiumingdll_free()`）或游戏进程退出时**自动还原**，不会残留任何系统级修改。
- 注意：本函数会影响真实系统光标，建议只在明确告知玩家或作为可控彩蛋时使用；按下 F12 的安全阀无法被游戏代码禁用。

## 示例

```gml
/// 恶作剧机关：踩到地雷后反向 5 秒
if (place_meeting(x, y, obj_trap)) {
    qiumingdll_cursor_set_invert(1);   // 返回 1，已开启
    alarm[0] = room_speed * 5;
}

/// （Alarm 0 事件）
qiumingdll_cursor_set_invert(0);       // 还原光标位置
show_message("你已恢复正常移动！");
```

```gml
// 玩家随时可以自救：效果生效期间快速按 8 次 F12 即可取消
if (qiumingdll_cursor_get_invert()) {
    draw_text(8, 8, "提示：连按 8 次 F12 解除反向移动");
}
```

## 相关函数

- [qiumingdll_cursor_get_invert](qiumingdll_cursor_get_invert.md)
