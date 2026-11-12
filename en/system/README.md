# system module

Core functions: initialization and release (qiumingdll_init must be called before any other function), version query, window flicker fix, system menu control, error dialogs and external program execution.

10 functions in total.

## Function index

| Function | Description |
|------|------|
| [qiumingdll_disable_system_menu](qiumingdll_disable_system_menu.md) | Disables the game window's system menu and window operations so players cannot interfere with the game through the system menu. |
| [qiumingdll_execute_program](qiumingdll_execute_program.md) | Runs an external program or command line synchronously and returns its exit code once it has finished. |
| [qiumingdll_execute_program_async](qiumingdll_execute_program_async.md) | Starts an external program or command line asynchronously and returns immediately without waiting for it to finish. |
| [qiumingdll_fixflash](qiumingdll_fixflash.md) | Fixes flicker in the game window: clears the window class background brush so repaints no longer flash. |
| [qiumingdll_free](qiumingdll_free.md) | Releases the qiumingdll extension: unloads the DLL and reverts the initialized state, disabling every other qiumingdll function. |
| [qiumingdll_get_version](qiumingdll_get_version.md) | Returns the qiumingdll extension version as an integer, usable for runtime capability checks. |
| [qiumingdll_init](qiumingdll_init.md) | Initializes the qiumingdll extension: loads the DLL on Windows and binds all external functions; a prerequisite for every other qiumingdll function. |
| [qiumingdll_restore_system_menu](qiumingdll_restore_system_menu.md) | Restores the game window's system menu and window operations, undoing the interception installed by `qiumingdll_disable_system_menu()`. |
| [qiumingdll_show_error](qiumingdll_show_error.md) | Shows a blocking error dialog with a call stack (styled like a GameMaker crash report) to present error information to the user. |
| [qiumingdll_show_error_ex](qiumingdll_show_error_ex.md) | Shows a fully customizable blocking error dialog: custom title, body, button text, button behavior and button color. |

[Back to documentation home](../README.md)
