"""Domain 1 activities — Understand Key Concepts of Service Management.

NOTE ON THE SCENARIO
  This activity deliberately uses the SAME organisation as the Case Study
  assessment (MediCare Health Group). The CS answer key cites this lab as the
  aligned in-class activity, so learners must have analysed this scenario in
  class before they are assessed on it. Do not change the organisation here
  without changing it in build_assessment_itil.py as well.
"""

DOMAIN1 = [
    dict(
        num=1,
        topic=1,
        title="Case Study: MediCare Health Group — Scenario Analysis from an ITIL Context",
        objective="LO1 (K1, A1) — Explain services, value, outcomes, costs, risks and the roles of service providers and consumers.",
        desc=(
            "MediCare Health Group, established in 1995, operates a network of private clinics and two "
            "specialist medical centres across Southeast Asia, employing more than 8,000 clinical and "
            "administrative staff across Singapore, Malaysia, Thailand, Indonesia, Vietnam and the "
            "Philippines. Rising middle-class incomes, greater health awareness, government subsidies "
            "for preventive screening and widespread smartphone adoption have created strong demand for "
            "private healthcare. MediCare has launched Essential, Advanced and Executive health "
            "screening packages, each bundling diagnostic tests, a digital health report, "
            "teleconsultation and a period of access to its online patient portal. Results are promised "
            "within 5 business days, backed by a 24x7 support hotline and a portal chatbot that "
            "escalates to a human officer. As the group expands, the IT Director has been asked to "
            "evaluate a service management solution that will give better insight into patient "
            "outcomes, service performance and clinic utilisation. Working in small groups of 2-3, "
            "analyse this scenario through an ITIL lens."
        ),
        build="A completed group analysis identifying opportunity, value, external factors, the service offering components and the selection criteria for a service management solution.",
        services="Case study brief, ITIL 4 Foundation slides, Learner Guide",
        steps=[
            ("Divide the class into 2-4 small groups, each with 2-3 persons, and read the MediCare Health Group scenario in full.", ""),
            ("Question 1: List examples of opportunity and value in the scenario. Distinguish the opportunity MediCare is pursuing from the value co-created for its patients.", ""),
            ("Question 2: Identify the external factors MediCare is leveraging. Use PESTLE (political, economic, social, technological, legal, environmental) to structure your answer.", ""),
            ("Question 3: Identify the goods, the access to resources and the service actions that make up the health screening service offering. Apply the ownership test to each.", ""),
            ("Question 4: Determine the consideration factors the IT Director should apply when evaluating a service management solution. Structure them using the four dimensions of service management.", ""),
            ("Document any assumptions your group made — market conditions, patient behaviours or technological capabilities available to MediCare.", ""),
            ("Each group presents its findings to the class, clearly justifying its answers and stating its assumptions.", ""),
        ],
        test="Your group can justify, for each of the four questions, which ITIL concept it applied and why — and can defend its assumptions when challenged by another group.",
    ),
]
