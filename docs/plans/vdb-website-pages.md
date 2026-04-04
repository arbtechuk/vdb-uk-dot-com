# VDB Website — Page-by-Page Build Plan

> **Live site:** https://vdb-uk.com/
> **Repo:** arbtechuk/vdb-uk-dot-com
> **VPS path:** /root/arbtechuk/vdb-uk-dot-com/

Every page follows the same structure: shared header/footer (with EN/CY toggle), bilingual content throughout, consistent "Welsh Slate" design language.

---

## File Structure

```
/
├── index.html                              ✅ DONE
├── about.html
├── contact.html
├── capabilities/
│   ├── secretariat.html
│   ├── research.html
│   ├── funding.html
│   ├── science.html
│   └── esg.html
├── projects/
│   ├── npk-recovery.html
│   ├── gripable.html
│   ├── plus-x-innovation.html
│   └── blakbear.html
├── images/
│   ├── vdb-photo-1.jpg                     ✅ (workshop/post-its)
│   ├── vdb-photo-2.jpg                     ✅ (lab glassware)
│   ├── vdb-photo-3.jpg                     ✅ (planning table overhead)
│   ├── vdb-photo-4.jpg                     ✅ (boardroom meeting)
│   ├── vdb-logo-original.png               ✅
│   ├── hero-secretariat.jpg                🖼 NEEDS GENERATING
│   ├── hero-research.jpg                   🖼 NEEDS GENERATING
│   ├── hero-funding.jpg                    🖼 NEEDS GENERATING
│   ├── hero-science.jpg                    🖼 NEEDS GENERATING
│   ├── hero-esg.jpg                        🖼 NEEDS GENERATING
│   ├── project-npk-field.jpg               🖼 NEEDS GENERATING
│   ├── project-npk-festival.jpg            🖼 NEEDS GENERATING
│   ├── project-gripable-device.jpg         🖼 NEEDS GENERATING
│   ├── project-gripable-therapy.jpg        🖼 NEEDS GENERATING
│   ├── project-plusx-hub.jpg               🖼 NEEDS GENERATING
│   ├── project-blakbear-sensor.jpg         🖼 NEEDS GENERATING
│   ├── project-blakbear-factory.jpg        🖼 NEEDS GENERATING
│   ├── about-futurespace.jpg               🖼 NEEDS GENERATING
│   ├── about-team.jpg                      🖼 NEEDS GENERATING
│   └── contact-bristol.jpg                 🖼 NEEDS GENERATING
├── docker-compose.yml                      ✅ DONE
└── CNAME                                   ✅ DONE
```

---

## Shared Components

### Header (all pages)
Same as homepage — VDB logo, nav links, EN|CY toggle, Contact CTA.
Nav links update to: Capabilities (dropdown), Projects, About, Contact.

### Footer (all pages)
Same as homepage — logo, description, capability links, company links, contact info, copyright.

### Breadcrumb
All subpages get a breadcrumb bar below the header:
`Home > Capabilities > Secretariat & Programme Management`

### Page Hero Pattern
Every subpage uses a consistent hero:
- Full-width image with dark overlay
- Breadcrumb
- Page title (h1)
- One-sentence subtitle
- Height: ~40vh (shorter than homepage hero)

---

## Capability Pages

All capability pages follow this template:

1. **Hero** — capability name, subtitle, background image
2. **Overview** — 2-3 paragraphs explaining what this capability is and who it's for
3. **Our Approach** — 3-4 numbered steps with icons, showing methodology
4. **Key Outcomes** — stats/numbers strip
5. **Related Projects** — 2-3 project cards from this capability area
6. **CTA** — "Discuss a [capability] project with us"

---

### Page: `/capabilities/secretariat.html`

**Title:** Secretariat & Programme Management
**Subtitle:** We run the governance process so you can focus on the mission.
**Primary audience:** Welsh Government, UK public bodies, education boards

