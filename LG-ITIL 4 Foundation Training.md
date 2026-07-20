# ITIL 4 Foundation Training — Learner Guide

**WSQ Course Code:** TGS-2024049350  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v12.0 · 20 July 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Skills Framework Alignment](#skills-framework-alignment)
- [Before You Start](#before-you-start)
- [Topic 01 — Understand Key Concepts of Service Management  (25%)](#topic-01--understand-key-concepts-of-service-management--25)
  - [Activity 1 — Case Study: MediCare Health Group — Scenario Analysis from an ITIL Context](#activity-1--case-study-medicare-health-group--scenario-analysis-from-an-itil-context)
- [Topic 02 — ITIL Guiding Principles  (20%)](#topic-02--itil-guiding-principles--20)
  - [Activity 2 — Group Activity: Applying an ITIL Guiding Principle in Your Organisation](#activity-2--group-activity-applying-an-itil-guiding-principle-in-your-organisation)
- [Topic 03 — The Four Dimensions of Service Management  (15%)](#topic-03--the-four-dimensions-of-service-management--15)
  - [Activity 3 — Group Activity: Analysing a Service Across the Four Dimensions](#activity-3--group-activity-analysing-a-service-across-the-four-dimensions)
- [Topic 04 — The Service Value System  (20%)](#topic-04--the-service-value-system--20)
  - [Activity 4 — Group Activity: Service Value Chain Inputs and Outputs](#activity-4--group-activity-service-value-chain-inputs-and-outputs)
- [Topic 05 — ITIL Practices  (20%)](#topic-05--itil-practices--20)
  - [Activity 5 — Group Activity: Triaging Incidents, Problems, Changes and Service Requests](#activity-5--group-activity-triaging-incidents-problems-changes-and-service-requests)
- [Key Distinctions to Master](#key-distinctions-to-master)
- [Quick Reference — The Seven Guiding Principles](#quick-reference--the-seven-guiding-principles)
- [Quick Reference — The Six Service Value Chain Activities](#quick-reference--the-six-service-value-chain-activities)
- [Assessment Preparation](#assessment-preparation)
- [Glossary](#glossary)


## Introduction

This Learner Guide accompanies the WSQ course ITIL 4 Foundation Training (TGS-2024049350), conducted by Tertiary Infotech Academy Pte Ltd. It provides step-by-step instructions for all 5 in-class activities, organised by the 5 course topics. Every activity maps to a learning outcome and to the Skills Framework TSC Infrastructure Support (ICT-OUS-3007-1.1).

Use this guide alongside the course slides and the in-class group activities. ITIL 4 Foundation is a knowledge-based course: the activities are group discussions, case-study analyses and scenario triage exercises rather than software labs, so the value comes from working through the reasoning with your group and defending your conclusions to the class.

Definitions matter in ITIL. Many assessment questions turn on the precise distinction between two similar terms — output and outcome, utility and warranty, incident and problem, service request and incident. Where this guide gives a definition, learn it as written.


## Course Learning Outcomes

- LO1: Explain the key concepts of service management, including services, value, outcomes, costs, risks, utility and warranty, and the roles of service providers and consumers. (K1, A1)
- LO2: Apply the seven ITIL guiding principles to service management decisions and improvement initiatives in the workplace. (K2, A2)
- LO3: Describe the four dimensions of service management and evaluate how each dimension affects the delivery of a service. (K3, A3, A4)
- LO4: Explain the ITIL service value system and the six service value chain activities, and apply the continual improvement model. (K4, A5, A6)
- LO5: Describe the purpose of the key ITIL practices and apply them to incident, problem, change and service request scenarios. (K5, K6, A7, A8)


## Skills Framework Alignment

This course is aligned to the Skills Framework TSC Infrastructure Support (ICT-OUS-3007-1.1).

**Abilities assessed**

- A1: Diagnose underlying technical problems or issues causing incidents and disruptions in infrastructure and network operations
- A2: Implement problem management procedures to resolve root causes of infrastructure-related incidents
- A3: Provide end-to-end management of technical issues and problems encountered by users within an agreed timeframe
- A4: Perform infrastructure configuration and support activities at a higher level of difficulty or complexity
- A5: Develop an action plan and timeline for infrastructure upgrade activities
- A6: Propose ideas for infrastructure related upgrades and improvements based on current and future user needs
- A7: Test infrastructure systems in advance to assess impact of potential upgrades or updates on performance level
- A8: Organise information for the development of user guides and training materials for infrastructure administration activities

**Knowledge assessed**

- K1: Diagnostic tools and processes to identify technical issues or disruptions in network infrastructure
- K2: Infrastructure and network configuration techniques
- K3: Troubleshooting techniques for infrastructure technical issues and problems
- K4: Potential benefits and impact of infrastructure upgrades
- K5: Sources of information and content for user guides and materials
- K6: Types of system tests and their purpose


## Before You Start

**What you need**

- No prior ITIL certification or technical prerequisite is required.
- Familiarity with an IT support, IT operations or service delivery environment is helpful but not essential.
- Bring a real service or workplace situation to discuss — several activities ask you to apply ITIL concepts to your own organisation.
- The course slides and this Learner Guide are the approved open-book materials for the assessment.

**Conventions used in every activity**

- Each activity states the learning outcome it maps to, so you can trace it back to the assessment.
- Activities are done in small groups of 2–3 persons; each group presents its findings to the class.
- 'Check your work' at the end of each activity is the standard your group's output should meet.
- Key ITIL terms appear in the Glossary at the end of this guide — learn the exact definitions.
- Record the assumptions your group makes; being able to justify an assumption is part of the skill.


## Topic 01 — Understand Key Concepts of Service Management  (25%)

Services · Value · Outcomes, Costs and Risks · Providers and Consumers · Utility and Warranty

**Key concepts**

- A service is a means of enabling value co-creation by facilitating outcomes customers want to achieve, without the customer having to manage specific costs and risks.
- Service management is a set of specialised organisational capabilities for enabling value to customers in the form of services.
- Value is co-created through an active relationship between the service provider and the service consumer.
- Service consumers take on the roles of customer, user and sponsor; providers deliver service offerings made up of goods, access to resources and service actions.
- Outputs are deliverables of an activity; outcomes are the results a stakeholder actually achieves, enabled by those outputs.
- Utility is what the service does (fit for purpose); warranty is how the service performs (fit for use).


### Activity 1 — Case Study: MediCare Health Group — Scenario Analysis from an ITIL Context

Learning outcome: LO1 (K1, A1) — Explain services, value, outcomes, costs, risks and the roles of service providers and consumers.

Goal: MediCare Health Group, established in 1995, operates a network of private clinics and two specialist medical centres across Southeast Asia, employing more than 8,000 clinical and administrative staff across Singapore, Malaysia, Thailand, Indonesia, Vietnam and the Philippines. Rising middle-class incomes, greater health awareness, government subsidies for preventive screening and widespread smartphone adoption have created strong demand for private healthcare. MediCare has launched Essential, Advanced and Executive health screening packages, each bundling diagnostic tests, a digital health report, teleconsultation and a period of access to its online patient portal. Results are promised within 5 business days, backed by a 24x7 support hotline and a portal chatbot that escalates to a human officer. As the group expands, the IT Director has been asked to evaluate a service management solution that will give better insight into patient outcomes, service performance and clinic utilisation. Working in small groups of 2-3, analyse this scenario through an ITIL lens.

**What you'll produce**

A completed group analysis identifying opportunity, value, external factors, the service offering components and the selection criteria for a service management solution.   (Materials: Case study brief, ITIL 4 Foundation slides, Learner Guide.)

**Step-by-step**

1. Divide the class into 2-4 small groups, each with 2-3 persons, and read the MediCare Health Group scenario in full.
2. Question 1: List examples of opportunity and value in the scenario. Distinguish the opportunity MediCare is pursuing from the value co-created for its patients.
3. Question 2: Identify the external factors MediCare is leveraging. Use PESTLE (political, economic, social, technological, legal, environmental) to structure your answer.
4. Question 3: Identify the goods, the access to resources and the service actions that make up the health screening service offering. Apply the ownership test to each.
5. Question 4: Determine the consideration factors the IT Director should apply when evaluating a service management solution. Structure them using the four dimensions of service management.
6. Document any assumptions your group made — market conditions, patient behaviours or technological capabilities available to MediCare.
7. Each group presents its findings to the class, clearly justifying its answers and stating its assumptions.

**Check your work**

Your group can justify, for each of the four questions, which ITIL concept it applied and why — and can defend its assumptions when challenged by another group.

---


## Topic 02 — ITIL Guiding Principles  (20%)

Focus on Value · Start Where You Are · Progress Iteratively · Collaborate · Think Holistically · Keep It Simple · Optimize and Automate

**Key concepts**

- A guiding principle is a recommendation that guides an organisation in all circumstances, regardless of changes in goals, strategies or type of work.
- Focus on value: everything the organisation does should link back, directly or indirectly, to value for itself, its customers and its stakeholders.
- Start where you are: assess and reuse what already exists rather than discarding it and rebuilding from scratch.
- Progress iteratively with feedback: organise work into smaller manageable sections, executed and completed in a timely manner, using feedback at each iteration.
- Collaborate and promote visibility: involve the right people in the right roles to improve buy-in, relevance and the likelihood of long-term success.
- Think and work holistically, keep it simple and practical, and optimize before you automate.


### Activity 2 — Group Activity: Applying an ITIL Guiding Principle in Your Organisation

Learning outcome: LO2 (K2, A2) — Apply the seven ITIL guiding principles to service management decisions and improvement initiatives.

Goal: The seven ITIL guiding principles are recommendations that hold in all circumstances, regardless of changes to an organisation's goals, strategies or type of work. Knowing the principles is not the same as being able to apply them. In this activity each group selects one guiding principle and works it through against a real situation from a member's own workplace, producing a concrete application rather than a restatement of the definition.

**What you'll produce**

A worked application of one guiding principle to a real workplace situation, with the specific actions it implies.   (Materials: ITIL 4 Foundation slides, Learner Guide, workplace examples from group members.)

**Step-by-step**

1. Divide the class into 2-4 small groups, each with 2-3 persons.
2. As a group, select ONE of the seven guiding principles: focus on value, start where you are, progress iteratively with feedback, collaborate and promote visibility, think and work holistically, keep it simple and practical, or optimize and automate.
3. Have each member briefly describe a current situation or improvement initiative in their own organisation. Choose one to work with.
4. State the principle in your own words, then explain specifically how it applies to the chosen situation.
5. List the concrete actions the principle would lead you to take — and, just as importantly, the actions it would lead you to STOP taking.
6. Identify what would be at risk if the principle were ignored in this situation.
7. Present your analysis to the class and take questions.

**Check your work**

Your group can explain how the selected principle changes what you would actually do in the chosen situation — not merely restate its definition.

---


## Topic 03 — The Four Dimensions of Service Management  (15%)

Organizations and People · Information and Technology · Partners and Suppliers · Value Streams and Processes

**Key concepts**

- The four dimensions ensure a holistic approach to service management; every component of the SVS must be considered from all four.
- Organizations and people covers roles, responsibilities, structures, culture and the competencies needed to deliver the service.
- Information and technology covers the information and knowledge required, plus the technologies that support and enable the service.
- Partners and suppliers covers relationships with other organisations involved in the design, deployment, delivery and support of services.
- Value streams and processes covers how the parts of the organisation work together, in an integrated and coordinated way, to enable value creation.
- External factors — political, economic, social, technological, legal and environmental (PESTLE) — constrain and shape all four dimensions.


### Activity 3 — Group Activity: Analysing a Service Across the Four Dimensions

Learning outcome: LO3 (K3, A3, A4) — Describe the four dimensions of service management and evaluate how each affects service delivery.

Goal: ITIL 4 requires a holistic approach: every component of the service value system must be considered from all four dimensions — organizations and people, information and technology, partners and suppliers, and value streams and processes. Neglecting a dimension is a common cause of service failure. In this activity groups take a familiar service and work it through all four dimensions, then identify which dimension is weakest and what that costs.

**What you'll produce**

A four-dimension analysis of a real service, with the weakest dimension identified and justified.   (Materials: ITIL 4 Foundation slides, Learner Guide, PESTLE framework.)

**Step-by-step**

1. Divide the class into 2-4 small groups, each with 2-3 persons.
2. Select a service your group knows well — a corporate IT service desk, an email service, a cloud hosting service or a service from a member's workplace.
3. Organizations and people: identify the roles, responsibilities, structures, culture and competencies the service depends on.
4. Information and technology: identify the information and knowledge required, and the technologies that support and enable the service.
5. Partners and suppliers: identify the external organisations involved in designing, deploying, delivering or supporting the service, and the dependencies they create.
6. Value streams and processes: map at a high level how the parts of the organisation work together to deliver the service end to end.
7. Apply PESTLE to identify the external factors that constrain the service across the dimensions.
8. Decide which of the four dimensions is currently weakest for this service, and explain the specific impact that weakness has on the value delivered.
9. Present your analysis to the class.

**Check your work**

Your group can name the weakest dimension for the chosen service and trace a concrete service failure or risk directly back to it.

---


## Topic 04 — The Service Value System  (20%)

ITIL SVS · Plan · Improve · Engage · Design and Transition · Obtain/Build · Deliver and Support

**Key concepts**

- The ITIL service value system describes how all components and activities of the organisation work together as a system to enable value creation.
- The SVS comprises guiding principles, governance, the service value chain, practices and continual improvement; its inputs are opportunity and demand.
- The service value chain is a set of six interconnected activities an organisation performs to deliver a valuable product or service to its consumers.
- Plan ensures a shared understanding of vision, status and improvement direction; improve ensures continual improvement of products, services and practices.
- Engage provides understanding of stakeholder needs and transparency; design and transition ensures products and services continually meet expectations.
- The continual improvement model runs from 'What is the vision?' through to 'How do we keep the momentum going?' in seven steps.


### Activity 4 — Group Activity: Service Value Chain Inputs and Outputs

Learning outcome: LO4 (K4, A5, A6) — Explain the ITIL service value system and the six service value chain activities.

Goal: The service value chain is a set of six interconnected activities an organisation performs to deliver a valuable product or service to its consumers. Each activity converts inputs into outputs, and the outputs of one activity commonly become the inputs of another — which is what makes the chain a system rather than a sequence. In this activity groups work through three of the six activities in detail, tracing what flows in and what flows out.

**What you'll produce**

Completed input/output tables for the 'Deliver and Support', 'Engage' and 'Design and Transition' value chain activities, with explanations.   (Materials: ITIL 4 Foundation slides, Learner Guide, service value chain diagram.)

**Step-by-step**

1. Divide the class into 2-4 small groups, each with 2-3 persons.
2. Review the service value chain diagram and confirm the six activities: plan, improve, engage, design and transition, obtain/build, and deliver and support.
3. For the 'Deliver and Support' activity, list the possible inputs and their corresponding outputs in a table.
4. For the 'Engage' activity, list the possible inputs and their corresponding outputs in a table.
5. For the 'Design and Transition' activity, list the possible inputs and their corresponding outputs in a table.
6. Explain each answer: why is that an input to this activity, and where does the output flow to next?
7. Trace at least one output from one of your three activities to the activity that consumes it as an input, demonstrating the interconnection.
8. Present your tables and explanations to the class.

**Check your work**

Your group can trace a complete path through the value chain — showing an output of one activity becoming the input of another — and explain why the chain is a system, not a linear process.

---


## Topic 05 — ITIL Practices  (20%)

Continual Improvement · Change Enablement · Incident · Problem · Service Request · Service Desk · Service Level Management

**Key concepts**

- A practice is a set of organisational resources designed for performing work or accomplishing an objective; ITIL 4 defines 34 practices in three groups.
- Incident management minimises the negative impact of incidents by restoring normal service operation as quickly as possible.
- Problem management reduces the likelihood and impact of incidents by identifying actual and potential causes; a known error is an analysed problem not yet resolved.
- Change enablement maximises the number of successful IT changes by ensuring risks are properly assessed and changes authorised by a change authority.
- The service desk captures demand for incident resolution and service requests, and is the entry point and single point of contact for users.
- Service level management sets clear business-based targets for service performance, documented in service level agreements (SLAs).


### Activity 5 — Group Activity: Triaging Incidents, Problems, Changes and Service Requests

Learning outcome: LO5 (K5, K6, A7, A8) — Describe the purpose of the key ITIL practices and apply them to real scenarios.

Goal: The most common practical error at Foundation level is misclassifying work: logging a service request as an incident, treating a recurring incident as a series of unrelated incidents rather than a problem, or pushing an undocumented change straight into production. In this activity groups triage a set of realistic scenarios, decide which practice owns each one, and justify the decision — then design the handling path.

**What you'll produce**

A triaged scenario set with the owning practice identified for each, plus a handling path for the most complex scenario.   (Materials: ITIL 4 Foundation slides, Learner Guide, practice definitions.)

**Step-by-step**

1. Divide the class into 2-4 small groups, each with 2-3 persons.
2. Scenario A: A user calls the service desk because they cannot access the shared drive. No one else is affected. Which practice owns this, and why?
3. Scenario B: The shared drive has failed four times this month, each time restored by a restart. Which practice owns this, and how does it differ from Scenario A?
4. Scenario C: A new employee needs a laptop, an email account and access to the CRM. Which practice owns this, and why is it not an incident?
5. Scenario D: The infrastructure team wants to apply an urgent security patch to the production database this evening. Which practice owns this, and what change type applies?
6. Scenario E: The business complains that the service desk 'never resolves anything on time', but no target has ever been agreed. Which practice owns this, and what artefact is missing?
7. For each scenario, state the practice, its purpose in your own words, and the key term that determines the classification (incident, problem, known error, workaround, service request, change, SLA).
8. Select the most complex scenario and design its end-to-end handling path, naming every practice it touches from initial contact to closure.
9. Present your triage decisions to the class and defend any the other groups classified differently.

**Check your work**

Your group can correctly classify all five scenarios and explain the distinguishing test between an incident and a problem, and between a service request and an incident.

---


## Key Distinctions to Master

Foundation-level questions frequently test whether you can separate these closely related terms. Be able to state the difference in one sentence and give an example of each.

**Output vs Outcome**

- Output — a tangible or intangible deliverable of an activity (a delivered package, a completed task, a generated report).
- Outcome — a result for a stakeholder, enabled by one or more outputs (the stakeholder can now do something they could not before).
- Test: if you can hand it over, it is an output; if it is a change in the stakeholder's situation, it is an outcome.

**Utility vs Warranty**

- Utility — what the service DOES; the functionality offered to meet a particular need. Fit for purpose.
- Warranty — how the service PERFORMS; availability, capacity, reliability, security and continuity. Fit for use.
- A service needs BOTH to deliver value: functionality that is unavailable delivers nothing.

**Incident vs Problem vs Known Error**

- Incident — an unplanned interruption to a service, or a reduction in the quality of a service. Restore service as quickly as possible.
- Problem — a cause, or potential cause, of one or more incidents. Reduce likelihood and impact.
- Known error — a problem that has been analysed and has not been resolved. Often managed with a workaround.
- Workaround — a solution that reduces or eliminates the impact of an incident or problem for which a full resolution is not yet available.

**Service Request vs Incident**

- Service request — a request from a user or their authorised representative that initiates a normal, pre-defined service action.
- Incident — something is broken or degraded that should not be.
- Test: was the service working as designed? If yes and the user simply wants something, it is a service request.

---


## Quick Reference — The Seven Guiding Principles

- Focus on value — everything links back, directly or indirectly, to value for the organisation, its customers and its stakeholders.
- Start where you are — assess and reuse what already exists rather than discarding it and rebuilding.
- Progress iteratively with feedback — organise work into smaller sections, using feedback at each iteration.
- Collaborate and promote visibility — involve the right people in the right roles; make work visible.
- Think and work holistically — no service, practice, process, department or supplier stands alone.
- Keep it simple and practical — use the minimum number of steps to accomplish an objective.
- Optimize and automate — optimize the process first, then automate; never automate a broken process.

---


## Quick Reference — The Six Service Value Chain Activities

- Plan — ensures a shared understanding of the vision, current status and improvement direction.
- Improve — ensures continual improvement of products, services and practices across all value chain activities.
- Engage — provides a good understanding of stakeholder needs, transparency and continual engagement.
- Design and transition — ensures products and services continually meet stakeholder expectations for quality, cost and time to market.
- Obtain/build — ensures service components are available when and where needed, and meet agreed specifications.
- Deliver and support — ensures services are delivered and supported according to agreed specifications and stakeholder expectations.

---


## Assessment Preparation

- The assessment is Written Assessment (SAQ) plus a Case Study, both open book.
- Open book means the course slides, this Learner Guide and approved materials ONLY.
- Re-read the Key Distinctions section — questions often hinge on separating two similar terms.
- Be able to state the purpose of each ITIL practice covered in Topic 5 in one sentence.
- Be able to name and explain all seven guiding principles, and apply one to a given scenario.
- For the case study, practise identifying opportunity, value, service offering components and external factors in a written scenario.
- A minimum of 75% attendance is required to be eligible for the assessment and for funding.


## Glossary

- **Service** — A means of enabling value co-creation by facilitating outcomes that customers want to achieve, without the customer having to manage specific costs and risks.
- **Service management** — A set of specialised organisational capabilities for enabling value to customers in the form of services.
- **Value** — The perceived benefits, usefulness and importance of something.
- **Value co-creation** — Value is created jointly by the provider and the consumer through an active service relationship — not delivered one way.
- **Output** — A tangible or intangible deliverable of an activity.
- **Outcome** — A result for a stakeholder, enabled by one or more outputs.
- **Utility** — The functionality offered by a product or service to meet a particular need — 'fit for purpose'.
- **Warranty** — Assurance that a product or service will meet agreed requirements — 'fit for use'.
- **Service offering** — A formal description of one or more services, designed to address the needs of a target consumer group; may include goods, access to resources and service actions.
- **Service relationship** — A cooperation between a service provider and a service consumer to co-create value.
- **Customer / User / Sponsor** — The consumer roles: the customer defines requirements and owns the outcomes; the user uses the service; the sponsor authorises the budget.
- **Service value system (SVS)** — How all the components and activities of the organisation work together as a system to enable value creation.
- **Service value chain** — The set of six interconnected activities an organisation performs to deliver a valuable product or service.
- **Practice** — A set of organisational resources designed for performing work or accomplishing an objective. ITIL 4 defines 34 practices.
- **Guiding principle** — A recommendation that guides an organisation in all circumstances, regardless of changes in goals, strategies or type of work.
- **Continual improvement** — A recurring organisational activity performed at all levels to ensure performance continually meets stakeholder expectations.
- **Incident** — An unplanned interruption to a service, or a reduction in the quality of a service.
- **Problem** — A cause, or potential cause, of one or more incidents.
- **Known error** — A problem that has been analysed and has not been resolved.
- **Workaround** — A solution that reduces or eliminates the impact of an incident or problem for which a full resolution is not yet available.
- **Service request** — A request from a user or a user's authorised representative that initiates a normal, pre-defined service action.
- **Change** — The addition, modification or removal of anything that could have a direct or indirect effect on services.
- **Change authority** — The person or group who authorises a change.
- **Configuration item (CI)** — Any component that needs to be managed in order to deliver an IT service.
- **Service level agreement (SLA)** — A documented agreement between a service provider and a customer identifying both the services required and the expected level of service.
- **Event** — Any change of state that has significance for the management of a service or other configuration item.
- **Four dimensions** — Organizations and people; information and technology; partners and suppliers; value streams and processes.
- **PESTLE** — Political, economic, social, technological, legal and environmental — the external factors that constrain an organisation.
