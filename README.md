# Kanagawa for Fish, Windows Terminal, VS Code, and Codex

Kanagawa color themes for the [Fish shell](https://fishshell.com), [Windows Terminal](https://github.com/microsoft/terminal), [VS Code](https://code.visualstudio.com), and the [Codex desktop app](https://learn.chatgpt.com/docs/app/settings#appearance), in three variants. Wave and Dragon are dark, and Lotus is light. In VS Code, the themes are settings for the Catppuccin extension.

## Fish

The steps depend on your Fish version. To check it, run `fish --version`.

### Fish 4.3 and later

1. Delete any of these files that exist:
   - `~/.config/fish/conf.d/fish_frozen_theme.fish`. Fish 4.3 creates it during an upgrade to keep your old colors, and it keeps applying them to anything Kanagawa doesn't set.
   - If you now install with Fisher, any `kanagawa-*.theme` files that you copied to `~/.config/fish/themes/` by hand. Fisher won't install over them.
2. Install the themes with [Fisher](https://github.com/jorgebucaran/fisher):

   ```fish
   fisher install handsomefox/kanagawa
   ```

   To install without Fisher, run:

   ```fish
   git clone https://github.com/handsomefox/kanagawa
   mkdir -p ~/.config/fish/themes
   cp kanagawa/themes/*.theme ~/.config/fish/themes/
   ```

3. Add this line to `~/.config/fish/config.fish`. For another variant, replace `wave` with `dragon` or `lotus`. The theme applies in new shells.

   ```fish
   fish_config theme choose kanagawa-wave
   ```

`kanagawa-wave` and `kanagawa-dragon` switch to Lotus when the terminal has a light background. If the terminal doesn't report its background, they stay dark. To keep the dark colors on a light background too, add `--color-theme=dark`:

```fish
fish_config theme choose kanagawa-wave --color-theme=dark
```

Don't use `--color-theme` with `kanagawa-lotus`. Its file has no `[light]` or `[dark]` sections, so the command fails.

If you installed with Fisher, run `fisher update handsomefox/kanagawa` to get theme updates.

### Fish 3.4 to 4.2

The files in `themes/` have `[light]` and `[dark]` sections, which these versions can't read. Fisher installs those files, so don't use Fisher on these versions. Fish 3.3 and earlier don't support theme files.

The commands use Wave. For another variant, replace `wave` with `dragon` or `lotus` in both steps.

1. Copy one file from [`static/`](static):

   ```fish
   git clone https://github.com/handsomefox/kanagawa
   mkdir -p ~/.config/fish/themes
   cp kanagawa/static/kanagawa-wave.theme ~/.config/fish/themes/
   ```

2. Add this line to `~/.config/fish/config.fish`. The theme applies in new shells.

   ```fish
   fish_config theme choose kanagawa-wave
   ```

## Windows Terminal

Each variant has a color scheme, such as [`windows-terminal/wave.json`](windows-terminal/wave.json), for the terminal colors. It also has a theme, such as [`windows-terminal/waveTheme.json`](windows-terminal/waveTheme.json), for the tabs and the light or dark window.

1. In Windows Terminal, press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>,</kbd> to open `settings.json`.
2. Paste the contents of `wave.json`, `dragon.json`, or `lotus.json` into the `schemes` array. If the array already has entries, add a comma after the last one.
3. If `settings.json` has no `themes` array, add `"themes": [],` on the line after the opening `{`. Paste the contents of the matching theme file, such as `waveTheme.json`, into the `themes` array, with a comma after any existing entry.
4. Set `"theme": "Kanagawa Wave"` at the top level. If the key is new, add it on the line after the opening `{`, with a comma at the end.
5. Set `"colorScheme": "Kanagawa Wave"` inside the existing `profiles` > `defaults` object.
6. Save `settings.json`.

For another variant, use `Kanagawa Dragon` or `Kanagawa Lotus` in steps 4 and 5. If either key already exists, change its value instead of adding a second one.

A profile that sets its own `colorScheme` ignores the one in `defaults`. To use the scheme in one profile only, set `colorScheme` in that profile instead.

## VS Code

[`vscode/settings.json`](vscode/settings.json) replaces the colors of three [Catppuccin for VSCode](https://marketplace.visualstudio.com/items?itemName=Catppuccin.catppuccin-vsc) flavors with Kanagawa colors. Each Kanagawa variant uses one flavor:

| Kanagawa variant | Catppuccin flavor to select |
| ---------------- | --------------------------- |
| Wave             | Catppuccin Mocha            |
| Dragon           | Catppuccin Macchiato        |
| Lotus            | Catppuccin Latte            |

Catppuccin Frappé keeps its own colors.

1. Install the Catppuccin for VSCode extension.
2. From the Command Palette, run **Preferences: Open User Settings (JSON)**.
3. Copy the `catppuccin.colorOverrides` and `catppuccin.customUIColors` keys from `vscode/settings.json`. Leave out the file's outer braces.
4. If your settings already have either key, merge the `mocha`, `macchiato`, and `latte` objects into it. Otherwise, paste both keys just before the final `}` of your settings, with a comma after the setting before them.
5. When Catppuccin asks, select **Reload window**.
6. Run **Preferences: Color Theme** and select the Catppuccin flavor for your variant.

The backgrounds, selection, cursor, git, and terminal colors match Kanagawa. Syntax colors are close but not exact, because Catppuccin uses each palette color for several kinds of code.

## Codex desktop app

Each variant has a theme import string and a readable JSON payload in [`codex/`](codex). Choose a variant:

| Kanagawa variant | Import string | Appearance slot |
| ---------------- | ------------- | --------------- |
| Wave             | [wave.txt](codex/wave.txt) | Dark theme |
| Dragon           | [dragon.txt](codex/dragon.txt) | Dark theme |
| Lotus            | [lotus.txt](codex/lotus.txt) | Light theme |

1. Open **Settings > Appearance** in the Codex desktop app.
2. Select **Import** in the matching **Dark theme** or **Light theme** section.
3. Copy the entire line from the variant's `.txt` file, including the `codex-theme-v1:` prefix, and paste it into the import dialog.
4. Confirm the import. Set the app's **Theme** to **Dark**, **Light**, or **System** to choose when it applies.

Import Wave or Dragon into the dark slot and Lotus into the light slot to follow your system appearance.

The background, foreground, accent, diff additions, diff removals, and skill colors use the shared Kanagawa palettes. Windows are opaque, fonts use the app defaults, and contrast is 60 for dark variants and 45 for Lotus. The app derives other interface colors from these settings.

The importer accepts built-in code-theme IDs, so these imports use `codex` for code highlighting. They do not add Kanagawa syntax highlighting or change the CLI's `tui.theme` setting. The import format follows the [DexThemes theme v1 contract](https://github.com/daeshawnballard/dexthemes/blob/main/shared/codex-theme-contract.js).

## Change the colors

The palettes are in [`build.py`](build.py), which needs Python 3.9 or later. After you edit a color, run it to regenerate every file in `themes/`, `static/`, `windows-terminal/`, `vscode/`, and `codex/`:

```sh
python3 build.py
```

## Credits

- The Kanagawa palette and the Fish syntax colors come from [rebelot/kanagawa.nvim](https://github.com/rebelot/kanagawa.nvim) by Tommaso Laurenzi, under the MIT license.
- The terminal colors come from [terminalcolors.com](https://terminalcolors.com/themes/kanagawa/).
- The VS Code colors are overrides for [catppuccin/vscode](https://github.com/catppuccin/vscode).
- The file layout follows [catppuccin/fish](https://github.com/catppuccin/fish) and [catppuccin/windows-terminal](https://github.com/catppuccin/windows-terminal).

## License

[MIT](LICENSE)