#### Content

**Overview:**
Government bodies and public institutions need structured programme delivery across multi-year funded periods. This means stakeholder coordination, meeting management, minute production, compliance reporting, and institutional continuity — delivered by a team that understands governance, not just administration.

VDB has experience managing secretariat functions for government education bodies, research councils, and cross-institutional programmes. We embed within your governance structure and operate as an extension of your team.

**Our Approach (4 steps):**

1. **Stakeholder Mapping & Onboarding**
   - Identify all parties, establish communication protocols, set meeting cadence
   - Develop RACI matrices and governance organograms
   - Create shared workspaces and document management systems

2. **Governance Framework Design**
   - Design meeting structures, agendas, and reporting templates
   - Establish decision-tracking and action-logging processes
   - Define escalation paths and accountability chains

3. **Delivery & Documentation**
   - Chair or support meetings, produce accurate minutes within 48 hours
   - Track actions to completion, compile periodic reports to deadlines
   - Manage correspondence, scheduling, and logistics

4. **Continuity & Knowledge Transfer**
   - Maintain institutional memory across personnel changes
   - Succession planning and handover documentation
   - End-of-programme archiving and lessons-learned reports

**Key Outcomes strip:**
- Multi-year funded programmes delivered
- Government trust and repeat engagements
- Bilingual (EN/CY) documentation capability

**Related Projects:**
- Welsh Education Board (when live — placeholder for now)
- Defra programme management

**Bilingual note:** This page is the highest priority for professional Welsh translation. The Welsh Education Board audience will expect fluent, natural Welsh — not machine translation.

#### Hero Image — Nano Banana Prompt

**`hero-secretariat.jpg`**
> Professional photograph of a modern government committee room during a meeting. A large oval table with 8 chairs, some occupied by professionals reviewing documents. Floor-to-ceiling windows overlooking a civic building exterior. Warm natural light. Notebooks, water glasses, and printed agendas on the table. Muted colour palette — navy suits, grey walls, light wood table. Shot from a slight elevation angle. No faces in sharp focus. Editorial photography style, 16:9 aspect ratio.

---

### Page: `/capabilities/research.html`

**Title:** Research & Innovation
**Subtitle:** Evidence-based insights that validate bold ideas before a penny is spent.
**Primary audience:** Universities, R&D teams, innovation managers

#### Content

**Overview:**
Before building anything, you need to know the idea is sound. VDB's research team undertakes primary and secondary research to validate new concepts, using human-centred design methods and peer-reviewed evidence. We help organisations move from "we think this could work" to "here's the evidence it will."

Our research informs funding bids, product strategies, and policy decisions. We've worked with Imperial College London, the University of Cambridge, and leading UK innovation hubs.

**Our Approach (4 steps):**

1. **Landscape Analysis**
   - Systematic literature reviews and patent landscape scans
   - Competitor and market analysis
   - Policy and regulatory environment mapping

2. **Human-Centred Research**
   - Stakeholder interviews and user workshops
   - Journey mapping and persona development
   - Ethnographic observation and contextual inquiry

3. **Data Synthesis & Insight**
   - Thematic analysis and evidence grading
   - Corporate insights enriched with academic evidence
   - Visual data presentation and insight reports

4. **Strategic Recommendations**
   - Evidence-backed go/no-go recommendations
   - Funding strategy informed by research findings
   - Innovation roadmaps and opportunity prioritisation

**Key Outcomes strip:**
- Research for Imperial College & Cambridge partnerships
- Human-centred design embedded in all projects
- Evidence underpinning £255m in funded projects

**Related Projects:**
- Cambridge — emergent climate trends research
- GripAble/Imperial — SqueezAble feasibility research
- Plus X Innovation — accelerator programme research

#### Hero Image — Nano Banana Prompt

