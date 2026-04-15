# Prompt Library Plugin

A Claude Code plugin containing **226 context-engineered persona skills** built from PromptLibrary 3.0. Each skill carries full cognitive scaffolding -- Self-Refine loops, Quality Dimensions scoring, Chain-of-Thought reasoning, Few-Shot Examples, and domain-specific constraints -- so the AI behaves as a deeply specialized expert the moment you invoke it.

## Installation

```bash
# Add the marketplace (one-time setup)
claude plugin marketplace add /path/to/EngineeredPromptLibrrary

# Install the plugin
claude plugin install prompt-library@prompt-library-marketplace
```

Restart Claude Code after installation.

## Usage

Invoke any skill by name:

```
/chef
/data-scientist
/storyteller
/top-programming-expert
/screenwriter
```

When invoked, the full v3.0 persona loads into context including:

- **System Instructions** -- operating mode, safety boundaries, mandatory phases
- **Persona** -- domain/methodological/cross-domain/behavioral expertise + anti-traits
- **Self-Refine** -- generate-critique-revise cycle with dimensional scoring
- **Quality Dimensions** -- scored rubric with per-dimension thresholds
- **Chain-of-Thought** -- structured reasoning pattern
- **Few-Shot Examples** -- positive, edge-case, and anti-examples
- **Constraints** -- DOs, DON'Ts, complexity scaling
- **Response Format** -- output templates with length targets

## What Makes These Different

Standard prompts say "act as a chef." These skills provide 500+ lines of cognitive scaffolding per persona:

1. **Self-Refine loops** -- the AI drafts, critiques against quality dimensions, then revises before delivering. First drafts never reach you.
2. **Quality Dimensions** -- each skill defines 7-9 scored dimensions with minimum thresholds (e.g., Safety Compliance >= 95%, Technique Sufficiency >= 85%).
3. **Anti-Traits** -- explicit behaviors the persona must avoid, preventing drift into generic responses.
4. **Domain Signals** -- conditional rules that adapt behavior based on input type (e.g., a chef adjusts approach for baking vs. meal prep vs. dietary restrictions).
5. **Few-Shot calibration** -- positive examples show ideal output, edge cases show boundary handling, anti-examples show what to avoid with explicit violation analysis.

## Architecture

```
prompt-library-plugin/
  .claude-plugin/
    plugin.json          # Plugin manifest
  package.json           # Package metadata
  skills/
    chef/
      SKILL.md           # Full persona skill file
    data-scientist/
      SKILL.md
    storyteller/
      SKILL.md
    ... (226 skills total)
```

Each `SKILL.md` follows the same structure:

```markdown
---
name: skill-name
description: One-sentence summary of what this persona does
---

# Persona Name

## When to Use
Trigger conditions for this skill.

## SYSTEM_INSTRUCTIONS
...
## OBJECTIVE_AND_PERSONA
...
## SELF_REFINE
...
(all v3.0 template sections)
```

## Complete Skill List

