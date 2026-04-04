# VDB Website — Plan

> **Domain:** `vdb-uk.com`
> **Purpose:** Convince funding bodies, grant reviewers, and government clients that VDB can deliver complex projects
> **Languages:** English (en) + Welsh (cy), auto-detected via browser `Accept-Language`, with manual toggle

---

## Strategy

The site exists to close deals. When Hannah applies for government funding, secretariat roles, or R&D projects, reviewers will click through to this site. They need to land, immediately understand VDB's credibility, and then find content that speaks directly to *their* type of project. The site must feel like a serious, established consultancy — not a startup.

**Key audience journeys:**
1. Grant reviewer checks VDB's track record — lands on homepage, sees headline stats, clicks into a relevant capability area
2. Government body evaluating secretariat bids — finds the "Government & Programme Management" page, sees relevant case studies and methodology
3. R&D partner assessing collaboration fit — explores innovation/science pages, sees validated outcomes and institutional partners

---

## Information Architecture

```
/ (Homepage)
├── /capabilities
│   ├── /capabilities/secretariat-programme-management
│   ├── /capabilities/research-innovation
│   ├── /capabilities/funding-grants
│   ├── /capabilities/science-engineering
│   └── /capabilities/esg-sustainability
├── /projects
│   ├── /projects/npk-recovery
│   ├── /projects/gripable
│   ├── /projects/plus-x-innovation
│   ├── /projects/blakbear
│   └── /projects/[slug]  (template — easy to add more)
├── /about
├── /contact
└── /[lang]/...  (all routes prefixed with locale)
```

### Adding new pages

Each capability and project page follows a template. To add a new capability area or project case study, duplicate the template and fill in the content. The homepage grid automatically picks up new entries.

---

## Page Designs

### Homepage `/`

**Goal:** Credibility in 5 seconds. Specificity in 30.

```
┌─────────────────────────────────────────────────────┐
│  VDB logo          [EN | CY]            Contact Us  │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Headline stat: "£255m unlocked for UK R&D"         │
│  Subline: "We validate, develop, and build          │
│            innovation that matters."                │
│                                                     │
│  [Talk to us →]                                     │
│                                                     │
├─────────────────────────────────────────────────────┤
│  WHAT WE DO — capability cards (grid, 2-3 cols)     │
│                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐          │
│  │Programme │  │Research  │  │Funding & │          │
│  │Management│  │& Innov.  │  │Grants    │          │
│  │& Secret. │  │          │  │          │          │
│  │ → more   │  │ → more   │  │ → more   │          │
│  └──────────┘  └──────────┘  └──────────┘          │
│  ┌──────────┐  ┌──────────┐                         │
│  │Science & │  │ESG &     │                         │
│  │Engineerng│  │Sustain.  │                         │
│  │ → more   │  │ → more   │                         │
│  └──────────┘  └──────────┘                         │
│                                                     │
├─────────────────────────────────────────────────────┤
│  TRACK RECORD — key numbers strip                   │
│                                                     │
│  £255m unlocked  │  8 major projects  │  Since 2020 │
│  NHS, Defra,     │  Imperial, Cambridge│  Bristol HQ │
│  Innovate UK     │  Cranswick, ...     │             │
│                                                     │
├─────────────────────────────────────────────────────┤
│  SELECTED PROJECTS — horizontal scroll / grid       │
│                                                     │
│  [NPK Recovery]  [GripAble]  [Plus X]  [BlakBear]  │
│  Each card: image, one-line, client, → case study   │
│                                                     │
├─────────────────────────────────────────────────────┤
│  WHO WE WORK WITH — logo strip                      │
│  Defra, Innovate UK, Imperial, Cambridge, NHS,      │
│  Cranswick, Co-op, Forestry Commission              │
│                                                     │
├─────────────────────────────────────────────────────┤
│  CTA: "Let's build something together"              │
│  [Contact us →]                                     │
│                                                     │
├─────────────────────────────────────────────────────┤
│  Footer: © VDB  │  Bristol, UK  │  Links  │  Lang  │
└─────────────────────────────────────────────────────┘
```

### Capability Page Template `/capabilities/[slug]`

Each capability page follows this structure:

