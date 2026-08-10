# qiumingdll_keeplive_init()

安装"窗口保活"消息钩子，防止目标窗口被系统判定为"无响应"而被关闭或清理，用于网页版游戏的全屏/无响应保护。

## 函数签名

```gml
qiumingdll_keeplive_init()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要 GML 参数。包装层会自动把主游戏窗口句柄 `window_handle()` 传给 DLL，目标窗口即为游戏主窗口 |

## 返回值

| 值 | 说明 |
|----|------|
| 0 | 成功：已为目标窗口安装保活钩子 |
| 1 | 失败：传入的窗口句柄无效或无法获取目标窗口所属线程。**非 Windows 平台**：包装层直接返回，不产生任何效果（实际不返回有效值，请仅按 Windows 场景处理） |

## 使用说明

- 前置条件：无；只能在 Windows 平台上生效，通常建议游戏主窗口已经创建后再调用（如对象的创建事件或房间开始事件）。
- 平台限制：仅 Windows 有效。钩子绑定在游戏主窗口所属线程上，处理该窗口的消息泵。
- 保活机制：钩子会拦截目标窗口的部分消息（如 WM_PAINT、WM_ERASEBKGND、WM_SETCURSOR 等）进行特殊处理，并吞掉系统菜单/标题栏的关闭命令（WM_SYSCOMMAND SC_CLOSE），避免窗口因长时间不回应用户操作而被系统判定"无响应"从而被终止。典型场景：网页版游戏（配合 WebView）进入全屏、长时间无操作或主线程繁忙时防止 Windows 弹出"未响应"提示并将其关闭。
- 重复调用：再次调用会重新安装钩子（同一窗口重复安装安全，但更推荐先 cleanup 再 init）。
- 退出游戏前应调用 qiumingdll_keeplive_cleanup() 卸载钩子；游戏被关闭时钩子会在窗口销毁后自动失效。
- 副作用：保活期间系统向目标窗口发送的关闭请求可能被吞掉，玩家用 Alt+F4 / 标题栏关闭游戏时请确保游戏逻辑里有自己的退出途径。

## 示例

```gml
/// 创建事件 (obj_keeplive_manager)
// 游戏主窗口创建后启用保活
var r = qiumingdll_keeplive_init();
if (r == 0)
{
    keepliveOn = true; // 保活钩子已安装
}

/// 房间结束事件
// 离开房间或游戏退出前卸载钩子
if (keepliveOn)
{
    qiumingdll_keeplive_cleanup();
    keepliveOn = false;
}

/// Draw GUI 事件（调试显示）
if (qiumingdll_keeplive_is_active() == 1)
{
    draw_text(10, 10, "窗口保活：已启用");
}
else
{
    draw_text(10, 10, "窗口保活：未启用");
}
```

## 相关函数

- [qiumingdll_keeplive_cleanup](qiumingdll_keeplive_cleanup.md)
- [qiumingdll_keeplive_is_active](qiumingdll_keeplive_is_active.md)