# qiumingdll_execute_program(path)

Runs an external program or command line synchronously and returns its exit code once it has finished.

## Signature

```gml
qiumingdll_execute_program(path)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| path | String | yes | Path of the program to run, or a complete command line. This can be the full path of an executable (e.g. `C:\tools\app.exe`), optionally with arguments (e.g. `C:\tools\app.exe /silent`); a command name that exists in `%PATH%` (e.g. `notepad.exe`) also works |

## Returns

| Value | Description |
|----|------|
| 0 | The child process exited normally with exit code 0 (success) |
| non-zero integer | The child process exit code: a negative or non-zero integer usually means failure or external termination |
| -1 | Failed to start (invalid path, file not found, insufficient permissions, etc.), or called on a non-Windows platform |

## Usage

- Prerequisite: call `qiumingdll_init()` first on Windows.
- Platform limit: Windows only; always returns -1 on other platforms.
- Behavior: creates a child process via `CreateProcess` and waits for it to finish completely (waiting indefinitely), then returns the child process exit code.
- Important warning: this function is **synchronously blocking** — the game is completely frozen during the call until the child process exits. Never use it to launch player-interactive programs (Notepad, a browser, etc.), or the game will hang until the player closes that program.
- Use cases: silently invoking command line tools (automation scripts, archivers, screenshot tools); use `qiumingdll_execute_program_async()` when you need concurrent execution.
- When the path contains spaces, it is recommended to quote it as a whole in the parameter, e.g. `"C:\Program Files\Tool\tool.exe" --work`.
- The returned exit code is the program's own return value: 0 means success, non-zero depends on the program, and can be used to judge the execution result.

## Example

```gml
// Silently waiting for Notepad to exit is not a recommended usage (it hangs the game);
// the following is a suggested scenario: call an automation tool, wait for it, and
// judge the result from its exit code
qiumingdll_init();

var exitCode = qiumingdll_execute_program("C:\\tools\\patch_apply.exe -p game");

if (exitCode == 0)
{
    show_debug_message("Patch applied successfully");
}
else
{
    qiumingdll_show_error("Patch failed, exit code: " + string(exitCode));
}
```

## Related functions

- [qiumingdll_execute_program_async](qiumingdll_execute_program_async.md)
- [qiumingdll_show_error](qiumingdll_show_error.md)
- [qiumingdll_init](qiumingdll_init.md)
