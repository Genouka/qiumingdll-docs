# qiumingdll_ime_get_commit_text()

Get the commit text confirmed for this input; the text is cleared once it has been read.

## Signature

```gml
qiumingdll_ime_get_commit_text()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| String | The text to be committed for this input (UTF-8); returns "" when there is no new commit text |

Non-Windows platforms always return "".

## Usage

- Platform limit: Windows only; other platforms always return "".
- Precondition: call `qiumingdll_ime_get_state` first and confirm that the status bits contain 0x02 (new commit text); otherwise you usually read "" (because the previous read already cleared it).
- **One-shot semantics**: the commit text is cleared immediately after being read, so the same text cannot be read a second time. If a read is missed (e.g. while the game is paused), that commit text stays buffered until the next read, when it is returned as well.
- The commit text may contain the accumulation of several inputs (concatenated as compositions are committed); a single read returns all of it.
- The text is UTF-8 encoded and can be appended directly to GML strings.
- Typical usage: append the return value to an in-game text variable (such as the confirmed text of a chat input box).
- Simplified alternative: `qiumingdll_ime_get_commit` checks status bit 0x02 internally, so you do not have to query the state manually first.

## Example

```gml
// Step event: append the commit text when one is detected
var state = qiumingdll_ime_get_state();
if (state & 2) { // There is new commit text
    var commit = qiumingdll_ime_get_commit_text();
    if (commit != "") {
        input_text += commit; // Append to the confirmed text
    }
}
```

## Related functions

- [qiumingdll_ime_get_commit](qiumingdll_ime_get_commit.md)
- [qiumingdll_ime_get_state](qiumingdll_ime_get_state.md)
- [qiumingdll_ime_poll_json](qiumingdll_ime_poll_json.md)