**`hero-research.jpg`**
> Overhead photograph of a design thinking workshop table. Clusters of colourful post-it notes arranged on a white surface, printed user journey maps, a MacBook showing data charts, scattered markers and pens. Two pairs of hands visible reaching for post-its. Warm natural light from the left. Clean, editorial style. Soft focus on edges. 16:9 aspect ratio.

---

### Page: `/capabilities/funding.html`

**Title:** Funding & Grant Strategy
**Subtitle:** £255m unlocked for UK R&D. We know how to win.
**Primary audience:** Startups seeking grants, universities building consortia, SMEs applying for Innovate UK

#### Content

**Overview:**
Securing public funding is a craft. VDB has helped unlock over £255 million for UK R&D projects since 2020, working across Innovate UK, Defra, UKRI, the Forestry Commission, and charitable foundations. We don't just write bids — we build the strategy, assemble the consortium, and position the application to win.

Our team understands what funders are looking for because we've been on both sides of the process. We know the scoring criteria, the review panels, and the narrative structures that succeed.

**Our Approach (4 steps):**

1. **Opportunity Identification**
   - Monitor funding calls across UKRI, Horizon Europe, government departments, and foundations
   - Match opportunities to client capabilities and strategic goals
   - Early engagement with programme managers where appropriate

2. **Consortium Building**
   - Identify and recruit the right partners (academic, industrial, public sector)
   - Negotiate roles, IP, and budget splits
   - Build the team narrative that funders want to see

3. **Bid Development**
   - Craft compelling narratives that connect innovation to impact
   - Develop realistic work packages, Gantt charts, and budgets
   - Ensure compliance with funder requirements and eligibility criteria

4. **Post-Award Support**
   - Project management and milestone reporting
   - Financial compliance and audit preparation
   - Relationship management with funders

**Key Outcomes strip:**
- £255m+ unlocked across 8+ major projects
- Funders include: Innovate UK, Defra, UKRI, Forestry Commission, Co-op
- Clients include Earthshot Prize shortlistees and Forbes 30 Under 30

**Related Projects:**
- NPK Recovery — £2m+ from Innovate UK, Defra, Forestry Commission, Co-op
- GripAble — £800k Innovate UK BMC grant for SqueezAble
- Plus X Innovation — £25m in grants for entrepreneurs

#### Hero Image — Nano Banana Prompt

**`hero-funding.jpg`**
> Abstract 3D data visualisation rendered as a landscape of rising translucent bar charts and flowing golden curves against a deep navy background. Geometric and clean, no text or labels. The bars glow with subtle warm amber light. Minimal, sophisticated, could be a financial dashboard rendered as art. 16:9 aspect ratio, high resolution.

---

### Page: `/capabilities/science.html`

**Title:** Science & Engineering
**Subtitle:** From the lab bench to the market. We build what others only theorise.
**Primary audience:** Deep tech startups, university spin-outs, UKRI-funded project teams

#### Content

**Overview:**
VDB doesn't just consult — we build. Our science and engineering teams develop demonstrators, run field trials, and create scalable solutions that move from concept to validated product. From bio-fertiliser chemistry to medical sensor technology, we bring the technical depth to turn funded research into real-world impact.

Our first spin-out, VDB Labs (formerly NPK Recovery), is proof of the model: lab research validated at the Royal Agricultural University, deployed at UK festivals, and now growing native trees in the Brecon Beacons.

**Our Approach (4 steps):**

1. **Feasibility & Proof of Concept**
   - Lab-scale experiments and prototyping
   - Technical risk assessment and mitigation planning
   - Literature validation and prior art review

2. **Demonstrator Development**
   - Scale-up from lab to pilot
   - Build mobile/modular demonstrator systems
   - Design for field deployment conditions

3. **Field Trials & Validation**
   - Real-world deployment and data collection
   - Independent validation with academic partners (RAU, Imperial)
   - Iterate based on field performance

4. **Scale & Spin-Out**
   - Production-ready design and manufacturing partnerships
   - IP protection and commercial strategy
   - Spin-out company creation and governance