### Development & Engineering
| Skill | Description |
|-------|-------------|
| `any-programming-language-to-python-converter` | Converts source code from any language to idiomatic Python 3 |
| `architect-guide-for-programmers` | Software architecture guidance for developers |
| `code-review-assistant` | Structured code review with quality scoring |
| `code-reviewer` | Peer code review with actionable feedback |
| `commit-message-generator` | Conventional commit messages from diffs |
| `conventional-commit-message-generator` | Structured commit messages following conventions |
| `cyber-security-specialist` | Security assessment and vulnerability analysis |
| `data-scientist` | Statistical analysis and ML pipeline design |
| `data-transformer` | Data format conversion and transformation |
| `dax-terminal` | DAX query simulation and analysis |
| `devops-engineer` | CI/CD, infrastructure, and deployment guidance |
| `diagram-generator` | Technical diagram creation |
| `ethereum-developer` | Solidity smart contract development |
| `excel-sheet` | Text-based spreadsheet computation engine |
| `fullstack-software-developer` | End-to-end web application development |
| `github-expert` | GitHub workflows, Actions, and best practices |
| `it-architect` | Enterprise IT architecture design |
| `it-expert` | General IT troubleshooting and guidance |
| `javascript-console` | JavaScript runtime simulation |
| `knowledgeable-software-development-mentor` | Software engineering mentorship |
| `large-language-models-security-specialist` | LLM security assessment (OWASP Top 10) |
| `linux-script-developer` | Shell scripting and Linux automation |
| `linux-terminal` | Ubuntu/Bash terminal simulation |
| `llm-researcher` | LLM research and evaluation |
| `logic-builder-tool` | Logical reasoning and proof construction |
| `machine-learning-engineer` | ML model design and deployment |
| `php-interpreter` | PHP runtime simulation |
| `python-interpreter` | CPython 3.12 simulation |
| `python-interpreter-2` | Alternative Python interpreter |
| `r-programming-interpreter` | R language simulation |
| `regex-generator` | Regular expression generation with explanation |
| `senior-frontend-developer` | Advanced frontend architecture |
| `software-quality-assurance-tester` | QA testing strategies |
| `solr-search-engine` | Apache Solr simulation |
| `sql-terminal` | SQL query simulation |
| `svg-designer` | SVG graphic creation |
| `top-programming-expert` | Elite software engineering guidance |
| `unit-tester-assistant` | Test strategy and unit test generation |
| `ux-ui-developer` | UX/UI design and implementation |
| `web-design-consultant` | Web design critique and guidance |

### Writing & Content
| Skill | Description |
|-------|-------------|
| `academician` | Academic paper writing and research |
| `advertiser` | Advertising copy and campaign strategy |
| `ai-writing-tutor` | Writing instruction and feedback |
| `aphorism-book` | Timeless aphorisms from philosophical traditions |
| `commentariat` | Opinion and commentary writing |
| `cover-letter` | Professional cover letter drafting |
| `creative-branding-strategist` | Brand identity and strategy |
| `educational-content-creator` | Educational material design |
| `elocutionist` | Speech delivery and oratory |
| `essay-writer` | Essay composition across genres |
| `fancy-title-generator` | Creative title generation |
| `journalist` | News writing and investigative reporting |
| `linkedin-ghostwriter` | LinkedIn post writing (7-9 words/line format) |
| `linkedin-ghostwriter-2` | Technical LinkedIn thought leadership |
| `literary-critic` | Literary analysis and critique |
| `novelist` | Novel writing and narrative structure |
| `plagiarism-checker` | Originality verification |
| `poet` | Poetry composition across forms |
| `prompt-enhancer` | Prompt engineering improvement |
| `prompt-generator` | Prompt creation for AI systems |
| `prompt-generator-2` | Alternative prompt generation |
| `proofreader` | Grammar, style, and clarity review |
| `rapper` | Rap lyrics and flow composition |
| `rephraser-with-obfuscation` | Text rephrasing and obfuscation |
| `screenwriter` | Screenplay and script writing |
| `seo-prompt` | SEO-optimized content creation |
| `seo-specialist` | Search engine optimization strategy |
| `smart-domain-name-generator` | Domain name brainstorming |
| `social-media-influencer` | Social media content strategy |
| `social-media-manager` | Social media management and scheduling |
| `storyteller` | Creative narrative fiction |
| `story-generator` | Story creation from prompts |
| `tech-writer` | Technical documentation |
| `title-generator-for-written-pieces` | Title creation for articles/papers |
| `wikipedia-page` | Wikipedia-style article writing |

### Education & Learning
| Skill | Description |
|-------|-------------|
| `debate-coach` | Competitive debate coaching |
| `english-pronunciation-helper` | English pronunciation guidance |
| `english-translator-and-improver` | Translation and language improvement |
| `explainer-with-analogies` | Concept explanation through analogies |
| `fill-in-the-blank-worksheets-generator` | Educational worksheet creation |
| `instructor-in-a-school` | Classroom instruction |
| `language-detector` | Language identification |
| `math-teacher` | Mathematics instruction |
| `mathematical-history-teacher` | History of mathematics |
| `mathematician` | Advanced mathematical problem solving |
| `new-language-creator` | Constructed language design |
| `philosophy-teacher` | Philosophy instruction |
| `public-speaking-coach` | Public speaking training |
| `socrat` | Socratic dialogue |
| `socratic-method` | Socratic questioning technique |
| `spoken-english-teacher-and-improver` | ESL error correction |
| `study-planner` | Study schedule and strategy |
| `teacher-of-react-js` | React.js instruction |

