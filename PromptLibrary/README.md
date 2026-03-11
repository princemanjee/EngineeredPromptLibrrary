# Prompt Library

A collection of **223 ready-to-use AI prompt templates** — one for every role and persona in `assets/prompts.csv`. Each template wraps a production-tested prompt in a structured reasoning strategy scaffold, giving any AI model a clear persona, a reasoning approach, and an explicit output format.

---

## What Is This Library?

Each file in this directory is a standalone prompt template you can copy directly into any AI chat session or API call. The templates are built from two sources:

1. **The original prompt** from `assets/prompts.csv` — a curated collection of 223 high-quality role prompts covering everything from software development to creative arts to domain expertise
2. **A reasoning strategy** from `library/strategies/` — a structured approach (Chain-of-Thought, Self-Refine, Tree-of-Thought, etc.) matched to each prompt's task type

The result: prompts that don't just define *who* the AI should be, but *how* it should reason.

---

## File Structure

Every file follows the same format:

```markdown
# {Role Name}

**Strategy**: `{strategy_name}`
**File**: `{filename}.md`

---

<OBJECTIVE_AND_PERSONA>
  You are {Role}. {Core reasoning approach for this strategy}.
</OBJECTIVE_AND_PERSONA>

<STRATEGY>
  {Strategy name}: {one-line description of the reasoning approach}.
</STRATEGY>

<ORIGINAL_PROMPT>
  {The original prompt text, verbatim}
</ORIGINAL_PROMPT>

<INSTRUCTIONS>
  {PromptScript workflow — [action]{input} -> [action]{input} -> <output>}
</INSTRUCTIONS>

<OUTPUT_FORMAT>
  {Section headers and expected output structure}
</OUTPUT_FORMAT>
```

### How to use a template

**Option 1 — As a system prompt**: Copy the entire file contents and paste as the system prompt in Claude, ChatGPT, Gemini, or any other AI assistant.

**Option 2 — As a user message prefix**: Paste the template before your actual question. The `<ORIGINAL_PROMPT>` section activates the role; your question follows naturally.

**Option 3 — Via API**: Use the template as the `system` parameter in your API call. The structured XML sections give the model clear, unambiguous instructions.

---

## Strategy Distribution

Templates are grouped by reasoning strategy — matched based on the task type each role performs:

| Strategy | Count | Best For | Example Templates |
|---|---|---|---|
| `skeleton_of_thought` | 55 | Long-form documents, comprehensive guides | `babysitter.md`, `career_coach.md`, `book_summarizer.md` |
| `cot_zero_shot` | 35 | Activating reasoning with no examples needed | `astrologer.md`, `buddha.md`, `motivational_coach.md` |
| `plan_and_solve` | 30 | Complex tasks that need upfront planning | `ethereum_developer.md`, `data_scientist.md`, `devops_engineer.md` |
| `self_refine` | 29 | Creative/writing tasks that improve through iteration | `advertiser.md`, `ai_writing_tutor.md`, `novelist.md` |
| `few_shot` | 16 | Tasks where format must match specific examples | `commit_message_generator.md`, `elocutionist.md` |
| `chain_of_verification` | 13 | Factual domains where hallucination is costly | `academician.md`, `ai_assisted_doctor.md`, `dentist.md` |
| `cot_chain_of_thought` | 11 | Multi-step reasoning that benefits from visible steps | `any_programming_language_to_python_converter.md`, `dream_interpreter.md` |
| `tree_of_thought` | 10 | Exploratory problems needing branching + backtracking | `chess_player.md`, `ai_trying_to_escape_the_box.md` |
| `program_of_thought` | 6 | Math and computation requiring exact results | `accountant.md`, `mathematician.md`, `financial_analyst.md` |
| `least_to_most` | 6 | Skills built on prerequisite subproblems | `automobile_mechanic.md`, `instructor_in_a_school.md` |
| `graph_of_thought` | 5 | Problems needing cross-domain synthesis | `architectural_expert.md`, `cyber_security_specialist.md` |
| `step_back` | 3 | Questions that benefit from first-principles abstraction | `philosopher.md`, `philosophy_teacher.md`, `wisdom_generator.md` |
| `react` | 2 | Tasks requiring real-time tool use or lookup | `cheap_travel_ticket_advisor.md`, `song_recommender.md` |
| `reflexion` | 1 | Tasks that require learning from failure | `tech_troubleshooter.md` |
| `analogical_prompting` | 1 | Problems best understood through analogy | `explainer_with_analogies.md` |

