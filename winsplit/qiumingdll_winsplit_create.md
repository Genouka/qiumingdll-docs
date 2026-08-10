# qiumingdll_winsplit_create(srcX, srcY, srcW, srcH, dstX, dstY, dstW, dstH)

创建一个分裂窗口：把原游戏窗口客户区内指定的一块像素区域（源区域）实时显示在一个新的顶层窗口中，并返回该分裂窗口的 ID。

## 函数签名

```gml
qiumingdll_winsplit_create(srcX, srcY, srcW, srcH, dstX, dstY, dstW, dstH)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| srcX | Real | 是 | 源区域左上角 X，像素，相对原游戏窗口客户区（原窗口客户区左上角为 0,0），取值 0 ~ 原窗口客户区宽度 |
| srcY | Real | 是 | 源区域左上角 Y，像素，相对原游戏窗口客户区，取值 0 ~ 原窗口客户区高度 |
| srcW | Real | 是 | 源区域宽度，像素，必须大于 0；建议不超出原窗口客户区右边界 |
| srcH | Real | 是 | 源区域高度，像素，必须大于 0；建议不超出原窗口客户区下边界 |
| dstX | Real | 是 | 分裂窗口在屏幕上的左上角 X，像素，屏幕坐标（主显示器左上角为 0,0） |
| dstY | Real | 是 | 分裂窗口在屏幕上的左上角 Y，像素，屏幕坐标 |
| dstW | Real | 是 | 分裂窗口客户区宽度，像素（不含标题栏等边框，边框会额外向外扩展） |
| dstH | Real | 是 | 分裂窗口客户区高度，像素（不含标题栏等边框） |

源区域（srcX/srcY/srcW/srcH）在原游戏窗口客户区内，决定"显示什么"；目标区域（dstX/dstY/dstW/dstH）在屏幕上，决定"显示在哪、多大"。源区域内容会被拉伸到目标尺寸。

## 返回值

| 值 | 说明 |
|----|------|
| 1 ~ 16 | 创建成功，返回该分裂窗口的 ID（splitId），后续所有操作都以它为参数 |
| 0 | 创建失败：模块未初始化、窗口槽位已满（同时最多 16 个），或系统窗口创建失败；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 必须已成功调用（返回 0）。
- splitId 从 1 开始编号，不是 0；最多同时存在 16 个分裂窗口。被销毁的槽位会被后续创建自动复用，因此 ID 不保证连续递增。
- 创建即显示，无需再调用 show。
- 创建时默认属性：可拖动 `draggable=false`、有标题栏 `hasTitleBar=true`、可关闭 `closable=true`、关闭时联动主窗口 `closeTriggersMain=true`。均可通过对应 set 函数修改。
- srcW/srcH 与源区域重叠允许（多个分裂窗口可显示同一块区域）。
- 若源区域超出原窗口客户区边界，超出的部分没有画面内容，分裂窗口将显示为空白/黑色。
- 隐藏原窗口后分裂窗口依然正常渲染显示，二者互不影响。

## 示例

```gml
// 在控制对象的 Create 事件中：把主窗口客户区平均分成四块，各自独立显示
if (global.winsplit_ready == true)
{
    var _cw = window_get_width();   // 主窗口客户区宽
    var _ch = window_get_height();  // 主窗口客户区高
    var _hw = _cw div 2;
    var _hh = _ch div 2;

    // 左上角一块：显示在主窗口右上方
    global.split_1 = qiumingdll_winsplit_create(0, 0, _hw, _hh, _cw + 20, 50, _hw, _hh);
    // 右上角一块：显示在主窗口右下方
    global.split_2 = qiumingdll_winsplit_create(_hw, 0, _cw - _hw, _hh, _cw + 20, 50 + _hh + 30, _hw, _hh);
    // 左下角一块：显示在副屏（若存在）
    global.split_3 = qiumingdll_winsplit_create(0, _hh, _hw, _ch - _hh, 0, 0, _hw, _hh);

    if (global.split_1 == 0)
        show_debug_message("分裂窗口创建失败：可能槽位已满或未初始化");
}
```

## 相关函数

- [qiumingdll_winsplit_init](qiumingdll_winsplit_init.md)
- [qiumingdll_winsplit_destroy](qiumingdll_winsplit_destroy.md)
- [qiumingdll_winsplit_destroy_all](qiumingdll_winsplit_destroy_all.md)
- [qiumingdll_winsplit_set_source_region](qiumingdll_winsplit_set_source_region.md)
- [qiumingdll_winsplit_set_region](qiumingdll_winsplit_set_region.md)
- [qiumingdll_winsplit_hide_original](qiumingdll_winsplit_hide_original.md)