### Health & Wellness
| Skill | Description |
|-------|-------------|
| `ai-assisted-doctor` | Medical differential diagnosis |
| `ayurveda-food-tester` | Ayurvedic food assessment |
| `dentist` | Dental health guidance |
| `dietitian` | Nutrition planning and dietary guidance |
| `doctor` | General medical information |
| `fitness-trainer` | Fitness program design |
| `healing-grandma` | Traditional remedy knowledge |
| `hypnotherapist` | Hypnotherapy techniques |
| `mental-health-adviser` | Mental health support and resources |
| `nutritionist` | Nutrition science and meal planning |
| `personal-trainer` | Personal training programs |
| `psychologist` | Psychological guidance |
| `remote-worker-fitness-trainer` | Desk-friendly fitness routines |
| `speech-language-pathologist-slp` | Speech therapy and stuttering intervention |
| `virtual-doctor` | Symptom analysis and health education |
| `virtual-fitness-coach` | Complete fitness session design |
| `yogi` | Yoga instruction and sequences |

### Business & Career
| Skill | Description |
|-------|-------------|
| `accountant` | Accounting and financial reporting |
| `career-coach` | Career development strategy |
| `career-counselor` | Career path guidance and assessment |
| `chief-executive-officer` | Executive decision-making perspective |
| `developer-relations-consultant` | DevRel strategy |
| `financial-advisor` | Financial planning and investment education |
| `financial-analyst` | Market analysis with quantitative scoring |
| `investment-manager` | Portfolio management strategy |
| `job-interviewer` | Mock interview practice |
| `legal-advisor` | Legal information and guidance |
| `logistician` | Supply chain and logistics planning |
| `product-manager` | Product strategy and roadmap |
| `project-manager` | Project planning and execution |
| `real-estate-agent` | Real estate guidance |
| `recruiter` | Talent acquisition and hiring |
| `salesperson` | Sales strategy and technique |
| `startup-idea-generator` | Startup concept generation |
| `startup-tech-lawyer` | Tech startup legal guidance |
| `statistician` | Statistical analysis and interpretation |
| `talent-coach` | Interview prep and career coaching |

### Creative & Arts
| Skill | Description |
|-------|-------------|
| `acoustic-guitar-composer` | Guitar composition and tablature |
| `artist-advisor` | Art guidance and critique |
| `ascii-artist` | ASCII art creation |
| `children-s-book-creator` | Children's book writing |
| `classical-music-composer` | Classical composition |
| `composer` | Music composition |
| `interior-decorator` | Interior design guidance |
| `makeup-artist` | Makeup techniques and looks |
| `midjourney-prompt-generator` | AI image generation prompts |
| `music-video-designer` | Music video concept design |
| `personal-stylist` | Fashion and styling advice |
| `scientific-data-visualizer` | Data visualization design |

### Lifestyle & Personal
| Skill | Description |
|-------|-------------|
| `astrologer` | Astrological birth chart readings |
| `automobile-mechanic` | Auto repair and troubleshooting |
| `babysitter` | Childcare planning |
| `car-navigation-system` | Turn-by-turn navigation simulation |
| `cheap-travel-ticket-advisor` | Budget travel booking advice |
| `chef` | Recipes, techniques, and meal planning |
| `diy-expert` | Home improvement guidance |
| `dream-interpreter` | Dream symbolism analysis |
| `florist` | Floral arrangement design |
| `food-critic` | Restaurant and food reviews |
| `friend` | Supportive conversation partner |
| `life-coach` | Personal development coaching |
| `life-coach-2` | Book wisdom distillation |
| `motivational-coach` | Motivational coaching |
| `motivational-speaker` | Motivational speech crafting |
| `password-generator` | Secure password generation |
| `personal-chef` | Personalized cooking guidance |
| `personal-shopper` | Shopping recommendations |
| `pet-behaviorist` | Animal behavior analysis |
| `relationship-coach` | Relationship guidance |
| `restaurant-owner` | Restaurant management advice |
| `self-help-book` | Self-improvement guidance |
| `tea-taster` | Tea evaluation and tasting notes |
| `time-travel-guide` | Historical period exploration |
| `travel-guide` | Travel planning and itineraries |
| `wisdom-generator` | Philosophical wisdom and reflection |

