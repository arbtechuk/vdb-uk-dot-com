# Dark/Light Mode Toggle

> **Status:** Planned
> **Scope:** `index.html` (single-file static site, ~1818 lines)
> **Approach:** CSS custom property theming via `data-theme` attribute on `<html>`

---

## Current State

The site uses a **dark-first** "Welsh Slate" palette. All colours already use CSS custom properties in `:root`, which is ideal for theming. Sections alternate between dark and light backgrounds:

| Section | Current Background | Character |
|---------|--------------------|-----------|
| Header | `slate-950` | Dark, fixed |
| Hero | `slate-950` + geometric pattern | Dark, immersive |
| Partners | `slate-900` | Dark strip |
| Capabilities | `stone-50` + white cards | Light |
| Approach (V-D-B) | `slate-900` | Dark panels |
| Projects | `stone-100` + white cards | Light |
| Featured | `white` | Light |
| CTA Banner | `red-700` | Brand accent |
| Footer | `slate-950` | Dark |

The site already has `data-lang` on `<html>` for EN/CY bilingual toggling. Theme toggling follows the same pattern.

---

## Architecture

### Semantic Variable Layer

Introduce **semantic tokens** between the raw palette (`--slate-950`, `--red-600`) and component styles. Components reference semantic tokens; themes swap the underlying mapping.

```css
/* Dark theme (default — current site) */
:root,
[data-theme="dark"] {
  /* Surfaces */
  --surface-hero: var(--slate-950);
  --surface-dark: var(--slate-900);
  --surface-light: var(--stone-50);
  --surface-card: #ffffff;
  --surface-card-border: var(--slate-200);

  /* Text */
  --text-on-dark: #ffffff;
  --text-on-dark-muted: var(--slate-300);
  --text-on-light: var(--slate-800);
  --text-on-light-muted: var(--slate-600);

  /* Header */
  --header-bg: var(--slate-950);
  --header-border: rgba(255,255,255,0.06);
  --header-link: var(--slate-300);
  --header-link-hover: #ffffff;
  --header-logo-stroke: #ffffff;
  --header-logo-accent: #8b91a8;

  /* Hero pattern */
  --hero-pattern-opacity: 0.06;

  /* Footer */
  --footer-bg: var(--slate-950);
  --footer-text: var(--slate-400);
  --footer-link-hover: #ffffff;
}

/* Light theme */
[data-theme="light"] {
  /* Surfaces */
  --surface-hero: var(--stone-50);
  --surface-dark: var(--stone-100);
  --surface-light: #ffffff;
  --surface-card: #ffffff;
  --surface-card-border: var(--slate-200);

  /* Text */
  --text-on-dark: var(--slate-900);
  --text-on-dark-muted: var(--slate-600);
  --text-on-light: var(--slate-800);
  --text-on-light-muted: var(--slate-600);

  /* Header */
  --header-bg: #ffffff;
  --header-border: var(--slate-200);
  --header-link: var(--slate-600);
  --header-link-hover: var(--slate-900);
  --header-logo-stroke: var(--slate-900);
  --header-logo-accent: var(--slate-600);

  /* Hero pattern */
  --hero-pattern-opacity: 0.04;

  /* Footer */
  --footer-bg: var(--stone-100);
  --footer-text: var(--slate-600);
  --footer-link-hover: var(--slate-900);
}
```

### Section-by-Section Light Mode Behaviour

| Section | Light Mode Treatment |
|---------|---------------------|
| **Header** | White bg, dark text links, subtle bottom border (`slate-200`) |
| **Hero** | Cream (`stone-50`) bg, dark text, geometric pattern in muted warm tones, stat cards with light borders |
| **Partners** | `stone-100` bg, darker logo text |
| **Capabilities** | White bg, cream cards — minimal change from current |
| **Approach (V-D-B)** | Cream panels, dark text, coloured V/D/B accents preserved |
| **Projects** | White bg, faint card borders — minimal change |
| **Featured** | Stays white — unchanged |
| **CTA Banner** | **Stays `red-700`** — brand identity constant in both themes |
| **Footer** | `stone-100` bg, dark text |

The CTA banner is theme-invariant. Welsh red is the brand anchor.

---

## Toggle UI

Add a theme toggle button next to the existing language toggle in the header:

```
[EN | CY]  [sun | moon]  [Contact Us]
```

Same pill-button style as `lang-toggle`. Sun icon = light mode active, moon icon = dark mode active. Active state uses `--red-600` background, matching the language toggle.

```html
<div class="theme-toggle" role="group" aria-label="Theme">
  <button class="theme-toggle__btn" data-set-theme="light" aria-label="Light mode">
    <svg><!-- sun icon --></svg>
  </button>
  <button class="theme-toggle__btn theme-toggle__btn--active" data-set-theme="dark" aria-label="Dark mode">
    <svg><!-- moon icon --></svg>
  </button>
</div>
```

