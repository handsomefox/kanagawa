# Kanagawa for Fish and Windows Terminal

Color themes for the [Fish shell](https://fishshell.com) and [Windows Terminal](https://github.com/microsoft/terminal), in all three Kanagawa variants:

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

Fish 4.2 and earlier can't read the `[light]` and `[dark]` sections. Use the single-variant files in [`static/`](static) instead. Fisher doesn't install these files.

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

## Regenerate the files

[`build.py`](build.py) holds the palettes and writes every file in `themes/` and `windows-terminal/`. After you change a color, run:

```sh
python3 build.py
```

## Credits

- The Kanagawa palette comes from [rebelot/kanagawa.nvim](https://github.com/rebelot/kanagawa.nvim) by Tommaso Laurenzi, under the MIT license.
- [terminalcolors.com](https://terminalcolors.com/themes/kanagawa/) is the source of the terminal colors.
- [catppuccin/fish](https://github.com/catppuccin/fish) and [catppuccin/windows-terminal](https://github.com/catppuccin/windows-terminal) are the models for the file layout.

## License

[MIT](LICENSE)
