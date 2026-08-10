# qiumingdll_winsplit_hide(splitId)

隐藏指定的分裂窗口，不影响其内部状态；之后可以随时用 show 重新显示。

## 函数签名

```gml
qiumingdll_winsplit_hide(splitId)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| splitId | Real | 是 | 分裂窗口 ID，取值 1 ~ 16，必须存在 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 隐藏成功 |
| 0 | 失败：splitId 无效或不存在；非 Windows 平台包装层直接返回 0 |

## 使用说明

- 前置条件：`qiumingdll_winsplit_init()` 已成功调用，且 splitId 对应的分裂窗口存在。
- 隐藏只是不显示，窗口仍然"存活"：`qiumingdll_winsplit_exists` 仍返回 1，也不算在可复用槽位里；位置、大小、源区域、形状等设置全部保留。
- 与销毁（destroy）的区别：hide 可逆，destroy 不可逆且释放槽位。
- 隐藏不会隐藏原游戏窗口，两者互不相干。

## 示例

```gml
// 剧情演出时隐藏所有分裂窗口，演出结束后恢复显示
// （例如场景管理器对象的某个脚本中）

// 隐藏
qiumingdll_winsplit_hide(global.split_1);
qiumingdll_winsplit_hide(global.split_2);

// ……若干秒后演出结束：恢复所有分裂窗口显示
qiumingdll_winsplit_show(global.split_1);
qiumingdll_winsplit_show(global.split_2);
```

## 相关函数

- [qiumingdll_winsplit_show](qiumingdll_winsplit_show.md)
- [qiumingdll_winsplit_destroy](qiumingdll_winsplit_destroy.md)
- [qiumingdll_winsplit_hide_original](qiumingdll_winsplit_hide_original.md)