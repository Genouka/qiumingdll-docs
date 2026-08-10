# qiumingdll_keeplive_cleanup()

卸载窗口保活的消息钩子，停止对目标窗口的保活保护，并清空内部记录的目标窗口状态。

## 函数签名

```gml
qiumingdll_keeplive_cleanup()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| （无返回值） | 本函数不返回数值；调用完毕后无需处理返回值。**非 Windows 平台**：包装层直接返回，不产生任何效果 |

## 使用说明

- 前置条件：无。即使未调用过 qiumingdll_keeplive_init()（钩子未安装），调用本函数也是安全的。
- 平台限制：仅 Windows 有效（非 Windows 平台包装函数直接返回，不做任何事）。
- 与 init 的对应：init 安装的钩子由本函数全部卸载；卸载后 qiumingdll_keeplive_is_active() 会返回 0。
- 调用时机：建议在游戏退出前、切换窗口模式（全屏 ↔ 窗口）或不需要保活保护的场景切换时调用。
- 行为细节：卸载后，目标窗口的关闭请求（标题栏×、Alt+F4 等系统命令）恢复正常处理；窗口也不再享受"无响应"豁免。
- 重复调用安全：重复卸载不会报错，只是没有更多可卸载的钩子。
- 通常全局清理流程会自动调用本函数；手动调用时注意不要与全局清理重复执行。
- 调试建议：卸载后可用 qiumingdll_keeplive_is_active() 验证已回到 0；若调用了 cleanup 却仍返回 1，说明还有其它保活实例在运行，请检查是否重复 init 过。

## 示例

```gml
/// 房间结束事件 (obj_keeplive_manager)
// 切换场景前关闭保活，避免钩子影响其他窗口逻辑
qiumingdll_keeplive_cleanup();

/// 游戏结束事件
// 游戏退出前的最终清理
qiumingdll_keeplive_cleanup();

/// 再次启用
// 需要保活时重新安装
if (needKeepAlive)
{
    qiumingdll_keeplive_init();
}
```

## 相关函数

- [qiumingdll_keeplive_init](qiumingdll_keeplive_init.md)
- [qiumingdll_keeplive_is_active](qiumingdll_keeplive_is_active.md)