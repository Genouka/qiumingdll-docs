# qiumingdll_json5_encode(value)

Encodes a GML value into a compact, readable JSON5-style string (keys unquoted, strings single-quoted, indented).

## Signature

```gml
qiumingdll_json5_encode(value)
```

## Parameters

| Parameter | Type | Required | Description |
|------|------|------|------|
| value | Any | Yes | Any GML value that can be serialized by `json_encode`: struct, ds_map, array, String, Real, Bool, undefined/null all work |

## Returns

| Value | Description |
|----|------|
| String | The encoded JSON5-style string. Example result: `{ name: 'Kris', level: 42, items: ['apple', 'pear'] }` |
| Empty string `""` | Returned when the passed value cannot be serialized or serialization fails |

## Usage

- Prerequisite: call `qiumingdll_init()` first on Windows.
- Platform support: on Windows the GML value is first converted to a standard JSON string by `json_encode`, then the DLL turns it into JSON5 style with pretty-printed indentation; on non-Windows platforms the function returns `json_encode(value)` directly (that is, standard JSON without JSON5 formatting).
- Behavior details (Windows):
  - Object keys: valid identifier keys are left unquoted (they start with a letter, `_` or `$`, contain only letters, digits, `_` and `$`, and are not a JS reserved word); all other keys keep double quotes;
  - Strings: always emitted with single quotes (single quotes inside the string content are escaped as `\'`);
  - Indentation: nested objects and arrays are broken onto new lines with 2-space indentation for easier reading.
- Note: `json_encode` fails on cyclic references or structs containing non-serializable content; in that case this function may return an empty string on Windows, so checking for an empty result after calling is recommended.
- Typical use: export data such as saves and settings to a human-readable, hand-editable configuration file, then read it back with `qiumingdll_json5_decode()`.
- The output is multi-line indented text; if you need a single-line compact output, strip the newlines and indentation yourself with GML string handling.

## Example

```gml
// Save the game configuration as a JSON5-style string
qiumingdll_init();

var config =
{
    name: "Kris",
    level: 42,
    inventory: ["apple", "pear", "sword"],
    settings:
    {
        sound: true,
        fullscreen: false,
    }
};

var json5Text = qiumingdll_json5_encode(config);
show_debug_message(json5Text);
// Output:
// {
//   name: 'Kris',
//   level: 42,
//   inventory: ['apple', 'pear', 'sword'],
//   settings: {
//     sound: true,
//     fullscreen: false
//   }
// }

// Save it to a file; it can later be read back with qiumingdll_json5_decode
// file_text_write_string(file_text_open_write("config.json5"), json5Text);
```

## Related functions

- [qiumingdll_json5_decode](qiumingdll_json5_decode.md)
- [qiumingdll_init](qiumingdll_init.md)
