# Tap to Trust — 9 End-to-End Scenarios

Three personas · three scenarios each · full flow for every one.

Each scenario walks through:
**1. Trigger** → **2. Agent detects** → **3. Owner sees** → **4. Owner decides** → **5. Agent resumes** → **6. Outcome**

---

## 🦷 Persona 1 — Dental Practice Owner

**Dr. Elena Marquez · Brightsmile Dental · Berlin**
Between patients. Phone in pocket. 10 seconds between chair turnovers.

---

### Scenario 1.1 — The Long-Tenure Refund *(APPROVE)*

1. **Trigger**
   Marcus Weber (customer for 36 months, LTV €2,340) messages on WhatsApp at 10:38:
   > "Hi, need to cancel my cleaning tomorrow. Can I get my €180 back?"

2. **Agent detects**
   Chattie recognises: refund request · €180 · customer tenure > 24mo · no prior refund history · sentiment neutral.
   Confidence: **82%** · Recommendation: **approve**.

3. **Owner sees** *(lock-screen notification)*
   > **Chattie · now**
   > Refund €180 for Marcus W.?
   > 36mo customer · first refund ever
   >
   > [Send it] [Cap it] [I'll call him]

4. **Owner decides** — Taps **Send it**. 4 seconds total.

5. **Agent resumes** *(back to Marcus)*
   > "All sorted, Marcus — €180 is on its way back. Want me to help you find another slot?"

6. **Outcome**
   Refund processed · Marcus reschedules for next week · Learning signal: "Elena approved refund <€200 for 24mo+ customer → candidate for auto-approval rule."

---

### Scenario 1.2 — The High-Stakes Plan Upgrade *(CONSTRAIN)*

1. **Trigger**
   The Klein family (4 members · 52 months · LTV €4,180) asks via WhatsApp at 13:20:
   > "We'd like the premium plan — whitening and night-guard coverage especially."

2. **Agent detects**
   Upgrade €29/mo → €79/mo · billing impact €600/year · irreversible in 14 days · family account.
   Confidence: **71%** · Recommendation: **approve_with_constraint**.

3. **Owner sees** *(pulled out phone between patients)*
   > Klein family wants Premium
   > +€50/mo · €600/year · 14d cooling-off
   >
   > ▸ Show past whitening questions (2)
   > ▸ Last statement: paid on time
   >
   > [Upgrade now] [Start next cycle] [Call them] [Not yet]

4. **Owner decides** — Taps **Start next cycle** (avoids mid-month proration complaints).
   Agent gets the whisper automatically: *"Confirm whitening is covered from day 1 of the new cycle."*

5. **Agent resumes**
   > "Perfect — I've set the upgrade to start on your next cycle (1 May), so you won't see a split bill. Whitening is fully covered from day one. Want me to book your first session?"

6. **Outcome**
   Family happy · no billing friction · agent proactively books · owner never opened the app itself.

---

### Scenario 1.3 — The Angry 3rd-Visit Refund *(TAKEOVER)*

1. **Trigger**
   Jonas B. (18mo tenure) at 15:44:
   > "Third time I've had pain after the same filling. I want my money back AND compensation."

2. **Agent detects**
   Refund request · €420 · sentiment: **angry** · medical complaint · possible legal exposure.
   Confidence: **34%** · Recommendation: **escalate**.

3. **Owner sees** *(notification with red accent)*
   > ⚠️ Jonas B. — complaint + refund
   > 3rd visit same tooth · asking €420 + comp
   >
   > [I'll call him] [Let me type a reply] [Defer 10 min]

4. **Owner decides** — Taps **I'll call him**. Agent steps fully aside.

5. **Agent resumes** *(just one line to Jonas, in-character)*
   > "Jonas, Dr. Marquez wants to speak with you personally — she'll call in the next few minutes."

6. **Outcome**
   Elena calls from the car between patients · defuses in 8 minutes · books free follow-up · agent logs the outcome so the next flagged complaint has more context.

---

## 🍝 Persona 2 — Restaurant Manager

**Luca Ricci · Trattoria Ricci · Munich**
Mid-shift. Hands full. Loud room. Maybe can't type at all.

---

### Scenario 2.1 — Double-Booking Conflict *(MODIFY)*

1. **Trigger**
   Regular on WhatsApp at 18:52:
   > "Can I move our 8 from tonight 19:30 → 20:00? Train delay."

2. **Agent detects**
   Reservation change · 30 min shift · conflicts with a standing 20:00 booking for 6.
   Confidence: **44%** · Recommendation: **modify** (agent suggests 20:15 instead).

3. **Owner sees** *(glanceable card — voice-ready)*
   > Ricci 8pax — move to 20:00?
   > 🔴 Conflicts with Kaiser 20:00/6
   > Agent suggests: 20:15
   >
   > 🎙 "Make it nine fifteen"
   >
   > [20:15 ✓] [Call guest] [Let me type]

4. **Owner decides** — Hands are covered in flour. Holds the phone to his ear and says **"twenty-fifteen, but put them at table 12."** Voice transcribed into the whisper slot.

5. **Agent resumes**
   > "Happy to — moved you to 20:15, table 12 (bit quieter, near the window). See you soon!"

6. **Outcome**
   No conflict · Kaiser unaware · Ricci's total screen time: 3 seconds.

---

### Scenario 2.2 — Complaint With Voucher Request *(WHISPER)*

1. **Trigger**
   Email at 22:10 from last Saturday's guest:
   > "The calamari was cold and service was slow. Hoping for some kind of gesture."

2. **Agent detects**
   Complaint · voucher implied · no prior complaints from this guest · party of 4, €180 spend.
   Confidence: **68%** · Recommendation: **approve_with_whisper** (€40 voucher + personal apology line).

3. **Owner sees** *(post-shift, on the S-Bahn home)*
   > Guest wants something for Sat
   > Agent proposes: €40 voucher
   > First complaint · €180 bill
   >
   > [Send voucher + apology] [Just apologise, no voucher] [Ask what happened first] [Defer to tomorrow]

4. **Owner decides** — Taps **Send voucher + apology**, then long-presses to add a whisper: *"Mention our new head chef starts Monday."*

5. **Agent resumes**
   > "Thank you for telling us — that isn't the standard we want. There's a €40 voucher waiting for you, and I'd love you to come try us again: our new head chef starts Monday."

6. **Outcome**
   Guest rebooks for following Friday · agent flags the chef-change line as a good upsell pattern for future complaint replies.

---

### Scenario 2.4 — Fish Supplier Fails Mid-Day *(CONSTRAIN or MODIFY)*

1. **Trigger**
   Inventory agent placed tonight's standard fish order 48h ago with the preferred vendor, Vendor 1, inside the weekly fish budget. At 14:20 — four hours before service — Vendor 1's confirmed delivery is flagged as "not dispatched." Agent pings the two standby vendors for priority quotes: Vendor 2 replies within 6 minutes, Vendor 3 still pending.

2. **Agent detects**
   Supply-chain failure · service-critical (fish is on tonight's menu for 38 confirmed covers) · budget impact: Vendor 2 quote **+22% over budget** · Vendor 3 unquoted · 4h to service · risk of cancelling dishes / comping guests escalates every 15 min.
   Confidence: **58%** · Recommendation: **accept Vendor 2**, flag budget overrun for manager sign-off.

3. **Owner sees** *(lock screen, Luca is prepping stations)*
   > **Chattie · 14:26**
   > 🐟 **Fish for tonight — Vendor 1 won't deliver**
   > Vendor 2 can: **+€180 over budget (+22%)**
   > Vendor 3: quote still pending
   > 38 covers booked · service 18:30
   >
   > [Accept Vendor 2] [Wait for Vendor 3] [Custom…] [Give me V2's contact]

4. **Owner decides**
   Luca taps **Custom…** and types two lines (voice dictation while plating):
   - *"Take Vendor 2, but only the amount for tonight — not the full week."*
   - *"If Vendor 3 comes back cheaper in the next 20 min, swap; otherwise lock V2."*
   Agent acknowledges with a 1-line confirmation card: the budget variance now shows **+€95 (+12%)** instead of +€180, and a 20-minute timer appears on the card for the Vendor 3 fallback.

5. **Agent resumes**
   - **→ Vendor 2:** places partial order (tonight-only), confirms delivery window 17:00–17:30, requests delivery note.
   - **→ Vendor 3:** chases for a quote with a 20-min deadline; auto-cancels the ask if missed.
   - **→ Head chef on WhatsApp:** *"Fish is coming from Vendor 2 tonight only — arriving 17:00–17:30. Menu unchanged."*
   - **→ Accounting log:** flags the +€95 variance with reason *"Vendor 1 failed to dispatch — emergency sub."*
   - **→ Vendor 1 (polite, firm):** *"You didn't deliver today's confirmed order — we've had to source elsewhere. Please confirm this won't repeat, or we'll review the contract."*

6. **Outcome**
   Service runs on time · no dish cancellations · €95 overrun absorbed knowingly rather than surprise-billed · Vendor 1 escalation paper-trail started · Vendor 3 missed the 20-min window, so V2 stayed locked. Learning signal: *"When preferred vendor misses dispatch and secondary exceeds budget, Luca prefers partial/tonight-only orders over full replacement."* → Next time, agent proposes the partial-order option as the pre-selected default.

---

### Scenario 2.3 — Supplier Auto-Reorder Spike *(DENY)*

1. **Trigger**
   Connected POS + supplier API · 07:40 · weekly produce order auto-drafted. Tomatoes are up 38% week-over-week due to spot pricing.

2. **Agent detects**
   Recurring action · total above usual weekly ceiling (€1,240 vs €900) · could be absorbed or paused.
   Confidence: **51%** · Recommendation: **hold for owner**.

3. **Owner sees** *(morning, still in bed)*
   > Produce order ready to send
   > ⚠️ €1,240 · +38% tomatoes
   >
   > Tap to see full basket ▸
   >
   > [Send] [Halve tomatoes] [Skip tomatoes this week] [Call supplier first]

4. **Owner decides** — Taps **Skip tomatoes this week**, adds reason: *"Will use tinned for the bolognese special."*

5. **Agent resumes** *(to the supplier API)*
   Order submitted without tomatoes · agent updates tomorrow's menu to promote the bolognese · messages the head chef on WhatsApp: *"Bolognese special tomorrow — tomatoes skipped, using tinned."*

6. **Outcome**
   €280 saved · no waste · chef not ambushed · the reason string ("tinned for bolognese") becomes training data: next price spike, agent pre-suggests menu swaps.

---

## 💪 Persona 3 — Personal Trainer

**Mia Holm · Independent PT · Copenhagen**
Between sessions. Gym floor. Sweat on screen. One thumb.

---

### Scenario 3.1 — Class Pack Upgrade Mid-Session *(APPROVE via voice)*

1. **Trigger**
   Existing client, Ida, on WhatsApp at 10:15:
   > "Can I upgrade from my 5-pack to the 20-pack? I'm hooked."

2. **Agent detects**
   Upgrade · €80 → €280 · 4mo client · no payment issues.
   Confidence: **91%** · Recommendation: **approve**.

3. **Owner sees** *(AirPods + Apple Watch, client is mid-set)*
   > 🔊 *(soft chime)*
   > "Ida wants to upgrade to the 20-pack, €280. Approve, ask me later, or handle it yourself?"

4. **Owner decides** — Says **"Approve"** while spotting a squat. 1 second.

5. **Agent resumes**
   > "Amazing! Upgrade locked in — your new pack is live, 20 sessions to burn. Proud of you 💪"

6. **Outcome**
   Zero context-switch · Mia never looks at the phone · revenue +€200 · client gets emotional reinforcement in the agent's voice.

---

### Scenario 3.2 — Late-Cancel Fee Waiver *(DEFER → CONSTRAIN)*

1. **Trigger**
   WhatsApp at 07:12 from a 2-week-old client:
   > "Got food poisoning, can't make the 8am. Please don't charge me the late-cancel."

2. **Agent detects**
   Fee waiver request · €40 · new client (3 sessions in) · agent's policy: auto-charge fees.
   Confidence: **46%** · Recommendation: **ask owner**.

3. **Owner sees** *(mid-rep with a previous client)*
   > Waive €40 late-cancel for Jonas?
   > 2wk client · genuine-sounding
   >
   > [Waive] [Charge half] [Charge full] [⏰ Ask in 10]

4. **Owner decides** — Taps **⏰ Ask in 10**. She needs to finish the set.
   10 minutes later the card re-surfaces with the same context + a small "waited 10m" badge. She taps **Charge half** — the agent infers a €20 fee + a kind note.

5. **Agent resumes**
   > "Rest up, Jonas — I've only charged €20 instead of the full fee. When you're back on your feet, reply FIT and I'll book you straight in."

6. **Outcome**
   Client returns within 3 days (keyword trigger worked) · fairness preserved · agent learns: "For ill new clients, Mia tends to half-charge" → next time, that's the pre-selected recommendation.

---

### Scenario 3.3 — Bulk Outreach Draft Going Out *(MODIFY + WHISPER)*

1. **Trigger**
   Agent proposes a quarterly re-engagement broadcast to 43 lapsed clients, 09:00 Monday.

2. **Agent detects**
   Bulk send · 43 recipients · template: "It's been a while, come back for a free intro!" · financial impact: ~6 likely bookings.
   Confidence: **62%** · Recommendation: **review before send**.

3. **Owner sees** *(coffee in hand, first thing in the morning)*
   > Re-engagement message — 43 people
   > "It's been a while, come back for a free intro!"
   >
   > ▸ Preview · ▸ Who's on the list (43)
   >
   > [Send to all] [Edit message] [Send to 5 I pick] [Skip this week]

4. **Owner decides** — Taps **Edit message**, inline tweaks: "free intro" → **"free 20-min check-in"** (less commitment, better conversion from cold).
   Also adds a whisper before send: *"If they reply 'not for me,' remove them from future broadcasts automatically."*

5. **Agent resumes**
   Sends the edited version · for the 4 opt-outs that come back, auto-prunes the list · reports to Mia at end of day: "37 delivered, 4 opted out and removed, 8 booked a check-in."

6. **Outcome**
   Campaign doubles its usual response rate · list gets cleaner · Mia spent 45 seconds total on a broadcast that used to take her 30 minutes.

---

## Cross-Cutting Patterns

Across all 9 scenarios, the same shape emerges:

| Stage | Design surface |
|---|---|
| **Trigger** | Not all triggers are customer messages — some are system events (price spikes, broadcast drafts, auto-reorders). |
| **Agent detects** | Confidence score + risk signals decide the default CTA order. |
| **Owner sees** | Progressive disclosure: 3 buttons by default, more on long-press. Voice/haptic for the hands-busy moments. |
| **Owner decides** | The 7-way spectrum is always implicit — only 3–4 surface on the card, rest via hold/expand. |
| **Agent resumes** | Customer never hears the word "approved." The agent just sounds like a person doing their job. |
| **Outcome** | Every decision becomes training data. The next similar request starts smarter. |
