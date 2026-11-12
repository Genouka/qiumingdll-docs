# qiumingdll_ime_get_commit()

Simplified commit-text retrieval: checks status bit 0x02 internally, returning the commit text when there is one and an empty string otherwise.

## Signature

```gml
qiumingdll_ime_get_commit()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| "" | There is no new commit text at the moment |
| String | The new commit text (UTF-8); internally it calls `qiumingdll_ime_get_commit_text`, and the text is cleared once read |

Non-Windows platforms always return "".

## Usage

- Platform limit: Windows only; other platforms always return "".
- Equivalent logic: `var s = qiumingdll_ime_get_state(); return (s & 2) ? qiumingdll_ime_get_commit_text() : "";` — i.e. the two steps "check state → read text" are done for you in the GML wrapper.
- Difference from `qiumingdll_ime_get_commit_text`: this function checks the status bit for you, so the caller never needs to look at the 0x02 flag; both share the one-shot read semantics (cleared after reading).
- Caution: this function calls `qiumingdll_ime_get_state` internally, which consumes the one-shot flags. If you still need the status bits in the same frame to read other data (composition, candidates, mode), call `qiumingdll_ime_get_state` first, keep the result, and then read the individual values as needed.
- Suited to simple scenarios: call it once per frame, treat any non-empty return value as committed text — the most concise code.

## Example

```gml
// Step event: the simplest commit logic
var commit = qiumingdll_ime_get_commit();
if (commit != "") {
    chat_text += commit; // Automatically appended once a composition is confirmed
}
```

```gml
// Coexisting with other state checks: fetch the state first, then read the commit
var state = qiumingdll_ime_get_state();
if (state & 2) {
    chat_text += qiumingdll_ime_get_commit_text();
}
```

## Related functions

- [qiumingdll_ime_get_commit_text](qiumingdll_ime_get_commit_text.md)
- [qiumingdll_ime_get_state](qiumingdll_ime_get_state.md)
