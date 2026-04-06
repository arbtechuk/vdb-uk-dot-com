# Case Studies Only Refactor Plan

This plan replaces the earlier "projects plus case studies" direction in [docs/plans/case-studies.md](/Users/adam/dev/arbtechuk/vdb-uk-dot-com/docs/plans/case-studies.md). The goal now is simpler: `Case Studies` becomes the only public proof-of-work content type, and every current `Project` is migrated into that format.

## Goal

- Remove `Projects` from the public information architecture.
- Migrate all current project detail pages into case study pages.
- Make the homepage, capability pages, nav, footer, and utility pages consistently point to `Case Studies`.
- Preserve credibility signals from the stronger project pages: outcomes, metrics, timelines, partners, and delivery detail.
- Avoid broken links by keeping a legacy path strategy for `/projects/`.

## Current State Audit

### Content silos

The repo currently has two parallel content types:

- `/projects/index.html` plus 9 detail pages:
  - `npk-recovery.html`
  - `gripable.html`
  - `plus-x-innovation.html`
  - `blakbear.html`
  - `lga-funding-analysis.html`
  - `wales-nutrient-recovery.html`
  - `wales-bilingual-organisations.html`
  - `devolved-political-campaigns.html`
  - `cambridge-sustainability-research.html`
- `/case-studies/index.html` plus 1 detail page:
  - `devolved-funding-architecture.html`

Note: CLAUDE.md's Site Structure section only lists 4 project pages (the product/startup ones). The 5 advisory project pages added later are not reflected there. This is a pre-existing documentation gap.

### IA duplication

- [index.html](/Users/adam/dev/arbtechuk/vdb-uk-dot-com/index.html) has both a `Selected projects` section and a separate `Case Studies` feature section.
- The homepage header nav has *both* a `#projects` link and a `/case-studies/` link — these need collapsing, not just removing one.
- Multiple headers and footers still link to `/#projects`, including the case study pages themselves (`case-studies/index.html` and `case-studies/devolved-funding-architecture.html`).
- The Contact nav link has already been removed from main navigation (commit `6c20035`), but Contact still appears in footers.
- Case Studies nav links were already added to all 9 project detail pages (commit `38204bd`), but those pages also still retain the `/#projects` nav link.

### Capability page label inconsistencies

The capability pages have inconsistent section labels and card patterns. Exact current state:

| Page | Section label | Label element | Card class | Cards link to |
| --- | --- | --- | --- | --- |
| `funding.html` | "Case Studies" | `.label--gold` | `.related-card` | `/projects/*` |
| `research.html` | "Related Projects" | `.label--gold` | `.project-card` | `/projects/*` |
| `science.html` | "Related projects" (lowercase) | `.label--gold` | `.related-card` | `/projects/*` |
| `secretariat.html` | "Related projects" (lowercase) | `.label--gold` | `.related-card` | `/projects/*` |
| `esg.html` | "Case Studies" (label) + "Related Projects" (h2) | `.label--red` | `.related-card` | `/projects/*` |
| `translation.html` | *No project/case study section* | — | — | — |

Issues to resolve:
- Three different label class variants (`.label--gold`, `.label--red`)
- Two different card class names (`.related-card`, `.project-card`)
- Three different label strings ("Case Studies", "Related Projects", "Related projects")
- ESG page has a confusing dual-label: "Case Studies" as the eyebrow label and "Related Projects" as the h2
- Translation page has no cards section at all — it needs cards *added*, not just updated

### Card link text

All capability page cards currently say "View project" / "Gweld prosiect" in their link text. These also need migrating to "View case study" / "Gweld astudiaeth achos" (or similar).

### Project page breadcrumbs

Each project detail page has a breadcrumb-style back-link: `<a href="/#projects">Projects</a>`. After migration, these become case study pages and need to link back to `/case-studies/` with "Case Studies" text.

### Template mismatch

There are effectively two proof-of-work templates in the site:

- Project pages:
  - More operational
  - More metric-heavy
  - Often use sections like `The Brief`, `What We Did`, `Results`, `Timeline`, `Partners`
- Case study page:
  - More narrative
  - More institutional and advisory in tone
  - Uses `Context`, `Objective`, `What We Delivered`, `Why It Mattered`, `Outcome`

