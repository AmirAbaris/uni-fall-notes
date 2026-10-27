---
course: "[[01 Courses/Software Design Principles/Course|Software Design Principles]]"
type: assignment
due:
status: in-progress
tags:
  - software-design
  - presentation
  - weeto
---
****# Semester Presentation Project — Weeto

## Presentation requirements

The instructor's listed requirements for the current stage are:

1. Select a subject.
2. Prepare an organizational chart (نمودار سازمانی).
3. Prepare a data-flow diagram (DFD).

This note records the selected subject and the two diagrams. Extend the same Weeto project as later weekly requirements are assigned.

## 1. Selected subject

### Title

**Analysis and design of Weeto: a Persian-first interview scheduling system**
**تحلیل و طراحی ویتو: سامانهٔ فارسی‌محور زمان‌بندی مصاحبه‌های استخدامی**

### Short description

Weeto helps hiring teams schedule interviews without the usual back-and-forth messages. A recruiter configures an organization, an interview type and availability, then shares a public booking link. A candidate chooses an available slot and provides contact details. Weeto records the booking, supports token-based rescheduling and cancellation, optionally creates a Google Calendar event with a Meet link, and queues email notifications.

### Problem and goal

Recruiters often coordinate interviews through chat and manual calendar work. This creates delays, repeated messages, forgotten meetings and avoidable no-shows. Weeto aims to make booking self-service and reduce that coordination effort, with Persian-first product goals such as a familiar local experience and Tehran time-zone support.

### Scope for this presentation

- Recruiter account and organization setup.
- Interview types and availability rules.
- Public listing of available slots and candidate booking.
- Recruiter booking list and cancellation.
- Candidate rescheduling and cancellation through secure links.
- Optional Google Calendar/Meet connection.
- Email notifications through a background outbox worker.

### Current implementation versus product vision

The backend repository is a Go HTTP API backed by PostgreSQL. Its routes and migrations support the core booking flow, Google integration, and an email notification outbox/worker. The checked code does **not** implement SMS delivery. The latest meeting-provider migration uses `google_meet` and `on_site`; therefore SMS and Bale/custom-link support should be presented as future/product-vision items, not as currently implemented backend features.

## 2. Organizational chart (نمودار سازمانی)

### Basis and assumptions

Cal.com is used as inspiration for the functions and founder responsibilities. Cal.com's public materials identify Bailey Pumfleet as CEO and Peer Richelsen as Chairman; its company/team description says Bailey leads go-to-market, marketing, sales and the rest of the business, while Peer leads product and engineering. Cal.com's team directory lists functions including Engineering, Platform, Product, Support, Enterprise, Compliance, Marketing, Growth and Sales. The public sources do **not** publish a complete reporting-line chart or explicitly say that Peer reports to Bailey.

For this university assignment, the Weeto diagram shows a conventional company hierarchy: the CEO is at the top, with Product & Engineering, Go-to-Market, and Operations & Customer Experience leads reporting to the CEO. The departments beneath them adapt Cal.com's published team functions to Weeto's needs. This is a **proposed Weeto hierarchy informed by Cal.com's published roles and teams**, not a claim about Cal.com's exact reporting lines or Weeto's current employees.

Open the organizational chart on its own note for a clearer, full-width view:
[[01 Courses/Software Design Principles/Assignments/Weeto Organizational Chart|Weeto Organizational Chart]].

### How to explain it

- **CEO / Founder:** owns company direction and coordinates the functions. At the MVP stage, this may be the founder wearing several hats.
- **Product:** product management (PM), user experience/design (UX), and user research shape the roadmap and Persian-first booking experience.
- **Engineering:** backend, frontend, quality assurance (QA), integrations, infrastructure, security and privacy deliver and operate the platform.
- **Growth & Market:** marketing, sales and customer success find hiring teams, grow adoption and help organizations get value from Weeto.
- **Operations:** support, finance and administration handle user requests and routine business operations.

**MVP reality:** The PRD describes a solo-developer build. This chart represents a sensible structure as Weeto grows; initially one person can cover multiple functions and some responsibilities can be outsourced. Do not imply all positions are currently staffed.

