# Welsh Toggle Kill Switch

> **Goal:** Hide the EN/CY language toggle on all pages. Allow re-enabling via a secret key combo for our Welsh speaker to review translations.

---

## Current State

- 23 HTML pages each have an inline `.lang-toggle` div with EN/CY buttons
- Language JS (`setLang`, browser detect, localStorage) is duplicated inline in each page
- Welsh translations are machine-generated and need human review before going public

## Plan

### 1. Create `/lang-config.js` (~20 lines)

Single shared config file loaded by all pages:

```js
(function () {
  var WELSH_ENABLED = false;

  // Secret unlock: ?cymraeg in URL sets persistent flag
  if (location.search.includes('cymraeg')) {
    localStorage.setItem('vdb-welsh-unlock', '1');
  }
  if (location.search.includes('nocymraeg')) {
    localStorage.removeItem('vdb-welsh-unlock');
    localStorage.removeItem('vdb-lang');
  }
  if (localStorage.getItem('vdb-welsh-unlock') === '1') {
    WELSH_ENABLED = true;
  }

  window.VDB_WELSH_ENABLED = WELSH_ENABLED;
})();
```

### 2. Add `<script src="/lang-config.js"></script>` to each page

Before the existing inline `<script>` block.

### 3. Modify each page's inline JS

Wrap the toggle setup so it respects the kill switch:

```js
if (!window.VDB_WELSH_ENABLED) {
  document.querySelectorAll('.lang-toggle').forEach(el => el.style.display = 'none');
  setLang('en');
} else {
  setLang(initialLang);
  langBtns.forEach(btn => {
    btn.addEventListener('click', () => setLang(btn.dataset.setLang));
  });
}
```

## How It Works

| Scenario | Result |
|---|---|
| Normal visitor | Toggle hidden, English only |
| Shift+W on any page | Toggles between EN and CY (even when toggle is hidden) |
| Visit `?cymraeg` | localStorage flag set, toggle button appears on all pages |
| Visit `?nocymraeg` | Flag cleared, back to hidden |
| Ready to go public | Set `WELSH_ENABLED = true` in one file |

## Scope

- 1 new file (`lang-config.js`)
- 23 pages: add one `<script>` tag + ~5-line JS tweak each
- No markup changes, no CSS changes, no string extraction
