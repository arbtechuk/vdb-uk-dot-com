# Team Carousel — About Page

## Overview

Replace the current text-only "Our Team" statement section on `about.html` with a dynamic, horizontally-scrolling carousel of team member cards. The goal: show VDB has a deep bench of brilliant people across disciplines — scientists, engineers, programme managers, funding strategists — deployed on projects as needed.

Hannah already has a dedicated Founder section above, so she appears in the carousel too but isn't duplicated in detail.

---

## Design Direction: "Editorial Rolodex"

**Aesthetic:** Magazine editorial meets institutional warmth. A slow-drifting horizontal carousel on a dark slate background, with warm gold accents. Each card is a portrait-forward vignette — large circular headshot, name in serif, expertise tag, and a crisp one-liner.

**Key principles:**
- **Portrait-first** — the headshots are the hero, not the text
- **Horizontal drift** — CSS-only infinite scroll animation, no JS libraries
- **Hover reveal** — cards lift and show a short bio on hover/focus
- **Accessible** — pause on hover, keyboard navigable, reduced-motion respects `prefers-reduced-motion`
- **Bilingual** — all text EN/CY with the existing `data-en`/`data-cy` system

**Visual details:**
- Dark section (`--slate-900`) with subtle radial glow behind the carousel
- Headshots in large circles (160px) with a thin gold ring on hover
- Name in Crimson Pro serif, role in Outfit uppercase tracked label
- Cards have a frosted glass background (`rgba(255,255,255,0.04)`) with `backdrop-filter: blur`
- Light theme: stone background, darker card borders, same gold accents
- The carousel duplicates its content for seamless infinite loop

---

## Team Members & Generalised Bios

Roles reframed for VDB (not NPK-specific). Each person gets:
- **Name**
- **VDB Role** (short expertise tag)
- **One-liner** (~20 words, what they bring to VDB projects)

| # | Name | VDB Role | Headshot File | Web-Ready |
|---|------|----------|---------------|-----------|
| 1 | Hannah Van Den Bergh | Founder & Director | Hannah Headshot.jpg | ✓ JPG |
| 2 | Lucy Bell-Reeves | Programme & Partnerships | Lucy Headshot.jpg | ✓ JPG |
| 3 | Philippa Parry | Engineering & Process Design | Phil Headshot.jpeg | ✓ JPG |
| 4 | Joe Nunn | Design & Automation Engineering | Joe Headshot.jpeg | ✓ JPG |
| 5 | Olivia Wilson | Science & Bioprocess | Oli Headshot.jpg | ✓ JPG |
| 6 | Nazanin Arafaty | Agricultural Science & Research | Naz Headshot.jpg | ✓ JPG |
| 7 | George Barnsley | Environmental Research | George Headshot_.png | ✓ PNG |
| 8 | Chloe Todd | Project Coordination & Funding | IMG_0721.HEIC | ⚠ HEIC → convert |
| 9 | Steph Kerley | Finance & Claims | Steph Headshot..heic | ⚠ HEIC → convert |
| 10 | Ian Parry | Technical Engineering | *none available* | ❌ placeholder |
| 11 | Alex McCormack | *TBC — ask Hannah* | Copy of Alex McCormack.jpeg | ✓ JPG |
| 12 | Nicola Cannon | *TBC — ask Hannah* | Nicola Cannon photo June 24.jpg | ✓ JPG (resize) |

**Notes:**
- Alex McCormack and Nicola Cannon have headshots but aren't in team.md — need roles from Hannah
- IMG_0721.HEIC is unidentified — likely Chloe (only person missing a named headshot)
- Ian Parry has no headshot — use initials-based placeholder or omit until photo supplied
- `Phil Headshot 2026` is a newer HEIC — convert and use if better quality than existing JPEG

---

## Image Pipeline

1. **Convert HEIC → JPG** using `sips` (macOS native):
   ```bash
   sips -s format jpeg "Steph Headshot..heic" --out steph-headshot.jpg
   sips -s format jpeg "IMG_0721.HEIC" --out chloe-headshot.jpg
   sips -s format jpeg "Phil Headshot 2026" --out phil-headshot-2026.jpg
   ```

