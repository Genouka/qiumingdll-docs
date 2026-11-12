# qiumingdll_webview_set_draggable(webviewId, draggable)

Set whether the specified WebView window can be dragged by holding down the window's content area.

## Signature

```gml
qiumingdll_webview_set_draggable(webviewId, draggable)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | yes | WebView id, range 1 ~ 16 |
| draggable | Real | yes | Boolean switch: 1 (non-zero) = hold anywhere in the window to drag it, 0 (default) = the window can only be dragged by its title bar (off by default) |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Call failed: invalid id, or there is no active WebView with that id |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Precondition: the WebView has been created; this is mainly designed for standalone windows.
- When enabled: hold the mouse **anywhere** inside the window (including the page content area) to drag the whole window, which makes moving borderless windows easy.
- Combined with set_titlebar(id, 0): gives a "borderless + drag anywhere" self-drawn window experience.
- Note: after enabling, in-page interactions that need "press and drag" (canvas dragging, sliders, text selection) may conflict with window dragging. Choose according to your actual needs, or let page elements intercept (you can add CSS elements following the `-webkit-app-region: no-drag` idea inside the page).
- Has no effect on child windows (child windows move with the main window and cannot be dragged on their own).

## Example

```gml
/// Create event (obj_webview_borderless)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(200, 200, 600, 400);

// Borderless + draggable from anywhere
qiumingdll_webview_set_titlebar(webviewId, 0);
qiumingdll_webview_set_draggable(webviewId, 1);

// Load the custom UI once ready
/// Step event
if (qiumingdll_webview_get_is_active(webviewId) == 1 && !loaded)
{
    loaded = true;
    qiumingdll_webview_navigate_to_string(webviewId,
        "<html><body style='margin:0;background:#20242c;color:#fff;user-select:none'>" +
        "<div style='padding:24px;text-align:center'>Hold me to drag the window</div>" +
        "</body></html>");
}

/// Room end event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_set_titlebar](qiumingdll_webview_set_titlebar.md)
- [qiumingdll_webview_set_position](qiumingdll_webview_set_position.md)
- [qiumingdll_webview_set_closable](qiumingdll_webview_set_closable.md)
