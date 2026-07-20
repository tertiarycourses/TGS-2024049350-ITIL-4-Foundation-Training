"""Domain 3 activities — The Four Dimensions of Service Management."""

DOMAIN3 = [
    dict(
        num=3,
        topic=3,
        title="Group Activity: Analysing a Service Across the Four Dimensions",
        objective="LO3 (K3, A3, A4) — Describe the four dimensions of service management and evaluate how each affects service delivery.",
        desc=(
            "ITIL 4 requires a holistic approach: every component of the service value system must be "
            "considered from all four dimensions — organizations and people, information and technology, "
            "partners and suppliers, and value streams and processes. Neglecting a dimension is a common "
            "cause of service failure. In this activity groups take a familiar service and work it "
            "through all four dimensions, then identify which dimension is weakest and what that costs."
        ),
        build="A four-dimension analysis of a real service, with the weakest dimension identified and justified.",
        services="ITIL 4 Foundation slides, Learner Guide, PESTLE framework",
        steps=[
            ("Divide the class into 2-4 small groups, each with 2-3 persons.", ""),
            ("Select a service your group knows well — a corporate IT service desk, an email service, a cloud hosting service or a service from a member's workplace.", ""),
            ("Organizations and people: identify the roles, responsibilities, structures, culture and competencies the service depends on.", ""),
            ("Information and technology: identify the information and knowledge required, and the technologies that support and enable the service.", ""),
            ("Partners and suppliers: identify the external organisations involved in designing, deploying, delivering or supporting the service, and the dependencies they create.", ""),
            ("Value streams and processes: map at a high level how the parts of the organisation work together to deliver the service end to end.", ""),
            ("Apply PESTLE to identify the external factors that constrain the service across the dimensions.", ""),
            ("Decide which of the four dimensions is currently weakest for this service, and explain the specific impact that weakness has on the value delivered.", ""),
            ("Present your analysis to the class.", ""),
        ],
        test="Your group can name the weakest dimension for the chosen service and trace a concrete service failure or risk directly back to it.",
    ),
]
