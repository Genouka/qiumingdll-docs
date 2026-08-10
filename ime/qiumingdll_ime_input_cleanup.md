# qiumingdll_ime_input_cleanup()

清理输入框资源：销毁候选列表 ds_list，DLL 模式下取消内联模式。

## 函数签名

```gml
qiumingdll_ime_input_cleanup()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不需要任何参数 |

## 返回值

无返回值（本函数不返回任何值）。

## 使用说明

- 在对象的 Clean Up 事件（Destroy 事件）中调用，与 `qiumingdll_ime_input_create` 成对使用；任何创建过输入框的实例销毁时都应调用，防止 ds_list 泄漏。
- 内部行为：
  1. 销毁 `ime_cand_list`（ds_list）；
  2. 若为 DLL 模式（`ime_use_dll == true`），自动调用 `qiumingdll_ime_reset_inline()` 取消内联，恢复系统默认输入法行为并清空全部 IME 状态。
- 重复调用安全：`ime_cand_list` 已通过 `ds_exists` 检查后再销毁；但正常用法还是仅调用一次。
- 回调脚本（`ime_on_*`）不需要额外释放（脚本资源由引擎管理；若传的是方法变量也无须释放）。
- 非 Windows 平台同样需要调用（回退模式也创建了 ds_list）。
- 注意：如果在销毁实例前还想保留 `ime_text` 内容，请先在别处保存；本函数不保存文本。

## 示例

```gml
// Clean Up 事件：释放输入框资源
qiumingdll_ime_input_cleanup();
```

```gml
// 手动销毁场景：不再需要输入框时
// 先取走文本（如果需要）
saved_text = ime_text;
qiumingdll_ime_input_cleanup();
instance_destroy();
```

## 相关函数

- [qiumingdll_ime_input_create](qiumingdll_ime_input_create.md)
- [qiumingdll_ime_reset_inline](qiumingdll_ime_reset_inline.md)
- [qiumingdll_ime_poll_destroy](qiumingdll_ime_poll_destroy.md)