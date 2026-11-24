#!/usr/bin/env python3
"""Generate the editor-inspired night themes (Dracula, T3 Chat, Monokai, Monokai Pro).

Edit the palettes in P, then run from the repo root:
    python3 tools/generate_editor_themes.py
It rewrites common/android/src/main/res/values/theme_editor_dark.xml and the
matching block at the end of AnkiDroid/src/main/assets/flashcard.css.
"""
import sys
XML = 'common/android/src/main/res/values/theme_editor_dark.xml'
CSS = 'AnkiDroid/src/main/assets/flashcard.css'
def hx(c): c=c.lstrip('#'); return [int(c[i:i+2],16) for i in (0,2,4)]
def mix(a,b,t):  # t of a over b
    A,B=hx(a),hx(b); return '#%02X%02X%02X'%tuple(round(x*t+y*(1-t)) for x,y in zip(A,B))

# name -> palette
P = {
 'Dracula': dict(bg='#282A36', bar='#21222C', surf='#2E303E', high='#44475A', fg='#F8F8F2', dim='#6272A4',
   outline='#44475A', primary='#FF79C6', onPrimary='#282A36', secondary='#BD93F9', tertiary='#8BE9FD',
   red='#FF5555', orange='#FFB86C', green='#50FA7B', blue='#8BE9FD', yellow='#F1FA8C', select='#44475A',
   fab='#FF79C6', link='#8BE9FD'),
 'T3Chat': dict(bg='#221D27', bar='#1C1720', surf='#28222D', high='#2C2632', fg='#D2C4DE', dim='#C2B6CF',
   outline='#3B3237', primary='#DB2777', onPrimary='#FFFFFF', secondary='#EFC0D8', tertiary='#C2B6CF',
   red='#F06A8A', orange='#F2A65A', green='#7BC99A', blue='#9FA8F0', yellow='#F5D67B', select='#463753',
   fab='#A3004C', container='#A3004C', onContainer='#EFC0D8', secContainer='#362D3D', link='#F472B6'),
 'Monokai': dict(bg='#272822', bar='#1E1F1C', surf='#2F302A', high='#3E3D32', fg='#F8F8F2', dim='#75715E',
   outline='#49483E', primary='#F92672', onPrimary='#F8F8F2', secondary='#66D9EF', tertiary='#AE81FF',
   red='#F92672', orange='#FD971F', green='#A6E22E', blue='#66D9EF', yellow='#E6DB74', select='#49483E',
   fab='#F92672', link='#66D9EF'),
 'MonokaiPro': dict(bg='#2D2A2E', bar='#221F22', surf='#363337', high='#403E41', fg='#FCFCFA', dim='#939293',
   outline='#5B595C', primary='#FFD866', onPrimary='#2D2A2E', secondary='#78DCE8', tertiary='#AB9DF2',
   red='#FF6188', orange='#FC9867', green='#A9DC76', blue='#78DCE8', yellow='#FFD866', select='#5B595C',
   fab='#FF6188', link='#78DCE8'),
}
SRC = {
 'Dracula': 'Dracula, official palette from https://draculatheme.com/spec',
 'T3Chat': 'T3 Chat dark theme (pink on aubergine); tokens per the community shadcn port',
 'Monokai': 'Monokai classic (Wimer Hazenberg)',
 'MonokaiPro': 'Monokai Pro "Pro" filter',
}

out = ['<?xml version="1.0" encoding="utf-8"?>',
 '<!-- SPDX-License-Identifier: GPL-3.0-or-later -->',
 '<!-- Editor-inspired night themes. Generated from palettes; keep the four themes in sync. -->',
 '<resources xmlns:tools="http://schemas.android.com/tools" tools:ignore="DuplicateCrowdInStrings">']
