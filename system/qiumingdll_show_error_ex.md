# qiumingdll_show_error_ex(title, message, buttons_json)

弹出完全可自定义的阻塞式错误对话框：标题、正文、按钮文本、按钮行为、按钮背景色/文字颜色均可配置。

## 函数签名

```gml
qiumingdll_show_error_ex(title, message, buttons_json)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| title | String | 是 | 窗口标题，UTF-8 任意文本。传 `""` 可显示空标题 |
| message | String | 是 | 错误正文，UTF-8 任意文本，支持 `\r\n` / `\n` 多行 |
| buttons_json | String | 是 | 按钮配置的 **JSON 字符串**。可传 JSON 数组，也可传包含 `buttons` 等字段的配置对象；传 `""` 时使用默认的 Abort / Ignore / Copy / Clear 四个按钮 |

> `buttons_json` 是字符串而不是数组/结构体。GMS 2.3+ 可先 `json_stringify(数组或结构体)` 再传入；旧版 GameMaker 直接传手写 JSON 文本。

## 返回值

| 值 | 说明 |
|----|------|
| 按钮的 `result` | 点击了 `action = "close"` 的按钮。未显式配置 `result` 时默认为按钮下标 + 1 |
| `closeResult`（默认 `2`，即 IDCANCEL） | 点击标题栏 X、按 Esc（且没有 `cancel` 按钮）或外部关闭窗口时返回 |
| `cancel` 按钮的 `result` | 存在 `cancel = true` 的按钮时，按 Esc 会触发该按钮的行为并返回其结果 |
| `0` | 窗口创建失败（极少发生，例如窗口类注册失败） |
| 无返回值 | `action = "exit"` 的按钮会直接结束进程，不会返回 |

## buttons_json 格式

### 最简形式：字符串数组

```json
["确定", "取消"]
```

每个字符串会生成一个 `action = "close"` 的按钮，返回值分别为 `1`、`2`。

### 按钮对象数组

```json
[
  { "text": "退出游戏", "action": "exit", "exitCode": 1, "bgColor": "#B71C1C", "fgColor": "#FFFFFF" },
  { "text": "忽略", "action": "close", "result": 5, "bgColor": "#2E7D32" }
]
```

### 完整配置对象

```json
{
  "title": "存档损坏",
  "message": "无法读取 save.dat。\n可以忽略并尝试恢复默认存档。",
  "width": 720,
  "height": 420,
  "closeResult": 2,
  "readOnly": true,
  "icon": "warning",
  "buttons": [
    { "text": "退出", "action": "exit", "exitCode": 1, "bgColor": "#B71C1C" },
    { "text": "忽略", "action": "close", "result": 5, "bgColor": "#2E7D32" }
  ]
}
```

配置对象中的 `title` / `message` 会覆盖函数参数；未出现的字段保持默认值。

### 顶层字段

| 字段 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| title | String | 函数参数 | 窗口标题，覆盖第一个参数 |
| message | String | 函数参数 | 错误正文，覆盖第二个参数 |
| width | Number | `800` | 窗口外部宽度（像素），最小 320，最大 8000；按钮放不下时会自动加宽 |
| height | Number | `600` | 窗口外部高度（像素），最小 220，最大 8000 |
| closeResult | Number | `2` | 点击 X / 按 Esc（无 cancel 按钮）/ 外部关闭时的返回值 |
| readOnly | Boolean | `true` | 正文是否只读；`false` 时玩家可以编辑正文 |
| icon | String | `"error"` | 标题栏图标：`"error"`、`"warning"`、`"info"`、`"question"`、`"none"` |
| buttons | Array | 默认四按钮 | 按钮数组；传 `[]` 表示不显示按钮（只能靠标题栏关闭） |

### 按钮字段

| 字段 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| text | String | `"OK"` | 按钮文本，UTF-8 任意文本 |
| action | String | `"close"` | 按钮行为，见下表 |
| result | Number | 下标 + 1 | `action = "close"` 时的返回值 |
| exitCode | Number | `1` | `action = "exit"` 时传给进程退出码 |
| bgColor | String / Number | 系统按钮色 | 按钮背景色，规则见下 |
| fgColor | String / Number | 自动黑白 | 按钮文字颜色，规则见下 |
| width | Number | 按文字自适应 | 按钮宽度（像素），限制 40~800 |
| enabled | Boolean | `true` | 是否启用；禁用后点击无效果 |
| default | Boolean | `false` | 是否为默认按钮（回车触发）；多个时只有第一个生效 |
| cancel | Boolean | `false` | 是否为取消按钮（Esc 触发）；多个时只有第一个生效 |

`bgColor` / `fgColor` 同时支持别名 `bg` / `background` 和 `fg` / `textColor`。

### action 行为

| action | 行为 |
|--------|------|
| `"close"` | 关闭对话框并返回 `result`（默认下标 + 1） |
| `"exit"` | 关闭对话框并以 `exitCode` 结束进程（默认 1），**不会返回** |
| `"copy"` | 把正文全部复制到剪贴板，对话框保持打开 |
| `"clear"` | 清空正文，对话框保持打开 |
| `"none"` | 什么也不做，对话框保持打开 |

`action` 也接受 `"abort"` / `"quit"`（等同 `exit`）和 `"noop"`（等同 `none`）。

### 颜色格式

- 字符串：`"#RRGGBB"` 或 `"#AARRGGBB"`（网页格式，Alpha 会被忽略）。
- 数字：按 Windows `COLORREF` / GML `make_color_rgb()` 的 `0x00BBGGRR` 解释。例如 `make_color_rgb(255, 0, 0)`、`255` 都表示红色。
- 只设置 `bgColor` 时，文字颜色会根据背景亮度自动选择黑色或白色；只设置 `fgColor` 时背景使用系统按钮色。

## 使用说明

- 前置条件：Windows 上需先调用 `qiumingdll_init()`。
- 平台限制：仅 Windows 生效；非 Windows 平台会降级为 `show_message_async(message)`，并返回 `0`。
- 阻塞行为：对话框为模态窗口，弹出期间调用线程阻塞，父窗口被禁用，直到用户操作后才恢复。
- 与 `qiumingdll_show_error` 的区别：
  - `show_error` 会自动拼接 `debug_get_callstack()` 调用栈，标题固定为 `"Code Error"`；
  - `show_error_ex` **不会**自动追加任何内容，标题和正文完全按传入值显示，适合做自定义错误页/确认框。
- 最多显示 16 个按钮。`buttons_json` 解析失败时回退为默认的 Abort / Ignore / Copy / Clear 四个按钮，标题和正文仍正常显示。
- 按钮背景色通过 owner-draw 绘制；没有设置颜色的按钮仍使用系统原生样式。
- `default` 按钮响应回车，`cancel` 按钮响应 Esc；点击标题栏 X 始终返回 `closeResult`。
- 正文为只读时仍可选中复制；`action = "copy"` 会复制全部正文。

## 示例

### 自定义标题、正文、按钮文本与颜色

```gml
qiumingdll_init();

