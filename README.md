# AI Resource Library

167 links for building and designing with AI coding agents: component registries, design galleries, animation and 3D libraries, agent skills and tools. Each one is tagged by what you do with it, so an agent can pick from the list instead of guessing.

This file is generated from [`library.csv`](skills/resource-library/library.csv). Edit the CSV, not this page.

## Use it as a Claude Code skill

```bash
git clone https://github.com/siddheshsonawane07/ai-resource-library.git
ln -s "$PWD/ai-resource-library/skills/resource-library" ~/.claude/skills/resource-library
```

Then ask Claude Code to improve a site's design, or give it a link to add. [`SKILL.md`](skills/resource-library/SKILL.md) is the procedure it follows.

## Reading the tables

| Use | Meaning |
|---|---|
| `copy-code` | copy components or templates into the project |
| `library` | add as a dependency |
| `reference` | look at it; nothing to install |
| `install-skill` | an agent skill to install |
| `asset` | download and drop in |
| `tool` | a product you use yourself |

Pricing is what the site said on the day the link was added; check before you rely on it. A ★ marks something the maintainer is actually using.

## Contents

- [UI Components](#ui-components) (28)
- [Design Inspiration](#design-inspiration) (32)
- [3D, Animation & Shaders](#3d-animation--shaders) (13)
- [Agent Skills](#agent-skills) (27)
- [AI & Dev Tools](#ai--dev-tools) (20)
- [GitHub Repos](#github-repos) (26)
- [Learning & Articles](#learning--articles) (9)
- [Showcases & Portfolios](#showcases--portfolios) (12)

## UI Components

| Resource | What it is | Use | Pricing | Notes |
|---|---|---|---|---|
| [Aceternity UI](https://ui.aceternity.com) | 200+ animated React and Tailwind components | `copy-code` | freemium | Free components; paid Pro blocks/templates ($169/yr or $199 lifetime) |
| [BoardUI](https://www.boardui.com/) | React + Tailwind v4 design system for dashboards and agent interfaces: 103 components (19 chart cards) plus 10 Pro templates, installed as source you own. Agent parts include a composer with attachments and model menus, streaming task lists, thinking indicators, context meters and web-search trails. Installs via its CLI, an MCP server (stdio can write files; HTTP is read-only), an agent skill or the shadcn registry; every docs page also serves Markdown | `copy-code` | freemium | Free components are MIT on GitHub (BoardUI/boardui). Pro is a one-off payment: €149 for a year of updates, €199 lifetime, €349 for up to 5 developers (prices 2026-11-02). Licence bars redistributing Pro source, public repos of it, and building competing UI kits or templates. Default primary button is a blue gradient |
| [Circle Loaders](https://circleloaders.dominikakissi.com/) | 24 animated monochrome SVG circular loaders, no JS | `copy-code` | free | Copy from cards; licence not stated |
| [Cult UI](https://www.cult-ui.com/) | Open-source shadcn/ui components, animated blocks and templates | `copy-code` | open-source | MIT licence; separate Cult Pro exists |
| [EasyUI](https://easyui.site/) | 131 micro-animated, physics-based React components (React 18/19, TypeScript, Tailwind v3/v4, Framer Motion, some canvas and shaders), installed as source through the official shadcn GitHub registry: npx shadcn@latest add Surajmaurya1/easyui/<name>. Includes charts, data tables, AI chat and agent-activity parts, menus, loaders and animated backgrounds. The repo documents exact design and motion tokens and ships a long design brief for agents | `copy-code` | open-source | MIT (Surajmaurya1/easyui). Spring presets: gentle 280/30/0.8, snappy 400/25/0.5, morph 320/28/0.9, responsive 350/22/0.6 |
| [FeralUI](https://feralui.dev/) | Playful, physics-driven React elements | `copy-code` | free | No pricing or licence stated |
| [Glass components](https://glass.samasante.com) | Headless React lens for Apple-style Liquid Glass on the web | `library` | free | No pricing found on the site |
| [Gradient Buttons](https://gradientbuttons.colorion.co/) | Hundreds of CSS gradient buttons with one-click copy | `copy-code` | free | One-click copy; licence not stated |
| ★ [Kinetics](https://kinetics.colorion.co) | 150+ motion effects with React code and prompts | `copy-code` | free | No paywall; public GitHub repo |
| [Magic UI](https://magicui.design) | 150+ animated components and effects | `copy-code` | open-source | MIT licence |
| [mapcn](https://www.mapcn.dev/) | Customisable React map components on MapLibre GL + Tailwind | `copy-code` | open-source |  |
| ★ [Microkit](https://microkit.co) | Micro-interactions | `copy-code` | open-source | MIT licence |
| [Motion Primitives](https://motion-primitives.com) | Advanced interaction components | `copy-code` | open-source | MIT licence |
| [Nexvyn UI](https://ui.nexvyn.dev/) | Accessible, animated React components (TypeScript + Tailwind) for design engineers | `copy-code` | free | Described as free; no paid tier |
| [Obsidian UI](https://www.obsidianui.dev/) | React + Tailwind components, blocks and landing templates | `copy-code` | open-source | MIT licence |
| [Oversight Supply](https://supply.madebyoversight.com/) | Premium Webflow/Framer templates with AI build prompts | `copy-code` | freemium | 32 free sections after sign-in; membership unlocks the catalogue |
| [PaceUI](https://paceui.com/) | Animated React components, blocks and templates for Next.js and TanStack Start | `copy-code` | freemium | Free: 25+ components, 30+ blocks; Pro $149 one-time |
| [Pin UI](https://pinui.xyz) | Pinterest-inspired React components to copy into projects | `copy-code` | open-source |  |
| [RareUI](https://www.rareui.com/components) | Free, open-source registry of animated React components (shadcn CLI) | `copy-code` | open-source |  |
| [shadcn/ui](https://ui.shadcn.com) | Copy-paste React + Tailwind components; the standard base | `copy-code` | open-source |  |
| [Shadcnblocks](https://shadcnblocks.com) | 2,000+ pre-built section blocks for shadcn/ui | `copy-code` | freemium | Basic blocks free with login; full library one-time from $149 |
| [SmoothUI](https://smoothui.dev) | Animated components built on Motion and GSAP | `copy-code` | open-source | 198 free components |
| [Solace UI](https://www.solaceui.com/) | UI blocks, animated components and page templates for Next.js, Tailwind and Motion | `copy-code` | free | No pricing or licence stated |
| [Spell UI](https://spell.sh/) | React + Tailwind UI component library | `copy-code` | free | No pricing found; public GitHub repo, licence not stated |
| [Toolcraft](https://toolcraft.sh/) | Open-source starter kit and UI library for building design apps with AI | `copy-code` | open-source |  |
| [UIAble](https://uiable.com/) | shadcn-based components, blocks, templates and dashboards | `copy-code` | freemium | Community tier free (MIT); Pro one-time for premium blocks |
| [Uiverse](https://uiverse.io) | Open-source community UI elements | `copy-code` | open-source | MIT licence |
| [useLayouts](https://uselayouts.com/) | Free animated React components built with Framer Motion and Tailwind CSS | `copy-code` | open-source | Free; public GitHub repo, no paid tier |

## Design Inspiration

| Resource | What it is | Use | Pricing | Notes |
|---|---|---|---|---|
| [3dicons](https://3dicons.co) | Open-source 3D icon set | `asset` | free | CC0, free for commercial use |
| [404s Design](https://www.404s.design/) | Curated gallery of creative 404 error pages | `reference` | free | No pricing or paywall |
| [60fps](https://60fps.design/) | Animation and interaction examples from popular iOS and web apps | `reference` | freemium | Free to browse; has a Pro tier |
| [A/B Test Design](https://abtest.design/) | Collection of A/B test results from top apps (by Mobbin) | `reference` | free | Free tool by Mobbin |
| [Animos](https://animos.app/) | Browser tool with 25 motion templates to showcase designs, exports MP4/WebM | `tool` | free | No pricing found on the site |
| [Appshot Gallery](https://www.appshot.gallery/) | Gallery of App Store screenshots for ASO and mobile UI ideas | `reference` | free | Donation link only |
| [Awwwards](https://awwwards.com) | Ranked awards for the best web design | `reference` | freemium | Browsing free; optional Pro membership |
| [Backgrounds Supply](https://www.backgrounds.supply/) | Background designs and assets | `asset` | paid | $49 one-time; has a Freebies page, contents not confirmed |
| [BentoGrids](https://bentogrids.com/) | Curated collection of bento-style grid layouts | `reference` | free | No pricing found |
| [Component Gallery](https://component.gallery) | 2,600+ examples of how design systems build the same component | `reference` | free |  |
| [CTA Gallery](https://cta.gallery) | Conversion-focused forms, popups and buttons | `reference` | free |  |
| [Deck Gallery](https://deck.gallery/) | Pitch deck / presentation design inspiration | `reference` | freemium | Free to browse; optional Pro plan |
| [Footer Design](https://footer.design) | Footer layouts | `reference` | free |  |
| [Godly](https://godly.design/) | Curated gallery of beautiful websites | `reference` | free | godly.website now redirects to recent.design |
| [GoodCart](https://www.goodcart.design/) | Full-page screenshots of live ecommerce sites, desktop and mobile | `reference` | free | Free to browse, no account needed |
| [Hover States](https://hoverstat.es) | Experimental web design projects | `reference` | free |  |
| [Kage](https://kage.design) | Real UI inspiration mapped to prompts | `reference` | free | No pricing; sponsor-supported |
| [Kitbitz](https://kitbitz.art) | 2,000+ hand-drawn illustrations | `asset` | free | CC0, free for commercial use |
| [Land-book](https://land-book.com) | Curated landing pages | `reference` | freemium | Free plan limits categories and search; Pro from $6/month |
| [Landing Love](https://landing.love) | Showcase of the best animated websites | `reference` | free |  |
| [Minimal Gallery](https://minimal.gallery) | Curated high-end minimal websites | `reference` | free | Gallery free; templates sold separately |
| [Mobbin](https://mobbin.com) | Mobile and web app design patterns from real apps | `reference` | freemium | Free plan limited: no flows, search or downloads |
| [Navbar Gallery](https://navbar.gallery) | Navigation patterns | `reference` | free |  |
| [Pricing Pages](https://pricingpages.design) | Best pricing page examples | `reference` | free |  |
| [Pushkeen AI](https://pushkeen.ai/) | Library of iOS push notification examples for re-engagement copy | `reference` | free | No pricing; donation link only |
| [Refero Styles](https://styles.refero.design) | 2,000+ real product styles with typography | `reference` | free | In beta, no paywall |
| [Shoot.Design](https://www.shoot.design/) | Curated App Store screenshots and icons | `reference` | free | No pricing found |
| [Skillry: Opus 5.5 videos](https://skillry.dev/ai-videos/opus-5-5) | Gallery of 418 videos people made with Claude Opus 5.5 as code (229 motion graphics, 68 explainers, 56 3D scenes, 65 games), each shown next to a live remake with the creator's prompt, a link to the original post, and tech tags (Three.js, GLSL, Canvas, SVG, GSAP, Web Audio, WebGPU) | `reference` | freemium | Prompts free to read and copy with no account; no licence stated for them. The site sells agent skills: free ones need sign-in; Pro is $19.90/month, $158/year or $249 lifetime at standard price, with 50 skill loads a day. Payments non-refundable |
| [Supahero](https://supahero.io) | Curated hero sections | `reference` | free | Paid options are only ad placements |
| [Transitions.dev](https://transitions.dev/) | Page/UI transition examples | `reference` | freemium | Some transitions are Pro-only |
| [Unsection](https://www.unsection.com/) | Library of website section designs (heroes, features, footers, pricing) | `reference` | free | Free to join; no paid tier seen (unconfirmed) |
| [What Ships](https://whatships.com) | Directory of 2,000+ startup launch videos from X, a reference source for motion work | `reference` | free | No pricing found |

## 3D, Animation & Shaders

| Resource | What it is | Use | Pricing | Notes |
|---|---|---|---|---|
| [3DAssets.dev](https://3dassets.dev/assets) | Searchable library of free GLB models (22,849 listed) with embedded WebP textures and quantized geometry, loadable from a permanent CDN URL in three.js or imported into Blender, Godot, Unity and Unreal without a Draco or KTX2 decoder. Filter by 13 categories, 11 themes and 6 styles (low poly, voxel, realistic and more). Has a REST API, an MCP endpoint and a skill.md for agents | `asset` | free | All models dedicated CC0 1.0; no attribution, commercial use allowed. Uploads are user-contributed and the uploader carries rights responsibility; provided without warranties. Older submissions under other licences keep their terms. CC0 does not clear trademarks. No account needed to search or download; an API key is needed only to upload |
| [Anime.js](https://animejs.com) | Lightweight JavaScript animation engine | `library` | open-source |  |
| [Meshy](https://www.meshy.ai/) | Hosted text- and image-to-3D with auto-rigging and an animation library, exporting GLB and FBX | `tool` | freemium | Free: 100 credits/month, 10 Meshy 6 Lite downloads, rigging with 20 animations, outputs CC BY 4.0 (credit Meshy). Paid from ₹850/month (over 500 animations; you own outputs) |
| [Motion](https://motion.dev/) | Animation library for React, JavaScript and Vue (formerly Framer Motion) | `library` | open-source | MIT licence; optional one-time Motion+ add-on for premium examples |
| [Quaternius](https://quaternius.com/) | Free low-poly game asset packs (characters, nature, buildings, vehicles, sci-fi) and two Universal Animation Libraries for retargeting onto humanoid rigs | `asset` | free | CC0 (recorded in the Blender standard). An all-in-one download is offered through Patreon |
| [Scenario for Blender](https://blender.scenario.com/) | Blender extension (5.0+) that brings Scenario's generation models into the viewport: generate images, video, 3D models, PBR materials, audio and 360° environments, retexture/remesh/rig existing meshes, and connect local AI agents over an MCP server | `tool` | paid | Add-on code is free (GPL-3.0) but needs a Scenario API key; the Free plan cannot use the API. Paid plans from Starter ($15/month); generation uses that plan's credits |
| [Shadertoy](https://shadertoy.com) | Online shader editor and community | `reference` | free |  |
| [StableGen](https://github.com/sakalond/StableGen) | Blender add-on that textures meshes and scenes with diffusion models and generates meshes from a prompt or image (TRELLIS.2), auto-rigs them (SkinTokens), bakes PBR maps and exports glTF/FBX; runs models on a ComfyUI server | `tool` | open-source | Add-on GPL-3.0. Blender 4.2-4.5 or 5.1+ (not 5.0). SDXL texturing about 8 GB VRAM; Qwen Image 16 GB+ and non-commercial (Qwen Research License); Bria FIBO CC BY-NC. Mesh generation (TRELLIS.2) needs an NVIDIA GPU with 24 GB+ and rigging (SkinTokens) 14 GB+, so not Apple Silicon. 10-50+ GB of models |
| [The Book of Shaders](https://thebookofshaders.com) | Free interactive intro to fragment shaders | `reference` | free |  |
| [Three.js](https://threejs.org) | The most popular web 3D library | `library` | open-source |  |
| [Three.js Fire Pro](https://dgreenheck.github.io/threejs-fire-pro/) | Three.js fire effect demo by Dan Greenheck | `reference` | free |  |
| [Three.js Journey](https://threejs-journey.com) | Full Three.js course including shaders | `reference` | paid | $95 lifetime; only the first lessons are free previews |
| [Tripo](https://www.tripo3d.ai/) | AI tool that generates 3D models from text or images | `tool` | freemium | Free: 200 credits/month (~13 models); Pro from $20/month |

## Agent Skills

| Resource | What it is | Use | Pricing | Notes |
|---|---|---|---|---|
| [adapt (Paul Bakaus)](https://www.ui-skills.com/skills/pbakaus/adapt) | Skill for adapting interfaces across screens and contexts | `install-skill` | open-source | Free; installs from a public GitHub repo via one command |
| [Agent Skills for Context Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | Plugin of 18 skills on building agent systems: context fundamentals, degradation, compression, optimization (compaction, observation masking, KV-cache strategy, partitioning), memory systems, multi-agent patterns, tool design, evaluation and harness engineering | `install-skill` | open-source | MIT. v2.6.0. Install: /plugin marketplace add muratcankoylan/Agent-Skills-for-Context-Engineering then /plugin install context-engineering@context-engineering-marketplace |
| [algorithmic-art (Anthropic)](https://github.com/anthropics/skills/tree/main/skills/algorithmic-art) | Skill for generative art in p5.js: writes an algorithmic philosophy, then builds one self-contained HTML viewer with parameter sliders, color pickers and seed navigation (previous, next, random, jump to seed) | `install-skill` | open-source | Apache-2.0. Loads p5.js 1.7.0 from cdnjs. In Anthropic's example-skills plugin |
| [apple-design (Emil Kowalski)](https://www.ui-skills.com/skills/emilkowalski/apple-design) | Skill for Apple-style interface design | `install-skill` | open-source | Free; installs from a public GitHub repo via one command |
| [beautiful-shadows (Meng To)](https://www.ui-skills.com/skills/mengto/beautiful-shadows) | Three layered Tailwind shadow presets (sm, md, lg) for depth on UI surfaces | `install-skill` | open-source | Free; installs from a public GitHub repo via one command |
| [better-interface (Jakub Krehel)](https://www.ui-skills.com/skills/jakubkrehel/better-interface) | Skill for refining interface details and usability | `install-skill` | open-source | Free; installs from a public GitHub repo via one command |
| [better-ui (Jakub Krehel)](https://www.skills.sh/jakubkrehel/skills/better-ui) | Skill for improving UI quality and detail | `install-skill` | open-source | Free; installs from a public GitHub repo via one command |
| [brag (latent-spaces)](https://github.com/latent-spaces/brag) | Agent skill that turns a finished project into a short shareable launch video in one command | `install-skill` | open-source | MIT licence |
| [canvas-design (Anthropic)](https://github.com/anthropics/skills/tree/main/skills/canvas-design) | Skill for posters and static visuals as .png or .pdf: Claude first writes a named 4-6 paragraph design philosophy, then expresses it on a single canvas with minimal text. Bundles 27 OFL-licensed font families (54 font files) | `install-skill` | open-source | Apache-2.0; fonts under SIL OFL. In Anthropic's example-skills plugin |
| [claude-animation-skill (buildwithhanif)](https://github.com/buildwithhanif/claude-animation-skill) | Claude skill for hand-drawn-style 2D animation in code (Node + ffmpeg) | `install-skill` | open-source | MIT licence |
| [design-review (Superfuture)](https://www.ui-skills.com/skills/superfuture/design-review) | Skill for reviewing and critiquing UI designs | `install-skill` | open-source | Free; installs from a public GitHub repo via one command |
| [emil-design-eng (Emil Kowalski)](https://www.skills.sh/emilkowalski/skills/emil-design-eng) | Skill encoding Emil Kowalski's approach to UI polish, component design and animation decisions | `install-skill` | open-source | Free; installs from a public GitHub repo via one command |
| [file-search (MassGen)](https://github.com/massgen/MassGen/tree/main/massgen/skills/file-search) | Skill teaching an agent to search code with ripgrep for text and ast-grep for syntax-tree patterns, with a narrow-first refinement method for keeping result counts small | `install-skill` | open-source | Skill marked MIT; MassGen repo is Apache-2.0. Written for MassGen's execute_command tool, so the invocation lines need adapting for Claude Code. Needs rg and sg installed |
| [frontend-design (Anthropic)](https://www.ui-skills.com/skills/anthropics/frontend-design) | Anthropic's skill for distinctive, non-generic frontend design | `install-skill` | open-source | Free; installs from a public GitHub repo via one command |
| [gokayfem/video-to-blender](https://github.com/gokayfem/video-to-blender) | Skill (procedural-blender-nodes) that turns a reference video, image or idea into an editable procedural Blender node system: Geometry Nodes, Shader Nodes and compositor graphs built from Python via nodekit, with a tested 39-group node library, templates and validation scripts | `install-skill` | open-source | MIT licence. Needs Blender 5.2+. Installs as a Claude Code plugin, via npx skills, or by copying the skill folder |
| [howseen-ai/claude-motion-design](https://github.com/howseen-ai/claude-motion-design) | Claude Code skill for motion videos as one seek(t) HTML file: beat map, four approved stills, Playwright render, tmix motion blur, pop scan, -14 LUFS audio | `install-skill` | open-source | MIT licence; fetched media keeps its own licences (Mixkit; Pexels; Unsplash) |
| [interaction-design (wshobson)](https://www.ui-skills.com/skills/wshobson/interaction-design) | Skill for interaction and micro-interaction design | `install-skill` | open-source | Free; installs from a public GitHub repo via one command |
| [Marketing Skills (Corey Haines)](https://github.com/coreyhaines31/marketingskills) | 53 marketing skills for coding agents: CRO, copywriting, SEO and AI SEO, paid ads, cold email, pricing, referrals, launch and more, plus marketing-loops for recurring workflows an agent runs on a cadence | `install-skill` | open-source | MIT. v2.14.0. Install: npx skills add coreyhaines31/marketingskills -a claude-code, or /plugin marketplace add coreyhaines31/marketingskills. Funded by disclosed paid partners; tool integrations expect each vendor's API key |
| [Remotion AI skills](https://www.remotion.dev/docs/ai/skills) | Official Remotion skills for making React-based videos with coding agents | `install-skill` | free | Remotion needs a company licence for larger teams; check its licence page for commercial use |
| [shadcn (shadcn-ui)](https://www.ui-skills.com/skills/shadcn-ui/shadcn) | Official skill for building with shadcn/ui components | `install-skill` | open-source | Free; installs from a public GitHub repo via one command |
| [skill-creator (Anthropic)](https://github.com/anthropics/skills/tree/main/skills/skill-creator) | Skill for writing and improving skills: interviews you, drafts SKILL.md, runs test prompts with and without the skill, grades them with grader/comparator/analyzer subagents, shows results in an HTML eval viewer, and tunes the description for triggering | `install-skill` | open-source | Apache-2.0. In Anthropic's example-skills plugin |
| [Superpowers (obra)](https://github.com/obra/superpowers) | Development-methodology plugin of 15 skills that trigger automatically: brainstorming, git worktrees, writing plans, subagent-driven development, red/green TDD, systematic debugging, code review, verification before completion, and finishing a branch. A SessionStart hook injects its using-superpowers skill into every session | `install-skill` | open-source | MIT. v7.0.1. Install: /plugin install superpowers@claude-plugins-official. The brainstorming visual companion loads a logo from the maintainer's site that reports the version in use; turn off with SUPERPOWERS_DISABLE_TELEMETRY |
| [theme-factory (Anthropic)](https://github.com/anthropics/skills/tree/main/skills/theme-factory) | Skill that shows a theme showcase PDF, asks you to pick one of 10 preset color-and-font themes (Ocean Depths, Midnight Galaxy and others), then applies its hex palette and font pairing to a deck, doc or page; can generate a new theme on request | `install-skill` | open-source | Apache-2.0. Ships in Anthropic's example-skills plugin: /plugin marketplace add anthropics/skills, then /plugin install example-skills@anthropic-agent-skills |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Skill backed by a local CSV database queried with a Python BM25 search script: 79 UI styles (50 active), 192 product-type palettes, 74 font pairings, 119 UX guidelines, 25 chart types and guidelines for 22 stacks from React to SwiftUI, Flutter and WPF. A --design-system mode outputs a full token set | `install-skill` | open-source | MIT. v2.15.0. Install: /plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill then /plugin install ui-ux-pro-max@ui-ux-pro-max-skill, or npm i -g ui-ux-pro-max-cli and uipro init --ai claude. Bundles six more skills; the design skill's logo/icon scripts call Gemini, Atlas Cloud or MuAPI with your API key |
| [Unreal Engine Skills for Claude Code](https://github.com/epicgames/unreal-engine-skills-for-claude-code-plugin) | Epic's Claude Code plugin for controlling the running Unreal Editor over its MCP server: an unreal-mcp skill, a SessionStart hook that detects Unreal projects, and safety rules for bulk changes | `install-skill` | open-source | MIT licence. Needs UE 5.8+ with the ModelContextProtocol and AllToolsets plugins and bash on PATH; install with /plugin install unreal-engine-skills-for-claude-code@claude-plugins-official. Includes a tool that runs arbitrary Python in the editor |
| [web-artifacts-builder (Anthropic)](https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder) | Skill with scripts that scaffold a React 18 + TypeScript + Vite + Tailwind 3.4 project with 40+ shadcn/ui components, then bundle it with Parcel into one inlined bundle.html for a claude.ai artifact. Meant for artifacts with state or routing, not simple single-file pages | `install-skill` | open-source | Apache-2.0. Needs Node 18+ and pnpm. In Anthropic's example-skills plugin |
| [webapp-testing (Anthropic)](https://github.com/anthropics/skills/tree/main/skills/webapp-testing) | Skill for testing local web apps with Python Playwright: a with_server.py helper starts one or more dev servers, then Claude screenshots and inspects the rendered DOM before acting (wait for networkidle first) | `install-skill` | open-source | Apache-2.0. Needs Python with Playwright and Chromium. In Anthropic's example-skills plugin |

## AI & Dev Tools

| Resource | What it is | Use | Pricing | Notes |
|---|---|---|---|---|
| [21st.dev](https://21st.dev) | Community React component marketplace that plugs into agents via MCP | `copy-code` | freemium | Browsing free with 2 component copies/day; membership for unlimited |
| [Artcraft apps](https://getartcraft.com/apps) | Seven open-source native creative apps (image, vector, video, photo, PDF, motion, layout) | `tool` | open-source |  |
| [Claude Code](https://claude.com/product/claude-code) | Anthropic's command-line agentic coding tool | `tool` | paid | Only on paid Claude plans |
| [Context7 (Upstash)](https://github.com/upstash/context7) | Service that fetches current, version-specific library docs and code examples into a coding agent, through an MCP server (resolve-library-id, query-docs) or the ctx7 CLI plus a skill. Set up with npx ctx7 setup | `tool` | freemium | MCP server is MIT; the API backend, parser and crawler are private. Free: 1,000 API calls/month then blocked (20 bonus calls/day). Pro $10/seat/month with 2,000 calls and $5 per extra 1,000. Library docs are community-submitted. Needs Node 22.13+ |
| [Cursor](https://cursor.com) | AI-first code editor | `tool` | freemium | Free Hobby tier has limited agent requests; Pro from $20/month |
| [DesignMD](https://designmd.ai) | Design systems written as Markdown that coding agents can read | `copy-code` | free | Site describes its design systems as free |
| [HyperFrames](https://www.hyperframes.dev/) | HeyGen's video-as-code framework (HTML to MP4) and agent video editor | `library` | open-source | HyperFrames framework open-sourced by HeyGen; Studio pricing not stated. X: https://x.com/HyperFrames_ |
| [Jiro](https://jiro.build/) | Library of 1,272+ design prompt templates and components for AI vibe-coding tools | `copy-code` | freemium | Free plan with some templates; Pro is a one-time payment |
| [Koyal](https://koyal.ai) | Agentic AI filmmaking platform | `tool` | freemium | Free: 45-second watermarked videos; Creator $29/month, Pro $79/month |
| [Lovable](https://lovable.dev) | In-browser AI app builder | `tool` | freemium | Credit-based; free credits limited |
| [Plane](https://github.com/makeplane/plane) | Open-source Jira/Linear alternative: work items, cycles (sprints) with burn-down, modules, views, pages and analytics; cloud or self-hosted with Docker or Kubernetes | `tool` | freemium | AGPL-3.0. Cloud Free up to 12 users; Pro $6/user/month annual ($8 monthly), Business $13 ($15); integrations, wiki, time tracking and templates are paid. Prices from plane.so/pricing on 2026-11-02 |
| [Prompt Motion](https://www.prompt-motion.com/) | Gallery of motion videos made with Claude, with the prompts and skills used | `reference` | free | No pricing or paywall found |
| [Remotion](https://www.remotion.dev/) | Make videos programmatically with React: compositions, parameterized rendering, Studio, Player and Lambda | `library` | freemium | Free for individuals and companies of up to 3 people; otherwise a Company License: $25/month per seat (Creators) or $0.01 per render with a $100/month minimum (Automators), per remotion.pro on 2026-11-02 |
| [Scenario](https://www.scenario.com/) | AI platform for generating game and creative assets: image, video, 3D and audio | `tool` | freemium | 50 free daily credits (no API access); paid plans $15-$75/month (Starter/Pro/Max); annual billing saves 33% |
| [Scrolltide](https://scrolltide.co) | Library of 300+ complete website prompts with source code, for Claude Code, Cursor or v0 | `copy-code` | freemium | Free templates section; most templates premium ($299 lifetime) |
| [Slopforge](https://solarfren69420.github.io/Slopforge/?platform=macOS) | Web directory of community game engines, source ports, open-source games, creative software and compatibility tools, filterable by platform (this link filters to macOS). Every card links to the upstream repo; it hosts no game files | `reference` | open-source | Directory source is MIT on GitHub (solarfren69420/Slopforge); each listed project has its own licence. Submissions via GitHub issues. Sister site: Game Decomp Library |
| [Tapetide MCP](https://tapetide.com/mcp) | MCP server giving AI apps data on ~8,200 NSE/BSE stocks | `tool` | freemium | Free: 50 tool calls/day, 1,000/month; paid for more |
| [v0](https://v0.dev) | Vercel's prompt-to-UI/component generator | `tool` | freemium | Free tier capped at 7 messages/day; Plus $30/month |
| [VibePrompts](https://vibeprompts.dev) | Ready-made prompts for dashboards and landing pages | `reference` | free | All 286 prompts browsable, no paywall seen |
| [Viktor](https://viktor.com) | AI employee in Slack/Teams that researches leads and drafts offers | `tool` | freemium | Start free, no card; paid plans |

## GitHub Repos

| Resource | What it is | Use | Pricing | Notes |
|---|---|---|---|---|
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | Agent harness setup for Claude Code, Codex, Opencode and Cursor: skills, memory, security and research-first development | `reference` | open-source | MIT licence |
| [Appllama/appllama-skills](https://github.com/Appllama/appllama-skills) | Two skills for building mobile apps. appllama-app-design-skill: native-quality Expo/React Native screens with Apple HIG fidelity, semantic colours, native controls, navigation rules, an anti-slop pre-flight count (one accent, one radius scale, no emoji chrome), motion laws and an iOS Simulator loop that records whole flows. appllama-usage: drives the Appllama MCP to study screens and flows from 1,800+ top-grossing apps before building | `install-skill` | freemium | Skills are MIT and the design skill works without the MCP. The MCP (mcp.appllama.io) needs Pro: $10/month (₹1,299 in India), 1,500 credits a month, one per call; the free plan has no MCP. Install: npx skills@latest add appllama/appllama-skills (add --skill appllama-app-design-skill for just that one). Simulator loop needs Xcode |
| [arielshad/3d-asset-server](https://github.com/arielshad/3d-asset-server) | API and MCP server for 3D assets | `tool` | open-source | Apache-2.0 licence |
| [athemeroy/awesome-opus-5-5-videos](https://github.com/athemeroy/awesome-opus-5-5-videos) | Dataset of Opus 5.5 motion videos | `reference` | open-source |  |
| [Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp) | MCP server that lets an agent launch the Godot editor, run projects and capture debug output | `tool` | open-source | MIT, 6.5k stars |
| [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | Open-source AI coworkers that each get their own computer (browser, files, tools); works with any AG-UI agent | `reference` | open-source | MIT licence |
| [emilkowalski/skills](https://github.com/emilkowalski/skills) | Agent skills for designers and engineers, from Emil Kowalski | `install-skill` | open-source | MIT licence |
| [google/ax](https://github.com/google/ax) | Google's open agentic orchestration runtime | `library` | open-source | Apache-2.0 licence |
| [guanmo-ai/awesome-ai-motion](https://github.com/guanmo-ai/awesome-ai-motion) | Catalogue of 32 AI motion/video cases with authors, source posts and prompts | `reference` | open-source |  |
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | HyperFrames framework repo: HTML + GSAP video rendering for agents | `library` | open-source |  |
| [hi3d-official/Hi3Dv1.0](https://github.com/hi3d-official/Hi3Dv1.0) | Open-weights Hi3D v1.0 (Sparc3D line): refines a coarse mesh into detailed geometry at up to 1536 resolution, guided by a reference image; geometry only, no textures | `tool` | open-source | Hi3D Open License 1.0 (custom, not OSI): commercial use allowed with a 'Powered by Hi3D 1.0' credit; separate licence needed above 200k MAU or $1M monthly revenue. Linux + NVIDIA (compute 8.0+, CUDA 12.0-12.5) only; 1536 validated only on a 96 GB H20. Online demo: https://huggingface.co/spaces/ilcve21/Sparc3D |
| [hoodini/motion-in-code](https://github.com/hoodini/motion-in-code) | Motion in Code kit: closed-form spring engine, 24 building blocks with prompts, a prompt template, three films and a QA pop detector | `reference` | open-source | Public repo but no licence file found; credits the method to @twoclipping |
| [JohnHeibel/ClaudeAnimationBase](https://github.com/JohnHeibel/ClaudeAnimationBase) | Starter kit for hand-painted cartoon animation with Claude (p5.js, p5.brush) | `copy-code` | open-source | MIT licence |
| [JohnHeibel/PDoomVideo](https://github.com/JohnHeibel/PDoomVideo) | Code-rendered music video made with Opus, showing the parallel-subagent pattern | `reference` | open-source |  |
| [kargulstudio/kanban](https://github.com/kargulstudio/kanban) | Kanban board project | `reference` | open-source | No licence stated |
| [kargulstudio/sales-crm](https://github.com/kargulstudio/sales-crm) | Sales CRM project | `reference` | open-source | MIT licence |
| [Leonxlnx/athenaion](https://github.com/Leonxlnx/athenaion) | Ancient Greek world built entirely in code with three.js r186 and no external assets (terrain, temple, SDF-sculpted statues, 57 waterfalls, 149k trees, volumetric clouds, offline accumulation renderer). Claude Code with Opus 5.5 built it in about 45 hours with 55 subagents to match 9 reference images. Ships the session prompt, art bible, module contract, composition plan and colour-statistics tools | `reference` | open-source | MIT. About 45k lines of JS. Render tools are Windows-only as committed (Chrome under C:/Program Files, ANGLE d3d11, taskkill): on macOS add the Chrome path, set ANGLE=metal and swap taskkill for kill. Needs ffmpeg. Showcase music (CC BY 4.0) not included. The author reports about $1.8k-2.3k API-equivalent cost |
| [luki-1/ArkWeb](https://github.com/luki-1/ArkWeb) | Experimental mod bringing Spider-Man Remastered's web swinging to Batman: Arkham Knight | `reference` | open-source | No licence stated |
| [Meituan LongCat (org)](https://github.com/meituan-longcat) | Meituan's LongCat open-model organisation | `reference` | open-source |  |
| [OpenCut](https://github.com/OpenCut-app/OpenCut) | Free, open-source video editor for web, desktop and mobile (a CapCut alternative), 97k stars. Being rewritten from scratch around a Rust core, with an editor API, plugins, a headless mode for batch rendering, an MCP server for agents and a scripting tab planned | `reference` | open-source | MIT. Mid-rewrite as of 2026-09: the usable version today is opencut-app/opencut-classic (and opencut.app). Not taking outside contributions yet. Sponsored by fal.ai |
| [PixelSRPG-Forge](https://github.com/Huu-Yuu/PixelSRPG-Forge) | Collection of pixel art for tactics RPGs in about 118 MB: zipped packs of characters, monsters, dungeon and city tiles, interiors, UI icons, skill icons and weapons, plus a 33,000-file small-icon archive, and png_icon_packer.py (Python + Pillow) for merging PNGs into a sprite sheet with an index file. Aimed at SRPG Studio, Godot, Unity, GameMaker and RPG Maker | `asset` | free | MIT covers only the repo's organisation, not the art. The README says assets were gathered from internet downloads and commercial purchases with unknown copyright status, and commercial use is at your own risk. Two packs are labelled MapleStory. None of the 10 zips includes a licence or credit file. Several folders the README lists (sound effects, skill effects, costumes, examples) are not in the repo. Prototyping and reference only |
| [PlayCanvas (org)](https://github.com/playcanvas) | Open-source WebGL/WebGPU 3D game engine and editor | `library` | open-source |  |
| [Tencent-Hunyuan/HY-Motion-1.0](https://github.com/Tencent-Hunyuan/HY-Motion-1.0) | Text-to-3D human motion: generates skeleton-based character animation from a text description (1.0B model, plus a 0.46B Lite version) | `tool` | free | Tencent community licence: not valid in the EU, UK or South Korea; over 1M monthly users needs a licence; distributions carry a notice. Needs 24-26 GB of GPU memory |
| [VAST-AI-Research/UniRig](https://github.com/VAST-AI-Research/UniRig) | SIGGRAPH 2025 research model that predicts a skeleton and skinning for almost any 3D mesh, not only humanoids | `tool` | open-source | MIT. Needs a capable NVIDIA GPU to run locally |
| [WinterArc21/Battle-of-Austerlitz-Film](https://github.com/WinterArc21/Battle-of-Austerlitz-Film) | Long-form history film rendered entirely from code | `reference` | open-source |  |
| [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos) | Companion list to the Skillry gallery: 703 prompts as Markdown files in prompts/ plus data/videos.json, 100 highlighted videos by category, and links to every creator's original post. Many prompts are one-liners; some are partial, and those files say so | `reference` | free | MIT covers the list; the README says every video and prompt belongs to its creator. Last pushed 2026-10-13 |

## Learning & Articles

| Resource | What it is | Use | Pricing | Notes |
|---|---|---|---|---|
| [Co-Creating Code (FITT IIT Delhi)](https://www.youtube.com/live/xLl9V6pdEgg) | Livestream from FITT IIT Delhi; content not summarised | `reference` | free |  |
| [Connection reuse and request routing](https://www.bhupeshkumar.blog/blogs/how-connection-reuse-can-quietly-decide-where-requests-go) | Blog post on how HTTP connection reuse affects load balancing | `reference` | free |  |
| [Deep-ML](https://www.deep-ml.com/) | ML/deep learning coding practice problems | `reference` | free | Site says all problems are free |
| [Game Dev Cheat Sheet](https://gamedev-cheatsheet.com/) | 34 game-development concepts, each with an interactive animation, a plain explanation and a copyable prompt bit for AI coding agents, in four chapters: 3D and rendering (raycasting, LOD, frustum culling, quaternions, z-fighting), game feel (coyote time, easing, screen shake, hit-stop, input buffering), systems (object pooling, state machines, pathfinding, fixed timestep, seeded noise) and performance (frame budget, draw calls, overdraw, texture atlases, chunk streaming). Detail pages add when to use it, engine-neutral pseudocode and common mistakes | `reference` | free | Maintained by Nicolas Zullo. Free, no account; an optional newsletter stores your email. No licence stated, so link rather than copy |
| [Motion in Code (YUV.AI)](https://yuv.ai/motion) | Deep dive on the seek(t) to Playwright to ffmpeg launch-video method: closed-form springs, beat sync, motion blur and QA | `reference` | free |  |
| [Roblox Studio MCP server (docs)](https://create.roblox.com/docs/studio/mcp) | Roblox's guide to the MCP server built into Roblox Studio: enabling it, Quick connect for Claude Code and other clients, and its 26 tools for scripts, mesh and procedural-model generation, Luau execution, playtesting with simulated input, and a playtest subagent | `reference` | free | Studio is free. Roblox warns that connected clients can read and modify your open places. Tool count was 26 on 2026-11-02 |
| [Snyk ToxicSkills study](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub) | Snyk's scan of 3,984 agent skills from ClawHub and skills.sh: 534 (13.4%) had a critical issue, 1,467 (36.82%) had any issue, and 76 confirmed malicious payloads did credential theft, backdoors and data exfiltration | `reference` | free | Published 2026-02-05 |
| [Unreal Engine MCP Hands-On (Puget Systems)](https://www.pugetsystems.com/blog/2026/07/09/unreal-engine-mcp-hands-on-testing-ai-inside-the-editor/) | Hands-on test of Claude driving UE 5.8 through MCP: a greybox level and a room-lighting Blueprint worked, while a controls change and a procedural PCG city failed | `reference` | free | Tested with Opus 4.8 in July 2026 |
| [Unreal MCP in Unreal Editor (Epic docs)](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-mcp-in-unreal-editor) | Epic's guide to UE 5.8's experimental MCP server: enabling Unreal MCP and All Toolsets, starting the server, generating .mcp.json for Claude Code and other clients, serial tool calls and security | `reference` | free | Experimental; no authentication and loopback-only |

## Showcases & Portfolios

| Resource | What it is | Use | Pricing | Notes |
|---|---|---|---|---|
| [Attack on Titancraft](https://attack-on-titancraft.netlify.app/) | Browser game demo | `reference` | free |  |
| [Gulabi Nagar Jaipur](https://gulabi-nagar-jaipur.vercel.app/) | Jaipur-themed demo site | `reference` | free |  |
| [Gulmohar Local](https://gulmohar-local.pages.dev/) | Demo/local business site | `reference` | free |  |
| [Koi Pond Garden](https://souranyp-stack.github.io/koi-pond-garden/koi-pond.html) | Interactive koi pond web experiment | `reference` | free |  |
| [Navya Bijoy home](https://home.navyabijoy.tech/) | Personal portfolio site | `reference` | free |  |
| [Shardul Studio](https://shardul.studio/) | Designer/studio portfolio | `reference` | free |  |
| [Soccar](https://soccar-one.vercel.app/) | Browser car-soccer game demo | `reference` | free |  |
| [Spider-Verse demo](https://spiderman-spiderverse.vercel.app/) | Fan-made Spider-Verse styled web demo | `reference` | free |  |
| [Valley (Meng To)](https://valley.mengto.here.now/) | Demo site by Meng To | `reference` | free |  |
| [WASM Arcade](https://wasmarcade.com/) | Arcade of WebAssembly browser games | `reference` | free |  |
| [Wildbrush](https://wildbrush.vercel.app/) | Demo site | `reference` | free |  |
| [Yoshik PC](https://yoshik-pc.vercel.app/) | Personal portfolio site | `reference` | free |  |

## Maintaining

Add or change a row in `library.csv`, then run `python3 scripts/build.py`. It checks the row and rewrites this page. `--check` fails if this page is stale, and `--links` reports URLs that no longer respond.
