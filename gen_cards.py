import os

OUT = "/home/claude/aashma-yadav/assets"
os.makedirs(OUT, exist_ok=True)

W, H = 420, 220

TEMPLATE = """<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg-{id}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A0E27"/>
      <stop offset="100%" stop-color="#120B2E"/>
    </linearGradient>
    <linearGradient id="acc-{id}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{c1}"/>
      <stop offset="100%" stop-color="{c2}"/>
    </linearGradient>
    <filter id="blur-{id}" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="18"/>
    </filter>
    <filter id="glow-{id}" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="2.4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="clip-{id}"><rect x="0" y="0" width="{w}" height="{h}" rx="18"/></clipPath>
  </defs>

  <g clip-path="url(#clip-{id})">
    <rect width="{w}" height="{h}" fill="url(#bg-{id})"/>
    <circle cx="{w}" cy="0" r="120" fill="{c1}" opacity="0.25" filter="url(#blur-{id})"/>
    <circle cx="0" cy="{h}" r="110" fill="{c2}" opacity="0.22" filter="url(#blur-{id})"/>

    <!-- glass panel -->
    <rect x="14" y="14" width="{wg}" height="{hg}" rx="14"
          fill="#ffffff" opacity="0.05" stroke="#ffffff" stroke-opacity="0.14" stroke-width="1"/>

    <rect x="14" y="14" width="4" height="{hg}" fill="url(#acc-{id})"/>

    <text x="34" y="46" font-family="'Courier New', monospace" font-size="12" letter-spacing="3" fill="{c1}" filter="url(#glow-{id})">{eyebrow}</text>
    <text x="34" y="76" font-family="'Courier New', monospace" font-weight="700" font-size="23" fill="#EAF2FF">{title}</text>
    <text x="34" y="98" font-family="'Courier New', monospace" font-size="12.5" fill="#93A6CC">{subtitle}</text>

    {bullets}

    <text x="34" y="{stack_y}" font-family="'Courier New', monospace" font-size="11.5" fill="{c2}">{stack}</text>
  </g>
  <rect x="1" y="1" width="{w2}" height="{h2}" rx="18" fill="none" stroke="url(#acc-{id})" stroke-width="1.5" opacity="0.65"/>
</svg>
"""

def bullet_lines(bullets, x=34, y0=118, dy=20):
    out = []
    for i, b in enumerate(bullets):
        y = y0 + i * dy
        out.append(
            f'<circle cx="{x}" cy="{y-4}" r="2.6" fill="#00F6FF"/>'
            f'<text x="{x+12}" y="{y}" font-family="\'Courier New\', monospace" font-size="12.5" fill="#C7D4F0">{b}</text>'
        )
    return "\n    ".join(out)

CARDS = [
    dict(id="minios", eyebrow="SYSTEMS · BARE-METAL", title="MiniOS", subtitle="ARM64 ML Inference Unikernel",
         c1="#00F6FF", c2="#7B2FFF",
         bullets=["7-policy scheduler · MLQ @ 269&#181;s pipeline", "&lt;8&#181;s context-switch (pure ARM64 asm)", "Custom RUDP stack + 23-op ONNX runtime"],
         stack="C / C++ · QEMU Cortex-A53 · ARM64 NEON"),
    dict(id="asl", eyebrow="PATTERN RECOGNITION · ML", title="Real-Time ASL Translator", subtitle="Sign language to speech, live",
         c1="#FF00E5", c2="#7B2FFF",
         bullets=["98% val. accuracy, 26 ASL letters", "&lt;2ms inference @ 30+ FPS", "Flask/SSE stream + majority-vote smoothing"],
         stack="scikit-learn · MediaPipe · Flask"),
    dict(id="dsa-viz", eyebrow="FULL-STACK · ALGORITHMS", title="Pattern Search Visualiser", subtitle="4 string-matching algorithms, head to head",
         c1="#00F6FF", c2="#FFE066",
         bullets=["KMP · Automaton · Suffix Trie · Ukkonen", "Benchmarked on 325K-char corpus live", "React dashboard: time &amp; complexity tradeoffs"],
         stack="C++ · Node.js · React"),
    dict(id="jarvis", eyebrow="LLM · VOICE ASSISTANT", title="JARVIS", subtitle="Fully local AI voice assistant",
         c1="#7B2FFF", c2="#00F6FF",
         bullets=["Event-driven, multi-threaded pipeline", "100+ built-in actions, NLP fallback", "Zero-latency UI via producer-consumer I/O"],
         stack="Python · Ollama REST API"),
    dict(id="ecom", eyebrow="DSA · HYBRID SYSTEM", title="Smart E-Commerce System", subtitle="Search, cart &amp; recommendations engine",
         c1="#FFE066", c2="#FF00E5",
         bullets=["Trie autocomplete · O(L) lookup", "Levenshtein fuzzy search fallback", "Graph-based BFS recommendations"],
         stack="C++ · Python · Tkinter"),
    dict(id="matching", eyebrow="RESEARCH-GUIDED · ALLOCATION", title="Stable Matching for BTP", subtitle="Constraint-aware Gale-Shapley extension",
         c1="#00F6FF", c2="#FF00E5",
         bullets=["CGPA-category constraints + capacity limits", "Verified stable, conflict-free across 70&#215;20", "Full-stack GUI for real academic deployment"],
         stack="Python · PostgreSQL"),
    dict(id="washify", eyebrow="PRODUCT · MERN", title="Washify", subtitle="[ add a one-line description here ]",
         c1="#FF00E5", c2="#00F6FF",
         bullets=["[ key feature 1 ]", "[ key feature 2 ]", "[ key feature 3 ]"],
         stack="MongoDB · Express · React · Node.js"),
]

for c in CARDS:
    bl = bullet_lines(c["bullets"])
    svg = TEMPLATE.format(
        w=W, h=H, w2=W-2, h2=H-2, wg=W-28, hg=H-28,
        id=c["id"], c1=c["c1"], c2=c["c2"],
        eyebrow=c["eyebrow"], title=c["title"], subtitle=c["subtitle"],
        bullets=bl, stack=c["stack"], stack_y=118 + len(c["bullets"])*20 + 18
    )
    with open(os.path.join(OUT, f'card-{c["id"]}.svg'), "w") as f:
        f.write(svg)

print("done", os.listdir(OUT))
