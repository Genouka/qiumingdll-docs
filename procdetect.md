# procdetect 模块

进程检测模块。检测系统中是否运行特定类型的程序。

## API

### qmProcDetectCheatEngine

```c
QM_EXPORT QM_Real qmProcDetectCheatEngine();
```

**返回值：**
- `1.0` - 检测到调试/作弊工具
- `0.0` - 未检测到

**检测列表：**
- Cheat Engine (各种版本)
- x64dbg, x32dbg, x96dbg
- OllyDbg, OllyIce
- WinDbg
- IDA Pro (各种版本)
- Process Hacker
- Process Monitor
- Process Explorer
- ArtMoney
- Game Conqueror
- ScanMem
- Ghidra

---

### qmProcDetectStreaming

```c
QM_EXPORT QM_Real qmProcDetectStreaming();
```

**返回值：**
- `1.0` - 检测到录屏/直播软件
- `0.0` - 未检测到

**检测列表：**
- OBS Studio
- oCam
- Bandicam
- XSplit
- Streamlabs OBS
- Action!
- Fraps
- Dxtory
- NVIDIA ShadowPlay
- GameCapture
- Streamlink
- vMix
- Wirecast
- Camtasia
- ShareX
- Loom
- 等等

---

### qmProcDetectMultiInstance

```c
QM_EXPORT QM_Real qmProcDetectMultiInstance();
```

**返回值：** 当前进程的实例数量

**说明：** 检测游戏是否运行了多个实例

---

### qmProcDetectProcess

```c
QM_EXPORT QM_Real qmProcDetectProcess(QM_String processName);
```

**参数：**
- `processName` - 要检测的进程名（不区分大小写）

**返回值：**
- `1.0` - 检测到
- `0.0` - 未检测到
- `-1.0` - 参数无效

**使用示例：**
```c
// 检测特定进程
if (qmProcDetectProcess("notepad.exe")) {
    // 检测到记事本
}

// 检测作弊工具
if (qmProcDetectCheatEngine()) {
    // 检测到作弊工具，可以采取措施
}

// 检测多开
int instances = qmProcDetectMultiInstance();
if (instances > 1) {
    // 游戏多开了
}
```