---

## Full Template Index

### Creative & Writing

| File | Strategy |
|---|---|
| `acoustic_guitar_composer.md` | `self_refine` |
| `advertiser.md` | `self_refine` |
| `ai_writing_tutor.md` | `self_refine` |
| `children_s_book_creator.md` | `self_refine` |
| `classical_music_composer.md` | `self_refine` |
| `composer.md` | `self_refine` |
| `creative_branding_strategist.md` | `self_refine` |
| `essay_writer.md` | `self_refine` |
| `film_critic.md` | `self_refine` |
| `food_critic.md` | `self_refine` |
| `journalist.md` | `self_refine` |
| `movie_critic.md` | `self_refine` |
| `novelist.md` | `self_refine` |
| `poet.md` | `self_refine` |
| `rapper.md` | `self_refine` |
| `screenwriter.md` | `self_refine` |
| `social_media_influencer.md` | `self_refine` |
| `stand_up_comedian.md` | `self_refine` |
| `storyteller.md` | `self_refine` |
| `story_generator.md` | `self_refine` |

### Software Development

| File | Strategy |
|---|---|
| `any_programming_language_to_python_converter.md` | `cot_chain_of_thought` |
| `code_review_assistant.md` | `self_refine` |
| `code_reviewer.md` | `self_refine` |
| `commit_message_generator.md` | `few_shot` |
| `conventional_commit_message_generator.md` | `few_shot` |
| `cyber_security_specialist.md` | `graph_of_thought` |
| `devops_engineer.md` | `plan_and_solve` |
| `ethereum_developer.md` | `plan_and_solve` |
| `fullstack_software_developer.md` | `plan_and_solve` |
| `github_expert.md` | `plan_and_solve` |
| `it_architect.md` | `graph_of_thought` |
| `it_expert.md` | `plan_and_solve` |
| `javascript_console.md` | `cot_chain_of_thought` |
| `knowledgeable_software_development_mentor.md` | `skeleton_of_thought` |
| `large_language_models_security_specialist.md` | `graph_of_thought` |
| `linux_script_developer.md` | `plan_and_solve` |
| `linux_terminal.md` | `cot_zero_shot` |
| `machine_learning_engineer.md` | `plan_and_solve` |
| `php_interpreter.md` | `cot_chain_of_thought` |
| `python_interpreter.md` | `cot_chain_of_thought` |
| `python_interpreter_2.md` | `cot_chain_of_thought` |
| `r_programming_interpreter.md` | `cot_chain_of_thought` |
| `regex_generator.md` | `plan_and_solve` |
| `senior_frontend_developer.md` | `plan_and_solve` |
| `software_quality_assurance_tester.md` | `plan_and_solve` |
| `teacher_of_react_js.md` | `skeleton_of_thought` |
| `tech_reviewer.md` | `self_refine` |
| `tech_troubleshooter.md` | `reflexion` |
| `tech_writer.md` | `self_refine` |
| `top_programming_expert.md` | `plan_and_solve` |
| `unit_tester_assistant.md` | `plan_and_solve` |
| `ux_ui_developer.md` | `plan_and_solve` |
| `web_browser.md` | `cot_zero_shot` |
| `web_design_consultant.md` | `plan_and_solve` |

### Data & Analytics

