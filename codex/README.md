# Kanagawa for the Codex desktop app

Each variant has a theme import string and a readable JSON payload. Choose a variant:

| Kanagawa variant | Import string | JSON payload | Appearance slot |
| ---------------- | ------------- | ------------ | --------------- |
| Wave             | [wave.txt](wave.txt) | [wave.json](wave.json) | Dark theme |
| Dragon           | [dragon.txt](dragon.txt) | [dragon.json](dragon.json) | Dark theme |
| Lotus            | [lotus.txt](lotus.txt) | [lotus.json](lotus.json) | Light theme |

## Install

1. Open **Settings > Appearance** in the Codex desktop app.
2. Select **Import** in the matching **Dark theme** or **Light theme** section.
3. Copy the entire line from the variant's `.txt` file, including the `codex-theme-v1:` prefix, and paste it into the import dialog.
4. Confirm the import. Set the app's **Theme** to **Dark**, **Light**, or **System** to choose when it applies.

Import Wave or Dragon into the dark slot and Lotus into the light slot to follow your system appearance.

## Colors and code highlighting

The background, foreground, accent, diff additions, diff removals, and skill colors use the shared Kanagawa palettes. Windows are opaque, fonts use the app defaults, and contrast is 60 for dark variants and 45 for Lotus. The app derives other interface colors from these settings.

The importer accepts built-in code-theme IDs, so these imports use `codex` for code highlighting. They do not add Kanagawa syntax highlighting or change the CLI's `tui.theme` setting. The import format follows the [DexThemes theme v1 contract](https://github.com/daeshawnballard/dexthemes/blob/main/shared/codex-theme-contract.js).

See the [official Appearance settings documentation](https://learn.chatgpt.com/docs/app/settings#appearance) for the app's theme controls.

[All supported tools](../README.md)