### Content clusters

The current project pages split into two groups:

- Product/startup delivery case studies:
  - `npk-recovery`
  - `gripable`
  - `plus-x-innovation`
  - `blakbear`
- Advisory / programme / institutional work that is already close to case-study form:
  - `lga-funding-analysis`
  - `wales-nutrient-recovery`
  - `wales-bilingual-organisations`
  - `devolved-political-campaigns`
  - `cambridge-sustainability-research`

### Platform constraint

This is a static site with no build step. That means legacy URL handling must be done in one of two ways:

- Static redirect stubs in `/projects/`
- VPS/nginx rewrites added outside the HTML files

The repo alone cannot guarantee true HTTP 301s unless the infra config is also changed.

## Target State

### Public IA

`Case Studies` becomes the only public proof-of-work destination.

Recommended target structure:

```text
/
├── index.html
├── case-studies/
│   ├── index.html
│   ├── devolved-funding-architecture.html
│   ├── npk-recovery.html
│   ├── gripable.html
│   ├── plus-x-innovation.html
│   ├── blakbear.html
│   ├── lga-funding-analysis.html
│   ├── wales-nutrient-recovery.html
│   ├── wales-bilingual-organisations.html
│   ├── devolved-political-campaigns.html
│   └── cambridge-sustainability-research.html
└── projects/
    ├── index.html                    # legacy redirect to /case-studies/
    └── *.html                        # legacy redirect stubs to matching case studies
```

### IA rules after refactor

- No header or footer link should say `Projects`.
- No public-facing section heading should say `Related Projects`.
- The homepage should have one case-study section, not parallel project and case-study sections.
- Capability pages should only surface case studies.
- `/projects/` should exist only as a legacy redirect layer during transition.

## Recommended Content Model

Do not force every migrated page into the exact current advisory case-study template. That would flatten the strongest product and delivery stories. Instead, use one case-study model with required core sections and optional evidence modules.

### Required core sections

1. Hero
2. Context
3. Challenge or Objective
4. Approach or What We Did
5. Outcome or Why It Mattered
6. Related Capabilities
7. CTA

### Optional evidence modules

- Metrics strip
- Timeline
- Deliverables grid
- Partner logos
- Supporting image block
- Pull quote
- Outcome checklist / takeaways

### Copy and voice rules

- Default to company voice: `VDB UK`, `we`, `our team`.
- Where work predates VDB UK or was delivered under another institution, add a short provenance note instead of rewriting history.
- Avoid implying that every historical engagement was formally contracted through the current company if that is not true.
- Keep bilingual EN/CY coverage complete on every migrated page.
- Card link text: use "View case study" / "Gweld astudiaeth achos" (not "View project").

### Design rule

The current gold-vs-red distinction exists partly to separate `Case Studies` from `Projects`. Once `Projects` disappears, keep the strongest visual pieces but remove any design logic that only exists to explain two content types.

Recommended:

- Keep the current case-study page as the base visual language.
- Keep red for primary CTA and brand emphasis.
- Use gold for editorial labels, highlights, and selective accents.
- Drop repetitive `Case Study` badges where they become redundant, especially on listing cards.
- Normalise card CSS class to one name (`.cs-card` or `.related-card`, not both plus `.project-card`).

## Migration Inventory

Use the existing project slugs under `/case-studies/` to minimise redirect complexity.

