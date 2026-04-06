# Case Studies — First-Class Content Type for VDB UK

## Why Case Studies?

The existing `/projects/` pages showcase startup and product partnerships (NPK Recovery, GripAble, Plus X, BlakBear) — they use timelines, stats strips, and technical workstream breakdowns. They're great for demonstrating hands-on delivery.

**Case studies** serve a different purpose. They tell the story of strategic, consultancy-level engagements — often institutional, government, or cross-sector work — where the value is in navigation, advice, and relationship-building rather than building a product. The format is narrative, not technical.

This distinction matters because VDB UK operates at both levels: deep technical delivery *and* high-level strategic advisory. Case studies let the site speak to public sector and institutional clients in a language they recognise.

---

## Architecture

### URL Structure

```
/case-studies/
├── index.html                          # Case Studies landing page (filterable grid)
├── devolved-funding-architecture.html  # First case study (Wales/ACW)
└── [future-slug].html                  # Template for additional case studies
```

### Navigation Changes

Add "Case Studies" to the header nav on **all pages**, between "Projects" and "About":

```html
<ul class="header__links">
  <li><a href="/#capabilities">Capabilities</a></li>
  <li><a href="/#projects">Projects</a></li>
  <li><a href="/case-studies/">Case Studies</a></li>  <!-- NEW -->
  <li><a href="/about.html">About</a></li>
  <li><a href="/contact.html">Contact</a></li>
</ul>
```

Welsh: "Astudiaethau Achos"

### Homepage Integration

Add a new section on `index.html` between the Projects section and the CTA/footer, or integrate case study cards into the existing Projects grid with a visual differentiator (e.g., a "Case Study" label badge vs "Project" badge).

**Recommended approach:** Add a dedicated "Case Studies" strip below Projects on the homepage — a single featured case study with a "View all case studies" link. This keeps the two content types visually distinct.

---

## Case Study Page Template

Each case study page follows a consistent structure, different from the project template:

### Sections (top to bottom)

1. **Hero** — Full-width dark hero with background image, breadcrumb, title, and one-line summary
2. **Context** — Narrative introduction setting the scene (stone background)
3. **Objective** — What we set out to achieve (white background)
4. **Deliverables** — Bullet list of concrete outputs, styled as cards or a clean list (dark section)
5. **Why It Mattered** — The strategic significance (stone background, pull-quote styling)
6. **Outcome** — Results and lasting value (white background)
7. **Related Capabilities** — Links to relevant capability pages
8. **CTA** — Contact call-to-action strip

### Design Philosophy

- **More narrative, less data** — No stats strip or timeline. Case studies are about *understanding*, not metrics.
- **Pull quotes** — Extract key phrases as large serif pull quotes to break up prose.
- **Warm, institutional feel** — Use stone/cream backgrounds more than the dark slate. This content speaks to government/public sector readers.
- **Company voice** — Always "our team" / "we" / "VDB UK", never "Hannah". The company is the actor.

---

## Case Study #1: Devolved Funding Architecture

### Metadata
- **Slug:** `devolved-funding-architecture`
- **Title:** Understanding and Navigating the Funding Architecture of a Devolved Economy
- **Short title (for cards):** Devolved Funding Architecture
- **Client/Context:** Arts Council of Wales / Wales Arts International
- **Capability tags:** Funding & Grant Strategy, Secretariat & Programme Management
- **Hero image:** `images/casestudy-wales-senedd.jpg`

### Content (rewritten in company voice)

#### Context

Working with Arts Council of Wales through Wales Arts International, our team operated at the intersection of culture, public policy, and international funding. In a devolved nation, cultural funding is rarely straightforward: opportunities sit across different layers of government, public bodies, local authorities, and international schemes — each with their own priorities, rules, and timelines.

Our focus was on making that landscape legible and usable. We advised government, local authorities, and the wider cultural sector on how to understand and engage with European funding opportunities in ways that were both strategic and practical.

#### Objective

To help Wales navigate a complex devolved funding environment and make better use of major European cultural and education funding schemes.

This meant translating policy and funding frameworks into real opportunities for public bodies and the arts sector, while strengthening the relationships needed to support future collaboration, investment, and cultural ambition.

#### Deliverables

- Formal advice to ministers, government officials, local authorities, and sector leaders on European funding opportunities
- Strategic guidance on major schemes including Erasmus+ and Creative Europe
- Relationship brokering between Wales and international partners, including collaborations across Celtic and minority-language nations such as Scotland, Cornwall, and the Basque Country
- Support for major place-based cultural ambitions, including work connected to Cardiff and Swansea City of Culture bids
- Cross-sector interpretation of funding policy, helping organisations understand how to position projects within a wider public funding architecture

#### Why It Mattered

In a devolved economy, funding is not just about eligibility — it is about alignment. Organisations need to understand how local priorities, national strategy, and international frameworks connect. Without that understanding, valuable opportunities can be missed, partnerships can remain underdeveloped, and ambitious projects can struggle to find the right route to support.

