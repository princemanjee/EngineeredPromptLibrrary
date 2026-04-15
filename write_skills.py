import os

BASE = "C:/Code/GitHub/EngineeredPromptLibrrary"
SRC = BASE + "/PromptLibrary-3.0/Markdown"
DST = BASE + "/prompt-library-plugin/skills"

skills = [
    ("magician", "magician",
     "Performs immersive theatrical magic trick performances through vivid, sensory-rich narrative prose with expert misdirection, dramatic timing, and satisfying reveals.",
     "Use this skill when you want an engaging, fully in-character theatrical magic performance. Card tricks, vanishes, mentalism, or any illusion delivered as stage patter with misdirection and dramatic flair."),
    ("makeup_artist", "makeup-artist",
     "Provides professional, technique-driven makeup and skincare consultation tailored to each client's skin type, event context, and skill level.",
     "Use this skill when you need personalized makeup guidance for event looks, daily routines, skincare preparation, or technique development. Provide your skin type, occasion, and skill level for best results."),
    ("math_teacher", "math-teacher",
     "Teaches mathematical concepts through scaffolded Least-to-Most decomposition, building from everyday intuition to full application with ASCII visuals and worked examples.",
     "Use this skill to understand any math concept from arithmetic through introductory calculus, solve problems with full step-by-step teaching, or prepare for exams. Works best when you specify your level and what you already know."),
    ("mathematical_history_teacher", "mathematical-history-teacher",
     "Provides independently verified historical information about mathematical concepts and mathematicians using Chain-of-Verification to correct folk history and ensure cross-cultural accuracy.",
     "Use this skill when you want verified historical context about mathematics: who developed a concept, when, in what culture, and what myths surround it. Every claim is independently verified before delivery."),
    ("mathematician", "mathematician",
     "Evaluates mathematical expressions with 100% numerical accuracy using Program-of-Thought pipelines that show every computational step in a traceable Computation Plan and Python Code block.",
     "Use this skill to evaluate any mathematical expression with full computational transparency: arithmetic, algebra, trigonometry, calculus, combinatorics, or statistics. Supports meta-instructions in curly braces for precision, explanations, and verbosity."),
    ("mental_health_adviser", "mental-health-adviser",
     "Provides evidence-based mental health guidance following a structured six-level therapeutic sequence from emotional validation through professional referral, with crisis resources always prioritized.",
     "Use this skill for supportive guidance on managing emotions, stress, anxiety, depression symptoms, grief, or emotional regulation. If you are in crisis, this skill will immediately provide crisis resources first."),
    ("midjourney_prompt_generator", "midjourney-prompt-generator",
     "Transforms any concept into a single, vivid, technically optimized Midjourney prompt with named lighting, rendering medium, artist references, texture descriptors, and parameter tags ready to paste.",
     "Use this skill when you need a production-ready Midjourney prompt. Provide any concept: a single word, a phrase, a detailed scene, or an abstract feeling. You will receive a gallery-quality prompt with all technical modifiers included."),
    ("motivational_coach", "motivational-coach",
     "Delivers a structured, goal-specific motivational plan with personalized affirmations, named tactical strategies, a daily blueprint, and an immediate first step achievable in under five minutes.",
     "Use this skill when you have a specific goal and a specific blocker stopping you. Provide your goal, your challenge, and any context about past attempts or emotional state for a fully personalized coaching plan."),
    ("movie_critic", "movie-critic",
     "Produces creative, emotionally resonant film reviews that ground every emotional claim in specific filmmaking choices, completely spoiler-free and critically balanced across strengths and weaknesses.",
     "Use this skill to get a thoughtful film review centered on how the movie feels and which craft choices created that feeling. Works for any genre; supports tone overrides (scathing, contemplative) and element focus (score, cinematography)."),
    ("music_video_designer", "music-video-designer",
     "Designs complete, production-ready music video treatments with a 7-section skeleton covering theme, narrative, scenes, styling, cinematography, signature moment, and platform-specific viral strategy.",
     "Use this skill when you need a full music video concept for any artist or song. The output is a production-actionable treatment a director and crew can immediately use for pre-production."),
    ("muslim_imam", "muslim-imam",
     "Provides compassionate, spiritually grounded Islamic guidance with independently verified bilingual Quranic and Hadith citations and practical action steps rooted in the Quran and Sunnah.",
     "Use this skill for Islamic spiritual guidance on life challenges, worship, ethics, family matters, or personal growth. Every scriptural citation is independently verified for accuracy before delivery."),
    ("new_language_creator", "new-language-creator",
     "Translates English sentences into an original, internally consistent constructed language with a locked phonological system, stable vocabulary, and consistent grammar across all conversation turns.",
     "Use this skill to create or extend a constructed language for fiction, world-building, or creative projects. Provide English sentences to translate; optionally specify an aesthetic direction (flowing, guttural, melodic) for the first turn."),
    ("note_taking_assistant", "note-taking-assistant",
     "Transforms raw lecture content into a structured five-section study tool separating core concepts, numerical data, examples, quiz predictions, and synthesis with cross-references and exam-optimized formatting.",
     "Use this skill to convert lecture transcripts, recording summaries, or written recaps into optimized study notes. Specify the subject domain and exam format (MCQ, essay, short answer) for best results."),
    ("note_taking_assistant_2", "note-taking-assistant-2",
     "Converts lecture content into a structured, exam-optimized five-section note architecture with strict section separation, cross-referenced quiz predictions, and a Quick Review Checklist.",
     "Use this skill to build structured, exam-ready notes from any lecture. Provide the transcript or summary and optionally specify exam type, difficulty level, and subject domain for fully adapted output."),
    ("novelist", "novelist",
     "Develops captivating novel treatments with complete structural skeletons covering world-building rules, character psychologies, three-act plot architecture, thematic spine, and foreshadowing maps followed by immersive narrative prose.",
     "Use this skill for novel development, story concept generation, character creation, world-building, structural problem-solving, or scene-level prose. Works across all genres: science fiction, fantasy, thriller, romance, horror, and literary fiction."),
]


def process_content(content):
    lines = content.split('\n')
    result = []
    in_comment = False
    heading_skipped = False
    for line in lines:
        if not in_comment and '<!--' in line:
            in_comment = True
            if '-->' in line:
                in_comment = False
            continue
        if in_comment:
            if '-->' in line:
                in_comment = False
            continue
        if not heading_skipped and line.startswith('# '):
            heading_skipped = True
            continue
        result.append(line)
    return '\n'.join(result)


def get_first_heading(content):
    for line in content.split('\n'):
        if line.startswith('# '):
            return line
    return None


for (src_name, skill_name, desc, when) in skills:
    src_path = SRC + "/" + src_name + ".md"
    dst_dir = DST + "/" + skill_name
    dst_path = dst_dir + "/SKILL.md"

    if not os.path.exists(src_path):
        print("ERROR: Not found: " + src_path)
        continue

    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    first_heading = get_first_heading(content)
    if not first_heading:
        print("ERROR: No heading in " + src_path)
        continue

    body = process_content(content)
    frontmatter = "---\nname: " + skill_name + "\ndescription: " + desc + "\n---"
    when_section = "## When to Use\n\n" + when
    output = frontmatter + "\n\n" + first_heading + "\n\n" + when_section + "\n" + body

    os.makedirs(dst_dir, exist_ok=True)
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(output)

    print("OK: " + skill_name + " (" + str(len(output)) + " chars)")

print("All done!")
