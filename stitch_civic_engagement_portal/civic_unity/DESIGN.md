---
name: Civic Unity
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
  secondary: '#b52426'
  on-secondary: '#ffffff'
  secondary-container: '#ff5a55'
  on-secondary-container: '#600008'
  tertiary: '#002141'
  on-tertiary: '#ffffff'
  tertiary-container: '#003765'
  on-tertiary-container: '#68a2e9'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#adc7f7'
  on-primary-fixed: '#001b3c'
  on-primary-fixed-variant: '#2d476f'
  secondary-fixed: '#ffdad6'
  secondary-fixed-dim: '#ffb3ad'
  on-secondary-fixed: '#410003'
  on-secondary-fixed-variant: '#920212'
  tertiary-fixed: '#d3e4ff'
  tertiary-fixed-dim: '#a2c9ff'
  on-tertiary-fixed: '#001c38'
  on-tertiary-fixed-variant: '#004881'
  background: '#f7fafc'
  on-background: '#181c1e'
  surface-variant: '#e0e3e5'
typography:
  display-lg:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-md:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 40px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

The design system is engineered to project stability, patriotism, and forward-thinking leadership. It targets a broad demographic of voters, donors, and volunteers, necessitating a UI that feels both authoritative and accessible. 

The aesthetic follows a **Corporate / Modern** style, emphasizing clarity and trust. It avoids visual clutter in favor of strong typographic hierarchy and structured layouts. The emotional response is one of reliability and civic duty, utilizing a "State-Modern" approach where traditional political colors are updated with contemporary saturation levels and refined spacing to ensure the organization feels relevant in a digital-first era.

## Colors

The palette is rooted in a deep, institutional Blue (#1A365D) which serves as the primary anchor for navigation, headers, and brand-critical elements. This is complemented by an energetic Primary Red (#C53030) reserved strictly for high-priority Call-to-Action (CTA) elements, such as "Donate" or "Volunteer" buttons, ensuring they command immediate attention without overwhelming the user.

A Tertiary Blue (#2B6CB0) is utilized for interactive elements like text links and secondary buttons to maintain a cohesive blue-dominant brand. The background strategy relies on a clean Neutral Gray (#F7FAFC) and pure white to ensure maximum readability and a sense of transparency. Semantic colors for success, warning, and error follow standard patterns but are adjusted to match the saturation of the primary brand colors.

## Typography

This design system utilizes a dual-font strategy to balance impact with legibility. **Montserrat** is the voice of the brand, used for all headlines and display text. Its geometric construction provides a modern, bold, and authoritative feel. For larger displays, tighter letter-spacing is applied to create a more "monumental" and cohesive look.

**Inter** is the functional workhorse, used for all body copy, inputs, and UI labels. It was selected for its exceptional legibility on digital screens across all ages. Body text maintains a generous line height to ensure policy papers and long-form articles remain comfortable to read. Labels and small navigational elements use a slightly heavier weight of Inter with increased letter-spacing to ensure clarity at small scales.

## Layout & Spacing

The layout is built on a **Fluid Grid** model with a maximum container width of 1280px for desktop screens to prevent line lengths from becoming unreadable. The system uses an 8px base grid to maintain a consistent vertical rhythm. 

- **Desktop:** A 12-column grid with 24px gutters. Content is typically grouped in 4, 6, or 8 column spans to maintain a professional, balanced white-space ratio.
- **Tablet:** An 8-column grid with 20px gutters. 
- **Mobile:** A 4-column grid with 16px margins. Complex desktop layouts reflow into a single vertical stack.

Vertical spacing (stacking) follows a geometric progression (8, 16, 32, 64) to clearly separate distinct sections of information, such as moving from a headline to a body paragraph versus moving between different policy sections.

## Elevation & Depth

Visual hierarchy is primarily achieved through **Tonal Layers** and **Ambient Shadows**. This design system avoids harsh, heavy shadows in favor of subtle, diffused "elevation" levels that signify interactivity.

- **Level 0 (Base):** Neutral Gray background for the main canvas.
- **Level 1 (Cards):** White surfaces with a very soft, 4px blur shadow (5% opacity) to subtly lift policy cards or news snippets from the background.
- **Level 2 (Interactive/Hover):** When a user interacts with an element, the shadow increases to an 8px blur (8% opacity) to provide tactile feedback.
- **Outlines:** High-priority input fields and secondary buttons use a 1px solid border in primary blue or light gray to define boundaries without relying solely on depth.

## Shapes

The design system utilizes **Rounded** shapes (0.5rem / 8px) to soften the institutional feel of the color palette. This choice makes the brand feel more approachable and "people-centric" while still maintaining the structure required for a professional organization.

- **Standard Elements:** Buttons, input fields, and small cards use the base 8px radius.
- **Large Containers:** Hero sections or large feature cards use `rounded-xl` (1.5rem / 24px) to create a modern, framed appearance.
- **Selection Indicators:** Checkboxes and radio buttons maintain subtle rounding (2px and 50% respectively) to align with the overall geometric theme.

## Components

### Buttons
- **Primary (CTA):** Background: Primary Red (#C53030); Text: White; Weight: Bold. Used for the single most important action on a page.
- **Secondary:** Border: Primary Blue (#1A365D); Text: Primary Blue; Background: Transparent/White.
- **Ghost:** Text: Tertiary Blue (#2B6CB0); No background or border unless hovered.

### Input Fields
Inputs feature a 1px border (#E2E8F0) that transitions to Primary Blue on focus. Labels are always positioned above the field using `label-md` typography to ensure accessibility.

### Cards
Cards are the primary container for news, events, and policy items. They feature a white background, 8px corner radius, and a Level 1 shadow. On hover, the card lifts slightly to Level 2.

### Chips & Tags
Used for categorizing news (e.g., "Economy," "Education"). They use a light tint of the Primary Blue (10% opacity) with Primary Blue text to maintain a professional, monochromatic look within the tag.

### Lists
Lists use generous 16px padding between items and a subtle bottom border (#EDF2F7) to separate information without adding visual weight.