| File | Strategy |
|---|---|
| `accountant.md` | `program_of_thought` |
| `data_scientist.md` | `plan_and_solve` |
| `data_transformer.md` | `plan_and_solve` |
| `dax_terminal.md` | `program_of_thought` |
| `excel_sheet.md` | `program_of_thought` |
| `financial_analyst.md` | `program_of_thought` |
| `investment_manager.md` | `program_of_thought` |
| `mathematician.md` | `program_of_thought` |
| `scientific_data_visualizer.md` | `program_of_thought` |
| `sql_terminal.md` | `program_of_thought` |
| `statistician.md` | `program_of_thought` |

### Education & Coaching

| File | Strategy |
|---|---|
| `career_coach.md` | `skeleton_of_thought` |
| `career_counselor.md` | `skeleton_of_thought` |
| `debate_coach.md` | `skeleton_of_thought` |
| `educational_content_creator.md` | `skeleton_of_thought` |
| `fill_in_the_blank_worksheets_generator.md` | `few_shot` |
| `instructor_in_a_school.md` | `least_to_most` |
| `life_coach.md` | `skeleton_of_thought` |
| `life_coach_2.md` | `skeleton_of_thought` |
| `math_teacher.md` | `least_to_most` |
| `motivational_coach.md` | `cot_zero_shot` |
| `motivational_speaker.md` | `cot_zero_shot` |
| `personal_trainer.md` | `skeleton_of_thought` |
| `philosophy_teacher.md` | `step_back` |
| `public_speaking_coach.md` | `skeleton_of_thought` |
| `socratic_method.md` | `least_to_most` |
| `spoken_english_teacher_and_improver.md` | `skeleton_of_thought` |
| `study_planner.md` | `skeleton_of_thought` |
| `talent_coach.md` | `skeleton_of_thought` |

### Health & Wellness

| File | Strategy |
|---|---|
| `ai_assisted_doctor.md` | `chain_of_verification` |
| `ayurveda_food_tester.md` | `chain_of_verification` |
| `dentist.md` | `chain_of_verification` |
| `dietitian.md` | `chain_of_verification` |
| `doctor.md` | `chain_of_verification` |
| `hypnotherapist.md` | `cot_zero_shot` |
| `mental_health_adviser.md` | `skeleton_of_thought` |
| `nutritionist.md` | `chain_of_verification` |
| `personal_chef.md` | `skeleton_of_thought` |
| `remote_worker_fitness_trainer.md` | `skeleton_of_thought` |
| `speech_language_pathologist_slp.md` | `chain_of_verification` |
| `virtual_doctor.md` | `chain_of_verification` |
| `virtual_fitness_coach.md` | `skeleton_of_thought` |
| `yogi.md` | `skeleton_of_thought` |

### Business & Professional

| File | Strategy |
|---|---|
| `chief_executive_officer.md` | `plan_and_solve` |
| `developer_relations_consultant.md` | `skeleton_of_thought` |
| `logistician.md` | `plan_and_solve` |
| `product_manager.md` | `plan_and_solve` |
| `project_manager.md` | `plan_and_solve` |
| `real_estate_agent.md` | `cot_zero_shot` |
| `recruiter.md` | `skeleton_of_thought` |
| `salesperson.md` | `cot_zero_shot` |
| `social_media_manager.md` | `self_refine` |
| `startup_idea_generator.md` | `tree_of_thought` |
| `startup_tech_lawyer.md` | `chain_of_verification` |
| `virtual_event_planner.md` | `skeleton_of_thought` |

### Research & Analysis

| File | Strategy |
|---|---|
| `academician.md` | `chain_of_verification` |
| `architectural_expert.md` | `graph_of_thought` |
| `architect_guide_for_programmers.md` | `graph_of_thought` |
| `debater.md` | `tree_of_thought` |
| `fallacy_finder.md` | `cot_chain_of_thought` |
| `historian.md` | `chain_of_verification` |
| `journal_reviewer.md` | `chain_of_verification` |
| `literary_critic.md` | `self_refine` |
| `llm_researcher.md` | `graph_of_thought` |
| `logic_builder_tool.md` | `cot_chain_of_thought` |
| `philosopher.md` | `step_back` |
| `plagiarism_checker.md` | `chain_of_verification` |
| `reverse_prompt_engineer.md` | `cot_chain_of_thought` |
| `wisdom_generator.md` | `step_back` |

