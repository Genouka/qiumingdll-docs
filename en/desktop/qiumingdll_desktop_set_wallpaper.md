# qiumingdll_desktop_set_wallpaper(path)

Sets the current desktop wallpaper to the specified image file (supports jpg / png / bmp and any other format the Windows desktop accepts).

## Signature

```gml
qiumingdll_desktop_set_wallpaper(path)
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| path | String | Yes | Full file path of the wallpaper image (absolute paths recommended). UTF-8 paths are supported and converted internally to a system wide-character path; if the conversion fails it falls back to interpreting the path as ANSI |

## Returns

| Value | Description |
|-------|-------------|
| `1` | Set successfully |
| `0` | Failed: the path is empty, the file is missing/inaccessible, the set API call failed, or the current platform is not supported |

## Usage

- Prerequisites: none; on Windows it uses `SystemParametersInfo(SPI_SETDESKTOPWALLPAPER)` with `SPIF_UPDATEINIFILE | SPIF_SENDCHANGE`, so the change takes effect immediately.
- Platform limits: Windows only; always returns 0 on other platforms.
- The path must point to a **real, existing image file**; an empty string or a nonexistent path returns 0. Relative paths depend on the process working directory, so build the path from `working_directory` / an absolute path.
- This operation **modifies the user's desktop directly**; call `qiumingdll_desktop_backup_wallpaper()` first and `qiumingdll_desktop_restore_wallpaper()` at the appropriate time so players are not left with an unexpected change.
- The image format and display mode ("fill / stretch / center", etc.) follow the current system settings.

## Example

```gml
// Put the wallpaper from the game directory onto the desktop (note the absolute path)
var _wp = working_directory + "assets/special_wallpaper.jpg";
if (file_exists(_wp))
{
    qiumingdll_desktop_backup_wallpaper();      // Back up the user's original wallpaper first
    if (qiumingdll_desktop_set_wallpaper(_wp) == 1)
    {
        show_debug_message("Desktop wallpaper switched to the game wallpaper");
    }
}
```

## Related functions

- [qiumingdll_desktop_backup_wallpaper](qiumingdll_desktop_backup_wallpaper.md)
- [qiumingdll_desktop_restore_wallpaper](qiumingdll_desktop_restore_wallpaper.md)
- [qiumingdll_desktop_get_username](qiumingdll_desktop_get_username.md)
