# ColorCargo Legal Docs — GitHub Pages

This `docs/` folder is served via GitHub Pages.

## Files

- `_config.yml` — Jekyll configuration (Cayman theme)
- `index.md` — landing page with links to legal docs
- `privacy.md` — Privacy Policy (mirror of `legal/en/privacy.md`)
- `terms.md` — Terms of Service (mirror of `legal/en/terms.md`)
- `about.md` — About page (mirror of `legal/en/about.md`)

## Updating Content

The canonical source is `legal/en/*.md`. To sync:

```bash
cp legal/en/privacy.md docs/privacy.md
cp legal/en/terms.md docs/terms.md
cp legal/en/about.md docs/about.md
git add docs/ && git commit -m "Sync legal docs to docs/"
git push
```

GitHub Pages rebuilds within ~1 min after push.

## Public URLs (after Pages enabled)

- Landing: `https://<USER>.github.io/<REPO>/`
- Privacy: `https://<USER>.github.io/<REPO>/privacy.html`
- Terms:   `https://<USER>.github.io/<REPO>/terms.html`
- About:   `https://<USER>.github.io/<REPO>/about.html`

Replace `<USER>` and `<REPO>` with actual GitHub username and repository name.
