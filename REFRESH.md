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

## Readability and catalog photography — October 13

Keep the approved hero composition, large display headings, and overall layout. Increase small support text: ingredient lists 14px desktop/13px mobile, collection links 15px/13px, prices 15px/14px, and product descriptions 16px/15px. Increase line spacing and retain dark ink contrast. Small utility labels use 11–13px; forms stay at 16px where appropriate. Navigation collapses before the larger labels can crowd the header.

Replace dull or distracting product backgrounds with consistently lit, soft pastel studio photographs. Use the original client photos as edit targets. Preserve actual container shape, drink color, caps, branding and readable label text. Shots retain their real cup packaging, jugs retain their actual no-label containers, and cleanse packages retain exact 6/12/18 bottle counts. Use built-in ImageGen, not code-based photo manipulation. Every currently displayed catalog image is reviewed; originals stay in the source audit rather than being mixed with the polished storefront images.
