#!/usr/bin/env python3
"""Generate the Fish, Windows Terminal, and VS Code theme files from the Kanagawa palette.

Terminal colors come from https://terminalcolors.com/themes/kanagawa/.
Syntax and UI roles come from rebelot/kanagawa.nvim (lua/kanagawa/themes.lua).

Run from the repository root: python3 build.py
"""

import json
from pathlib import Path
from typing import TypedDict

ROOT = Path(__file__).resolve().parent
URL = "https://github.com/handsomefox/kanagawa"


class Variant(TypedDict):
    name: str
    appearance: str
    term: dict[str, str]
    ui: dict[str, str]
    syn: dict[str, str]
    status: dict[str, str]


VARIANTS: dict[str, Variant] = {
    "wave": {
        "name": "Kanagawa Wave",
        "appearance": "dark",
        "term": {
            "background": "#1f1f28",
            "foreground": "#dcd7ba",
            "cursor": "#dcd7ba",
            "selection": "#2d4f67",
            "black": "#16161d",
            "red": "#c34043",
            "green": "#76946a",
            "yellow": "#c0a36e",
            "blue": "#7e9cd8",
            "purple": "#957fb8",
            "cyan": "#6a9589",
            "white": "#c8c093",
            "brightBlack": "#727169",
            "brightRed": "#e82424",
            "brightGreen": "#98bb6c",
            "brightYellow": "#e6c384",
            "brightBlue": "#7fb4ca",
            "brightPurple": "#938aa9",
            "brightCyan": "#7aa89f",
            "brightWhite": "#dcd7ba",
        },
        "ui": {
            "fg": "#dcd7ba",  # fujiWhite
            "bg": "#1f1f28",  # sumiInk3
            "bg_m2": "#181820",  # sumiInk1
            "bg_m3": "#16161d",  # sumiInk0
            "bg_p1": "#2a2a37",  # sumiInk4
            "bg_p2": "#363646",  # sumiInk5
            "bg_visual": "#223249",  # waveBlue1
            "bg_search": "#2d4f67",  # waveBlue2
            "pmenu_bg_sel": "#2d4f67",  # waveBlue2
            "fg_dim": "#c8c093",  # oldWhite
            "special": "#938aa9",  # springViolet1
            "nontext": "#54546d",  # sumiInk6
        },
        "syn": {
            "string": "#98bb6c",  # springGreen
            "number": "#d27e99",  # sakuraPink
            "constant": "#ffa066",  # surimiOrange
            "special2": "#e46876",  # waveRed
            "identifier": "#e6c384",  # carpYellow
            "parameter": "#b8b4d0",  # oniViolet2
            "fun": "#7e9cd8",  # crystalBlue
            "keyword": "#957fb8",  # oniViolet
            "operator": "#c0a36e",  # boatYellow2
            "type": "#7aa89f",  # waveAqua2
            "regex": "#c0a36e",  # boatYellow2
            "comment": "#727169",  # fujiGray
            "special1": "#7fb4ca",  # springBlue
            "error": "#e82424",  # samuraiRed
        },
        "status": {
            "warning": "#ff9e3b",  # roninYellow
            "info": "#658594",  # dragonBlue
            "hint": "#6a9589",  # waveAqua1
            "added": "#76946a",  # autumnGreen
            "changed": "#dca561",  # autumnYellow
            "removed": "#c34043",  # autumnRed
        },
    },
    "dragon": {
        "name": "Kanagawa Dragon",
        "appearance": "dark",
        "term": {
            "background": "#181616",
            "foreground": "#c5c9c5",
            "cursor": "#c5c9c5",
            "selection": "#2d4f67",
            "black": "#0d0c0c",
            "red": "#c4746e",
            "green": "#8a9a7b",
            "yellow": "#c4b28a",
            "blue": "#8ba4b0",
            "purple": "#a292a3",
            "cyan": "#8ea4a2",
            "white": "#c8c093",
            "brightBlack": "#a6a69c",
            "brightRed": "#e46876",
            "brightGreen": "#87a987",
            "brightYellow": "#e6c384",
            "brightBlue": "#7fb4ca",
            "brightPurple": "#938aa9",
            "brightCyan": "#7aa89f",
            "brightWhite": "#c5c9c5",
        },
        "ui": {
            "fg": "#c5c9c5",  # dragonWhite
            "bg": "#181616",  # dragonBlack3
            "bg_m2": "#12120f",  # dragonBlack1
            "bg_m3": "#0d0c0c",  # dragonBlack0
            "bg_p1": "#282727",  # dragonBlack4
            "bg_p2": "#393836",  # dragonBlack5
            "bg_visual": "#223249",  # waveBlue1
            "bg_search": "#2d4f67",  # waveBlue2
            "pmenu_bg_sel": "#2d4f67",  # waveBlue2
            "fg_dim": "#c8c093",  # oldWhite
            "special": "#7a8382",  # dragonGray3
            "nontext": "#625e5a",  # dragonBlack6
        },
        "syn": {
            "string": "#8a9a7b",  # dragonGreen2
            "number": "#a292a3",  # dragonPink
            "constant": "#b6927b",  # dragonOrange
            "special2": "#c4746e",  # dragonRed
            "identifier": "#c4b28a",  # dragonYellow
            "parameter": "#a6a69c",  # dragonGray
            "fun": "#8ba4b0",  # dragonBlue2
            "keyword": "#8992a7",  # dragonViolet
            "operator": "#c4746e",  # dragonRed
            "type": "#8ea4a2",  # dragonAqua
            "regex": "#c4746e",  # dragonRed
            "comment": "#737c73",  # dragonAsh
            "special1": "#949fb5",  # dragonTeal
            "error": "#e82424",  # samuraiRed
        },
        "status": {
            "warning": "#ff9e3b",  # roninYellow
            "info": "#658594",  # dragonBlue
            "hint": "#6a9589",  # waveAqua1
            "added": "#76946a",  # autumnGreen
            "changed": "#dca561",  # autumnYellow
            "removed": "#c34043",  # autumnRed
        },
    },
    "lotus": {
        "name": "Kanagawa Lotus",
        "appearance": "light",
        "term": {
            "background": "#f2ecbc",
            "foreground": "#545464",
            "cursor": "#545464",
            "selection": "#c9cbd1",
            "black": "#1f1f28",
            "red": "#c84053",
            "green": "#6f894e",
            "yellow": "#77713f",
            "blue": "#4d699b",
            "purple": "#b35b79",
            "cyan": "#597b75",
            "white": "#545464",
            "brightBlack": "#8a8980",
            "brightRed": "#d7474b",
            "brightGreen": "#6e915f",
            "brightYellow": "#836f4a",
            "brightBlue": "#6693bf",
            "brightPurple": "#624c83",
            "brightCyan": "#5e857a",
            "brightWhite": "#43436c",
        },
        "ui": {
            "fg": "#545464",  # lotusInk1
            "bg": "#f2ecbc",  # lotusWhite3
            "bg_m2": "#dcd5ac",  # lotusWhite1
            "bg_m3": "#d5cea3",  # lotusWhite0
            "bg_p1": "#e7dba0",  # lotusWhite4
            "bg_p2": "#e4d794",  # lotusWhite5
            "bg_visual": "#c9cbd1",  # lotusViolet3
            "bg_search": "#b5cbd2",  # lotusBlue2
            "pmenu_bg_sel": "#9fb5c9",  # lotusBlue3
            "fg_dim": "#43436c",  # lotusInk2
            "special": "#766b90",  # lotusViolet2
            "nontext": "#a09cac",  # lotusViolet1
        },
        "syn": {
            "string": "#6f894e",  # lotusGreen
            "number": "#b35b79",  # lotusPink
            "constant": "#cc6d00",  # lotusOrange
            "special2": "#c84053",  # lotusRed
            "identifier": "#77713f",  # lotusYellow
            "parameter": "#5d57a3",  # lotusBlue5
            "fun": "#4d699b",  # lotusBlue4
            "keyword": "#624c83",  # lotusViolet4
            "operator": "#836f4a",  # lotusYellow2
            "type": "#597b75",  # lotusAqua
            "regex": "#836f4a",  # lotusYellow2
            "comment": "#8a8980",  # lotusGray3
            "special1": "#6693bf",  # lotusTeal2
            "error": "#e82424",  # lotusRed3
        },
        "status": {
            "warning": "#e98a00",  # lotusOrange2
            "info": "#5a7785",  # lotusTeal3
            "hint": "#5e857a",  # lotusAqua2
            "added": "#6e915f",  # lotusGreen2
            "changed": "#de9800",  # lotusYellow3
            "removed": "#d7474b",  # lotusRed2
        },
    },
}

