# POD Profit Scout

A small GitHub-first starter product for people selling print-on-demand art, stickers, shirts, mugs, or digital downloads.

It turns a messy product folder into a simple readiness report so a seller can see what is ready to publish, what is missing, and what to fix next.

## Why this exists

Marketplace publishing can get blocked by accounts, API keys, reviews, or platform friction. This tool keeps the sale pipeline moving by proving which products are actually ready before you spend time uploading them.

## What it checks

- Product metadata exists
- Image files exist
- Mockup files exist
- Price/title/tag fields are present
- A clean markdown report can be handed to a human publisher or agent

## Quick start

```bash
python pod_profit_scout.py sample_catalog.json
```

Output:

```bash
reports/pod_readiness_report.md
```

## Who it is for

- Etsy sellers
- Printify/Printful POD sellers
- AI-art shop builders
- Agencies managing product drops
- Anyone with a folder full of designs and no clean launch checklist

## Monetization path

GitHub itself is the proof and distribution hub. The paid version can be sold through:

1. GitHub Marketplace if packaged as a GitHub App or Action and accepted as a verified publisher product.
2. GitHub Sponsors tiers for supporters who receive templates, setup help, and private updates.
3. A payment link from Gumroad, Lemon Squeezy, Stripe, Ko-fi, or Buy Me a Coffee linked from this README.
4. Consulting/setup service sold from Issues or Discussions intake.

GitHub does not work like Etsy for ordinary digital files. For fastest cash, use GitHub as the credibility page and attach an external checkout link.

## Buy / checkout rail

**$19 POD Launch Audit Kit**

[Buy the POD Launch Audit Kit — $19](https://buy.stripe.com/test_8x2eVegjY0mE8QEfASd3i00)

Stripe checkout is now wired with the current test-mode Stripe Payment Link. Use this link for test purchases and replace it with a live-mode Stripe Payment Link before claiming live payment collection.

Includes:
- This readiness checker
- Sample catalog format
- Product launch checklist
- Metadata template
- 30-minute setup add-on offered separately

Optional setup service: **$99** through GitHub Issues.

See `CHECKOUT.md` for the exact buyer flow, delivery copy, and setup-service intake.

## Files

- `pod_profit_scout.py` — readiness checker
- `sample_catalog.json` — sample products
- `templates/product_metadata_template.csv` — metadata starter template
- `templates/launch_checklist.md` — checklist for publishing
- `SALES_PAGE.md` — copy for the GitHub repo or external checkout page
- `CHECKOUT.md` — checkout rail, delivery copy, and setup-service intake

## License

Starter public version: MIT.

Paid templates, setup service, and custom automation can be sold separately.
