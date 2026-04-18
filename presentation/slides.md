---
theme: seriph
title: Tap to Trust
info: |
  ## Tap to Trust
  Aria and the 5% — designing the approval moment for agentic AI.
  YZR Team · Superchat Design Challenge.
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: fade
mdc: true
fonts:
  sans: Inter
  serif: Inter
  weights: '300,400,500,600,700,800,900'
colorSchema: light
exportFilename: tap-to-trust
---

<div class="title-slide">
  <div class="title-gradient-bg"></div>
  <div class="title-content">
    <div class="eyebrow">YZR · Superchat Design Challenge</div>
    <h1 class="title-wordmark">Tap to Trust</h1>
    <div class="title-sub">Aria and the 5%</div>
    <div class="title-footer">Zahra · Yunrong · Robert</div>
  </div>
</div>

<style scoped>
.title-slide {
  position: absolute;
  inset: 0;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #ffffff;
}
.title-gradient-bg {
  position: absolute;
  inset: -10%;
  background:
    radial-gradient(ellipse at 20% 30%, rgba(251, 191, 160, 0.55), transparent 55%),
    radial-gradient(ellipse at 80% 20%, rgba(196, 181, 253, 0.55), transparent 55%),
    radial-gradient(ellipse at 60% 85%, rgba(147, 197, 253, 0.6), transparent 55%),
    linear-gradient(120deg, #fff7f1 0%, #f5f3ff 50%, #eff6ff 100%);
  filter: blur(0px);
}
.title-content {
  position: relative;
  text-align: center;
  z-index: 1;
}
.eyebrow {
  font-size: 0.85rem;
  font-weight: 500;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #6b7280;
  margin-bottom: 2.2rem;
}
.title-wordmark {
  font-family: Inter, sans-serif;
  font-weight: 900;
  font-size: 8.5rem;
  line-height: 0.95;
  letter-spacing: -0.04em;
  background: linear-gradient(120deg, #f59e0b 0%, #ef4444 30%, #8b5cf6 65%, #3b82f6 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  margin: 0;
}
.title-sub {
  font-size: 1.9rem;
  font-weight: 300;
  color: #374151;
  margin-top: 1.2rem;
  letter-spacing: -0.01em;
}
.title-footer {
  margin-top: 3.5rem;
  font-size: 0.8rem;
  font-weight: 500;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #9ca3af;
}
</style>

---
layout: none
title: Who we are
---

<div class="slide-bright team-slide">
  <div class="slide-eyebrow">The team</div>
  <h2 class="slide-title">Who we are</h2>
  <div class="slide-lede">Three designers and builders who turn complex systems into decisions people can actually make. <span class="lede-accent">Exactly what the 5% problem needs.</span></div>

  <div class="team-grid">
    <div class="team-card">
      <div class="team-avatar" style="background: linear-gradient(135deg, #fb923c, #f59e0b);">Z</div>
      <div class="team-name">Zahra Zare</div>
      <div class="team-role">UX/UI Designer</div>
      <div class="team-edge">Reads workflows before screens. Systems thinking — spots when a "UX problem" is actually a broken process, and designs the fix at the right layer.</div>
    </div>
    <div class="team-card team-card--featured">
      <div class="team-avatar" style="background: linear-gradient(135deg, #a78bfa, #8b5cf6);">Y</div>
      <div class="team-name">Yunrong Jhan</div>
      <div class="team-role">UX/UI Product Designer</div>
      <div class="team-edge">Turns complex systems into decision-based UX. Shipped across Airbus, SaaS, AI, consumer — activation and task efficiency through data-driven design.</div>
      <a href="https://yunrong.framer.website" target="_blank" class="team-link">yunrong.framer.website →</a>
    </div>
    <div class="team-card">
      <div class="team-avatar" style="background: linear-gradient(135deg, #60a5fa, #3b82f6);">R</div>
      <div class="team-name">Robert Sicken</div>
      <div class="team-role">Product Manager</div>
      <div class="team-edge">Ten years across dev, services, and product. Comfortable in code, strategy, and the messy space between. Keeps scope tight and the build moving.</div>
    </div>
  </div>

  <div class="split-strip">
    <div class="split-label">How we split this one</div>
    <div class="split-items">
      <div><b>Zahra</b> — workflow logic & the approval moment</div>
      <div><b>Yunrong</b> — decision UX, visual design, Lovable prototype</div>
      <div><b>Robert</b> — framing, scenario, deck, narrative</div>
    </div>
  </div>
</div>

<style scoped>
.slide-bright {
  position: absolute;
  inset: 0;
  padding: 3.2rem 4rem;
  background: linear-gradient(180deg, #ffffff 0%, #fafbff 100%);
  color: #111827;
  font-family: Inter, sans-serif;
}
.slide-eyebrow {
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #8b5cf6;
}
.slide-title {
  font-size: 3.2rem;
  font-weight: 800;
  letter-spacing: -0.03em;
  margin: 0.3rem 0 0.6rem;
  color: #0f172a;
}
.slide-lede {
  font-size: 1.05rem;
  color: #475569;
  max-width: 48rem;
  font-weight: 400;
  line-height: 1.5;
}
.lede-accent { color: #0f172a; font-weight: 600; }

.team-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 1.25rem;
  margin-top: 2rem;
}
.team-card {
  background: #ffffff;
  border-radius: 1.5rem;
  padding: 1.6rem;
  box-shadow: 0 10px 30px -12px rgba(15, 23, 42, 0.12), 0 2px 6px rgba(15, 23, 42, 0.04);
  border: 1px solid rgba(15, 23, 42, 0.05);
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
}
.team-card--featured {
  background: linear-gradient(180deg, #ffffff 0%, #faf5ff 100%);
  border-color: rgba(139, 92, 246, 0.18);
}
.team-avatar {
  width: 3rem;
  height: 3rem;
  border-radius: 9999px;
  color: white;
  font-weight: 800;
  font-size: 1.2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 0.6rem;
  box-shadow: 0 6px 16px -4px rgba(0, 0, 0, 0.18);
}
.team-name { font-weight: 700; font-size: 1.15rem; color: #0f172a; }
.team-role { font-size: 0.78rem; font-weight: 500; color: #8b5cf6; letter-spacing: 0.04em; text-transform: uppercase; margin-bottom: 0.4rem; }
.team-edge { font-size: 0.85rem; color: #475569; line-height: 1.45; }
.team-link { margin-top: 0.6rem; font-size: 0.78rem; font-weight: 600; color: #8b5cf6; text-decoration: none; }

.split-strip {
  margin-top: 1.5rem;
  padding: 1rem 1.4rem;
  background: #ffffff;
  border-radius: 1rem;
  border: 1px dashed rgba(15, 23, 42, 0.15);
  display: flex;
  align-items: center;
  gap: 1.5rem;
}
.split-label {
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: #64748b;
  white-space: nowrap;
}
.split-items { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1.2rem; flex: 1; font-size: 0.82rem; color: #334155; }
.split-items b { color: #0f172a; font-weight: 700; }
</style>

---
layout: none
title: From talk to action
---

<div class="slide-bright slide-center">
  <div class="slide-eyebrow" style="color:#3b82f6">Context · 10 seconds</div>
  <h2 class="huge-statement">
    Agents used to <span class="strike">talk.</span><br/>
    Now they <span class="gradient-text">act.</span>
  </h2>

  <div class="act-grid">
    <div class="act-pill"><span class="act-icon" style="background:#dbeafe;color:#3b82f6">📦</span> Reorder stock</div>
    <div class="act-pill"><span class="act-icon" style="background:#d1fae5;color:#10b981">📅</span> Confirm bookings</div>
    <div class="act-pill"><span class="act-icon" style="background:#ede9fe;color:#8b5cf6">👥</span> Reshuffle shifts</div>
    <div class="act-pill"><span class="act-icon" style="background:#fef3c7;color:#f59e0b">💬</span> Reply to guests</div>
  </div>

  <div class="sub-line">Hundreds of small decisions a day. Most of them, the manager never sees.</div>
</div>

<style scoped>
.slide-bright {
  position: absolute; inset: 0; padding: 3.2rem 4rem;
  background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
  color: #111827; font-family: Inter, sans-serif;
}
.slide-center { display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }
.slide-eyebrow { font-size: 0.75rem; font-weight: 600; letter-spacing: 0.2em; text-transform: uppercase; }
.huge-statement {
  font-size: 5rem; font-weight: 800; line-height: 1.05;
  letter-spacing: -0.04em; color: #0f172a; margin: 1rem 0 0;
}
.strike { color: #94a3b8; text-decoration: line-through; text-decoration-color: #cbd5e1; text-decoration-thickness: 4px; }
.gradient-text {
  background: linear-gradient(120deg, #3b82f6 0%, #8b5cf6 60%, #ef4444 100%);
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.act-grid { display: grid; grid-template-columns: repeat(4, auto); gap: 0.8rem; margin-top: 3rem; }
.act-pill {
  display: flex; align-items: center; gap: 0.6rem;
  padding: 0.8rem 1.2rem; background: #ffffff; border-radius: 9999px;
  font-size: 0.95rem; font-weight: 500; color: #1f2937;
  box-shadow: 0 6px 16px -8px rgba(15, 23, 42, 0.15);
  border: 1px solid rgba(15, 23, 42, 0.05);
}
.act-icon { width: 2rem; height: 2rem; border-radius: 9999px; display: inline-flex; align-items: center; justify-content: center; font-size: 1rem; }
.sub-line { margin-top: 2.5rem; font-size: 1.15rem; color: #64748b; font-weight: 400; max-width: 36rem; }
</style>

---
layout: none
title: 95% · 5%
---

<div class="slide-bright hero-95">
  <div class="hero-left">
    <div class="slide-eyebrow" style="color:#ef4444">The framing</div>
    <h2 class="hero-title">
      Aria handles<br/>
      <span class="big-pct">95<span class="pct-sym">%</span></span><br/>
      <span class="hero-sub-em">on her own.</span>
    </h2>
    <div class="hero-sub">The other <b class="five">5%</b> is where design lives.</div>
    <div class="hero-body">Time-sensitive. Budget-sensitive. Relationship-sensitive. The ones where two rules collide and Aria can't pick without you.</div>
  </div>

  <div class="hero-right">
    <svg viewBox="0 0 400 400" class="dots-svg">
      <defs>
        <radialGradient id="five-glow" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#ef4444"/>
          <stop offset="100%" stop-color="#f97316"/>
        </radialGradient>
      </defs>
      <!-- 10x10 grid of 100 dots. 5 of them in a vibrant accent. -->
      <!-- Dots generated by a single loop written out. cell = 34px, radius = 11 -->
      <g>
        <!-- row 0 -->
        <circle cx="28" cy="28" r="11" fill="#e2e8f0"/><circle cx="62" cy="28" r="11" fill="#e2e8f0"/><circle cx="96" cy="28" r="11" fill="#e2e8f0"/><circle cx="130" cy="28" r="11" fill="#e2e8f0"/><circle cx="164" cy="28" r="11" fill="#e2e8f0"/><circle cx="198" cy="28" r="11" fill="#e2e8f0"/><circle cx="232" cy="28" r="11" fill="#e2e8f0"/><circle cx="266" cy="28" r="11" fill="#e2e8f0"/><circle cx="300" cy="28" r="11" fill="#e2e8f0"/><circle cx="334" cy="28" r="11" fill="#e2e8f0"/>
        <!-- row 1 -->
        <circle cx="28" cy="62" r="11" fill="#e2e8f0"/><circle cx="62" cy="62" r="11" fill="#e2e8f0"/><circle cx="96" cy="62" r="11" fill="#e2e8f0"/><circle cx="130" cy="62" r="11" fill="#e2e8f0"/><circle cx="164" cy="62" r="11" fill="#e2e8f0"/><circle cx="198" cy="62" r="11" fill="#e2e8f0"/><circle cx="232" cy="62" r="11" fill="#e2e8f0"/><circle cx="266" cy="62" r="11" fill="#e2e8f0"/><circle cx="300" cy="62" r="11" fill="#e2e8f0"/><circle cx="334" cy="62" r="11" fill="#e2e8f0"/>
        <!-- row 2 -->
        <circle cx="28" cy="96" r="11" fill="#e2e8f0"/><circle cx="62" cy="96" r="11" fill="#e2e8f0"/><circle cx="96" cy="96" r="11" fill="#e2e8f0"/><circle cx="130" cy="96" r="11" fill="#e2e8f0"/><circle cx="164" cy="96" r="11" fill="#e2e8f0"/><circle cx="198" cy="96" r="11" fill="#e2e8f0"/><circle cx="232" cy="96" r="11" fill="#e2e8f0"/><circle cx="266" cy="96" r="11" fill="#e2e8f0"/><circle cx="300" cy="96" r="11" fill="#e2e8f0"/><circle cx="334" cy="96" r="11" fill="#e2e8f0"/>
        <!-- row 3 -->
        <circle cx="28" cy="130" r="11" fill="#e2e8f0"/><circle cx="62" cy="130" r="11" fill="#e2e8f0"/><circle cx="96" cy="130" r="11" fill="#e2e8f0"/><circle cx="130" cy="130" r="11" fill="#e2e8f0"/><circle cx="164" cy="130" r="11" fill="#e2e8f0"/><circle cx="198" cy="130" r="11" fill="#e2e8f0"/><circle cx="232" cy="130" r="11" fill="#e2e8f0"/><circle cx="266" cy="130" r="11" fill="#e2e8f0"/><circle cx="300" cy="130" r="11" fill="#e2e8f0"/><circle cx="334" cy="130" r="11" fill="#e2e8f0"/>
        <!-- row 4 with 3 highlighted -->
        <circle cx="28" cy="164" r="11" fill="#e2e8f0"/><circle cx="62" cy="164" r="11" fill="#e2e8f0"/><circle cx="96" cy="164" r="11" fill="#e2e8f0"/><circle cx="130" cy="164" r="11" fill="url(#five-glow)" class="dot-pulse"/><circle cx="164" cy="164" r="11" fill="url(#five-glow)" class="dot-pulse"/><circle cx="198" cy="164" r="11" fill="url(#five-glow)" class="dot-pulse"/><circle cx="232" cy="164" r="11" fill="#e2e8f0"/><circle cx="266" cy="164" r="11" fill="#e2e8f0"/><circle cx="300" cy="164" r="11" fill="#e2e8f0"/><circle cx="334" cy="164" r="11" fill="#e2e8f0"/>
        <!-- row 5 with 2 highlighted -->
        <circle cx="28" cy="198" r="11" fill="#e2e8f0"/><circle cx="62" cy="198" r="11" fill="#e2e8f0"/><circle cx="96" cy="198" r="11" fill="#e2e8f0"/><circle cx="130" cy="198" r="11" fill="url(#five-glow)" class="dot-pulse"/><circle cx="164" cy="198" r="11" fill="url(#five-glow)" class="dot-pulse"/><circle cx="198" cy="198" r="11" fill="#e2e8f0"/><circle cx="232" cy="198" r="11" fill="#e2e8f0"/><circle cx="266" cy="198" r="11" fill="#e2e8f0"/><circle cx="300" cy="198" r="11" fill="#e2e8f0"/><circle cx="334" cy="198" r="11" fill="#e2e8f0"/>
        <!-- row 6 -->
        <circle cx="28" cy="232" r="11" fill="#e2e8f0"/><circle cx="62" cy="232" r="11" fill="#e2e8f0"/><circle cx="96" cy="232" r="11" fill="#e2e8f0"/><circle cx="130" cy="232" r="11" fill="#e2e8f0"/><circle cx="164" cy="232" r="11" fill="#e2e8f0"/><circle cx="198" cy="232" r="11" fill="#e2e8f0"/><circle cx="232" cy="232" r="11" fill="#e2e8f0"/><circle cx="266" cy="232" r="11" fill="#e2e8f0"/><circle cx="300" cy="232" r="11" fill="#e2e8f0"/><circle cx="334" cy="232" r="11" fill="#e2e8f0"/>
        <!-- row 7 -->
        <circle cx="28" cy="266" r="11" fill="#e2e8f0"/><circle cx="62" cy="266" r="11" fill="#e2e8f0"/><circle cx="96" cy="266" r="11" fill="#e2e8f0"/><circle cx="130" cy="266" r="11" fill="#e2e8f0"/><circle cx="164" cy="266" r="11" fill="#e2e8f0"/><circle cx="198" cy="266" r="11" fill="#e2e8f0"/><circle cx="232" cy="266" r="11" fill="#e2e8f0"/><circle cx="266" cy="266" r="11" fill="#e2e8f0"/><circle cx="300" cy="266" r="11" fill="#e2e8f0"/><circle cx="334" cy="266" r="11" fill="#e2e8f0"/>
        <!-- row 8 -->
        <circle cx="28" cy="300" r="11" fill="#e2e8f0"/><circle cx="62" cy="300" r="11" fill="#e2e8f0"/><circle cx="96" cy="300" r="11" fill="#e2e8f0"/><circle cx="130" cy="300" r="11" fill="#e2e8f0"/><circle cx="164" cy="300" r="11" fill="#e2e8f0"/><circle cx="198" cy="300" r="11" fill="#e2e8f0"/><circle cx="232" cy="300" r="11" fill="#e2e8f0"/><circle cx="266" cy="300" r="11" fill="#e2e8f0"/><circle cx="300" cy="300" r="11" fill="#e2e8f0"/><circle cx="334" cy="300" r="11" fill="#e2e8f0"/>
        <!-- row 9 -->
        <circle cx="28" cy="334" r="11" fill="#e2e8f0"/><circle cx="62" cy="334" r="11" fill="#e2e8f0"/><circle cx="96" cy="334" r="11" fill="#e2e8f0"/><circle cx="130" cy="334" r="11" fill="#e2e8f0"/><circle cx="164" cy="334" r="11" fill="#e2e8f0"/><circle cx="198" cy="334" r="11" fill="#e2e8f0"/><circle cx="232" cy="334" r="11" fill="#e2e8f0"/><circle cx="266" cy="334" r="11" fill="#e2e8f0"/><circle cx="300" cy="334" r="11" fill="#e2e8f0"/><circle cx="334" cy="334" r="11" fill="#e2e8f0"/>
      </g>
    </svg>
    <div class="legend">
      <div class="legend-row"><span class="swatch" style="background:#e2e8f0"></span> 95 decisions · Aria alone</div>
      <div class="legend-row"><span class="swatch" style="background:linear-gradient(135deg,#ef4444,#f97316)"></span> 5 decisions · she taps you</div>
    </div>
  </div>
</div>

<style scoped>
.slide-bright {
  position: absolute; inset: 0; padding: 3rem 4rem;
  background: linear-gradient(180deg, #ffffff 0%, #fff7ed 100%);
  color: #111827; font-family: Inter, sans-serif;
}
.hero-95 { display: grid; grid-template-columns: 1.1fr 1fr; gap: 3rem; align-items: center; height: 100%; }
.slide-eyebrow { font-size: 0.75rem; font-weight: 600; letter-spacing: 0.2em; text-transform: uppercase; }
.hero-title { font-size: 3.4rem; font-weight: 800; letter-spacing: -0.03em; line-height: 1.05; color: #0f172a; margin: 0.8rem 0 0; }
.big-pct {
  display: inline-block; font-size: 9rem; font-weight: 900; line-height: 0.9;
  background: linear-gradient(120deg, #0f172a 0%, #334155 100%);
  -webkit-background-clip: text; background-clip: text; color: transparent;
  letter-spacing: -0.06em;
}
.pct-sym { font-size: 5rem; opacity: 0.6; margin-left: 0.1em; }
.hero-sub-em { font-weight: 400; color: #64748b; }
.hero-sub { margin-top: 1.4rem; font-size: 1.5rem; color: #334155; font-weight: 500; }
.five { background: linear-gradient(135deg, #ef4444, #f97316); -webkit-background-clip: text; background-clip: text; color: transparent; font-weight: 800; }
.hero-body { margin-top: 1rem; font-size: 0.95rem; color: #64748b; max-width: 28rem; line-height: 1.5; }

.hero-right { display: flex; flex-direction: column; align-items: center; gap: 1.2rem; }
.dots-svg {
  width: 100%; max-width: 22rem; height: auto;
  filter: drop-shadow(0 12px 24px rgba(239, 68, 68, 0.15));
}
.dot-pulse { animation: dotPulse 2.2s ease-in-out infinite; transform-origin: center; transform-box: fill-box; }
.dot-pulse:nth-child(1) { animation-delay: 0s; }
.dot-pulse:nth-child(2) { animation-delay: 0.3s; }
.dot-pulse:nth-child(3) { animation-delay: 0.6s; }
.dot-pulse:nth-child(4) { animation-delay: 0.9s; }
.dot-pulse:nth-child(5) { animation-delay: 1.2s; }
@keyframes dotPulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.45; } }

.legend { display: flex; flex-direction: column; gap: 0.4rem; font-size: 0.8rem; color: #475569; }
.legend-row { display: flex; align-items: center; gap: 0.6rem; }
.swatch { width: 14px; height: 14px; border-radius: 9999px; display: inline-block; }
</style>

---
layout: default
title: Meet Aria
---

# Meet Aria

Superchat's agentic system for restaurants. Wired into the whole operating stack — live data in, action out.

**Aria is connected to:**

- 📅 **Booking** — reservations, cancellations, waitlist
- 📦 **Inventory** — supplier orders, stock, prices
- 👥 **Shifts** — rotas, sick-calls, cover
- 💬 **Comms** — WhatsApp, email, voice

She acts autonomously on the vast majority. *When two rules collide — she stops and asks.*

<br/>

**Today, so far:** 47 bookings confirmed · 6 cancellations · 3 supplier orders · 112 guest messages · 2 shift swaps

**→ Needed you: 1**

---
layout: none
title: Restaurant manager
---

<div class="slide-bright slide-center">
  <div class="slide-eyebrow" style="color:#f59e0b">Who we designed for</div>
  <h2 class="slide-title">The restaurant manager.</h2>

  <div class="persona-card">
    <div class="persona-icon">🍝</div>
    <div class="persona-body">
      <div class="persona-line">Mid-shift.</div>
      <div class="persona-line">Hands full.</div>
      <div class="persona-line">Loud room.</div>
      <div class="persona-sep"></div>
      <div class="persona-sub">Can't read long text. Maybe can't type at all.</div>
      <div class="persona-quote">"Voice? A glance? A tap?"</div>
    </div>
  </div>

  <div class="persona-caption">We deliberately picked the hardest persona. If it works here, it works everywhere.</div>
</div>

<style scoped>
.slide-bright {
  position: absolute; inset: 0; padding: 3rem 4rem;
  background: linear-gradient(180deg, #ffffff 0%, #fff7ed 100%);
  color: #111827; font-family: Inter, sans-serif;
}
.slide-center { display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }
.slide-eyebrow { font-size: 0.75rem; font-weight: 600; letter-spacing: 0.2em; text-transform: uppercase; }
.slide-title { font-size: 3.4rem; font-weight: 800; letter-spacing: -0.03em; color: #0f172a; margin: 0.4rem 0 2rem; }

.persona-card {
  display: flex; align-items: center; gap: 2.2rem;
  padding: 2rem 2.8rem;
  background: linear-gradient(135deg, #ffffff 0%, #fff7ed 100%);
  border-radius: 2rem;
  border: 1px solid rgba(245, 158, 11, 0.25);
  box-shadow: 0 20px 40px -16px rgba(245, 158, 11, 0.25);
  max-width: 44rem;
}
.persona-icon { font-size: 5rem; line-height: 1; }
.persona-body { text-align: left; }
.persona-line { font-size: 2rem; font-weight: 800; color: #0f172a; letter-spacing: -0.02em; line-height: 1.1; }
.persona-sep { height: 1px; background: rgba(245, 158, 11, 0.3); margin: 0.8rem 0; }
.persona-sub { font-size: 0.95rem; color: #64748b; }
.persona-quote { margin-top: 0.6rem; font-size: 1.3rem; font-style: italic; font-weight: 500; color: #ea580c; }

.persona-caption { margin-top: 1.6rem; font-size: 0.9rem; color: #64748b; max-width: 36rem; }
</style>

---
layout: none
title: The scenario
---

<div class="slide-bright">
  <div class="slide-eyebrow" style="color:#ef4444">The scenario</div>
  <h2 class="slide-title">Fish for tonight. Four hours to service.</h2>
  <div class="scenario-sub">A single, realistic Monday afternoon · 38 covers booked · fish on the menu.</div>

  <svg viewBox="0 0 1000 160" class="timeline-svg">
    <defs>
      <linearGradient id="tl-line" x1="0%" x2="100%">
        <stop offset="0%" stop-color="#10b981"/>
        <stop offset="50%" stop-color="#f59e0b"/>
        <stop offset="100%" stop-color="#ef4444"/>
      </linearGradient>
    </defs>
    <line x1="80" y1="70" x2="920" y2="70" stroke="url(#tl-line)" stroke-width="4" stroke-linecap="round"/>
    <!-- node 1: 2 days ago - green -->
    <circle cx="120" cy="70" r="20" fill="#ffffff" stroke="#10b981" stroke-width="4"/>
    <circle cx="120" cy="70" r="9" fill="#10b981"/>
    <text x="120" y="38" text-anchor="middle" font-size="12" font-weight="700" fill="#047857" font-family="Inter, sans-serif" letter-spacing="1">2 DAYS AGO</text>
    <text x="120" y="114" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a" font-family="Inter, sans-serif">Order placed</text>
    <!-- node 2: 14:20 - amber -->
    <circle cx="500" cy="70" r="22" fill="#ffffff" stroke="#f59e0b" stroke-width="4"/>
    <circle cx="500" cy="70" r="10" fill="#f59e0b"/>
    <text x="500" y="38" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" font-family="Inter, sans-serif" letter-spacing="1">14:20 TODAY</text>
    <text x="500" y="114" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a" font-family="Inter, sans-serif">Vendor fails</text>
    <!-- node 3: 14:26 - red, pulsing -->
    <circle cx="880" cy="70" r="24" fill="#ffffff" stroke="#ef4444" stroke-width="4" class="pulse-ring"/>
    <circle cx="880" cy="70" r="12" fill="#ef4444"/>
    <text x="880" y="38" text-anchor="middle" font-size="12" font-weight="700" fill="#b91c1c" font-family="Inter, sans-serif" letter-spacing="1">14:26</text>
    <text x="880" y="114" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a" font-family="Inter, sans-serif">Aria escalates</text>
  </svg>

  <div class="scenario-grid">
    <div class="scen-card scen-green">
      <div class="scen-chip" style="background:#d1fae5;color:#047857">Confirmed · in budget</div>
      <div class="scen-body">Aria placed the standard weekly fish order with <b>Vendor 1</b>. Off the manager's plate.</div>
    </div>
    <div class="scen-card scen-amber">
      <div class="scen-chip" style="background:#fef3c7;color:#b45309">Not dispatched</div>
      <div class="scen-body">V1's delivery flips: no driver, no ETA. <b>38 covers booked · 4h to service.</b></div>
    </div>
    <div class="scen-card scen-red">
      <div class="scen-chip" style="background:#fee2e2;color:#b91c1c">Rules colliding</div>
      <div class="scen-body">V2 can deliver — but <b>+22% over budget</b>. V3 silent. Aria can't pick between two of your rules.</div>
    </div>
  </div>
</div>

<style scoped>
.slide-bright {
  position: absolute; inset: 0; padding: 2.8rem 3.5rem;
  background: linear-gradient(180deg, #ffffff 0%, #fffbeb 100%);
  color: #111827; font-family: Inter, sans-serif;
}
.slide-eyebrow { font-size: 0.75rem; font-weight: 600; letter-spacing: 0.2em; text-transform: uppercase; }
.slide-title { font-size: 2.6rem; font-weight: 800; letter-spacing: -0.03em; margin: 0.3rem 0 0.4rem; color: #0f172a; }
.scenario-sub { font-size: 0.95rem; color: #64748b; margin-bottom: 1.5rem; }

.timeline-svg { width: 100%; max-width: 60rem; height: auto; display: block; margin: 0.5rem auto; }
.pulse-ring { animation: ringPulse 1.6s ease-in-out infinite; transform-origin: 880px 70px; }
@keyframes ringPulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.35; } }

.scenario-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1.2rem; margin-top: 1.2rem; }
.scen-card {
  padding: 1.2rem 1.3rem; border-radius: 1.2rem;
  background: #ffffff;
  box-shadow: 0 8px 22px -10px rgba(15, 23, 42, 0.12);
  border: 1px solid rgba(15, 23, 42, 0.05);
  display: flex; flex-direction: column; gap: 0.7rem;
}
.scen-green { border-top: 3px solid #10b981; }
.scen-amber { border-top: 3px solid #f59e0b; }
.scen-red { border-top: 3px solid #ef4444; }
.scen-chip {
  display: inline-block; align-self: flex-start;
  padding: 0.2rem 0.65rem; border-radius: 9999px;
  font-size: 0.68rem; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase;
}
.scen-body { font-size: 0.88rem; color: #334155; line-height: 1.5; }
.scen-body b { color: #0f172a; }
</style>

---
layout: none
title: The moment · live prototype
---

<div class="slide-bright slide-center moment-slide">
  <div class="slide-eyebrow" style="color:#3b82f6">The moment · live demo</div>
  <h2 class="moment-title">A single tap on a lock screen.</h2>
  <div class="moment-sub">Three things visible. Everything else a long-press away.</div>

  <a class="demo-cta" href="https://hands-free-help.lovable.app" target="_blank" rel="noopener">
    <div class="demo-phone-icon">
      <div class="demo-speaker"></div>
      <div class="demo-screen">
        <div class="demo-dot"></div>
        <div class="demo-text">🐟 Fish for tonight…</div>
        <div class="demo-bar"></div>
        <div class="demo-bar"></div>
      </div>
    </div>
    <div class="demo-cta-text">
      <div class="demo-cta-label">Open the live prototype</div>
      <div class="demo-cta-url">hands-free-help.lovable.app ↗</div>
    </div>
  </a>

  <div class="moment-footer">
    Source → <a href="https://github.com/roger704/hands-free-help" target="_blank">github.com/roger704/hands-free-help</a>
  </div>
</div>

<style scoped>
.slide-bright {
  position: absolute; inset: 0; padding: 2rem 3rem;
  background: linear-gradient(180deg, #ffffff 0%, #eff6ff 100%);
  color: #111827; font-family: Inter, sans-serif;
}
.slide-center { display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }
.slide-eyebrow { font-size: 0.75rem; font-weight: 600; letter-spacing: 0.2em; text-transform: uppercase; }
.moment-title { font-size: 2.4rem; font-weight: 800; letter-spacing: -0.03em; margin: 0.3rem 0 0.3rem; color: #0f172a; }
.moment-sub { font-size: 0.95rem; color: #64748b; margin-bottom: 1rem; max-width: 36rem; }

.demo-cta {
  margin-top: 2rem;
  display: flex; align-items: center; gap: 2rem;
  padding: 1.5rem 2.2rem 1.5rem 1.5rem;
  background: linear-gradient(135deg, #ffffff 0%, #eff6ff 100%);
  border-radius: 1.5rem;
  border: 1px solid rgba(59, 130, 246, 0.2);
  box-shadow: 0 20px 50px -16px rgba(59, 130, 246, 0.35), 0 2px 6px rgba(15, 23, 42, 0.06);
  text-decoration: none;
  color: inherit;
  transition: transform 0.15s ease, box-shadow 0.15s ease;
}
.demo-cta:hover { transform: translateY(-2px); box-shadow: 0 24px 60px -18px rgba(59, 130, 246, 0.45); }
.demo-phone-icon {
  width: 90px; height: 150px; background: #0f172a; border-radius: 1.2rem;
  padding: 10px 8px 10px; display: flex; flex-direction: column; align-items: stretch; gap: 6px;
  box-shadow: inset 0 0 0 2px rgba(255,255,255,0.08);
  flex-shrink: 0;
}
.demo-speaker { width: 28px; height: 3px; border-radius: 9999px; background: #334155; margin: 0 auto; }
.demo-screen {
  flex: 1; background: white; border-radius: 0.7rem; padding: 8px 7px;
  display: flex; flex-direction: column; gap: 4px; align-items: flex-start;
}
.demo-dot { width: 6px; height: 6px; border-radius: 9999px; background: #3b82f6; }
.demo-text { font-size: 8px; font-weight: 700; color: #0f172a; line-height: 1.1; }
.demo-bar { width: 100%; height: 4px; border-radius: 9999px; background: #e5edff; }
.demo-bar:last-child { width: 70%; }
.demo-cta-text { text-align: left; }
.demo-cta-label { font-size: 1.4rem; font-weight: 800; color: #0f172a; letter-spacing: -0.02em; }
.demo-cta-url {
  margin-top: 0.3rem;
  font-size: 1rem; font-weight: 600;
  background: linear-gradient(120deg, #3b82f6, #8b5cf6);
  -webkit-background-clip: text; background-clip: text; color: transparent;
  font-family: 'SF Mono', ui-monospace, monospace;
}

.moment-footer { margin-top: 1.8rem; font-size: 0.8rem; color: #94a3b8; }
.moment-footer a { color: #3b82f6; text-decoration: none; font-weight: 600; }
</style>

---
layout: none
title: Not a menu. An opinion.
---

<div class="slide-bright opinion-slide">
  <div class="opinion-left">
    <div class="slide-eyebrow" style="color:#8b5cf6">The insight</div>
    <h2 class="slide-title">Not a menu.<br/><span class="gradient-text-v">An opinion.</span></h2>
    <div class="opinion-body">
      Aria doesn't offer four neutral choices. She <b>picks one</b> — the call she'd make if she had the authority — and lets the manager override.
    </div>
    <div class="opinion-quote">
      Aria isn't a form. She's a colleague who has an opinion — and respects that you might overrule her.
    </div>
  </div>

  <div class="opinion-right">
    <div class="opt opt--picked">
      <div class="opt-top">
        <div class="opt-title">Accept Vendor 2's price</div>
        <div class="opt-badge">Aria's pick</div>
      </div>
      <div class="opt-meta">confidence 58% · +€180 over budget</div>
      <div class="confidence-bar"><div class="confidence-fill" style="width:58%"></div></div>
    </div>
    <div class="opt opt--muted">
      <div class="opt-title">Wait for Vendor 3's quote</div>
    </div>
    <div class="opt opt--muted">
      <div class="opt-title">Custom instructions…</div>
    </div>
    <div class="opt opt--muted">
      <div class="opt-title">Give me V2's contact — I'll call</div>
    </div>
  </div>
</div>

<style scoped>
.slide-bright {
  position: absolute; inset: 0; padding: 3rem 4rem;
  background: linear-gradient(180deg, #ffffff 0%, #faf5ff 100%);
  color: #111827; font-family: Inter, sans-serif;
}
.opinion-slide { display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; align-items: center; height: 100%; }
.slide-eyebrow { font-size: 0.75rem; font-weight: 600; letter-spacing: 0.2em; text-transform: uppercase; }
.slide-title { font-size: 3.6rem; font-weight: 800; letter-spacing: -0.03em; color: #0f172a; margin: 0.4rem 0 1rem; line-height: 1.05; }
.gradient-text-v {
  background: linear-gradient(120deg, #8b5cf6 0%, #3b82f6 100%);
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.opinion-body { font-size: 1.05rem; color: #475569; line-height: 1.55; max-width: 26rem; }
.opinion-body b { color: #0f172a; }
.opinion-quote {
  margin-top: 1.4rem;
  padding: 1rem 1.2rem;
  background: linear-gradient(135deg, #faf5ff, #eff6ff);
  border-left: 4px solid #8b5cf6;
  border-radius: 0.75rem;
  font-size: 0.95rem; color: #334155; font-style: italic; line-height: 1.5;
}

.opinion-right { display: flex; flex-direction: column; gap: 0.75rem; }
.opt {
  padding: 1rem 1.2rem;
  background: #ffffff;
  border-radius: 1rem;
  border: 1px solid rgba(15, 23, 42, 0.06);
  box-shadow: 0 4px 12px -6px rgba(15, 23, 42, 0.08);
}
.opt--picked {
  background: linear-gradient(135deg, #ecfdf5, #ffffff);
  border: 1.5px solid #10b981;
  box-shadow: 0 12px 28px -12px rgba(16, 185, 129, 0.3);
}
.opt--muted { opacity: 0.7; }
.opt-top { display: flex; justify-content: space-between; align-items: center; }
.opt-title { font-weight: 700; color: #0f172a; font-size: 1.05rem; }
.opt-badge {
  font-size: 0.65rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase;
  padding: 0.2rem 0.6rem; border-radius: 9999px;
  background: #10b981; color: white;
}
.opt-meta { font-size: 0.78rem; color: #64748b; margin-top: 0.3rem; }
.confidence-bar { margin-top: 0.6rem; height: 6px; border-radius: 9999px; background: #e2e8f0; overflow: hidden; }
.confidence-fill { height: 100%; background: linear-gradient(90deg, #10b981, #34d399); border-radius: 9999px; }
</style>

