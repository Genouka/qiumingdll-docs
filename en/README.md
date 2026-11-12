# qiumingdll Documentation

Complete function reference for the qiumingdll extension, a Windows-only extension for GameMaker.

> **Translation notice.** The [Chinese documentation](../README.md) is the authoritative source. This English copy is generated from it and may fall behind when Chinese pages are updated. The site shows an **outdated translation** banner on any English page whose Chinese source has changed since it was translated.

## Modules

| Module | Directory | Docs | Description |
|--------|-----------|------|-------------|
| Core | [system](system/) | 16 | `qiumingdll_init` / `free` / version / system menu / program execution / custom error dialogs, etc. |
| Process detection | [procdetect](procdetect/) | 10 | Detect Cheat Engine, streaming software, multiple instances and arbitrary processes; count by name, read command lines, CPU/memory/GPU usage; asynchronous background scanning by default, with an optional synchronous mode |
| Cursor | [cursor](cursor/) | 2 | Globally inverted cursor (the cursor moves opposite to the mouse); 8×F12 safety valve; restored automatically on exit |
| Window effects | [wineffect](wineffect/) | 9 | Window-level shake / outline distortion / tear effects; operates on the real window position and region without capturing window contents |
| Desktop | [desktop](desktop/) | 4 | Current login user name; desktop wallpaper backup / restore / set |
| Networking | [net](net/) | 15 | TCP host/client multiplayer: shared variables / shared instances / custom events / player list / disconnect notifications |
| Game window | [winself](winself/) | 8 | Opacity and irregular shapes for the game's own main window |
| JSON5 | [json5](json5/) | 2 | JSON5 encoding / decoding |
| Window splitting | [winsplit](winsplit/) | 65 | Multi-window split display, shape clipping, batch animation, 9-Patch auto-follow |
| WebView | [webview](webview/) | 41 | Embedded browser windows (standalone / child), 9-Patch auto-follow |
| IME | [ime](ime/) | 23 | IME candidates, pinyin, inline editing, polling |
| Microphone volume | [volume](volume/) | 10 | Peak / RMS / dB measurement and thresholds |
| Pitch detection | [pitch](pitch/) | 8 | Pitch / note detection from microphone input |
| Keep-alive | [keeplive](keeplive/) | 3 | Prevent the system from sleeping / turning off the screen |

216 function pages in total, covering all 210 GML wrapper functions under `gml/`; polymorphic functions such as webview/set_region are split into several pages.

## Documentation format

Every function page follows [doc-template.md](doc-template.md):

- Function signature and parameter descriptions
- Return value table
- Usage notes (preconditions, platform limits, caveats)
- GML example code
- Links to related functions

## Quick start

```gml
qiumingdll_init();              // 1. Initialize (Windows only)
qiumingdll_fixflash();          // 2. Optional: fix the Flash control
show_debug_message(qiumingdll_get_version());  // 3. Verify the extension version
```

See [system/qiumingdll_init.md](system/qiumingdll_init.md) for details.

## Keeping the translation in sync

- Each English page records the FNV-1a 64-bit hash of its Chinese source at translation time in [`_sync.json`](_sync.json). The English site re-hashes the live Chinese page and shows a warning banner when they differ.
- After updating Chinese documentation, re-translate the affected English page(s), then run `python tools/en_sync.py update` from the repository root and commit `en/_sync.json`.
- `python tools/en_sync.py status` lists stale, untracked, orphaned and untranslated pages. `python tools/en_sync.py verify` checks that every English page keeps the heading, code-block, table and link structure of its Chinese source.