# Theme files that follow the terminal's light/dark mode (fish 4.3+).
# Lotus is the light half of each dark variant, as Latte is for Catppuccin.
ADAPTIVE = {"wave": ("lotus", "wave"), "dragon": ("lotus", "dragon")}

# Windows Terminal color names, in ANSI order.
ANSI_COLORS = (
    "black",
    "red",
    "green",
    "yellow",
    "blue",
    "purple",
    "cyan",
    "white",
    "brightBlack",
    "brightRed",
    "brightGreen",
    "brightYellow",
    "brightBlue",
    "brightPurple",
    "brightCyan",
    "brightWhite",
)

# The Catppuccin flavor that each variant replaces in VS Code. Frappe stays stock.
VSCODE_FLAVORS = {"wave": "mocha", "dragon": "macchiato", "lotus": "latte"}


def hx(color: str) -> str:
    return color.lstrip("#")


def fish_body(variant: Variant) -> list[str]:
    ui, syn = variant["ui"], variant["syn"]
    rows = [
        ("fish_color_normal", hx(ui["fg"])),
        ("fish_color_command", hx(syn["fun"])),
        ("fish_color_keyword", hx(syn["keyword"])),
        ("fish_color_param", hx(syn["parameter"])),
        ("fish_color_option", hx(syn["special1"])),
        ("fish_color_quote", hx(syn["string"])),
        ("fish_color_redirection", hx(syn["operator"])),
        ("fish_color_operator", hx(syn["operator"])),
        ("fish_color_end", hx(syn["constant"])),
        ("fish_color_escape", hx(syn["regex"])),
        ("fish_color_comment", hx(syn["comment"])),
        ("fish_color_autosuggestion", hx(syn["comment"])),
        ("fish_color_error", hx(syn["error"])),
        ("fish_color_cancel", hx(syn["error"])),
        ("fish_color_status", hx(syn["error"])),
        ("fish_color_gray", hx(syn["comment"])),
        ("fish_color_valid_path", "--underline"),
        ("fish_color_history_current", "--bold"),
        ("fish_color_selection", f"--background={hx(ui['bg_visual'])}"),
        ("fish_color_search_match", f"--background={hx(ui['bg_search'])}"),
        ("fish_color_cwd", hx(syn["identifier"])),
        ("fish_color_cwd_root", hx(syn["error"])),
        ("fish_color_user", hx(syn["type"])),
        ("fish_color_host", hx(syn["fun"])),
        ("fish_color_host_remote", hx(syn["string"])),
        ("fish_pager_color_progress", hx(syn["comment"])),
        ("fish_pager_color_prefix", f"{hx(syn['identifier'])} --bold"),
        ("fish_pager_color_completion", hx(ui["fg"])),
        ("fish_pager_color_description", hx(syn["comment"])),
        (
            "fish_pager_color_selected_background",
            f"--background={hx(ui['pmenu_bg_sel'])}",
        ),
    ]
    return [f"# preferred_background: {hx(ui['bg'])}"] + [f"{k} {v}" for k, v in rows]


