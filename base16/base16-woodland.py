# -*- coding: utf-8 -*-

# base16-prompt-toolkit (https://github.com/memeplex/base16-prompt-toolkit)
# Base16 Prompt Toolkit template by Carlos Pita (carlosjosepita@gmail.com
# Woodland scheme by Jay Cornwall (https://jcornwall.com)

from prompt_toolkit.terminal.vt100_output import _256_colors
from pygments.style import Style
from pygments.token import (Keyword, Name, Comment, String, Error, Text,
                            Number, Operator, Literal, Token)

# See http://chriskempson.com/projects/base16/ for a description of the role
# of the different colors in the base16 palette.

base00 = '#231e18'
base01 = '#302b25'
base02 = '#48413a'
base03 = '#9d8b70'
base04 = '#b4a490'
base05 = '#cabcb1'
base06 = '#d7c8bc'
base07 = '#e4d4c8'
base08 = '#d35c5c'
base09 = '#ca7f32'
base0A = '#e0ac16'
base0B = '#b7ba53'
base0C = '#6eb958'
base0D = '#88a4d3'
base0E = '#bb90e2'
base0F = '#b49368'

# See https://github.com/jonathanslenders/python-prompt-toolkit/issues/355

colors = (globals()['base0' + d] for d in '08BADEC5379F1246')
for i, color in enumerate(colors):
    r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:], 16)
    _256_colors[r, g, b] = i + 6 if i > 8 else i

# See http://pygments.org/docs/tokens/ for a description of the different
# pygments tokens.

class Base16Style(Style):

    background_color = base00
    highlight_color = base02
    default_style = base05

    styles = {
        Text: base05,
        Error: '%s bold' % base08,
        Comment: base03,
        Keyword: base0E,
        Keyword.Constant: base0D,
        Keyword.Namespace: base0D,
        Name.Builtin: base0D,
        Name.Function: base0D,
        Name.Class: base0D,
        Name.Decorator: base0E,
        Name.Exception: base08,
        Number: base09,
        Operator.Word: base0D,
        Literal: base0B,
        String: base0B
    }

# See https://github.com/jonathanslenders/python-prompt-toolkit/blob/master/prompt_toolkit/styles/defaults.py
# for a description of prompt_toolkit related pseudo-tokens.

overrides = {
    Token.Prompt: base0B,
    Token.PromptNum: '%s bold' % base0B,
    Token.OutPrompt: base08,
    Token.OutPromptNum: '%s bold' % base08,
    Token.Menu.Completions.Completion: 'bg:%s %s' % (base01, base04),
    Token.Menu.Completions.Completion.Current: 'bg:%s %s' % (base04, base01),
    Token.MatchingBracket.Other: 'bg:%s %s' % (base03, base00)
}