2. **Resize all to max 400×400** (plenty for 160px display + retina):
   ```bash
   sips -Z 400 *.jpg *.jpeg *.png
   ```

3. **Rename to consistent convention** and copy to `images/`:
   ```
   team-hannah.jpg
   team-lucy.jpg
   team-phil.jpg
   team-joe.jpg
   team-oli.jpg
   team-naz.jpg
   team-george.jpg
   team-chloe.jpg
   team-steph.jpg
   team-alex.jpg
   team-nicola.jpg
   ```

4. **Optimise** with `sips` quality reduction or `imagemagick` if available

---

## HTML Structure

Replace the existing `team-statement` section (lines 1617–1632 of about.html) with:

```html
<section class="team-carousel section--dark reveal">
  <div class="team-carousel__header container">
    <span class="label label--gold">Our team / Ein tîm</span>
    <h2>The right expertise for every brief</h2>
    <p class="team-carousel__subtitle">VDB draws on a network of researchers, scientists, engineers, programme managers, and funding strategists...</p>
  </div>

  <div class="team-carousel__track-wrapper">
    <div class="team-carousel__track">
      <!-- Card × N, duplicated for infinite loop -->
      <article class="team-card">
        <div class="team-card__image">
          <img src="/images/team-lucy.jpg" alt="Lucy Bell-Reeves" loading="lazy">
        </div>
        <div class="team-card__info">
          <h3 class="team-card__name">Lucy Bell-Reeves</h3>
          <span class="team-card__role">Programme & Partnerships</span>
          <p class="team-card__bio">Builds strategic partnerships and leads delivery teams across complex multi-stakeholder programmes.</p>
        </div>
      </article>
      <!-- ... more cards ... -->
      <!-- Duplicate set for seamless loop -->
    </div>
  </div>
</section>
```

---

## CSS Carousel Mechanics

```css
.team-carousel__track-wrapper {
  overflow: hidden;
  mask-image: linear-gradient(90deg, transparent 0%, black 8%, black 92%, transparent 100%);
}

.team-carousel__track {
  display: flex;
  gap: 2rem;
  width: max-content;
  animation: scroll-team 40s linear infinite;
}

@keyframes scroll-team {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

/* Pause on hover for accessibility */
.team-carousel__track:hover {
  animation-play-state: paused;
}

@media (prefers-reduced-motion: reduce) {
  .team-carousel__track {
    animation: none;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
  }
  .team-card { scroll-snap-align: start; }
}
```

---

## Card Design

Each `.team-card`:
- Width: ~220px
- Headshot: 160px circle, `object-fit: cover`, thin `--slate-700` border
- On hover: border becomes `--gold-400`, card lifts with `translateY(-4px)`, bio fades in
- Name: Crimson Pro 1.1rem weight 600
- Role: Outfit 0.72rem uppercase tracked, `--gold-500` colour
- Bio: Outfit 0.85rem, `--slate-400`, max 2 lines

---

## Light Theme

- Section bg: `--stone-100`
- Card bg: `white` with `--slate-200` border
- Name: `--slate-900`
- Role: `--gold-600` (WCAG-safe)
- Bio: `--slate-600`

---

## Questions for Hannah

1. Who are Alex McCormack and Nicola Cannon? What are their VDB roles?
2. Is IMG_0721.HEIC Chloe Todd's headshot?
3. Does Ian Parry have a headshot, or should we omit him for now?
4. Any team members to add or remove from the carousel?
5. Should Hannah appear in the carousel too, or is the Founder section enough?

---

## Implementation Order

1. ✅ Write this plan
2. Process & optimise images (HEIC conversion, resize, rename, copy to `images/`)
3. Write generalised bios for each team member
4. Build carousel HTML/CSS/JS into `about.html`
5. Test both themes, mobile, reduced-motion
6. Get Hannah's answers to open questions, iterate