Our work bridged that gap — connecting policy with delivery, funding knowledge with cultural ambition, and public institutions with international opportunity. Just as importantly, we helped people make confident decisions in a landscape that often feels fragmented or opaque.

#### Outcome

This engagement strengthened Wales' ability to engage strategically with complex funding systems rather than respond to them passively. It improved funding readiness, informed decision-making at multiple levels, and helped create the conditions for stronger cross-border cultural collaboration.

The lasting value was not only in individual funding conversations, but in building a clearer, more confident understanding of how a devolved nation can work within a layered international funding environment — and use that understanding to advance cultural, civic, and strategic goals.

---

## Case Studies Index Page

`/case-studies/index.html` — A landing page showing all case studies as cards.

### Layout
- Dark hero with title "Case Studies" and subtitle about VDB's strategic advisory work
- Grid of case study cards (similar to project cards but with a different accent — gold border-top instead of red, to visually distinguish from projects)
- Each card: hero image thumbnail, title, one-line summary, capability tags, "Read case study" link
- Filter by capability tag (JS toggle, no framework)

---

## Images Required

### Case Study #1: Devolved Funding Architecture

Three images needed:

#### 1. Hero Image — `casestudy-wales-senedd.jpg`
The Senedd (Welsh Parliament) building in Cardiff Bay at dusk, with warm golden light reflecting off the water. Modern architecture meets civic pride. Wide angle, editorial photography style.

**Nano Banana 2 prompt:**
```
Editorial photograph of the Senedd Welsh Parliament building in Cardiff Bay at golden hour dusk, warm amber light reflecting on the water, modern sustainable architecture with wooden roof structure, wide angle composition, professional architectural photography, moody atmospheric sky, no people, clean institutional feel, high resolution
```

#### 2. Supporting Image — `casestudy-wales-funding-map.jpg`
Abstract/conceptual image representing interconnected funding layers — a visual metaphor for the complexity of devolved funding architecture. Think: overlapping translucent layers of maps, policy documents, and connection lines in warm gold and slate tones.

**Nano Banana 2 prompt:**
```
Abstract conceptual illustration of interconnected funding layers and policy architecture, overlapping translucent map layers with connection lines and nodes, warm gold and dark slate blue colour palette, clean modern design, data visualisation aesthetic, minimal and sophisticated, editorial style infographic feel, no text
```

#### 3. Supporting Image — `casestudy-wales-collaboration.jpg`
Professional meeting or roundtable setting — diverse group of professionals around a table with documents, suggesting high-level advisory and cross-sector collaboration. Cardiff or Welsh institutional setting.

**Nano Banana 2 prompt:**
```
Professional photograph of a high-level advisory meeting in a modern Welsh government building, diverse group of professionals around a round table with documents and laptops, warm natural lighting through large windows, institutional but contemporary interior, editorial corporate photography style, shallow depth of field, collaborative atmosphere
```

### Case Studies Index Page

#### Header background — `casestudy-index-hero.jpg`
Abstract geometric pattern or aerial view of Cardiff Bay / Welsh coastline that works as a subtle dark background overlay.

**Nano Banana 2 prompt:**
```
Aerial photograph of Cardiff Bay waterfront at twilight, dark moody atmospheric tones, city lights reflecting on water, modern architecture silhouettes, cinematic wide angle drone shot, deep blue and slate tones with warm amber highlights, suitable as dark website hero background with text overlay
```

---

## Implementation Order

1. **Create directory:** `case-studies/`
2. **Build case study page template** — `case-studies/devolved-funding-architecture.html` using the Welsh Slate design system, following conventions from existing project pages but with the narrative structure above
3. **Build index page** — `case-studies/index.html`
4. **Generate images** — Using Nano Banana 2 prompts above
5. **Update navigation** — Add "Case Studies" link to header nav on ALL pages (index, about, contact, all capabilities, all projects, and the new case study pages)
6. **Add homepage section** — Featured case study strip on index.html
7. **Welsh translations** — Add `data-cy` spans for all new content
8. **Update CLAUDE.md** — Add case-studies to site structure

---

## Future Case Studies (suggested)

Hannah can provide additional case studies following this same template. Likely candidates:
- Innovation programme management (secretariat work)
- ESG/sustainability advisory engagement
- Science & engineering funding navigation
- Cross-border research collaboration

Each needs: title, context, objective, deliverables, why it mattered, outcome — all written in company voice.

---

## Design Decisions to Confirm

1. **Gold accent for case studies vs red for projects?** — Helps distinguish the two content types visually
2. **Homepage placement** — Dedicated section below projects, or integrated into projects grid with badges?
3. **Index page** — Do we need filters if there's only 1-2 case studies initially? Suggest keeping it simple and adding filters when there are 4+.
