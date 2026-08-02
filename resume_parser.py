import PyPDF2


def extract_text(pdf_path):
    text = ""

    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text


SKILLS = [
    "python",
    "machine learning",
    "sql",
    "html",
    "css",
    "flask",
    "java",
    "c++",
    "git",
    "github"
]


def extract_skills(text):

    text = text.lower()

    found = []

    for skill in SKILLS:
        if skill in text:
            found.append(skill)

    return found


def calculate_score(found_skills):

    total_skills = len(SKILLS)

    score = int((len(found_skills) / total_skills) * 100)

    missing = []

    for skill in SKILLS:
        if skill not in found_skills:
            missing.append(skill)

    return score, missing


def recommend_career(skills):

    skills = [skill.lower() for skill in skills]

    if "machine learning" in skills and "python" in skills:
        return "🤖 AI Engineer"

    elif "python" in skills and "sql" in skills:
        return "📊 Data Scientist"

    elif "html" in skills and "css" in skills:
        return "🌐 Frontend Developer"

    elif "python" in skills:
        return "💻 Python Developer"

    elif "java" in skills:
        return "☕ Java Developer"

    else:
        return "📚 Learn more skills to get a recommendation."


def learning_roadmap(career):

    roadmap = {

        "🤖 AI Engineer": [
            "Python Advanced",
            "NumPy",
            "Pandas",
            "Machine Learning",
            "Deep Learning",
            "Flask / FastAPI",
            "Build AI Projects",
            "Deploy on Render"
        ],

        "📊 Data Scientist": [
            "Python",
            "SQL",
            "Statistics",
            "Pandas",
            "Matplotlib",
            "Machine Learning",
            "Power BI"
        ],

        "🌐 Frontend Developer": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Tailwind CSS",
            "Git",
            "GitHub"
        ],

        "💻 Python Developer": [
            "Python",
            "OOP",
            "Flask",
            "SQL",
            "REST API",
            "Git",
            "GitHub"
        ],

        "☕ Java Developer": [
            "Java",
            "OOP",
            "Spring Boot",
            "MySQL",
            "Git",
            "GitHub"
        ]
    }

    return roadmap.get(
        career,
        [
            "Programming Basics",
            "Python",
            "Git & GitHub",
            "Projects"
        ]
    )