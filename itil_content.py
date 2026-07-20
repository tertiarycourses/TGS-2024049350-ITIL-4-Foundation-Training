"""
Substantive ITIL 4 Foundation content, written from ITIL 4 domain knowledge.

WHY THIS FILE EXISTS
  The v11 master deck carries many one-line slides — "Plan Value Chain Activity"
  with a single sentence, "What is a Practice?" with one line. Rendering those as
  a card gives a thin, unteachable slide. This module supplies real teaching
  content for each of them: the definition, the key points a Foundation candidate
  must know, a worked example, and the exam trap where one exists.

  Keyed by the v11 slide number it enriches. Any slide not listed here falls back
  to its original v11 text.

  All content is original, written for this course. No third-party study guide or
  copyrighted book is reproduced.
"""

# Untitled v11 diagram slides — a title inferred from the surrounding context, so
# they do not fall back to the generic "ITIL 4 Foundation" heading.
DIAGRAM_TITLES = {
    21:  "Services and Service Management",
    23:  "What Is a Service?",
    36:  "The Nature of Value",
    38:  "Three Dimensions of Value",
    66:  "From Utility and Warranty to the Service Value Chain",
    165: "The ITIL Service Value System at a Glance",
}

# slide-number -> dict(kicker, title, points[], example=(label, text), tip=str)
ENRICH = {

    # ============================================ TOPIC 1 — key concepts
    27: dict(
        title="The ITIL Service Value System (SVS)",
        points=[
            "The SVS describes how all the components and activities of an organisation work together as a system to enable value creation.",
            "Inputs: OPPORTUNITY (possibilities to add value) and DEMAND (the need for services from consumers).",
            "Output: VALUE — the perceived benefits, usefulness and importance of something.",
            "Five components: guiding principles, governance, the service value chain, practices, and continual improvement.",
            "Its purpose is to prevent organisational silos — every part must work as one system, not as separate functions.",
        ],
        example=("Why it matters",
                 "A service desk that hits its own ticket targets while releases keep breaking production is optimising a silo, not the system."),
        tip="Know the five SVS components and that the two inputs are opportunity and demand.",
    ),

    33: dict(
        title="Opportunity and Demand — the Inputs to the SVS",
        points=[
            "OPPORTUNITY represents options or possibilities to add value for stakeholders, or otherwise improve the organisation.",
            "DEMAND is the need or desire for products and services from internal and external consumers.",
            "Both trigger activities within the SVS; those activities lead to the creation of value.",
            "Opportunity and demand are always entering the system — the organisation chooses which to accept.",
            "Not all demand should be met, and not every opportunity should be pursued: both are filtered against strategy and capacity.",
        ],
        example=("In practice",
                 "Rising remote working (demand) plus a new cloud licensing model (opportunity) together justify a VDI service."),
        tip="Exam wording: the INPUTS to the SVS are 'opportunity and demand'. Value is the OUTPUT.",
    ),

    45: dict(
        title="Service Offerings",
        points=[
            "A service offering is a formal description of one or more services, designed to address the needs of a target consumer group.",
            "It may include GOODS, ACCESS TO RESOURCES, and SERVICE ACTIONS.",
            "GOODS — ownership is TRANSFERRED to the consumer, who takes responsibility for future use.",
            "ACCESS TO RESOURCES — ownership is NOT transferred; access is granted or licensed under agreed terms and conditions.",
            "SERVICE ACTIONS — performed by the service provider to address a consumer need, according to an agreement.",
        ],
        example=("Mobile phone plan",
                 "Goods: the handset you keep. Access to resources: the network and data allowance. Service actions: activation and support calls."),
        tip="The test is ownership: transferred = goods; granted for a period = access to resources; performed by the provider = service action.",
    ),

    54: dict(
        title="Resources, Cost and Risk",
        points=[
            "A RESOURCE is personnel, material, finance or any other entity required to execute an activity or achieve an objective.",
            "Resources used by an organisation may be owned by it, or used under agreement with their owner.",
            "Service relationships shift the burden of certain resources from the consumer to the provider.",
            "This is precisely how a service removes cost and risk from the consumer — the provider carries them instead.",
            "The consumer still manages the resources it needs in order to CONSUME the service.",
        ],
        example=("Cloud hosting",
                 "The provider owns the data centre, hardware and patching; the consumer keeps only the skills to use the platform."),
        tip="Resources are the 'what you need to do the work'. Do not confuse them with the service actions performed with them.",
    ),

    59: dict(
        title="Costs in a Service Relationship",
        points=[
            "COST is the amount of money spent on a specific activity or resource; it can also be expressed non-monetarily, as time or effort.",
            "Every service both IMPOSES costs on the consumer and REMOVES costs from the consumer.",
            "Costs IMPOSED: the fees, charges and effort of adopting and using the service.",
            "Costs REMOVED: the infrastructure, staff, training and maintenance the consumer no longer has to fund.",
            "A service is worth adopting when the costs removed plus the outcomes enabled exceed the costs imposed.",
        ],
        example=("Payroll SaaS",
                 "Imposes a subscription and migration effort; removes a payroll server, an in-house specialist and quarterly compliance updates."),
        tip="Expect a question that asks which costs a service REMOVES — the answer is the consumer's own infrastructure and effort.",
    ),

    62: dict(
        title="Risks in a Service Relationship",
        points=[
            "A RISK is a possible event that could cause harm or loss, or make it more difficult to achieve objectives.",
            "Risk can also be defined as uncertainty of outcome, and can be used to measure both positive and negative uncertainty.",
            "Like cost, a service both IMPOSES and REMOVES risk for the consumer.",
            "Risks IMPOSED: service outages, security exposure, supplier lock-in, compliance gaps.",
            "Risks REMOVED: the consumer no longer carries hardware failure, capacity planning or specialist staff turnover.",
        ],
        example=("Managed security",
                 "Removes the risk of missing a critical patch; imposes the risk of depending on the provider's own response times."),
        tip="A service NEVER removes all risk. Foundation questions test that both directions exist.",
    ),

    67: dict(
        title="The Service Value Chain",
        points=[
            "The service value chain is an operating model: a set of six interconnected activities an organisation performs to deliver a valuable product or service.",
            "The six activities are PLAN, IMPROVE, ENGAGE, DESIGN AND TRANSITION, OBTAIN/BUILD, and DELIVER AND SUPPORT.",
            "Each activity converts inputs into outputs; the outputs of one commonly become the inputs of another.",
            "The activities can be combined in many sequences — these combinations are called VALUE STREAMS.",
            "The chain is flexible by design: no fixed order is prescribed, so it adapts to any type of demand.",
        ],
        example=("One value stream",
                 "An incident enters at 'engage', is resolved by 'deliver and support', and a fix is fed to 'improve'."),
        tip="Learn all six activity names and the PURPOSE sentence of each — they are examined directly.",
    ),

    97: dict(
        title="What Is a Guiding Principle?",
        points=[
            "A guiding principle is a recommendation that guides an organisation in ALL circumstances, regardless of changes in its goals, strategies, type of work or management structure.",
            "The principles are universal and enduring — they do not change when the organisation's situation changes.",
            "They embody the core messages of ITIL and of service management generally.",
            "They support successful action and good decisions at every level, from strategy to a single ticket.",
            "There are SEVEN principles, and an organisation need not adopt them one at a time — they reinforce each other.",
        ],
        example=("How they are used",
                 "Faced with any decision, ask which principles apply and what each would have you do — and stop doing."),
        tip="Universality is the defining trait: 'in all circumstances, regardless of changes'.",
    ),

    151: dict(
        title="Value Streams",
        points=[
            "A VALUE STREAM is a series of steps an organisation undertakes to create and deliver products and services to consumers.",
            "It is a specific combination of service value chain activities, arranged for a particular scenario.",
            "Value streams are designed around the consumer's journey, not around the organisation's departments.",
            "Mapping a value stream exposes bottlenecks, waste, rework and hand-off delays that no single team can see.",
            "Improving the value stream is how an organisation improves the end-to-end experience rather than a local step.",
        ],
        example=("A new-starter value stream",
                 "Request → approve → provision accounts → issue laptop → grant access → confirm ready — crossing HR, IT and facilities."),
        tip="Value STREAM = the end-to-end path for one scenario. Value CHAIN = the six generic activities it draws on.",
    ),

    153: dict(
        title="Processes",
        points=[
            "A PROCESS is a set of interrelated or interacting activities that transforms inputs into outputs.",
            "A process defines the sequence of actions and their dependencies — what is done, in what order, to achieve an objective.",
            "Processes describe WHAT is done; procedures describe HOW; work instructions describe the detailed steps for a specific role.",
            "Well-defined processes improve productivity within and across organisations, and make outcomes repeatable.",
            "Processes should be designed to produce a specific outcome for a specific stakeholder — never for their own sake.",
        ],
        example=("Hierarchy in practice",
                 "Process: handle an incident. Procedure: how the service desk triages it. Work instruction: the exact steps to reset an AD password."),
        tip="Work instruction = HOW something is carried out, in detail, for one role. This exact distinction is examined.",
    ),

    169: dict(
        title="The Six Service Value Chain Activities",
        points=[
            "PLAN — ensures a shared understanding of the vision, current status and improvement direction for all four dimensions.",
            "IMPROVE — ensures continual improvement of products, services and practices across all value chain activities.",
            "ENGAGE — provides a good understanding of stakeholder needs, transparency, and continual engagement and good relationships.",
            "DESIGN AND TRANSITION — ensures products and services continually meet stakeholder expectations for quality, cost and time to market.",
            "OBTAIN/BUILD — ensures service components are available when and where needed, and that they meet agreed specifications.",
            "DELIVER AND SUPPORT — ensures services are delivered and supported according to agreed specifications and expectations.",
        ],
        example=("They interconnect",
                 "'Engage' captures a requirement, 'design and transition' shapes it, 'obtain/build' assembles it, 'deliver and support' runs it."),
        tip="Learn the one-sentence PURPOSE of each activity — they are examined by their opening phrase.",
    ),

    170: dict(
        title="Plan — Value Chain Activity",
        points=[
            "PURPOSE: to ensure a shared understanding of the vision, current status and improvement direction for all four dimensions and all products and services across the organisation.",
            "Plan sets direction; it does not do the work — it makes sure everyone is heading the same way.",
            "Key inputs: policies, requirements and constraints from governance; consolidated demand and opportunity; improvement initiatives.",
            "Key outputs: strategic, tactical and operational plans; portfolio decisions; architectures and policies.",
            "Applies at every level — enterprise strategy down to the plan for a single service.",
        ],
        example=("Typical trigger",
                 "Annual service portfolio review deciding which services to invest in, sustain or retire."),
        tip="If a question mentions 'vision, current status and improvement direction', the answer is PLAN.",
    ),

    171: dict(
        title="Improve — Value Chain Activity",
        points=[
            "PURPOSE: to ensure continual improvement of products, services and practices across all value chain activities and all four dimensions.",
            "Improve is a value chain ACTIVITY; continual improvement is also an SVS component and a PRACTICE — the same idea at three levels.",
            "Improvement work is driven by measurement: you cannot improve what you do not measure.",
            "Key inputs: performance information, stakeholder feedback, improvement opportunities from every other activity.",
            "Key outputs: improvement initiatives and plans, updated performance information, value chain performance reports.",
        ],
        example=("Typical trigger",
                 "Repeat incidents on one service prompt a problem review and a permanent fix rather than another restart."),
        tip="Improve appears in the value chain AND as a practice AND as an SVS component — all three are examinable.",
    ),

    174: dict(
        title="Engage — Value Chain Activity",
        points=[
            "PURPOSE: to provide a good understanding of stakeholder needs, transparency, and continual engagement and good relationships with all stakeholders.",
            "Stakeholders include customers, users, sponsors, suppliers, partners, regulators and internal teams.",
            "Engage is the primary point of contact with the outside world — it is where demand and feedback enter the SVS.",
            "Key inputs: consumer demand, user requests and incidents, supplier information, market opportunity.",
            "Key outputs: consolidated demand and opportunity, service performance reports, contract and agreement requirements.",
        ],
        example=("Typical trigger",
                 "A quarterly service review with the customer that reshapes the improvement backlog."),
        tip="'Transparency and good relationships with ALL stakeholders' is the signature phrase for ENGAGE.",
    ),

    175: dict(
        title="Design and Transition — Value Chain Activity",
        points=[
            "PURPOSE: to ensure products and services continually meet stakeholder expectations for QUALITY, COST and TIME TO MARKET.",
            "Covers design of the service and its transition into live operation — including testing, validation and release readiness.",
            "Considers all four dimensions, not only the technology.",
            "Key inputs: portfolio decisions, requirements from engage, improvement initiatives, service components from obtain/build.",
            "Key outputs: requirements and specifications for obtain/build, new and changed services, contract requirements.",
        ],
        example=("Typical trigger",
                 "A new customer portal moving from design sign-off through UAT to a controlled go-live."),
        tip="Three words identify this activity: quality, cost, time to market.",
    ),

    176: dict(
        title="Obtain / Build — Value Chain Activity",
        points=[
            "PURPOSE: to ensure service components are available when and where they are needed, and that they meet agreed specifications.",
            "Components may be built in-house or obtained from a supplier — the make-or-buy decision sits here.",
            "Make: builds internal expertise and control, but costs time and capacity.",
            "Buy: uses supplier expertise and speed, but creates dependency and less control.",
            "Key outputs: service components, change requests, knowledge and information about components.",
        ],
        example=("Make or buy",
                 "Building a bespoke CRM gives exact fit; licensing one gives faster delivery and a supported upgrade path."),
        tip="'Available when and where needed, meeting specifications' points to OBTAIN/BUILD.",
    ),

    179: dict(
        title="Deliver and Support — Value Chain Activity",
        points=[
            "PURPOSE: to ensure services are delivered and supported according to agreed specifications and stakeholders' expectations.",
            "This is the activity users experience day to day — it is where the service actually runs.",
            "Includes handling incidents and service requests, and performing routine operational tasks.",
            "Key inputs: new and changed services, service components, user requests and incidents from engage.",
            "Key outputs: services delivered to consumers, information on completed tasks, change requests and improvement opportunities.",
        ],
        example=("Typical trigger",
                 "A user cannot access a shared drive: logged at engage, restored at deliver and support."),
        tip="Delivery AND support together — this activity covers both running the service and fixing it.",
    ),

    182: dict(
        title="Continual Improvement",
        points=[
            "PURPOSE: to align the organisation's practices and services with changing business needs, through ongoing identification and improvement of every element involved in the management of products and services.",
            "Continual improvement appears three times in ITIL 4: as an SVS component, a value chain activity, and a practice.",
            "It applies to every element — services, practices, processes, relationships and the four dimensions.",
            "Everyone contributes: it is not the job of a dedicated improvement team alone.",
            "Improvement ideas are captured in a CONTINUAL IMPROVEMENT REGISTER (CIR) so nothing is lost.",
        ],
        example=("The register",
                 "A CIR lets a small idea from a service-desk agent be assessed and prioritised alongside a strategic initiative."),
        tip="The database or structured document used to track improvement ideas is the Continual Improvement Register (CIR).",
    ),

    185: dict(
        title="Step 1 — What Is the Vision?",
        points=[
            "Every improvement initiative must support the organisation's goals and objectives.",
            "This step sets the vision and defines what success will look like before any work begins.",
            "It translates organisational vision into a vision for THIS specific improvement.",
            "Stakeholders must understand and buy into the vision, or the improvement will stall later.",
            "Skipping this step is the most common reason an improvement delivers change nobody wanted.",
        ],
        example=("A clear vision",
                 "'Cut new-starter setup from 5 days to 1' — measurable, time-bound, and obviously tied to a business goal."),
        tip="Step 1 is about DIRECTION, not measurement. 'Where are we now?' is Step 2.",
    ),

    187: dict(
        title="Step 2 — Where Are We Now?",
        points=[
            "The success of an improvement depends on a clear, accurate understanding of the starting point.",
            "This step performs an objective, evidence-based CURRENT-STATE ASSESSMENT — a baseline.",
            "Assess existing services, ways of working, people, technology, partners and processes.",
            "The assessment must be honest: an inaccurate baseline makes every later measurement meaningless.",
            "Without a baseline you cannot demonstrate at Step 6 that the improvement actually worked.",
        ],
        example=("The baseline",
                 "Measure the real current setup time — 5.2 days on average — before promising an improvement to 1 day."),
        tip="Step 2 = the BASELINE. It is what Step 6 measures against.",
    ),

    189: dict(
        title="Step 3 — Where Do We Want to Be?",
        points=[
            "Step 2 describes Point A; Step 3 describes Point B — the target state.",
            "Perform a GAP ANALYSIS between the current state and the desired state.",
            "Define measurable targets and critical success factors, plus the KPIs that will show progress.",
            "The target must be realistic in the light of Step 2's honest baseline.",
            "The size of the gap determines whether one iteration is enough or several will be needed.",
        ],
        example=("Gap analysis",
                 "Current 5.2 days, target 1 day: a 4.2-day gap, likely to need several iterations rather than one change."),
        tip="Step 3 is where GAP ANALYSIS and measurable targets belong.",
    ),

    191: dict(
        title="Step 4 — How Do We Get There?",
        points=[
            "This step produces the plan — the route from Point A to Point B.",
            "The plan may be a direct route for a simple improvement, or an iterative series of changes for a complex one.",
            "Applying 'progress iteratively with feedback' here reduces risk and surfaces problems early.",
            "Experiments and pilots are legitimate: the best route is not always known in advance.",
            "Each iteration should deliver something of value, not just progress towards a distant end state.",
        ],
        example=("Iterating",
                 "Automate account creation first (5.2 → 3 days), then laptop imaging, then access approval."),
        tip="Step 4 is the PLAN. Executing it is Step 5.",
    ),

    193: dict(
        title="Step 5 — Take Action",
        points=[
            "In this step the plan for the improvement is acted upon — the work is actually done.",
            "The approach may be traditional and sequential, or agile and iterative with experiments.",
            "Change enablement, project management and organisational change management all support this step.",
            "Progress must be tracked, and the plan adjusted when reality differs from expectation.",
            "Communication matters as much as delivery: people affected by the change need to know what is happening.",
        ],
        example=("Taking action",
                 "Building and releasing the automated account-creation workflow into production."),
        tip="Step 5 is EXECUTION. Checking whether it worked is Step 6.",
    ),

    195: dict(
        title="Step 6 — Did We Get There?",
        points=[
            "It is too often assumed that once an improvement is in motion, the expected benefits were achieved.",
            "This step CHECKS the outcome against the Step 2 baseline and the Step 3 targets, using evidence.",
            "If the target was met, confirm and communicate it with data.",
            "If it was not, that is not a failure — it is information. Return to an earlier step and iterate.",
            "Honest measurement here is what separates real improvement from an assumption of improvement.",
        ],
        example=("Checking",
                 "Measured setup time now 1.4 days: a genuine gain, short of the 1-day target — so iterate again."),
        tip="Step 6 verifies against the BASELINE from Step 2. This link is examined.",
    ),

    197: dict(
        title="Step 7 — How Do We Keep the Momentum Going?",
        points=[
            "If the improvement delivered the expected value, the focus shifts to MARKETING that success and reinforcing the new ways of working.",
            "Embed the change so the organisation does not quietly drift back to the old behaviour.",
            "Share the result: visible success builds support and appetite for the next improvement.",
            "Update documentation, training and the continual improvement register.",
            "Momentum is the point — continual improvement is a recurring activity, not a one-off project.",
        ],
        example=("Keeping momentum",
                 "Publishing the setup-time result to the business, then opening the next improvement from the CIR."),
        tip="Step 7 is about REINFORCING and MARKETING the improvement so it sticks.",
    ),

    # ============================================ TOPIC 1 — cost / utility
    60: dict(
        title="Types of Cost — Imposed and Removed",
        points=[
            "Costs IMPOSED on the consumer: the fees, charges and expenses of adopting and using the service.",
            "Also imposed: migration effort, training time, and the cost of integrating the service with existing systems.",
            "Costs REMOVED from the consumer: the infrastructure, licences, premises and staff no longer needed.",
            "Also removed: the effort of maintenance, patching, capacity planning and specialist recruitment.",
            "Adoption is justified when the costs removed, plus the outcomes enabled, outweigh the costs imposed.",
        ],
        example=("Both directions at once",
                 "Moving email to a cloud suite imposes per-seat fees; it removes mail servers, backups and an administrator."),
        tip="Every service does BOTH. A question naming only one direction is testing whether you know the other exists.",
    ),

    63: dict(
        title="Utility and Warranty",
        points=[
            "UTILITY is the functionality offered by a product or service to meet a particular need — 'what the service DOES'.",
            "Utility determines whether a service is FIT FOR PURPOSE.",
            "To have utility, a service must either support the performance of the consumer, or remove constraints from the consumer — many do both.",
            "WARRANTY is the assurance that a product or service will meet agreed requirements — 'how the service PERFORMS'.",
            "Warranty determines whether a service is FIT FOR USE, and covers availability, capacity, security and continuity.",
            "A service needs BOTH to create value: functionality nobody can reach delivers nothing.",
        ],
        example=("Hotel room",
                 "Utility: a bed, wifi and a desk. Warranty: the room is available on the night booked, and the door lock works."),
        tip="Utility = fit for PURPOSE = what it does. Warranty = fit for USE = how it performs. Both are needed.",
    ),

    # ============================================ TOPIC 2 — principles
    101: dict(
        title="Focus on Value",
        points=[
            "Everything the organisation does should link back, directly or indirectly, to value for itself, its customers and its other stakeholders.",
            "Start by knowing WHO is being served — the consumer, and any other stakeholder affected.",
            "Then establish WHAT is being delivered or improved for them, and what they actually consider valuable.",
            "Value is defined by the CONSUMER, not by the provider's opinion of its own service.",
            "Value takes many forms: revenue, customer loyalty, reduced cost, reduced risk, better experience.",
        ],
        example=("Applying it",
                 "Before adding a feature, ask which consumer outcome it improves. If nobody can answer, it is not value."),
        tip="'Know who is being served' and 'understand what the consumer values' are the signature phrases.",
    ),

    111: dict(
        title="Progress Iteratively with Feedback",
        points=[
            "Resist the temptation to do everything at once — even huge initiatives must be accomplished iteratively.",
            "Organise work into smaller, manageable sections that can be executed and completed in a timely manner.",
            "Each iteration should deliver something of value, not merely progress towards a distant end state.",
            "Seek and use FEEDBACK before, throughout and after each iteration — feedback is what makes iteration work.",
            "Iteration reduces risk: problems surface early, while they are still cheap to correct.",
        ],
        example=("Applying it",
                 "Pilot a new service desk tool with one team for two weeks, act on what they report, then extend it."),
        tip="Iteration WITHOUT feedback is just phasing. The feedback loop is the point of the principle.",
    ),

    115: dict(
        title="Collaborate and Promote Visibility",
        points=[
            "When initiatives involve the right people in the correct roles, efforts benefit from better buy-in and more relevance.",
            "Collaboration across boundaries produces a greater likelihood of long-term success than isolated silo activity.",
            "Identify and involve ALL relevant stakeholders, not only the obvious or the convenient ones.",
            "Promote visibility: work that is hidden cannot be prioritised, supported or improved.",
            "Poor visibility leads to poor decisions — people assume rather than know what is happening.",
        ],
        example=("Applying it",
                 "A visible Kanban board of live work stops leaders from adding urgent requests onto an already-saturated team."),
        tip="Two halves: involve the RIGHT PEOPLE, and make the work VISIBLE. Expect both in the answer.",
    ),

    120: dict(
        title="Think and Work Holistically",
        points=[
            "No service, practice, process, department or supplier stands alone.",
            "The outputs an organisation delivers to itself, its customers and other stakeholders will suffer unless it works on the whole, not just on the parts.",
            "Establish an understanding of how all parts of the organisation work together in an integrated way.",
            "Work towards END-TO-END delivery: optimising one step at the expense of the whole makes the service worse.",
            "Apply all FOUR DIMENSIONS when planning any change — people, information and technology, partners, and value streams.",
        ],
        example=("Applying it",
                 "A faster deployment pipeline is no gain if the service desk is not trained to support what it now ships weekly."),
        tip="Signature phrase: 'approach activities as related to the whole rather than as separate parts'.",
    ),

    157: dict(
        title="Value Streams and Processes — Considerations",
        points=[
            "The same structure applies at every level: VALUE STREAMS, then PROCESSES, then PROCEDURES, then WORK INSTRUCTIONS.",
            "Ask what the value streams are for each service, and how they are currently performing.",
            "Ask which activities are performed, in what order, and who is accountable for each.",
            "Identify bottlenecks, unnecessary hand-offs, rework and waste — they hide in the gaps between teams.",
            "Optimise the flow of work end-to-end, not the efficiency of any single step in isolation.",
        ],
        example=("Where waste hides",
                 "A request approved in 5 minutes but waiting 3 days between two teams: the delay is entirely in the hand-off."),
        tip="Structure order: value stream → process → procedure → work instruction. Learn it in that direction.",
    ),

    173: dict(
        title="The PDCA / Deming Cycle",
        points=[
            "PDCA — Plan, Do, Check, Act — is a cyclic method for the continual improvement of processes and products.",
            "PLAN: identify the problem and objective, and design the change to be tested.",
            "DO: implement the change, ideally on a small scale first.",
            "CHECK: measure the result against the objective set in the Plan step, using evidence.",
            "ACT: if it worked, standardise and roll it out; if not, adjust and run the cycle again.",
            "It is a CYCLE, not a project — it repeats, which is exactly what makes improvement continual.",
        ],
        example=("A full turn",
                 "Plan: inconsistent machine settings cause defects. Do: standardise on one line. Check: defects fall 40%. Act: roll out to all lines."),
        tip="PDCA maps onto the continual improvement model — both check the result against a baseline before standardising.",
    ),

    # ============================================ TOPIC 5 — practices
    206: dict(
        title="The 34 ITIL Practices — Three Groups",
        points=[
            "A practice is a set of organisational resources designed for performing work or accomplishing an objective.",
            "GENERAL MANAGEMENT PRACTICES (14) — adopted from general business management, e.g. continual improvement, information security management, relationship management, supplier management.",
            "SERVICE MANAGEMENT PRACTICES (17) — developed within service management, e.g. incident management, problem management, change enablement, service desk, service level management.",
            "TECHNICAL MANAGEMENT PRACTICES (3) — adapted from technology management: deployment management, infrastructure and platform management, and software development and management.",
            "A practice is broader than a process: it includes the people, tools, information and processes required to do the work.",
        ],
        example=("Why 'practice' not 'process'",
                 "Incident management needs a process, but also trained agents, a tool, a knowledge base and an escalation path."),
        tip="34 practices = 14 general + 17 service + 3 technical. The three technical ones are worth memorising.",
    ),

    212: dict(
        title="Information Security Management",
        points=[
            "PURPOSE: to protect the information needed by the organisation to conduct its business.",
            "Covers CONFIDENTIALITY (only the right people see it), INTEGRITY (it is accurate and complete) and AVAILABILITY (it is there when needed).",
            "Also covers authentication (the person is who they claim) and non-repudiation (an action cannot later be denied).",
            "Security must balance PROTECTION against AVAILABILITY — controls so tight that nobody can work have failed.",
            "It is a general management practice: it applies across every service, not only to IT systems.",
        ],
        example=("The balance",
                 "Mandatory MFA on a clinical system protects records, but must not lock a clinician out during an emergency."),
        tip="CIA — confidentiality, integrity, availability — is the core of this practice.",
    ),

    218: dict(
        title="Relationship Management",
        points=[
            "PURPOSE: to establish and nurture the links between the organisation and its stakeholders at strategic and tactical levels.",
            "Covers the identification, analysis, monitoring and continual improvement of relationships with and between stakeholders.",
            "Ensures stakeholders' needs are understood and that priorities are balanced across competing demands.",
            "Builds the trust that allows difficult conversations — about cost, risk or capacity — to happen productively.",
            "Distinct from supplier management: this practice covers ALL stakeholders, not only vendors.",
        ],
        example=("In practice",
                 "A regular business-relationship review that surfaces an upcoming acquisition before IT is asked to absorb it."),
        tip="Relationship management = all stakeholders. Supplier management = the supply side specifically.",
    ),

    219: dict(
        title="Supplier Management",
        points=[
            "PURPOSE: to ensure the organisation's suppliers and their performance are managed appropriately to support the seamless provision of quality products and services.",
            "Includes creating closer, more collaborative relationships with key suppliers to uncover and realise new value.",
            "Activities: evaluating and selecting suppliers, negotiating contracts, managing performance, and managing renewal or termination.",
            "Strategy considerations include strategic focus, resource scarcity, cost, subject-matter expertise and external constraints.",
            "Underpinning contracts with suppliers must support the service levels promised to your own customers.",
        ],
        example=("The chain",
                 "A 4-hour SLA to the business is undeliverable if the hardware vendor's underpinning contract is next-business-day."),
        tip="Supplier commitments must be at least as strong as the SLAs they support — expect a question on this chain.",
    ),

    222: dict(
        title="Change Enablement",
        points=[
            "PURPOSE: to maximise the number of successful IT changes by ensuring risks are properly assessed, authorising changes to proceed, and managing the change schedule.",
            "A CHANGE is the addition, modification or removal of anything that could have a direct or indirect effect on services.",
            "Every change is authorised by a CHANGE AUTHORITY — the person or group with the right to approve it.",
            "The practice balances SPEED against RISK: too much control and delivery stalls; too little and outages follow.",
            "It is 'change enablement', not 'change control' — the aim is to enable change safely, not to prevent it.",
        ],
        example=("Balance",
                 "Pre-authorising low-risk standard changes frees the change authority to scrutinise the genuinely risky ones."),
        tip="Note the wording: MAXIMISE the number of SUCCESSFUL changes — not minimise the number of changes.",
    ),

    224: dict(
        title="The Three Types of Change",
        points=[
            "STANDARD — pre-authorised, low-risk, well-understood and fully documented; implemented without needing new authorisation each time.",
            "NORMAL — must be scheduled, assessed and authorised following a defined process; the change authority depends on the level of risk.",
            "EMERGENCY — must be implemented as soon as possible, typically to resolve a major incident or apply a critical security patch.",
            "Emergency changes are still authorised, but by a smaller, faster body and often with documentation completed afterwards.",
            "Emergency changes may have a separate change authority and an accelerated assessment and approval path.",
        ],
        example=("Each type",
                 "Standard: create a user account. Normal: upgrade a database. Emergency: patch an actively exploited vulnerability."),
        tip="Standard = pre-authorised, NOT 'simple'. That distinction is a common exam trap.",
    ),

    225: dict(
        title="Change Authority and the Change Schedule",
        points=[
            "The CHANGE AUTHORITY is the person or group who authorises a change.",
            "Authority is assigned by risk and impact: low-risk changes are devolved to the team; high-risk ones escalate.",
            "Centralising all authority in one committee creates a bottleneck and slows delivery — devolution is deliberate.",
            "The CHANGE SCHEDULE is used to plan changes, assist communication, avoid conflicts and assign resources.",
            "The schedule also supports post-incident review: it shows what changed and when.",
        ],
        example=("Devolved authority",
                 "A standard account creation is authorised by the service desk; a core network upgrade goes to a senior authority."),
        tip="The change schedule helps plan, communicate, avoid conflicts and assign resources — learn those four uses.",
    ),

    227: dict(
        title="What Is an Incident?",
        points=[
            "An INCIDENT is an unplanned interruption to a service, or a reduction in the quality of a service.",
            "The purpose of incident management is to minimise the negative impact of incidents by restoring normal service operation as quickly as possible.",
            "Every incident should be logged and managed to ensure it is resolved in a time that meets the expectations of the customer and user.",
            "Incidents are prioritised by IMPACT (how much of the business is affected) and URGENCY (how quickly it must be fixed).",
            "Restoring service takes priority over finding the underlying cause — that is problem management's job.",
        ],
        example=("Degradation counts",
                 "A system that still works but has become very slow is an incident: quality of service is reduced."),
        tip="'Unplanned interruption OR reduction in quality' — the reduction half is frequently the tested part.",
    ),

    228: dict(
        title="IT Asset Management",
        points=[
            "PURPOSE: to plan and manage the full lifecycle of all IT assets, to help the organisation maximise value, control costs, manage risks and support decision-making about purchase, reuse and retirement.",
            "An IT ASSET is any financially valuable component that can contribute to the delivery of an IT product or service.",
            "Covers the full lifecycle: acquisition, deployment, operation, maintenance, and disposal or retirement.",
            "Supports licence compliance — knowing what is owned prevents both over-buying and under-licensing.",
            "Distinct from configuration management: assets are about FINANCIAL value; CIs are about SERVICE relationships.",
        ],
        example=("Why it saves money",
                 "An accurate asset register reveals 300 licences paid for and unassigned after a restructure."),
        tip="IT asset management = financial value and lifecycle. Service configuration management = relationships between components.",
    ),

    229: dict(
        title="Monitoring and Event Management",
        points=[
            "PURPOSE: to systematically observe services and service components, and record and report selected changes of state identified as events.",
            "An EVENT is any change of state that has significance for the management of a service or other configuration item.",
            "Events are typically classified as INFORMATIONAL, WARNING or EXCEPTION.",
            "Informational: no action needed. Warning: something is approaching a threshold. Exception: a breach requiring action.",
            "This practice identifies and prioritises events, and establishes the right response — including raising an incident.",
        ],
        example=("The three types",
                 "Informational: a backup completed. Warning: disk 85% full. Exception: disk full and the service has stopped."),
        tip="Informational / warning / exception — know all three and that an exception may trigger an incident.",
    ),

    239: dict(
        title="Configuration Items and the CMDB",
        points=[
            "A CONFIGURATION ITEM (CI) is any component that needs to be managed in order to deliver an IT service.",
            "CIs include hardware, software, networks, buildings, people, suppliers and documentation.",
            "A CONFIGURATION MANAGEMENT DATABASE (CMDB) stores configuration records and the RELATIONSHIPS between CIs.",
            "The value is in the relationships: they let you see what a change or failure will actually affect.",
            "Collect only the CI data that is genuinely needed — an over-detailed CMDB becomes inaccurate and is then trusted by nobody.",
        ],
        example=("Why relationships matter",
                 "Rebooting one server is safe or catastrophic depending on which services depend on it — the CMDB is what tells you."),
        tip="A CI is anything needing management to deliver a service — including people and documentation, not just kit.",
    ),

    243: dict(
        title="Service Level Agreements",
        points=[
            "A SERVICE LEVEL AGREEMENT (SLA) is a documented agreement between a service provider and a customer that identifies both the services required and the expected level of service.",
            "The purpose of service level management is to set clear business-based targets for service performance, so delivery can be properly assessed, monitored and managed.",
            "SLAs must be written in business terms the customer recognises — not in technical metrics only IT understands.",
            "Beware the 'watermelon SLA': green on every technical metric, red in the customer's actual experience.",
            "SLAs require regular review: targets that no longer reflect business need are worse than no targets at all.",
        ],
        example=("Watermelon SLA",
                 "99.9% server uptime reported as success, while the login service was unusable every Monday morning."),
        tip="'Clear BUSINESS-BASED targets' is the phrase — service level management is not a technical metrics exercise.",
    ),

    247: dict(
        title="Deployment Management",
        points=[
            "PURPOSE: to move new or changed hardware, software, documentation, processes or any other component to live environments.",
            "It may also be involved in deploying components to other environments, such as test or staging.",
            "Deployment is DISTINCT from release: deployment moves a component; release makes it available to users.",
            "Common approaches: phased deployment, continuous delivery, big-bang deployment, and pull deployment.",
            "It is one of the three TECHNICAL MANAGEMENT practices in ITIL 4.",
        ],
        example=("Deploy vs release",
                 "Code deployed behind a feature flag is live on the servers but not released — users see nothing until the flag flips."),
        tip="Deployment = moving it. Release = making it available to users. The two are deliberately separated.",
    ),

    205: dict(
        title="What Is a Practice?",
        points=[
            "A PRACTICE is a set of organisational resources designed for performing work or accomplishing an objective.",
            "ITIL 4 defines 34 practices, grouped into three categories.",
            "GENERAL MANAGEMENT practices (14) — adopted from general business, e.g. continual improvement, information security management, relationship management, supplier management.",
            "SERVICE MANAGEMENT practices (17) — developed in service management, e.g. incident management, problem management, change enablement, service desk, service level management.",
            "TECHNICAL MANAGEMENT practices (3) — adapted from technology management, e.g. deployment management, infrastructure and platform management, software development and management.",
        ],
        example=("Practices, not processes",
                 "A practice includes the people, tools, information and processes needed — it is broader than a process alone."),
        tip="34 practices in 3 groups: 14 general management, 17 service management, 3 technical management.",
    ),
}
