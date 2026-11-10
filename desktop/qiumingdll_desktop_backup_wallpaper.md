# qiumingdll_desktop_backup_wallpaper()

读取并备份当前桌面壁纸的路径，供后续用 `qiumingdll_desktop_restore_wallpaper()` 还原。建议在修改壁纸之前先调用本函数。

## 函数签名

```gml
qiumingdll_desktop_backup_wallpaper()
```

## 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| （无） | - | - | 本函数不接受任何参数 |

## 返回值

| 值 | 说明 |
|----|------|
| 1 | 备份成功（已记录当前壁纸路径） |
| 0 | 备份失败：读取系统壁纸路径的 API 调用失败，或当前平台不支持 |

## 使用说明

- 前置条件：无；Windows 上通过 `SystemParametersInfo(SPI_GETDESKTOPWALLPAPER)` 读取。
- 平台限制：仅 Windows 有效，其他平台固定返回 0。
- 只保留**最近一次**备份：多次调用会以最后一次为准；如需保留多份，请在外部自行记录路径。
- 备份的是壁纸文件的"路径"，还原时按该路径重新设置，因此期间请勿删除/移动原壁纸文件，否则还原会失败。
- 与 `set_wallpaper` 配合的典型流程：先 `backup_wallpaper()` → `set_wallpaper(...)` 临时换壁纸 → 游戏退出前 `restore_wallpaper()` 还原。

## 示例

```gml
// 进入特殊场景前：先备份，再换成游戏专属壁纸
if (qiumingdll_desktop_backup_wallpaper() == 1)
{
    qiumingdll_desktop_set_wallpaper("C:/game/special_wallpaper.jpg");
}

// 退出场景时还原
qiumingdll_desktop_restore_wallpaper();
```

## 相关函数

- [qiumingdll_desktop_restore_wallpaper](qiumingdll_desktop_restore_wallpaper.md)
- [qiumingdll_desktop_set_wallpaper](qiumingdll_desktop_set_wallpaper.md)
- [qiumingdll_desktop_get_username](qiumingdll_desktop_get_username.md)
