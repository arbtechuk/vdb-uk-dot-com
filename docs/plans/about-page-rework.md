# About Page Rework Plan

> **Status:** Revised
> **Scope:** `about.html`, `images/hannah-blouse.jpg`
> **Goal:** Reposition the About page around present-day capability and proof, not startup-origin storytelling.

## Why

The current About page still tells a "started as one person in 2019" story. That framing undersells what VDB looks like now: a multidisciplinary consultancy with a wider delivery record across research, funding, science, engineering, ESG, and programme management.

The page should leave a prospective client or partner with a simple impression: VDB already delivers serious work, has the right expertise around the table, and can lead complex programmes from brief to outcome.

## Current State Audit

- The hero subtitle and meta description still foreground `since 2019` / `Founded in 2019`.
- The `Who we are` copy opens with a growth-from-one-person narrative instead of a capability-led one.
- The NPK section gives one spin-out disproportionate space on what should be a company-level credibility page.
- The draft plan introduces `500+ companies advised`, `GBP50m+ grant funding raised`, and `GBP100m+ follow-on investment`, but those figures are not currently evidenced elsewhere in this repo.
- The clearest repo-backed proof point is still `GBP255m unlocked for UK R&D projects since 2020`.
- "Keep company details untouched" conflicts with the stated goal of removing age-signalling. The legal card can stay, but it should not undermine the new positioning.

## Content Principles

- Lead with current capability, not founding chronology.
- Use proof points already supported elsewhere in the site or internal docs.
- Keep NPK / VDB Labs as a case study or venture example, not the centrepiece of the About page.
- Treat incorporation date as a factual company detail, not brand positioning.
- Keep EN/CY coverage complete for every new string, alt attribute, and metadata field.

## Recommended Page Flow

1. Hero
2. Who We Are
3. Track Record
4. Founder & Director
5. Our Team
6. UK Presence + Company Details
7. CTA

## Section Changes

### 1. Hero and Metadata

**Current issue:** The hero subtitle and meta description still invite "how old is this company?" thinking.

**Keep:**
- H1: `About VDB`
- Existing hero image and overall structure

**Change:**
- Replace the hero subtitle with capability-led language.
- Update the localized meta description so it matches the new positioning.
- Remove `since 2019` / `Founded in 2019` from the hero and metadata.

**Recommended hero subtitle:**
- `Multidisciplinary consultancy delivering complex programmes across the UK.`

**Recommended meta description direction:**
- Mention multidisciplinary delivery, UK-wide scope, and the `GBP255m` proof point.
- Keep it short enough to work as a real search snippet.

### 2. Rework "Who We Are"

**Current:**
- Founding story
- Innovation lifecycle description

**New direction:**
- Capability-led framing: VDB assembles the right team for each brief and delivers across disciplines.

**H2:**
- Replace `Programme delivery and innovation - idea to impact`
- With `Whatever the challenge, we deliver it`

**Copy direction:**
- Paragraph 1: VDB is a multidisciplinary consultancy spanning research, funding strategy, science and engineering, ESG, and programme delivery. The point is not one discipline; it is assembling the right team for the job.
- Paragraph 2: Proof through breadth. Reference work across cleantech, healthtech, fintech, government, and the cultural sector, plus the existing repo-backed `GBP255m unlocked for UK R&D projects` signal.

**Keep:**
- `about-team.jpg` as the supporting image. It helps the section feel like a team-led consultancy rather than a solo practice.

**Avoid:**
- `Founded by...`
- `We've grown from...`
- Generic "full innovation lifecycle" language if it starts to sound like a process diagram rather than a capability statement

### 3. Remove the NPK Recovery Section

Remove the current `.vdb-labs` section entirely.

Reason:
- It makes the About page feel too close to a single-project story.
- The page already has better company-level proof in the awards strip and the broader sector story.
- If venture-building proof is needed, it can appear as one sentence in the founder/team copy or remain on project/case-study pages.

