Nexstep
=======

Every message becomes the next step. Nexstep turns client conversations from Gmail/Outlook and WhatsApp into actionable tasks, auto‑scheduled meetings, and a weekly ops summary—purpose‑built for agencies and freelancers.

What is Nexstep?
----------------

Nexstep is an ops copilot for small agencies and solo freelancers that converts inbox chaos into clear action:

*   Detects key intents in emails/WhatsApp (leads, proposals, meetings, invoices)
    
*   Auto-creates tasks on a built‑in Kanban board
    
*   Sends a smart booking link for instant scheduling (Google/Microsoft Calendar)
    
*   Delivers a weekly report of leads, stalled threads, invoices, and meetings
    

Built for quick setup, reliability, and measurable time savings.

Core Features (v1)
------------------

*   Multi‑inbox intake
    
    *   Gmail + Outlook via OAuth
        
    *   WhatsApp read‑only via email‑forwarding bridge (send via API planned for v2)
        
*   Intent detection (week‑1 set)
    
    *   New lead inquiry
        
    *   Proposal/quote request or approval
        
    *   Meeting scheduling/rescheduling (fully automated with booking link)
        
    *   Invoice/payment issue
        
*   Actions and automation
    
    *   Built‑in Kanban: New, Waiting, Action Needed, Scheduled, Done
        
    *   Auto‑scheduling via booking link with guardrails:
        
        *   Business hours: 9am–6pm, Mon–Fri
            
        *   Minimum notice: 12h
            
        *   Buffer: 15min
            
    *   Weekly email report
        
*   Owner experience
    
    *   Web app with responsive PWA
        
    *   Magic‑link and Google/Microsoft OAuth login
        
    *   Sends from the connected inbox for natural client experience
        
        

Who is it for?
--------------

*   Marketing, design, and dev agencies (1–10 people)
    
*   Freelancers and consultants handling client threads across email and WhatsApp
    
*   Anyone who wants fewer missed leads, faster scheduling, and clearer follow‑ups
    

Roadmap
-------

*   v1.1
    
    *   Additional intents: scope updates, support/bug, project status
        
    *   Slack/Telegram notifications
        
    *   Per‑day business hours
        
*   v2
    
    *   WhatsApp Cloud API for sending
        
    *   External task sync (Asana/Trello/Notion)
        
    *   SOP checklists and recurring reminders
        
    *   Multi‑user teams and permissions
        

Tech Stack
----------

*   Backend: Python (FastAPI), Postgres
    
*   Ingestion: Gmail API, Microsoft Graph, WhatsApp email bridge
    
*   Scheduling: Google Calendar + Microsoft Outlook Calendar
    
*   Intelligence: deterministic rules + lightweight prompts
    
*   Frontend: React + Tailwind (PWA-ready)
    
*   Billing: Stripe (v1 launch)
    
*   Hosting: any modern PaaS or VPS
    

High‑Level Architecture
-----------------------

*   Connect accounts (OAuth) → ingest messages → normalize and classify → create tasks and optional drafts → auto‑schedule meetings via booking link → weekly report summarizing outcomes.
    
*   Deterministic rules handle week‑1 intents; uncertain cases go to “Review.”
    

Local Development
-----------------

Prereqs

*   Python 3.11+
    
*   Postgres 14+
    
*   Node 18+
    

Backend setup

*   Create Postgres DB and set DATABASE\_URL
    
*   Install: fastapi, uvicorn, sqlmodel, psycopg\[binary\], google‑api‑python‑client, google‑auth, requests
    
*   Configure env vars: Google/Microsoft OAuth creds, SMTP for magic links
    
*   Run: uvicorn app.main:app --reload
    

Frontend setup

*   Vite + React + Tailwind
    
*   Set VITE\_API\_URL to backend URL
    
*   Run: npm run dev
    

Recommended first milestone

*   Connect Gmail (read‑only), ingest last 30 days, classify 4 intents, create tasks, render Kanban
    
*   Enable booking link with combined free/busy from Google/Microsoft
    

Security and Privacy
--------------------

*   Data stays tied to the connected accounts; sending uses the owner’s inbox identity
    
*   WhatsApp via read‑only email bridge in v1; API sending only with explicit consent in v2
    
*   Export and delete controls for threads and tasks planned for early versions
    

FAQ
---

*   Does Nexstep replace my CRM?
    
    *   No—it’s a lightweight ops layer to turn conversations into next steps, and can coexist with any CRM.
        
*   Can I use only one inbox?
    
    *   Yes. Connect Gmail or Outlook (or both), plus calendars as needed.
        
*   Will it message clients automatically?
    
    *   Only for scheduling (booking link) in v1; all other replies require manual approval.
        
*   How does WhatsApp work in v1?
    
    *   Forward chat exports to a unique intake email; Nexstep parses and tags them as WhatsApp. Full API send comes in v2.
