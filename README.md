# Kanagawa

Kanagawa color themes in three variants. **Wave** and **Dragon** are dark, and **Lotus** is light.

## Supported tools

Choose a tool for installation instructions.

| Tool | Theme support |
| ---- | ------------- |
| [Fish](fish/README.md) | Adaptive themes for Fish 4.3+, fixed themes for Fish 3.4 to 4.2 |
| [Windows Terminal](windows-terminal/README.md) | Terminal color schemes and window themes |
| [VS Code](vscode/README.md) | Color overrides for the Catppuccin extension |
| [Codex desktop app](codex/README.md) | Appearance imports with Kanagawa interface and diff colors |

## Change the colors

Edit the palettes in [`build.py`](build.py), then regenerate the theme files with Python 3.9 or later:

```sh
python3 build.py
```

## Credits

- The Kanagawa palette and the Fish syntax colors come from [rebelot/kanagawa.nvim](https://github.com/rebelot/kanagawa.nvim) by Tommaso Laurenzi, under the MIT license.
- The terminal colors come from [terminalcolors.com](https://terminalcolors.com/themes/kanagawa/).

## License

[MIT](LICENSE)
