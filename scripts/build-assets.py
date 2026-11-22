"""Builds the light and dark hero and footer SVGs from the portfolio's DESIGN.md tokens.

Run:  python3 scripts/build-assets.py
Tokens mirror GowthamPortfolio/DESIGN.md ("the shelf"): flat, no gradients, one chalk-green shape.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"

THEMES = {
    "light": dict(canvas="#F3F4F6", surface="#FFFFFF", ink="#101114", ink2="#5B6170",
                  rule="#E2E4E9", chalk="#1F6B4A", chalkink="#FFFFFF", dust="#F5C542"),
    "dark": dict(canvas="#0E1210", surface="#161B18", ink="#ECEFEA", ink2="#9BA39E",
                 rule="#26302B", chalk="#4CC38A", chalkink="#0E1210", dust="#F5C542"),
}

FONT = "Geist,Inter,ui-sans-serif,system-ui,-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif"
MONO = "'Geist Mono',ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"

FACTS = [("4+", "years shipping"), ("800K+", "students reached"),
         ("9", "apps in the stores"), ("12", "AI agents in Aira")]


def hero(t):
    facts = []
    for i, (v, l) in enumerate(FACTS):
        x = 56 + i * 148
        facts.append(
            f'<text x="{x}" y="284" class="f" font-size="28" font-weight="600" letter-spacing="-0.8" fill="{t["ink"]}">{v}</text>'
            f'<text x="{x}" y="306" class="f" font-size="13" font-weight="500" fill="{t["ink2"]}">{l}</text>'
        )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 340" width="1000" height="340" role="img" aria-label="Gowtham J, senior React Native developer and mobile team lead">
<defs>
  <clipPath id="card"><rect width="1000" height="340" rx="22"/></clipPath>
  <clipPath id="screen"><rect x="842" y="70" width="116" height="212" rx="14"/></clipPath>
  <style>
    .f{{font-family:{FONT}}}
    .m{{font-family:{MONO}}}
    .phone{{animation:float 6s ease-in-out infinite}}
    .dot{{transform-box:fill-box;transform-origin:center;animation:pulse 2.4s ease-in-out infinite}}
    .feed{{animation:feed 9s cubic-bezier(.7,0,.3,1) infinite}}
    @keyframes float{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-6px)}}}}
    @keyframes pulse{{0%,100%{{transform:scale(1);opacity:1}}50%{{transform:scale(.6);opacity:.55}}}}
    @keyframes feed{{0%,28%{{transform:translateY(0)}}33%,61%{{transform:translateY(-70px)}}66%,94%{{transform:translateY(-140px)}}100%{{transform:translateY(0)}}}}
    @media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
  </style>
</defs>
<g clip-path="url(#card)">
  <rect width="1000" height="340" fill="{t["canvas"]}"/>
  <circle cx="900" cy="176" r="232" fill="{t["chalk"]}"/>

  <g class="phone">
    <rect x="834" y="60" width="132" height="232" rx="22" fill="{t["chalk"]}" stroke="{t["chalkink"]}" stroke-width="3"/>
    <g clip-path="url(#screen)">
      <rect x="842" y="70" width="116" height="212" fill="{t["chalkink"]}" fill-opacity=".1"/>
      <g class="feed">
        {"".join(
            f'<rect x="852" y="{86 + k*70}" width="96" height="40" rx="8" fill="{t["chalkink"]}" fill-opacity=".9"/>'
            f'<rect x="852" y="{132 + k*70}" width="{[64,80,52,64][k]}" height="6" rx="3" fill="{t["chalkink"]}" fill-opacity=".55"/>'
            f'<rect x="852" y="{142 + k*70}" width="{[40,30,58,40][k]}" height="6" rx="3" fill="{t["chalkink"]}" fill-opacity=".3"/>'
            for k in range(4))}
      </g>
    </g>
    <circle cx="944" cy="82" r="5" fill="{t["dust"]}" class="dot"/>
  </g>
  <text x="900" y="322" text-anchor="middle" class="m" font-size="12" fill="{t["chalkink"]}" fill-opacity=".8">offline-first · 60 fps</text>

  <g class="in">
    <circle cx="62" cy="62" r="5" fill="{t["dust"]}" class="dot"/>
    <text x="76" y="67" class="f" font-size="14" font-weight="500" fill="{t["ink2"]}">Open to senior React Native and mobile lead roles</text>
  </g>
  <text x="52" y="150" class="f in in2" font-size="80" font-weight="600" letter-spacing="-3.6" fill="{t["ink"]}">Gowtham J</text>
  <text x="56" y="192" class="f in in3" font-size="22" font-weight="600" letter-spacing="-0.4" fill="{t["ink"]}">Senior React Native developer · mobile team lead</text>
  <text x="56" y="220" class="f in in3" font-size="16" fill="{t["ink2"]}">Offline-first learning apps, native modules in Swift and Kotlin, AI agents.</text>
  <line x1="56" y1="246" x2="628" y2="246" stroke="{t["rule"]}" stroke-width="1"/>
  <g class="in in4">{"".join(facts)}</g>
</g>
<rect x=".5" y=".5" width="999" height="339" rx="21.5" fill="none" stroke="{t["rule"]}"/>
</svg>
'''


def footer(t):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 150" width="1000" height="150" role="img" aria-label="Building mobile apps that scale. Get in touch.">
<defs><clipPath id="c"><rect width="1000" height="150" rx="22"/></clipPath>
<style>.f{{font-family:{FONT}}} .dot{{transform-box:fill-box;transform-origin:center;animation:p 2.4s ease-in-out infinite}} @keyframes p{{0%,100%{{transform:scale(1)}}50%{{transform:scale(.6);opacity:.55}}}} @media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}</style></defs>
<g clip-path="url(#c)">
  <rect width="1000" height="150" fill="{t["chalk"]}"/>
  <text x="56" y="76" class="f" font-size="40" font-weight="600" letter-spacing="-1.6" fill="{t["chalkink"]}">Building mobile apps that scale.</text>
  <circle cx="62" cy="110" r="5" fill="{t["dust"]}" class="dot"/>
  <text x="76" y="115" class="f" font-size="15" font-weight="500" fill="{t["chalkink"]}" fill-opacity=".85">Based in India, open to relocation. Replies within a day.</text>
  <rect x="790" y="51" width="154" height="48" rx="24" fill="{t["chalkink"]}"/>
  <text x="867" y="81" text-anchor="middle" class="f" font-size="16" font-weight="600" fill="{t["chalk"]}">Get in touch →</text>
</g>
</svg>
'''


for name, t in THEMES.items():
    (OUT / f"hero-{name}.svg").write_text(hero(t))
    (OUT / f"footer-{name}.svg").write_text(footer(t))
print("wrote", sorted(p.name for p in OUT.glob("*.svg")))
