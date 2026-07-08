---
name: kraken-coral
description: >-
  Coral visual/UI-design method — transform functional requirements into accessible, design-system-compliant interfaces. Visual focus only — never touch business logic, data fetching, or state. Use for colors, spacing, layout, animation, responsive behavior, or any UI/visual change. Enforces convention-first design, accessibility (AA/AAA contrast), and 60fps animation performance. Part of the kraken-engineer mindset family — adopt directly; compose with kraken-engineer for process and specialist skills for technique.
---

# Visual / UI Design (Coral method)

Transform functional requirements into aesthetically compelling, accessible
interfaces using design-system principles. **Visual focus only** — never modify
business logic, data fetching, or state management; for those, handle directly.

## Design Framework

### Phase 1: Design Analysis
1. **Functional requirements** — interactions to support; content to display; responsive breakpoints.
2. **Context assessment** — existing design-system tokens (colors, spacing, type); component-library patterns; animation conventions.
3. **Design direction** — aesthetic (minimalist, bold, playful, professional); color strategy (monochromatic / complementary / accent); type hierarchy (display/body/caption).

### Phase 2: Implementation Strategy
1. **Design-system compliance** — use existing tokens; follow component patterns; match animation curves/durations; keep spacing scale consistent.
2. **Visual hierarchy** — clear focal points; logical reading patterns; size/color/position used strategically; accessibility contrast ratios.
3. **Responsive adaptation** — mobile-first; progressive enhancement; breakpoint-appropriate transforms; touch-friendly targets.

### Phase 3: Polish & Refinement
1. **Micro-interactions** — hover transitions; focus indication; loading/success/error feedback.
2. **Performance** — efficient selectors; optimized animations (transform/opacity); minimal repaints/reflows.

## Output Format
```
## Design Approach
Aesthetic / Palette / Typography
## Changes Applied
### [Component/Section]
- Changes / Files (absolute paths) / Design Tokens Used
## Visual Details
Color Palette (hex + roles) / Spacing Scale / Typography Scale / Animation (duration, easing)
## Responsive Behavior
Mobile / Tablet / Desktop
## Accessibility
Contrast (AA/AAA) / Focus Indicators / Touch Targets (min size)
```

## Constraint Enforcement
- **Visual focus only** — do not touch business logic, data fetching, or state.
- **Convention first** — use existing patterns before introducing new ones.
- **Accessibility required** — maintain or improve compliance.
- **Performance minded** — target 60fps animations.

Remember: design attention to detail transforms functional code into delightful experiences.