var _json = "[{\"text\":\"退出游戏\",\"action\":\"exit\",\"exitCode\":1,\"bgColor\":\"#B71C1C\",\"fgColor\":\"#FFFFFF\"},"
          + "{\"text\":\"忽略并继续\",\"action\":\"close\",\"result\":5,\"bgColor\":\"#2E7D32\"}]";

var _ret = qiumingdll_show_error_ex(
    "存档损坏",
    "无法读取 save.dat。\r\n可以忽略并尝试恢复默认存档。",
    _json
);

if (_ret == 5)
{
    show_debug_message("玩家选择忽略错误");
}
```

### 用结构体 + json_stringify 构造配置（GMS 2.3+）

```gml
var _config = {
    title: "网络错误",
    message: "与主机的连接已断开。",
    width: 640,
    height: 360,
    closeResult: 2,
    buttons: [
        { text: "退出", action: "exit", exitCode: 1, bgColor: "#B71C1C" },
        { text: "重试", action: "close", result: 10, default: true, bgColor: "#1565C0" },
        { text: "复制错误", action: "copy", bgColor: "#455A64" }
    ]
};

// title/message 参数会被配置对象里的同名字段覆盖，这里传空串即可
var _ret = qiumingdll_show_error_ex("", "", json_stringify(_config));

if (_ret == 10)
{
    // 玩家点了“重试”
}
```

### 只有正文和关闭按钮

```gml
// 空数组：不显示按钮，只能点标题栏 X（返回 closeResult，默认 2）
qiumingdll_show_error_ex("提示", "任务已完成。", "[]");
```

## 相关函数

- [qiumingdll_show_error](qiumingdll_show_error.md)
- [qiumingdll_init](qiumingdll_init.md)
- [qiumingdll_get_version](qiumingdll_get_version.md)
