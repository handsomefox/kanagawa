# Kanagawa for VS Code

[settings.json](settings.json) replaces the colors of three [Catppuccin for VSCode](https://marketplace.visualstudio.com/items?itemName=Catppuccin.catppuccin-vsc) flavors with Kanagawa colors. Each Kanagawa variant uses one flavor:

| Kanagawa variant | Catppuccin flavor to select |
| ---------------- | --------------------------- |
| Wave             | Catppuccin Mocha            |
| Dragon           | Catppuccin Macchiato        |
| Lotus            | Catppuccin Latte            |

Catppuccin Frappé keeps its own colors.

## Install

1. Install the Catppuccin for VSCode extension.
2. From the Command Palette, run **Preferences: Open User Settings (JSON)**.
3. Copy the `catppuccin.colorOverrides` and `catppuccin.customUIColors` keys from [settings.json](settings.json). Leave out the file's outer braces.
4. If your settings already have either key, merge the `mocha`, `macchiato`, and `latte` objects into it. Otherwise, paste both keys just before the final `}` of your settings, with a comma after the setting before them.
5. When Catppuccin asks, select **Reload window**.
6. Run **Preferences: Color Theme** and select the Catppuccin flavor for your variant.

The backgrounds, selection, cursor, git, and terminal colors match Kanagawa. Syntax colors are close but not exact, because Catppuccin uses each palette color for several kinds of code.

The colors are overrides for [catppuccin/vscode](https://github.com/catppuccin/vscode).

[All supported tools](../README.md)
