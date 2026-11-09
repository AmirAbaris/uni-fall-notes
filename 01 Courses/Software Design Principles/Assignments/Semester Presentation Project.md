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

The organizational chart has been redesigned as a realistic, scalable, enterprise-grade technology company hierarchy (inspired by mature SaaS benchmarks like Cal.com, Slack, and Zoom). Instead of an oversimplified three-box structure, it reflects a complete executive leadership (C-Suite) and specialized functional departments that support scaling from seed stage to series A/B.

The organizational hierarchy includes:
- **Board of Directors (هیئت مدیره) & CEO (مدیرعامل):** Corporate governance, strategy, and overall executive direction, supported by Chief of Staff & Legal Counsel.
- **Technology & Engineering (CTO):** Core software engineering (Backend, Frontend, Integrations), Cloud Infrastructure/DevOps (SRE & security), and QA/Test Automation.
- **Product & Design (CPO):** Core and Enterprise Product Managers, UI/UX Designers, User Researchers, and Product Data Analysts.
- **Marketing & Growth (CMO):** Performance/growth marketing, content marketing, social media, and brand/PR.
- **Sales & Business Development (VP of Sales):** Enterprise B2B sales and strategic partnerships with job portals and ATS systems.
- **Operations & Customer Experience (COO):** Customer Success (enterprise onboarding and retention), 24/7 technical support helpdesk, and SLA compliance.
- **Finance, Legal & People (CFO):** People operations / HR, talent acquisition, and finance & accounting.

Open the organizational chart on its own note for a clearer, full-width view:
[[01 Courses/Software Design Principles/Assignments/Weeto Organizational Chart|Weeto Organizational Chart]].

### How to explain it

- **Executive & Governance:** Clear separation between board governance and daily operational C-suite execution.
- **Scalable Divisions:** Each department has specialized leads and contributor roles, avoiding bottlenecking multiple disparate functions into a single vague bucket.
- **Growth Stage Reality:** In early MVP stages, co-founders wear multiple hats (e.g., technical founder spans CTO + Product). As the company scales and secures enterprise contracts, departments naturally populate their designated teams without restructuring the company's organizational DNA.

## 3. Data-flow diagram (DFD / نمودار جریان داده)

### DFD Level 0 — Context diagram

The whole Weeto system is shown as one central process (`سامانهٔ Weeto`) interacting with outside actors and external cloud services:
- **Recruiter (مسئول استخدام):** sets up account, organization, interview types, and availability.
- **Candidate (داوطلب):** queries available slots and books/manages appointments.
- **Google Calendar / Meet:** cloud calendar and meeting provider for generating online video links.
- **Email Service (سرویس ایمیل):** external service for delivering confirmation and reminder emails.

Open the context diagram on its own note:
[[01 Courses/Software Design Principles/Assignments/Weeto DFD Level 0 - Context|Weeto DFD Level 0 — Context]].

### DFD Level 1 — Interview booking flow (Refactored to Academic Scope)

Following direct instructor feedback regarding class progress, **DFD Level 1 has been refactored to focus strictly on functional decomposition and service-to-service data flows**, deliberately omitting database data stores (`D1..D5`) and advanced backend plumbing (such as outbox queues, worker daemons, and token hashes):
1. `1.0` مدیریت حساب و مشخصات سازمان (Account & Organization Setup)
2. `2.0` تنظیم انواع مصاحبه و ساعات کاری مجاز (Interview Type & Availability Setup)
3. `3.0` استعلام و نمایش زمان‌های آزاد (Slot Availability & Discovery)
4. `4.0` ثبت و مدیریت نوبت مصاحبه (Booking, Rescheduling & Cancellation)
5. `5.0` آماده‌سازی و ارسال اعلان‌ها (Notification & Email Dispatch)

Open the booking-process diagram on its own note:
[[01 Courses/Software Design Principles/Assignments/Weeto DFD Level 1 - Booking|Weeto DFD Level 1 — Booking]].

### DFD notes and pedagogical alignment

- **No Data Stores (No DB):** In line with the instructor's syllabus, early DFD modeling analyzes how data flows between processes, human actors, and external services. Data stores are intentionally excluded until database modeling / ER diagrams are formally covered.
- **Retained Service Integrations:** Interactions with Google Calendar / Meet (for meeting generation) and the Email Service (for dispatching confirmations) are fully preserved as external entities.
- **No Advanced Queue / Outbox Mechanics:** Internal implementation artifacts (e.g., asynchronous workers, database tables, and pending queue states) are kept out of this conceptual presentation diagram.

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
