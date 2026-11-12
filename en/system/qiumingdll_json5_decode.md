# qiumingdll_json5_decode(json5Text)

Parses JSON5 text (extended syntax with comments, single quotes, unquoted keys, and more) and returns the corresponding GML data structure.

## Signature

```gml
qiumingdll_json5_decode(json5Text)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| json5Text | String | yes | Text in JSON5 format. Supports many syntax extensions beyond standard JSON (see the notes below) |

## Returns

| Value | Description |
|----|------|
| struct / array / ds_map | On success, the GML data structure matching the content (the concrete type is determined by the underlying `json_decode`: objects become a struct or ds_map, arrays become an array) |
| the result of `json_decode("")` | Returned on parse failure (i.e. the result of decoding an empty string, usually some empty-data representation; no exception is thrown) |

## Usage

- Prerequisite: call `qiumingdll_init()` first on Windows.
- Platform limit: on Windows the DLL first converts JSON5 to standard JSON and then hands it to GML's `json_decode`; on non-Windows platforms it calls `json_decode(json5Text)` directly (i.e. JSON5 extension syntax is not supported, only standard JSON is accepted).
- Supported JSON5 extensions (Windows platform):
  - Comments: `// line comments` and `/* block comments */`;
  - Strings: both single quotes `'...'` and double quotes `"..."` work, with escapes such as `\x41` and `\u0041`;
  - Keys: object keys may be unquoted (bare identifiers, e.g. `{ name: "A" }`), and escapes such as `\n` and `\uXXXX` are supported in keys;
  - Trailing commas: an extra comma is allowed after the last element of an object or array;
  - Numbers: hexadecimal (`0xFF`), signed `Infinity`, `NaN` (decoded as null / a very large number), leading decimal point (`.5`), etc.;
  - Booleans and null: `true`, `false`, `null`.
- Failure behavior: malformed text (e.g. unclosed brackets, a key missing its colon, leftover stray characters) is treated as a parse failure and returns the result of `json_decode("")` without crashing. Validate the returned content after calling.
- Note: whether a parsed object ends up as a struct or a ds_map depends on the behavior of GML's `json_decode` at runtime; if you must get a ds_map, set the appropriate json options beforehand (which `json_*` buffer/format settings to use is up to the project).
- Typical use: reading human-written configuration files that contain comments.

## Example

```gml
// Read a JSON5 config with comments and single quotes
qiumingdll_init();

var json5Text = @"
{
  // Player configuration
  name: 'Kris',          // single-quoted string + unquoted key
  level: 0x2A,           // hexadecimal number (= 42)
  items: ['apple', 'pear',],
  boss: {
    hp: Infinity,
  }
}";

var cfg = qiumingdll_json5_decode(json5Text);
if (is_struct(cfg) || is_ds_map(cfg))
{
    show_debug_message("Player name: " + string(cfg.name));   // access depends on the returned type
}
```

## Related functions

- [qiumingdll_json5_encode](qiumingdll_json5_encode.md)
- [qiumingdll_init](qiumingdll_init.md)
