# Pa’lais-led refinement

Brief: refine the existing complete Juice Bar storefront for simpler, more beautiful shopping, using the user's explicit Pa’lais reference. Existing catalog, pricing, ingredients, and shopping behavior stay intact.

Reference lock: Pa’lais (https://www.palais.bio/, Refero style 96e33985-645f-449f-8901-02a97a3f81dc). The user-provided older Refero UUID is unavailable; the current same-site style was retrieved instead. Preserve white/ghost-frost canvas, ocean-blue functional ink, playful condensed display headings, handwritten subheads, botanical line motifs, curved decorative color fields, and rounded primary actions. Secondary Misuko reference (32027352-da9e-42e3-838e-476d81d5e316) contributes only restrained card chrome and readable product hierarchy. No palette averaging.

| Decision | Source role | Application |
|---|---|---|
| Split hero with generous space | Pa’lais visual hierarchy and Misuko product focus | A short fresh-by-nature headline, one main shopping CTA, actual bottle composition |
| Playful condensed display font | Pa’lais hero typography | Smaller, easier-to-read headings; replace heavy Work Sans billboards |
| Handwritten accent | Pa’lais secondary typography | One supporting phrase in the hero; restrained use elsewhere |
| White/ocean-blue functional system | Pa’lais canvas and action roles | Clear navigation and filled primary shop/add-to-bag buttons |
| Organic yellow shape and line leaves | Pa’lais decorative-only colors/media | Frame bottles without obscuring the product labels |
| Quiet product cards and concise copy | Misuko restrained commerce pattern | Products, ingredients, and price remain the important content |
| Complete 21-product storefront | User brief and audited catalog | Preserve collections, details, search, gift/jug selection and cart |

Reject: giant background words on every page, multiple stamps and competing hero captions, repeated oversized slogan sections, heavy card borders, decorative shadows on controls, and unsupported product promises.

QA: compare desktop/mobile render to the locked reference; verify page/asset coverage and core product/cart interactions after visual changes. Production integration limitations remain in AUDIT.md.

## Delivery scope

Private staged redesign, not an edit to the live Shopify theme. All 21 catalog products and public content routes use the refined visual system. The local cart persists and links to the existing Shopify store for secure checkout. Customer accounts remain with Shopify. Newsletter signup remains a clearly identified preview pending integration. Source evidence, original screenshots, and integration limitations remain in AUDIT.md.

## Reading and photography refinement

Small shopping and support text uses larger, darker type with comfortable line spacing. Ingredient lists, categories, prices, descriptions, form labels, and order notes receive the increase; the approved display heading sizes and hero composition are preserved. Product media now uses 20 edited studio photographs with softly colored backgrounds and clearer lighting. Real packaging, labels, and cleanse counts remain the invariants. See REFRESH.md, research/media.md and research/studio-photos.json for decisions, final files and exact prompts.

## Bright white finish

The approved Juice Bar/Pa’lais composition and display lettering remain. Apple is the bounded reference for pure white canvas, graphite body text, system UI typography, precise dividers, and restrained product framing. All page/section/dialog/form surfaces use white. Warm page fields and the hero yellow wash are removed. Color remains within the approved product photographs and navy brand/actions; no raster sharpen or brightness filters were added. Reference and role decisions are in REFRESH.md.


Color correction: restore navy reading text, pale yellow hero and gift backgrounds, warm section bands, and borderless header. Keep pure white white-area canvases, system UI typography, enlarged reading sizes, and studio photos. Browser computed styles confirmed navy ink, white body, yellow hero/gift, warm ticker/cleanse, and zero header border. CSS-only update; generated routes unchanged.