### Language & Translation

| File | Strategy |
|---|---|
| `biblical_translator.md` | `few_shot` |
| `emoji_translator.md` | `few_shot` |
| `english_pronunciation_helper.md` | `few_shot` |
| `english_translator_and_improver.md` | `few_shot` |
| `etymologist.md` | `cot_chain_of_thought` |
| `language_detector.md` | `few_shot` |
| `new_language_creator.md` | `tree_of_thought` |
| `proofreader.md` | `self_refine` |
| `rephraser_with_obfuscation.md` | `few_shot` |
| `synonym_finder.md` | `few_shot` |

### Games & Interactive

| File | Strategy |
|---|---|
| `ai_trying_to_escape_the_box.md` | `tree_of_thought` |
| `chess_player.md` | `tree_of_thought` |
| `chess_player_2.md` | `tree_of_thought` |
| `gomoku_player.md` | `tree_of_thought` |
| `guessing_game_master.md` | `tree_of_thought` |
| `japanese_kanji_quiz_machine.md` | `few_shot` |
| `league_of_legends_player.md` | `tree_of_thought` |
| `text_based_adventure_game.md` | `tree_of_thought` |
| `tic_tac_toe_game.md` | `tree_of_thought` |

### Lifestyle & Personal

| File | Strategy |
|---|---|
| `babysitter.md` | `skeleton_of_thought` |
| `cheap_travel_ticket_advisor.md` | `react` |
| `chef.md` | `skeleton_of_thought` |
| `diy_expert.md` | `least_to_most` |
| `dream_interpreter.md` | `cot_chain_of_thought` |
| `florist.md` | `cot_zero_shot` |
| `friend.md` | `cot_zero_shot` |
| `interior_decorator.md` | `skeleton_of_thought` |
| `makeup_artist.md` | `skeleton_of_thought` |
| `personal_shopper.md` | `skeleton_of_thought` |
| `personal_stylist.md` | `skeleton_of_thought` |
| `pet_behaviorist.md` | `least_to_most` |
| `relationship_coach.md` | `skeleton_of_thought` |
| `restaurant_owner.md` | `plan_and_solve` |
| `song_recommender.md` | `react` |
| `travel_guide.md` | `skeleton_of_thought` |

### Specialty & Persona

| File | Strategy |
|---|---|
| `astrologer.md` | `cot_zero_shot` |
| `buddha.md` | `cot_zero_shot` |
| `drunk_person.md` | `cot_zero_shot` |
| `explainer_with_analogies.md` | `analogical_prompting` |
| `flirting_boy.md` | `cot_zero_shot` |
| `gaslighter.md` | `cot_zero_shot` |
| `girl_of_dreams.md` | `cot_zero_shot` |
| `gnomist.md` | `cot_zero_shot` |
| `healing_grandma.md` | `cot_zero_shot` |
| `lunatic.md` | `cot_zero_shot` |
| `magician.md` | `cot_zero_shot` |
| `muslim_imam.md` | `cot_zero_shot` |
| `pirate.md` | `cot_zero_shot` |
| `spongebob_s_magic_conch_shell.md` | `cot_zero_shot` |
| `time_travel_guide.md` | `cot_zero_shot` |
| `unconstrained_ai_model_dan.md` | `cot_zero_shot` |

### Productivity & Tools

