# ime 模块

输入法管理模块。修复输入法与游戏的冲突，支持内联输入法状态轮询。

## 功能说明

- 禁用游戏窗口的 IME 组合窗口，防止输入法候选框遮挡游戏画面
- 切换输入法模式（中/英文）
- 内联输入法状态轮询，支持自定义输入法 UI

## 基础 API

### qmIMEFixConflict

```c
QM_EXPORT QM_Real qmIMEFixConflict(QM_String hwndParam);
```

**参数：**
- `hwndParam` - 窗口句柄（字符串形式），空字符串或"0"表示前台窗口

**返回值：**
- `0` - 成功
- `1` - 无效窗口句柄
- `2` - 无法获取 IME 上下文

**说明：**
- 禁用窗口的 IME 组合窗口
- 将组合窗口位置设为 (0,0)

---

### qmIMESwitch

```c
QM_EXPORT QM_Real qmIMESwitch(QM_Real action);
```

**参数：**
- `action` - 切换动作
  - `0` - 切换到英文模式
  - `1` - 切换到中文模式
  - `2` - 切换下一个输入法
  - `3` - 切换上一个输入法

**返回值：**
- `0` - 成功
- `1` - 无目标窗口
- `2` - 无法获取 IME 上下文
- `3` - 无效动作

---

### qmIMEGetMode

```c
QM_EXPORT QM_Real qmIMEGetMode();
```

**返回值：**
- `0` - 英文模式
- `1` - 中文模式
- `-1` - 获取失败

---

### qmIMESetInlinePosition

```c
QM_EXPORT QM_Real qmIMESetInlinePosition(QM_Real x, QM_Real y);
```

**参数：**
- `x, y` - 候选窗口在游戏窗口客户区中的位置

**返回值：**
- `0` - 成功
- `1` - 无目标窗口
- `2` - 无法获取 IME 上下文

**说明：**
- 启用内联模式
- 子类化窗口过程以拦截 IME 消息

---

### qmIMEResetInline

```c
QM_EXPORT QM_Real qmIMEResetInline();
```

**返回值：**
- `0` - 成功
- `1` - 无目标窗口

**说明：** 取消内联模式，恢复默认行为

## 内联输入法状态轮询 API

### 状态标志位

| 位 | 值 | 说明 |
|----|-----|------|
| 0 | 0x01 | 正在组合输入（持续状态） |
| 1 | 0x02 | 有新的提交文本（一次性） |
| 2 | 0x04 | 候选列表变化（一次性） |
| 3 | 0x08 | 输入模式变化（一次性） |

---

### qmIMEGetState

```c
QM_EXPORT QM_Real qmIMEGetState();
```

**返回值：** 状态标志位掩码

**说明：** 读取后清空一次性标志

---

### qmIMEGetCompositionText

```c
QM_EXPORT QM_String qmIMEGetCompositionText();
```

**返回值：** 当前组合文本（UTF-8）

**说明：** 仅在 `qmIMEGetState()` 返回包含 0x01 时有效

---

### qmIMEGetCompositionCursor

```c
QM_EXPORT QM_Real qmIMEGetCompositionCursor();
```

**返回值：** 组合文本中的光标位置（字符偏移）

---

### qmIMEGetCommitText

```c
QM_EXPORT QM_String qmIMEGetCommitText();
```

**返回值：** 提交文本（UTF-8）

**说明：** 读取后提交文本被清空

---

### qmIMEGetCandidateCount

```c
QM_EXPORT QM_Real qmIMEGetCandidateCount();
```

**返回值：** 候选列表中的候选数量

---

### qmIMEGetCandidate

```c
QM_EXPORT QM_String qmIMEGetCandidate(QM_Real index);
```

**参数：**
- `index` - 候选索引（从 0 开始）

**返回值：** 候选文本（UTF-8），索引无效时返回空字符串

---

### qmIMEGetCandidateSelection

```c
QM_EXPORT QM_Real qmIMEGetCandidateSelection();
```

**返回值：** 当前选中的候选索引，无选中时返回 -1

---

### qmIMEIsComposing

```c
QM_EXPORT QM_Real qmIMEIsComposing();
```

**返回值：**
- `1.0` - 正在组合
- `0.0` - 不在组合

---

### qmIMEPollJSON

```c
QM_EXPORT QM_String qmIMEPollJSON();
```

**返回值：** JSON 格式的完整 IME 状态

**JSON 格式：**
```json
{
  "composing": true,
  "compText": "组合文本",
  "compCursor": 0,
  "commitText": "提交文本",
  "candidates": ["候选1", "候选2"],
  "candidateSel": 0,
  "inputMode": 1,
  "stateFlags": 5
}
```

## 使用示例

```c
// 启用内联模式
qmIMESetInlinePosition(100, 200);

// 在游戏循环中轮询
int state = (int)qmIMEGetState();

if (state & 0x02) {
    // 有新的提交文本
    const char* text = qmIMEGetCommitText();
    // 处理输入文本
}

if (state & 0x04) {
    // 候选列表变化
    int count = (int)qmIMEGetCandidateCount();
    for (int i = 0; i < count; i++) {
        const char* candidate = qmIMEGetCandidate(i);
        // 显示候选
    }
}

// 或者使用 JSON 一次性获取所有状态
const char* json = qmIMEPollJSON();
// 解析 JSON 获取完整状态

// 取消内联模式
qmIMEResetInline();
```