| Current page | Target page | Effort | Migration notes |
| --- | --- | --- | --- |
| `/case-studies/devolved-funding-architecture.html` | Keep in place | Low | Use as the base reference template, but update nav, footer, and related content after `Projects` is removed. |
| `/projects/npk-recovery.html` | `/case-studies/npk-recovery.html` | High | Reframe from a startup/product page into an end-to-end circular nutrient recovery case study. Preserve metrics and timeline as optional evidence modules. |
| `/projects/gripable.html` | `/case-studies/gripable.html` | Medium | Reframe around multi-partner medtech programme delivery, partner coordination, and grant-backed execution. |
| `/projects/plus-x-innovation.html` | `/case-studies/plus-x-innovation.html` | Medium | Reframe around accelerator design, innovation ecosystem mapping, and national programme impact. |
| `/projects/blakbear.html` | `/case-studies/blakbear.html` | Medium | Reframe around industrial deployment, food-waste reduction, and commercial scaling support. |
| `/projects/lga-funding-analysis.html` | `/case-studies/lga-funding-analysis.html` | Low | Already close to advisory case study form. Mostly a structural rewrite into the new template. |
| `/projects/wales-nutrient-recovery.html` | `/case-studies/wales-nutrient-recovery.html` | Low | Already consultancy-shaped. Minimal narrative restructuring needed. |
| `/projects/wales-bilingual-organisations.html` | `/case-studies/wales-bilingual-organisations.html` | Low | Already reads like institutional delivery work. Tighten company voice and add provenance if needed. |
| `/projects/devolved-political-campaigns.html` | `/case-studies/devolved-political-campaigns.html` | Medium | Strong candidate for the new format, but requires careful handling of political sensitivity and provenance. |
| `/projects/cambridge-sustainability-research.html` | `/case-studies/cambridge-sustainability-research.html` | Medium | Reframe around research, systems analysis, and strategic design; retain clear provenance to Cambridge-linked work. |

## File-Level Impact

### Pages that need IA cleanup

- [index.html](/Users/adam/dev/arbtechuk/vdb-uk-dot-com/index.html)
- [about.html](/Users/adam/dev/arbtechuk/vdb-uk-dot-com/about.html)
- [contact.html](/Users/adam/dev/arbtechuk/vdb-uk-dot-com/contact.html)
- [privacy.html](/Users/adam/dev/arbtechuk/vdb-uk-dot-com/privacy.html)
- [cookies.html](/Users/adam/dev/arbtechuk/vdb-uk-dot-com/cookies.html)
- [accessibility.html](/Users/adam/dev/arbtechuk/vdb-uk-dot-com/accessibility.html)

### Capability pages that need card and copy changes

- [capabilities/funding.html](/Users/adam/dev/arbtechuk/vdb-uk-dot-com/capabilities/funding.html)
- [capabilities/research.html](/Users/adam/dev/arbtechuk/vdb-uk-dot-com/capabilities/research.html)
- [capabilities/science.html](/Users/adam/dev/arbtechuk/vdb-uk-dot-com/capabilities/science.html)
- [capabilities/secretariat.html](/Users/adam/dev/arbtechuk/vdb-uk-dot-com/capabilities/secretariat.html)
- [capabilities/esg.html](/Users/adam/dev/arbtechuk/vdb-uk-dot-com/capabilities/esg.html)
- [capabilities/translation.html](/Users/adam/dev/arbtechuk/vdb-uk-dot-com/capabilities/translation.html)

### Case study pages that need updates

- [case-studies/index.html](/Users/adam/dev/arbtechuk/vdb-uk-dot-com/case-studies/index.html)
- [case-studies/devolved-funding-architecture.html](/Users/adam/dev/arbtechuk/vdb-uk-dot-com/case-studies/devolved-funding-architecture.html)
- 9 new migrated case-study pages under `/case-studies/`

### Legacy project pages that need redirect treatment

- [projects/index.html](/Users/adam/dev/arbtechuk/vdb-uk-dot-com/projects/index.html)
- Each detail page currently in `/projects/`

### Documentation that should be updated after implementation

- [CLAUDE.md](/Users/adam/dev/arbtechuk/vdb-uk-dot-com/CLAUDE.md)

## Recommended Rollout Order

### Phase 0: Normalise existing inconsistencies

Before content migration begins, clean up the inconsistencies that already exist across capability pages. This makes migration diffs cleaner and reduces merge-conflict risk.

- Normalise all capability page section labels to one string: "Case Studies" / "Astudiaethau Achos".
- Normalise all card classes to one name (recommend `.cs-card` to match the case-studies index page).
- Fix the ESG page dual-label: remove the "Related Projects" h2 text, replace with a contextual heading like the other pages use.
- Normalise label element class to `.label--gold` everywhere.
- Change all "View project" / "Gweld prosiect" link text to "View case study" / "Gweld astudiaeth achos".
- Add a case study cards section to `translation.html` (currently has none).

This phase can be done in a single commit and is independent of content migration.

### Phase 1: Lock the new case study model

