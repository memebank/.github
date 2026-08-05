# MemeBank marketing site

Complete Astro source staged for the future public repository `memebank/memebank.github.io` and URL `https://memebank.github.io/`.

## Canonical planning

- Linear project: [memebank](https://linear.app/denman/project/memebank-3db5f5cc7452)
- GitHub Project: [memebank-project #1](https://github.com/orgs/memebank/projects/1)
- Organization: [memebank](https://github.com/memebank)

## Product context

MemeBank is a Flutter mobile/desktop and Rust service platform for importing, deduplicating, enriching, searching, previewing, sharing, and copying reusable images. Planned enrichment includes OCR, captions, tags, embeddings, full-text/vector search, and portable storage across S3/R2 and user-owned drive providers. ClipTown interoperability stays behind explicit API/SDK boundaries.

There is not yet a public `memebank-clients` repository. The page therefore labels its TypeScript, Python, curl, and job-document examples as an **API preview**, not as released SDKs.

## Publish

1. Create public repository `memebank.github.io` in the `memebank` organization.
2. Copy this directory to its repository root.
3. Run `npm install && npm run build`.
4. Add the standard Astro GitHub Pages workflow and select GitHub Actions as the Pages source.
5. Verify `https://memebank.github.io/` and update the linked GitHub and Linear tickets.
