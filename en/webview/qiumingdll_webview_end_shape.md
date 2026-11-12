# qiumingdll_webview_end_shape(webviewId)

Ends the irregular-shape editing of the WebView window, applying the shape region previously set via `qiumingdll_webview_set_region`.

## Signature

```gml
qiumingdll_webview_end_shape(webviewId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | Yes | WebView id (1 ~ 16), returned by `qiumingdll_webview_create` / `qiumingdll_webview_create_child` |

## Returns

| Value | Description |
|----|------|
| 1 | Shape region set and applied successfully |
| 0 | Failure. Possible reasons: invalid webviewId, no region has been set, non-Windows platform, or not initialized |

## Usage

- Precondition: on Windows, `qiumingdll_webview_init()` must have been called; `qiumingdll_webview_set_region(webviewId, ...)` must be called before this function.
- Platform support: Windows only.
- Behavior: `set_region` describes the shape; this function ends editing and commits the shape so the window displays according to the configured region.
- Note: to change the shape after ending it, just call `set_region` and `end_shape` again; calling `hide` / `show` does not lose an applied shape.

## Example

```gml
// Clip the browser window to an irregular shape
qiumingdll_webview_set_region(webviewId, ...);
qiumingdll_webview_end_shape(webviewId);
```

## Related functions

- [qiumingdll_webview_set_region](qiumingdll_webview_set_region.md)
- [qiumingdll_webview_create](qiumingdll_webview_create.md)
- [qiumingdll_webview_destroy](qiumingdll_webview_destroy.md)
