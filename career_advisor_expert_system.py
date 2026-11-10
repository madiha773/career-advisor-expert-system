"""
=============================================================
  CAREER ADVISOR EXPERT SYSTEM
  Course  : Knowledge Representation and Reasoning (KRR)
  Domain  : Career / Field of Study Advisor
  Method  : Rule-Based Expert System with Forward Chaining
=============================================================
"""

import time

# ─────────────────────────────────────────────────────────────
# KNOWLEDGE BASE
# Each rule has:
#   - id         : unique rule identifier
#   - conditions : dict of {trait: True/False} that must ALL match
#   - career     : recommended career
#   - reason     : explanation shown to user
# ─────────────────────────────────────────────────────────────

KNOWLEDGE_BASE = [

    # ── Software / CS ──────────────────────────────────────
    {
        "id": "R01",
        "conditions": {"loves_coding": True, "logical_thinking": True, "math_interest": True},
        "career": "Software Engineer / Computer Scientist",
        "reason": "You enjoy coding, think logically, and have strong math skills — a perfect match for software development and computer science."
    },
    {
        "id": "R02",
        "conditions": {"loves_coding": True, "creative_thinking": True, "math_interest": False},
        "career": "Front-End Developer / UI-UX Designer",
        "reason": "You like coding and creativity but are not heavily into math — front-end development or UI/UX design is ideal for you."
    },
    {
        "id": "R03",
        "conditions": {"loves_coding": True, "data_interest": True, "math_interest": True},
        "career": "Data Scientist / Machine Learning Engineer",
        "reason": "Coding + data + math = the foundation of Data Science and AI/ML careers."
    },

    # ── Business / Management ──────────────────────────────
    {
        "id": "R04",
        "conditions": {"leadership_skills": True, "communication_skills": True, "business_interest": True},
        "career": "Business Manager / Entrepreneur",
        "reason": "Leadership, communication, and business interest together point strongly toward management or starting your own venture."
    },
    {
        "id": "R05",
        "conditions": {"business_interest": True, "math_interest": True, "data_interest": True},
        "career": "Financial Analyst / Accountant",
        "reason": "Business + math + data analysis skills align perfectly with finance and accounting careers."
    },
    {
        "id": "R06",
        "conditions": {"communication_skills": True, "creative_thinking": True, "business_interest": True},
        "career": "Marketing / Digital Marketing Specialist",
        "reason": "Creativity + communication + business sense = a strong marketing career path."
    },

    # ── Engineering ────────────────────────────────────────
    {
        "id": "R07",
        "conditions": {"math_interest": True, "logical_thinking": True, "loves_building": True, "loves_coding": False},
        "career": "Civil / Mechanical / Electrical Engineer",
        "reason": "You love math, logical thinking, and building things physically — traditional engineering is your domain."
    },
    {
        "id": "R08",
        "conditions": {"loves_coding": True, "loves_building": True, "logical_thinking": True},
        "career": "Embedded Systems / Hardware Engineer",
        "reason": "Coding + building hardware + logical thinking = embedded systems or hardware engineering."
    },

    # ── Medicine / Science ─────────────────────────────────
    {
        "id": "R09",
        "conditions": {"science_interest": True, "helping_others": True, "patience": True},
        "career": "Doctor / Medical Professional",
        "reason": "Science knowledge, desire to help others, and patience are the core traits of a successful doctor."
    },
    {
        "id": "R10",
        "conditions": {"science_interest": True, "research_interest": True, "math_interest": True},
        "career": "Research Scientist / Pharmacist",
        "reason": "Science + research + math = a strong fit for research labs, pharmacology, or academia."
    },

    # ── Arts / Design ──────────────────────────────────────
    {
        "id": "R11",
        "conditions": {"creative_thinking": True, "art_interest": True, "communication_skills": True},
        "career": "Graphic Designer / Animator / Content Creator",
        "reason": "Creativity + art + communication skills open doors in design, animation, and content creation."
    },
    {
        "id": "R12",
        "conditions": {"creative_thinking": True, "art_interest": True, "loves_writing": True},
        "career": "Writer / Journalist / Content Writer",
        "reason": "Creativity + art appreciation + writing talent = journalism, copywriting, or book writing."
    },

    # ── Education / Law ────────────────────────────────────
    {
        "id": "R13",
        "conditions": {"communication_skills": True, "patience": True, "helping_others": True, "leadership_skills": True},
        "career": "Teacher / Professor / Counselor",
        "reason": "Communication, patience, helping nature, and leadership together describe an excellent educator or counselor."
    },
    {
        "id": "R14",
        "conditions": {"logical_thinking": True, "communication_skills": True, "loves_writing": True, "helping_others": True},
        "career": "Lawyer / Legal Advisor",
        "reason": "Logic + communication + writing + helping others = a strong foundation for a legal career."
    },

    # ── Network / Cybersecurity ────────────────────────────
    {
        "id": "R15",
        "conditions": {"loves_coding": True, "logical_thinking": True, "security_interest": True},
        "career": "Cybersecurity Expert / Ethical Hacker",
        "reason": "Coding + logical thinking + interest in security = a career in cybersecurity or ethical hacking."
    },

    # ── Psychology / Social Work ───────────────────────────
    {
        "id": "R16",
        "conditions": {"helping_others": True, "communication_skills": True, "science_interest": False, "business_interest": False},
        "career": "Psychologist / Social Worker / HR Specialist",
        "reason": "Helping mindset + strong communication without strict science/business focus = psychology, social work, or HR."
    },

    # ── Game Development ───────────────────────────────────
    {
        "id": "R17",
        "conditions": {"loves_coding": True, "creative_thinking": True, "art_interest": True},
        "career": "Game Developer / Creative Technologist",
        "reason": "Coding + creativity + art = game development or creative tech roles."
    },

    # ── Cloud / DevOps ─────────────────────────────────────
    {
        "id": "R18",
        "conditions": {"loves_coding": True, "logical_thinking": True, "loves_building": True},
        "career": "Cloud Engineer / DevOps Specialist",
        "reason": "Coding + logic + building/deploying systems = cloud computing or DevOps career path."
    },

    # ── Teaching + Tech ────────────────────────────────────
    {
        "id": "R19",
        "conditions": {"loves_coding": True, "communication_skills": True, "helping_others": True},
        "career": "IT Trainer / Technical Content Creator / EdTech Developer",
        "reason": "Technical skills + teaching/helping personality = IT training, YouTube tech content, or EdTech platforms."
    },

    # ── General Business ───────────────────────────────────
    {
        "id": "R20",
        "conditions": {"business_interest": True, "leadership_skills": True, "creative_thinking": True},
        "career": "Product Manager / Startup Founder",
        "reason": "Business mindset + leadership + creativity = product management or building your own startup."
    },
]