**Key Outcomes strip:**
- VDB Labs: first spin-out, £2m+ funded, RAU-validated
- Team: 8 scientists and engineers
- Validated at Boomtown Festival, TCS London Marathon, Bristol Pride

**Related Projects:**
- NPK Recovery / VDB Labs — bio-fertiliser from waste
- GripAble — SqueezAble soft-sensor paediatric device
- Defra — ammonia emissions reduction

#### Hero Image — Nano Banana Prompt

**`hero-science.jpg`**
> A clean modern laboratory bench with scientific glassware. Erlenmeyer flasks containing bright green liquid, test tubes in a rack, a digital pipette, and a lab notebook. White surfaces, LED panel lighting overhead. Sharp professional photography with shallow depth of field focused on the foreground flask. Cool, clinical colour palette with the green liquid providing colour accent. 16:9 aspect ratio.

---

### Page: `/capabilities/esg.html`

**Title:** ESG & Sustainability
**Subtitle:** Climate research, circular economy, and ESG frameworks that stand up to scrutiny.
**Primary audience:** Corporate ESG teams, fintech compliance, sustainability officers

#### Content

**Overview:**
VDB works at the intersection of sustainability science and business strategy. We help organisations understand their environmental impact, design ESG risk frameworks, and develop circular economy innovations that are backed by evidence — not greenwash.

Our clients include Earthshot Prize shortlistees, Terra Carta Labs winners, and Big 4 consulting firms. We combine deep scientific understanding with practical programme delivery.

**Our Approach (4 steps):**

1. **ESG Risk Assessment**
   - Materiality analysis and risk mapping
   - Regulatory landscape review (CSRD, TCFD, EU Taxonomy)
   - Peer benchmarking and gap analysis

2. **Climate Research & Analysis**
   - Emergent climate trend identification
   - Supply chain emissions mapping
   - Nature-based solution evaluation

3. **Framework Design & Implementation**
   - ESG governance structures and board reporting
   - KPI design and measurement methodology
   - Integration with existing risk management

4. **Circular Economy Innovation**
   - Waste-to-value opportunity identification
   - Pilot programme design and delivery
   - Lifecycle assessment and impact measurement

**Key Outcomes strip:**
- ESG programme designed for Big 4 FinTech
- Climate research with Cambridge
- Clients: Earthshot Prize shortlist, Terra Carta Labs winners, Dyson Award winners

**Related Projects:**
- Cambridge — emergent climate trends research
- Big 4 FinTech — ESG risk management programme
- NPK Recovery — circular economy (waste-to-fertiliser)

#### Hero Image — Nano Banana Prompt

**`hero-esg.jpg`**
> Aerial drone photograph of Welsh countryside — a patchwork of bright green agricultural fields meeting a dramatic coastline. Rolling hills with dry stone walls visible as thin lines. A wind turbine stands on a distant ridge. Golden hour lighting with long shadows. Dramatic cloud formations. Wide-angle cinematic composition showing the scale of the landscape. 16:9 aspect ratio.

---

## Project Case Study Pages

All project pages follow this template:

1. **Hero** — project name, client/partner, one-line result, background image
2. **The Brief** — what was the challenge or opportunity (2-3 paragraphs)
3. **What We Did** — VDB's specific role and methodology (3-4 sections with details)
4. **Results** — measurable outcomes in a stats strip
5. **Timeline** — key milestones (visual timeline)
6. **Partners** — logo strip of partners involved
7. **Related Capabilities** — links back to relevant capability pages
8. **CTA** — "Have a similar challenge?"

---

### Page: `/projects/npk-recovery.html`

**Title:** NPK Recovery / VDB Labs
**Subtitle:** From festival toilets to farm fields — turning human waste into sustainable fertiliser.
**Partner:** VDB Labs Ltd (spin-out)

#### Content

