# qiumingdll_webview_go_forward(webviewId)

Navigate the given WebView forward to the next page in its browsing history (equivalent to the browser's Forward button).

## Signature

```gml
qiumingdll_webview_go_forward(webviewId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| webviewId | real | yes | WebView id, range 1 ~ 16 |

## Returns

| Value | Description |
|----|------|
| `1` | Forward request submitted (does not guarantee that the history actually moved forward) |
| `0` | Failure: invalid id, WebView does not exist, or not ready yet |
| `0` | Non-Windows platforms: the GML wrapper returns 0 directly |

## Usage

- Prerequisite: the WebView is ready.
- **Depends on browsing history**: you must have gone back first (or later history entries must exist) for there to be anything to move forward to; if you have never gone back, the call returns 1 but the page stays unchanged.
- Typical "forward" scenario: the user went back to view an older page and now wants to return to the page they came from.
- History is maintained per WebView.
- Combine with go_back / reload for a complete browser toolbar.
- Asynchronous: a return value of 1 only means the request was issued.

## Example

```gml
/// Create event (obj_browser_toolbar)
qiumingdll_webview_init();
webviewId = qiumingdll_webview_create(200, 150, 800, 600);
loaded = false;

/// Step event
// Once ready, demonstrate a "multi-page browsing" flow:
// page A -> page B -> back -> forward
if (qiumingdll_webview_get_is_active(webviewId) == 1 && !loaded)
{
    loaded = true;
    qiumingdll_webview_navigate(webviewId, "https://example.com/page_a");
    step_phase = 0;
}

switch (step_phase)
{
case 0:  // Switch to page B after 60 frames
    phase_tick++;
    if (phase_tick >= 60)
    {
        qiumingdll_webview_navigate(webviewId, "https://example.com/page_b");
        step_phase = 1;
        phase_tick = 0;
    }
    break;
case 1:  // After another 60 frames, go back
    phase_tick++;
    if (phase_tick >= 60)
    {
        qiumingdll_webview_go_back(webviewId);      // Back to page A
        step_phase = 2;
        phase_tick = 0;
    }
    break;
case 2:  // After another 60 frames, go forward
    phase_tick++;
    if (phase_tick >= 60)
    {
        qiumingdll_webview_go_forward(webviewId);   // Back to page B
        step_phase = 3;
    }
    break;
}

/// Room end event
qiumingdll_webview_cleanup();
```

## Related functions

- [qiumingdll_webview_go_back](qiumingdll_webview_go_back.md)
- [qiumingdll_webview_reload](qiumingdll_webview_reload.md)
- [qiumingdll_webview_navigate](qiumingdll_webview_navigate.md)
