# qiumingdll_winsplit_set_title(splitId, title)

Set the title text shown on the specified split window's title bar (visible only when a title bar is present).

## Signature

```gml
qiumingdll_winsplit_set_title(splitId, title)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window ID, value 1 ~ 16, must exist |
| title | String | yes | Title text to display, UTF-8 encoded, Chinese supported; length recommended not to exceed a few hundred characters |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Failed: `splitId` is invalid or does not exist; on non-Windows platforms the wrapper returns `0` directly |

## Usage

- Prerequisite: `qiumingdll_winsplit_init()` has been called successfully, and the split window corresponding to `splitId` exists.
- The title is shown only on the title bar; if the window currently has no title bar (`set_titlebar(splitId, false)`), setting the title has no visible effect (it is still stored internally and becomes visible when the title bar is re-enabled).
- Takes effect immediately after setting; the title bar is redrawn in real time.
- A split window's default title is an empty string at creation; if never set, there is no title.
- Chinese can be passed directly without transcoding (the wrapper passes it to the DLL as UTF-8).
- The title does not affect any logic behavior (it does not participate in close/drag decisions, etc.); it is purely for display.

## Example

```gml
// In the controller object's Create event, right after creating the split windows, give them memorable names
if (global.split_2 > 0)
{
    qiumingdll_winsplit_set_title(global.split_2, "Side minimap");
    qiumingdll_winsplit_set_title(global.split_1, "First-person view");
}
```

```gml
// Rename at any time, e.g. show the current room name
qiumingdll_winsplit_set_title(global.split_1, "Current room: " + room_get_name(room));
```

## Related functions

- [qiumingdll_winsplit_set_titlebar](qiumingdll_winsplit_set_titlebar.md)
- [qiumingdll_winsplit_create](qiumingdll_winsplit_create.md)
- [qiumingdll_winsplit_set_closable](qiumingdll_winsplit_set_closable.md)
