# qiumingdll_procdetect_cheatengine()

Detects whether common cheating and debugging tools exist among system processes, for anti-cheat or for reporting an abnormal environment.

## Signature

```gml
qiumingdll_procdetect_cheatengine()
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| (none) | - | - | This function takes no parameters |

## Returns

| Value | Description |
|----|------|
| 1 | At least one cheating/debugging tool process is running |
| 0 | No target process detected, or called on a non-Windows platform |

## Usage

- Prerequisite: call `qiumingdll_init()` first on Windows.
- Platform support: Windows only; other platforms always return 0.
- Behavior: internally walks a snapshot of system processes and compares each process name (case-insensitive, exact exe file name) against a built-in list, returning 1 on the first hit. The built-in list includes:
  - Memory editing/cheating tools: Cheat Engine (cheatengine.exe, cheat engine.exe, cheatengine-x86_64.exe, etc.), ArtMoney (artmoney.exe), GameConqueror (gameconqueror.exe), scanmem.exe, etc.;
  - Debuggers/disassemblers: x64dbg, x32dbg, x96dbg, OllyDbg (ollydbg.exe, ollyice.exe), WinDbg (windbg.exe), IDA (ida.exe, ida64.exe, idag.exe, idaq64.exe), Ghidra (ghidra.exe), etc.;
  - System monitoring tools: Process Hacker (processhacker.exe), Process Monitor (procmon.exe, procmon64.exe), Process Explorer (procexp.exe, procexp64.exe), etc.
- Detection works by "comparing process names against a list", so it only works for the **default executable file names** of the listed tools; renamed tools may go undetected, and false positives are possible (other programs with the same file name).
- Note: this function performs no blocking action, it only returns the detection result; whether to warn the player or exit the game is up to the caller.
- Detection is snapshot-based: processes started or terminated after the check do not affect the current result; poll per frame or at an interval if you need real-time monitoring.

## Example

```gml
// Detect cheating tools at game start; notify and quit if found
qiumingdll_init();

if (qiumingdll_procdetect_cheatengine() == 1)
{
    qiumingdll_show_error("A cheating/debugging tool was detected; the game will exit");
    game_end();
}
else
{
    show_debug_message("Environment clean, game running normally");
}
```

## Related functions

- [qiumingdll_procdetect_streaming](qiumingdll_procdetect_streaming.md)
- [qiumingdll_procdetect_process](qiumingdll_procdetect_process.md)
- [qiumingdll_procdetect_multiinstance](qiumingdll_procdetect_multiinstance.md)
- [qiumingdll_init](qiumingdll_init.md)
