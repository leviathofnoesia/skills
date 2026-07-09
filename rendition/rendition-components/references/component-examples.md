# Rendition component examples (lifted from source specimens)

> Minimal, copy-able markup from `preview/components-buttons.html`, `components-cards.html`,
> `components-nav.html`. All examples assume `tokens.css` is linked (`../tokens.css` in the
> specimens). Specimens hardcode some literals for self-containment — in production use the
> `--c-*`/`--space-*`/`--radius-*` tokens via `var()` (see `rendition-adherence`).

## Buttons

Two tiers. Pill (soft, in-product) and Slab (brutalist, Edition surface).

```html
<!-- Pill tier — Geist 600, 14px, fully-rounded, Dusk→Lilac gradient on primary -->
<button class="btn btn-pill btn-pill-primary">Begin Sanctuary <span class="arr">→</span></button>
<button class="btn btn-pill btn-pill-secondary">Pause</button>
<button class="btn btn-pill btn-pill-tertiary">End early</button>

<!-- Slab tier — Geist 700, 11px, 2px radius, 0.18em uppercase -->
<button class="btn btn-slab btn-slab-primary">Open Sanctuary <span class="arr">→</span></button>
<button class="btn btn-slab btn-slab-onyx">Read Manifesto <span class="arr">→</span></button>
<button class="btn btn-slab btn-slab-dusk">Begin Tour <span class="arr">→</span></button>
<button class="btn btn-slab btn-slab-teal">Confirm</button>
<button class="btn btn-slab btn-slab-ghost">Cancel</button>

<!-- Mini mono tag -->
<button class="btn btn-mini dusk">01</button>
<button class="btn btn-mini lilac">02</button>
<button class="btn btn-mini teal">03</button>
```

Press interaction: subtle "breath" scale on `--ease-breath`; hover lift via `--shadow-md`.
Never raw hex in production — bg from `--c-dusk` / surface tokens.

## Cards

Three siblings, shown here carrying the `.specimen` brutalist wrapper + mono `.strip`.

```html
<!-- Specimen (brutalist): hard corner, pigment border, mono header strip -->
<div class="specimen lilac">
  <div class="strip"><span>+ SPECIMEN · CALM MARKETING</span><span>NPX-CP-A1</span></div>
  <div class="body"> …content… </div>
</div>

<!-- Glass (atmospheric): translucent watercolor surface over imagery. Class is `.glass` (defined in
     tokens.css); the bundled specimens also use the alias `.glass-card` — prefer `.glass`. -->
<div class="glass"> …content… </div>

<!-- Brutal-quote (Edition): Onyx ground, Cormorant italic body, pigment strip -->
<div class="brutal-quote teal">
  <div class="strip"><span>+ VOICE</span><span>NPX-VO</span></div>
  <div class="body">We measure success by how quickly you <span class="em">forget</span> us.</div>
</div>
```

`.specimen` border pigment: base `--c-dusk`, `.teal` → `--c-teal-deep`, `.lilac` → `--c-lilac-deep`.
Glass for atmosphere; specimen for structure.
## Nav

Concrete, copy-able nav markup in the system is the **running header** (`.nav-run`, sticky, hairline
divided cells, `+ 0X` mono codes, single CTA) and the in-app **tab bar** (`.tabbar`, rounded, Onyx
ground, active tab in Lilac with a glow). The "floating pill nav" is a *design intent* (glassmorphic,
Dusk border, grid texture, single primary CTA, Lucide-style icons from `assets/icons/`), not a single
bundled class — compose it from `.glass` + `.nav-run` structure, or lift the full floating nav from the
`rendition-kit` specimens (`preview/components-nav.html`).

```html
<!-- Running header -->
<nav class="nav-run" aria-label="Sample">
  <div class="codes"><span class="reg-mini"></span><span>NPX-0224-S</span><span class="ver">v 2.4</span></div>
  <a class="brand" href="#"><span class="mk"></span><span class="name">nov pax</span></a>
  <div class="links">
    <a href="#"><span class="n">+ 01</span> Manifesto</a>
    <a href="#"><span class="n">+ 02</span> Pillars</a>
    <a href="#"><span class="n">+ 03</span> Sanctuary</a>
  </div>
  <div class="cta"><a href="#">Open Sanctuary →</a></div>
</nav>

<!-- In-app tab bar (Sanctuary) -->
<div class="tabbar">
  <a class="tab active" href="#"><div class="icon"></div><span class="lbl">HOME</span></a>
  <a class="tab" href="#"><div class="icon"></div><span class="lbl">FOCUS</span></a>
  <a class="tab" href="#"><div class="icon"></div><span class="lbl">REST</span></a>
  <a class="tab" href="#"><div class="icon"></div><span class="lbl">SETTINGS</span></a>
</div>
```

## Where the CSS lives

This skill is the **class vocabulary** (names, anatomy, states). The actual visual CSS for `.btn*`,
`.glass`, `.specimen`, `.nav-run`, `.tabbar`, and the primitives is defined in `rendition-tokens`
`assets/tokens.css` and the full styled components in `rendition-kit` (`preview/components-*.html`,
`preview/components-nav.html`). Copy a working styled component from the kit; this file gives you the
correct class names to drop in.

## Primitives (from tokens.css / specimens)

`.divider-edit` (thin line + diamond accent), `.diamond` bullet, `.orb` (companion dusk+lilac glow),
`.t-aurora` gradient text, `.t-display`/`.t-display-it` Cormorant, `.t-kicker`/`.t-marker`/`.t-pixel`
editorial type utilities. State & a11y: focus-visible rings from `--c-dusk`; reduced-motion disables
breath/marquee (see `rendition-a11y`).