- Confirm that `Case Studies` is the only public label going forward.
- Confirm slug strategy:
  - Recommended: keep current project slugs and move them under `/case-studies/`.
- Confirm provenance rule for historically personal or institution-linked work.
- Confirm whether the homepage section should be called `Selected Case Studies` or simply `Case Studies`.
- Decide homepage curation: which 4–6 of the 10 case studies get homepage placement, and by what criteria.

### Phase 2: Build the unified template

- Use [case-studies/devolved-funding-architecture.html](/Users/adam/dev/arbtechuk/vdb-uk-dot-com/case-studies/devolved-funding-architecture.html) as the base page shell.
- Add optional modules needed by the stronger project stories:
  - metrics
  - timeline
  - partners
  - supporting imagery
- Make that template the default for all future proof-of-work pages.

### Phase 3: Migrate the low-risk advisory pages first

Start with the pages that already read like case studies:

- `lga-funding-analysis`
- `wales-nutrient-recovery`
- `wales-bilingual-organisations`
- `devolved-political-campaigns`
- `cambridge-sustainability-research`

Reason:

- Faster wins
- Quicker consistency on capability pages
- Less risk of weakening the strongest product-led stories before the template has optional evidence modules

### Phase 4: Migrate the product/startup pages

Then migrate:

- `gripable`
- `plus-x-innovation`
- `blakbear`
- `npk-recovery`

These should keep strong evidence components, but the framing should shift from `here is a project` to `here is the client challenge, our role, our approach, and the outcome`.

### Phase 5: Switch the public IA

- Replace the homepage project section with a single case-study section.
- Collapse the duplicate homepage nav links (`#projects` + `/case-studies/`) into one `/case-studies/` link.
- Expand [case-studies/index.html](/Users/adam/dev/arbtechuk/vdb-uk-dot-com/case-studies/index.html) from 1 card to the full catalogue.
- Remove `Projects` from headers and footers across *all* pages, including the case study pages themselves (which still have `/#projects` nav links).
- Update project detail page breadcrumb back-links from `/#projects` → `/case-studies/`.
- If Phase 0 was not done earlier, rename any remaining `Related Projects` sections to `Related Case Studies` or a stronger contextual heading such as `Relevant Case Studies`.
- Update capability page card hrefs from `/projects/*` to `/case-studies/*`.

### Phase 6: Add the legacy path layer

- Turn [projects/index.html](/Users/adam/dev/arbtechuk/vdb-uk-dot-com/projects/index.html) into a redirect page to `/case-studies/`.
- Turn each `/projects/*.html` file into a redirect page to its matching `/case-studies/*.html`.
- If true 301s are required, add nginx rules on the VPS as a follow-up infra task.

### Phase 7: QA and cleanup

- Remove leftover `/#projects` links from all live pages.
- Search for `/projects/` references and reduce them to legacy redirect stubs only.
- Update docs so the repo no longer describes `Projects` as a first-class content type.

## Homepage Plan

The homepage should not keep both the current `Selected projects` block and the newer `Case Studies` feature block.

Recommended homepage structure:

- Replace both with one `Selected Case Studies` section.
- Show 4 to 6 cards spanning product delivery, public-sector advisory, and research/system work.
- Keep a single CTA to `/case-studies/`.
- Rename the section anchor to `case-studies`.

For compatibility during transition:

- Either preserve a hidden `projects` anchor near the new section
- Or accept that old `/#projects` links will stop working once nav and footer are updated

Recommendation:

- Keep a temporary compatibility anchor for one release so existing links do not dead-end.

## Capability Page Plan

Each capability page should move to one proof-of-work pattern:

- Section label: `Related Case Studies`
- Cards point only to `/case-studies/*`
- Mix advisory and delivery examples more deliberately

Notes by capability:

- Funding:
  - Currently has: 3 cards (npk-recovery, gripable, plus-x-innovation). Label says "Case Studies" but cards link to `/projects/*`.
  - Good fit for `devolved-funding-architecture`, `lga-funding-analysis`, `npk-recovery`, `plus-x-innovation`
- Research:
  - Currently has: 2 cards (gripable, plus-x-innovation). Label says "Related Projects", uses `.project-card` class (different from other pages).
  - Good fit for `cambridge-sustainability-research`, `gripable`, `plus-x-innovation`, `wales-nutrient-recovery`
