# Tiny Kaiju

A 75-second three.js browser game. You play a baby kaiju in a pastel toy city: smash anything shorter than you, grow with every building, and level the skyline.

**Controls:** WASD / arrow keys to move, Space to stomp, M to mute. On a phone, drag to move and tap STOMP.

## Layout

- `src/index.html` — the game (three.js from jsDelivr, all sound synthesized with Web Audio)
- `assets/kaiju.glb` — hero model (concept image from Higgsfield GPT Image 2.6, mesh from Tripo H3.1)
- `build.py` — inlines the model into `docs/index.html`, a single self-contained file
- `docs/` — the built game; GitHub Pages serves this folder

## Build

```bash
python3 build.py
```

Then open `docs/index.html` through any static server (e.g. `python3 -m http.server -d docs`).

## Hosting

GitHub Pages: Settings → Pages → Deploy from branch → `main` / `docs`.
`docs/index.html` also works as-is on Netlify Drop, itch.io or Cloudflare Pages.