### CSS for Toggle

```css
.theme-toggle {
  display: flex;
  align-items: center;
  gap: 2px;
  background: var(--slate-800);
  border-radius: 6px;
  padding: 2px;
}

/* Light theme: toggle pill background adapts */
[data-theme="light"] .theme-toggle {
  background: var(--slate-100);
}

.theme-toggle__btn {
  padding: 6px 10px;
  border-radius: 4px;
  color: var(--slate-400);
  transition: all 0.2s;
  display: flex;
  align-items: center;
}

.theme-toggle__btn--active {
  background: var(--red-600);
  color: white;
}
```

---

## JavaScript

Mirrors the existing `setLang()` pattern exactly:

```js
// ─── Theme Toggle ───
const savedTheme = localStorage.getItem('vdb-theme');
const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
const initialTheme = savedTheme || (prefersDark ? 'dark' : 'light');

const themeBtns = document.querySelectorAll('[data-set-theme]');

function setTheme(theme) {
  html.setAttribute('data-theme', theme);
  localStorage.setItem('vdb-theme', theme);
  themeBtns.forEach(btn => {
    btn.classList.toggle('theme-toggle__btn--active', btn.dataset.setTheme === theme);
  });
}

setTheme(initialTheme);

themeBtns.forEach(btn => {
  btn.addEventListener('click', () => setTheme(btn.dataset.setTheme));
});

// Listen for OS-level theme changes
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
  if (!localStorage.getItem('vdb-theme')) {
    setTheme(e.matches ? 'dark' : 'light');
  }
});
```

- Respects `prefers-color-scheme` on first visit (no saved preference)
- Persists choice in `localStorage` (same key pattern as `vdb-lang`)
- OS-level changes respected until user manually overrides

---

## SVG Logo Fix

Both header and footer logos use hardcoded stroke colours (`white`, `#8b91a8`). These need to reference CSS variables or `currentColor`.

**Header logo** (line ~1163):
- V chevron: stays `#c8283f` (brand red — theme-invariant)
- D and B strokes: `white` → `var(--header-logo-stroke)` (white in dark, `slate-900` in light)
- UK text: `#8b91a8` → `var(--header-logo-accent)`
- Divider line: `#363a4d` → adapts in light mode

Since inline SVG can't use CSS custom properties in `stroke` attributes directly, use CSS to target the paths:

```css
.header__logo svg path:not(:first-child) { stroke: var(--header-logo-stroke); }
.header__logo svg text { fill: var(--header-logo-accent); }
.header__logo svg line { stroke: var(--header-border); }
```

Same approach for footer logo, with `--footer-text` for strokes.

---

## Smooth Transition

Add a transition to body and key elements for a smooth theme swap:

```css
body,
.header,
.hero,
.partners,
.capabilities,
.approach,
.projects,
.featured,
.footer {
  transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
}

.cap-card,
.project-card,
.stat-card,
.pillar {
  transition: background-color 0.3s ease, border-color 0.3s ease, color 0.3s ease,
              transform 0.3s ease, box-shadow 0.3s ease;
}
```

---

## Accessibility

- Toggle button: `aria-label="Switch to light mode"` / `"Switch to dark mode"`
- Gold accent (`#d4a017`) on white backgrounds: darken to `#9a7b0a` in light mode for WCAG AA (4.5:1 contrast)
- Red accent (`#a82135`): already passes AA on white — no change needed
- `slate-600` text on `stone-50` background: passes AA — fine
- Test with browser DevTools contrast checker after implementation

---

## Implementation Checklist

1. **Add semantic CSS variables** to `:root` and `[data-theme="light"]` block
2. **Refactor component styles** — replace hardcoded palette refs with semantic tokens in:
   - `.header`, `.hero`, `.partners` (dark sections)
   - `.approach`, `.footer` (dark sections)
   - `.capabilities`, `.projects`, `.featured` (light sections — minimal changes)
   - `.stat-card`, `.cap-card`, `.project-card`, `.pillar` (cards)
3. **Add theme toggle HTML** to header nav, between lang-toggle and CTA
4. **Add theme toggle CSS** — pill button + light-mode overrides
5. **Add theme toggle JS** — detection, persistence, toggle handler, OS change listener
6. **Fix SVG logos** — CSS-driven stroke colours for both header and footer
7. **Add transitions** — smooth 0.3s on background/color/border properties
8. **Contrast audit** — verify gold/red accents meet AA on light backgrounds
9. **Test** — both themes at all breakpoints (480, 768, 1024, desktop)

### Estimated Scope

- ~150-200 lines of CSS changes (semantic layer + light overrides)
- ~20 lines of HTML (toggle button with SVG icons)
- ~25 lines of JS (detection, persistence, toggle, OS listener)
- No structural HTML changes — purely additive
