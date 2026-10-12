# Juice Bar Company website audit and redesign

Prepared for Digital Bar. Audited October 12, 2026.

## Evidence collected

Source: https://thejuicebarjuicecompany.com/. Public sitemap, every public product, all six collections, two editorial articles, About, Contact, search, and empty cart were inspected. 42 screenshots include 37 desktop routes and five mobile template examples. Screenshot index: [screenshot-index.json](research/screenshot-index.json). Original HTML, product JSON, collection JSON, and asset provenance remain in research/. Customer authentication and payment are hosted by Shopify; no private account was inspected and no live purchase was made.

## Offering

21 products: ten juice/drink blends, three cleanse packages, three wellness shots, three half-gallon jugs, one sea moss gel, and one gift card with four denominations. Prices and variant IDs were captured from the public catalog.

| Original product | Price | Category | Variants |
|---|---|---|---|
| Watermelon Punch | $6 | Cold Pressed Juice | 1 |
| 1/2 Gallon Elderberry Tea | $20 | Half-gallon Jugs | 1 |
| 1/2 Gallon Alka-Lime/Strawberry Lemonade | $15 | Half-gallon Jugs | 1 |
| 1/2 Gallon Cold Pressed Juice | $25 | Half-gallon Jugs | 1 |
| Refresh | $6 | Cold Pressed Juice | 1 |
| Green Supreme | $6 | Cold Pressed Juice | 1 |
| Strawberry Lemonade | $3.99 | Cold Pressed Juice | 1 |
| 16 oz Sea Moss | $18 | Sea Moss | 1 |
| Wake Up! | $6 | Cold Pressed Juice | 1 |
| Cayenne Ginger (Hot Shot!) | $2 | Wellness Shots | 1 |
| Pineapple Ginger Shot | $2 | Wellness Shots | 1 |
| Apple Ginger Shot | $1 | Wellness Shots | 1 |
| The Juice Bar Juice Company Gift Card | From $10 | Gift Cards | 4 |
| 1 Day Juice Cleanse | $36 | Juice Cleanse Packages | 1 |
| 3 Day Juice Cleanse | $108 | Juice Cleanse Packages | 1 |
| 2 Day Juice Cleanse | $72 | Juice Cleanse Packages | 1 |
| Ginger Ale | $6 | Cold Pressed Juice | 1 |
| Flu Shot | $6 | Cold Pressed Juice | 1 |
| Sunny Day | $6 | Cold Pressed Juice | 1 |
| Beet It | $6 | Cold Pressed Juice | 1 |
| Alka-lime | $6 | Cold Pressed Juice | 1 |

## Findings and changes

The original homepage has an oversized raster logo and a rotating hero that competes with shopping navigation. Collections are distributed between a drawer and homepage sections; wellness shots are absent from the primary menu. The cold-pressed collection also includes the gift card. Ingredients and flavour selection are buried in descriptions, and jug flavour requests depend on checkout notes. Several product descriptions make medical or absolute nutrition claims; redesigned copy focuses on verifiable ingredients, flavour, size, and convenience. Original descriptions remain preserved in the source catalog for client review.

The redesign gives all six categories clear navigation, introduces a spacious Pa’lais-inspired split hero with the client’s actual bottles, makes ingredients prominent, compares cleanse packages by price and bottle count, exposes jug flavour selection before add-to-cart, adds ingredient-aware search and sorting, and keeps the complete catalog. All product and content screens use the same visual system. The family-owned story, location, phone, and email are preserved. No invented hours, discounts, customer reviews, nutrition panels, or policies were added.

## Integration and launch

This is a private staged redesign, not a change to the live store. Catalog prices/availability are an audit snapshot. The local cart persists in the browser and builds a Shopify cart permalink with verified variant IDs, quantities, and jug notes. Shopify retains final checkout, payment, availability checks, fulfilment, gift-card delivery, and customer accounts. Newsletter signup remains a clearly identified staging preview until connected to the client’s Shopify marketing system. Direct phone/email contact works through native links.

Before a production theme migration, client access is needed for live catalog sync, newsletter capture, native Shopify cart/checkout testing, published shipping/refund policy copy, pickup scheduling, and final brand/content approval. The existing source site does not publish operating hours or substantive refund/shipping policies in its visible public content; its refund link leads to Contact.

## Reference and QA

Visual direction: the user-requested Pa’lais reference, with restrained product hierarchy informed by Misuko. White and ghost-frost canvases, ocean-blue actions, playful condensed headings, handwritten supporting phrases, and organic decorative shapes. See DESIGN.md and REFRESH.md for role-based tokens and decisions. Validation covers public route availability, local links/assets, product coverage, desktop/mobile layout, search, sorting, image galleries, gift amounts, jug flavour selection, local cart persistence and totals, and checkout URL construction. No live order is submitted during QA.
