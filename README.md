# Kanagawa for Fish and Windows Terminal

Color themes for the [Fish shell](https://fishshell.com), [Windows Terminal](https://github.com/microsoft/terminal), and [VS Code](https://code.visualstudio.com), in all three Kanagawa variants:

| Variant | Appearance | Background |
| ------- | ---------- | ---------- |
| Wave    | Dark       | `#1F1F28`  |
| Dragon  | Dark       | `#181616`  |
| Lotus   | Light      | `#F2ECBC`  |

The terminal colors match [terminalcolors.com](https://terminalcolors.com/themes/kanagawa/). The Fish syntax colors follow the per-variant highlight groups in [kanagawa.nvim](https://github.com/rebelot/kanagawa.nvim).

## Fish

### Install

To install with [Fisher](https://github.com/jorgebucaran/fisher), run:

```fish
fisher install handsomefox/kanagawa
```

To install by hand, copy the files from [`themes/`](themes) to `~/.config/fish/themes/`.

### Choose a theme (Fish 4.3 and later)

Add one of these lines to `~/.config/fish/config.fish`:

```fish
fish_config theme choose kanagawa-wave
fish_config theme choose kanagawa-dragon
fish_config theme choose kanagawa-lotus
```

`kanagawa-wave` and `kanagawa-dragon` follow the terminal's color mode. They use Lotus when the terminal background is light. To keep the dark variant in every mode, add `--color-theme=dark`:

```fish
fish_config theme choose kanagawa-wave --color-theme=dark
```

`kanagawa-lotus` is always light. Don't pass `--color-theme` to it. The file has no `[dark]` section, so `--color-theme=dark` fails.

If you upgraded from Fish 4.2 or earlier, delete `~/.config/fish/conf.d/fish_frozen_theme.fish`. Otherwise it overrides the theme you choose.

### Choose a theme (Fish 4.2 and earlier)

Fish 4.2 and earlier can't read the `[light]` and `[dark]` sections. Use the single-variant files in [`static/`](static) instead. Fisher doesn't install these files. Don't combine them with a Fisher install, because they have the same file names.

1. Copy a file from `static/` to `~/.config/fish/themes/`.
2. Run `fish_config theme choose kanagawa-wave`, using the name of the file you copied.

## Windows Terminal

Each variant has two files in [`windows-terminal/`](windows-terminal):

- `<variant>.json` is the color scheme: the background, the foreground, the cursor, the selection, and the 16 ANSI colors.
- `<variant>Theme.json` is the theme: the tab, the tab row, and the light or dark window frame.

To add a variant:

1. Open Windows Terminal and press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>,</kbd> to open `settings.json`.
2. Paste the contents of `wave.json`, `dragon.json`, or `lotus.json` into the `schemes` array:

   ```jsonc
   "schemes": [
     {
       "name": "Kanagawa Wave",
       // ...
     }
   ]
   ```

3. Paste the contents of the matching `<variant>Theme.json` into the `themes` array.
4. Save the file.
5. In **Settings** > **Profiles**, select a profile, or select **Defaults** for all profiles.
6. In **Appearance** > **Color scheme**, select the Kanagawa variant.
7. In **Settings** > **Appearance** > **Theme**, select the matching theme.
8. Select **Save**.

## VS Code

This repository doesn't ship a VS Code extension. Instead, [`vscode/settings.json`](vscode/settings.json) recolors the [Catppuccin extension](https://github.com/catppuccin/vscode) through its `catppuccin.colorOverrides` and `catppuccin.customUIColors` settings. Each Kanagawa variant replaces one Catppuccin flavor:

| Select this theme      | To get          |
| ---------------------- | --------------- |
| Catppuccin Mocha       | Kanagawa Wave   |
| Catppuccin Macchiato   | Kanagawa Dragon |
| Catppuccin Latte       | Kanagawa Lotus  |

Catppuccin Frappe keeps its stock colors.

To set it up:

1. Install the [Catppuccin for VSCode](https://marketplace.visualstudio.com/items?itemName=Catppuccin.catppuccin-vsc) extension.
2. Run **Preferences: Open User Settings (JSON)** from the Command Palette.
3. Copy both keys from `vscode/settings.json` into your settings. If you already have either key, merge the flavor objects.
4. Select **Reload window** when Catppuccin asks. The extension writes its theme files when the settings change, and VS Code reads them only on reload.
5. Run **Preferences: Color Theme** and select the flavor from the table.

The overrides map Kanagawa's highlight roles onto Catppuccin's palette slots. For example, `mauve` colors keywords, so it gets Kanagawa's keyword color. The match isn't exact everywhere. Catppuccin reuses each slot for several roles, so a color can appear where Kanagawa wouldn't put it. `catppuccin.customUIColors` sets the selection, cursor, diagnostics, git decorations, and the 16 terminal colors directly.

## Regenerate the files

[`build.py`](build.py) holds the palettes and writes every file in `themes/`, `static/`, `windows-terminal/`, and `vscode/`. After you change a color, run:

```sh
python3 build.py
```

## Credits

- The Kanagawa palette comes from [rebelot/kanagawa.nvim](https://github.com/rebelot/kanagawa.nvim) by Tommaso Laurenzi, under the MIT license.
- [terminalcolors.com](https://terminalcolors.com/themes/kanagawa/) is the source of the terminal colors.
- [catppuccin/fish](https://github.com/catppuccin/fish) and [catppuccin/windows-terminal](https://github.com/catppuccin/windows-terminal) are the models for the file layout.
- The VS Code colors depend on [catppuccin/vscode](https://github.com/catppuccin/vscode) and its override settings.

## License

[MIT](LICENSE)