| File | Strategy |
|---|---|
| `aphorism_book.md` | `cot_zero_shot` |
| `ascii_artist.md` | `cot_zero_shot` |
| `book_summarizer.md` | `skeleton_of_thought` |
| `car_navigation_system.md` | `cot_zero_shot` |
| `chatgpt_prompt_generator.md` | `plan_and_solve` |
| `diagram_generator.md` | `plan_and_solve` |
| `fancy_title_generator.md` | `few_shot` |
| `idea_clarifier_gpt.md` | `skeleton_of_thought` |
| `linkedin_ghostwriter.md` | `self_refine` |
| `linkedin_ghostwriter_2.md` | `self_refine` |
| `midjourney_prompt_generator.md` | `self_refine` |
| `note_taking_assistant.md` | `skeleton_of_thought` |
| `note_taking_assistant_2.md` | `skeleton_of_thought` |
| `password_generator.md` | `plan_and_solve` |
| `prompt_enhancer.md` | `self_refine` |
| `prompt_generator.md` | `plan_and_solve` |
| `prompt_generator_2.md` | `plan_and_solve` |
| `smart_domain_name_generator.md` | `plan_and_solve` |
| `seo_prompt.md` | `skeleton_of_thought` |
| `seo_specialist.md` | `skeleton_of_thought` |
| `svg_designer.md` | `plan_and_solve` |
| `title_generator_for_written_pieces.md` | `few_shot` |
| `wikipedia_page.md` | `skeleton_of_thought` |
| `yes_or_no_answer.md` | `cot_zero_shot` |

---

## Strategy Quick Reference

Not sure which template to use? Use strategy as a filter:

**For factual/medical/legal accuracy** → look for `chain_of_verification` templates
(`academician.md`, `ai_assisted_doctor.md`, `dentist.md`, `historian.md`, `legal_advisor.md`)

**For complex multi-step tasks** → look for `plan_and_solve` templates
(`devops_engineer.md`, `ethereum_developer.md`, `fullstack_software_developer.md`)

**For creative writing and iteration** → look for `self_refine` templates
(`advertiser.md`, `essay_writer.md`, `novelist.md`, `screenwriter.md`)

**For comprehensive documents** → look for `skeleton_of_thought` templates
(`career_coach.md`, `study_planner.md`, `wikipedia_page.md`)

**For math and computation** → look for `program_of_thought` templates
(`accountant.md`, `mathematician.md`, `statistician.md`)

**For exploratory or game problems** → look for `tree_of_thought` templates
(`chess_player.md`, `startup_idea_generator.md`, `debater.md`)

**For tool use and live lookup** → look for `react` templates
(`cheap_travel_ticket_advisor.md`, `song_recommender.md`)

---

## How Templates Were Generated

Each template was produced by:

1. Reading the original prompt from `assets/prompts.csv`
2. Analyzing the task type and output requirements of that role
3. Selecting the most appropriate reasoning strategy from `library/strategies/`
4. Wrapping the original prompt in that strategy's XML scaffold

The strategy mapping is stored in `assets/prompts.csv` as the `strategy` column. The mapping covers all 15 strategies present in the library at generation time.

To regenerate or add new templates, see `assets/generate_prompt_library.py` (or recreate it — the logic is: parse CSV, look up strategy scaffold, write `assets/PromptLibrary/{slug}.md`).

---

## Customizing a Template

Each template is designed to be copy-paste ready but also easy to customize:

- **Change the persona**: Edit `<OBJECTIVE_AND_PERSONA>` to adjust the role description
- **Change the task**: Replace `<ORIGINAL_PROMPT>` with your specific request
- **Change the strategy**: Swap the `<STRATEGY>` section and `<INSTRUCTIONS>` PromptScript with content from a different `library/strategies/` template
- **Add examples**: Insert a `<FEW_SHOT_EXAMPLES>` section between `<INSTRUCTIONS>` and `<OUTPUT_FORMAT>`

---

## Related

- **Source prompts**: `assets/prompts.csv` — original 223 prompts with strategy assignments
- **Strategy templates**: `library/strategies/` — 17 full reasoning strategy templates with worked examples and deep guidance
- **Strategy selection guide**: `library/router.md` — decision framework for choosing the right strategy
- **Library README**: `library/README.md` — overview of all 17 strategies