# ─────────────────────────────────────────────────────────────
# QUESTION BANK
# Maps each trait to a user-friendly question.
# All traits used in KNOWLEDGE_BASE conditions are listed here.
# ─────────────────────────────────────────────────────────────

QUESTIONS = {
    "loves_coding"        : "Do you enjoy writing code or programming?",
    "math_interest"       : "Do you like Mathematics or working with numbers?",
    "logical_thinking"    : "Are you good at logical / analytical thinking?",
    "creative_thinking"   : "Do you consider yourself a creative person?",
    "data_interest"       : "Are you interested in analyzing data or finding patterns?",
    "business_interest"   : "Are you interested in business, markets, or economics?",
    "leadership_skills"   : "Do you have leadership skills or enjoy leading a team?",
    "communication_skills": "Are you good at communication and public speaking?",
    "loves_building"      : "Do you enjoy building / designing physical things?",
    "science_interest"    : "Are you interested in Biology, Chemistry, or Physics?",
    "helping_others"      : "Do you genuinely enjoy helping or supporting other people?",
    "patience"            : "Would you say you are a patient person?",
    "research_interest"   : "Do you enjoy researching, studying, or academic work?",
    "art_interest"        : "Are you interested in art, design, or visual creativity?",
    "loves_writing"       : "Do you enjoy writing — stories, essays, or articles?",
    "security_interest"   : "Are you curious about cybersecurity or hacking concepts?",
}


# ─────────────────────────────────────────────────────────────
# INFERENCE ENGINE  —  Forward Chaining
# Matches user facts against every rule in the knowledge base.
# Returns a list of all matching (career, reason, rule_id) tuples.
# ─────────────────────────────────────────────────────────────

def run_inference(user_facts: dict) -> list:
    """
    Forward Chaining Inference:
    Start from known facts (user answers) and fire every rule
    whose conditions are fully satisfied.
    Returns all matched conclusions sorted by match count.
    """
    matched_results = []

    for rule in KNOWLEDGE_BASE:
        conditions = rule["conditions"]
        # Check if every condition in this rule matches the user's facts
        all_match = all(
            user_facts.get(trait) == expected_value
            for trait, expected_value in conditions.items()
        )
        if all_match:
            matched_results.append({
                "rule_id" : rule["id"],
                "career"  : rule["career"],
                "reason"  : rule["reason"],
                "matched" : len(conditions),   # how many conditions matched
            })

    # Sort by number of conditions matched (more specific = higher priority)
    matched_results.sort(key=lambda x: x["matched"], reverse=True)
    return matched_results


# ─────────────────────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────────────────────

def get_yes_no(question: str, q_num: int, total: int) -> bool:
    """Ask a yes/no question and return True for yes, False for no."""
    while True:
        answer = input(f"  Q{q_num}/{total}  {question} (yes/no): ").strip().lower()
        if answer in ("yes", "y"):
            return True
        elif answer in ("no", "n"):
            return False
        else:
            print("       ⚠  Please type 'yes' or 'no'.")


