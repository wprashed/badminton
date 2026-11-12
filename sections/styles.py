# Styles module for Badminton Cup - SupportHub Design System
CSS_CONTENT = """
<style>
/* ═══════════════════════════════════════════════════
   DESIGN TOKENS & RESET (SupportHub Clean Slate System)
═══════════════════════════════════════════════════ */
/* ═══════════════════════════════════════════════════
   DESIGN TOKENS & ATHLETIC SLATE PALETTE (SupportHub Redesign)
═══════════════════════════════════════════════════ */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html {
  touch-action: manipulation;
  -webkit-text-size-adjust: 100%;
}
:root {
  --bg-gradient: none;
  --clr-bg: #0b0f19;
  --clr-surface: rgba(17, 24, 39, 0.94);
  --clr-surface-hi: #1f2937;
  --clr-surface-card: #111827;
  --clr-border: #1f2937;
  --clr-border-subtle: rgba(255, 255, 255, 0.07);
  --clr-border-focus: #10b981;
  --clr-text: #f9fafb;
  --clr-text-muted: #9ca3af;
  --clr-text-subtle: #6b7280;
  --clr-green: #10b981;
  --clr-green-glow: rgba(16, 185, 129, 0.15);
  --clr-cyan: #06b6d4;
  --clr-gold: #f59e0b;
  --clr-gold-glow: rgba(245, 158, 11, 0.15);
  --clr-silver: #9ca3af;
  --clr-bronze: #d97706;
  --clr-red: #ef4444;
  --clr-blue: #3b82f6;
  --court-mat: #064e3b;
  --court-line: rgba(255, 255, 255, 0.95);
  --radius-xs: 6px;
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 16px;
  --radius-full: 9999px;
  --shadow-card: 0 4px 6px -1px rgba(0, 0, 0, 0.25), 0 2px 4px -2px rgba(0, 0, 0, 0.2);
  --shadow-dropdown: 0 20px 25px -5px rgba(0, 0, 0, 0.6), 0 8px 10px -6px rgba(0, 0, 0, 0.5);
  --font-display: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-body: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
}

body.theme-light {
  --bg-gradient: none;
  --clr-bg: #f8fafc;
  --clr-surface: rgba(255, 255, 255, 0.96);
  --clr-surface-hi: #f1f5f9;
  --clr-surface-card: #ffffff;
  --clr-border: #e2e8f0;
  --clr-border-subtle: #edf2f7;
  --clr-border-focus: #059669;
  --clr-text: #0f172a;
  --clr-text-muted: #64748b;
  --clr-text-subtle: #94a3b8;
  --clr-green: #059669;
  --clr-green-glow: rgba(5, 150, 105, 0.12);
  --court-mat: #047857;
  --court-line: #ffffff;
  --shadow-card: 0 1px 3px 0 rgba(0, 0, 0, 0.06), 0 1px 2px -1px rgba(0, 0, 0, 0.04);
  --shadow-dropdown: 0 10px 25px -5px rgba(0, 0, 0, 0.08), 0 8px 10px -6px rgba(0, 0, 0, 0.04);
}

body.theme-contrast {
  --bg-gradient: none;
  --clr-bg: #000000;
  --clr-surface: #111111;
  --clr-surface-hi: #222222;
  --clr-surface-card: #141414;
  --clr-border: #ffffff;
  --clr-border-subtle: #444444;
  --clr-border-focus: #ffff00;
  --clr-text: #ffffff;
  --clr-text-muted: #cccccc;
  --clr-text-subtle: #aaaaaa;
  --clr-green: #00ff00;
  --clr-gold: #ffff00;
  --clr-red: #ff3333;
  --clr-blue: #00ffff;
}

body {
  font-family: var(--font-body);
  background: var(--bg-gradient), var(--clr-bg);
  background-attachment: fixed;
  color: var(--clr-text);
  min-height: 100vh;
  line-height: 1.5;
  display: flex;
  flex-direction: column;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}

/* ═══════════════════════════════════════════════════
   VECTOR SINGLE-COLOR FLAT ICONS (FLATICONS)
═══════════════════════════════════════════════════ */
.icon {
  display: inline-block;
  width: 15px;
  height: 15px;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
  fill: none;
  vertical-align: -2px;
  flex-shrink: 0;
  transition: transform 120ms ease;
}
.icon-xs { width: 12px; height: 12px; stroke-width: 2; }
.icon-sm { width: 14px; height: 14px; stroke-width: 2; }
.icon-md { width: 16px; height: 16px; stroke-width: 2; }
.icon-lg { width: 18px; height: 18px; stroke-width: 2; }
.icon-xl { width: 22px; height: 22px; stroke-width: 2; }
.icon-2xl { width: 28px; height: 28px; stroke-width: 1.75; }
.icon-3xl { width: 38px; height: 38px; stroke-width: 1.5; }
.icon-fill { fill: currentColor; stroke: none; }
.tab-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: currentColor;
}
.tab-icon .icon { width: 15px; height: 15px; vertical-align: 0; }

/* ═══════════════════════════════════════════════════
   ACCESSIBILITY & FOCUS RINGS
═══════════════════════════════════════════════════ */
:focus-visible {
  outline: 2px solid var(--clr-green) !important;
  outline-offset: 2px !important;
}
button:focus-visible, input:focus-visible, select:focus-visible, textarea:focus-visible {
  outline: 2px solid var(--clr-green) !important;
  outline-offset: 2px !important;
}
.score-digit, .stat-value, .coin-val, #matchDurationClock, #userCoinBalance, td, th, .bracket-team-row span:last-child {
  font-variant-numeric: tabular-nums;
}

/* ═══════════════════════════════════════════════════
   APP TOURNAMENT STAGE NAVIGATION (SupportHub Pill Tabs)
═══════════════════════════════════════════════════ */
.app-stage-nav {
  position: sticky;
  top: 56px;
  z-index: 45;
  background: var(--clr-surface);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--clr-border);
  padding: 8px 24px;
  transition: opacity 200ms ease;
  box-sizing: border-box;
}
.stage-tab {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 7px 14px;
  border-radius: var(--radius-sm);
  border: 1px solid transparent;
  background: transparent;
  color: var(--clr-text-muted);
  font-size: 0.84rem;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  transition: all 140ms ease;
  text-decoration: none;
}
.stage-tab:hover {
  color: var(--clr-text);
  background: rgba(255, 255, 255, 0.05);
}
.stage-tab.active {
  color: var(--clr-green);
  background: rgba(16, 185, 129, 0.12);
  border-color: rgba(16, 185, 129, 0.3);
}
body.theme-light .app-stage-nav {
  background: rgba(255, 255, 255, 0.95);
  border-color: #e2e8f0;
}
body.theme-contrast .app-stage-nav {
  background: #000000;
  border-color: #ffffff;
}
.stage-nav-inner {
  max-width: 1280px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  gap: 4px;
  overflow-x: auto;
  scrollbar-width: none;
  -webkit-overflow-scrolling: touch;
}
.stage-nav-inner::-webkit-scrollbar {
  display: none;
}
.stage-tab {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  padding: 6px 12px;
  border-radius: var(--radius-sm);
  border: 1px solid transparent;
  background: transparent;
  color: var(--clr-text-muted);
  font-size: 0.81rem;
  font-weight: 500;
  cursor: pointer;
  white-space: nowrap;
  transition: all var(--transition-fast);
  text-decoration: none;
  touch-action: manipulation;
}
.stage-tab:hover {
  color: var(--clr-text);
  background: rgba(255, 255, 255, 0.05);
}
body.theme-light .stage-tab:hover {
  background: #f1f5f9;
  color: #0f172a;
}
.stage-tab.active {
  background: rgba(255, 255, 255, 0.08);
  border-color: rgba(255, 255, 255, 0.12);
  color: #ffffff;
  font-weight: 600;
}
body.theme-light .stage-tab.active {
  background: #ffffff;
  border-color: #cbd5e1;
  color: #0f172a;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}
body.theme-contrast .stage-tab.active {
  background: #ffffff;
  color: #000000;
  border-color: #ffffff;
}

/* ═══════════════════════════════════════════════════
   KEYBOARD HINTS & EMPTY STATES
═══════════════════════════════════════════════════ */
.kbd-hint {
  display: inline-block;
  font-family: monospace;
  font-size: 0.7rem;
  background: rgba(0, 0, 0, 0.35);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 4px;
  padding: 1px 5px;
  color: rgba(255, 255, 255, 0.8);
  margin-left: 6px;
  vertical-align: middle;
}
.empty-state-card {
  text-align: center;
  padding: 44px 24px;
  background: rgba(255, 255, 255, 0.02);
  border: 1px dashed var(--clr-border);
  border-radius: var(--radius-md);
  margin: 16px 0;
}
.empty-state-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 14px;
  color: var(--clr-text-muted);
  opacity: 0.85;
}
.empty-state-icon .icon { width: 36px; height: 36px; }
.empty-state-title {
  font-size: 1.1rem;
  font-weight: 600;
  letter-spacing: -0.01em;
  margin-bottom: 6px;
}
.empty-state-desc {
  font-size: 0.85rem;
  color: var(--clr-text-muted);
  max-width: 460px;
  margin: 0 auto 18px;
}

/* ═══════════════════════════════════════════════════
   HEADER & TOP BAR (SupportHub Clean Nav)
═══════════════════════════════════════════════════ */
.top-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  height: 56px;
  background: var(--clr-surface);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--clr-border);
  position: sticky;
  top: 0;
  z-index: 50;
  gap: 14px;
  flex-wrap: nowrap !important;
  box-sizing: border-box;
}
.brand-title {
  display: flex;
  align-items: center;
  gap: 8px;
}
.brand-badge {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  background: rgba(16, 185, 129, 0.12);
  border: 1px solid rgba(16, 185, 129, 0.25);
  color: #34d399;
  font-size: 0.68rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  padding: 3px 7px;
  border-radius: 4px;
  text-transform: uppercase;
}
.brand-heading {
  font-family: var(--font-display);
  font-size: 1.15rem;
  font-weight: 600;
  letter-spacing: -0.02em;
  text-transform: none;
  margin: 0;
  color: var(--clr-text);
}
.brand-heading .accent {
  color: var(--clr-green);
  font-weight: 700;
}

.user-panel {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: transparent;
  padding: 0;
  border: none;
}
.user-pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--clr-border);
  padding: 4px 10px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: all 140ms ease;
  user-select: none;
}
.user-pill:hover {
  background: rgba(255, 255, 255, 0.08);
  border-color: rgba(255, 255, 255, 0.2);
}
body.theme-light .user-pill {
  background: #f1f5f9;
  border-color: #cbd5e1;
}
body.theme-light .user-pill:hover {
  background: #e2e8f0;
}
body.theme-light .user-panel {
  background: #ffffff;
  border-color: #e2e8f0;
}
.user-avatar {
  width: 24px;
  height: 24px;
  border-radius: var(--radius-xs);
  background: var(--clr-surface-hi);
  border: 1px solid var(--clr-border);
  color: var(--clr-text);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  font-weight: 700;
}
.user-name-label {
  font-size: 0.8rem;
  font-weight: 600;
}
.user-role-badge {
  font-size: 0.62rem;
  background: rgba(245, 158, 11, 0.15);
  border: 1px solid rgba(245, 158, 11, 0.3);
  color: #fbbf24;
  font-weight: 600;
  padding: 2px 5px;
  border-radius: 3px;
  text-transform: uppercase;
  letter-spacing: 0.03em;
}

/* ═══════════════════════════════════════════════════
   BUTTONS & CONTROLS (SupportHub Flat Action Style)
═══════════════════════════════════════════════════ */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  font-family: inherit;
  font-weight: 600;
  font-size: 0.84rem;
  padding: 8px 14px;
  border-radius: var(--radius-sm);
  border: 1px solid transparent;
  cursor: pointer;
  transition: all var(--transition-fast);
  white-space: nowrap;
  user-select: none;
  -webkit-tap-highlight-color: transparent;
  min-height: 36px;
}
.btn-xs {
  font-size: 0.74rem;
  padding: 5px 9px;
  min-height: 28px;
}
.btn-sm {
  font-size: 0.78rem;
  padding: 6px 12px;
  min-height: 32px;
}
.btn-lg {
  font-size: 0.95rem;
  padding: 12px 20px;
  min-height: 44px;
}
.btn-primary {
  background: var(--clr-green);
  color: #0b0f19;
  border-color: var(--clr-green);
  font-weight: 700;
}
.btn-primary:hover {
  background: #059669;
  border-color: #059669;
  color: #ffffff;
}
.btn-secondary {
  background: var(--clr-surface-hi);
  color: var(--clr-text);
  border-color: var(--clr-border);
}
.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.12);
  border-color: var(--clr-border-focus);
}
.btn-ghost {
  background: transparent;
  color: var(--clr-text-muted);
  border-color: var(--clr-border);
}
.btn-ghost:hover {
  background: var(--clr-surface-hi);
  color: var(--clr-text);
  border-color: var(--clr-border-subtle);
}
.btn-ghost.active {
  background: var(--clr-surface-hi);
  color: var(--clr-green);
  border-color: var(--clr-green);
}
.btn-xs { padding: 4px 8px; font-size: 0.75rem; border-radius: var(--radius-xs); }
.btn-sm { padding: 5px 10px; font-size: 0.8rem; }
.btn-lg { padding: 10px 20px; font-size: 0.95rem; border-radius: var(--radius-sm); }

/* ═══════════════════════════════════════════════════
   LAYOUT & SCREEN CONTAINERS
═══════════════════════════════════════════════════ */
.main-content {
  flex: 1;
  max-width: 1280px;
  width: 100%;
  margin: 0 auto;
  padding: 24px 20px 80px;
}
.screen {
  display: none;
  animation: fadeIn 200ms ease-out;
}
.screen.active {
  display: block;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}

.card {
  background: var(--clr-surface-card);
  border: 1px solid var(--clr-border);
  border-radius: var(--radius-md);
  padding: 20px;
  box-shadow: var(--shadow-card);
}
.card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 18px;
  flex-wrap: wrap;
  gap: 12px;
}
.card-title {
  font-family: var(--font-display);
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: -0.01em;
  text-transform: none;
  display: flex;
  align-items: center;
  gap: 8px;
  color: var(--clr-text);
}

/* ═══════════════════════════════════════════════════
   COURT VISUALIZER & FLIPPED COURT
═══════════════════════════════════════════════════ */
.court-container {
  background: var(--court-mat);
  border: 3px solid var(--court-line);
  border-radius: var(--radius-md);
  padding: 16px;
  box-shadow: inset 0 0 30px rgba(0,0,0,0.5), 0 4px 16px rgba(0,0,0,0.3);
  margin-bottom: 20px;
  position: relative;
  perspective: 1000px;
  transition: all 400ms cubic-bezier(0.4, 0, 0.2, 1);
}
.court-flipped .badminton-court {
  transform: rotate(180deg);
}
.court-flipped .court-box span,
.court-flipped .court-player-name {
  transform: rotate(180deg);
}
/* Visual countdown overlay for 60s/120s intervals */
.interval-countdown-overlay {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(9, 13, 22, 0.92);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border-radius: var(--radius-md);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 20;
  animation: fadeIn 200ms ease;
}
.interval-countdown-digit {
  font-family: var(--font-display);
  font-size: 5.5rem;
  font-weight: 800;
  color: var(--clr-gold);
  line-height: 1;
  margin: 8px 0;
}
.interval-countdown-label {
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--clr-text-muted);
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

/* Digital Signature Canvas Pad */
.signature-canvas-container {
  border: 1px dashed var(--clr-border);
  border-radius: var(--radius-sm);
  background: rgba(0,0,0,0.25);
  position: relative;
  touch-action: none;
}
body.theme-light .signature-canvas-container {
  background: #f8fafc;
  border-color: #cbd5e1;
}
.signature-canvas {
  width: 100%;
  height: 110px;
  display: block;
  cursor: crosshair;
}

/* Radar comparison chart for H2H analytics */
.radar-chart-container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 16px;
}

/* Network Sync Indicator Pill in top bar */
.sync-pill {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: 0.7rem;
  font-weight: 600;
  padding: 3px 8px;
  border-radius: var(--radius-xs);
  background: rgba(16, 185, 129, 0.12);
  border: 1px solid rgba(16, 185, 129, 0.25);
  color: #34d399;
}
.sync-pill.offline {
  background: rgba(245, 158, 11, 0.12);
  border-color: rgba(245, 158, 11, 0.25);
  color: #fbbf24;
}

.badminton-court {
  display: grid;
  grid-template-columns: 1fr 14px 1fr;
  gap: 0;
  min-height: 220px;
  background: rgba(0,0,0,0.15);
  border: 2px solid var(--court-line);
  position: relative;
  transition: transform 300ms ease;
}
.court-side {
  display: grid;
  grid-template-rows: 1fr 1fr;
  grid-template-columns: 1fr;
  border-right: 2px solid var(--court-line);
  position: relative;
}
.court-side-b {
  border-right: none;
  border-left: 2px solid var(--court-line);
}
.court-net-line {
  background: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 8px rgba(255,255,255,0.7);
  position: relative;
  z-index: 2;
}
.court-net-line::before {
  content: 'NET';
  writing-mode: vertical-rl;
  font-size: 0.55rem;
  color: #000;
  font-weight: 800;
  letter-spacing: 0.2em;
}

.court-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-bottom: 2px solid var(--court-line);
  padding: 8px;
  font-size: 0.78rem;
  font-weight: 600;
  color: rgba(255,255,255,0.85);
  position: relative;
  transition: all 180ms ease;
  min-height: 90px;
}
.court-box:last-child {
  border-bottom: none;
}
.court-box.active-service {
  background: rgba(16, 185, 129, 0.4);
  box-shadow: inset 0 0 16px rgba(16, 185, 129, 0.6);
  color: #ffffff;
}
.court-box.active-receiver {
  background: rgba(59, 130, 246, 0.35);
  box-shadow: inset 0 0 16px rgba(59, 130, 246, 0.5);
  color: #ffffff;
}
.court-box-label {
  font-size: 0.65rem;
  opacity: 0.8;
  letter-spacing: 0.05em;
  margin-bottom: 4px;
}
.court-player-name {
  font-size: 0.95rem;
  font-weight: 700;
  text-shadow: 0 2px 4px rgba(0,0,0,0.8);
}

.diagonal-indicator {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(0,0,0,0.4);
  border: 1px solid rgba(255,255,255,0.2);
  padding: 4px 10px;
  border-radius: var(--radius-sm);
  font-size: 0.75rem;
  font-weight: 600;
}

/* ═══════════════════════════════════════════════════
   UMPIRE SCOREBOARD DIGITS & BADGES
═══════════════════════════════════════════════════ */
.score-board-grid {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  gap: 16px;
  margin-bottom: 24px;
}
.score-side-panel {
  background: var(--clr-surface-card);
  border: 1px solid var(--clr-border);
  border-radius: var(--radius-md);
  padding: 24px;
  text-align: center;
  position: relative;
  transition: all 160ms ease;
}
.score-side-panel.serving {
  border-color: var(--clr-green);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
}
.score-side-panel.serving::before {
  content: '• SERVING';
  position: absolute;
  top: -10px;
  right: 18px;
  background: var(--clr-green);
  color: #ffffff;
  font-size: 0.65rem;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: var(--radius-xs);
  letter-spacing: 0.06em;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
}
.score-digit {
  font-family: var(--font-display);
  font-size: 5rem;
  font-weight: 700;
  line-height: 1;
  color: #ffffff;
  margin: 10px 0;
  user-select: none;
  transition: transform 120ms ease;
}
body.theme-light .score-digit {
  color: #0f172a;
}
.score-digit.pop {
  transform: scale(1.12);
  color: var(--clr-green);
}
.player-name-main {
  font-size: 1.15rem;
  font-weight: 600;
  letter-spacing: -0.01em;
}

.set-pips {
  display: flex;
  justify-content: center;
  gap: 6px;
  margin-top: 8px;
}
.set-pip {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.12);
  border: 1px solid var(--clr-border);
}
.set-pip.won {
  background: var(--clr-green);
  border-color: var(--clr-green);
  box-shadow: 0 0 0 1px var(--clr-green);
}

/* Status Badges (SupportHub Flat Sub-surface Style) */
.status-badge-live {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 3px 8px;
  border-radius: var(--radius-xs);
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
.badge-game-point {
  background: rgba(245, 158, 11, 0.15);
  border: 1px solid rgba(245, 158, 11, 0.3);
  color: #fbbf24;
}
.badge-match-point {
  background: rgba(239, 68, 68, 0.15);
  border: 1px solid rgba(239, 68, 68, 0.3);
  color: #f87171;
}
.badge-deuce {
  background: rgba(139, 92, 246, 0.15);
  border: 1px solid rgba(139, 92, 246, 0.3);
  color: #c084fc;
}
.badge-sudden-death {
  background: rgba(239, 68, 68, 0.18);
  border: 1px solid rgba(239, 68, 68, 0.4);
  color: #fca5a5;
}
.badge-invited {
  background: rgba(245, 158, 11, 0.12);
  color: #fbbf24;
  border: 1px solid rgba(245, 158, 11, 0.25);
  padding: 2px 7px;
  border-radius: var(--radius-xs);
  font-size: 0.7rem;
  font-weight: 600;
}
.badge-active {
  background: rgba(16, 185, 129, 0.12);
  color: #34d399;
  border: 1px solid rgba(16, 185, 129, 0.25);
  padding: 2px 7px;
  border-radius: var(--radius-xs);
  font-size: 0.7rem;
  font-weight: 600;
}
.badge-declined {
  background: rgba(239, 68, 68, 0.12);
  color: #fca5a5;
  border: 1px solid rgba(239, 68, 68, 0.25);
  padding: 2px 7px;
  border-radius: var(--radius-xs);
  font-size: 0.7rem;
  font-weight: 600;
}
.badge-paid {
  background: rgba(16, 185, 129, 0.12);
  color: #34d399;
  border: 1px solid rgba(16, 185, 129, 0.25);
  font-size: 0.68rem;
  font-weight: 600;
  padding: 2px 6px;
  border-radius: 3px;
}
.badge-unpaid {
  background: rgba(239, 68, 68, 0.12);
  color: #fca5a5;
  border: 1px solid rgba(239, 68, 68, 0.25);
  font-size: 0.68rem;
  font-weight: 600;
  padding: 2px 6px;
  border-radius: 3px;
}

/* Skill Tiers */
.tier-badge {
  font-size: 0.68rem;
  font-weight: 600;
  padding: 2px 6px;
  border-radius: 3px;
  text-transform: uppercase;
  letter-spacing: 0.03em;
}
.tier-pro { background: rgba(239, 68, 68, 0.15); border: 1px solid rgba(239, 68, 68, 0.3); color: #f87171; }
.tier-advanced { background: rgba(59, 130, 246, 0.15); border: 1px solid rgba(59, 130, 246, 0.3); color: #60a5fa; }
.tier-club { background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.3); color: #34d399; }
.tier-novice { background: rgba(148, 163, 184, 0.15); border: 1px solid rgba(148, 163, 184, 0.3); color: #94a3b8; }

.hotkey-legend {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
  padding: 8px 12px;
  background: rgba(0, 0, 0, 0.2);
  border-radius: var(--radius-sm);
  font-size: 0.75rem;
  color: var(--clr-text-muted);
  margin-top: 14px;
  border: 1px solid var(--clr-border);
}
.hotkey-legend kbd {
  background: rgba(255, 255, 255, 0.1);
  color: #fff;
  padding: 1px 5px;
  border-radius: 3px;
  font-family: monospace;
  font-weight: 600;
  border: 1px solid rgba(255, 255, 255, 0.15);
}

/* ═══════════════════════════════════════════════════
   STADIUM ARENA TV MULTI-COURT DISPLAY
═══════════════════════════════════════════════════ */
.stadium-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 16px;
  margin-top: 16px;
}
.stadium-court-card {
  background: var(--clr-surface-card);
  border: 1px solid var(--clr-border);
  border-radius: var(--radius-md);
  padding: 18px;
  box-shadow: var(--shadow-card);
  position: relative;
  transition: all 180ms ease;
}
.stadium-court-card.live-court {
  border-color: var(--clr-green);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
}

/* ═══════════════════════════════════════════════════
   OBS STREAMING LOWER-THIRD OVERLAY
═══════════════════════════════════════════════════ */
body.obs-mode {
  background: transparent !important;
}
body.obs-mode .top-bar, body.obs-mode #appToast, body.obs-mode dialog, body.obs-mode .main-content > section:not(#obsOverlayContainer) {
  display: none !important;
}
.obs-lower-third {
  position: fixed;
  bottom: 24px;
  left: 24px;
  background: rgba(15, 23, 42, 0.96);
  border: 1px solid var(--clr-border);
  border-radius: var(--radius-md);
  padding: 12px 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8);
  display: flex;
  align-items: center;
  gap: 16px;
  z-index: 99999;
}

/* ═══════════════════════════════════════════════════
   TABLES & BRACKET NODES (SupportHub Sleek Data Tables)
═══════════════════════════════════════════════════ */
.data-table-container {
  overflow-x: auto;
  border-radius: var(--radius-sm);
  border: 1px solid var(--clr-border);
  background: var(--clr-surface-card);
}
.data-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.84rem;
  text-align: left;
}
.data-table th {
  background: rgba(0, 0, 0, 0.25);
  padding: 10px 14px;
  font-weight: 600;
  text-transform: uppercase;
  font-size: 0.7rem;
  letter-spacing: 0.05em;
  color: var(--clr-text-muted);
  border-bottom: 1px solid var(--clr-border);
}
body.theme-light .data-table th {
  background: #f8fafc;
  border-bottom: 1px solid #e2e8f0;
}
.data-table td {
  padding: 11px 14px;
  border-bottom: 1px solid var(--clr-border-subtle);
}
.data-table tr:hover td {
  background: rgba(255, 255, 255, 0.02);
}
body.theme-light .data-table tr:hover td {
  background: #f8fafc;
}

.bracket-container {
  display: flex;
  gap: 32px;
  overflow-x: auto;
  padding: 20px 8px;
}
.bracket-round {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  min-width: 250px;
  gap: 16px;
}
.bracket-round-header {
  font-family: var(--font-display);
  font-size: 0.95rem;
  font-weight: 600;
  text-transform: none;
  color: var(--clr-text);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  margin-bottom: 10px;
}
.bracket-match-card {
  background: var(--clr-surface-card);
  border: 1px solid var(--clr-border);
  border-radius: var(--radius-sm);
  padding: 12px;
  box-shadow: var(--shadow-card);
  position: relative;
}
.bracket-match-card.completed {
  border-color: rgba(16, 185, 129, 0.35);
}
.bracket-team-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 5px 8px;
  border-radius: 4px;
  font-size: 0.84rem;
  font-weight: 600;
}
.bracket-team-row.winner {
  background: rgba(16, 185, 129, 0.12);
  color: var(--clr-green);
}

/* ═══════════════════════════════════════════════════
   PLAYER PICKER & LISTS
═══════════════════════════════════════════════════ */
.player-picker-list {
  max-height: 280px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-top: 10px;
}
.player-picker-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 9px 12px;
  border-radius: var(--radius-sm);
  background: rgba(0, 0, 0, 0.2);
  border: 1px solid var(--clr-border);
  cursor: pointer;
  transition: all 140ms ease;
}
.player-picker-item:hover {
  border-color: var(--clr-green);
  background: rgba(16, 185, 129, 0.08);
}
.player-picker-item.selected {
  border-color: var(--clr-green);
  background: rgba(16, 185, 129, 0.15);
}

/* ═══════════════════════════════════════════════════
   MODALS & TOASTS (SupportHub Clean Overlays)
═══════════════════════════════════════════════════ */
dialog {
  border: 1px solid var(--clr-border);
  background: var(--clr-surface-card);
  color: var(--clr-text);
  border-radius: var(--radius-md);
  padding: 0;
  max-width: 92vw;
  width: auto;
  margin: auto;
  box-shadow: 0 20px 45px -10px rgba(0, 0, 0, 0.7);
  overflow: hidden;
}
dialog.modal {
  border: none !important;
  background: transparent !important;
  box-shadow: none !important;
  padding: 0 !important;
}
dialog.modal .modal-box {
  border: 1px solid var(--clr-border);
  background: var(--clr-surface-card);
  border-radius: var(--radius-md);
  box-shadow: 0 20px 45px -10px rgba(0, 0, 0, 0.7);
  width: 100%;
  margin: 0 auto;
  box-sizing: border-box;
}
body.theme-light dialog {
  background: #ffffff;
  border-color: #e2e8f0;
  box-shadow: 0 20px 45px -10px rgba(0, 0, 0, 0.15);
}
body.theme-light dialog.modal .modal-box {
  background: #ffffff !important;
  border-color: #e2e8f0 !important;
  box-shadow: 0 20px 45px -10px rgba(0, 0, 0, 0.15) !important;
}
dialog::backdrop {
  background: rgba(0, 0, 0, 0.65);
  backdrop-filter: blur(4px);
}
.modal-card, .modal-box {
  padding: 22px 24px 30px;
  background: var(--clr-surface-card);
  color: var(--clr-text);
  box-sizing: border-box;
  position: relative;
}
button.modal-close,
.modal-close {
  -webkit-appearance: none !important;
  appearance: none !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 32px !important;
  height: 32px !important;
  border-radius: var(--radius-xs) !important;
  background: transparent !important;
  background-color: transparent !important;
  border: none !important;
  box-shadow: none !important;
  color: var(--clr-text-muted) !important;
  cursor: pointer !important;
  padding: 0 !important;
  margin: 0 !important;
  transition: all 140ms ease !important;
  font-family: inherit !important;
  -webkit-tap-highlight-color: transparent !important;
  outline: none !important;
}
button.modal-close:hover,
.modal-close:hover {
  background: rgba(255, 255, 255, 0.08) !important;
  background-color: rgba(255, 255, 255, 0.08) !important;
  color: var(--clr-text) !important;
}
button.modal-close .icon,
.modal-close .icon {
  width: 18px !important;
  height: 18px !important;
  stroke: currentColor !important;
  stroke-width: 2.2 !important;
  fill: none !important;
}
.modal-card {
  padding: 22px;
}
.modal-form-item {
  margin-bottom: 14px;
}
.modal-form-item label {
  display: block;
  font-size: 0.78rem;
  font-weight: 600;
  margin-bottom: 5px;
  color: var(--clr-text-muted);
}
.modal-input {
  width: 100%;
  padding: 8px 12px;
  background: rgba(0, 0, 0, 0.25);
  border: 1px solid var(--clr-border);
  border-radius: var(--radius-sm);
  color: #fff;
  font-family: inherit;
  font-size: 0.88rem;
  transition: border-color 140ms ease, box-shadow 140ms ease;
  box-sizing: border-box;
}
body.theme-light .modal-input {
  background: #ffffff;
  color: #0f172a;
  border-color: #cbd5e1;
}
.modal-input:focus {
  outline: none;
  border-color: var(--clr-green);
  box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.25);
}

/* Universal Modern Accessible Form Select */
select.modal-input,
select.app-custom-select,
.app-custom-select,
.modal-box select {
  -webkit-appearance: none !important;
  -moz-appearance: none !important;
  appearance: none !important;
  background-color: rgba(15, 23, 42, 0.6) !important;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%2394a3b8' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E") !important;
  background-repeat: no-repeat !important;
  background-position: calc(100% - 12px) center !important;
  background-size: 14px 14px !important;
  padding-right: 36px !important;
  cursor: pointer !important;
  border: 1px solid var(--clr-border) !important;
  border-radius: var(--radius-sm) !important;
  color: var(--clr-text) !important;
  font-family: inherit !important;
  font-size: 0.88rem !important;
  line-height: 1.4 !important;
  transition: border-color 140ms ease, box-shadow 140ms ease !important;
  box-sizing: border-box !important;
}

select.modal-input:focus,
select.app-custom-select:focus,
.app-custom-select:focus,
.modal-box select:focus {
  outline: none !important;
  border-color: var(--clr-green) !important;
  box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.25) !important;
}

select.modal-input option,
select.app-custom-select option,
.app-custom-select option,
.modal-box select option {
  background-color: #0f172a !important;
  color: #f8fafc !important;
  padding: 8px !important;
}

/* Light Theme Select Rules - Explicit No-Repeat and Single Position */
body.theme-light select.modal-input,
body.theme-light select.app-custom-select,
body.theme-light .app-custom-select,
body.theme-light .modal-box select {
  background-color: #ffffff !important;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23475569' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E") !important;
  background-repeat: no-repeat !important;
  background-position: calc(100% - 12px) center !important;
  background-size: 14px 14px !important;
  padding-right: 36px !important;
  color: #0f172a !important;
  border-color: #cbd5e1 !important;
}

body.theme-light select.modal-input option,
body.theme-light select.app-custom-select option,
body.theme-light .app-custom-select option,
body.theme-light .modal-box select option {
  background-color: #ffffff !important;
  color: #0f172a !important;
}

#appToast {
  position: fixed;
  bottom: 24px;
  right: 24px;
  background: #1e293b;
  border: 1px solid var(--clr-border);
  color: #fff;
  padding: 10px 18px;
  border-radius: var(--radius-sm);
  box-shadow: var(--shadow-dropdown);
  font-weight: 600;
  font-size: 0.84rem;
  display: none;
  align-items: center;
  gap: 8px;
  z-index: 100;
  animation: slideUp 180ms ease;
}
body.theme-light #appToast {
  background: #ffffff;
  color: #0f172a;
  border-color: #cbd5e1;
}
#appToast.show { display: inline-flex; }
@keyframes slideUp {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}

/* ═══════════════════════════════════════════════════
   TOURNAMENT SCHEDULE, RULES & ANALYTICS PAGES
═══════════════════════════════════════════════════ */
.schedule-filter-bar {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 18px;
  background: rgba(0, 0, 0, 0.2);
  padding: 10px 14px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--clr-border);
}
body.theme-light .schedule-filter-bar {
  background: #ffffff;
  border-color: #e2e8f0;
}
.schedule-card {
  background: var(--clr-surface-card);
  border: 1px solid var(--clr-border);
  border-radius: var(--radius-sm);
  padding: 14px 16px;
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  flex-wrap: wrap;
  transition: all var(--transition-fast);
}
.schedule-card:hover {
  border-color: rgba(16, 185, 129, 0.35);
  background: rgba(16, 185, 129, 0.04);
}
.schedule-card.live-fixture {
  border-color: var(--clr-green);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.25);
}
.court-pill {
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: 0.02em;
  padding: 3px 8px;
  border-radius: var(--radius-xs);
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid var(--clr-border);
  color: var(--clr-text-muted);
}
.rules-card {
  background: var(--clr-surface-card);
  border: 1px solid var(--clr-border);
  border-radius: var(--radius-md);
  padding: 18px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.rules-card h3 {
  font-family: var(--font-display);
  font-size: 1.05rem;
  font-weight: 600;
  text-transform: none;
  color: var(--clr-text);
  display: flex;
  align-items: center;
  gap: 8px;
}
.rules-callout {
  background: rgba(0, 0, 0, 0.25);
  border-left: 3px solid var(--clr-gold);
  padding: 8px 12px;
  border-radius: 0 var(--radius-xs) var(--radius-xs) 0;
  font-size: 0.83rem;
  margin: 4px 0;
}
.h2h-compare-bar {
  display: flex;
  align-items: center;
  gap: 10px;
  margin: 8px 0;
}
.h2h-bar-segment {
  height: 6px;
  border-radius: var(--radius-full);
  transition: width 300ms ease;
}

/* ═══════════════════════════════════════════════════
   PRINT STYLESHEET
═══════════════════════════════════════════════════ */
@media print {
  body {
    background: #ffffff !important;
    color: #000000 !important;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }
  .top-bar, .app-stage-nav, .btn, #userStatusPanel, .hotkey-legend, #appToast, dialog:not([open]) {
    display: none !important;
  }
  .screen {
    display: block !important;
    max-width: 100% !important;
    padding: 0 !important;
  }
  .card {
    border: 1px solid #ccc !important;
    box-shadow: none !important;
    background: #fff !important;
    color: #000 !important;
    page-break-inside: avoid;
  }
  .bracket-container {
    overflow: visible !important;
    gap: 16px !important;
  }
  .bracket-match-card {
    border: 1px solid #333 !important;
    background: #fff !important;
    color: #000 !important;
  }
  .bracket-team-row.winner {
    background: #eee !important;
    font-weight: bold !important;
    color: #000 !important;
  }
  .scorecard-sheet {
    display: block !important;
    page-break-before: always;
  }
}

/* ═══════════════════════════════════════════════════
   CORE CARDS & INTERACTION BUTTONS (Clean Modern Style)
═══════════════════════════════════════════════════ */
.card {
  background: var(--clr-surface-card);
  border: 1px solid var(--clr-border);
  border-radius: var(--radius-md);
  padding: 18px;
  box-shadow: var(--shadow-card);
  transition: all var(--transition-fast);
  box-sizing: border-box;
}
.card:hover {
  border-color: rgba(255, 255, 255, 0.14);
}
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 14px;
  flex-wrap: wrap;
  gap: 10px;
}
.card-title {
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--clr-text);
  display: flex;
  align-items: center;
  gap: 8px;
  letter-spacing: -0.01em;
}

/* Quick Action Match Buttons on Cards */
.quick-match-row {
  display: flex;
  gap: 6px;
  margin-top: 10px;
  padding-top: 10px;
  border-top: 1px solid var(--clr-border);
  flex-wrap: wrap;
  width: 100%;
  box-sizing: border-box;
}
.quick-win-btn {
  flex: 1;
  min-width: 85px;
  padding: 6px 10px;
  font-size: 0.74rem;
  font-weight: 700;
  border-radius: var(--radius-xs);
  background: rgba(16, 185, 129, 0.12);
  border: 1px solid rgba(16, 185, 129, 0.35);
  color: #34d399;
  cursor: pointer;
  transition: all 140ms ease;
  text-align: center;
  font-family: inherit;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
}
.quick-win-btn:hover {
  background: #10b981;
  color: #ffffff;
}
.quick-score-btn {
  padding: 6px 12px;
  font-size: 0.74rem;
  font-weight: 600;
  border-radius: var(--radius-xs);
  background: var(--clr-surface-hi);
  border: 1px solid var(--clr-border);
  color: var(--clr-text-muted);
  cursor: pointer;
  transition: all 140ms ease;
  font-family: inherit;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
}
.quick-score-btn:hover {
  background: rgba(255, 255, 255, 0.1);
  color: var(--clr-text);
}

/* Open Challenge Board */
.challenge-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(100%, 280px), 1fr));
  gap: 14px;
  margin-top: 14px;
}
.challenge-card {
  background: var(--clr-surface-card);
  border: 1px solid var(--clr-border);
  border-radius: var(--radius-sm);
  padding: 16px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 12px;
  position: relative;
  transition: all 140ms ease;
  box-sizing: border-box;
}
.challenge-card:hover {
  border-color: var(--clr-green);
}
.challenge-card.open-status {
  border-left: 3px solid #10b981;
}
.challenge-card.accepted-status {
  border-left: 3px solid #3b82f6;
}
.challenge-badge {
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  padding: 2px 6px;
  border-radius: 3px;
  letter-spacing: 0.03em;
}
.challenge-badge.open {
  background: rgba(16, 185, 129, 0.15);
  color: #34d399;
  border: 1px solid rgba(16, 185, 129, 0.3);
}
.challenge-badge.accepted {
  background: rgba(59, 130, 246, 0.15);
  color: #60a5fa;
  border: 1px solid rgba(59, 130, 246, 0.3);
}

/* Reset Danger Button */
.btn-danger-reset {
  background: rgba(239, 68, 68, 0.15);
  border: 1px solid rgba(239, 68, 68, 0.4);
  color: #f87171;
  font-weight: 600;
  transition: all 140ms ease;
}
.btn-danger-reset:hover {
  background: #ef4444;
  color: #ffffff;
}

/* Streamlined Mobile & PWA Navigation Buttons */
.notify-btn {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 6px 10px;
  border-radius: var(--radius-sm);
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--clr-border);
  color: var(--clr-text-muted);
  cursor: pointer;
  transition: all 150ms ease;
  font-family: inherit;
  font-size: 0.8rem;
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
}
.notify-btn:hover {
  background: rgba(255, 255, 255, 0.1);
  color: var(--clr-text);
}
.notify-btn.active {
  color: #34d399;
  border-color: rgba(16, 185, 129, 0.4);
  background: rgba(16, 185, 129, 0.12);
}
.notify-badge-dot {
  position: absolute;
  top: 4px;
  right: 4px;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #10b981;
  box-shadow: none;
  display: none;
}
.notify-btn.active .notify-badge-dot {
  display: block;
}

.install-app-pill {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 5px 11px;
  border-radius: var(--radius-sm);
  background: rgba(16, 185, 129, 0.15);
  border: 1px solid rgba(16, 185, 129, 0.35);
  color: #34d399;
  font-size: 0.76rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 150ms ease;
  font-family: inherit;
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
}
.install-app-pill:hover {
  background: #10b981;
  color: #ffffff;
}

/* More Menu Drawer / Grid */
.more-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(100%, 210px), 1fr));
  gap: 12px;
  margin-top: 14px;
  margin-bottom: 20px;
}
.more-card-item {
  background: var(--clr-surface-card);
  border: 1px solid var(--clr-border);
  border-radius: var(--radius-sm);
  padding: 12px 14px;
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  transition: all 140ms ease;
  text-align: left;
  width: 100%;
  color: var(--clr-text);
  font-family: inherit;
  box-sizing: border-box;
}
.more-card-item:hover {
  border-color: var(--clr-green);
  background: rgba(16, 185, 129, 0.06);
  transform: translateY(-1px);
}
.more-card-icon {
  width: 36px;
  height: 36px;
  border-radius: var(--radius-xs);
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--clr-border);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--clr-green);
  flex-shrink: 0;
}
.more-card-text {
  display: flex;
  flex-direction: column;
}
.more-card-title {
  font-size: 0.86rem;
  font-weight: 700;
  color: var(--clr-text);
}
.more-card-desc {
  font-size: 0.72rem;
  color: var(--clr-text-muted);
  margin-top: 2px;
}

/* Mobile Bottom Navigation Bar (Fixed 5-Tab Bar) */
.mobile-bottom-nav {
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: calc(58px + env(safe-area-inset-bottom, 0px));
  padding-bottom: env(safe-area-inset-bottom, 0px);
  background: var(--clr-surface);
  border-top: 1px solid var(--clr-border);
  z-index: 990;
  box-shadow: 0 -4px 20px rgba(0, 0, 0, 0.45);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
}
body.theme-light .mobile-bottom-nav {
  background: rgba(255, 255, 255, 0.96);
  border-color: #e2e8f0;
}
body.theme-contrast .mobile-bottom-nav {
  background: #000000;
  border-color: #ffffff;
}

.mobile-bottom-nav-inner {
  display: flex;
  height: 100%;
  max-width: 650px;
  margin: 0 auto;
  align-items: stretch;
  justify-content: space-around;
}

.mobile-nav-btn {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2px;
  padding: 4px 0;
  color: var(--clr-text-muted);
  text-decoration: none;
  background: transparent;
  border: none;
  cursor: pointer;
  min-height: 48px;
  font-family: inherit;
  font-size: 0.72rem;
  font-weight: 600;
  transition: color 150ms ease;
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
}
.mobile-nav-btn .icon {
  width: 20px;
  height: 20px;
  stroke-width: 2;
  transition: transform 150ms ease, color 150ms ease;
}
.mobile-nav-btn:hover {
  color: var(--clr-text);
}
.mobile-nav-btn.active {
  color: var(--clr-green);
}
.mobile-nav-btn.active .icon {
  transform: translateY(-2px);
  color: var(--clr-green);
}

/* ═══════════════════════════════════════════════════
   100% MOBILE RESPONSIVE ENGINE (Tablets, Mobiles, Foldables)
═══════════════════════════════════════════════════ */

/* ── Tablet & Small Laptops (<= 1024px) ── */
@media (max-width: 1024px) {
  .top-bar {
    padding: 10px 16px;
  }
  .bracket-container {
    gap: 20px;
  }
}

/* ── Tablet Portrait & Large Mobiles (<= 768px) ── */
@media (max-width: 768px) {
  /* Layout & Navigation */
  .top-bar {
    padding: 8px 12px;
    gap: 6px;
    flex-wrap: nowrap !important;
    min-height: 50px;
  }
  .brand-heading {
    font-size: 1rem;
    white-space: nowrap;
  }
  .brand-badge {
    display: none !important;
  }
  #headerMoreBtn {
    display: none !important; /* Managed by 5th tab on bottom nav */
  }
  .app-stage-nav {
    display: none !important;
  }
  .mobile-bottom-nav {
    display: block !important;
  }
  .main-content {
    padding: 12px 10px calc(76px + env(safe-area-inset-bottom, 0px)) !important;
    max-width: 100vw;
    overflow-x: hidden;
    box-sizing: border-box;
  }

  /* Cards & Containers */
  .card {
    padding: 14px 12px;
    border-radius: var(--radius-sm);
  }
  .card-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
    margin-bottom: 12px;
  }
  .card-title {
    font-size: 0.95rem;
  }

  /* Grids */
  .more-grid {
    grid-template-columns: 1fr;
  }
  .pools-grid {
    grid-template-columns: 1fr !important;
    gap: 14px !important;
  }
  #groupMatchesContainer {
    grid-template-columns: 1fr !important;
  }

  /* Live Scoreboard */
  .score-board-grid {
    grid-template-columns: 1fr;
    gap: 12px;
  }
  .score-digit {
    font-size: 3.8rem;
  }

  /* Modals */
  dialog {
    width: 94vw !important;
    max-width: 94vw !important;
    max-height: 86dvh !important;
    max-height: 86vh !important;
    margin: auto !important;
    overflow-y: auto !important;
    -webkit-overflow-scrolling: touch !important;
    box-sizing: border-box !important;
  }
  .modal-card, .modal-box {
    padding: 16px 12px !important;
  }

  /* Tournament Bracket Touch-Swiping */
  .bracket-container {
    padding: 12px 6px 18px;
    gap: 16px;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    scroll-snap-type: x mandatory;
    scrollbar-width: thin;
  }
  .bracket-round {
    min-width: 240px;
    max-width: 84vw;
    scroll-snap-align: center;
    flex-shrink: 0;
  }

  /* Tables Containment */
  .data-table-container {
    width: 100%;
    max-width: 100%;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    overscroll-behavior-x: contain;
  }
  .data-table th, .data-table td {
    padding: 8px 10px;
    font-size: 0.76rem;
    white-space: nowrap;
  }
}

/* ── Standard Phones (<= 600px, e.g. iPhone 13/14/15/16, Pixel, Galaxy) ── */
@media (max-width: 600px) {
  .top-bar {
    padding: 6px 8px;
    gap: 4px;
  }
  .brand-heading {
    font-size: 0.92rem;
  }
  #networkSyncPill #syncStatusLabel {
    display: none !important;
  }
  #networkSyncPill {
    padding: 3px 6px;
  }
  #headerCoinBtn {
    padding: 3px 6px;
    font-size: 0.72rem;
    gap: 3px;
  }
  #userStatusPanel {
    padding: 2px 4px;
    gap: 4px;
  }
  #userStatusPanel .user-avatar {
    width: 26px;
    height: 26px;
    font-size: 0.72rem;
  }
  #headerUsername {
    display: none !important;
  }
  #authBtn {
    padding: 3px 7px;
    font-size: 0.7rem;
  }
  #installAppBtn span {
    display: none !important;
  }
  #installAppBtn {
    padding: 4px 6px;
  }

  /* Match Card 2-Tier Responsive Quick Actions (50/50 Win, 33/33/33 Tools) */
  .quick-match-row {
    display: grid !important;
    grid-template-columns: repeat(6, 1fr) !important;
    gap: 6px !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }
  .quick-match-row > .quick-win-btn:first-of-type {
    grid-column: 1 / span 3 !important;
    grid-row: 1 !important;
    min-height: 42px !important;
    font-size: 0.76rem !important;
  }
  .quick-match-row > .quick-win-btn:last-of-type {
    grid-column: 4 / span 3 !important;
    grid-row: 1 !important;
    min-height: 42px !important;
    font-size: 0.76rem !important;
  }
  .quick-match-row > .quick-score-btn {
    grid-column: 1 / span 2 !important;
    grid-row: 2 !important;
    min-height: 38px !important;
    font-size: 0.72rem !important;
  }
  .quick-match-row > button[onclick*="openBettingModal"] {
    grid-column: 3 / span 2 !important;
    grid-row: 2 !important;
    min-height: 38px !important;
    font-size: 0.72rem !important;
  }
  .quick-match-row > button[onclick*="startUmpireMatch"] {
    grid-column: 5 / span 2 !important;
    grid-row: 2 !important;
    min-height: 38px !important;
    font-size: 0.72rem !important;
  }

  /* Completed Match Card Actions */
  .quick-match-row > div[style*="display:flex"] {
    width: 100% !important;
    flex-direction: column !important;
    align-items: stretch !important;
    gap: 8px !important;
  }
  .quick-match-row > div[style*="display:flex"] > div {
    display: flex !important;
    width: 100% !important;
    gap: 6px !important;
  }
  .quick-match-row > div[style*="display:flex"] > div > button {
    flex: 1 !important;
    min-height: 38px !important;
  }

  /* Grids & Cards */
  .challenge-grid {
    grid-template-columns: 1fr !important;
  }
  #scorecardsGalleryContainer {
    grid-template-columns: 1fr !important;
  }

  /* Form Inputs (16px to prevent iOS Safari auto-zoom on focus) */
  input, select, textarea, .modal-input {
    font-size: 16px !important;
  }
  .btn {
    min-height: 36px;
  }
}

/* ── Ultra-Compact / Foldable Outer Screens (<= 380px, e.g. iPhone SE, Galaxy Z Fold) ── */
@media (max-width: 380px) {
  .top-bar {
    padding: 5px 6px;
    gap: 3px;
  }
  .brand-heading {
    font-size: 0.85rem;
  }
  #networkSyncPill {
    display: none !important; /* Hide completely on ultra-narrow viewports */
  }
  #headerCoinBtn {
    padding: 2px 4px;
    font-size: 0.68rem;
  }
  #notifyBtn {
    padding: 4px 6px;
  }
  .quick-win-btn, .quick-score-btn {
    font-size: 0.68rem !important;
    padding: 4px 4px !important;
  }
  .mobile-nav-btn {
    font-size: 0.65rem;
  }
  .mobile-nav-btn .icon {
    width: 18px;
    height: 18px;
  }
  .card {
    padding: 12px 10px;
  }
}

/* ── Touch Ergonomics (Mobile Browsers) ── */
@media (hover: none) and (pointer: coarse) {
  button, a, input, select {
    touch-action: manipulation;
    -webkit-tap-highlight-color: transparent;
  }
  .card:hover, .more-card-item:hover, .challenge-card:hover {
    transform: none !important;
  }
}


/* ═══════════════════════════════════════════════════
   LIGHT MODE COMPONENT SYSTEM (Clean Gymnasium Theme)
═══════════════════════════════════════════════════ */
body.theme-light {
  background: #f8fafc !important;
  color: #0f172a !important;
}

body.theme-light .top-bar {
  background: rgba(255, 255, 255, 0.96) !important;
  border-bottom: 1px solid #e2e8f0 !important;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

body.theme-light .brand-heading {
  color: #0f172a !important;
}

body.theme-light .card {
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05), 0 1px 2px rgba(0, 0, 0, 0.03) !important;
  color: #0f172a !important;
}

body.theme-light .card:hover {
  border-color: #cbd5e1 !important;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.07) !important;
}

body.theme-light .card-title {
  color: #0f172a !important;
}

body.theme-light .btn-primary {
  background: #059669 !important;
  color: #ffffff !important;
  border-color: #059669 !important;
}

body.theme-light .btn-primary:hover {
  background: #047857 !important;
  border-color: #047857 !important;
  color: #ffffff !important;
}

body.theme-light .btn-ghost {
  background: transparent !important;
  color: #475569 !important;
  border-color: #cbd5e1 !important;
}

body.theme-light .btn-ghost:hover {
  background: #f1f5f9 !important;
  color: #0f172a !important;
  border-color: #94a3b8 !important;
}

body.theme-light .btn-secondary {
  background: #f1f5f9 !important;
  color: #0f172a !important;
  border-color: #cbd5e1 !important;
}

body.theme-light .btn-secondary:hover {
  background: #e2e8f0 !important;
  color: #0f172a !important;
}

body.theme-light .quick-win-btn {
  background: rgba(5, 150, 105, 0.1) !important;
  border: 1px solid rgba(5, 150, 105, 0.3) !important;
  color: #047857 !important;
}

body.theme-light .quick-win-btn:hover {
  background: #059669 !important;
  color: #ffffff !important;
}

body.theme-light .quick-score-btn {
  background: #f1f5f9 !important;
  border: 1px solid #cbd5e1 !important;
  color: #334155 !important;
}

body.theme-light .quick-score-btn:hover {
  background: #e2e8f0 !important;
  color: #0f172a !important;
}

body.theme-light .sync-pill {
  background: #f1f5f9 !important;
  border: 1px solid #cbd5e1 !important;
  color: #475569 !important;
}

body.theme-light .notify-btn {
  background: #ffffff !important;
  border: 1px solid #cbd5e1 !important;
  color: #475569 !important;
}

body.theme-light .notify-btn:hover {
  background: #f1f5f9 !important;
  color: #0f172a !important;
}

body.theme-light .data-table-container {
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
}

body.theme-light .data-table th {
  background: #f8fafc !important;
  border-bottom: 1px solid #cbd5e1 !important;
  color: #475569 !important;
}

body.theme-light .data-table td {
  border-bottom: 1px solid #f1f5f9 !important;
  color: #0f172a !important;
}

body.theme-light .data-table tr:hover td {
  background: #f8fafc !important;
}

body.theme-light .bracket-match-card {
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
}

body.theme-light .bracket-match-card.completed {
  border-color: rgba(5, 150, 105, 0.4) !important;
}

body.theme-light .bracket-team-row {
  color: #0f172a !important;
}

body.theme-light .bracket-team-row.winner {
  background: rgba(5, 150, 105, 0.1) !important;
  color: #047857 !important;
}

body.theme-light .challenge-card {
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
}

body.theme-light .challenge-card:hover {
  border-color: #059669 !important;
}

body.theme-light .challenge-badge.open {
  background: rgba(5, 150, 105, 0.12) !important;
  color: #047857 !important;
  border: 1px solid rgba(5, 150, 105, 0.25) !important;
}

body.theme-light .challenge-badge.accepted {
  background: rgba(37, 99, 235, 0.12) !important;
  color: #1d4ed8 !important;
  border: 1px solid rgba(37, 99, 235, 0.25) !important;
}

body.theme-light .more-card-item {
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
  color: #0f172a !important;
}

body.theme-light .more-card-item:hover {
  background: #f8fafc !important;
  border-color: #059669 !important;
}

body.theme-light .more-card-icon {
  background: #f1f5f9 !important;
  border: 1px solid #e2e8f0 !important;
  color: #059669 !important;
}

body.theme-light .more-card-title {
  color: #0f172a !important;
}

body.theme-light .more-card-desc {
  color: #64748b !important;
}

body.theme-light dialog {
  background: #ffffff !important;
  color: #0f172a !important;
  border: 1px solid #cbd5e1 !important;
  box-shadow: 0 20px 45px -10px rgba(0, 0, 0, 0.18) !important;
}

body.theme-light .modal-box,
body.theme-light .modal-card {
  background: #ffffff !important;
  color: #0f172a !important;
}

body.theme-light .modal-close {
  color: #64748b !important;
}

body.theme-light .modal-close:hover {
  background: #f1f5f9 !important;
  color: #0f172a !important;
  border-color: #cbd5e1 !important;
}

body.theme-light input:not([type="checkbox"]):not([type="radio"]),
body.theme-light textarea {
  background-color: #ffffff !important;
  color: #0f172a !important;
  border: 1px solid #cbd5e1 !important;
}

body.theme-light input:focus,
body.theme-light select:focus,
body.theme-light textarea:focus {
  border-color: #059669 !important;
  box-shadow: 0 0 0 1px #059669 !important;
}

body.theme-light .mobile-bottom-nav {
  background: rgba(255, 255, 255, 0.96) !important;
  border-top: 1px solid #e2e8f0 !important;
  box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.05) !important;
}

body.theme-light .mobile-nav-btn {
  color: #64748b !important;
}

body.theme-light .mobile-nav-btn:hover {
  color: #0f172a !important;
}

body.theme-light .mobile-nav-btn.active {
  color: #059669 !important;
}

body.theme-light .user-panel {
  background: #f1f5f9 !important;
  border: 1px solid #e2e8f0 !important;
}

body.theme-light .user-avatar {
  background: #e2e8f0 !important;
  border: 1px solid #cbd5e1 !important;
  color: #0f172a !important;
}

body.theme-light #matchDurationClock {
  background: #f1f5f9 !important;
  color: #0f172a !important;
  border: 1px solid #cbd5e1 !important;
}


/* ═══════════════════════════════════════════════════
   ROLE-BASED PRIVILEGE CONTROL (STRICT HIDING)
   Non-admins (guests and players) never see admin sections
═══════════════════════════════════════════════════ */
body:not(.role-admin) .admin-only-item {
  display: none !important;
}

body.role-admin .admin-only-item {
  /* Default display when admin is logged in */
}

/* Modal close button hardening */
button.modal-close,
.modal-close,
dialog .modal-close {
  -webkit-appearance: none !important;
  -moz-appearance: none !important;
  appearance: none !important;
  box-sizing: border-box !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 32px !important;
  height: 32px !important;
  min-width: 32px !important;
  min-height: 32px !important;
  padding: 0 !important;
  margin: 0 !important;
  background: rgba(255, 255, 255, 0.05) !important;
  background-color: rgba(255, 255, 255, 0.05) !important;
  border: 1px solid var(--clr-border) !important;
  border-radius: var(--radius-xs) !important;
  color: var(--clr-text-muted) !important;
  cursor: pointer !important;
  transition: all 140ms ease !important;
  outline: none !important;
  box-shadow: none !important;
}

button.modal-close:hover,
.modal-close:hover,
dialog .modal-close:hover {
  background: rgba(255, 255, 255, 0.12) !important;
  background-color: rgba(255, 255, 255, 0.12) !important;
  color: var(--clr-text) !important;
  border-color: rgba(255, 255, 255, 0.25) !important;
}

body.theme-light button.modal-close,
body.theme-light .modal-close,
body.theme-light dialog .modal-close {
  background: #f1f5f9 !important;
  background-color: #f1f5f9 !important;
  border: 1px solid #cbd5e1 !important;
  color: #475569 !important;
}

body.theme-light button.modal-close:hover,
body.theme-light .modal-close:hover,
body.theme-light dialog .modal-close:hover {
  background: #e2e8f0 !important;
  background-color: #e2e8f0 !important;
  color: #0f172a !important;
  border-color: #94a3b8 !important;
}


/* ═══════════════════════════════════════════════════
   MODAL SCROLL LOCK & PRINT STYLES
═══════════════════════════════════════════════════ */
body.modal-open {
  overflow: hidden !important;
  touch-action: none !important;
}

/* Print-optimized stylesheet for tournament venue posters & scorecards */
@media print {
  header,
  nav,
  .top-bar,
  .app-stage-nav,
  .mobile-bottom-nav,
  .btn,
  .modal-close,
  #headerThemeBtn,
  #headerSoundBtn,
  #headerMoreBtn,
  .hotkey-legend,
  .quick-match-row,
  .more-grid {
    display: none !important;
  }

  body {
    background: #ffffff !important;
    color: #000000 !important;
    font-size: 10pt !important;
    margin: 0 !important;
    padding: 10px !important;
  }

  .screen {
    display: block !important;
  }

  .card, .table-container, table {
    border: 1px solid #1e293b !important;
    box-shadow: none !important;
    background: #ffffff !important;
    color: #000000 !important;
    page-break-inside: avoid;
  }

  th, td {
    border-color: #cbd5e1 !important;
    color: #000000 !important;
  }

  .badge-active, .badge-pool {
    border: 1px solid #000000 !important;
    color: #000000 !important;
    background: transparent !important;
  }
}

/* Offline mode status badge */
.badge-offline {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: 0.72rem;
  font-weight: 700;
  background: rgba(239, 68, 68, 0.15);
  color: #f87171;
  border: 1px solid rgba(239, 68, 68, 0.3);
  padding: 3px 8px;
  border-radius: 12px;
  line-height: 1;
}

/* Umpire interval timer pulse */
@keyframes intervalPulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.03); }
  100% { transform: scale(1); }
}

#intervalTimerOverlay {
  animation: intervalPulse 1.8s ease-in-out infinite;
}


/* ═══════════════════════════════════════════════════
   BASELINE UI: TYPOGRAPHY, MOTION & COMPOSITOR RULES
═══════════════════════════════════════════════════ */
h1, h2, h3, h4, h5, h6 {
  text-wrap: balance;
  font-family: var(--font-display);
  letter-spacing: -0.012em;
}

p, .lead-desc, .modal-desc, .empty-state-desc, .more-card-desc, .rule-item-desc {
  text-wrap: pretty;
}

/* Tabular numerals for stable live sports figures */
.score-digit,
.score-tag,
.stat-value,
.coin-val,
#matchDurationClock,
#intervalSecondsDisplay,
#headerCoinCount,
.table-rank,
td,
th,
.bracket-team-row span:last-child {
  font-feature-settings: "tnum";
  font-variant-numeric: tabular-nums;
}

/* Micro-interaction feedback (max 150ms, compositor only) */
.btn,
.stage-tab,
.mobile-nav-btn,
.more-card-item,
.notify-btn,
.quick-win-btn,
.quick-score-btn {
  touch-action: manipulation;
  transition: transform 120ms ease-out, opacity 120ms ease-out, background-color 140ms ease-out, border-color 140ms ease-out;
}

.btn:active,
.stage-tab:active,
.mobile-nav-btn:active,
.more-card-item:active,
.notify-btn:active,
.quick-win-btn:active,
.quick-score-btn:active {
  transform: scale(0.975);
}

/* Accessibility: Reduced motion preference */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}

/* Table row interactive feedback */
tbody tr {
  transition: background-color 100ms ease;
}
tbody tr:hover {
  background: rgba(255, 255, 255, 0.025);
}
body.theme-light tbody tr:hover {
  background: #f8fafc;
}


/* Leaderboard Filter Pills & Podium */
.leaderboard-filter-bar {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  align-items: center;
  margin-bottom: 20px;
}
.filter-pill-btn {
  background: var(--clr-surface-card);
  border: 1px solid var(--clr-border);
  color: var(--clr-text-muted);
  padding: 6px 14px;
  border-radius: 9999px;
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 140ms ease;
}
.filter-pill-btn:hover {
  color: var(--clr-text);
  border-color: var(--clr-text-muted);
}
.filter-pill-btn.active {
  background: rgba(34, 197, 94, 0.12);
  border-color: var(--clr-green);
  color: var(--clr-green);
  font-weight: 700;
}
body.theme-light .filter-pill-btn.active {
  background: #ecfdf5;
  border-color: #059669;
  color: #059669;
}

/* Podium Showcase */
.podium-grid {
  display: grid;
  grid-template-columns: 1fr 1.15fr 1fr;
  gap: 14px;
  align-items: flex-end;
  margin-bottom: 24px;
}
@media (max-width: 640px) {
  .podium-grid {
    grid-template-columns: 1fr;
  }
}
.podium-card {
  background: var(--clr-surface-card);
  border: 1px solid var(--clr-border);
  border-radius: var(--radius-md);
  padding: 16px;
  text-align: center;
  position: relative;
  transition: transform 140ms ease;
}
.podium-card:hover {
  transform: translateY(-2px);
}
.podium-gold {
  border-color: rgba(245, 158, 11, 0.5);
  background: linear-gradient(180deg, rgba(245, 158, 11, 0.08) 0%, var(--clr-surface-card) 100%);
  padding: 22px 16px;
  order: 2;
}
.podium-silver {
  border-color: rgba(148, 163, 184, 0.4);
  background: linear-gradient(180deg, rgba(148, 163, 184, 0.06) 0%, var(--clr-surface-card) 100%);
  order: 1;
}
.podium-bronze {
  border-color: rgba(217, 119, 6, 0.35);
  background: linear-gradient(180deg, rgba(217, 119, 6, 0.05) 0%, var(--clr-surface-card) 100%);
  order: 3;
}
@media (max-width: 640px) {
  .podium-gold { order: 1; }
  .podium-silver { order: 2; }
  .podium-bronze { order: 3; }
}

.podium-avatar {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  margin: 0 auto 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.35rem;
  font-weight: 900;
  color: #fff;
  box-shadow: 0 4px 12px rgba(0,0,0,0.25);
}
.podium-gold .podium-avatar {
  width: 60px;
  height: 60px;
  font-size: 1.55rem;
  border: 3px solid var(--clr-gold);
  background: linear-gradient(135deg, #f59e0b, #d97706);
}
.podium-silver .podium-avatar {
  border: 2px solid #94a3b8;
  background: linear-gradient(135deg, #94a3b8, #64748b);
}
.podium-bronze .podium-avatar {
  border: 2px solid #d97706;
  background: linear-gradient(135deg, #b45309, #78350f);
}

/* Athlete Profile Stacks */
.profile-stacks-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 220px), 1fr));
  gap: 16px;
  margin-bottom: 24px;
}
.stack-card {
  background: var(--clr-surface-card);
  border: 1px solid var(--clr-border);
  border-radius: var(--radius-sm);
  padding: 16px;
  position: relative;
  overflow: hidden;
}
.stack-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}
.stack-title {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--clr-text-muted);
}
.stack-value {
  font-family: var(--font-display);
  font-size: 2rem;
  font-weight: 800;
  line-height: 1.1;
  color: var(--clr-text);
  margin-bottom: 4px;
}
.stack-sublabel {
  font-size: 0.76rem;
  color: var(--clr-text-muted);
}
.stack-progress-bg {
  width: 100%;
  height: 6px;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 999px;
  margin-top: 10px;
  overflow: hidden;
}
body.theme-light .stack-progress-bg {
  background: #e2e8f0;
}
.stack-progress-fill {
  height: 100%;
  border-radius: 999px;
  transition: width 300ms ease;
}


/* Gold Coin & Points Badge Styling */
.gold-coin-icon {
  display: inline-block;
  vertical-align: middle;
}
body.theme-light #headerCoinBtn {
  background: #fef3c7 !important;
  border-color: #f59e0b !important;
  color: #b45309 !important;
}
body.theme-light #headerCoinBtn span {
  color: #b45309 !important;
}



/* Match Fixture Cards - Clean Modern Sports Board Styling */
.match-fixture-card {
  background: var(--clr-surface-card);
  border: 1px solid var(--clr-border);
  border-radius: var(--radius-md);
  padding: 16px 18px;
  box-shadow: var(--shadow-card);
  transition: transform 140ms ease, border-color 140ms ease, box-shadow 140ms ease;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.match-fixture-card:hover {
  border-color: rgba(255, 255, 255, 0.16);
  transform: translateY(-2px);
}
.match-fixture-card.is-live {
  border-color: rgba(16, 185, 129, 0.6) !important;
  box-shadow: 0 0 16px rgba(16, 185, 129, 0.12);
}
.match-fixture-card.is-completed {
  border-color: rgba(16, 185, 129, 0.25);
}
body.theme-light .match-fixture-card {
  background: #ffffff;
  border-color: #e2e8f0;
}
body.theme-light .match-fixture-card:hover {
  border-color: #cbd5e1;
}
body.theme-light .match-fixture-card.is-live {
  border-color: #10b981 !important;
  box-shadow: 0 4px 12px rgba(16, 185, 129, 0.15);
}
body.theme-light .match-fixture-card.is-completed {
  border-color: #cbd5e1;
}

.mfc-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.76rem;
}
.mfc-court-pill {
  display: flex;
  align-items: center;
  gap: 6px;
}
.mfc-badge-court {
  font-weight: 700;
  color: var(--clr-text-muted);
  background: rgba(255, 255, 255, 0.06);
  padding: 3px 8px;
  border-radius: 4px;
}
body.theme-light .mfc-badge-court {
  background: #f1f5f9;
  color: #475569;
}
.mfc-badge-pool {
  font-weight: 600;
  color: var(--clr-text-muted);
  font-size: 0.72rem;
}
.mfc-badge-completed {
  color: var(--clr-green);
  font-weight: 700;
  font-size: 0.72rem;
  letter-spacing: 0.03em;
  text-transform: uppercase;
  background: rgba(16, 185, 129, 0.1);
  padding: 2px 8px;
  border-radius: 12px;
  border: 1px solid rgba(16, 185, 129, 0.25);
}
body.theme-light .mfc-badge-completed {
  background: #ecfdf5;
  color: #059669;
  border-color: #a7f3d0;
}
.mfc-badge-scheduled {
  color: var(--clr-text-muted);
  font-size: 0.72rem;
  background: rgba(255, 255, 255, 0.05);
  padding: 2px 8px;
  border-radius: 12px;
}
body.theme-light .mfc-badge-scheduled {
  background: #f1f5f9;
  color: #64748b;
}

.mfc-body {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 10px 12px;
  background: rgba(0, 0, 0, 0.16);
  border-radius: var(--radius-sm);
  border: 1px solid rgba(255, 255, 255, 0.04);
}
body.theme-light .mfc-body {
  background: #f8fafc;
  border-color: #f1f5f9;
}
.mfc-competitor-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  padding: 4px 0;
  transition: opacity 140ms ease;
}
.mfc-competitor-row.is-defeated {
  opacity: 0.65;
}
.mfc-player-info {
  display: flex;
  align-items: center;
  gap: 10px;
  min-width: 0;
  flex: 1;
}
.mfc-name-group {
  min-width: 0;
  display: flex;
  flex-direction: column;
}
.mfc-name {
  font-weight: 700;
  font-size: 0.92rem;
  color: var(--clr-text);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  display: flex;
  align-items: center;
  gap: 5px;
}
.mfc-competitor-row.is-winner .mfc-name {
  color: var(--clr-green);
  font-weight: 800;
}
body.theme-light .mfc-competitor-row.is-winner .mfc-name {
  color: #059669;
}
.mfc-role {
  font-size: 0.68rem;
  color: var(--clr-text-muted);
}
.mfc-score-group {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-shrink: 0;
}
.mfc-score-pill {
  font-family: monospace;
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--clr-text-muted);
  min-width: 26px;
  text-align: center;
  white-space: nowrap;
}
.mfc-score-pill.is-set-winner {
  color: var(--clr-gold);
  font-weight: 800;
}
body.theme-light .mfc-score-pill.is-set-winner {
  color: #b45309;
}
.mfc-games-won {
  font-family: monospace;
  font-size: 1.05rem;
  font-weight: 900;
  min-width: 28px;
  height: 28px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  background: rgba(255, 255, 255, 0.06);
  color: var(--clr-text);
  border: 1px solid var(--clr-border);
}
body.theme-light .mfc-games-won {
  background: #ffffff;
  color: #0f172a;
  border-color: #cbd5e1;
}
.mfc-games-won.winner-games {
  background: rgba(16, 185, 129, 0.16);
  color: var(--clr-green);
  border-color: rgba(16, 185, 129, 0.45);
}
body.theme-light .mfc-games-won.winner-games {
  background: #ecfdf5;
  color: #059669;
  border-color: #10b981;
}

.mfc-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
  padding-top: 6px;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
}
body.theme-light .mfc-footer {
  border-top-color: #f1f5f9;
}
.mfc-winner-banner {
  font-size: 0.82rem;
  color: var(--clr-green);
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 5px;
}
body.theme-light .mfc-winner-banner {
  color: #059669;
}
.mfc-footer-actions {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-left: auto;
}
.mfc-action-main {
  flex: 1;
  justify-content: center;
  gap: 6px;
  font-weight: 600;
}
.mfc-action-predict {
  justify-content: center;
  gap: 6px;
  border-color: rgba(245, 158, 11, 0.3) !important;
  color: var(--clr-gold) !important;
  font-weight: 600;
}

/* Hope Ball & Game Ball Badges */
.badge-hope-ball {
  background: rgba(245, 158, 11, 0.16) !important;
  color: #fbbf24 !important;
  border: 1px solid rgba(245, 158, 11, 0.4) !important;
}
.badge-game-ball {
  background: rgba(239, 68, 68, 0.18) !important;
  color: #f87171 !important;
  border: 1px solid rgba(239, 68, 68, 0.45) !important;
  animation: pulse 1.2s infinite;
}

/* Data Table Typography & Comfortable Row Spacing */
.data-table th {
  padding: 10px 12px !important;
  font-size: 0.74rem !important;
  letter-spacing: 0.05em !important;
  text-transform: uppercase !important;
  font-weight: 700 !important;
  color: var(--clr-text-muted) !important;
  border-bottom: 1px solid var(--clr-border) !important;
}
.data-table td {
  padding: 11px 12px !important;
  font-size: 0.88rem !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.04) !important;
}
body.theme-light .data-table td {
  border-bottom: 1px solid #f1f5f9 !important;
}
</style>
"""
