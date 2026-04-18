# Tap to Trust — Deck

Web-based Slidev deck. Embeds the Lovable mock **live** in an iframe, so whenever the prototype updates the deck updates too.

## Run it

```bash
cd presentation
npm install
npm run dev
```

Opens at `http://localhost:3030`.

## Export

```bash
npm run build     # static site → dist/
npm run export    # → slides-export.pdf
```

## Edit

Everything lives in [`slides.md`](./slides.md). Each `---` is a slide. Markdown + Vue + Tailwind.

## The Lovable URL

The iframes point to `https://hands-free-help.lovable.app`. If Lovable publishes the app at a different URL, swap it in `slides.md` (two places: the Live Prototype slide and the Walkthrough slide).

## Deck flow

1. Title
2. The 10-second problem
3. Target user (3 personas)
4. The response spectrum (7 ways)
5. The 6-step shape
6. **Live prototype (iframe)**
7. Scenario walkthrough (fish supply chain) + iframe
8. The feel (context / customer / handoff / tone)
9. Voice mode
10. Learning loops
11. Failure modes
12. Closing + links