def print_separator(char="─", width=60):
    print(char * width)


def slow_print(text: str, delay: float = 0.03):
    """Print text character by character for a typing effect."""
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()


# ─────────────────────────────────────────────────────────────
# MAIN PROGRAM  —  Entry Point
# ─────────────────────────────────────────────────────────────

def main():
    # ── Welcome Banner ──────────────────────────────────────
    print()
    print_separator("═")
    slow_print("  🎓  CAREER ADVISOR EXPERT SYSTEM")
    print("       Knowledge Representation & Reasoning — KRR Project")
    print("       Method : Rule-Based Forward Chaining")
    print(f"       Rules  : {len(KNOWLEDGE_BASE)}  |  Traits: {len(QUESTIONS)}")
    print_separator("═")
    print()
    print("  Answer a few simple YES / NO questions.")
    print("  The system will analyze your personality and interests,")
    print("  then recommend the most suitable career path for you.")
    print()
    input("  Press ENTER to begin... ")
    print()

    # ── Collect User Answers ─────────────────────────────────
    user_facts = {}
    total_q    = len(QUESTIONS)
    print_separator()
    print("  SECTION: Your Interests & Personality Traits")
    print_separator()
    print()

    for i, (trait, question) in enumerate(QUESTIONS.items(), start=1):
        user_facts[trait] = get_yes_no(question, i, total_q)

    # ── Run Inference Engine ─────────────────────────────────
    print()
    print_separator()
    slow_print("  ⚙  Inference Engine running — matching your profile to rules...")
    time.sleep(0.8)
    print_separator()
    print()

    results = run_inference(user_facts)

    # ── Display Results ──────────────────────────────────────
    if not results:
        # No rule matched — show partial analysis
        print("  ⚠  No exact career rule matched your profile.")
        print()
        print("  This may happen because your interests are very diverse")
        print("  or your combination is unique. Some observations:")
        print()

        # Count positives for rough guidance
        yes_count = sum(1 for v in user_facts.values() if v)
        if yes_count <= 4:
            print("  → You answered YES to very few traits. Try exploring more fields.")
        elif user_facts.get("helping_others") and user_facts.get("science_interest"):
            print("  → You show medical/social traits. Consider healthcare or social work.")
        else:
            print("  → Consider career counseling with a professional advisor.")

    else:
        # Primary recommendation
        top = results[0]
        print("  ✅  ANALYSIS COMPLETE")
        print()
        print_separator("─")
        slow_print(f"  🏆  PRIMARY RECOMMENDATION  [{top['rule_id']}]")
        print_separator("─")
        slow_print(f"  Career  :  {top['career']}", delay=0.02)
        print()
        slow_print(f"  Why     :  {top['reason']}", delay=0.015)
        print()

        # Secondary recommendations (if any)
        if len(results) > 1:
            print_separator("─")
            print("  📌  ALTERNATIVE CAREER OPTIONS")
            print_separator("─")
            for alt in results[1:4]:   # Show up to 3 alternatives
                print(f"  [{alt['rule_id']}]  {alt['career']}")
                print(f"        {alt['reason']}")
                print()

    # ── Show Working Memory (transparency) ───────────────────
    print_separator()
    print("  📋  YOUR PROFILE SUMMARY  (Working Memory)")
    print_separator()
    yes_traits = [q for trait, q in QUESTIONS.items() if user_facts.get(trait)]
    no_traits  = [q for trait, q in QUESTIONS.items() if not user_facts.get(trait)]

    print("  Strengths / Interests:")
    if yes_traits:
        for t in yes_traits:
            print(f"    ✓  {t}")
    else:
        print("    (none selected)")

    print()
    print("  Not applicable:")
    if no_traits:
        for t in no_traits[:5]:   # Show only first 5 to keep it brief
            print(f"    ✗  {t}")
        if len(no_traits) > 5:
            print(f"    ...and {len(no_traits) - 5} more")

    # ── Inference Statistics ─────────────────────────────────
    print()
    print_separator()
    print(f"  📊  Rules evaluated : {len(KNOWLEDGE_BASE)}")
    print(f"       Rules matched   : {len(results)}")
    print(f"       Facts collected : {len(user_facts)}")
    print_separator("═")
    print()
    print("  Thank you for using the Career Advisor Expert System!")
    print("  Good luck with your future! 🚀")
    print()
    print_separator("═")

    # ── Restart Option ───────────────────────────────────────
    again = input("\n  Run again for another profile? (yes/no): ").strip().lower()
    if again in ("yes", "y"):
        print("\n" * 2)
        main()
    else:
        print("\n  Goodbye! 👋\n")


# ─────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