Additional note:
- Internal docs now reference the spin-out as `VDB Labs` following the March 2026 rename. If the venture is mentioned anywhere in new copy, use the current naming consistently.

### 4. Add Founder & Director Section

This should replace the current NPK slot in the page flow.

**Photo**
- Use `images/hannah-blouse.jpg`
- Current asset: `896x1195`, roughly `550KB`
- The portrait already suits the site's warm stone/cream palette and works well at a `3:4` crop

**Layout**
- Image left, text right on desktop
- Portrait can be sticky on desktop scroll
- Fall back to a normal stacked layout on tablet/mobile

**Bio direction**
- Target length: `180-220` words, not `280+`
- Frame Hannah as the leader of an established consultancy, not as the protagonist of an origin story
- Good source material already exists in `docs/vandenberghuk.md`: Cambridge sustainability research, UNFCCC policy work, financial-services experience, Arts Council Wales, Julie's Bicycle, C40, and cross-sector programme design

**Stats strip**

Recommended launch version:
- `GBP255m+` unlocked for UK R&D projects
- UK-wide delivery across research, government, and industry
- Portfolio recognised by Earthshot, Terra Carta, Dyson, and Forbes

Important guardrail:
- Only use the `500+ / GBP50m+ / GBP100m+` trio if those figures are confirmed for public use and then applied consistently across the wider site.

### 5. Add "Our Team" Section

**Recommendation for launch:** Use the collective-team statement, not a placeholder carousel.

Reason:
- It projects an established delivery model without inventing bios or publishing incomplete team data.
- It avoids the weak signal of `coming soon`.

**Recommended format:**
- Dark section
- Short heading plus one compact paragraph about the mix of researchers, scientists, engineers, programme managers, and funding strategists VDB draws on

**Future-proofing:**
- This section can later expand into a carousel of named profiles without changing its place in the page flow.

### 6. Keep UK Presence, but Tidy the Company Details Card

The `Working across the UK` section can stay.

The company card should also stay, but with one adjustment:
- Treat incorporation date as a factual compliance detail, not a positioning statement

Recommended change:
- Relabel `Founded` to `Incorporated`
- Place it lower in the card, after the more decision-relevant fields

Keep:
- Legal name
- Companies House number
- Director
- Location

Optional:
- Drop the incorporation row entirely if the aim is to remove age-signalling from every part of the page

### 7. Keep the Rest

No major change needed for:
- Track Record / awards strip
- CTA banner
- Footer

## Technical Notes

- Single file implementation: `about.html`
- No build step
- Remove the `.vdb-labs*` markup, base styles, responsive rules, and light-theme overrides
- Add new `.founder*` and `.team-statement*` styles
- Update the light-theme section for any new selectors
- Extend the smooth-transition selector list if the new sections need it
- Add complete `data-en` / `data-cy` coverage for all new copy
- Add `data-alt-en` / `data-alt-cy` for the founder portrait
- Update localized metadata values in the `<title>` / `<meta name="description">` block if the copy changes
- Because the founder portrait sits below the fold, use explicit `width` and `height`, plus `loading="lazy"` and `decoding="async"` to reduce layout shift
- Optimise `images/hannah-blouse.jpg` before shipping; current `550KB` is heavier than the other About-page images. A target closer to `180-220KB` is more realistic than `150KB` while preserving detail.

## Verification

- Hero subtitle, metadata, and opening copy no longer say `since 2019` or `Founded in 2019`
- No NPK / VDB Labs showcase section remains on the About page
- Founder and team sections render correctly in dark and light themes
- EN/CY toggle switches every new string and image alt attribute
- Layout holds at `1024px`, `768px`, and `480px`
- Sticky founder image works on desktop and falls back cleanly on smaller screens
- Any published metrics match figures already documented in the repo or explicitly approved for public use

## Decisions to Confirm Before Implementation

- Are `500+ companies advised`, `GBP50m+ grant funding raised`, and `GBP100m+ follow-on investment` approved and source-backed for public use?
- Should the company details card keep the incorporation date, or should that row be removed entirely?
