# qiumingdll_show_error(message)

Shows a blocking error dialog with a call stack (styled like a GameMaker crash report) to present an error message to the user.

## Signature

```gml
qiumingdll_show_error(message)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| message | String | Yes | Error text to show. May be multi-line (separate lines with `\r\n` or `\n`); it is displayed in the dialog's text box |

## Returns

| Value | Description |
|----|------|
| 3 (IDABORT) | The user clicked the "Abort" button. Note: the DLL then terminates the whole process immediately (equivalent to quitting the program) and does not return |
| 5 (IDIGNORE) | The user clicked the "Ignore" button, closing the dialog; the game keeps running |
| 2 (IDCANCEL) | The user closed the dialog directly (the window X or Esc), equivalent to ignoring |
| 0 | Returned when dialog creation fails (very rare) |
| (no return value) | Called on a non-Windows platform: falls back to a `show_message_async` popup with no return value |

## Usage

- Prerequisite: call `qiumingdll_init()` first on Windows.
- Platform support: on Windows a native error dialog is shown (title "Code Error", with the four buttons Abort / Ignore / Copy / Clear); non-Windows platforms automatically fall back to an asynchronous `show_message_async(message)` popup.
- Behavior details:
  - The dialog is a blocking modal window; the game is fully paused while it is open and continues only after the user acts.
  - Besides the `message` text, the dialog appends call stack information automatically (internally `debug_get_callstack` is concatenated into the text) to help locate the error source.
  - Abort: terminates the process immediately (the DLL performs the process exit with exit code 1); suitable for letting players close the game quickly on a crash.
  - Ignore: closes the dialog and continues running the game.
  - Copy: copies the current text to the clipboard so players can report the error easily.
  - Clear: clears the text box content (display only).
- Note: make sure `message` is never `undefined`; wrapping non-string values with `string(...)` is recommended.
- Use case: script exceptions, corrupted saves, missing configuration and other situations the player should know about, as a display alternative to `show_error` / `show_message`.

## Example

```gml
// Simulate an error that needs to be shown to the user
qiumingdll_init();

var errText = "Corrupted save detected!\r\nCannot read save.dat";
var choice = qiumingdll_show_error(errText);

// Execution only reaches here when Ignore (return value 5) or the dialog was closed (return value 2)
// On Abort the process has already terminated
if (choice == 5 || choice == 2)
{
    show_debug_message("User chose to ignore the error, attempting to restore the default save");
    // Continue the game logic...
}
```

## Related functions

- [qiumingdll_init](qiumingdll_init.md)
- [qiumingdll_show_error_ex](qiumingdll_show_error_ex.md)
- [qiumingdll_fixflash](qiumingdll_fixflash.md)
