# qiumingdll_procdetect_multiinstance()

检测当前系统中是否存在多个游戏进程实例。

## 函数签名

```gml
qiumingdll_procdetect_multiinstance()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 检测到除当前进程外还有其他同名游戏进程在运行（多开） |
| 0 | 未检测到多开，或非 Windows 平台 / 未初始化（此时返回 0） |

## 使用说明

- 前置条件：Windows 平台需先调用 `qiumingdll_init()`。
- 平台限制：仅 Windows。
- 行为细节：通过当前可执行文件名（exe 名）在系统进程列表中进行匹配，从而判断是否被多开。
- 注意：若玩家通过修改 exe 文件名的方式多开，本函数可能无法识别；检测结果只在调用瞬间有效。

## 示例

```gml
/// 游戏启动时检查
qiumingdll_init();
if (qiumingdll_procdetect_multiinstance())
{
    show_message("检测到游戏已多开，是否继续？");
}
```

## 相关函数

- [qiumingdll_procdetect_cheatengine](qiumingdll_procdetect_cheatengine.md)
- [qiumingdll_procdetect_streaming](qiumingdll_procdetect_streaming.md)
- [qiumingdll_procdetect_process](qiumingdll_procdetect_process.md)