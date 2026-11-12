# qiumingdll_desktop_get_username()

Gets the currently logged-in Windows username (for example `29800`). Useful for distinguishing players, storing saves under the user directory, and so on.

## Signature

```gml
qiumingdll_desktop_get_username()
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|-------|-------------|
| String | The current Windows username (a UTF-8 string) |
| Empty string `""` | Retrieval failed (very rare, e.g. the API call failed) or the current platform is not supported |

## Usage

- Prerequisites: none; on Windows it reads directly through `GetUserName`, with no initialization required.
- Platform limits: only Windows returns a real username; other platforms always return an empty string.
- The return value uses an internal static buffer and stays valid **until the next call to this function**; copy it immediately if you need to keep it (for example `var u = qiumingdll_desktop_get_username();` and then use or store it right away).
- The result matches the system login account name; case sensitivity follows whatever the system returns.

## Example

```gml
var _user = qiumingdll_desktop_get_username();
if (_user != "")
{
    show_debug_message("Current Windows user: " + _user);
    // For example, store configuration per user directory
    var _savePath = "C:/Users/" + _user + "/AppData/Local/mygame/save.dat";
}
```

## Related functions

- [qiumingdll_desktop_backup_wallpaper](qiumingdll_desktop_backup_wallpaper.md)
- [qiumingdll_desktop_restore_wallpaper](qiumingdll_desktop_restore_wallpaper.md)
- [qiumingdll_desktop_set_wallpaper](qiumingdll_desktop_set_wallpaper.md)
