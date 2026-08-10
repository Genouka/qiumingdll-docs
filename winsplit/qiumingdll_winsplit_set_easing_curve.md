# qiumingdll_winsplit_set_easing_curve(splitId, curve)

设置指定分裂窗口的缓动曲线，该曲线将应用于该窗口后续所有普通动画（位置/尺寸/区域/路径动画）。

## 函数签名

```gml
qiumingdll_winsplit_set_easing_curve(splitId, curve)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口编号，从 1 开始，最大 16（与 qiumingdll_winsplit_create 返回的编号一致） |
| curve | Real | 是 | 缓动曲线枚举，取值范围 0~11，含义见下表 |

缓动曲线枚举（与 `qiumingdll_winsplit_batch_set_easing` 共用同一套枚举）：

| 值 | 名称 | 说明 |
|----|------|------|
| 0 | linear | 线性，全程匀速 |
| 1 | ease-in | 二次方缓入（先慢后快） |
| 2 | ease-out | 二次方缓出（先快后慢） |
| 3 | ease-in-out | 二次方缓入缓出 |
| 4 | in-cubic | 三次方缓入 |
| 5 | out-cubic | 三次方缓出 |
| 6 | in-out-cubic | 三次方缓入缓出 |
| 7 | in-back | 过冲回拉的缓入（先反向再冲过目标） |
| 8 | out-back | 过冲回拉的缓出（冲过目标再回摆） |
| 9 | in-out-back | 过冲回拉的缓入缓出 |
| 10 | bounce-out | 弹跳缓出（落地弹跳几次） |
| 11 | elastic-out | 弹性缓出（弹性震荡收敛） |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | splitId 无效（不在 1~16 范围或该分裂窗口不存在）；或非 Windows 平台（GML 包装的回退返回值） |

## 使用说明

- 前置条件：必须先调用 qiumingdll_winsplit_init() 初始化，再用 qiumingdll_winsplit_create() 创建分裂窗口。
- 平台限制：仅 Windows；其他平台该 GML 包装直接返回 0。
- 该设置是持久状态：创建窗口后、开始动画前设置一次即可，之后调用 set_position_animate / set_size_animate / set_region_animate / move_path_animate 都会沿用该曲线，直到再次修改。
- 默认曲线为 ease-in-out（值 3），不调用本函数时动画也使用该默认值。
- 只影响该窗口的普通动画，不影响批处理动画；批处理需要用 qiumingdll_winsplit_batch_set_easing 单独设置（不过 batch_begin 会把窗口当前的曲线作为批处理初始曲线）。
- 不要传入 0~11 之外的值，内部按整型直接赋值，越界值行为未定义。

## 示例

```gml
// Create 事件：创建分裂窗口并配置弹跳缓出曲线
qiumingdll_winsplit_init();

global.splitId = qiumingdll_winsplit_create(0, 0, 640, 480, 100, 100, 320, 240);
if (global.splitId > 0)
{
    qiumingdll_winsplit_set_easing_curve(global.splitId, 10);  // bounce-out
}

// 按键事件：触发位置动画，将使用 bounce-out 曲线飞出
if (keyboard_check_pressed(vk_space))
{
    qiumingdll_winsplit_set_position_animate(global.splitId, 800, 600, 1000, 16);
}
```

## 相关函数

- [qiumingdll_winsplit_set_src_anim_mode](qiumingdll_winsplit_set_src_anim_mode.md)
- [qiumingdll_winsplit_set_position_animate](qiumingdll_winsplit_set_position_animate.md)
- [qiumingdll_winsplit_set_size_animate](qiumingdll_winsplit_set_size_animate.md)
- [qiumingdll_winsplit_set_region_animate](qiumingdll_winsplit_set_region_animate.md)
- [qiumingdll_winsplit_move_path_animate](qiumingdll_winsplit_move_path_animate.md)
- [qiumingdll_winsplit_batch_set_easing](qiumingdll_winsplit_batch_set_easing.md)