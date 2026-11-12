# qiumingdll_desktop_backup_wallpaper()

Reads and backs up the path of the current desktop wallpaper so it can later be restored with `qiumingdll_desktop_restore_wallpaper()`. Call this before changing the wallpaper.

## Signature

```gml
qiumingdll_desktop_backup_wallpaper()
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|-------|-------------|
| `1` | Backup succeeded (the current wallpaper path has been recorded) |
| `0` | Failed: the API call that reads the system wallpaper path failed, or the current platform is not supported |

## Usage

- Prerequisites: none; on Windows it reads via `SystemParametersInfo(SPI_GETDESKTOPWALLPAPER)`.
- Platform limits: Windows only; always returns 0 on other platforms.
- Only the **most recent** backup is kept: calling it multiple times keeps the last one; record the paths yourself if you need several.
- What is backed up is the wallpaper file's "path", and restoring re-applies that path, so do not delete/move the original wallpaper file in the meantime, or the restore will fail.
- Typical flow with `set_wallpaper`: `backup_wallpaper()` → `set_wallpaper(...)` to change the wallpaper temporarily → `restore_wallpaper()` before the game exits.

## Example

```gml
// Before entering a special scene: back up first, then switch to the game-only wallpaper
if (qiumingdll_desktop_backup_wallpaper() == 1)
{
    qiumingdll_desktop_set_wallpaper("C:/game/special_wallpaper.jpg");
}

// Restore when leaving the scene
qiumingdll_desktop_restore_wallpaper();
```

## Related functions

- [qiumingdll_desktop_restore_wallpaper](qiumingdll_desktop_restore_wallpaper.md)
- [qiumingdll_desktop_set_wallpaper](qiumingdll_desktop_set_wallpaper.md)
- [qiumingdll_desktop_get_username](qiumingdll_desktop_get_username.md)
