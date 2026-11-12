# desktop module

Desktop environment control: read the current logged-in username, back up/restore the current desktop wallpaper, and set the desktop wallpaper.

4 functions in total.

## Function index

| Function | Description |
|----------|-------------|
| [qiumingdll_desktop_get_username](qiumingdll_desktop_get_username.md) | Gets the current Windows login username (UTF-8 string). |
| [qiumingdll_desktop_backup_wallpaper](qiumingdll_desktop_backup_wallpaper.md) | Reads and backs up the current desktop wallpaper path for later restore (keeps the most recent one only). |
| [qiumingdll_desktop_restore_wallpaper](qiumingdll_desktop_restore_wallpaper.md) | Restores the desktop wallpaper from the most recent backup. |
| [qiumingdll_desktop_set_wallpaper](qiumingdll_desktop_set_wallpaper.md) | Sets the desktop wallpaper to the specified image file (absolute path). |

## Typical usage

```gml
// Before entering a special scene: back up the original wallpaper → switch to the game wallpaper
qiumingdll_desktop_backup_wallpaper();
qiumingdll_desktop_set_wallpaper("C:/game/special_wallpaper.jpg");

// …gameplay in progress…

// Restore the user's original wallpaper on exit
qiumingdll_desktop_restore_wallpaper();
```

## Platform limits

All functions are Windows-only; on non-Windows platforms `get_username` returns an empty string and the others return 0.

[Back to documentation home](../README.md)
