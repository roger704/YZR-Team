# Tap to Trust design materials and presentation

Reviewed against source `d628c69a054fd248d3b32efca8f275bdc00509c7` on 2026-09-17. This guide describes tracked implementation and does not assert live deployment state.

## Purpose and architecture

Design challenge, sample scenarios, diagrams and a Slidev deck under `presentation/`. The interactive mock-up is the separate `hands-free-help` repository; an iframe does not make that code part of this repository.

## Setup and development

Run `npm ci` then `npm run dev` inside `presentation/`. Inspect `presentation/package.json` for deck scripts. Source scenarios and diagrams live at the repository root.

## Verification

Build the deck using the same base path as CI: `npx slidev build --base /YZR-Team/ --out dist`. Verify slide navigation and embedded prototype loading in a browser.

## Deployment and operations

`.github/workflows/deploy.yml` builds `presentation/dist`, copies index to 404 for SPA fallback, and deploys with the `deploy` job to the `github-pages` environment. Source changes outside the presentation path do not automatically trigger that deployment.

Every actual deployment needs a distinct record under [changelogs](../changelogs/README.md), including exact revision/artifact, environment, outcome and operational notes. A source merge or successful build is not deployment evidence.

## Interfaces and further reading

No repository-owned HTTP API. `sample-data.json` is design fixture data, not a live approval service.
