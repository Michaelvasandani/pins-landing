# Frevana Agent-App Pages: Design Language

Taken from three Frevana agent-app landing pages:

- https://www.frevana.com/agent-apps/ai-product-video
- https://www.frevana.com/agent-apps/aeo
- https://www.frevana.com/agent-apps/ad-clone

All three use the same template (Next.js + Tailwind, shadcn-style tokens). The page skeleton, the tokens and most components are identical. Only the hero visual and one or two content sections change per app. The values below were read from computed styles in the live pages (October 2026).

---

## 1. Overall character

**Calm, editorial and monochrome, with a faint sage-green accent.** It feels closer to an app-store listing or a Notion or Linear docs page than a loud SaaS marketing page.

- **Near-black on off-white.** There are no saturated brand colors in the chrome. Green appears only as a whisper: the trust banner, the hero glow, the rating star and FAQ open states.
- **Regular weight everywhere.** Headings are 400 weight and rely on size and tight negative tracking for hierarchy, not boldness.
- **Soft, rounded surfaces.** Cards are 20–28px radius. Every button and chip is a full pill. Hairline 1px rings (`black/4%`) replace drop shadows.
- **Two surface tones.** White cards are for reading content. Warm-grey `#f3f3f1` cards are for meta information and lists. The page background is `#fafafa`.
- **The product is the hero.** The right half of the hero is a real screenshot or a scaled-down live render of the app UI, with a deep shadow. It is the only element on the page with real depth.
- **SEO-structured content.** The sections are: capabilities, why use it, "People also search" (keyword chips), FAQ and a CTA. The copy is plain and informative, not hype.

---

## 2. Color tokens

### Neutrals (most of the palette)

| Token | Hex | Use |
|---|---|---|
| `--bg-page` | `#fafafa` | Page, header and footer background |
| `--surface` | `#ffffff` | Content cards (Why, People also search, FAQ) and the secondary button |
| `--surface-muted` | `#f3f3f1` | Feature cards, sidebar "app info" card, keyword chips. Slightly warm grey |
| `--surface-hover` | `#efefef` | Nav link hover background |
| `--ink` | `#1a1a1a` | Headings, body emphasis, primary button background, CTA band background |
| `--ink-hover` | `#333333` | Primary button hover |
| `--text-body` | `#3f3f3f` | Chip text, card descriptions |
| `--text-secondary` | `#5c5c5c` | Long-form paragraphs and the hero subhead |
| `--text-nav` | `#555555` | Top nav links |
| `--text-muted` | `#8b8b8b` / `#888888` | Captions, meta rows, eyebrow labels, icon strokes |
| `--text-faint` | `#9a9a9a` | Footer column headings |
| `--border` | `#e5e5e5` / `#e8e8e8` / `#ececec` | Secondary button border, footer top rule, FAQ row dividers |
| `--border-strong` | `#dddddd` | "Sign up" pill outline |
| `--ring` | `rgba(0,0,0,0.04)` | 1px ring on white cards (replaces shadow) |

### Accent: sage and forest green (used sparingly)

| Token | Hex | Use |
|---|---|---|
| `--green-tint` | `#f3f8f4` | Trust banner background |
| `--green-tint-border` | `#e4eee6` | Trust banner top and bottom border |
| `--green-glow` | `#e7f0e8` | Radial hero glow (top center fades to `#fafafa` at 62%) |
| `--green-text` | `#4a6550` | Trust banner text |
| `--green-text-strong` | `#1a2e1c` | Bold brand names in the trust banner |
| `--green` | `#2f7233` / `#3d9040` | Rating star, FAQ toggle border and icon when open (`#3d9040` at 30% opacity) |

### App-specific accent (AEO page only)

The AEO hero embeds a product UI with a deeper forest palette: `#11261b → #1d3b2b` (135° gradient) with a `rgba(101,190,132,.16)` highlight sweep. It also uses ink `#17211c`, borders `#bacac0` / `#ccd8d1`, mint `#96d5ab` and primary `#2f7d4b`. Keep this palette inside the product preview, not in the page chrome.

---

## 3. Typography

- **Family:** `"Noto Sans", sans-serif` for everything (headings, body, UI). The bundle also loads League Spartan, Host Grotesk, Inter and Libre Baskerville, but these pages don't use them. The "Frevana" wordmark is an image.
- **Weight:** effectively **400 everywhere** on the marketing chrome. Classes say `font-medium`, but the rendered weight is 400. The only 600-weight text is inside embedded product UIs, such as the AEO audit header.
- **Tracking:** headings are set tight, at roughly −3% to −4% of the font size. Eyebrows are uppercase with +4% tracking.

