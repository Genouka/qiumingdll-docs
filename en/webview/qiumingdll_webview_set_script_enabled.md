# qiumingdll_webview_set_script_enabled(webviewId, enabled)

Enable or disable JavaScript execution in the specified WebView page.

## Signature

```gml
qiumingdll_webview_set_script_enabled(webviewId, enabled)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | Real | yes | WebView id, range 1 ~ 16 |
| enabled | Real | yes | Boolean switch: 1 (non-zero) = allow JavaScript execution (**on by default**), 0 = forbid the page from running any script |

## Returns

| Value | Description |
|----|------|
| 1 | Set successfully |
| 0 | Call failed: invalid id, the WebView does not exist, or it is not ready yet (this function requires readiness) |
| 0 | Non-Windows platform: the GML wrapper returns 0 directly |

## Usage

- Precondition: the WebView has been created and is ready (wait until get_is_active returns 1).
- **On by default**; under normal circumstances there is no need to call this function.
- After disabling:
  - None of the page's own `<script>` / inline JS executes;
  - `execute_script(id, ...)` also stops working (the submission fails or has no effect).
- Purpose: when loading untrusted third-party HTML content, disable scripts to improve security (combined with disabling DevTools and the context menu, this forms a "display-only" mode).
- Affects a single WebView only.

## Example

```gml
/// Create event (obj_webview_unsafe)
qiumingdll_webview_init();

// A window for showing "untrusted content": scripts and the context menu are off, view only
webviewId = qiumingdll_webview_create(200, 150, 800, 600);
hardened = false;

/// Step event
if (!hardened && qiumingdll_webview_get_is_active(webviewId) == 1)
{
    hardened = true;
    // Turn everything off: scripts, context menu, status bar, DevTools (DevTools is off by default anyway)
    qiumingdll_webview_set_script_enabled(webviewId, 0);
    qiumingdll_webview_set_default_context_menus_enabled(webviewId, 0);
    qiumingdll_webview_set_devtools_enabled(webviewId, 0);
    qiumingdll_webview_navigate(webviewId, "file:///C:/game/readme.html");
}

/// Room end event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_execute_script](qiumingdll_webview_execute_script.md)
- [qiumingdll_webview_set_devtools_enabled](qiumingdll_webview_set_devtools_enabled.md)
- [qiumingdll_webview_set_default_context_menus_enabled](qiumingdll_webview_set_default_context_menus_enabled.md)
- [qiumingdll_webview_get_is_active](qiumingdll_webview_get_is_active.md)
