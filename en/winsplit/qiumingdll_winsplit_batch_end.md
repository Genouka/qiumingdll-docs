# qiumingdll_winsplit_batch_end(splitId)

Ends batch recording for the given split window; only afterwards can batch_play / batch_play_frame_sync be called to play it.

## Signature

```gml
qiumingdll_winsplit_batch_end(splitId)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| splitId | Real | yes | Split window number, starting from 1, maximum 16 |

## Returns

| Value | Description |
|----|------|
| 1 | Recording ended |
| 0 | Invalid splitId (the split window does not exist); or non-Windows platform (fallback return value of the GML wrapper) |

## Usage

- Prerequisite: qiumingdll_winsplit_batch_begin must have been called to start recording.
- Platform support: Windows only; on other platforms the GML wrapper returns 0 directly.
- Ending recording only sets the state to "playable"; it does not play immediately. Playback requires another call to batch_play or batch_play_frame_sync.
- All commands added during recording are kept; to discard this recording, call qiumingdll_winsplit_batch_clear to clear it, or call batch_begin again (which clears it automatically).
- Even if no command was added, batch_end returns 1; but a later batch_play with a command count of 0 returns 0 (nothing is played).
- After ending, batch_begin can be called again to record a new sequence; the old commands are cleared.

## Example

```gml
// Key event: the complete "record -> end -> play" flow
if (keyboard_check_pressed(vk_enter))
{
    qiumingdll_winsplit_batch_begin(global.splitId);
    qiumingdll_winsplit_batch_add_region(global.splitId, 300, 200, 480, 360, 500);
    qiumingdll_winsplit_batch_add_wait(global.splitId, 300);
    qiumingdll_winsplit_batch_end(global.splitId);     // end recording (key step)
    qiumingdll_winsplit_batch_play(global.splitId, 1); // start playback
}
```

## Related functions

- [qiumingdll_winsplit_batch_begin](qiumingdll_winsplit_batch_begin.md)
- [qiumingdll_winsplit_batch_play](qiumingdll_winsplit_batch_play.md)
- [qiumingdll_winsplit_batch_play_frame_sync](qiumingdll_winsplit_batch_play_frame_sync.md)
- [qiumingdll_winsplit_batch_clear](qiumingdll_winsplit_batch_clear.md)