| Role | Size / line-height | Tracking | Color |
|---|---|---|---|
| H1 (hero) | 46px / 1.12 | −1.84px (−0.04em) | `#1a1a1a` |
| H2 (section) | 26px / 1.5 | −0.78px (−0.03em) | `#1a1a1a` |
| H2 (CTA band) | 28px / 1.5 | −0.84px | white |
| H3 (feature card, Ad Clone) | 20–22px | −0.03em | `#1a1a1a` |
| Hero subhead | 15→16px / 26px (`leading-relaxed`) | normal | `#5c5c5c` |
| Body long-form | 15px / 28px (`leading-7`) | normal | `#5c5c5c` |
| Card description | 14px / relaxed | normal | `#3f3f3f` |
| Button | 14px (13px small) | normal | — |
| Nav link / chip / meta | 13px | normal | `#555` / `#3f3f3f` / `#8b8b8b` |
| Eyebrow | 12px, UPPERCASE | +0.04em | `#8b8b8b` |
| Footer heading | 12px | normal | `#9a9a9a` |

The type scale is compact. Body sizes are 13–16px and there is one dramatic jump to the 46px H1. Most UI text sits at 13px.

---

## 4. Layout and spacing

- **Content width:** `max-width: 1180px`, centered. Section gutters are `px-4 → sm:px-6 → md:px-10` (16 / 24 / 40px).
- **Section rhythm:** `py-8 md:py-10` (32–40px). The FAQ uses `md:py-12`. The final CTA uses `pb-16 md:pb-20`. Spacing is tight, and sections read as stacked cards rather than full-bleed bands.
- **Hero grid:** two columns at `minmax(0,0.9fr) minmax(0,1.1fr)` with a 32–48px gap. The text column is narrower and the visual is wider. Text measure is capped at `max-w-[460px]`.
- **"Why" section grid:** `minmax(0,1.4fr) minmax(280px,0.8fr)`, with a 24px gap. Long-form text sits in a white card on the left and a sticky-style info aside on the right.
- **Feature grid:** `gap-3` (12px). Product Video and AEO use `md:grid-cols-2 xl:grid-cols-3`. Ad Clone uses `md:grid-cols-2`.
- **Card padding:** 32px (`sm:px-8 sm:py-8`) for white content cards, 24px for the aside and 16–20px for feature cards.
- **Common gaps:** 6, 8, 10, 12, 20, 24 and 40px, on a Tailwind 4px base.

---

## 5. Radius and elevation

| Element | Radius |
|---|---|
| Buttons, chips, tags, icon toggles | `9999px` (full pill) |
| Nav link hover pill | 10px |
| App icon tile | 12px |
| Hero product frame | 16px (`rounded-2xl`) |
| Feature cards | 20px |
| Content cards, aside, video frame | 24px |
| Final CTA band | 28px |

**Elevation is almost flat.**
- Cards: `box-shadow: 0 0 0 1px rgba(0,0,0,.04)`, a ring with no blur.
- Small tags: `ring-1 ring-black/5`.
- **One deep shadow, on the hero product frame only:** `0 1px 3px rgba(0,0,0,.35), 0 18px 40px rgba(0,0,0,.45)` on a `#0a0a0a` background with a 1px border. This makes the screenshot "float" against an otherwise flat page.
- The AEO embedded form uses a tinted shadow: `0 18px 42px rgba(17,38,27,.15)`.

---

## 6. Components

### Top nav
- `#fafafa` background with no border or blur. It is 56px tall with a small top padding.
- Left: a 22px logo mark and the "Frevana" wordmark image (18px tall).
- Center: text links at 13px `#555`, padded `6px 10px`. On hover they get a `#efefef` background, 10px radius and ink-colored text.
- Right: a globe/language icon, a plain-text "Sign in" link and a "Sign up" outline pill (1px `#ddd` border, 13px text, `px-14`).

### Trust banner (directly under the nav)
- Full width, `#f3f8f4` background with `#e4eee6` borders top and bottom. It is 36px tall with centered 13.5px text.
- Copy: "Backed by **a16z, Craft, OpenAI**. Trusted by **500+** leading brands." Brand names use the darker green `#1a2e1c`.
- **Sheen animation:** a 1/3-width `linear-gradient(90deg, transparent, rgba(255,255,255,.65), transparent)` sweeps across every 4.5s (`ease-in-out infinite`).

