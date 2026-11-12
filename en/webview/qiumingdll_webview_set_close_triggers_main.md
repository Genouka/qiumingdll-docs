# qiumingdll_webview_set_close_triggers_main(webviewId, triggers)

Set whether closing this WebView standalone window also closes the game main window.

## Signature

```gml
qiumingdll_webview_set_close_triggers_main(webviewId, triggers)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | yes | WebView id, range 1 ~ 16 |
| triggers | Real | yes | Boolean switch: 1 (non-zero) = closing this window also sends a close signal to the game main window, 0 (default) = close only this window |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Call failed: invalid id, or there is no active WebView with that id |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Precondition: the WebView has been created; only meaningful for standalone windows.
- Default: for standalone windows created by create, **triggers = 0** (closing the browser does not affect the game); after setting 1, when the user closes this window by clicking X or pressing Alt+F4, the game main window also receives a close request (equivalent to quitting the game).
- Only triggered when the user actively closes the window; calling destroy / destroy_all in-game does **not** trigger the chained close.
- Relation to set_closable: with closable=0 the user cannot close the window, so this setting never triggers; the combination triggers=1 + closable=1 is common for fullscreen "browser as the main UI" games.
- Common for standalone (non-child) game windows used as the main menu or main interface: closing the browser means quitting the game.
- Has no effect on child windows (child windows cannot be closed by the user).

## Example

```gml
/// Create event (obj_main_menu_browser)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(0, 0, 1280, 720);
qiumingdll_webview_navigate(webviewId, "file:///C:/game/menu/index.html");

// Main menu browser: closing it = quitting the game
qiumingdll_webview_set_closable(webviewId, 1);               // Allow closing
qiumingdll_webview_set_close_triggers_main(webviewId, 1);    // Closing also exits the main program

// Rest of the flow: wait until ready, rotate the page, etc.
/// Step event
if (qiumingdll_webview_get_is_active(webviewId) == 1 && !navigated)
{
    navigated = true;
    qiumingdll_webview_execute_script(webviewId, "startMenu();");  // Call a function in the page
}

/// Room end event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_set_closable](qiumingdll_webview_set_closable.md)
- [qiumingdll_webview_destroy](qiumingdll_webview_destroy.md)
- [qiumingdll_webview_cleanup](qiumingdll_webview_cleanup.md)
