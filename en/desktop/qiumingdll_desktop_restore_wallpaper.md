# qiumingdll_desktop_restore_wallpaper()

Restores the desktop wallpaper backed up by the most recent `qiumingdll_desktop_backup_wallpaper()` call. Use it to return the wallpaper the game changed temporarily to the user's original one.

## Signature

```gml
qiumingdll_desktop_restore_wallpaper()
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|-------|-------------|
| `1` | Restored successfully |
| `0` | Failed: `backup_wallpaper()` was never called (no backup), the restore API call failed, or the current platform is not supported |

## Usage

- Prerequisites: `qiumingdll_desktop_backup_wallpaper()` must have been called successfully and returned 1; otherwise there is no backup to restore and the function returns 0.
- Platform limits: Windows only; always returns 0 on other platforms.
- The restore is done through `SystemParametersInfo(SPI_SETDESKTOPWALLPAPER)` and immediately notifies the system to refresh the desktop (`SPIF_UPDATEINIFILE | SPIF_SENDCHANGE`).
- It restores the file path recorded at backup time; if the original wallpaper file has been deleted/moved, the restore fails (returns 0).
- Call it when the game exits or when a scene switches back to the normal UI, so the game wallpaper is not left on the desktop.

## Example

```gml
// Switch the wallpaper when the game enters a "special scene", restore it on exit
qiumingdll_desktop_backup_wallpaper();
qiumingdll_desktop_set_wallpaper("C:/game/special_wallpaper.jpg");

// …gameplay in progress…

// Leaving the special scene: restore (always check the return value; a failure must not interrupt the game)
if (qiumingdll_desktop_restore_wallpaper() != 1)
{
    show_debug_message("Warning: failed to restore the desktop wallpaper, please check manually");
}
```

## Related functions

- [qiumingdll_desktop_backup_wallpaper](qiumingdll_desktop_backup_wallpaper.md)
- [qiumingdll_desktop_set_wallpaper](qiumingdll_desktop_set_wallpaper.md)
- [qiumingdll_desktop_get_username](qiumingdll_desktop_get_username.md)
