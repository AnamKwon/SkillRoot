#!/usr/bin/env python3
"""Synchronize generated SkillRoot docs and UI metadata."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "theories" / "catalog.yml"
SKILLS = ROOT / "skills"


SKILL_DATA = {
    "abstract-interpretation": {
        "display": "Abstract Interpretation",
        "short": "Sound static reasoning with approximations",
        "prompt": "Use $abstract-interpretation to reason about this safety property without enumerating every execution path.",
        "concepts": [
            "Concrete executions are replaced by an abstraction that safely over-approximates behavior.",
            "The abstraction is only useful when it preserves the property under analysis.",
            "Precision loss must be reported as false-positive, false-negative, or unmodeled-behavior risk.",
        ],
        "translation": "Use it to choose a property, define the abstract state, trace joins and loops, and state precision limits before claiming safety.",
        "misuse": "Do not use a few sampled executions as if they were a sound abstraction.",
        "mapping": "Property -> abstraction -> precision limits -> focused verification.",
    },
    "activity-theory": {
        "display": "Activity Theory",
        "short": "Workflow change through activity systems",
        "prompt": "Use $activity-theory to locate the workflow contradiction before changing this tool or code path.",
        "concepts": [
            "Work is an activity system: subject, object, tools, rules, community, division of labor, and outcome.",
            "Failures often arise from contradictions between system elements.",
            "A local tool improvement can worsen the whole activity if roles or rules are ignored.",
        ],
        "translation": "Use it to map the activity system and place code changes at the contradiction that changes the outcome.",
        "misuse": "Do not optimize one actor's step while hiding a broader workflow conflict.",
        "mapping": "Activity element conflict -> code/tool location -> workflow outcome check.",
    },
    "cleanroom-software-engineering": {
        "display": "Cleanroom Engineering",
        "short": "Defect prevention with precise specs",
        "prompt": "Use $cleanroom-software-engineering to define the increment, specification, and verification evidence before coding.",
        "concepts": [
            "Reliability is built through precise specification and defect prevention.",
            "Small increments should be reviewable and verifiable before broad debugging.",
            "Testing should reflect realistic usage profiles, not only convenient examples.",
        ],
        "translation": "Use it to write the behavioral specification, reason about correctness, and validate a small reliable increment.",
        "misuse": "Do not treat after-the-fact debugging as a substitute for deciding what correctness means.",
        "mapping": "Specification -> increment -> correctness argument -> usage-profile validation.",
        "fallbacks": [
            ("UTK publication page", "https://voljournals.utk.edu/utk_harlan/18/"),
            ("Course-hosted PDF", "https://www.cs.toronto.edu/~chechik/courses07/csc410/mills.pdf"),
        ],
    },
    "cognitive-dimensions": {
        "display": "Cognitive Dimensions",
        "short": "Ergonomic checks for code notations",
        "prompt": "Use $cognitive-dimensions to evaluate this API or config shape for human editing and debugging.",
        "concepts": [
            "A notation should be judged by the cognitive work it imposes on users.",
            "Dimensions such as viscosity, visibility, hidden dependencies, and error-proneness expose tradeoffs.",
            "The right notation depends on the user's task, not only implementation convenience.",
        ],
        "translation": "Use it to identify the notation surface, inspect key dimensions, and show a before/after usage example.",
        "misuse": "Do not claim a notation is better without naming which cognitive dimension improved and what got worse.",
        "mapping": "Notation surface -> relevant dimensions -> tradeoff -> usage example.",
    },
    "conways-law": {
        "display": "Conway's Law",
        "short": "Architecture shaped by communication paths",
        "prompt": "Use $conways-law to check whether this service or package boundary fits the ownership and handoff structure.",
        "concepts": [
            "System designs tend to mirror the communication structures that produce them.",
            "Boundaries need maintainers, reviewers, deployers, and consumers who can sustain them.",
            "A technically clean split can fail when ownership and coordination do not match it.",
        ],
        "translation": "Use it to map ownership and handoffs before changing architecture, packages, or service seams.",
        "misuse": "Do not preserve poor structure forever just because the current organization produced it.",
        "mapping": "Communication path -> technical boundary -> coordination proof.",
    },
    "design-by-contract": {
        "display": "Design by Contract",
        "short": "Explicit caller and provider obligations",
        "prompt": "Use $design-by-contract to define preconditions, postconditions, and invariants for this boundary.",
        "concepts": [
            "A software boundary is a contract between caller obligations and provider guarantees.",
            "Preconditions, postconditions, and invariants assign responsibility clearly.",
            "Checks are most useful where they clarify trusted and untrusted boundaries.",
        ],
        "translation": "Use it to state obligations and guarantees, then test valid and invalid contract cases.",
        "misuse": "Do not scatter defensive checks everywhere when one boundary contract would be clearer.",
        "mapping": "Boundary -> preconditions/postconditions/invariants -> contract tests.",
    },
    "design-patterns": {
        "display": "Design Patterns",
        "short": "Apply patterns only when forces match",
        "prompt": "Use $design-patterns to decide whether a known pattern fits this recurring design problem.",
        "concepts": [
            "A pattern is a named solution to a recurring problem in context.",
            "The forces and consequences matter more than the pattern name.",
            "Patterns improve communication only when they fit the present collaboration structure.",
        ],
        "translation": "Use it to identify forces first, compare local idioms, then choose a pattern or a simpler alternative.",
        "misuse": "Do not add abstract participants for one caller or choose a pattern before naming the problem.",
        "mapping": "Recurring problem -> forces -> pattern or simpler alternative -> consequence check.",
        "fallbacks": [
            ("University metadata page", "https://experts.illinois.edu/en/publications/design-patterns-elements-of-reusable-object-oriented-software/"),
        ],
    },
    "distributed-cognition": {
        "display": "Distributed Cognition",
        "short": "Trace knowledge across people and tools",
        "prompt": "Use $distributed-cognition to trace how operational knowledge moves through code, tools, and people.",
        "concepts": [
            "Cognitive work can be distributed across people, artifacts, representations, and environments.",
            "Software operations often depend on logs, dashboards, runbooks, schemas, queues, and handoffs.",
            "Correctness can fail when information is represented in the wrong place or not propagated.",
        ],
        "translation": "Use it to map information flow and update the artifact another actor depends on.",
        "misuse": "Do not fix code locally while leaving dashboards, runbooks, alerts, or schemas inconsistent.",
        "mapping": "Distributed representation -> propagation path -> whole-system verification.",
        "fallbacks": [
            ("UCSD interaction paper", "https://pages.ucsd.edu/~ehutchins/integratedCogSci/DCOG-Interaction.pdf"),
        ],
    },
    "domain-driven-design": {
        "display": "Domain-Driven Design",
        "short": "Model code around domain language",
        "prompt": "Use $domain-driven-design to model this business rule with bounded context and ubiquitous language.",
        "concepts": [
            "The domain model should use the language of the business domain.",
            "Bounded contexts protect different meanings of the same term.",
            "Aggregates and domain concepts should own the invariants they enforce.",
        ],
        "translation": "Use it to name concepts from domain examples, place behavior with invariant owners, and translate across contexts.",
        "misuse": "Do not add DDD tactical patterns as ceremony when CRUD or simple data transformation is enough.",
        "mapping": "Domain language -> bounded context -> invariant owner -> domain example.",
    },
    "double-loop-learning": {
        "display": "Double-Loop Learning",
        "short": "Revise assumptions behind repeated failures",
        "prompt": "Use $double-loop-learning to identify the governing assumption behind this repeated failure.",
        "concepts": [
            "Single-loop learning corrects an action while leaving governing variables unchanged.",
            "Double-loop learning questions assumptions, policies, metrics, defaults, or incentives.",
            "A repeated failure often means the old rule made the bad action reasonable.",
        ],
        "translation": "Use it to separate the immediate fix from the premise change that prevents recurrence.",
        "misuse": "Do not make broad policy changes from one isolated failure without evidence.",
        "mapping": "Error -> single-loop fix -> governing variable -> future-case proof.",
        "fallbacks": [
            ("HBR article page", "https://hbr.org/1977/09/double-loop-learning-in-organizations"),
            ("Action Design reading list", "https://actiondesign.com/resources/readings/double-loop-learning"),
        ],
    },
    "essential-complexity": {
        "display": "Essential Complexity",
        "short": "Separate domain essence from accidents",
        "prompt": "Use $essential-complexity to simplify accidental complexity without hiding the essential domain rules.",
        "concepts": [
            "Essential complexity belongs to the problem itself.",
            "Accidental complexity comes from tools, representations, ceremony, duplication, or stale abstractions.",
            "Simplification is harmful when it erases real domain distinctions.",
        ],
        "translation": "Use it to classify complexity, remove accidental parts, and keep essential rules visible.",
        "misuse": "Do not flatten domain rules just to make code look shorter.",
        "mapping": "Essential rule kept -> accidental machinery removed -> behavior proof.",
    },
    "information-hiding": {
        "display": "Information Hiding",
        "short": "Hide volatile decisions behind interfaces",
        "prompt": "Use $information-hiding to choose the module boundary that hides the most volatile design decision.",
        "concepts": [
            "Modules should hide design decisions likely to change.",
            "The interface should express stable caller intent rather than internal mechanics.",
            "A good boundary protects callers from representation, policy, algorithm, or vendor churn.",
        ],
        "translation": "Use it to identify volatile decisions and place them behind the closest existing owner.",
        "misuse": "Do not create broad abstractions for a speculative future caller.",
        "mapping": "Volatile decision -> owning module -> stable interface -> caller proof.",
        "fallbacks": [
            ("Public copy PDF", "https://wstomv.win.tue.nl/edu/2ip30/references/criteria_for_modularization.pdf"),
        ],
    },
    "literate-programming": {
        "display": "Literate Programming",
        "short": "Align human explanation with code behavior",
        "prompt": "Use $literate-programming to make this implementation readable in the order a maintainer needs.",
        "concepts": [
            "Programs can be written as explanations for human readers.",
            "Explanatory order may differ from machine execution order.",
            "Names, examples, prose, and tests should keep intent recoverable.",
        ],
        "translation": "Use it to identify the maintainer-facing story and keep prose, examples, and behavior synchronized.",
        "misuse": "Do not add long comments that duplicate obvious code facts.",
        "mapping": "Reader story -> explanation order -> code/examples/tests synchronization.",
        "fallbacks": [
            ("Knuth Stanford page", "https://www-cs-faculty.stanford.edu/~knuth/lp.html"),
            ("Oxford Academic article", "https://academic.oup.com/comjnl/article/27/2/97/343244"),
        ],
    },
    "programming-as-theory-building": {
        "display": "Programming as Theory Building",
        "short": "Preserve program theory while changing code",
        "prompt": "Use $programming-as-theory-building to map the domain invariant before changing this code.",
        "concepts": [
            "The useful product of programming is the programmer's theory of the program.",
            "Code, tests, names, and docs are evidence from which the theory is recovered.",
            "A change is good when it preserves and improves the theory, not just the text.",
        ],
        "translation": "Use it to map world rules to code, place changes beside existing concepts, and verify the invariant.",
        "misuse": "Do not edit code as disconnected text when the domain mapping is unclear.",
        "mapping": "World rule -> current program theory -> closest facility -> verification.",
    },
    "reflective-practice": {
        "display": "Reflective Practice",
        "short": "Reframe coding surprises during action",
        "prompt": "Use $reflective-practice to reframe this debugging surprise before adding another patch.",
        "concepts": [
            "A professional makes a move, the situation talks back, and the frame may need to change.",
            "Surprise is evidence that the old framing may be wrong.",
            "Small experiments test the revised frame while work is still reversible.",
        ],
        "translation": "Use it to name the surprise, revise the frame, and run the next small experiment.",
        "misuse": "Do not keep patching without stating what each patch is testing.",
        "mapping": "Move -> back-talk -> revised frame -> experiment.",
    },
    "sensemaking": {
        "display": "Sensemaking",
        "short": "Build plausible stories from messy cues",
        "prompt": "Use $sensemaking to turn these logs, errors, and reports into a testable working story.",
        "concepts": [
            "Understanding is cue-driven, retrospective, and provisional.",
            "A useful story is plausible and testable, not prematurely certain.",
            "New evidence should update the narrative instead of being forced into it.",
        ],
        "translation": "Use it to gather cues, build a working story, and choose a diagnostic action that could change the story.",
        "misuse": "Do not label a cause like cache issue or race condition without supporting cues.",
        "mapping": "Cues -> plausible story -> diagnostic test -> revised story.",
    },
    "situated-action": {
        "display": "Situated Action",
        "short": "Adapt plans to local runtime evidence",
        "prompt": "Use $situated-action to revise this plan based on the current files, tests, and user feedback.",
        "concepts": [
            "Plans are resources for action, not scripts that determine action.",
            "Real work unfolds in local situations with changing evidence.",
            "A stale plan should yield to user feedback, logs, tests, and tool output.",
        ],
        "translation": "Use it to state the current plan, inspect local evidence, and revise the next step when the situation changes.",
        "misuse": "Do not keep following a checklist after the workspace or user has contradicted it.",
        "mapping": "Plan -> situated evidence -> plan revision -> immediate proof.",
        "fallbacks": [
            ("Internet Archive book page", "https://archive.org/details/planssituatedact0000such"),
            ("Google Books page", "https://books.google.com/books/about/Plans_and_Situated_Actions.html?id=AJ_eBJtHxmsC"),
        ],
    },
    "stepwise-refinement": {
        "display": "Stepwise Refinement",
        "short": "Refine specs into code one decision at a time",
        "prompt": "Use $stepwise-refinement to refine this high-level behavior into executable code in small steps.",
        "concepts": [
            "Start from a precise high-level specification.",
            "Replace abstract operations with concrete ones one decision at a time.",
            "Each refinement must preserve the intent of the level above.",
        ],
        "translation": "Use it to name abstract operations, refine one decision, and verify preservation at each level.",
        "misuse": "Do not invent layers or helper abstractions that are not required by the current refinement.",
        "mapping": "Specification -> abstract operation -> refinement -> preservation check.",
        "fallbacks": [
            ("Public copy PDF", "https://pascal.hansotten.com/uploads/wirth/StepwiseRefinement.pdf"),
        ],
    },
    "structured-programming": {
        "display": "Structured Programming",
        "short": "Keep control flow reasoned and tractable",
        "prompt": "Use $structured-programming to simplify this control flow while preserving behavior.",
        "concepts": [
            "Programs should be composed from control structures that support reasoning.",
            "Blocks need clear entry, effect, and continuation.",
            "The goal is tractable correctness, not style purity.",
        ],
        "translation": "Use it to inspect branches, loops, state changes, and exits before refactoring control flow.",
        "misuse": "Do not force awkward nesting when a guard clause clarifies invalid cases.",
        "mapping": "Control shape -> block reasoning -> branch/loop verification.",
    },
    "test-driven-development": {
        "display": "Test-Driven Development",
        "short": "Drive behavior through red-green-refactor",
        "prompt": "Use $test-driven-development to implement the next behavior with a red-green-refactor loop.",
        "concepts": [
            "A failing test expresses the next behavior before production code changes.",
            "The smallest honest implementation makes the test pass.",
            "Refactoring happens after green while tests preserve behavior.",
        ],
        "translation": "Use it to choose one behavior slice, observe red, implement green, and refactor under the test.",
        "misuse": "Do not write tests that assert implementation details instead of observable behavior.",
        "mapping": "Behavior slice -> red test -> green code -> refactor proof.",
    },
    "wicked-problems": {
        "display": "Wicked Problems",
        "short": "Probe contested product and architecture work",
        "prompt": "Use $wicked-problems to frame this ambiguous product or architecture change before coding.",
        "concepts": [
            "Wicked problems have no final problem statement or single stopping rule.",
            "Stakeholders value different criteria and every solution changes the situation.",
            "Design rationale preserves why one probe or tradeoff was chosen.",
        ],
        "translation": "Use it to state stakeholders, competing frames, conflicting criteria, and a reversible probe.",
        "misuse": "Do not use wickedness as an excuse to avoid implementing a well-bounded task.",
        "mapping": "Stakeholder conflict -> problem frame -> probe -> rationale record.",
    },
}

SELECTION_ROWS = [
    ("Preserve domain-program mapping while editing code", "programming-as-theory-building", "domain-driven-design, information-hiding"),
    ("Choose a module or API boundary", "information-hiding", "design-by-contract, conways-law"),
    ("Align architecture with teams or ownership", "conways-law", "activity-theory, distributed-cognition"),
    ("Model complex business rules", "domain-driven-design", "programming-as-theory-building"),
    ("Specify API obligations and guarantees", "design-by-contract", "cleanroom-software-engineering"),
    ("Implement behavior test-first", "test-driven-development", "cleanroom-software-engineering, stepwise-refinement"),
    ("Refine a high-level algorithm", "stepwise-refinement", "structured-programming"),
    ("Reason about many possible executions", "abstract-interpretation", "structured-programming"),
    ("Simplify without erasing domain rules", "essential-complexity", "domain-driven-design"),
    ("Improve human-facing APIs or configs", "cognitive-dimensions", "literate-programming"),
    ("Clarify code for maintainers", "literate-programming", "programming-as-theory-building"),
    ("Untangle messy incidents or failures", "sensemaking", "reflective-practice, double-loop-learning"),
    ("Adapt a plan after new evidence", "situated-action", "reflective-practice"),
    ("Reframe a surprising debug result", "reflective-practice", "sensemaking"),
    ("Prevent repeated failures", "double-loop-learning", "sensemaking"),
    ("Analyze workflow-level contradictions", "activity-theory", "distributed-cognition"),
    ("Trace operational knowledge across artifacts", "distributed-cognition", "activity-theory"),
    ("Handle contested product or architecture work", "wicked-problems", "sensemaking"),
    ("Use a recurring design solution", "design-patterns", "information-hiding, domain-driven-design"),
    ("Build high-reliability increments", "cleanroom-software-engineering", "design-by-contract"),
    ("Refactor tangled control flow", "structured-programming", "test-driven-development"),
]


def parse_catalog() -> list[dict[str, str]]:
    text = CATALOG.read_text(encoding="utf-8")
    matches = list(re.finditer(r"^  - slug: ([a-z0-9-]+)\n", text, re.MULTILINE))
    entries: list[dict[str, str]] = []
    for index, match in enumerate(matches):
        block = text[match.start() : matches[index + 1].start() if index + 1 < len(matches) else len(text)]
        entry = {"slug": match.group(1)}
        for key in ["skill_name", "branch", "status", "agent_use"]:
            found = re.search(rf"^    {key}: \"?([^\n\"]+)\"?$", block, re.MULTILINE)
            if found:
                entry[key] = found.group(1)
        for section, prefix in [("primary_source", "primary"), ("supporting_source", "supporting"), ("model_skill", "model")]:
            section_match = re.search(rf"^    {section}:\n((?:      .+\n)+)", block, re.MULTILINE)
            if not section_match:
                continue
            section_text = section_match.group(1)
            for key in ["title", "author", "year", "url"]:
                found = re.search(rf"^      {key}: \"?([^\n\"]+)\"?$", section_text, re.MULTILINE)
                if found:
                    entry[f"{prefix}_{key}"] = found.group(1)
        entries.append(entry)
    return entries


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def write_agents(entry: dict[str, str]) -> None:
    slug = entry["slug"]
    data = SKILL_DATA[slug]
    agents_dir = SKILLS / slug / "agents"
    agents_dir.mkdir(parents=True, exist_ok=True)
    text = "\n".join(
        [
            "interface:",
            f"  display_name: {yaml_quote(data['display'])}",
            f"  short_description: {yaml_quote(data['short'])}",
            f"  default_prompt: {yaml_quote(data['prompt'])}",
            "policy:",
            "  allow_implicit_invocation: true",
            "",
        ]
    )
    (agents_dir / "openai.yaml").write_text(text, encoding="utf-8")


def write_source_notes(entry: dict[str, str]) -> None:
    slug = entry["slug"]
    data = SKILL_DATA[slug]
    lines = [
        f"# Source Notes: {slug}",
        "",
        f"- Primary source: {entry.get('primary_title', '')}",
        f"- Author: {entry.get('primary_author', '')}",
        f"- Year: {entry.get('primary_year', '')}",
        f"- URL: {entry.get('primary_url', '')}",
    ]
    if entry.get("supporting_title"):
        lines.extend(
            [
                f"- Supporting source: {entry.get('supporting_title')}",
                f"- Supporting URL: {entry.get('supporting_url')}",
            ]
        )
    if entry.get("model_title"):
        lines.extend(
            [
                f"- Model skill: {entry.get('model_title')}",
                f"- Model skill URL: {entry.get('model_url')}",
            ]
        )
    if data.get("fallbacks"):
        lines.extend(["", "## Fallback Sources", ""])
        for title, url in data["fallbacks"]:
            lines.append(f"- {title}: {url}")
    lines.extend(
        [
            "",
            "## Key Concepts",
            "",
        ]
    )
    lines.extend(f"- {concept}" for concept in data["concepts"])
    lines.extend(
        [
            "",
            "## Agent Translation",
            "",
            data["translation"],
            "",
            "## Common Misuse",
            "",
            data["misuse"],
            "",
            "## Source Mapping",
            "",
            data["mapping"],
            "",
            "## Drafting Notes",
            "",
            "Keep the runnable skill concise. Move detailed theory reminders here, and",
            "only load this file when the task needs source grounding or misuse checks.",
            "",
        ]
    )
    path = SKILLS / slug / "references" / "source-notes.md"
    path.write_text("\n".join(lines), encoding="utf-8")


def write_selection_guide(entries: list[dict[str, str]]) -> None:
    lines = [
        "# Theory Skill Selection Guide",
        "",
        "Use this guide before loading a specific skill when several theories could apply.",
        "Prefer the primary skill when it names the current problem directly; use the",
        "alternatives when the stop conditions in that skill point elsewhere.",
        "",
        "| Situation | Primary Skill | Alternatives |",
        "| --- | --- | --- |",
    ]
    for situation, primary, alternatives in SELECTION_ROWS:
        lines.append(f"| {situation} | `{primary}` | {alternatives} |")
    lines.extend(
        [
            "",
            "## Boundary Rules",
            "",
            "- If the problem is ambiguous, start with `sensemaking` before choosing a design theory.",
            "- If fresh evidence invalidates the plan, switch to `situated-action` before continuing.",
            "- If a code change is already well bounded, prefer `programming-as-theory-building` and only add a specialized skill for the dominant force.",
            "- If a skill would introduce ceremony for one caller, choose the simpler alternative named in its stop conditions.",
            "",
        ]
    )
    (ROOT / "theories" / "selection-guide.md").write_text("\n".join(lines), encoding="utf-8")


def write_readme(entries: list[dict[str, str]]) -> None:
    lines = [
        "# SkillRoot",
        "",
        "Theory-grounded skills for coding agents.",
        "",
        "This repository collects one skill per theory. Each skill translates a",
        "software, organizational, design, or cognition theory into a compact agent",
        "workflow with source notes and UI metadata.",
        "",
        "## Repository Rules",
        "",
        "- Put installable skills under `skills/<skill-name>/SKILL.md`.",
        "- Keep each skill short and procedural. Put source grounding and misuse notes in `skills/<skill-name>/references/source-notes.md`.",
        "- Add one theory or skill per branch, then merge through `main` after validation.",
        "- Record research candidates in `theories/catalog.yml` before generating a skill.",
        "- Keep `agents/openai.yaml` in sync with `SKILL.md` for every skill.",
        "- Cite primary papers, books, or stable publisher pages where possible, and add fallback sources when the primary URL is fragile.",
        "",
        "## Current Skills",
        "",
        "| Skill | Focus | Source |",
        "| --- | --- | --- |",
    ]
    for entry in sorted(entries, key=lambda item: item["slug"]):
        slug = entry["slug"]
        title = SKILL_DATA[slug]["display"]
        focus = SKILL_DATA[slug]["short"]
        source = entry.get("primary_title", "")
        lines.append(f"| [{title}](skills/{slug}/SKILL.md) | {focus} | {source} |")
    lines.extend(
        [
            "",
            "## Choose A Skill",
            "",
            "Start with [the selection guide](theories/selection-guide.md) when multiple",
            "skills could apply. The guide maps common coding situations to the most",
            "likely theory and alternatives.",
            "",
            "## Add A Theory Skill",
            "",
            "Create a branch for the theory:",
            "",
            "```bash",
            "git switch main",
            "git pull --ff-only",
            "git switch -c skill/<theory-slug>",
            "```",
            "",
            "Generate the skill skeleton from the catalog:",
            "",
            "```bash",
            "python3 scripts/new_theory_skill.py <theory-slug>",
            "```",
            "",
            "Synchronize generated docs and metadata:",
            "",
            "```bash",
            "python3 scripts/sync_skill_artifacts.py",
            "```",
            "",
            "Validate before committing:",
            "",
            "```bash",
            "python3 scripts/validate_skills.py",
            "```",
            "",
            "Commit and push:",
            "",
            "```bash",
            "git add skills/<theory-slug> theories/catalog.yml README.md theories/selection-guide.md",
            "git commit -m \"Add <theory-slug> skill\"",
            "git push -u origin skill/<theory-slug>",
            "```",
            "",
        ]
    )
    (ROOT / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    entries = parse_catalog()
    missing = sorted({entry["slug"] for entry in entries}.difference(SKILL_DATA))
    extra = sorted(set(SKILL_DATA).difference(entry["slug"] for entry in entries))
    if missing or extra:
        raise SystemExit(f"SKILL_DATA mismatch missing={missing} extra={extra}")
    for entry in entries:
        write_agents(entry)
        write_source_notes(entry)
    write_selection_guide(entries)
    write_readme(entries)
    print(f"synchronized {len(entries)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
