"""Domain 5 activities — ITIL Practices."""

DOMAIN5 = [
    dict(
        num=5,
        topic=5,
        title="Group Activity: Triaging Incidents, Problems, Changes and Service Requests",
        objective="LO5 (K5, K6, A7, A8) — Describe the purpose of the key ITIL practices and apply them to real scenarios.",
        desc=(
            "The most common practical error at Foundation level is misclassifying work: logging a "
            "service request as an incident, treating a recurring incident as a series of unrelated "
            "incidents rather than a problem, or pushing an undocumented change straight into "
            "production. In this activity groups triage a set of realistic scenarios, decide which "
            "practice owns each one, and justify the decision — then design the handling path."
        ),
        build="A triaged scenario set with the owning practice identified for each, plus a handling path for the most complex scenario.",
        services="ITIL 4 Foundation slides, Learner Guide, practice definitions",
        steps=[
            ("Divide the class into 2-4 small groups, each with 2-3 persons.", ""),
            ("Scenario A: A user calls the service desk because they cannot access the shared drive. No one else is affected. Which practice owns this, and why?", ""),
            ("Scenario B: The shared drive has failed four times this month, each time restored by a restart. Which practice owns this, and how does it differ from Scenario A?", ""),
            ("Scenario C: A new employee needs a laptop, an email account and access to the CRM. Which practice owns this, and why is it not an incident?", ""),
            ("Scenario D: The infrastructure team wants to apply an urgent security patch to the production database this evening. Which practice owns this, and what change type applies?", ""),
            ("Scenario E: The business complains that the service desk 'never resolves anything on time', but no target has ever been agreed. Which practice owns this, and what artefact is missing?", ""),
            ("For each scenario, state the practice, its purpose in your own words, and the key term that determines the classification (incident, problem, known error, workaround, service request, change, SLA).", ""),
            ("Select the most complex scenario and design its end-to-end handling path, naming every practice it touches from initial contact to closure.", ""),
            ("Present your triage decisions to the class and defend any the other groups classified differently.", ""),
        ],
        test="Your group can correctly classify all five scenarios and explain the distinguishing test between an incident and a problem, and between a service request and an incident.",
    ),
]
