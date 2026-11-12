# qiumingdll_cursor_get_invert()

Queries whether the "cursor moves opposite to the mouse" state is currently active.

## Signature

```gml
qiumingdll_cursor_get_invert()
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|-------|-------------|
| 1 | The cursor inversion effect is currently enabled |
| 0 | Not enabled (never enabled, already disabled manually, or cancelled by the 8×F12 safety valve) |

## Usage

- Precondition: on Windows, `qiumingdll_init()` must be called first.
- Platform limit: Windows only.
- Behavior details: after the player cancels the effect with the F12 safety valve, this function also returns 0, so you can use it for UI hints about whether the effect needs to be re-enabled.
- This function only queries; it does not change the effect state.

## Example

```gml
/// Step event: show a hint while the effect is active
if (qiumingdll_cursor_get_invert()) {
    draw_text(8, 8, "Mouse inverted! Press F12 8 times to cancel");
} else {
    draw_text(8, 8, "");
}
```

## Related functions

- [qiumingdll_cursor_set_invert](qiumingdll_cursor_set_invert.md)
