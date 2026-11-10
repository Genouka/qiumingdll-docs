# desktop 模块

桌面环境控制：读取当前登录用户名、备份/还原当前桌面壁纸、设置桌面壁纸。

共 4 个函数。

## 函数索引

| 函数 | 说明 |
|------|------|
| [qiumingdll_desktop_get_username](qiumingdll_desktop_get_username.md) | 获取当前 Windows 登录用户名（UTF-8 字符串）。 |
| [qiumingdll_desktop_backup_wallpaper](qiumingdll_desktop_backup_wallpaper.md) | 读取并备份当前桌面壁纸路径，供后续还原（保留最近一次）。 |
| [qiumingdll_desktop_restore_wallpaper](qiumingdll_desktop_restore_wallpaper.md) | 还原到最近一次备份的桌面壁纸。 |
| [qiumingdll_desktop_set_wallpaper](qiumingdll_desktop_set_wallpaper.md) | 将当前桌面壁纸设置为指定图片文件（绝对路径）。 |

## 典型用法

```gml
// 进入特殊场景前：备份原壁纸 → 换成游戏壁纸
qiumingdll_desktop_backup_wallpaper();
qiumingdll_desktop_set_wallpaper("C:/game/special_wallpaper.jpg");

// …游戏进行中…

// 退出时还原用户原壁纸
qiumingdll_desktop_restore_wallpaper();
```

## 平台限制

全部函数仅 Windows 有效；非 Windows 平台下 `get_username` 返回空字符串、其余返回 0。

[返回文档首页](../README.md)
