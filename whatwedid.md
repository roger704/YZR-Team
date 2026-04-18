# What we did

> YZR Team · Superchat Design Challenge: *Tap to Trust*
> **Status:** mock-up is still WIP — this doc is the narrative that frames it.

---

## Who we are

**YZR — three designers and builders who spend their careers turning complex systems into decisions people can actually make.**
Exactly what the 5% problem needs.

### Zahra Zare · UX/UI Designer
Came to design through marketing and process optimization, which means she reads workflows before she reads screens. Figma, prototyping, user research, usability testing — but her real edge is systems thinking: spotting where a "small UX problem" is actually a broken workflow, and designing the fix at the right layer.

### Yunrong Jhan · UX/UI Product Designer
Specializes in turning complex systems into **decision-based UX**. Shipped across B2B enterprise (Airbus), SaaS, AI, and consumer products — improving activation, adoption, and task efficiency through data-driven design and AI-assisted prototyping. Portfolio → [yunrong.framer.website](https://yunrong.framer.website)

### Robert Sicken · Product Manager
Ten years across software development, professional services, and product management. Comfortable in code, strategy, and the messy space between. Role on the team: keep the product decisions honest, the scope tight, and the build moving.

### How we split this one

- **Zahra** — workflow logic, interaction patterns, the shape of the approval moment
- **Yunrong** — decision UX, visual design, the Lovable prototype
- **Robert** — framing, scenario, deck, and the narrative wrapped around the mock



---

## The framing

> **Aria handles 95% on her own. The other 5% is where design lives.**

The whole submission is about that 5% — the small number of moments per day when an agentic system has to stop, surface, and hand the decision back to a human. Done badly, it's a modal with two buttons. Done well, it feels like a trusted colleague tapping you on the shoulder.

We didn't design an approval screen. We designed a handoff between teammates.

---

## Background — Aria, Superchat's agent for restaurants

Superchat gives a restaurant manager a new agentic system: **Aria**.

Aria is wired into the restaurant's operating stack:

- **Booking management** — reservations, cancellations, waitlist
- **Inventory management** — supplier orders, stock levels, prices
- **Shift planning** — rotas, sick-calls, last-minute cover
- **Customer communication** — WhatsApp, email, voice across all channels

Based on live data and pre-set instructions, **Aria acts autonomously on the vast majority of operational decisions**. She reorders stock, confirms bookings, reshuffles shifts, replies to guests — all without the manager ever looking at a screen.

But a handful of decisions every week are different: **time-sensitive, budget-sensitive, or relationship-sensitive**. For those, Aria needs the manager *in the loop* — and she needs that loop to take 10 seconds, not 10 minutes.

That's the design problem.

---

## Who we designed for

**The restaurant manager.**
Mid-shift. Hands full. Loud room. Can't read long text; maybe can't type at all.

> *"Voice? A glance? A tap?"*

We deliberately picked the hardest of the three personas in the brief. If the interaction works for someone plating fish with flour on their hands, it works for the dental owner and the PT too.

---

## The scenario — Supply Chain Issue

A single, realistic Monday afternoon. Fish for tonight's service.

### The setup

Aria is running inventory management. Two days ago she placed the standard weekly fish order with Vendor 1 — a preferred supplier, inside the weekly budget. Confirmed. Done. Off the manager's plate.

**38 covers are booked for tonight. Fish is on the menu.**

### The problem

**14:20 — four hours before service.** Vendor 1's confirmed delivery flips to *"not dispatched."* No driver. No ETA. No fish.

Aria already knows what to do next — that's what a good agent does. Without waking the manager, she:

1. Pings **two standby vendors** on her pre-approved list for priority quotes
2. **Vendor 2** replies in 6 minutes — can deliver in time, but the price is **+22% over budget**
3. **Vendor 3** doesn't reply

Aria now has a fork she can't resolve alone: she can keep the menu but break the budget, or protect the budget and risk the service. Either way, she's picking between two rules the manager gave her. That's the definition of the 5%.

### The moment

Aria sends a single lock-screen notification. The manager — halfway through prep — glances down:

> **🐟 Fish for tonight — Vendor 1 won't deliver**
> Vendor 2 can: **+€180 over budget (+22%)**
> Vendor 3: quote pending
> *38 covers · service 18:30*
>
> **→ Accept Vendor 2's price** *(Aria's pick)*
> → Request an offer from Vendor 3
> → Provide custom instructions
> → Handle it personally: "Give me V2's contact"

Four options. **One is pre-selected with Aria's confidence weight** — she's an opinionated colleague, not a neutral menu. The others are escape hatches for when the manager knows something Aria doesn't.

### The resolution — why this matters

The manager taps **Custom instructions** and dictates two sentences by voice while still plating:

> *"Take Vendor 2, but only tonight's amount — not the full week. If Vendor 3 beats them in 20 minutes, swap."*

The overrun drops from +€180 to **+€95**. Aria acknowledges and takes over again:

- Places the partial order with V2, confirms delivery window 17:00–17:30
- Chases V3 with a 20-minute deadline; auto-cancels if missed
- WhatsApps the head chef: *"Fish from V2 tonight only, 17:00–17:30. Menu unchanged."*
- Logs the +€95 variance in accounting with the reason attached
- Sends V1 a polite but firm follow-up: *"You didn't deliver — we sourced elsewhere. Confirm this won't repeat, or we'll review the contract."*

**Service runs on time. No dish cancelled. €85 saved vs. Aria's default.** The manager's total screen time: 14 seconds.

### What Aria learns

The manager's reasoning — *"partial order, not full week"* — becomes a signal. Next time Vendor 1 fails, Aria's pre-selected option is no longer "accept V2's full quote" — it's "accept V2 for tonight only." The deck shrinks. Trust compounds.

---

## What we're actually showing

Three things, in this order:

1. **The framing** — agents act autonomously; the design problem is the handoff, not the chat.
2. **The moment** — the mobile mock-up of the 14:26 notification, live from Lovable. Not a static screenshot; the actual prototype, updating as we iterate.
3. **The loop** — what happens in the 15 minutes *after* the tap, because that's where the feeling of teamwork lives.

---

## Open threads (mock-up is WIP)

- Voice-first path: the dictation moment needs to feel like speaking to a colleague, not dictating a memo.
- The post-decision state: what Luca sees 20 minutes later (V3 missed, V2 locked, chef acknowledged).
- The "invisible handoff" to the guest — does the customer ever see any of this? (Answer: no.)
- The learning confirmation — at what point does Aria ask "Should I handle this the same way next time?" and how does that feel *earned* rather than creepy?
