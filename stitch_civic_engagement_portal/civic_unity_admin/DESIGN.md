---
name: Civic Unity Admin
colors:
  surface: '#f7fafc'
  surface-dim: '#d7dadc'
  surface-bright: '#f7fafc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f4f6'
  surface-container: '#ebeef0'
  surface-container-high: '#e5e9eb'
  surface-container-highest: '#e0e3e5'
  on-surface: '#181c1e'
  on-surface-variant: '#43474e'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eef1f3'
  outline: '#74777f'
  outline-variant: '#c4c6cf'
  surface-tint: '#455f88'
  primary: '#002045'
  on-primary: '#ffffff'
  primary-container: '#1a365d'
  on-primary-container: '#86a0cd'
  inverse-primary: '#adc7f7'
  secondary: '#0061a5'
  on-secondary: '#ffffff'
  secondary-container: '#66affe'
  on-secondary-container: '#004172'
  tertiary: '#122234'
  on-tertiary: '#ffffff'
  tertiary-container: '#28374a'
  on-tertiary-container: '#91a0b7'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#adc7f7'
  on-primary-fixed: '#001b3c'
  on-primary-fixed-variant: '#2d476f'
  secondary-fixed: '#d2e4ff'
  secondary-fixed-dim: '#9fcaff'
  on-secondary-fixed: '#001d37'
  on-secondary-fixed-variant: '#00497e'
  tertiary-fixed: '#d4e4fc'
  tertiary-fixed-dim: '#b8c8e0'
  on-tertiary-fixed: '#0d1c2e'
  on-tertiary-fixed-variant: '#39485c'
  background: '#f7fafc'
  on-background: '#181c1e'
  surface-variant: '#e0e3e5'
typography:
  display-sm:
    fontFamily: Montserrat
    fontSize: 30px
    fontWeight: '700'
    lineHeight: 38px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-sm:
    fontFamily: Montserrat
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 18px
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 10px
    fontWeight: '500'
    lineHeight: 14px
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  sidebar-width: 260px
  sidebar-collapsed: 64px
  container-padding: 2rem
  gutter: 1rem
  stack-compact: 0.5rem
  stack-default: 1rem
  stack-loose: 1.5rem
---

## Brand & Style
The design system for the admin environment prioritizes efficiency, oversight, and institutional trust. While the consumer-facing brand is warm and community-driven, the admin variant shifts toward **Modern Corporate Minimalism**. The goal is to reduce cognitive load for operators managing high volumes of data, donations, and reports.

The aesthetic is characterized by high information density, structured layouts, and a "subdued-functional" atmosphere. It retains the core identity through strategic use of typography and the signature primary navy, but introduces a more rigid, grid-based logic to ensure clarity during complex administrative tasks.

## Colors
This design system utilizes a foundation of **Civic Navy (#1a365d)** to maintain brand authority. The palette is expanded with a refined functional set designed for high-glanceability in dashboards:

- **Primary & Core:** The deep navy is used for navigation sidebars and primary actions to anchor the UI.
- **Surface & Background:** A series of cool grays (`#f7fafc` to `#edf2f7`) are used to differentiate content areas without adding visual noise.
- **Semantic Status:** A custom-weighted palette for Success, Warning, and Error is implemented with slightly higher saturation than the standard brand to ensure critical alerts are not missed in dense data tables.
- **Data Visualization:** Use the primary and secondary blues as the baseline, utilizing tertiary grays for background tracks or inactive states.

## Typography
The typography strategy balances brand recognition with extreme legibility for data management:

- **Headlines (Montserrat):** Used sparingly for page titles and section headers to maintain the brand's confident and bold personality.
- **Body (Plus Jakarta Sans):** Replaces the display font for all interface text. Its slightly wider apertures and clean grotesque form ensure readability in long lists and multi-column forms.
- **Data & Labels (JetBrains Mono):** Introduced for transaction IDs, timestamps, and numerical data in tables. The monospaced nature ensures that columns of numbers align perfectly for easy comparison.
- **Scaling:** Mobile font sizes for headlines are capped at 20px to accommodate dense side-scrolling tables and narrow viewports.

## Layout & Spacing
The layout follows a **Fixed-Fluid Hybrid** model optimized for wide-screen monitors:

- **Navigation:** A permanent left-hand sidebar acts as the primary navigation hub. It uses a dark theme (`#1a365d`) to separate intent from content.
- **Content Area:** A fluid white surface that expands to fill the remaining viewport, with a maximum content width of 1600px to prevent line lengths from becoming unreadable.
- **Grid:** A 12-column grid is used for dashboard widgets. Gutters are kept tight (16px) to maximize the amount of information visible above the fold.
- **Breakpoints:**
  - **Desktop (1280px+):** Full sidebar, 3-4 column widget layouts.
  - **Tablet (768px - 1279px):** Collapsed icon-only sidebar, 2 column layouts.
  - **Mobile (<767px):** Bottom navigation or hamburger menu, single column layout.

## Elevation & Depth
In this design system, depth is used to indicate interactivity and information hierarchy without creating visual clutter:

- **Low-Contrast Outlines:** Instead of heavy shadows, use 1px borders (`#e2e8f0`) to define cards and table containers. This maintains a "flat" and professional look.
- **Tonal Layers:** The main background is a light gray (`#f7fafc`), while active work surfaces (cards, whiteboards) are pure white. This creates a subtle lift.
- **Focused Elevation:** Reserved specifically for modals and dropdown menus. Use a single, soft ambient shadow: `0px 4px 12px rgba(26, 54, 93, 0.08)`.
- **Active State:** Hover states on rows or buttons should use a subtle background tint (`#edf2f7`) rather than a shadow to keep the interface feeling fast and responsive.

## Shapes
The shape language is **Soft (0.25rem)**. This provides a clean, modern edge that feels structured and precise, moving away from the playfulness of larger border radii.

- **Standard Elements:** Buttons, input fields, and checkboxes use a 4px radius.
- **Containers:** Large dashboard cards and "wells" use the `rounded-lg` (8px) setting to provide a slight visual distinction from interactive components.
- **Status Pills:** Status tags (e.g., "Pending", "Resolved") are the only exception, using a full pill-shape to distinguish them from clickable buttons.

## Components
- **Data Tables:** The core of the admin experience. Features include zebra-striping on hover, sticky headers, and monospaced font for numerical columns.
- **Primary Buttons:** Solid Civic Navy with white text. Use "Compact" sizing (32px height) for table actions and "Default" (44px) for page-level actions.
- **Input Fields:** Flat design with a 1px gray border. On focus, the border transitions to Civic Navy with a 2px outer glow of 10% opacity.
- **Status Chips:** Small, uppercase labels using `label-sm` typography. Backgrounds are 10% opacity versions of the status colors (Success/Warning/Error) with 100% opacity text.
- **Sidebar Nav:** High contrast (Navy background, light gray text). Active states use a left-hand "accent bar" in Secondary Blue.
- **Stats Cards:** Top-level dashboard cards featuring a large `display-sm` value and a small `label-md` trend indicator (percentage increase/decrease).