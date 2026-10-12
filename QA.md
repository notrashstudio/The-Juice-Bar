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