- Science:
  - Currently has: 2 cards (npk-recovery, gripable). Label says "Related projects" (lowercase).
  - Good fit for `npk-recovery`, `gripable`, `blakbear`, `wales-nutrient-recovery`
- Secretariat:
  - Currently has: 2 cards (gripable, npk-recovery). Label says "Related projects" (lowercase).
  - Good fit for `gripable`, `devolved-political-campaigns`, `devolved-funding-architecture`, `plus-x-innovation`
- ESG:
  - Currently has: 2 cards (npk-recovery, blakbear). Has a confusing dual-label: "Case Studies" eyebrow + "Related Projects" h2. Uses `.label--red` instead of `.label--gold`.
  - Good fit for `npk-recovery`, `blakbear`, `cambridge-sustainability-research`, `wales-nutrient-recovery`
- Translation:
  - Currently has: **no case study / project cards section at all**. Needs a cards section *built*, not just updated.
  - Good fit for `wales-bilingual-organisations` and `devolved-political-campaigns`

## Redirect and SEO Plan

Recommended default:

- New canonical pages live under `/case-studies/`.
- Old `/projects/*` URLs remain as lightweight redirect stubs.
- Each redirect stub should include:
  - immediate meta refresh
  - canonical link to the new case study URL
  - plain-text fallback link for users with refresh disabled

If the VPS setup is being touched anyway, add server-level rewrites later for real 301 behaviour.

## Acceptance Criteria

The refactor is complete when all of the following are true:

- No public nav or footer item says `Projects`.
- No homepage section is presented as `Projects`.
- The homepage header nav has exactly one proof-of-work link (`/case-studies/`), not two.
- [case-studies/index.html](/Users/adam/dev/arbtechuk/vdb-uk-dot-com/case-studies/index.html) is the single catalogue for proof-of-work content.
- All current project stories exist as case studies under `/case-studies/`.
- Capability pages link only to case studies.
- No card or link text says "View project" — all say "View case study" (or equivalent).
- All capability page section labels, card classes, and label classes are consistent.
- Every capability page (including `translation.html`) has a case study cards section.
- Live HTML outside the legacy redirect stubs contains no internal `/projects/` links.
- Live HTML outside the legacy redirect stubs contains no `/#projects` links.
- Welsh content is present for all new or rewritten copy.
- Historical/provenance-sensitive pages do not overstate VDB UK's formal role.
- CLAUDE.md Site Structure section reflects the new `/case-studies/` layout (not the old 4-project list).

## Risks and Decisions To Make Up Front

### 1. Provenance risk

Some pages currently describe experience that appears personal, pre-company, or delivered under another brand. Those pages should not be rewritten carelessly into pure corporate voice without a provenance line.

### 2. Template over-normalisation

If every migrated page is forced into the current advisory-only case study layout, pages like `npk-recovery` and `gripable` will lose persuasive delivery detail. The unified template must stay modular.

### 3. Homepage density

Moving from 1 case study plus 4 projects to 10 case studies raises curation questions. The homepage should stay selective (4–6 cards), not become a second full index. Decide the curation criteria (recency? sector diversity? strongest outcomes?) in Phase 1, not during implementation.

### 4. Redirect strategy

Static redirect stubs are easy and repo-local. True 301s are cleaner, but require VPS/nginx work.

### 5. Existing inconsistencies compound during migration

The capability pages already have 3 different label strings, 2 different card classes, and 1 page with no cards at all. If these aren't normalised first (Phase 0), each migrated page will either inherit a random variant or require fixing two things at once, making diffs harder to review.

## Recommended Execution Summary

0. Normalise existing capability page inconsistencies (labels, card classes, link text, translation page cards).
1. Build one modular case-study template from the existing case study page.
2. Migrate the five advisory-shaped project pages first.
3. Migrate the four product/startup project pages next, preserving metrics and timelines as optional modules.
4. Replace the homepage project and case-study split with one case-study section. Collapse duplicate nav links.
5. Update all capability pages, nav, footer, and utility pages to remove `Projects`. Update breadcrumbs and card hrefs.
6. Leave `/projects/` in place only as a legacy redirect layer.
