# qiumingdll_ime_poll_destroy(map)

销毁 `qiumingdll_ime_poll()` 返回的 ds_map，并同时销毁其中的候选列表 ds_list。

## 函数签名

```gml
qiumingdll_ime_poll_destroy(map)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| map | ds_map | 是 | `qiumingdll_ime_poll()` 返回的 ds_map |

## 返回值

无返回值（本函数不返回任何值）。

## 使用说明

- 平台限制：所有平台可用（非 Windows 下 `qiumingdll_ime_poll` 返回空 ds_map，同样需要用它销毁）。
- 必须与 `qiumingdll_ime_poll` 成对使用：每次 poll 返回的 ds_map 都必须在确认不再需要后调用本函数释放，否则会持续泄漏内存（ds_map + 内部 ds_list 两个层级）。
- 内部行为：若 map 中存在 "candidates" 键，先销毁对应的 ds_list，再销毁 ds_map 本身；对不存在的 map（`ds_map_exists` 为 false）调用会被安全忽略。
- 只应销毁由 `qiumingdll_ime_poll` 返回的 map；用其他来源（如 `json_parse`）得到的相似结构请用对应的常规销毁方式。
- 注意不要对同一个 map 重复销毁，也不要销毁后继续使用其中的 ds_list 引用。

## 示例

```gml
var m = qiumingdll_ime_poll();

// ... 使用 m 中的各项数据 ...

qiumingdll_ime_poll_destroy(m); // 记得销毁，防内存泄漏
```

```gml
// 配合每帧轮询的标准写法
repeat (2) { // 演示：循环中的正确用法
    var m = qiumingdll_ime_poll();
    // 读取数据 ...
    qiumingdll_ime_poll_destroy(m);
}
```

## 相关函数

- [qiumingdll_ime_poll](qiumingdll_ime_poll.md)
- [qiumingdll_ime_poll_json](qiumingdll_ime_poll_json.md)