def fish_header(name: str) -> list[str]:
    return [f"# name: '{name}'", f"# url: '{URL}'", ""]


def write(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n")


def build_fish() -> None:
    themes = ROOT / "themes"
    for key, (light, dark) in ADAPTIVE.items():
        lines = fish_header(VARIANTS[key]["name"])
        for section, source in (("light", light), ("dark", dark), ("unknown", dark)):
            lines += [f"[{section}]", *fish_body(VARIANTS[source]), ""]
        write(themes / f"kanagawa-{key}.theme", lines[:-1])

    # Lotus on its own: no sections, so it stays light in any terminal mode.
    lotus = VARIANTS["lotus"]
    write(
        themes / "kanagawa-lotus.theme", fish_header(lotus["name"]) + fish_body(lotus)
    )

    # Single-mode files for fish 4.2 and earlier, which do not read sections.
    # They live outside themes/ because Fisher copies everything in themes/.
    for key, variant in VARIANTS.items():
        write(
            ROOT / "static" / f"kanagawa-{key}.theme",
            fish_header(variant["name"]) + fish_body(variant),
        )


def build_windows_terminal() -> None:
    out = ROOT / "windows-terminal"
    for key, variant in VARIANTS.items():
        term, ui = variant["term"], variant["ui"]
        scheme = {
            "name": variant["name"],
            "cursorColor": term["cursor"],
            "selectionBackground": term["selection"],
            "background": term["background"],
            "foreground": term["foreground"],
        }
        for color in ANSI_COLORS:
            scheme[color] = term[color]
        scheme = {k: v.upper() if v.startswith("#") else v for k, v in scheme.items()}

        theme = {
            "name": variant["name"],
            "tab": {
                "background": f"{ui['bg'].upper()}FF",
                "showCloseButton": "always",
                "unfocusedBackground": None,
            },
            "tabRow": {
                "background": f"{ui['bg_m2'].upper()}FF",
                "unfocusedBackground": f"{ui['bg_m3'].upper()}FF",
            },
            "window": {"applicationTheme": variant["appearance"]},
        }
        write(out / f"{key}.json", [json.dumps(scheme, indent=2)])
        write(out / f"{key}Theme.json", [json.dumps(theme, indent=2)])


def vscode_palette(variant: Variant) -> dict[str, str]:
    """Map Kanagawa roles onto the Catppuccin palette slots the extension uses."""
    ui, syn, status = variant["ui"], variant["syn"], variant["status"]
    return {
        "rosewater": ui["fg_dim"],
        "flamingo": syn["number"],
        "pink": syn["regex"],
        "mauve": syn["keyword"],
        "red": syn["special2"],
        "maroon": syn["parameter"],
        "peach": syn["constant"],
        "yellow": syn["type"],
        "green": syn["string"],
        "teal": syn["operator"],
        "sky": syn["special1"],
        "sapphire": status["hint"],
        "blue": syn["fun"],
        "lavender": syn["identifier"],
        "text": ui["fg"],
        "subtext1": ui["fg_dim"],
        "subtext0": ui["special"],
        "overlay2": syn["comment"],
        "overlay1": ui["nontext"],
        "overlay0": ui["nontext"],
        "surface2": ui["nontext"],
        "surface1": ui["bg_p2"],
        "surface0": ui["bg_p1"],
        "base": ui["bg"],
        "mantle": ui["bg_m2"],
        "crust": ui["bg_m3"],
    }


def vscode_ui_colors(variant: Variant) -> dict[str, str]:
    """Workbench colors that no palette slot can express."""
    ui, syn, status, term = (
        variant["ui"],
        variant["syn"],
        variant["status"],
        variant["term"],
    )
    colors = {
        "editor.selectionBackground": ui["bg_visual"],
        "editorCursor.foreground": term["cursor"],
        "editorError.foreground": syn["error"],
        "editorWarning.foreground": status["warning"],
        "editorInfo.foreground": status["info"],
        "gitDecoration.addedResourceForeground": status["added"],
        "gitDecoration.untrackedResourceForeground": status["added"],
        "gitDecoration.modifiedResourceForeground": status["changed"],
        "gitDecoration.deletedResourceForeground": status["removed"],
        "editorGutter.addedBackground": status["added"],
        "editorGutter.modifiedBackground": status["changed"],
        "editorGutter.deletedBackground": status["removed"],
        "terminalCursor.foreground": term["cursor"],
        "terminal.selectionBackground": term["selection"],
    }
    # Catppuccin takes terminal colors from its own palette, not the overrides.
    for color in ANSI_COLORS:
        name = color.replace("purple", "magenta").replace("Purple", "Magenta")
        colors[f"terminal.ansi{name[0].upper()}{name[1:]}"] = term[color]
    return colors


def build_vscode() -> None:
    settings = {
        "catppuccin.colorOverrides": {
            flavor: vscode_palette(VARIANTS[key])
            for key, flavor in VSCODE_FLAVORS.items()
        },
        "catppuccin.customUIColors": {
            flavor: vscode_ui_colors(VARIANTS[key])
            for key, flavor in VSCODE_FLAVORS.items()
        },
    }
    write(ROOT / "vscode" / "settings.json", [json.dumps(settings, indent=2)])


def build_codex() -> None:
    """Build desktop Appearance imports, using Codex's built-in code palette."""
    out = ROOT / "codex"
    for key, variant in VARIANTS.items():
        ui, syn, status = variant["ui"], variant["syn"], variant["status"]
        payload = {
            "codeThemeId": "codex",
            "theme": {
                "accent": syn["fun"],
                "contrast": 60 if variant["appearance"] == "dark" else 45,
                "fonts": {"code": None, "ui": None},
                "ink": ui["fg"],
                "opaqueWindows": True,
                "semanticColors": {
                    "diffAdded": status["added"],
                    "diffRemoved": status["removed"],
                    "skill": syn["keyword"],
                },
                "surface": ui["bg"],
            },
            "variant": variant["appearance"],
        }
        write(out / f"{key}.json", [json.dumps(payload, indent=2)])
        share = "codex-theme-v1:" + json.dumps(payload, separators=(",", ":"))
        write(out / f"{key}.txt", [share])


if __name__ == "__main__":
    build_fish()
    build_windows_terminal()
    build_vscode()
    build_codex()
