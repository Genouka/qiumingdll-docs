# qiumingdll_desktop_restore_wallpaper()

还原到最近一次 `qiumingdll_desktop_backup_wallpaper()` 备份的桌面壁纸。用于将游戏临时更换的壁纸恢复为用户原壁纸。

## 函数签名

```gml
qiumingdll_desktop_restore_wallpaper()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 还原成功 |
| 0 | 还原失败：从未调用过 `backup_wallpaper()`（无备份），或还原 API 调用失败，或当前平台不支持 |

## 使用说明

- 前置条件：必须先成功调用过 `qiumingdll_desktop_backup_wallpaper()` 且返回 1；否则无备份可还原，返回 0。
- 平台限制：仅 Windows 有效，其他平台固定返回 0。
- 还原通过 `SystemParametersInfo(SPI_SETDESKTOPWALLPAPER)` 完成，并立即通知系统刷新桌面（`SPIF_UPDATEINIFILE | SPIF_SENDCHANGE`）。
- 还原的是备份时记录的文件路径；若原壁纸文件已被删除/移动，还原会失败（返回 0）。
- 建议在游戏退出或场景切换回普通界面时调用，避免把游戏壁纸遗留在桌面上。

## 示例

```gml
// 游戏进入"特殊场景"时换壁纸，退出时还原
qiumingdll_desktop_backup_wallpaper();
qiumingdll_desktop_set_wallpaper("C:/game/special_wallpaper.jpg");

// …游戏进行中…

// 退出特殊场景：还原（务必判断返回值，失败也不应中断游戏）
if (qiumingdll_desktop_restore_wallpaper() != 1)
{
    show_debug_message("警告：桌面壁纸还原失败，请手动检查");
}
```

## 相关函数

- [qiumingdll_desktop_backup_wallpaper](qiumingdll_desktop_backup_wallpaper.md)
- [qiumingdll_desktop_set_wallpaper](qiumingdll_desktop_set_wallpaper.md)
- [qiumingdll_desktop_get_username](qiumingdll_desktop_get_username.md)