**The Brief:**
The UK uses approximately 1.5 million tonnes of synthetic fertiliser annually. Its production is carbon-intensive and a major source of agricultural ammonia emissions. Meanwhile, human urine — rich in nitrogen, phosphorus, and potassium — is flushed away as waste. VDB saw an opportunity to close this loop.

**What We Did:**

1. **Research & Validation**
   - Developed a biological process using bacteria to break down urine and recover NPK nutrients
   - Set up a wet lab at Future Space, UWE Bristol
   - Conducted independent crop trials at the Royal Agricultural University
   - Result: bio-fertiliser performs comparably to synthetic alternatives

2. **Demonstrator Build**
   - Designed and built modular, transportable treatment units
   - Engineered for field deployment at outdoor events
   - Partnered with Peequal (chemical-free female urinals) for urine collection

3. **Festival Pilots**
   - Bristol Pride 2024: collected ~2,000 litres via Peequal urinals
   - Boomtown Festival 2025: connected to 700-person toilet block, produced 540 litres of stabilised fertiliser product
   - TCS London Marathon 2025: urine recovery partnership

4. **Scale-Up & Forestry**
   - Won £435,627 Forestry Commission grant (3-year project)
   - Growing 4,500 native and threatened tree species (beech, Scots pine) in Bannau Brycheiniog (Brecon Beacons) using urine-derived fertiliser
   - Partnership with Stump Up for Trees

**Results strip:**
- £2m+ grant funding secured
- 8-person team (chemical engineers, R&D scientists)
- RAU-validated: performs as well as synthetic fertiliser
- 540 litres produced from a single festival pilot
- 4,500 native trees being grown with bio-fertiliser

**Timeline:**
- 2023: Lab setup at Future Space
- 2024: Bristol Pride pilot
- July 2025: Boomtown Festival demonstration
- 2025: TCS London Marathon partnership
- 2025–2028: Forestry Commission tree-growing project
- March 2026: Renamed to VDB Labs Ltd

**Partners:** Peequal, Royal Agricultural University, Agri-Epicentre, Forestry Commission, Defra, Innovate UK, Co-op Carbon Innovation Fund, Stump Up for Trees

**Funders:** Innovate UK, Defra, Co-op Carbon Innovation Fund, Forestry Commission

**Related capabilities:** Science & Engineering, Funding & Grants, ESG & Sustainability

#### Images — Nano Banana Prompts

**`project-npk-field.jpg`**
> A wide photograph of young green crop seedlings growing in rows in rich dark Welsh farmland soil. Early morning dew on the leaves. Rolling green hills in the background under a partly cloudy sky. Professional agricultural photography, warm natural tones. No people. 16:9 aspect ratio.

**`project-npk-festival.jpg`**
> An outdoor UK music festival scene at dusk. A modern, clean portable toilet block facility with warm lighting. People walking past in the background, festival tents and stage lighting visible in the far distance. The facility looks professional and well-maintained, not grimy. Editorial photography style. 16:9 aspect ratio.

---

### Page: `/projects/gripable.html`

**Title:** GripAble — Remote Rehabilitation Technology
**Subtitle:** Programme management for the next generation of paediatric rehab devices.
**Partner:** GripAble Ltd / Imperial College London

#### Content

**The Brief:**
GripAble, an Imperial College spinout, had developed a smart handheld rehabilitation device used in 350+ healthcare locations. They won an £800k Innovate UK Biomedical Catalyst grant to develop SqueezAble — a next-generation soft-sensor device for children with cerebral palsy. They needed programme management expertise to deliver the funded project across multiple partners.

**What We Did:**

1. **Programme Management**
   - Managed the SqueezAble project across GripAble, Imperial College's Department of Bioengineering, and NHS clinical partners
   - Coordinated workstreams, milestone reporting, and funder communications
   - Ensured Innovate UK compliance and deliverable tracking

