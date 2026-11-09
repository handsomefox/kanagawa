# Kanagawa for Windows Terminal

Each variant has a [Windows Terminal](https://github.com/microsoft/terminal) color scheme and a window theme for the tabs and the light or dark window.

| Variant | Color scheme | Window theme | Name in settings |
| ------- | ------------ | ------------ | ---------------- |
| Wave | [wave.json](wave.json) | [waveTheme.json](waveTheme.json) | `Kanagawa Wave` |
| Dragon | [dragon.json](dragon.json) | [dragonTheme.json](dragonTheme.json) | `Kanagawa Dragon` |
| Lotus | [lotus.json](lotus.json) | [lotusTheme.json](lotusTheme.json) | `Kanagawa Lotus` |

## Install

1. In Windows Terminal, press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>,</kbd> to open `settings.json`.
2. Paste the contents of `wave.json`, `dragon.json`, or `lotus.json` into the `schemes` array. If the array already has entries, add a comma after the last one.
3. If `settings.json` has no `themes` array, add `"themes": [],` on the line after the opening `{`. Paste the contents of the matching theme file, such as `waveTheme.json`, into the `themes` array, with a comma after any existing entry.
4. Set `"theme": "Kanagawa Wave"` at the top level. If the key is new, add it on the line after the opening `{`, with a comma at the end.
5. Set `"colorScheme": "Kanagawa Wave"` inside the existing `profiles` > `defaults` object.
6. Save `settings.json`.

For another variant, use `Kanagawa Dragon` or `Kanagawa Lotus` in steps 4 and 5. If either key already exists, change its value instead of adding a second one.

A profile that sets its own `colorScheme` ignores the one in `defaults`. To use the scheme in one profile only, set `colorScheme` in that profile instead.

The theme file layout follows [catppuccin/windows-terminal](https://github.com/catppuccin/windows-terminal).

[All supported tools](../README.md)
