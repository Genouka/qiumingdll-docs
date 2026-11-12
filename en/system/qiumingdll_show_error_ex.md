# qiumingdll_show_error_ex(title, message, buttons_json)

Shows a fully customizable blocking error dialog: title, body text, button text, button behavior, and button background/text colors can all be configured.

## Signature

```gml
qiumingdll_show_error_ex(title, message, buttons_json)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| title | String | Yes | Window title, any UTF-8 text. Pass `""` to show an empty title |
| message | String | Yes | Error body, any UTF-8 text, supports `\r\n` / `\n` multi-line |
| buttons_json | String | Yes | Button configuration as a **JSON string**. You may pass a JSON array, or a configuration object containing fields such as `buttons`; passing `""` uses the default Abort / Ignore / Copy / Clear buttons |

> `buttons_json` is a string, not an array/struct. On GMS 2.3+ call `json_stringify(array or struct)` first and pass the result; on older GameMaker pass hand-written JSON text directly.

## Returns

| Value | Description |
|----|------|
| The button's `result` | The button with `action = "close"` was clicked. Without an explicit `result`, it defaults to the button index + 1 |
| `closeResult` (default `2`, i.e. IDCANCEL) | Returned when the title bar X is clicked, Esc is pressed (and no `cancel` button exists), or the window is closed externally |
| The `result` of the `cancel` button | When a button with `cancel = true` exists, pressing Esc triggers that button's behavior and returns its result |
| `0` | Window creation failed (very rare, e.g. window class registration failure) |
| No return value | A button with `action = "exit"` terminates the process directly and does not return |

## buttons_json format

### Simplest form: string array

```json
["OK", "Cancel"]
```

Each string produces a button with `action = "close"`, returning `1`, `2` respectively.

### Array of button objects

```json
[
  { "text": "Quit game", "action": "exit", "exitCode": 1, "bgColor": "#B71C1C", "fgColor": "#FFFFFF" },
  { "text": "Ignore", "action": "close", "result": 5, "bgColor": "#2E7D32" }
]
```

### Full configuration object

```json
{
  "title": "Corrupted save",
  "message": "Cannot read save.dat.\nYou can ignore this and try to restore the default save.",
  "width": 720,
  "height": 420,
  "closeResult": 2,
  "readOnly": true,
  "icon": "warning",
  "buttons": [
    { "text": "Quit", "action": "exit", "exitCode": 1, "bgColor": "#B71C1C" },
    { "text": "Ignore", "action": "close", "result": 5, "bgColor": "#2E7D32" }
  ]
}
```

The `title` / `message` in the configuration object override the function parameters; absent fields keep their default values.

### Top-level fields

| Field | Type | Default | Description |
|------|------|--------|------|
| title | String | Function parameter | Window title; overrides the first parameter |
| message | String | Function parameter | Error body; overrides the second parameter |
| width | Number | `800` | Outer window width in pixels, minimum 320, maximum 8000; widened automatically when the buttons do not fit |
| height | Number | `600` | Outer window height in pixels, minimum 220, maximum 8000 |
| closeResult | Number | `2` | Return value when X is clicked / Esc pressed (no cancel button) / the window is closed externally |
| readOnly | Boolean | `true` | Whether the body is read-only; with `false` the player can edit the body |
| icon | String | `"error"` | Title bar icon: `"error"`, `"warning"`, `"info"`, `"question"`, `"none"` |
| buttons | Array | Default four buttons | Button array; pass `[]` to show no buttons (closing is then only possible via the title bar) |

### Button fields

| Field | Type | Default | Description |
|------|------|--------|------|
| text | String | `"OK"` | Button text, any UTF-8 text |
| action | String | `"close"` | Button behavior, see the table below |
| result | Number | Index + 1 | Return value when `action = "close"` |
| exitCode | Number | `1` | Process exit code used when `action = "exit"` |
| bgColor | String / Number | System button color | Button background color, see the rules below |
| fgColor | String / Number | Automatic black or white | Button text color, see the rules below |
| width | Number | Fit to text | Button width in pixels, limited to 40~800 |
| enabled | Boolean | `true` | Whether the button is enabled; clicking a disabled button does nothing |
| default | Boolean | `false` | Whether it is the default button (triggered by Enter); with several, only the first takes effect |
| cancel | Boolean | `false` | Whether it is the cancel button (triggered by Esc); with several, only the first takes effect |

`bgColor` / `fgColor` also accept the aliases `bg` / `background` and `fg` / `textColor`.

### action behaviors

| action | Behavior |
|--------|------|
| `"close"` | Closes the dialog and returns `result` (default index + 1) |
| `"exit"` | Closes the dialog and ends the process with `exitCode` (default 1); it **does not return** |
| `"copy"` | Copies the whole body to the clipboard; the dialog stays open |
| `"clear"` | Clears the body; the dialog stays open |
| `"none"` | Does nothing; the dialog stays open |

`action` also accepts `"abort"` / `"quit"` (equivalent to `exit`) and `"noop"` (equivalent to `none`).

### Color format

- String: `"#RRGGBB"` or `"#AARRGGBB"` (web format; Alpha is ignored).
- Number: interpreted as Windows `COLORREF` / GML `make_color_rgb()` `0x00BBGGRR`. For example, `make_color_rgb(255, 0, 0)` and `255` both mean red.
- When only `bgColor` is set, the text color is chosen automatically as black or white based on the background brightness; when only `fgColor` is set, the background uses the system button color.

## Usage

- Prerequisite: call `qiumingdll_init()` first on Windows.
- Platform support: Windows only; non-Windows platforms fall back to `show_message_async(message)` and return `0`.
- Blocking behavior: the dialog is a modal window; while it is open the calling thread blocks and the parent window is disabled until the user acts.
- Difference from `qiumingdll_show_error`:
  - `show_error` appends the `debug_get_callstack()` call stack automatically and always uses the title `"Code Error"`;
  - `show_error_ex` appends **nothing** automatically; the title and body are shown exactly as passed, which suits custom error pages/confirmation boxes.
- At most 16 buttons are shown. If `buttons_json` fails to parse, it falls back to the default Abort / Ignore / Copy / Clear buttons, while the title and body still display normally.
- Button background colors are drawn via owner-draw; buttons without a color set still use the native system style.
- The `default` button responds to Enter and the `cancel` button responds to Esc; clicking the title bar X always returns `closeResult`.
- When the body is read-only it can still be selected and copied; `action = "copy"` copies the whole body.

## Example

### Custom title, body, button text and colors

```gml
qiumingdll_init();

