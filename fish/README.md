# Kanagawa for Fish

The steps depend on your [Fish](https://fishshell.com) version. To check it, run `fish --version`.

## Fish 4.3 and later

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

## Fish 3.4 to 4.2

The files in [`themes/`](../themes) have `[light]` and `[dark]` sections, which these versions can't read. Fisher installs those files, so don't use Fisher on these versions. Fish 3.3 and earlier don't support theme files.

The commands use Wave. For another variant, replace `wave` with `dragon` or `lotus` in both steps.

1. Copy one file from [`static/`](../static):

   ```fish
   git clone https://github.com/handsomefox/kanagawa
   mkdir -p ~/.config/fish/themes
   cp kanagawa/static/kanagawa-wave.theme ~/.config/fish/themes/
   ```

2. Add this line to `~/.config/fish/config.fish`. The theme applies in new shells.

   ```fish
   fish_config theme choose kanagawa-wave
   ```

The theme file layout follows [catppuccin/fish](https://github.com/catppuccin/fish).

[All supported tools](../README.md)