colors=[]
for n,p in P.items():
    bg=p['bg']
    cont=p.get('container', mix(p['primary'],bg,0.35))
    oncont=p.get('onContainer', mix(p['primary'],'#FFFFFF',0.35))
    sec=p.get('secContainer', mix(p['secondary'],bg,0.25))
    items = [
     ('colorPrimary',p['primary']),('colorOnPrimary',p['onPrimary']),
     ('colorPrimaryContainer',cont),('colorOnPrimaryContainer',oncont),
     ('colorSecondary',p['secondary']),('colorOnSecondary',bg),
     ('colorSecondaryContainer',sec),('colorOnSecondaryContainer',p['fg']),
     ('colorTertiary',p['tertiary']),('colorOnTertiary',bg),
     ('colorTertiaryContainer',mix(p['tertiary'],bg,0.3)),('colorOnTertiaryContainer',p['fg']),
     ('colorSurface',bg),('colorOnSurface',p['fg']),('colorOnBackground',p['fg']),
     ('colorSurfaceVariant',p['high']),('colorOnSurfaceVariant',p['dim']),
     ('colorOutline',p['dim']),('colorOutlineVariant',p['outline']),
     ('colorErrorContainer',mix(p['red'],bg,0.25)),
     ('colorSurfaceDim',mix('#000000',bg,0.2)),('colorSurfaceBright',p['high']),
     ('colorSurfaceContainerLowest',bg),('colorSurfaceContainerLow',p['surf']),
     ('colorSurfaceContainer',p['surf']),('colorSurfaceContainerHigh',p['high']),
     ('colorSurfaceContainerHighest',p['high']),
     ('colorSurfaceInverse',p['fg']),('colorOnSurfaceInverse',bg),('colorPrimaryInverse',mix(p['primary'],'#000000',0.7)),
     ('android:colorBackground',bg),('android:windowBackground',bg),
     ('android:textColor',p['fg']),('android:textColorPrimary',p['fg']),
     ('android:textColorSecondary',p['dim']),('android:textColorTertiary',p['dim']),
     ('android:textColorHint',p['dim']),('android:textColorLink',p['link']),
     ('android:textColorHighlight',p['select']),
     ('preferenceCategoryTitleTextColor',p['primary']),
     ('appBarColor',p['bar']),('actionBarTextColor',p['fg']),('topBarColor',p['bar']),
     ('android:navigationBarColor',bg),
     ('bottomNavActiveIconColor',p['primary']),
     ('selectedRowBackgroundColor',p['high']),('dynDeckColor',p['secondary']),
     ('newCountColor',p['blue']),('learnCountColor',p['red']),('reviewCountColor',p['green']),
     ('zeroCountColor',p['outline']),
     ('showAnswerButtonBackground',mix(p['primary'],bg,0.6)),('showAnswerColor',p['high']),
     ('showAnswerTextColor',p['fg']),
     ('againButtonBackground',mix(p['red'],bg,0.45)),('hardButtonBackground',mix(p['dim'],bg,0.5)),
     ('goodButtonBackground',mix(p['green'],bg,0.45)),('easyButtonBackground',mix(p['blue'],bg,0.45)),
     ('againButtonTextColor',p['fg']),('hardButtonTextColor',p['fg']),
     ('goodButtonTextColor',p['fg']),('easyButtonTextColor',p['fg']),
     ('againTextColor',p['red']),('hardTextColor',p['orange']),('goodTextColor',p['green']),('easyTextColor',p['blue']),
     ('againBackgroundColor',mix(p['red'],bg,0.15)),('hardBackgroundColor',mix(p['orange'],bg,0.15)),
     ('goodBackgroundColor',mix(p['green'],bg,0.15)),('easyBackgroundColor',mix(p['blue'],bg,0.15)),
     ('maxTimerColor',p['red']),('clozeColor',p['secondary']),
     ('suspendedColor',mix(p['yellow'],bg,0.3)),('buriedColor',mix(p['orange'],bg,0.3)),
     ('markedColor',mix(p['tertiary'],bg,0.35)),('duplicateColor',mix(p['red'],bg,0.35)),
     ('cardBrowserDivider',p['outline']),
     ('fabNormalColor',p['fab']),('fabPressedColor',mix(p['fab'],bg,0.75)),
     ('popupBackgroundColor',p['high']),('dialogBackground',p['surf']),
     ('incrementerButtonBackground',p['high']),('introductionLogoTransparent','#88'+bg[1:]),
     ('cardViewStyle',f'@style/{n}CardBackground'),
     ('alertDialogTheme',f'@style/ThemeOverlay.AnkiDroid.AlertDialog.{n}'),
     ('bottomSheetDialogTheme',f'@style/ThemeOverlay.App.BottomSheetDialog.{n}'),
    ]
    out.append(f'\n    <!-- {SRC[n]} -->')
    out.append(f'    <style name="Theme.AnkiDroid.{n}" parent="Theme.AnkiDroid">')
    import re as _re
    pre = 'theme_'+_re.sub(r'(?<!^)([A-Z])', r'_\1', n).lower()+'_'
    def ref(k,v):
        if not v.startswith('#'): return v
        cname = pre+_re.sub(r'(?<!^)([A-Z])', r'_\1', k.replace('android:','')).lower()
        colors.append(f'    <color name="{cname}">{v}</color>')
        return '@color/'+cname
    out += [f'        <item name="{k}">{ref(k,v)}</item>' for k,v in items]
    out.append('    </style>')
    out.append(f'    <style name="{n}CardBackground" parent="CardView">\n        <item name="cardBackgroundColor">{p["surf"]}</item>\n    </style>')
    out.append(f'    <style name="ThemeOverlay.AnkiDroid.AlertDialog.{n}" parent="ThemeOverlay.AnkiDroid.AlertDialog">\n        <item name="android:colorBackground">{p["surf"]}</item>\n    </style>')
    out.append(f'    <style name="ThemeOverlay.App.BottomSheetDialog.{n}" parent="ThemeOverlay.App.BottomSheetDialog">\n        <item name="android:colorBackground">{p["surf"]}</item>\n        <item name="elevationOverlayEnabled">false</item>\n    </style>')
out.append('\n    <!-- Palette colors referenced by the themes above -->')
out += colors
out.append('</resources>\n')
open(XML,'w').write('\n'.join(out))

css=['','/* Editor-inspired night themes (theme_editor_dark.xml) */']
for n,p in P.items():
    c='ankidroid_'+{'Dracula':'dracula','T3Chat':'t3_chat','Monokai':'monokai','MonokaiPro':'monokai_pro'}[n]+'_mode'
    css.append(f'body.{c} {{\n  color: {p["fg"]};\n  background-color: {p["bg"]};\n}}\n\n.{c} input#typeans {{\n  color: {p["fg"]};\n  background-color: {p["surf"]};\n}}\n\n.{c} a {{\n  color: {p["link"]};\n}}\n')
MARK = '\n/* Editor-inspired night themes'
base = open(CSS).read()
if MARK in base:
    base = base[:base.index(MARK)]
open(CSS,'w').write(base + '\n'.join(css))
