# qiumingdll_desktop_get_username()

获取当前登录的 Windows 用户名（例如 `29800`）。可用于区分不同玩家、按用户目录存放存档等。

## 函数签名

```gml
qiumingdll_desktop_get_username()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 字符串 | 当前 Windows 用户名（UTF-8 字符串） |
| 空字符串 `""` | 获取失败（极少见，如 API 调用失败）或当前平台不支持 |

## 使用说明

- 前置条件：无；Windows 上直接用 `GetUserName` 读取，无需初始化。
- 平台限制：仅在 Windows 平台返回真实用户名；其他平台固定返回空字符串。
- 返回值使用内部静态缓冲区，内容在**下一次调用本函数前有效**；若需长期保存，应立即复制（例如 `var u = qiumingdll_desktop_get_username();` 后马上使用或存入持久变量）。
- 该结果与系统登录账户名一致，区分大小写按系统返回为准。

## 示例

```gml
var _user = qiumingdll_desktop_get_username();
if (_user != "")
{
    show_debug_message("Current Windows user: " + _user);
    // 例如按用户目录存放配置
    var _savePath = "C:/Users/" + _user + "/AppData/Local/mygame/save.dat";
}
```

## 相关函数

- [qiumingdll_desktop_backup_wallpaper](qiumingdll_desktop_backup_wallpaper.md)
- [qiumingdll_desktop_restore_wallpaper](qiumingdll_desktop_restore_wallpaper.md)
- [qiumingdll_desktop_set_wallpaper](qiumingdll_desktop_set_wallpaper.md)
