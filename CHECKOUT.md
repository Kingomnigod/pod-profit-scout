# POD Profit Scout Checkout Rail

This file is the checkout rail for the GitHub product. It is designed so the repo can sell immediately once one payment URL is added.

## Current product

**POD Launch Audit Kit** — $19

Includes:
- POD Profit Scout readiness checker
- Sample catalog format
- Product metadata template
- Launch checklist
- Report output workflow

Upsell:
- **Setup service** — $99
- Buyer sends their product folder format and target marketplace; seller helps wire the catalog and first audit.

## Live checkout URL

Current public contact/support rail:

```text
https://github.com/Kingomnigod
```

Stripe is still the preferred direct product checkout once connected. For now, this GitHub profile link is the public GitHub-side contact/support rail from the product page.

Recommended fastest rails:
1. Stripe Payment Link
2. Gumroad product link
3. Lemon Squeezy checkout link
4. Ko-fi or Buy Me a Coffee product/support link
5. GitHub Sponsors tier link

## Buyer flow

1. Buyer clicks **Buy the POD Launch Audit Kit**.
2. Payment page collects $19.
3. Buyer receives the latest release ZIP or repo download instructions.
4. Buyer can optionally request $99 setup help through GitHub Issues.

## Fulfillment copy

Use this on the payment provider delivery page or receipt email:

```text
Thanks for buying the POD Launch Audit Kit.

Download the current repo ZIP here:
https://github.com/Kingomnigod/pod-profit-scout/archive/refs/heads/main.zip

Start here:
1. Unzip the package.
2. Open README.md.
3. Run: python pod_profit_scout.py sample_catalog.json
4. Replace sample_catalog.json with your own catalog when ready.

Need setup help? Open an issue here:
https://github.com/Kingomnigod/pod-profit-scout/issues
```

## GitHub README button

Use this Markdown button once the checkout URL is real:

```md
[Buy the POD Launch Audit Kit — $19](https://github.com/Kingomnigod)
```

## Setup service intake

For the $99 setup service, ask the buyer to open a GitHub Issue with:

- Target marketplace: Etsy, Printify, Printful, Shopify, or other
- Product type: sticker, shirt, mug, digital download, or mixed
- Catalog format: CSV, JSON, spreadsheet, folder of images, or unknown
- Their first blocker
- Whether they want a one-time audit or repeatable workflow

## Verification status

The product is staged and functional locally. Payment is not live until this contact/support URL is replaced with a real provider checkout URL.
