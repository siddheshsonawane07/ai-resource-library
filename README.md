# AI Resource Library

129 links for building and designing with AI coding agents: component registries, design galleries, animation and 3D libraries, agent skills and tools. Each one is tagged by what you do with it, so an agent can pick from the list instead of guessing.

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

- [UI Components](#ui-components) (27)
- [Design Inspiration](#design-inspiration) (31)
- [3D, Animation & Shaders](#3d-animation--shaders) (8)
- [Agent Skills](#agent-skills) (13)
- [AI & Dev Tools](#ai--dev-tools) (17)
- [GitHub Repos](#github-repos) (18)
- [Learning & Articles](#learning--articles) (3)
- [Showcases & Portfolios](#showcases--portfolios) (12)

## UI Components

| Resource | What it is | Use | Pricing | Notes |
|---|---|---|---|---|
| [Aceternity UI](https://ui.aceternity.com) | 200+ animated React and Tailwind components | `copy-code` | freemium | Free components; paid Pro blocks/templates ($169/yr or $199 lifetime) |
| [Circle Loaders](https://circleloaders.dominikakissi.com/) | 24 animated monochrome SVG circular loaders, no JS | `copy-code` | free | Copy from cards; licence not stated |
| [Cult UI](https://www.cult-ui.com/) | Open-source shadcn/ui components, animated blocks and templates | `copy-code` | open-source | MIT licence; separate Cult Pro exists |
| [EasyUI](https://easyui.site/) | Animated React components with Tailwind and Framer Motion | `copy-code` | open-source |  |
| [FeralUI](https://feralui.dev/) | Playful, physics-driven React elements | `copy-code` | free | No pricing or licence stated |
| [Glass components](https://glass.samasante.com) | Headless React lens for Apple-style Liquid Glass on the web | `library` | free | No pricing found on the site |
| [Gradient Buttons](https://gradientbuttons.colorion.co/) | Hundreds of CSS gradient buttons with one-click copy | `copy-code` | free | One-click copy; licence not stated |
| [Kinetics](https://kinetics.colorion.co) | 150+ motion effects with React code and prompts | `copy-code` | free | No paywall; public GitHub repo |
| [Magic UI](https://magicui.design) | 150+ animated components and effects | `copy-code` | open-source | MIT licence |
| [mapcn](https://www.mapcn.dev/) | Customisable React map components on MapLibre GL + Tailwind | `copy-code` | open-source |  |
| [Microkit](https://microkit.co) | Micro-interactions | `copy-code` | open-source | MIT licence |
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
| [Supahero](https://supahero.io) | Curated hero sections | `reference` | free | Paid options are only ad placements |
| [Transitions.dev](https://transitions.dev/) | Page/UI transition examples | `reference` | freemium | Some transitions are Pro-only |
| [Unsection](https://www.unsection.com/) | Library of website section designs (heroes, features, footers, pricing) | `reference` | free | Free to join; no paid tier seen (unconfirmed) |
| [What Ships](https://whatships.com) | Directory of 2,000+ startup launch videos from X, a reference source for motion work | `reference` | free | No pricing found |

## 3D, Animation & Shaders

| Resource | What it is | Use | Pricing | Notes |
|---|---|---|---|---|
| [Anime.js](https://animejs.com) | Lightweight JavaScript animation engine | `library` | open-source |  |
| [Motion](https://motion.dev/) | Animation library for React, JavaScript and Vue (formerly Framer Motion) | `library` | open-source | MIT licence; optional one-time Motion+ add-on for premium examples |
| [Shadertoy](https://shadertoy.com) | Online shader editor and community | `reference` | free |  |
| [The Book of Shaders](https://thebookofshaders.com) | Free interactive intro to fragment shaders | `reference` | free |  |
| [Three.js](https://threejs.org) | The most popular web 3D library | `library` | open-source |  |
| [Three.js Fire Pro](https://dgreenheck.github.io/threejs-fire-pro/) | Three.js fire effect demo by Dan Greenheck | `reference` | free |  |
| [Three.js Journey](https://threejs-journey.com) | Full Three.js course including shaders | `reference` | paid | $95 lifetime; only the first lessons are free previews |
| [Tripo](https://www.tripo3d.ai/) | AI tool that generates 3D models from text or images | `tool` | freemium | Free: 200 credits/month (~13 models); Pro from $20/month |

## Agent Skills

| Resource | What it is | Use | Pricing | Notes |
|---|---|---|---|---|
| [adapt (Paul Bakaus)](https://www.ui-skills.com/skills/pbakaus/adapt) | Skill for adapting interfaces across screens and contexts | `install-skill` | open-source | Free; installs from a public GitHub repo via one command |
| [apple-design (Emil Kowalski)](https://www.ui-skills.com/skills/emilkowalski/apple-design) | Skill for Apple-style interface design | `install-skill` | open-source | Free; installs from a public GitHub repo via one command |
| [beautiful-shadows (Meng To)](https://www.ui-skills.com/skills/mengto/beautiful-shadows) | Three layered Tailwind shadow presets (sm, md, lg) for depth on UI surfaces | `install-skill` | open-source | Free; installs from a public GitHub repo via one command |
| [better-interface (Jakub Krehel)](https://www.ui-skills.com/skills/jakubkrehel/better-interface) | Skill for refining interface details and usability | `install-skill` | open-source | Free; installs from a public GitHub repo via one command |
| [better-ui (Jakub Krehel)](https://www.skills.sh/jakubkrehel/skills/better-ui) | Skill for improving UI quality and detail | `install-skill` | open-source | Free; installs from a public GitHub repo via one command |
| [brag (latent-spaces)](https://github.com/latent-spaces/brag) | Agent skill that turns a finished project into a short shareable launch video in one command | `install-skill` | open-source | MIT licence |
| [claude-animation-skill (buildwithhanif)](https://github.com/buildwithhanif/claude-animation-skill) | Claude skill for hand-drawn-style 2D animation in code (Node + ffmpeg) | `install-skill` | open-source | MIT licence |
| [design-review (Superfuture)](https://www.ui-skills.com/skills/superfuture/design-review) | Skill for reviewing and critiquing UI designs | `install-skill` | open-source | Free; installs from a public GitHub repo via one command |
| [emil-design-eng (Emil Kowalski)](https://www.skills.sh/emilkowalski/skills/emil-design-eng) | Skill encoding Emil Kowalski's approach to UI polish, component design and animation decisions | `install-skill` | open-source | Free; installs from a public GitHub repo via one command |
| [frontend-design (Anthropic)](https://www.ui-skills.com/skills/anthropics/frontend-design) | Anthropic's skill for distinctive, non-generic frontend design | `install-skill` | open-source | Free; installs from a public GitHub repo via one command |
| [interaction-design (wshobson)](https://www.ui-skills.com/skills/wshobson/interaction-design) | Skill for interaction and micro-interaction design | `install-skill` | open-source | Free; installs from a public GitHub repo via one command |
| [Remotion AI skills](https://www.remotion.dev/docs/ai/skills) | Official Remotion skills for making React-based videos with coding agents | `install-skill` | free | Remotion needs a company licence for larger teams; check its licence page for commercial use |
| [shadcn (shadcn-ui)](https://www.ui-skills.com/skills/shadcn-ui/shadcn) | Official skill for building with shadcn/ui components | `install-skill` | open-source | Free; installs from a public GitHub repo via one command |

## AI & Dev Tools

| Resource | What it is | Use | Pricing | Notes |
|---|---|---|---|---|
| [21st.dev](https://21st.dev) | Community React component marketplace that plugs into agents via MCP | `copy-code` | freemium | Browsing free with 2 component copies/day; membership for unlimited |
| [Artcraft apps](https://getartcraft.com/apps) | Seven open-source native creative apps (image, vector, video, photo, PDF, motion, layout) | `tool` | open-source |  |
| [Claude Code](https://claude.com/product/claude-code) | Anthropic's command-line agentic coding tool | `tool` | paid | Only on paid Claude plans |
| [Cursor](https://cursor.com) | AI-first code editor | `tool` | freemium | Free Hobby tier has limited agent requests; Pro from $20/month |
| [DesignMD](https://designmd.ai) | Design systems written as Markdown that coding agents can read | `copy-code` | free | Site describes its design systems as free |
| [HyperFrames](https://www.hyperframes.dev/) | HeyGen's video-as-code framework (HTML to MP4) and agent video editor | `library` | open-source | HyperFrames framework open-sourced by HeyGen; Studio pricing not stated. X: https://x.com/HyperFrames_ |
| [Jiro](https://jiro.build/) | Library of 1,272+ design prompt templates and components for AI vibe-coding tools | `copy-code` | freemium | Free plan with some templates; Pro is a one-time payment |
| [Koyal](https://koyal.ai) | Agentic AI filmmaking platform | `tool` | freemium | Free: 45-second watermarked videos; Creator $29/month, Pro $79/month |
| [Lovable](https://lovable.dev) | In-browser AI app builder | `tool` | freemium | Credit-based; free credits limited |
| [Prompt Motion](https://www.prompt-motion.com/) | Gallery of motion videos made with Claude, with the prompts and skills used | `reference` | free | No pricing or paywall found |
| [Scenario](https://www.scenario.com/) | AI platform for generating game and creative assets: image, video, 3D and audio | `tool` | freemium | 50 free daily credits; paid plans $10-$50/month |
| [Scrolltide](https://scrolltide.co) | Library of 300+ complete website prompts with source code, for Claude Code, Cursor or v0 | `copy-code` | freemium | Free templates section; most templates premium ($299 lifetime) |
| [Slopforge](https://solarfren69420.github.io/Slopforge/?platform=macOS) | Community directory of game revivals, open-source tools and compatibility layers | `reference` | open-source | Source on GitHub; listed projects have their own licences |
| [Tapetide MCP](https://tapetide.com/mcp) | MCP server giving AI apps data on ~8,200 NSE/BSE stocks | `tool` | freemium | Free: 50 tool calls/day, 1,000/month; paid for more |
| [v0](https://v0.dev) | Vercel's prompt-to-UI/component generator | `tool` | freemium | Free tier capped at 7 messages/day; Plus $30/month |
| [VibePrompts](https://vibeprompts.dev) | Ready-made prompts for dashboards and landing pages | `reference` | free | All 286 prompts browsable, no paywall seen |
| [Viktor](https://viktor.com) | AI employee in Slack/Teams that researches leads and drafts offers | `tool` | freemium | Start free, no card; paid plans |

## GitHub Repos

| Resource | What it is | Use | Pricing | Notes |
|---|---|---|---|---|
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | Agent harness setup for Claude Code, Codex, Opencode and Cursor: skills, memory, security and research-first development | `reference` | open-source | MIT licence |
| [Appllama/appllama-skills](https://github.com/Appllama/appllama-skills) | Agent skills that turn top-grossing app patterns into native-quality mobile screens | `install-skill` | open-source | MIT licence |
| [arielshad/3d-asset-server](https://github.com/arielshad/3d-asset-server) | API and MCP server for 3D assets | `tool` | open-source | Apache-2.0 licence |
| [athemeroy/awesome-opus-5-5-videos](https://github.com/athemeroy/awesome-opus-5-5-videos) | Dataset of Opus 5.5 motion videos | `reference` | open-source |  |
| [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | Open-source AI coworkers that each get their own computer (browser, files, tools); works with any AG-UI agent | `reference` | open-source | MIT licence |
| [emilkowalski/skills](https://github.com/emilkowalski/skills) | Agent skills for designers and engineers, from Emil Kowalski | `install-skill` | open-source | MIT licence |
| [google/ax](https://github.com/google/ax) | Google's open agentic orchestration runtime | `library` | open-source | Apache-2.0 licence |
| [guanmo-ai/awesome-ai-motion](https://github.com/guanmo-ai/awesome-ai-motion) | Catalogue of 32 AI motion/video cases with authors, source posts and prompts | `reference` | open-source |  |
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | HyperFrames framework repo: HTML + GSAP video rendering for agents | `library` | open-source |  |
| [JohnHeibel/ClaudeAnimationBase](https://github.com/JohnHeibel/ClaudeAnimationBase) | Starter kit for hand-painted cartoon animation with Claude (p5.js, p5.brush) | `copy-code` | open-source | MIT licence |
| [JohnHeibel/PDoomVideo](https://github.com/JohnHeibel/PDoomVideo) | Code-rendered music video made with Opus, showing the parallel-subagent pattern | `reference` | open-source |  |
| [kargulstudio/kanban](https://github.com/kargulstudio/kanban) | Kanban board project | `reference` | open-source | No licence stated |
| [kargulstudio/sales-crm](https://github.com/kargulstudio/sales-crm) | Sales CRM project | `reference` | open-source | MIT licence |
| [luki-1/ArkWeb](https://github.com/luki-1/ArkWeb) | Experimental mod bringing Spider-Man Remastered's web swinging to Batman: Arkham Knight | `reference` | open-source | No licence stated |
| [Meituan LongCat (org)](https://github.com/meituan-longcat) | Meituan's LongCat open-model organisation | `reference` | open-source |  |
| [OpenCut](https://github.com/OpenCut-app/OpenCut) | Open-source video editor (CapCut alternative) | `reference` | open-source |  |
| [PlayCanvas (org)](https://github.com/playcanvas) | Open-source WebGL/WebGPU 3D game engine and editor | `library` | open-source |  |
| [WinterArc21/Battle-of-Austerlitz-Film](https://github.com/WinterArc21/Battle-of-Austerlitz-Film) | Long-form history film rendered entirely from code | `reference` | open-source |  |

## Learning & Articles

| Resource | What it is | Use | Pricing | Notes |
|---|---|---|---|---|
| [Co-Creating Code (FITT IIT Delhi)](https://www.youtube.com/live/xLl9V6pdEgg) | Livestream from FITT IIT Delhi; content not summarised | `reference` | free |  |
| [Connection reuse and request routing](https://www.bhupeshkumar.blog/blogs/how-connection-reuse-can-quietly-decide-where-requests-go) | Blog post on how HTTP connection reuse affects load balancing | `reference` | free |  |
| [Deep-ML](https://www.deep-ml.com/) | ML/deep learning coding practice problems | `reference` | free | Site says all problems are free |

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
