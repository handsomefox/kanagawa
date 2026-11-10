# Kanagawa for the Codex desktop app

Each variant has an import string for **Settings** > **Appearance** in the Codex desktop app.

| Variant | Import string | Appearance slot | Code theme |
| ------- | ------------- | --------------- | ---------- |
| Wave    | [wave.txt](wave.txt)     | Dark  | Tokyo Night |
| Dragon  | [dragon.txt](dragon.txt) | Dark  | Nord        |
| Lotus   | [lotus.txt](lotus.txt)   | Light | One Light   |

## Install

1. Open the `.txt` file for your variant and copy the whole line, including the `codex-theme-v1:` prefix.
2. In Codex, open **Settings** > **Appearance**.
3. In the dark or light section that matches the table, select **Import theme**.
4. Paste the line, then approve the import.

To follow your system's light or dark mode, import Wave or Dragon into the dark slot and Lotus into the light slot.

## Colors

The background, text, accent, diff, and skill colors come from the Kanagawa palette. Codex derives the rest of the interface from them.

Codex can't import syntax colors. It accepts only its built-in code themes, so each import picks the one whose colors are closest to the variant's kanagawa.nvim highlights. Code highlighting is close to Kanagawa but not identical.

The `.json` files show the same settings in readable form. [`build.py`](../build.py) generates both formats. The format follows the [DexThemes `codex-theme-v1` contract](https://github.com/daeshawnballard/dexthemes/blob/main/shared/codex-theme-contract.js).

[All supported tools](../README.md)
