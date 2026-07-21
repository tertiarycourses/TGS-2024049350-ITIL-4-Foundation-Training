#!/usr/bin/env python3
"""
ITIL 4 Foundation Training (TGS-2024049350) — WSQ assessment generator.

Mirrors the ORIGINAL papers pulled from the TMS (reference/tms/):
  * Written Assessment (SAQ) — 6 open-ended questions, codes K1..K6, 1 hour
  * Case Study (CS)          — 5 questions, codes A1..A8, 1 hour

Instrument, question count, codes and timings are preserved exactly; only the
content is rewritten from this course's slides, Learner Guide and activities.

Layout enforced by the WSQ house standard:
  page 1  — WSQ cover page naming the instrument (no version-control record)
  page 2  — Trainee Information + Instructions to Candidate + Grading block ONLY
  page 3+ — scenario and questions
Answer keys: cover page, then model answers.

Outputs four DOCX into assessment/.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.join(HERE, ".claude", "skills")
sys.path.insert(0, os.path.join(SKILL, "courseware-build", "build"))
sys.path.insert(0, os.path.join(SKILL, "tertiary-lesson-plan"))

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH as AL
import course_data as C

# prodoc gives us the house cover page / page numbers
try:
    sys.path.insert(0, os.path.join(SKILL, "courseware-build", "build"))
    import prodoc
except ImportError:
    prodoc = None

OUT = os.path.join(HERE, "assessment")
ASSETS = os.path.join(SKILL, "courseware-build", "assets")
TITLE = C.TITLE
COURSE_CODE = C.COURSE_CODE
VER = "v12"

DARK = RGBColor(0x16, 0x1B, 0x26); BRAND = RGBColor(0x1F, 0x6F, 0xEB); GREY = RGBColor(0x55, 0x5B, 0x66)

LMS = "https://lms-tms.tertiaryinfotech.com/"


# ================================================================ doc helpers
def new_doc():
    d = Document(); n = d.styles["Normal"]; n.font.name = "Arial"; n.font.size = Pt(11)
    if prodoc: prodoc.style_headings(d)
    return d


def line(d, text="", bold=False, size=11, color=DARK, after=6, align=None):
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(after)
    if align is not None: p.alignment = align
    r = p.add_run(text); r.bold = bold; r.font.size = Pt(size)
    r.font.color.rgb = color; r.font.name = "Arial"
    return p


def runs(d, segments, after=6, style=None):
    p = d.add_paragraph(style=style); p.paragraph_format.space_after = Pt(after)
    for text, bold in segments:
        r = p.add_run(text); r.bold = bold; r.font.size = Pt(11)
        r.font.name = "Arial"; r.font.color.rgb = DARK
    return p


def bullet(d, text):
    return runs(d, [(text, False)], after=3, style="List Bullet")


def _hr(d, color="9AA3AF"):
    """A horizontal rule drawn as a paragraph bottom border.

    A row of underscores wraps when it exceeds the text width, leaving an
    orphan "______" fragment on the following line. A border cannot wrap.
    """
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    p = d.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(10)
    pPr = p._p.get_or_add_pPr()
    borders = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), color)
    borders.append(bottom)
    pPr.append(borders)
    return p


def cover(d, instrument):
    """Page 1 — WSQ house cover page naming the instrument. No version-control record."""
    if prodoc:
        prodoc.add_cover_page(d, instrument, TITLE, VER.lstrip("v"),
                              org_logo=os.path.join(ASSETS, "tertiary-infotech-logo.png"),
                              course_logo=None, course_code=COURSE_CODE)
    else:
        line(d, TITLE, bold=True, size=18, color=BRAND, after=6, align=AL.CENTER)
        line(d, instrument, bold=True, size=14, after=4, align=AL.CENTER)
        line(d, f"WSQ Course Code: {COURSE_CODE}", size=11, color=GREY, after=2, align=AL.CENTER)
        line(d, f"{C.ORG}  ·  {C.UEN}", size=11, color=GREY, after=2, align=AL.CENTER)
        d.add_page_break()


def admin_page(d, minutes, instrument_short):
    """Page 2 — Trainee Information + Instructions + Grading block, and nothing else."""
    line(d, "A: Trainee Information", bold=True, size=12, after=6)
    line(d, "Trainee Name (as per NRIC): _______________________________", after=6)
    line(d, "Last 3 digits and alphabet of NRIC / FIN: _________________", after=6)
    line(d, "Date: __________________", after=14)

    line(d, "B: Instructions to Candidate", bold=True, size=12, after=6)
    for t in [
        "1. This is an individual exercise. No discussion with other candidates is permitted.",
        "2. This is an open book assessment. Open book includes the course slides, the Learner Guide "
        "and any approved materials only. Mobile phones and all other materials must be placed under "
        "the table or on the floor.",
        f"3. A total of {minutes} is given to complete this {instrument_short}.",
        "4. Answer ALL questions in your own words in the space provided. Answers copied verbatim "
        "from the course materials will not be accepted.",
        "5. Write legibly using a black or blue pen. Do not use liquid paper or correction tape — "
        "cross out neatly and rewrite instead.",
        "6. You will be assessed as Competent (C) or Not Yet Competent (NYC). To be assessed as "
        "Competent you must answer all questions to the required standard.",
        "7. If you are assessed Not Yet Competent, you are entitled to one re-assessment. An appeal "
        "process is available if you disagree with the outcome — speak to your trainer or the "
        "course administrator.",
        "8. Submit your completed answers on the document provided when time is up.",
    ]:
        line(d, t, after=4)
    p = d.add_paragraph(); p.paragraph_format.space_after = Pt(16)
    r = p.add_run("9. Upload your completed answers to the LMS at ")
    r.font.size = Pt(11); r.font.name = "Arial"
    r2 = p.add_run(LMS); r2.font.size = Pt(11); r2.font.name = "Arial"
    r2.font.color.rgb = BRAND; r2.underline = True      # a hyperlink — underlined by design

    # House standard: the block is headed "Grading" and lives HERE, on page 2.
    # There is NO "For Official Use Only" block at the back of the paper.
    # A bottom BORDER separates it — not a row of underscores, which wraps and
    # leaves an orphan fragment on the next line.
    _hr(d)
    line(d, "C: Grading", bold=True, size=12, after=8)
    line(d, "Grade:            C  /  NYC          (delete as appropriate)", after=10)
    line(d, "Assessor Name:", after=10)
    line(d, "Assessor NRIC:", after=10)
    line(d, "Date:", after=10)
    line(d, "Assessor Signature:", after=4)
    d.add_page_break()


def _set_cell_border(cell, color="9AA3AF", sz="8"):
    """Draw all four borders on a table cell."""
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    tcPr = cell._tc.get_or_add_tcPr()
    borders = OxmlElement("w:tcBorders")
    for edge in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), sz)
        el.set(qn("w:color"), color)
        borders.append(el)
    tcPr.append(borders)


def answer_lines(d, n=5):
    """A single bordered answer box sized to roughly n writing lines.

    House rule: every question carries a BORDERED answer box — not underscore
    rules, which wrap unpredictably and render as broken half-lines.
    """
    line(d, "Answer:", bold=True, color=GREY, after=3)
    tbl = d.add_table(rows=1, cols=1)
    cell = tbl.rows[0].cells[0]
    _set_cell_border(cell)
    cell.text = ""
    # blank paragraphs give the candidate writing room inside the box
    for i in range(max(n, 3)):
        p = cell.paragraphs[0] if i == 0 else cell.add_paragraph()
        p.paragraph_format.space_after = Pt(9)
        r = p.add_run(""); r.font.size = Pt(11); r.font.name = "Arial"
    d.add_paragraph().paragraph_format.space_after = Pt(6)


def finish(d, path):
    if prodoc:
        prodoc.add_page_numbers(d)
    d.save(path)
    return path


# ================================================================ WRITTEN (SAQ) — 6 Q, K1..K6
# (code, context, question, [model answer points], source)
WRITTEN = [
    ("K1",
     "Your company, a regional logistics provider, has experienced repeated disruptions to its "
     "warehouse management system. Management wants to understand how the organisation's own "
     "structure, roles and working practices contribute to the problem.",
     "Which dimension of ITIL 4 addresses the activities organizations undertake, and how they are "
     "organized to efficiently and effectively enable value co-creation for stakeholders? Explain what "
     "this dimension covers.",
     ["The value streams and processes dimension.",
      "It is concerned with how the various parts of the organisation work together, in an integrated "
      "and coordinated way, to enable value creation through products and services.",
      "It defines the activities, workflows, controls and procedures needed to achieve agreed objectives.",
      "A value stream is a series of steps an organisation uses to create and deliver products and "
      "services to a consumer; a process is a set of activities that transforms inputs into outputs.",
      "Accept 'organizations and people' ONLY if the candidate explicitly argues roles/responsibilities "
      "and justifies it — the stem's wording ('activities ... and how they are organized') points to "
      "value streams and processes."],
     "Topic 3 — The Four Dimensions of Service Management"),

    ("K2",
     "Your IT department is deploying a critical new cloud-based application. Several teams — "
     "infrastructure, security, applications and the service desk — each own a part of the deployment, "
     "and previous rollouts failed because each team optimised only its own step.",
     "Which ITIL 4 guiding principle focuses on working in an integrated way, approaching activities as "
     "related to the whole rather than as separate parts? Explain what applying it would require here.",
     ["The 'think and work holistically' principle.",
      "No service, practice, process, department or supplier stands alone; the outputs the organisation "
      "delivers depend on all of them working together as an integrated whole.",
      "Applying it requires establishing an understanding of how all parts of the organisation work "
      "together, and working towards end-to-end delivery rather than local optimisation.",
      "In this scenario: plan the deployment across all four dimensions and all involved teams, and "
      "measure success on the end-to-end outcome, not on each team's individual step."],
     "Topic 2 — ITIL Guiding Principles"),

    ("K3",
     "Your organization faces complex decisions regarding technology investments and needs authoritative "
     "guidance that will hold regardless of how its strategy or priorities change.",
     "Which component within the ITIL service value system is intended to make recommendations that "
     "guide an organization in all circumstances? Name it and explain its defining characteristic.",
     ["The guiding principles.",
      "A guiding principle is a recommendation that guides an organisation in ALL circumstances, "
      "regardless of changes in its goals, strategies, type of work or management structure.",
      "This universality is the defining characteristic — the principles do not change when the "
      "organisation's situation changes.",
      "The SVS components are: guiding principles, governance, the service value chain, practices and "
      "continual improvement. Governance directs and controls; the guiding principles recommend."],
     "Topic 4 — The Service Value System / Topic 2"),

    ("K4",
     "Your organization is planning an extensive upgrade to its customer service portal. Effective "
     "communication, transparency and continuous alignment with customer expectations throughout the "
     "upgrade are critical to its success.",
     "Which service value chain activity provides a good understanding of stakeholder needs and promotes "
     "transparency, continual engagement and good relationships with all stakeholders?",
     ["The 'engage' value chain activity.",
      "Its purpose is to provide a good understanding of stakeholder needs, transparency, and continual "
      "engagement and good relationships with all stakeholders.",
      "It covers all stakeholders — customers, users, suppliers, partners and internal groups.",
      "In this scenario, engage is what keeps the upgrade aligned to customer expectations from "
      "requirements through to delivery and feedback."],
     "Topic 4 — The Service Value System"),

    ("K5",
     "During a significant software update, your technical team encounters an urgent problem that could "
     "delay the project. Under time pressure the team proposes dropping several planned features to hit "
     "the original date.",
     "What describes the 'focus on value' principle, and how would it guide the team's decision here?",
     ["Everything the organisation does should link back, directly or indirectly, to value for itself, "
      "its customers and its other stakeholders.",
      "Applying it means knowing who is being served, what is being delivered or improved for them, and "
      "what the consumer actually values.",
      "Value takes many forms — revenue, customer loyalty, reduced cost, reduced risk.",
      "In this scenario: decide which features to drop based on which ones the service consumer actually "
      "values, rather than dropping whatever is easiest or hitting the date for its own sake."],
     "Topic 2 — ITIL Guiding Principles"),

    ("K6",
     "Your software development team is launching a major application update intended to improve "
     "customer satisfaction through better functionality, reliability and performance, delivered in line "
     "with market demands and timelines.",
     "Which service value chain activity ensures that products and services continually meet stakeholder "
     "expectations for quality, cost and time to market?",
     ["The 'design and transition' value chain activity.",
      "Its purpose is to ensure that products and services continually meet stakeholder expectations for "
      "quality, cost and time to market.",
      "It covers the design of the service and its transition into live use — including testing, "
      "validation and release readiness.",
      "Distinguish it from 'obtain/build' (ensuring components are available and meet specifications) "
      "and 'deliver and support' (delivering and supporting to agreed specifications)."],
     "Topic 4 — The Service Value System"),
]


# ================================================================ CASE STUDY — 5 Q, A1..A8
# The scenario deliberately uses BrightDesk Services — the SAME organisation as
# Labs 1-8, which learners work through in class. The answer key cites those labs,
# so the assessment must test the scenario they actually practised on.
SCENARIO_TITLE = "Scenario: BrightDesk Services — Employee Digital Workplace"
SCENARIO = (
    "BrightDesk Services provides an Employee Digital Workplace service to a group of corporate "
    "clients across Singapore and the region. Around 12,000 end users at those clients rely on it "
    "every working day for laptops, email, chat, file sharing, and access to HR and finance "
    "applications. BrightDesk employs about 400 staff across its service desk, infrastructure, "
    "applications and client-management teams."
)
SCENARIO_POINTS = [
    "The service bundles a managed laptop, a productivity and collaboration suite, identity and "
    "access management, and a 24x5 service desk with out-of-hours emergency cover.",
    "Client organisations sign a master agreement; each has its own service level targets, and "
    "renewals are negotiated annually against BrightDesk's reported performance.",
    "Demand has grown sharply as client organisations shifted to hybrid working and retired their "
    "own in-house IT support teams.",
    "Cloud licensing has moved to per-user subscription, which lets BrightDesk offer a lower entry "
    "price but exposes it to vendor price changes it does not control.",
    "Data protection obligations differ by client sector — the financial-services clients impose "
    "audit and retention requirements the others do not.",
    "Laptops, imaging and field support are supplied by two contracted third-party providers whose "
    "turnaround times BrightDesk does not directly control.",
    "Users repeatedly say that BrightDesk talks about tickets and systems, while what they care "
    "about is staying productive.",
]
SCENARIO_OFFER_INTRO = (
    "BrightDesk offers the Employee Digital Workplace in three service tiers:"
)
SCENARIO_TABLE = [
    ("Tier", "Price (S$/user/month)", "Inclusions", "Additional Services"),
    ("Standard", "35 – 55",
     "Managed laptop; email, chat and file sharing; service desk 9am–6pm",
     "Self-service portal and knowledge base; next-business-day hardware replacement"),
    ("Professional", "56 – 95",
     "Standard tier plus HR and finance application support; service desk 24x5",
     "Named service delivery contact; quarterly service review; 4-hour hardware replacement"),
    ("Enterprise", "96 and above",
     "Professional tier plus identity and access management, and security monitoring",
     "Dedicated service delivery manager; monthly service review; on-site engineer; "
     "priority incident handling"),
]
SCENARIO_TAIL = (
    "Every tier commits to acknowledging a request within 4 working hours. If a user hears nothing "
    "within that window they can call the service desk hotline or use the self-service portal, whose "
    "chatbot escalates to a human agent when it cannot resolve the query.\n\n"
    "The service depends on several supporting systems: an IT service management tool holding "
    "tickets, a device management platform, an identity provider, and the self-service portal "
    "itself. These were introduced at different times and are only partly integrated — a user's "
    "ticket, device record and access rights are currently reconciled by hand when anything "
    "unusual happens. The two contracted hardware providers send delivery confirmations by email, "
    "which service desk staff re-key into the ticketing tool.\n\n"
    "Over the last two quarters the service desk has recorded a rising number of contacts about "
    "requests acknowledged later than the 4-hour commitment. Most are resolved by chasing an "
    "engineer or a supplier directly. Nobody has yet established why the delays recur, and the same "
    "categories of contact keep returning. Team leads report that they cannot see, at any point in "
    "the week, how much work is open against the capacity available to clear it.\n\n"
    "As BrightDesk takes on more clients, there is a growing need for better insight into user "
    "outcomes, service performance and team utilisation. This would let the company direct its "
    "resources to where demand is greatest, and hold both internal teams and external suppliers to "
    "agreed service levels. The IT Director has been tasked with evaluating a service management "
    "solution to address this need."
)

# (label, codes, prompt, answer_lines)
CS_Q = [
    ("Question 1", "A1",
     "Based on the scenario above, what are examples of opportunity and value from an ITIL context? "
     "Identify each clearly and explain the difference between them.", 8),
    ("Question 2", "A2",
     "From an ITIL context, identify and explain the external factors that BrightDesk is leveraging "
     "to offer its Employee Digital Workplace service to consumers.", 8),
    ("Question 3", "A3, A4",
     "From an ITIL context, identify what is considered the goods, the access to resources and the "
     "service actions within BrightDesk's Employee Digital Workplace service offering.", 9),
    ("Question 4", "A5, A6",
     "If you were BrightDesk's IT Director, what consideration factors would you use to evaluate the "
     "service management solution? Justify your factors.", 9),
    ("Question 5", "A7, A8",
     "State the assumptions you made to justify your answers above, and explain how you would present "
     "and defend your analysis to the rest of the group.", 8),
]

# (label, codes, activity_ref, [model points])
CS_A = [
    ("Question 1", "A1", "Lab 1 — Service Management, Value Co-Creation, Utility and Warranty (Topic 1)", [
        "OPPORTUNITY — options or possibilities to add value for stakeholders, or otherwise improve the "
        "organisation. In this scenario: the shift to hybrid working; client organisations retiring "
        "their own in-house IT support teams; per-user cloud subscription licensing allowing a lower "
        "entry price; the chance to win new corporate clients as demand grows.",
        "Opportunity and demand are the INPUTS to the ITIL service value system — they trigger the "
        "activities that lead to the creation of value.",
        "VALUE — the perceived benefits, usefulness and importance of something. Value is co-created "
        "between BrightDesk and its client organisations and their users, not delivered one way.",
        "Value to the user and the client: staying productive; a working laptop and access on day one; "
        "requests acknowledged within 4 working hours; no need to run an in-house IT support team; "
        "predictable per-user cost.",
        "Value to BrightDesk: recurring subscription revenue; annual renewals; client retention; "
        "richer service data with which to improve the service.",
        "KEY DISTINCTION the candidate must show: an opportunity is a possibility the organisation may "
        "pursue; value is the benefit actually co-created once it does. Award the mark where both are "
        "identified AND distinguished.",
    ]),
    ("Question 2", "A2", "Lab 3 — Four Dimensions of Service Management, incl. PESTLE (Topic 3)", [
        "External factors are addressed in ITIL 4 with PESTLE — political, economic, social, "
        "technological, legal and environmental. Service providers do not operate in isolation.",
        "ECONOMIC — client organisations are retiring in-house IT support teams to convert fixed staff "
        "cost into a predictable per-user charge; per-user cloud subscription licensing lets BrightDesk "
        "offer a lower entry price, but exposes it to vendor price changes it does not control.",
        "SOCIAL — the shift to hybrid working has changed where and how users need support, and has "
        "sharply increased demand for a managed digital workplace.",
        "TECHNOLOGICAL — cloud productivity suites, device management platforms and identity providers "
        "make a fully remote managed workplace viable; the self-service portal and chatbot depend on it.",
        "LEGAL — data protection obligations differ by client sector; the financial-services clients "
        "impose audit and retention requirements that constrain how the service is delivered.",
        "Accept POLITICAL and ENVIRONMENTAL factors only where the candidate justifies them from the "
        "scenario — the scenario does not supply obvious examples of either.",
        "Award the mark for correctly categorising factors and linking each to something concrete in the "
        "scenario. The candidate need not use all six PESTLE categories, but must explain those used.",
    ]),
    ("Question 3", "A3, A4", "Lab 1 — Service Management, Value Co-Creation, Utility and Warranty (Topic 1)", [
        "A SERVICE OFFERING is a formal description of one or more services designed to address the needs "
        "of a target consumer group. It may include goods, access to resources, and service actions.",
        "GOODS — supplied to the consumer; ownership is TRANSFERRED to the consumer, who takes "
        "responsibility for future use. In this scenario: any hardware or accessories transferred "
        "outright to the client. Note the managed laptop is arguably NOT goods — it remains "
        "BrightDesk's asset and is returned; credit either reading if the candidate justifies it.",
        "ACCESS TO RESOURCES — ownership is NOT transferred; access is granted or licensed under agreed "
        "terms and conditions. In this scenario: the managed laptop provided for the contract term; the "
        "productivity and collaboration suite licensed per user; access to the self-service portal and "
        "knowledge base; access to the service desk hotline; identity and access management (Enterprise).",
        "SERVICE ACTIONS — actions performed by the service provider to address a consumer need, "
        "performed according to an agreement. In this scenario: staffing the service desk 9am–6pm or "
        "24x5; acknowledging requests within 4 working hours; imaging and replacing hardware; supporting "
        "the HR and finance applications; security monitoring; the quarterly or monthly service review; "
        "the named contact or dedicated service delivery manager's activities.",
        "KEY DISTINCTION the candidate must show: goods transfer ownership; access to resources does NOT "
        "transfer ownership; service actions are performed BY the provider. Award marks where each "
        "category is correctly populated from the scenario, not merely defined.",
    ]),
    ("Question 4", "A5, A6", "Lab 3 — Four Dimensions of Service Management (Topic 3)", [
        "A strong answer structures the consideration factors using the FOUR DIMENSIONS of service "
        "management, since a solution must be evaluated holistically.",
        "ORGANIZATIONS AND PEOPLE — will service desk, infrastructure and applications staff adopt it? "
        "What training is required? Are the roles, responsibilities and competencies to operate it in "
        "place? Does it fit BrightDesk's culture, given users already say it talks about tickets rather "
        "than productivity?",
        "INFORMATION AND TECHNOLOGY — is it compatible with the current architecture (ITSM tool, device "
        "management platform, identity provider, self-service portal)? Will it close the manual "
        "reconciliation gap between ticket, device record and access rights? Does it meet the "
        "financial-services clients' audit and retention requirements? Is the data it produces actually "
        "the insight the IT Director was asked for — user outcomes, service performance, team utilisation?",
        "PARTNERS AND SUPPLIERS — vendor viability and support model; how it handles the two contracted "
        "hardware providers whose turnaround BrightDesk does not control; whether it can replace the "
        "re-keying of supplier emails; the dependency and lock-in the relationship creates.",
        "VALUE STREAMS AND PROCESSES — how will it fit the end-to-end journey from user contact through "
        "fulfilment to closure? Will it support or disrupt the 4-working-hour acknowledgement commitment? "
        "Will it show open work against available capacity, which team leads currently cannot see?",
        "Also credit: total cost of ownership; scalability across multiple clients with different SLAs; "
        "data protection and retention compliance; measurable improvement against the stated need.",
        "The strongest answers tie the factors back to the ORIGINAL requirement — better insight into "
        "user outcomes, service performance and team utilisation — rather than listing generic "
        "procurement criteria.",
    ]),
    ("Question 5", "A7, A8", "Lab 8 — ITIL Capstone and Exam Readiness (all topics)", [
        "ASSUMPTIONS — the candidate should state the assumptions made in reaching their answers. "
        "Reasonable examples: assumed market conditions (hybrid working persists, stable vendor "
        "pricing); assumed user behaviours (willingness to use the self-service portal); assumed "
        "technological capability (the existing tools expose usable integration points); assumed "
        "client-contract stability at renewal; assumed internal capability and budget to implement.",
        "Any reasonable assumption is acceptable PROVIDED it is explicitly stated and used to justify a "
        "specific answer above — an unstated assumption or one unconnected to the analysis earns no mark.",
        "PRESENTATION — the candidate should describe how they would present the analysis: state the "
        "ITIL concept applied for each question, walk through the reasoning from the scenario evidence to "
        "the conclusion, and clearly flag every assumption made.",
        "DEFENDING THE ANALYSIS — be able to justify why a particular categorisation was chosen "
        "(for example, why portal access is 'access to resources' rather than 'goods'), and to "
        "acknowledge where another group's different-but-defensible reading also holds.",
        "Award the mark for stated, relevant assumptions plus a coherent account of how the analysis "
        "would be presented and justified — not for presentation style.",
    ]),
]


# ================================================================ builders
def build_wa_paper():
    d = new_doc()
    cover(d, "WRITTEN ASSESSMENT (SAQ)")
    admin_page(d, "1 hour", "Written Assessment")
    line(d, "D: Short Answer Questions", bold=True, size=12, after=6)
    line(d, "Answer ALL questions in your own words in the space provided.", after=10)
    # explicit pagination: 2 questions per page — never leave it to the renderer
    PER_PAGE = 2
    for i, (code, ctx, q, _, _) in enumerate(WRITTEN, 1):
        runs(d, [(f"Question {i}: ", True), (ctx, False)], after=4)
        runs(d, [(q, False), (f"  ({code})", True)], after=6)
        answer_lines(d, 5)
        if i % PER_PAGE == 0 and i < len(WRITTEN):
            d.add_page_break()
        else:
            line(d, "", after=8)
    return finish(d, os.path.join(OUT, f"WA (SAQ) - {TITLE} - {VER}.docx"))


def build_wa_answers():
    d = new_doc()
    cover(d, "WRITTEN ASSESSMENT (SAQ) — ANSWER KEY")
    line(d, "Answer Key and Marking Guide", bold=True, size=13, color=BRAND, after=6)
    line(d, "Mark each answer against the model points below. Award the mark where the candidate covers "
            "the key terms and the underlying distinction — exact wording will vary. Every question is "
            "answerable from the course slides and the Learner Guide (source shown for each).", after=10)
    line(d, "TRAINER COPY — NOT FOR RELEASE TO LEARNERS.", bold=True, size=11, color=BRAND, after=12)
    for i, (code, ctx, q, points, src) in enumerate(WRITTEN, 1):
        runs(d, [(f"Question {i}  ({code})", True)], after=3)
        runs(d, [("Context: ", True), (ctx, False)], after=3)
        runs(d, [("Question: ", True), (q, False)], after=3)
        runs(d, [("Source: ", True), (src, False)], after=4)
        line(d, "Model answer points:", bold=True, after=3)
        for p in points: bullet(d, p)
        line(d, "", after=10)
    return finish(d, os.path.join(OUT, f"Answer to WA (SAQ) - {TITLE} - {VER}.docx"))


def _scenario_block(d):
    """The case-study scenario. It owns page 3 in full — questions follow from
    page 4. Set at normal body size for readability; a candidate reads this
    scenario for the whole hour, so it must not be cramped."""
    line(d, "D: Case Study", bold=True, size=12, after=6)
    line(d, SCENARIO_TITLE, bold=True, size=11, after=4)
    line(d, SCENARIO, after=6)
    for pt in SCENARIO_POINTS: bullet(d, pt)
    line(d, "", after=4)
    line(d, SCENARIO_OFFER_INTRO, after=6)

    tbl = d.add_table(rows=0, cols=4); tbl.style = "Table Grid"
    hdr = tbl.add_row().cells
    for i, h in enumerate(SCENARIO_TABLE[0]):
        hdr[i].text = ""
        r = hdr[i].paragraphs[0].add_run(h); r.bold = True; r.font.size = Pt(9.5); r.font.name = "Arial"
    for row in SCENARIO_TABLE[1:]:
        cells = tbl.add_row().cells
        for i, v in enumerate(row):
            cells[i].text = ""
            r = cells[i].paragraphs[0].add_run(v); r.font.size = Pt(9.5); r.font.name = "Arial"
    line(d, "", after=8)
    for para in SCENARIO_TAIL.split("\n\n"):
        line(d, para, after=6)


def build_cs_paper():
    d = new_doc()
    cover(d, "CASE STUDY (CS) ASSESSMENT")
    admin_page(d, "1 hour", "Case Study Assessment")
    # Page 3 is where the assessment CONTENT starts: the scenario. Questions
    # follow from page 4, one per page, each with a full answer box. Page 2
    # carries only Trainee Info + Instructions + Grading — never a question or
    # any part of the scenario.
    _scenario_block(d)
    d.add_page_break()
    line(d, "E: Questions", bold=True, size=12, after=8)
    for n, (label, codes, prompt, nlines) in enumerate(CS_Q, 1):
        runs(d, [(f"{label}: ", True), (prompt, False), (f"  ({codes})", True)], after=2)
        # cite the in-class activity this task is drawn from — the answer key
        # cites the same lab, so paper and key must agree
        runs(d, [("Aligned in-class activity: ", True),
                 ("Lab 1 — Service Management, Value Co-Creation, Utility, Warranty", False)], after=6)
        answer_lines(d, nlines)
        if n < len(CS_Q):
            d.add_page_break()
    return finish(d, os.path.join(OUT, f"CS (Case Study) - {TITLE} - {VER}.docx"))


def build_cs_answers():
    d = new_doc()
    cover(d, "CASE STUDY (CS) ASSESSMENT — ANSWER KEY")
    line(d, "Answer Key and Marking Guide", bold=True, size=13, color=BRAND, after=6)
    line(d, "The model answers below follow the analysis learners carry out in the in-class activities "
            "(cited per question). Award marks where the candidate identifies the correct ITIL concept "
            "AND applies it to evidence from the scenario — a correct definition with no application to "
            "BrightDesk does not earn the mark.", after=8)
    line(d, "TRAINER COPY — NOT FOR RELEASE TO LEARNERS.", bold=True, size=11, color=BRAND, after=12)
    _scenario_block(d)
    d.add_page_break()
    for label, codes, ref, points in CS_A:
        runs(d, [(f"{label}  ({codes})", True)], after=3)
        runs(d, [("Aligned in-class activity: ", True), (ref, False)], after=4)
        line(d, "Model answer points:", bold=True, after=3)
        for p in points: bullet(d, p)
        line(d, "", after=10)
    return finish(d, os.path.join(OUT, f"Answer to CS (Case Study) - {TITLE} - {VER}.docx"))


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)

    # HOUSE RULE: assessments are DOCX ONLY — never a PDF. A PDF is not fillable
    # and creates a second, divergent copy of the paper. Remove any strays.
    import glob
    for stray in glob.glob(os.path.join(OUT, "*.pdf")):
        os.remove(stray)
        print("removed stray PDF:", os.path.basename(stray))
    for fn in (build_wa_paper, build_wa_answers, build_cs_paper, build_cs_answers):
        print("Saved", fn())

    # coverage self-check
    wa_codes = {c for c, *_ in WRITTEN}
    cs_codes = {c.strip() for _, codes, *_ in CS_Q for c in codes.split(",")}
    need_k = set(f"K{i}" for i in range(1, 7))
    need_a = set(f"A{i}" for i in range(1, 9))
    print(f"\nWA questions: {len(WRITTEN)} (original 6)   codes: {sorted(wa_codes)}")
    print(f"CS questions: {len(CS_Q)} (original 5)   codes: {sorted(cs_codes)}")
    missing_k, missing_a = need_k - wa_codes, need_a - cs_codes
    print("K coverage:", "COMPLETE" if not missing_k else f"MISSING {sorted(missing_k)}")
    print("A coverage:", "COMPLETE" if not missing_a else f"MISSING {sorted(missing_a)}")