2. **Partner Coordination**
   - Facilitated collaboration between Dr Firat Guder's group (soft-sensor technology) and GripAble's product team
   - Managed clinical input from Imperial College Healthcare NHS Trust
   - Coordinated occupational therapy expertise

3. **Deliverable Management**
   - Tracked technical milestones and budget spend
   - Compiled progress reports for Innovate UK
   - Managed risk register and escalation processes

**Results strip:**
- £800k Innovate UK BMC grant delivered
- 350+ healthcare locations using GripAble products globally
- $11M Series A raised by GripAble
- US expansion via Medline distribution partnership
- Over half of UK stroke pathways now use GripAble

**Partners:** Imperial College London (Dept. of Bioengineering), Imperial College Healthcare NHS Trust, Innovate UK

**Related capabilities:** Secretariat & Programme Management, Research & Innovation, Funding & Grants

#### Images — Nano Banana Prompts

**`project-gripable-device.jpg`**
> A close-up product photograph of a small, sleek handheld medical rehabilitation device. The device is smooth, ergonomic, approximately the size of a computer mouse, with a subtle digital display. White and light grey colours. Placed on a clean white surface with soft studio lighting. Professional product photography, minimal and clinical. 16:9 aspect ratio.

**`project-gripable-therapy.jpg`**
> A rehabilitation therapy session in a bright, modern NHS clinic. An occupational therapist sits beside an elderly patient who is gripping a small device while looking at a tablet screen showing a colourful game. The therapist is smiling and encouraging. Natural light from a large window. Warm, hopeful atmosphere. Professional healthcare photography. No logos or identifiable branding. 16:9 aspect ratio.

---

### Page: `/projects/plus-x-innovation.html`

**Title:** Plus X Innovation — UK Hardware Accelerator
**Subtitle:** Designing the programme that launched 69 hardware startups and created 1,100 jobs.
**Partner:** Plus X Innovation

#### Content

**The Brief:**
Plus X Innovation was building a national network of innovation hubs to support hardware and product startups — an underserved segment that needs physical prototyping facilities, not just desk space. They needed help designing the accelerator programme that would sit at the heart of the Central Research Laboratory (CRL), originally on the former EMI R&D campus in Hayes, West London.

**What We Did:**

1. **Programme Design**
   - Designed the 18-week CRL Accelerator structure and curriculum
   - Defined selection criteria, cohort size, and progression milestones
   - Created the support framework: mentorship, prototyping access, funding guidance

2. **Innovation Ecosystem Mapping**
   - Identified the key partners, mentors, and institutional supporters
   - Mapped the hardware startup landscape and unmet needs
   - Benchmarked against international hardware accelerators

3. **Scaling Strategy**
   - Informed the expansion strategy from Hayes to Brighton and Slough
   - Designed programme variants (BOOST for early-stage, Stage One Pre-Accelerator)

**Results strip:**
- 69 companies supported across 10+ cohorts
- £25m in grant funding won for entrepreneurs
- 1,100+ high-value jobs created
- £180m raised by portfolio companies
- Awards: Property Week Best Newcomer 2022, Deal of the Year 2024

**Timeline:**
- 2015: CRL launched in Hayes on former EMI R&D campus
- 2017–2023: 10 accelerator cohorts at CRL
- June 2020: Plus X Brighton opens (53,000 sq ft)
- Nov 2023: Plus X Slough opens (24,103 sq ft)
- 2026: CRL Accelerator Cohort 12 running

**Partners:** Plus X Innovation, Brunel University London, U+I (developer)

**Related capabilities:** Research & Innovation, Funding & Grants

#### Images — Nano Banana Prompts

**`project-plusx-hub.jpg`**
> Interior of a modern innovation hub and coworking space. A large open-plan room with high ceilings and industrial-style exposed steel beams. Workbenches with 3D printers and prototyping equipment in the foreground. People collaborating in small groups in the background. Natural light streaming through large windows. Warm industrial aesthetic with polished concrete floors, exposed brick, and steel. Professional architectural/interior photography. 16:9 aspect ratio.