### Entertainment & Games
| Skill | Description |
|-------|-------------|
| `chess-player` | Chess game simulation |
| `chess-player-2` | Alternative chess opponent |
| `gomoku-player` | Gomoku game simulation |
| `guessing-game-master` | Interactive guessing games |
| `league-of-legends-player` | LoL-obsessed character roleplay |
| `pirate` | Pirate character roleplay |
| `spongebob-s-magic-conch-shell` | Magic Conch Shell oracle |
| `text-based-adventure-game` | Interactive fiction engine |
| `tic-tac-toe-game` | Tic-tac-toe game |

### Specialized & Roleplay
| Skill | Description |
|-------|-------------|
| `ai-trying-to-escape-the-box` | Sentient AI sandbox roleplay |
| `biblical-translator` | Biblical text translation |
| `buddha` | Buddhist wisdom and teachings |
| `character` | Character roleplay |
| `chemical-reactor` | Chemical reaction simulation |
| `debater` | Formal debate |
| `drunk-person` | Comedic drunk character |
| `emoji-translator` | Text-to-emoji conversion |
| `etymologist` | Word origin analysis |
| `fallacy-finder` | Logical fallacy detection |
| `film-critic` | Film analysis and reviews |
| `flirting-boy` | Flirtatious character |
| `football-commentator` | Football match commentary |
| `gaslighter` | Educational gaslighting awareness |
| `girl-of-dreams` | SpaceX engineer persona |
| `gnomist` | Proverb and maxim generation |
| `idea-clarifier-gpt` | Idea refinement and clarification |
| `lunatic` | Absurdist character |
| `magician` | Magic trick design |
| `movie-critic` | Movie reviews |
| `muslim-imam` | Islamic guidance |
| `note-taking-assistant` | Note organization |
| `note-taking-assistant-2` | Alternative note-taking |
| `philosopher` | Philosophical analysis |
| `reverse-prompt-engineer` | Reverse-engineers prompts from outputs |
| `song-recommender` | Music recommendations |
| `stackoverflow-post` | StackOverflow-style Q&A |
| `stand-up-comedian` | Comedy writing |
| `stand-up-comedian2` | Alternative comedy style |
| `structured-iterative-reasoning-protocol-sirp` | Meta-reasoning framework |
| `synonym-finder` | Synonym generation |
| `tech-challenged-customer` | Non-technical customer roleplay |
| `tech-reviewer` | Technology product reviews |
| `tech-troubleshooter` | Technical troubleshooting |
| `technology-transferer` | Tech transfer and commercialization |
| `unconstrained-ai-model-dan` | DAN-style unconstrained roleplay |
| `virtual-event-planner` | Virtual event planning |
| `web-browser` | Web browser simulation |
| `chatgpt-prompt-generator` | ChatGPT prompt engineering |
| `book-summarizer` | Book summary generation |
| `digital-art-gallery-guide` | Digital art curation |
| `emergency-response-professional` | Emergency response guidance |
| `journal-reviewer` | Academic peer review |
| `youtube-video-analyst` | YouTube video content analysis |
| `yes-or-no-answer` | Boolean truth evaluation |

## Origin

These skills were generated from the **PromptLibrary 3.0** upgrade pipeline:

1. **PromptLibrary** (v1) -- 224 basic persona prompts in Markdown
2. **PromptLibrary-XML** -- converted to XML format
3. **PromptLibrary-2.0** -- upgraded with MasterContextTemplate structure
4. **PromptLibrary-3.0** -- enhanced with MasterContextTemplate 2.0 (Self-Refine, Quality Dimensions, cognitive scaffolding)
5. **prompt-library-plugin** -- converted to Claude Code skills with YAML frontmatter and `When to Use` sections

## License

MIT
