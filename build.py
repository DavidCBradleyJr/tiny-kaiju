# Inlines assets/kaiju.glb into src/index.html -> docs/index.html (one self-contained file; GitHub Pages serves docs/)
import base64, pathlib
root = pathlib.Path(__file__).parent
html = (root / "src/index.html").read_text()
glb = base64.b64encode((root / "assets/kaiju.glb").read_bytes()).decode()
js = f'window.KAIJU_B64="{glb}";'
(root / "dist").mkdir(exist_ok=True)
(root / "dist/kaiju.js").write_text(js)
assert html.count('<script src="kaiju.js"></script>') == 1
(root / "docs").mkdir(exist_ok=True)
(root / "docs/index.html").write_text(html.replace('<script src="kaiju.js"></script>', f'<script>{js}</script>'))
print("docs/index.html", (root / "docs/index.html").stat().st_size, "bytes")

# claude.ai Artifact variant: host supplies doctype/html/head/body; GLB published alongside as kaiju.glb
import re
art = re.sub(r'<!doctype html>\s*|</?html[^>]*>\s*|</?head>\s*|</?body>\s*', '', html, flags=re.I)
art = art.replace('<style>\n  :root {', '<style>\n  :root { color-scheme:light;', 1)
(root / "dist/artifact.html").write_text(art)
print("dist/artifact.html", len(art), "bytes")