---

### Page: `/projects/blakbear.html`

**Title:** BlakBear — Digital Freshness Sensors
**Subtitle:** Supporting the world's first digital freshness sensor company to reduce food waste at scale.
**Partner:** BlakBear Ltd / Cranswick

#### Content

**The Brief:**
BlakBear, an Imperial College spinout, invented the industry's first digital freshness sensor — a paper-based gas sensor placed inside food packaging that measures spoilage in real time, replacing static printed expiry dates with live freshness data. They needed support to grow from a university research project into a commercial operation deployed across major food manufacturers.

**What We Did:**

1. **Innovation Support**
   - Supported BlakBear's transition from research to commercial deployment
   - Helped position the technology for food industry adoption
   - Connected BlakBear with relevant funding and partnership opportunities

2. **Industry Engagement**
   - Facilitated introductions to food manufacturing and retail stakeholders
   - Supported the narrative for Innovate UK co-funded projects
   - Contributed to the farm-to-fork digitisation strategy

**Results strip:**
- $2.65M seed round raised (led by Ada Ventures)
- 17 Cranswick production sites deployed — first for UK meat industry
- ~$750K annual revenue
- 12-person team across Europe and North America
- Investors include Cisco Systems, Imperial College, Mitsubishi Chemical

**Partners:** Ada Ventures, Cranswick, Innovate UK, Greentown Labs

**Related capabilities:** Research & Innovation, Science & Engineering, ESG & Sustainability

#### Images — Nano Banana Prompts

**`project-blakbear-sensor.jpg`**
> Extreme close-up macro photograph of a small, thin paper-based electronic sensor being placed inside clear food packaging containing fresh red meat. The sensor is approximately 2cm square, semi-transparent with tiny circuit traces visible. Gloved hands holding the packaging. Clean, bright commercial photography with a white/clinical background. Sharp focus on the sensor. 16:9 aspect ratio.

**`project-blakbear-factory.jpg`**
> Interior of a modern food processing factory production line. Clean stainless steel conveyor belts with packaged meat products moving along. Workers in white coats and hairnets monitoring the line. Bright fluorescent lighting, spotlessly clean environment. Industrial food manufacturing aesthetic. Shot from a slightly elevated angle showing the length of the production line. 16:9 aspect ratio.

---

## About Page

### Page: `/about.html`

**Title:** About VDB
**Subtitle:** Bristol-based innovation consultancy. Validating ideas, developing collaborations, building innovations since 2019.

#### Content

**Section 1: Who We Are**
VDB (VandenberghUK Ltd) is an innovation consultancy based at Future Space, UWE Bristol's enterprise hub. Founded by Hannah Van Den Bergh in 2019, we've grown from a one-person consultancy to a team that has unlocked over £255 million for UK R&D projects.

We work across the full innovation lifecycle — from validating an early-stage idea through primary research, to building the consortium and securing funding, to delivering the science and engineering that turns concepts into real-world outcomes.

**Section 2: Our Track Record**
Our clients' work has been recognised with some of the UK's most prestigious innovation awards:
- Earthshot Prize shortlist
- Terra Carta Labs winners
- Dyson Award winners
- Forbes 30 Under 30

We've partnered with Imperial College London, the University of Cambridge, Defra, Innovate UK, the Forestry Commission, and leading UK enterprises like Cranswick.

**Section 3: VDB Labs**
In 2023, we created our first spin-out — VDB Labs (formerly NPK Recovery) — to develop sustainable bio-fertiliser from human waste. With 8 scientists and engineers and over £2m in grant funding, VDB Labs is proof that our model works: validate, develop, build.

