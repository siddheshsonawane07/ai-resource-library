---
name: resource-library
description: A curated library of UI component registries, design-inspiration galleries, animation and 3D libraries, agent skills and AI tools, with a procedure for choosing from it. Use when asked to improve, redesign or polish a website or app UI, to add animation, 3D or a specific section (hero, navbar, pricing, footer, loaders), or to find a component or a design reference. Also use when the user gives a link to add to the library, or asks to recategorise or update an entry.
---

# Resource library

`library.csv`, next to this file, holds one row per link. It is the only copy of the data; the repo's `README.md` is generated from it.

| Column | Holds |
|---|---|
| `name`, `url`, `description` | What it is, in the site's own terms |
| `category` | One of the eight sections listed under "Allowed values" |
| `use` | What you do with it (see step 4) |
| `stack` | Space-separated tech tags it needs: `react tailwind shadcn motion three` and so on. Empty means it does not depend on a stack |
| `good_for` | Space-separated tags for what it helps with: `hero navbar pricing loaders animation` and so on |
| `pricing` | `open-source`, `free`, `freemium`, `paid` or `unverified`. `notes` says where the free tier ends |
| `status` | The maintainer's verdict: `not-started`, `exploring`, `using`, `bookmarked`, `not-useful` |
| `added` | Date the row was added, `YYYY-MM-DD` |

## Using it for design work

1. **Read the project before the library.** Find the framework, the styling approach and any component library already installed (`package.json`, `components.json`, the existing components). A resource whose `stack` the project does not have is out, however good it looks.

2. **Filter the file; do not read all of it.** Most rows are irrelevant to any one task. Grep for the category or the tag you need, and keep the header so the columns stay readable:

   ```bash
   head -1 library.csv; grep -E "UI Components|3D, Animation & Shaders" library.csv
   head -1 library.csv; grep -iE "hero|landing" library.csv
   ```

   For design work the relevant categories are UI Components, Design Inspiration, 3D, Animation & Shaders, and Agent Skills. The other four hold tools, repos, articles and showcases that rarely apply.

3. **Rank what is left.** Prefer `using`, then `exploring`, then `not-started`; never pick `not-useful`. Prefer `open-source` and `free`. For `freemium`, read `notes` first, because some free tiers stop at a couple of copies a day. Use `paid` only when the user asks for it.

4. **Act according to `use`.**

   | `use` | What to do |
   |---|---|
   | `copy-code` | Open the resource's own docs for the install command or the component source. Do not guess a CLI command from the name. |
   | `library` | Add it as a dependency, unless the project already has something that does the same job. |
   | `reference` | It only helps if you look at it. Open it with a browser or fetch tool; if you cannot, offer it to the user as a place to pick a direction from. Never say a design follows a gallery you did not open. |
   | `install-skill` | Do not install it mid-task. A skill is a set of instructions you would then follow, so name it to the user and read its `SKILL.md` before anything is installed. |
   | `asset` | Download and place it, after checking the licence in `notes`. |
   | `tool` | The user runs it themselves. Mention it if it fits; there is nothing to implement. |

5. **Say what you chose, then build.** Shortlist two or three, state which you are using and why in a line each, and implement. Check with the user before adding a new dependency or registry to their project.

6. **Record the verdict.** After a resource has been used, set its `status` to `using` or `exploring`; if it turned out badly, set `not-useful` and say why in `notes`. Every row started as `not-started`, so these verdicts are what make the next choice better. Then regenerate the README (below).

## Adding a link

1. **Check it is not already there.** Grep `library.csv` for the domain.
2. **Fetch the page and describe what it says.** Write the description from the page, not from the URL or the name. If the page cannot be fetched, or does not say what the thing is, tell the user and leave it out; a guessed description is worse than a missing row.
3. **Fill every column.** Pick the category by what the thing is and `use` by what someone does with it. Look for a pricing or licence page and record where the free tier ends in `notes`. Set `status` to `not-started` unless the user says otherwise, and `added` to today.
4. **Keep it publishable.** This file is public. Leave out where the link came from, why the user personally wants it, and anything resembling a key or token.
5. **Append the row** with correct CSV quoting (a field containing a comma goes in double quotes), then regenerate.

## Regenerating the README

This skill normally lives inside its repo at `skills/resource-library/`. Resolve the real path of this directory (it may be reached through a symlink); the repo root is two levels up. If `scripts/build.py` exists there, run it:

```bash
python3 "$(realpath <this directory>)/../../scripts/build.py"
```

It validates every row (allowed values, duplicates, dates) and rewrites `README.md`. Fix whatever it reports. Do not edit `README.md` by hand, and do not commit or push unless the user asks.

## Allowed values

- `category`: UI Components · Design Inspiration · 3D, Animation & Shaders · Agent Skills · AI & Dev Tools · GitHub Repos · Learning & Articles · Showcases & Portfolios
- `use`: copy-code · library · reference · install-skill · asset · tool
- `pricing`: open-source · free · freemium · paid · unverified
- `status`: not-started · exploring · using · bookmarked · not-useful

A new value in any of these is a change to `scripts/build.py` as well, which holds the same lists and rejects anything else.
