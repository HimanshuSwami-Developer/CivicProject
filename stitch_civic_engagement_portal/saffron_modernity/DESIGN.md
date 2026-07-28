---
name: Saffron Modernity
colors:
  surface: '#f8f9fa'
  surface-dim: '#d9dadb'
  surface-bright: '#f8f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f5'
  surface-container: '#edeeef'
  surface-container-high: '#e7e8e9'
  surface-container-highest: '#e1e3e4'
  on-surface: '#191c1d'
  on-surface-variant: '#554336'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#887364'
  outline-variant: '#dbc2b0'
  surface-tint: '#8f4e00'
  primary: '#8f4e00'
  on-primary: '#ffffff'
  primary-container: '#ff9933'
  on-primary-container: '#693800'
  inverse-primary: '#ffb77a'
  secondary: '#586062'
  on-secondary: '#ffffff'
  secondary-container: '#dae1e3'
  on-secondary-container: '#5d6466'
  tertiary: '#9f3e43'
  on-tertiary: '#ffffff'
  tertiary-container: '#ff9395'
  on-tertiary-container: '#7d242b'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdcc2'
  primary-fixed-dim: '#ffb77a'
  on-primary-fixed: '#2e1500'
  on-primary-fixed-variant: '#6d3a00'
  secondary-fixed: '#dde4e6'
  secondary-fixed-dim: '#c1c8ca'
  on-secondary-fixed: '#161d1f'
  on-secondary-fixed-variant: '#41484a'
  tertiary-fixed: '#ffdad9'
  tertiary-fixed-dim: '#ffb3b3'
  on-tertiary-fixed: '#400009'
  on-tertiary-fixed-variant: '#80272e'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  display-lg:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '800'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
  headline-md:
    fontFamily: Manrope
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
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base-unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
---

## Brand & Style

The brand personality is energetic, warm, and authoritative. It centers on a "Modern Corporate" aesthetic that leans into high-quality typography and intentional whitespace to evoke a sense of reliability and optimism. By moving away from cooler green tones and embracing a vibrant saffron-based palette, the interface feels more sun-drenched, active, and distinct from typical enterprise software.

The design style utilizes a mix of **Minimalism** and **Modern Corporate** influences. It prioritizes clarity and functional beauty, ensuring that the warmth of the primary accent does not compromise the professional integrity of the product. The emotional response should be one of confidence and accessibility.

## Colors

The palette is anchored by **Saffron (#FF9933)**, a high-visibility primary color used for key call-to-actions, active states, and brand-critical iconography. All previous green accents have been purged in favor of this warm spectrum.

- **Primary (Saffron):** Used for buttons, progress indicators, and primary highlights.
- **Secondary (Charcoal):** Provides a grounding contrast for text and heavy UI elements.
- **Success/Positive States:** Instead of green, use a refined Saffron tint or high-contrast neutral-dark tones with specific "check" iconography to indicate completion.
- **Surface Neutrals:** A range of cool-to-warm greys are used to define boundaries and containment without competing with the primary saffron accent.

## Typography

This design system uses **Manrope** for headlines to provide a modern, geometric, and friendly character. Its open apertures ensure legibility at large scales. For body copy and functional labels, **Inter** is utilized for its supreme readability and systematic, utilitarian nature.

Scale is handled through a tight typographic rhythm. Display sizes use tighter letter spacing and heavier weights to create a strong visual anchor. Mobile views automatically downscale "Display" and "Headline Large" tokens to prevent awkward text wrapping on smaller viewports.

## Layout & Spacing

The layout philosophy follows a **Fluid Grid** model with a 12-column structure for desktop and a 4-column structure for mobile. A strict 4px baseline grid governs all spacing decisions, ensuring vertical rhythm and consistent alignment across all components.

- **Desktop:** 12 columns with 24px gutters. The content is capped at a 1280px max-width container to maintain line-length readability.
- **Tablet:** 8 columns with 24px gutters and 24px side margins.
- **Mobile:** 4 columns with 16px gutters and 16px side margins. Components reflow vertically, and padding is reduced to prioritize content density.

## Elevation & Depth

Visual hierarchy is established through **Tonal Layers** and **Ambient Shadows**. This design system avoids harsh borders in favor of soft depth cues that suggest interactivity.

1.  **Level 0 (Floor):** The base background, typically a very light neutral grey.
2.  **Level 1 (Card/Surface):** White surfaces with a subtle, 1px low-contrast outline (#E9ECEF) to define edges.
3.  **Level 2 (Raised):** Used for interactive elements like cards. Features an ambient, diffused shadow with a 12px blur and 4% opacity, slightly tinted with the secondary charcoal color.
4.  **Level 3 (Overlay):** Used for modals and dropdowns. Uses a more pronounced shadow (24px blur, 8% opacity) to create a distinct physical separation from the content below.

## Shapes

The shape language is defined as **Rounded**, striking a balance between organic friendliness and professional structure. 

Standard components (inputs, small buttons) use a 0.5rem (8px) radius. Larger containers, such as cards or featured banners, utilize 1rem (16px) for a more pronounced, modern feel. This consistency in rounding helps soften the impact of the bold Saffron color, making the UI feel approachable.

## Components

- **Buttons:** Primary buttons are solid Saffron (#FF9933) with white text. Hover states should darken to a deep amber. Secondary buttons use a Saffron outline with Saffron text.
- **Chips/Tags:** Status tags that were previously green (Success) now use a light Saffron tint background with dark Saffron text. For generic categories, use neutral grey tints.
- **Inputs:** Use a 1px neutral border that transitions to a 2px Saffron border on focus. Error states remain a clear, accessible red to maintain safety standards.
- **Icons:** All functional icons (e.g., "Success" checkmarks, "Add" buttons) must use Saffron or Charcoal. Never use green.
- **Cards:** Cards should have a white background, Level 2 elevation (shadow), and 1rem corner rounding.
- **Checkboxes & Radios:** When selected, these components are filled with Saffron. The "check" or "dot" remains white for high contrast.