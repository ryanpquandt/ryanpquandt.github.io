# quandtify.com — academic site

Plain static HTML + one CSS file. No build step, no dependencies, no JavaScript beyond a
three-line fallback for the missing headshot.

```
website/
├── index.html                Home — bio, portrait, contact
├── research.html             Research overview — one summary paragraph + three area cards
├── research-economics.html   Economics — publications
├── research-ai.html          AI — publications
├── research-philosophy.html  Philosophy — publications
├── teaching.html             Teaching philosophy (+ commented-out courses section)
├── cv.html                   Positions, education, fields, links to CV PDF
├── styles.css                All styling; edit the :root variables at the top to retheme
├── images/                   Put headshot.jpg here
└── files/                    Put quandt-cv.pdf here (create the folder)
```

## Preview locally

```sh
cd website
python3 serve.py
# open http://localhost:8000
```

`serve.py` is Python's built-in static server with caching turned off, so every refresh
shows the file as it is on disk. (`python3 -m http.server 8000` also works, but browsers
sometimes hold on to an old copy; if a change seems missing, hard-refresh with
Cmd-Shift-R.) No build step. Stop the server with Ctrl-C.

## Editing the research pages

| What                         | File                       | Look for                  |
|------------------------------|----------------------------|---------------------------|
| Summary paragraph            | `research.html`            | `<section id="summary">`  |
| Area cards (one-line blurbs) | `research.html`            | `<div class="areas">`     |
| Page ledes (grey subtitle)   | each research page         | `<p class="lede">`        |

Each area page is a lede plus publication lists in `<ul class="pubs">` format. To move a paper
between areas, cut its `<li>` and paste it into the other file. The sub-navigation
(Overview / Economics / AI / Philosophy) is repeated at the top of all four research pages; if
you rename an area, update it in all four.

Edit HTML in VS Code (`open -a "Visual Studio Code" .`) or in TextEdit with Settings → Open and
Save → "Display HTML files as HTML code" turned on. Saving from TextEdit's formatted view
rewrites the file and drops the stylesheet.

## Before it goes live

1. **Headshot** — `images/headshot.jpg` (900×900, ~150KB) is what the home page shows.
   To swap it, overwrite that file; keep it under ~1000px on the long side.
2. **CV PDF** — lives at `files/quandt-cv.pdf`; overwrite it to update the download.
3. **Email** — `ryan.p.quandt@gmail.com` is used on Home and CV. Swap for a Cicero
   address if you'd rather (three places: `index.html`, `cv.html`, `teaching.html` footer).
4. **Commented-out sections** — `research.html` has a working-papers template;
   `teaching.html` has a courses template; `cv.html` has awards/talks/service headings
   and blank MA/BA entries. Fill in and delete the surrounding `<!-- -->`.

## Publishing

The site is hosted on GitHub Pages from the repository
`github.com/ryanpquandt/ryanpquandt.github.io` (branch `main`, root folder). The `CNAME`
file tells GitHub the custom domain is `quandtify.com`; DNS for the domain is managed at
Cloudflare (four A records to GitHub Pages plus a `www` CNAME to `ryanpquandt.github.io`).

To publish a change, commit and push:

```sh
git add -A
git commit -m "Describe the change"
git push
```

GitHub rebuilds the site within a minute or two. Note: this folder lives in Dropbox, and
`git add` occasionally fails with "short read while indexing"; just run it again.

`.gitignore` keeps `.DS_Store`, Dropbox metadata, and the unused original headshot out of
the repository.

## Retheming

Everything visual is driven by the custom properties at the top of `styles.css`:
`--accent` (currently a muted navy) sets link and rule color, `--serif` sets the
display face used for the name and page titles. Dark mode inherits automatically from
the `prefers-color-scheme` block just below.
