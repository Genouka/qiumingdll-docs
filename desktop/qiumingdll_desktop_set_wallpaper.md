# qiumingdll_desktop_set_wallpaper(path)

设置当前桌面壁纸为指定的图片文件（支持 jpg / png / bmp 等 Windows 桌面支持的格式）。

## 函数签名

```gml
qiumingdll_desktop_set_wallpaper(path)
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| path | String | 是 | 壁纸图片的完整文件路径（建议使用绝对路径）。支持 UTF-8 路径，内部会转换成系统宽字符路径；转换失败时回退为 ANSI 解释 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 设置成功 |
| 0 | 设置失败：路径为空、文件不存在/无法访问、或设置 API 调用失败，或当前平台不支持 |

## 使用说明

- 前置条件：无；Windows 上通过 `SystemParametersInfo(SPI_SETDESKTOPWALLPAPER)` 并设置 `SPIF_UPDATEINIFILE | SPIF_SENDCHANGE` 立即生效。
- 平台限制：仅 Windows 有效，其他平台固定返回 0。
- 路径必须指向**真实存在的图片文件**；传入空字符串或不存在的路径会返回 0。相对路径可能因进程工作目录而异，建议使用 `working_directory` / 绝对路径拼接。
- 该操作会**直接修改用户桌面**，建议先用 `qiumingdll_desktop_backup_wallpaper()` 备份，并在合适时机用 `qiumingdll_desktop_restore_wallpaper()` 还原，避免给玩家留下意外改动。
- 图片格式与"填充/拉伸/居中"等显示方式沿用系统当前设置。

## 示例

```gml
// 把游戏目录下的壁纸设到桌面（注意使用绝对路径）
var _wp = working_directory + "assets/special_wallpaper.jpg";
if (file_exists(_wp))
{
    qiumingdll_desktop_backup_wallpaper();      // 先备份用户原壁纸
    if (qiumingdll_desktop_set_wallpaper(_wp) == 1)
    {
        show_debug_message("桌面壁纸已切换到游戏壁纸");
    }
}
```

## 相关函数

- [qiumingdll_desktop_backup_wallpaper](qiumingdll_desktop_backup_wallpaper.md)
- [qiumingdll_desktop_restore_wallpaper](qiumingdll_desktop_restore_wallpaper.md)
- [qiumingdll_desktop_get_username](qiumingdll_desktop_get_username.md)