### Hero
- A background radial glow: `radial-gradient(ellipse at top, #e7f0e8 0%, #fafafa 62%)`, about 420px tall, absolutely positioned.
- Breadcrumb ("Agent apps › App name") in 13px muted text.
- An app identity row: a 44px app-icon tile (12px radius) with the eyebrow `AGENT APP · CATEGORY` (12px uppercase muted).
- H1, then the subhead, then a meta line `5.0 ★ · 1.1k installs` (13px `#8b8b8b`, with a green star and tabular numbers).
- CTA pair, 10px apart:
  - **Primary:** `Open the app`. It is 44px tall with `px-20`, a `#1a1a1a` background, white 14px text and a pill shape. Hover is `#333` with a 150ms transition.
  - **Secondary:** `Browse agent apps`. It is 44px tall with a white background, 1px `#e5e5e5` border and `#444` text, in a pill shape.
- **Right column:** the product visual in a dark rounded-16 frame with the deep shadow. Product Video uses a static screenshot of the app's dark UI. AEO uses a live app component scaled down with `transform-origin: top left` and `pointer-events: none`. Ad Clone uses a light, empty preview frame.

### Feature / capability cards ("What you can do" / "Built for this workflow")
- Section header row: the H2 on the left and a 13px muted caption on the right (right-aligned, `max-w-[420px]`).
- Card: a `#f3f3f1` background, 20px radius, `16px 20px` padding, with a 24px **solid black circular check badge** (white lucide check) followed by 15–16px text.
- Ad Clone variant: a title (20–22px, tight tracking) with a 14px `#3f3f3f` description and no check badge, laid out 2×2.

### "Why teams use…" split
- **Left:** a white card (24px radius, 32px padding, 4% ring). It holds the H2 and three or four 15px/28px `#5c5c5c` paragraphs, spaced 16px apart.
- **Right:** an `<aside>` app-info card with a `#f3f3f1` background, 24px radius and 24px padding.
  - The eyebrow category (12px uppercase).
  - The app name.
  - A `<dl>` of `installs` and `rating` rows (13px, label muted, value ink, justified).
  - Tag pills: white background, 12px `#444` text, `4px 10px` padding, 5% ring.
  - A full-width 40px black pill button, `Open the app`.

### "People also search"
- A white card with a 13px muted caption: "High-intent terms this agent app is built to rank and convert on."
- A wrap of keyword chips: `#f3f3f1` background, 13px `#3f3f3f` text, `6px 12px` padding, full pill, 8px gap.

### Product demo video (Ad Clone)
- An H2 with a 13px muted caption, then a 16:9 `<video>` inside a black, 24px-radius, ring-1 frame.

### FAQ
- A white card with a two-column grid (40px column gap).
- Each item is a native `<details>` with a 1px `#ececec` top border, 16px vertical padding and a 15px question.
- Toggle: a 28px circle with a 1px `#e5e5e5` border and a muted lucide `plus` icon. When open, the plus rotates 45° into an ×, and the border and icon turn green (`#3d9040`).

### Final CTA band
- A `#1a1a1a` block with 28px radius and 40px padding, inside the 1180px container.
- Left: a 28px white H2 and 14px `white/65%` copy (max 460px).
- Right: a white pill button with ink text that turns `#f3f3f1` on hover.
- This is the only dark section on the page, and it works as a visual full stop.

### Footer
- `#fafafa` background with a 1px `#e8e8e8` top border and 56px vertical padding.
- Brand column: the wordmark (about 32px), a tagline ("AI agent apps for more growth and less operations.") and a row of circular social icon buttons.
- Four link columns (Product, Resources, Company, Legal). Each has a 12px `#9a9a9a` heading, with links in 13–14px ink.
- A centered `© 2026 Frevana. All rights reserved.` in muted text, under a divider.

---

## 7. Iconography and imagery

- **Icons:** lucide (`lucide-plus`, `lucide-check` and others), with thin strokes at 14–16px, usually muted grey or white on black.
- **App icons:** square image tiles with 12px corners, shown at 44px.
- **Imagery:** real product UI only. There are no illustrations, stock photos or 3D blobs. The ad-clone video thumbnail is the only "marketing" graphic: a soft green radial blur with large black and green type.