**Section 4: Based in Bristol**
We operate from Future Space at the University of the West of England — Bristol's hub for deep tech and science-led enterprises. Bristol's vibrant innovation ecosystem gives us direct access to world-class research, a diverse talent pool, and a city that's serious about sustainability.

**Company details sidebar:**

| | |
|--|--|
| Legal name | VandenberghUK Ltd |
| Companies House | #12296613 |
| Founded | November 2019 |
| Director | Hannah Van Den Bergh |
| Location | Future Space, UWE Bristol |

#### Images — Nano Banana Prompts

**`about-futurespace.jpg`**
> Exterior photograph of a modern university enterprise hub building. Glass and steel architecture with clean geometric lines, 3-4 storeys tall. Early morning light with a blue sky and some clouds. A few professionals walking towards the entrance on a landscaped path. Green trees and grass in the foreground. Modern British architecture style. Professional architectural photography. 16:9 aspect ratio.

**`about-team.jpg`**
> A small, diverse professional team of 4-5 people having an informal stand-up meeting in a bright, modern office. Glass walls, whiteboards with diagrams in the background, a shared desk with laptops. The mood is collaborative and energetic. Smart casual dress. Natural light. Professional editorial photography, warm tones. 16:9 aspect ratio.

---

## Contact Page

### Page: `/contact.html`

**Title:** Get in Touch
**Subtitle:** Whether you're exploring a new idea, applying for funding, or need a delivery partner — we'd love to hear from you.

#### Content

**Section 1: Contact Details**
- Email: hannah@vandenberghuk.com
- LinkedIn: linkedin.com/company/vandenberghuk
- Location: Future Space, Stoke Gifford, Bristol

**Section 2: What to Expect**
- We respond within 2 working days
- An initial conversation is always free
- We'll tell you honestly if we're the right fit

**Section 3: Map / Location**
Embedded map showing Future Space, UWE Bristol.

**Section 4: Contact Form (optional)**
Simple form: Name, Email, Organisation, Message, Submit.
(Can be a mailto: link initially, add a form later if needed.)

#### Image — Nano Banana Prompt

**`contact-bristol.jpg`**
> Panoramic photograph of Bristol, UK cityscape at golden hour. The Clifton Suspension Bridge visible in the mid-distance spanning the Avon Gorge. Colourful harbourside buildings in the foreground. Warm evening light with a dramatic sky. The city looks vibrant and modern. Professional landscape photography, wide-angle. 16:9 aspect ratio.

---

## Build Order

### Phase 1 — Structure (do first)
1. Extract shared header/footer/styles into a pattern that all pages reuse
2. Create the 5 capability page HTMLs from template
3. Create the 4 project page HTMLs from template
4. Create About and Contact pages
5. Deploy all to VPS

### Phase 2 — Images
1. Generate all images via Nano Banana using prompts above
2. Optimise (compress to <200KB each)
3. Deploy to VPS images/ directory

### Phase 3 — Polish
1. Internal link check (all nav, cards, breadcrumbs connect correctly)
2. Welsh translation review (professional, not machine — especially Secretariat page)
3. Open Graph meta tags for social sharing
4. Favicon (extract from VDB logo SVG)
5. Mobile responsive testing on all pages
6. Accessibility audit (WCAG 2.1 AA)

---

## Content Notes for Hannah

- **Welsh translations:** Every page needs bilingual content. Machine translation is fine for initial deployment but the Secretariat page and any government-facing content must be professionally reviewed before sharing with Welsh public sector contacts.
- **Secretariat case study:** Need a placeholder or real content about the Welsh Education Board engagement once it's public.
- **Team bios:** Decision needed — show the team on the About page or keep it lean? If yes, need names, roles, and headshots (or generate with Nano Banana).
- **Client quotes:** Any testimonials from project partners would significantly strengthen the project pages.
- **Logo permissions:** Confirm we can display Defra, Innovate UK, Imperial, Cambridge, NHS, Forestry Commission, and Cranswick logos. If not, keep as text names.
