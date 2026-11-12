# qiumingdll_webview_set_opacity(webviewId, opacity)

Set the overall opacity of the specified WebView window.

## Signature

```gml
qiumingdll_webview_set_opacity(webviewId, opacity)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | yes | WebView id, range 1 ~ 16 |
| opacity | Real | yes | Opacity value, range 0 ~ 255: 0 = fully transparent (invisible), 255 = fully opaque (default). Values outside the range are clamped to 0 ~ 255 automatically (fractions are truncated to integers) |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Call failed: invalid id, or there is no active WebView with that id |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Precondition: the WebView has been created. Does not require readiness.
- Opacity applies to the **entire window** (including the title bar and all page content); animations must be implemented by changing the value gradually in the Step event.
- At 255 the layered attribute is removed internally (restoring a normal window, best performance); below 255 a layered window is enabled (WS_EX_LAYERED).
- At 0 the window is fully transparent but **still exists** (it intercepts the mouse and receives input). Distinguish this from hide: use hide when you need it completely invisible and non-interactive.
- A semi-transparent window still renders and interacts normally within the page above it, which suits "ghost hints" and "preview overlays".

## Example

```gml
/// Create event (obj_webview_ghost)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(300, 200, 400, 300);
qiumingdll_webview_navigate(webviewId, "https://example.com");
fading = false;
alphaNow = 255;

/// Step event
// Press G to start the fade in/out loop
if (keyboard_check_pressed(ord("G"))) fading = true;

if (fading)
{
    alphaNow += 3 * choose_alpha_dir;  // Simplified demo: change linearly
    // Safer approach: keep a direction variable and reverse it at the bounds
    if (alphaNow > 255) { alphaNow = 255; fading = false; }
    qiumingdll_webview_set_opacity(webviewId, alphaNow);
}

// Declare choose_alpha_dir before using it
/// Create event addendum
choose_alpha_dir = 1;

/// Room end event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_hide](qiumingdll_webview_hide.md)
- [qiumingdll_webview_show](qiumingdll_webview_show.md)
- [qiumingdll_webview_set_position](qiumingdll_webview_set_position.md)