var _json = "[{\"text\":\"Quit game\",\"action\":\"exit\",\"exitCode\":1,\"bgColor\":\"#B71C1C\",\"fgColor\":\"#FFFFFF\"},"
          + "{\"text\":\"Ignore and continue\",\"action\":\"close\",\"result\":5,\"bgColor\":\"#2E7D32\"}]";

var _ret = qiumingdll_show_error_ex(
    "Corrupted save",
    "Cannot read save.dat.\r\nYou can ignore this and try to restore the default save.",
    _json
);

if (_ret == 5)
{
    show_debug_message("Player chose to ignore the error");
}
```

### Building the configuration with a struct + json_stringify (GMS 2.3+)

```gml
var _config = {
    title: "Network error",
    message: "The connection to the host was lost.",
    width: 640,
    height: 360,
    closeResult: 2,
    buttons: [
        { text: "Quit", action: "exit", exitCode: 1, bgColor: "#B71C1C" },
        { text: "Retry", action: "close", result: 10, default: true, bgColor: "#1565C0" },
        { text: "Copy error", action: "copy", bgColor: "#455A64" }
    ]
};

// The title/message parameters are overridden by the same-named fields in the configuration object, so pass empty strings here
var _ret = qiumingdll_show_error_ex("", "", json_stringify(_config));

if (_ret == 10)
{
    // The player clicked "Retry"
}
```

### Body text with only a close button

```gml
// Empty array: no buttons are shown, only the title bar X can be clicked (returns closeResult, default 2)
qiumingdll_show_error_ex("Notice", "The task is complete.", "[]");
```

## Related functions

- [qiumingdll_show_error](qiumingdll_show_error.md)
- [qiumingdll_init](qiumingdll_init.md)
- [qiumingdll_get_version](qiumingdll_get_version.md)
