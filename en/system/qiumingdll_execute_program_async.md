# qiumingdll_execute_program_async(path)

Starts an external program or command line asynchronously and returns immediately without waiting for it to finish.

## Signature

```gml
qiumingdll_execute_program_async(path)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| path | String | yes | Path of the program to run, or a complete command line. This can be the full path of an executable (e.g. `C:\tools\app.exe`), optionally with arguments (e.g. `C:\tools\app.exe --flag`); a command name that exists in `%PATH%` also works |

## Returns

| Value | Description |
|----|------|
| 1 | Started successfully (the child process was created) |
| 0 | Failed to start (invalid path, file not found, etc.), or called on a non-Windows platform |

## Usage

- Prerequisite: call `qiumingdll_init()` first on Windows.
- Platform limit: Windows only; always returns 0 on other platforms.
- Behavior: creates a child process via `CreateProcess` and returns immediately without waiting for it to finish, so the game keeps running normally.
- Difference from `qiumingdll_execute_program()`: this function only "starts" the process and does not care about its exit code afterwards — suitable for opening associated external programs, launching server processes, or bringing up tool windows where the result is not needed.
- Note: the return value only means "whether the process was created successfully"; it does not mean the child process keeps running or does not crash — for example, if the program reports an error and exits right after starting, this function still returns 1.
- When the path contains spaces, it is recommended to quote it as a whole in the parameter, e.g. `"C:\Program Files\Tool\tool.exe" --listen`.
- Consecutive asynchronous launches do not block each other, which makes it suitable for starting several external processes in bulk.

## Example

```gml
// Start an external tool asynchronously; the game does not need to wait
qiumingdll_init();

// Open a background music player
var ok = qiumingdll_execute_program_async("C:\\music\\player.exe D:\\songs\\bgm.mp3");
if (ok == 1)
{
    show_debug_message("Player started");
}
else
{
    show_debug_message("Failed to start player");
}

// Start two server processes in bulk; neither blocks the other
qiumingdll_execute_program_async("C:\\server\\web_server.exe");
qiumingdll_execute_program_async("C:\\server\\db_server.exe");
```

## Related functions

- [qiumingdll_execute_program](qiumingdll_execute_program.md)
- [qiumingdll_init](qiumingdll_init.md)