## 3. Data-flow diagram (DFD / نمودار جریان داده)

### DFD Level 0 — Context diagram

The whole Weeto system is shown as one process and its exchanges with outside actors/services.

Open the context diagram on its own note:
[[01 Courses/Software Design Principles/Assignments/Weeto DFD Level 0 - Context|Weeto DFD Level 0 — Context]].

### DFD Level 1 — Interview booking flow

Open the booking-process diagram on its own note:
[[01 Courses/Software Design Principles/Assignments/Weeto DFD Level 1 - Booking|Weeto DFD Level 1 — Booking]].

### DFD notes and implementation mapping

- The public booking flow is implemented under `/public/{orgSlug}/{typeSlug}` routes. The recruiter manages organization, interview type, availability and bookings through authenticated routes.
- Data stores correspond to PostgreSQL tables such as `users`, `refresh_tokens`, `organization`, `interview_type`, `availability_*`, `slots`, `booking` and `notification_outbox`.
- Booking and slot availability must be coordinated safely to prevent two candidates from taking the same slot. The database enforces a unique active booking per slot.
- The notification outbox lets the booking operation save notification work, then a separate worker sends email. Email sending is implemented; SMS is not shown in this DFD as an implemented flow.
- Google Calendar/Meet is conditional: it is used for interview types configured for Google Meet and a connected recruiter account. On-site interviews do not need that external flow.

## Repository evidence

- Product problem, target users, scope and implementation plan: [Weeto backend PRD](../../../../weeto-backend/docs/PRD.md) (local repository: `/Users/amirabaris/Documents/weeto-backend/docs/PRD.md`).
- API routes: `/Users/amirabaris/Documents/weeto-backend/internal/server/routes.go`.
- API dependency wiring: `/Users/amirabaris/Documents/weeto-backend/cmd/api/main.go`.
- Background notification worker: `/Users/amirabaris/Documents/weeto-backend/cmd/worker/main.go` and `/Users/amirabaris/Documents/weeto-backend/internal/worker/notification/processor.go`.
- Tables and constraints: `/Users/amirabaris/Documents/weeto-backend/db/migrations/`.

## Cal.com inspiration and references

- [Cal.com About](https://cal.com/about) — mission, product scope and company approach.
- [Cal.com About — team and founder roles](https://www.cal-staging.com/about) — describes Peer Richelsen's product/engineering role and Bailey Pumfleet's CEO/go-to-market role; also describes the distributed team functions.
- [Cal.com Open — leadership titles](https://next.cal.com/open) — lists Peer Richelsen as Co-Founder/Chairman and Bailey Pumfleet as Co-Founder/CEO; it does not specify their reporting relationship.
- [Cal.com public team directory](https://i.cal.com/) — shows team groups such as Engineering, Platform, Product, Support, Enterprise, Compliance, Marketing, Growth and Sales. Team groups do not by themselves prove reporting lines.
- [Cal.com Teams](https://cal.com/teams) — describes customer use cases such as marketing and customer success; this is product positioning, not an employee org chart.

## Weekly progress

| Week / date | Instructor's assignment | Addition to the project | Deliverable / link | Status |
| --- | --- | --- | --- | --- |
| 2026-10-12 | Choose a semester presentation subject | Selected Weeto, an interview scheduling system | This note | Done |
| 2026-10-26 | Organizational chart and DFD | Proposed Cal.com-inspired Weeto organization chart; DFD context and Level 1 booking flow | This note | Done |

## Next steps

- [ ] Confirm presentation duration, format, and grading rubric with the instructor.
- [ ] Add each new weekly requirement here and extend the same Weeto design.
- [ ] Turn the diagrams into presentation-ready slides after the complete semester requirements are known.

## What I learned

- An organizational chart represents people/functions and reporting responsibility; it is different from a software architecture diagram.
- A DFD shows actors, processes, data stores and the data exchanged between them.
- Product vision and implemented code must be labeled separately when presenting a real project.
