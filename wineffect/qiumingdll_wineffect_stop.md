# qiumingdll_wineffect_stop()

立即停止窗口特效，并把颤动/扭曲/撕裂三种强度清零，恢复窗口位置和原始区域。

## 函数签名

```gml
qiumingdll_wineffect_stop()
```

## 参数说明

无参数。

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 已停止并还原 |

## 使用说明

- 与 `set_enabled(0)` 的区别：本函数还会把三种强度全部清零，适合"彻底结束演出"。
- 停止后仍保持窗口绑定；可以重新设置强度并再次 `set_enabled(1)`。
- 如果尚未初始化，调用本函数也是安全的（直接返回 1）。

## 示例

```gml
/// 强制结束所有窗口特效
qiumingdll_wineffect_stop();
```

## 相关函数

- [qiumingdll_wineffect_set_enabled](qiumingdll_wineffect_set_enabled.md)
- [qiumingdll_wineffect_cleanup](qiumingdll_wineffect_cleanup.md)
- [qiumingdll_wineffect_get_state](qiumingdll_wineffect_get_state.md)
