# wineffect module

Window-level effects: directly change the **position and shape of the game window itself** — no screen capture, no window content copying, no overlay created. Suitable for cutscenes, glitch/horror segments, prank levels and similar scenarios.

The three effects can be enabled individually or simultaneously, each with its own strength control (0.0 ~ 1.0), while a single speed multiplier controls the overall animation pace.

| Effect | Target | Implementation |
|------|----------|----------|
| Shake | Window position | `SetWindowPos` moves the real window along a sinusoidal path; max displacement about 24px |
| Distort | Window outline | `SetWindowRgn` shrinks the left/right edges row by row in a sine wave; max shrink about 48px |
| Tear | Window outline + position | `SetWindowRgn` generates misaligned horizontal strips, notches and vertical cracks, plus window jumps |

> Distort/tear change the **window outline and visible area**; the image is clipped along with the window region. This module does no image resampling (that belongs to window-content effects). Areas clipped off the window expose the desktop / underlying windows directly.

- The animation is driven on the game window's UI thread via a 16ms `WM_TIMER` + window subclassing; no background thread is created.
- On stop/cleanup the window's original position is restored; when enabling (`set_enabled(1)`) any existing `SetWindowRgn` region of the window is saved as well and restored on stop.
- When the window is minimized, invisible or loses the foreground, effects pause automatically and restore; they resume once the window is back in the foreground.
- A maximized window cannot be moved; shake/tear jumps are skipped automatically, but the region effects still work.
- Under Exclusive Fullscreen the effects may be invisible; windowed / borderless fullscreen works fine.
- Do not use at the same time as winself's shaped windows: both modify the window region, and whichever is set later overrides the previous one.

9 functions in total.

## Function index

| Function | Description |
|------|------|
| [qiumingdll_wineffect_init](qiumingdll_wineffect_init.md) | Binds the game window (does not start any effect). |
| [qiumingdll_wineffect_set_enabled](qiumingdll_wineffect_set_enabled.md) | Master switch: enable / stop and restore the window. |
| [qiumingdll_wineffect_set_shake](qiumingdll_wineffect_set_shake.md) | Sets the window shake strength. |
| [qiumingdll_wineffect_set_distort](qiumingdll_wineffect_set_distort.md) | Sets the window outline distortion strength. |
| [qiumingdll_wineffect_set_tear](qiumingdll_wineffect_set_tear.md) | Sets the window tearing strength. |
| [qiumingdll_wineffect_set_speed](qiumingdll_wineffect_set_speed.md) | Sets the animation speed multiplier. |
| [qiumingdll_wineffect_stop](qiumingdll_wineffect_stop.md) | Stops immediately and zeroes all three strengths. |
| [qiumingdll_wineffect_get_state](qiumingdll_wineffect_get_state.md) | Queries enabled / per-effect / actively running state. |
| [qiumingdll_wineffect_cleanup](qiumingdll_wineffect_cleanup.md) | Unbinds the window and releases all resources. |

[Back to documentation home](../README.md)