---

## 8. Motion

- Color and background transitions on interactive elements take `150ms cubic-bezier(.4,0,.2,1)` (Tailwind `transition`).
- The FAQ plus icon rotates 45° on open.
- The trust banner sheen is the only ambient animation. It loops every 4.5s with ease-in-out.
- There are no scroll-triggered reveals or parallax. The page is static and fast.

---

## 9. Page structure (template)

```
Header (nav)
Trust banner (green, sheen)
Hero  ── breadcrumb · app icon + eyebrow · H1 · subhead · rating/installs · [Open the app] [Browse agent apps]
      └─ product visual (dark frame, deep shadow)
What you can do / Built for this workflow  ── H2 + right caption · grid of check cards
(app-specific sections, e.g. AEO audit form, Ad Clone 2×2 + demo video)
Why teams use {App}  ── long-form white card | app-info aside
People also search  ── keyword chips
Frequently Asked Questions  ── 2-col <details>
Start using {App}  ── black rounded CTA band
Footer
```

---

## 10. Starter tokens (CSS)

```css
:root {
  --font-sans: "Noto Sans", system-ui, sans-serif;

  --bg-page: #fafafa;
  --surface: #ffffff;
  --surface-muted: #f3f3f1;
  --surface-hover: #efefef;

  --ink: #1a1a1a;
  --ink-hover: #333333;
  --text-body: #3f3f3f;
  --text-secondary: #5c5c5c;
  --text-muted: #8b8b8b;
  --text-faint: #9a9a9a;

  --border: #e5e5e5;
  --divider: #ececec;
  --ring: rgba(0, 0, 0, 0.04);

  --green-tint: #f3f8f4;
  --green-tint-border: #e4eee6;
  --green-glow: #e7f0e8;
  --green-text: #4a6550;
  --green-text-strong: #1a2e1c;
  --green: #3d9040;

  --radius-pill: 9999px;
  --radius-sm: 10px;
  --radius-icon: 12px;
  --radius-frame: 16px;
  --radius-card-sm: 20px;
  --radius-card: 24px;
  --radius-band: 28px;

  --shadow-ring: 0 0 0 1px var(--ring);
  --shadow-hero: 0 1px 3px rgba(0,0,0,.35), 0 18px 40px rgba(0,0,0,.45);

  --container: 1180px;
  --ease: cubic-bezier(.4, 0, .2, 1);
}

h1 { font-size: 46px; line-height: 1.12; letter-spacing: -0.04em; font-weight: 400; }
h2 { font-size: 26px; line-height: 1.5;  letter-spacing: -0.03em; font-weight: 400; }
.eyebrow { font-size: 12px; text-transform: uppercase; letter-spacing: 0.04em; color: var(--text-muted); }

.btn-primary   { height: 44px; padding: 0 20px; border-radius: var(--radius-pill); background: var(--ink); color: #fff; font-size: 14px; transition: background-color .15s var(--ease); }
.btn-primary:hover { background: var(--ink-hover); }
.btn-secondary { height: 44px; padding: 0 20px; border-radius: var(--radius-pill); background: #fff; border: 1px solid var(--border); color: #444; font-size: 14px; }

.card       { background: var(--surface); border-radius: var(--radius-card); padding: 32px; box-shadow: var(--shadow-ring); }
.card-muted { background: var(--surface-muted); border-radius: var(--radius-card-sm); padding: 16px 20px; }
.chip       { background: var(--surface-muted); border-radius: var(--radius-pill); padding: 6px 12px; font-size: 13px; color: var(--text-body); }

.hero-glow  { background: radial-gradient(ellipse at top, var(--green-glow) 0%, var(--bg-page) 62%); }
```

---

## 11. Do / Don't

**Do**
- Keep chrome monochrome, and let product screenshots carry the color.
- Use regular weight with tight negative tracking for headings.
- Make every interactive element a pill.
- Separate content with surface-tone changes (`#fafafa` → `#fff` → `#f3f3f1`), not lines or shadows.
- Reserve green for trust and confirmation moments: the banner, rating and FAQ open state.
- End the page with a single dark rounded CTA band.

**Don't**
- Use bold display type, gradients on text or saturated brand fills.
- Stack heavy shadows. The hero frame gets the only deep one.
- Use illustrations or stock photography. Show the actual app instead.
- Use full-bleed colored sections. Everything except the trust banner sits inside the 1180px container as rounded cards.