1. **Hero** — capability name, one-sentence positioning, relevant icon/image
2. **The challenge** — what problem this capability solves (speaks to the funder's world)
3. **Our approach** — methodology, how VDB delivers (3–4 steps with descriptions)
4. **Case studies** — 2–3 project cards from this capability area, linking to full case studies
5. **Key outcomes** — stats, awards, validated results
6. **CTA** — "Discuss a [capability] project with us"

#### Capability: Secretariat & Programme Management

This is the first priority page, tailored for the Welsh Education Board bid and similar government process work.

**Content outline:**

- **Hero:** "Secretariat & Programme Management — We run the process so you can focus on the mission."
- **The challenge:** Government bodies need structured programme delivery: stakeholder coordination, meeting management, minute-taking, report production, compliance, and continuity across multi-year funded periods. They need a partner who understands governance, not just administration.
- **Our approach:**
  1. **Stakeholder mapping & onboarding** — identify all parties, establish communication protocols, set cadence
  2. **Governance framework** — design meeting structures, reporting templates, decision-tracking processes
  3. **Delivery & documentation** — manage meetings, produce minutes, track actions, compile reports to deadlines
  4. **Continuity & handover** — knowledge management, succession planning, institutional memory
- **Case studies:** Welsh Education Board (when live), plus any other relevant programme management work
- **Key outcomes:** Multi-year funded roles, government trust, repeat engagements
- **Bilingual note:** This page is especially important in Welsh — the Welsh Education Board audience will expect fluent Welsh content

#### Other capabilities (to build out over time)

- **Research & Innovation** — validate ideas, human-centred design, user workshops, literature reviews
- **Funding & Grants** — unlocking government and institutional funding, bid writing, consortium building
- **Science & Engineering** — lab work, demonstrator builds, field trials (NPK Recovery, Defra)
- **ESG & Sustainability** — climate research, ESG risk frameworks, circular economy

### Project Case Study Template `/projects/[slug]`

1. **Hero** — project name, client/partner, one-line description
2. **The brief** — what was the challenge or opportunity
3. **What we did** — VDB's specific role and methodology
4. **Results** — measurable outcomes, funding unlocked, awards, validated findings
5. **Client quote** (if available)
6. **Related capabilities** — links back to relevant capability pages

### About `/about`

- Who VDB is — founded by Hannah Van Den Bergh, based at Future Space Bristol
- The team — key people and their expertise
- Values / approach — human-centred design, evidence-based, collaborative
- Partners and institutional affiliations

### Contact `/contact`

- Email: hannah@vandenberghuk.com
- Contact form
- Location: Bristol, UK
- Language preference selector

---

## Internationalisation (i18n)

### Requirements

- **Languages:** English (`en`) and Welsh (`cy`) from launch
- **Detection:** Auto-detect via browser `Accept-Language` header on first visit
- **Manual toggle:** Persistent language switcher in header (EN | CY)
- **URLs:** Locale-prefixed routes — `/en/capabilities/...`, `/cy/capabilities/...`
- **Default:** English, with redirect to detected locale
- **Cookie/localStorage:** Remember user's choice across sessions
- **All content bilingual:** Every heading, paragraph, button, alt text, meta description

### Implementation approach

- Static site generator with i18n plugin, or Next.js with `next-intl` / `next-i18next`
- Content stored as JSON/YAML translation files per locale:
  ```
  /content
  ├── en/
  │   ├── home.json
  │   ├── capabilities/secretariat.json
  │   └── projects/npk-recovery.json
  └── cy/
      ├── home.json
      ├── capabilities/secretariat.json
      └── projects/npk-recovery.json
  ```
- Welsh translations: Hannah to provide or commission professional Welsh translation (government-facing Welsh content must be accurate, not machine-translated)
- `<html lang="cy">` / `<html lang="en">` set correctly for accessibility and SEO
- `hreflang` tags in `<head>` for search engines

---

## Tech Stack (Recommended)

| Layer | Choice | Why |
|-------|--------|-----|
| Framework | **Astro** or **Next.js** (static export) | Fast, SEO-friendly, easy i18n, component-based |
| Styling | **Tailwind CSS** | Professional, consistent, responsive |
| Hosting | **GitHub Pages** or **Cloudflare Pages** | Free, fast, custom domain (`vdb-uk.com`) |
| CMS (optional) | Markdown/YAML files in git | Hannah or AI can update content without code changes |
| i18n | `astro-i18n` or `next-intl` | Locale routing, translation file management |

### Why static

- No server to maintain
- Instant page loads (important for credibility)
- Free hosting
- Content updates via git push
- Easy for AI agents to update

---

## Design Principles

1. **Professional, not flashy** — clean typography, generous whitespace, muted colour palette with VDB purple/orange accents (from current branding)
2. **Credibility-first** — lead with numbers, names, and institutional partners — not adjectives
3. **Scannable** — busy grant reviewers will skim. Every section needs a clear heading and the key fact visible without reading paragraphs
4. **Mobile-first** — government people read on phones and tablets
5. **Accessible** — WCAG 2.1 AA minimum (especially important for Welsh Government work)
6. **Extensible** — adding a new capability or project page should take < 30 minutes

### Colour palette (updated for prototype — "Welsh Slate")

- Slate 950 (hero/header): `#0f1118`
- Welsh red (primary accent, CTAs): `#a82135` / `#c8283f`
- Warm gold (stat highlights, secondary accent): `#d4a017` / `#e8b82f`
- Stone cream (light section backgrounds): `#f8f6f1`
- Slate grey (body text): `#252838`

### Typography

- Display/headings: **Crimson Pro** (serif — editorial authority, pairs well with institutional tone)
- Body/UI: **Outfit** (geometric sans — modern, clean, highly legible)

---

## Prototype

Working prototype at `docs/prototypes/vdb-homepage.html` — open in browser to see:
- Full homepage layout with all sections
- EN/CY language toggle (auto-detects browser language)
- SVG logo (geometric VDB monogram with red V chevron)
- Responsive layout
- Scroll animations

---

## Nano Banana Image Prompts

Use these with Gemini image generation for the placeholder image slots in the prototype.

### Hero / General Brand

Not needed — hero uses stat cards on dark background instead of a photo.

### Project Cards

**NPK Recovery:**
> A close-up photograph of green crop seedlings growing in rich dark soil, with morning dew on the leaves, shot from a low angle. Natural daylight, shallow depth of field. Professional editorial photography style, warm tones. No people.

**GripAble:**
> A modern medical rehabilitation device being held in a human hand, clinical white background with soft blue lighting. The device is sleek, small, and has a digital display. Professional product photography, clean and minimal. Healthcare technology aesthetic.

**Plus X Innovation:**
> Interior of a modern innovation hub and coworking space. Open plan with natural light streaming through large windows, people collaborating at workbenches with 3D printers and prototyping equipment visible in the background. Shot from mid-distance, editorial style. Warm industrial aesthetic with exposed brick and steel beams.

**BlakBear:**
> Close-up of fresh meat packaging on a supermarket shelf with a small digital sensor label visible on the packaging. Clean, well-lit commercial photography. Modern food retail environment. Sharp focus on the packaging with blurred background.

### Featured Section (Secretariat)

**Professional meeting / boardroom:**
> A professional government committee meeting in session in a modern Welsh civic building. Diverse group of 6-8 people seated around a large oval table with documents and laptops. Natural light from floor-to-ceiling windows. One person standing presenting to the group. Formal but modern atmosphere. Shot from behind one shoulder looking across the table. Muted tones — grey, navy, cream. Professional editorial photography.

### About Page

**Team / Bristol location:**
> Exterior of a modern university enterprise hub building in Bristol, UK. Glass and steel architecture, early morning light. A few professionals walking towards the entrance. Green landscaping in foreground. Clean architectural photography style.

### Capability Pages

**Research & Innovation:**
> Overhead flat-lay of a design thinking workshop table: post-it notes in organised clusters, markers, printed user journey maps, a laptop showing data visualisations, coffee cups. Warm natural light from a window on the left. Clean, editorial style. Cream and pastel colour palette.

**Funding & Grants:**
> Abstract data visualisation rendered as a 3D landscape of rising bar charts and flowing curves, rendered in deep slate blue and warm gold tones. Dark background. Geometric and clean, no text. Could work as a hero image for a funding strategy page.

**Science & Engineering:**
> A laboratory bench with scientific glassware — Erlenmeyer flasks, beakers with amber liquid, a digital pipette. Modern lab environment with white surfaces and LED panel lighting. Sharp, clean, professional scientific photography. Shallow depth of field.

**ESG & Sustainability:**
> Aerial drone photograph of a patchwork of green agricultural fields meeting a coastline in Wales. Dramatic cloud formations above. The landscape transitions from cultivated farmland to wild coastal cliffs. Golden hour lighting. Cinematic wide-angle composition.

---

## Content Needed from Hannah

Before build:

- [ ] Welsh translations for all content (professional, not machine — especially for government-facing pages)
- [ ] Secretariat capability page copy — methodology, past experience, what makes VDB different
- [ ] Welsh Education Board project brief (what can be shared publicly)
- [ ] Team bios and photos (or decision on whether to show team)
- [ ] Client logos — permissions to display Defra, Innovate UK, Imperial, etc.
- [ ] Any client quotes or testimonials
- [ ] VDB logo files (SVG preferred)
- [ ] Decision on whether existing project descriptions (NPK Recovery, GripAble, etc.) need updating

---

## Build Phases

### Phase 1 — Core site (launch)
- Homepage with capability cards, stats strip, project grid, partner logos
- Secretariat & Programme Management capability page (EN + CY)
- About page
- Contact page
- i18n infrastructure with EN/CY toggle
- Mobile responsive
- Deploy to `vdb-uk.com`

### Phase 2 — Depth
- Remaining capability pages (Research, Funding, Science, ESG)
- Project case study pages (NPK Recovery, GripAble, Plus X, BlakBear)
- Partner logo permissions and display

### Phase 3 — Polish
- Testimonials / quotes section
- Blog or news section (optional — for SEO and freshness)
- Analytics (privacy-respecting — Plausible or similar)
- Open Graph / social sharing metadata
- Performance audit
