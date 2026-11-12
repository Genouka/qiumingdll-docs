# qiumingdll_json5_decode(json5_string)

Parses a JSON5 string into GameMaker data structures (DS Map / Array / primitive types). On Windows it prefers the JSON5 parser in the DLL; on non-Windows platforms it falls back to `json_decode`.

## Signature

```gml
qiumingdll_json5_decode(json5_string)
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| json5_string | String | yes | JSON5 text. JSON5 is a superset of JSON and supports comments (`//`, `/* */`), unquoted keys, single-quoted strings, trailing commas, hexadecimal numbers, etc. |

## Returns

| Value | Description |
|-------|-------------|
| DS Map / Array / Real / String | Parsed successfully: returns native GameMaker data structures depending on the content (objects/arrays are mapped to DS Map and Array). The returned structures must be released by the caller with `ds_map_destroy` etc. |
| Invalid value | Parse failed (for example, the string is empty or completely malformed); in that case you can fall back to `json_decode` on the structure |

## Usage

- Preconditions: on Windows, call `qiumingdll_init()` first; if it has not been initialized, or on a non-Windows platform, the function automatically falls back to the built-in `json_decode(argument0)`.
- Platform limits: the DLL path is available only on Windows; the fallback mode supports standard JSON only and does not accept JSON5 extensions such as comments or single quotes.
- Behavior details: the difference from standard `json_decode` is that the parser itself accepts JSON5 syntax; internally the function passes the GML string to the DLL, then converts the JSON text returned by the DLL into structures with `json_decode`.
- Note: parsed DS Maps must be destroyed manually to avoid memory leaks.

## Example

```gml
// JSON5 text with comments and unquoted keys
var str = "{ name: 'qiuming', // single quotes + comment" +
          "  version: 0x2a,  // hexadecimal" +
          "  tags: [a, b, c,], }";

var data = qiumingdll_json5_decode(str);
if (is_struct(data))
{
    show_debug_message(string(data.name));
    ds_map_destroy(data);
}
```

## Related functions

- [qiumingdll_json5_encode](qiumingdll_json5_encode.md)
