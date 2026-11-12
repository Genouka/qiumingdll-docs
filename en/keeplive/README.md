# keeplive module

System keep-alive: continuously wakes the system to prevent it from sleeping, locking the screen or turning the display off while the game is running.

3 functions in total.

## Function index

| Function | Description |
|------|------|
| [qiumingdll_keeplive_cleanup](qiumingdll_keeplive_cleanup.md) | Uninstall the window keep-alive message hook, stop keep-alive protection for the target window, and clear the internally recorded target-window state. |
| [qiumingdll_keeplive_init](qiumingdll_keeplive_init.md) | Install the "window keep-alive" message hook so the target window is not judged "not responding" by the system and closed or cleaned up; used for fullscreen / not-responding protection in web games. |
| [qiumingdll_keeplive_is_active](qiumingdll_keeplive_is_active.md) | Query whether the window keep-alive hook is currently installed; returns 1 when keep-alive is active and 0 when it is not installed. |

[Back to documentation home](../README.md)
