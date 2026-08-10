# qiumingdll_winsplit_get_info(splitId, infoType)

查询指定分裂窗口的运行状态：窗口位置、客户区尺寸、源区域数值。一次只能查询一项，由 infoType 指定。

## 函数签名

```gml
qiumingdll_winsplit_get_info(splitId, infoType)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口 ID，取值 1 ~ 16，必须存在 |
| infoType | Real | 是 | 要查询的项目，取值 0 ~ 7，含义见下表 |

infoType 取值：

| infoType | 含义 | 坐标系/单位 |
|----------|------|------------|
| 0 | 窗口左上角 X | 屏幕像素坐标 |
| 1 | 窗口左上角 Y | 屏幕像素坐标 |
| 2 | 客户区宽度 | 像素 |
| 3 | 客户区高度 | 像素 |
| 4 | 源区域 srcX | 原游戏窗口客户区像素 |
| 5 | 源区域 srcY | 原游戏窗口客户区像素 |
| 6 | 源区域 srcW | 像素 |
| 7 | 源区域 srcH | 像素 |

## 返回值

| 值 | 说明 |
|----|------|
| ≥ 0 | 查询结果，具体含义由 infoType 决定（窗口坐标、尺寸或源区域数值） |
| -1 | 查询失败：splitId 无效/不存在，或 infoType 不在 0~7 范围内；非 Windows 平台包装层直接返回 -1 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用，且 splitId 对应的分裂窗口存在。
- 0/1 读取的是窗口外框左上角（含标题栏）的实时屏幕坐标；用户拖动窗口后读取到的值与新位置一致。
- 2/3 读取的是客户区（画面显示区域）的实际尺寸，与 set_size/set_region 传入的 w/h 对应。
- 4~7 读取的是内部记录的源区域值，与最近一次 create 或 set_source_region 的设置一致。
- 如果只需要判断窗口是否存在，用 `qiumingdll_winsplit_exists` 更直接。

## 示例

```gml
// 在控制对象的 Step 事件中：按 F1 打印 1 号分裂窗口的全部状态
if (keyboard_check_pressed(vk_f1))
{
    var _x  = qiumingdll_winsplit_get_info(global.split_1, 0);
    var _y  = qiumingdll_winsplit_get_info(global.split_1, 1);
    var _w  = qiumingdll_winsplit_get_info(global.split_1, 2);
    var _h  = qiumingdll_winsplit_get_info(global.split_1, 3);
    var _sx = qiumingdll_winsplit_get_info(global.split_1, 4);
    var _sy = qiumingdll_winsplit_get_info(global.split_1, 5);
    var _sw = qiumingdll_winsplit_get_info(global.split_1, 6);
    var _sh = qiumingdll_winsplit_get_info(global.split_1, 7);

    show_debug_message("窗口位置: (" + string(_x) + ", " + string(_y) + ")");
    show_debug_message("客户区尺寸: " + string(_w) + " x " + string(_h));
    show_debug_message("源区域: (" + string(_sx) + ", " + string(_sy) + ") " + string(_sw) + " x " + string(_sh));
}
```

## 相关函数

- [qiumingdll_winsplit_exists](qiumingdll_winsplit_exists.md)
- [qiumingdll_winsplit_get_count](qiumingdll_winsplit_get_count.md)
- [qiumingdll_winsplit_set_position](qiumingdll_winsplit_set_position.md)
- [qiumingdll_winsplit_set_source_region](qiumingdll_winsplit_set_source_region.md)