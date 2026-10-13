# Validation

- Build: 39 HTML routes, 21 products, six collections. All product images and local page/asset references resolve.
- JavaScript syntax check passed.
- 53 browser layout checks: desktop and mobile content/collection templates plus all 21 mobile product pages. No horizontal page overflow or broken loaded images. Detailed evidence: research/responsive-qa.json.
- Tested required jug flavour selection, quantity increment/decrement, $25 jug line arithmetic, $50 gift-card denomination and correct variant ID, subtotal $75, notes persistence across navigation, and checkout URL construction with both variants and jug flavour notes.
- Tested quick-add, removal, empty-cart recovery, modal menu with six collections, ingredient search (ginger returns seven products), zero-result state, ascending-price sort, and product gallery selection.
- Newsletter shows an honest staging message and does not submit personal data. Direct phone/email and directions use native links.
- No live checkout submission or purchase. Shopify handoff needs client acceptance testing before migrating the production theme. Catalog data is an audit snapshot, not a live inventory connection.

Source audit includes 42 screenshots and original HTML/catalog data. Hero photography is an ImageGen composition of the client's bottles; see research/media.md. Gift-card illustration is an original code-based SVG; the original client product image is preserved as a gallery alternative.

Checkout URL format and `note` handling were checked against Shopify's primary documentation: https://shopify.dev/docs/apps/build/checkout/create-cart-permalinks.

## Pa’lais refinement validation

The latest visual pass checked 74 route/viewport combinations: all 21 products and 16 main storefront/content routes at 1440px desktop and 390px mobile widths. No horizontal overflow or broken loaded images. Evidence: research/refinement-qa.json. Product add-to-bag, cart subtotal/removal, required jug flavor selection, and flavor preservation were rechecked through the mobile UI. All 39 generated HTML routes and asset references pass validate.py. Hero, mobile, and full homepage evidence is saved in research/refined-*.jpg.

The current visual reference lock is in REFRESH.md and DESIGN.md. The older screenshots are retained as audit history; refined-* files show the current design.

## Readability and photography — October 13, 2026

117 route/viewport checks passed: all 39 generated pages at 1440px, 390px, and 320px. No horizontal overflow, broken loaded images, or original catalog photos left in the current storefront. Detailed evidence: research/readability-photo-qa.json. Ingredient lines are 14px desktop/13px mobile; category links 15px/13px; product descriptions 16px/15px. Large heading sizes and the approved hero image are preserved. The mobile floating contact shortcut is hidden so it cannot obscure product descriptions; contact remains available through navigation and footer.

Twenty built-in ImageGen photo edits were inspected against original product references. Bottles and sea moss retain their visible brand/title/ingredient label content; shots retain real clear-cup packaging; jugs remain unlabelled; cleanse images have 6, 12, and 18 bottles respectively. Complete package images use contain sizing to avoid cropping products. The gift card uses the existing sharp vector artwork. Prompt/provenance and output filenames: research/studio-photos.json. All images are optimized JPEGs generated from those edits; original client photography remains in the audit assets.

## Bright white finish

117 checks passed across all 39 routes at 1440px, 390px, and 320px. Body and every main section/dialog/form canvas is #ffffff; body reading text is #1d1d1f. No horizontal overflow, unexpected tinted page surfaces, or broken loaded images. Evidence: research/bright-white-qa.json. The approved high-resolution product assets, large heading sizes, shopping functionality, and larger reading sizes remain intact. Desktop/mobile landing-page screenshots are research/bright-white-hero.jpg and research/bright-white-mobile.jpg.
