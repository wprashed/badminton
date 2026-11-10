# Scripts module for Badminton Cup
SCRIPTS_CONTENT = r"""
<script>

/* ═══════════════════════════════════════════════════
   VECTOR SINGLE-COLOR FLAT ICONS HELPER
═══════════════════════════════════════════════════ */

/* ═══════════════════════════════════════════════════
   SYNTHETIC WEB AUDIO WHISTLE & BUZZER
═══════════════════════════════════════════════════ */
function playUmpireWhistle() {
  try {
    const ctx = new (window.AudioContext || window.webkitAudioContext)();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(2400, ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(1800, ctx.currentTime + 0.15);
    osc.frequency.exponentialRampToValueAtTime(2600, ctx.currentTime + 0.3);
    gain.gain.setValueAtTime(0.3, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.35);
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + 0.36);
  } catch (e) {}
}

function triggerLetCall() {
  showToast('LET called: Rally replayed (BWF Law 14).');
  playUmpireWhistle();
  speakUmpire('Let. Play again.');
  const ann = document.getElementById('ariaLiveAnnouncer');
  if (ann) ann.textContent = 'Let called by umpire. Point replayed.';
  const match = state.matches.find(m => m.id === state.currentMatchId);
  if (match) {
    if (!match.history) match.history = [];
    match.history.push({
      set: state.currentSetIdx + 1,
      score: match.sets[state.currentSetIdx].score.slice(),
      scorer: 'LET (Re-serve)',
      time: new Date().toLocaleTimeString()
    });
    renderMatchRallyLog(match);
  }
}


/* ═══════════════════════════════════════════════════
   QUICK SCORE & MANUAL WIN LOGIC (Foosball Simplicity)
═══════════════════════════════════════════════════ */
function openQuickScoreModal(matchId) {
  const match = state.matches.find(m => m.id === matchId);
  if (!match) return;
  document.getElementById('quickMatchId').value = match.id;
  document.getElementById('quickTeamAName').textContent = match.a;
  document.getElementById('quickTeamBName').textContent = match.b;
  document.getElementById('quickScoreLabelA').textContent = `${match.a} Points`;
  document.getElementById('quickScoreLabelB').textContent = `${match.b} Points`;
  document.getElementById('quickScoreInputA').value = state.ptsToWin || 21;
  document.getElementById('quickScoreInputB').value = Math.max(0, (state.ptsToWin || 21) - 6);
  document.getElementById('quickScoreModal').showModal();
}

function awardInstantWinner(side, specificMatchId = null) {
  const matchId = specificMatchId || document.getElementById('quickMatchId')?.value;
  const match = state.matches.find(m => m.id === matchId);
  if (!match) return;

  const pts = state.ptsToWin || 21;
  const winName = side === 'a' ? match.a : match.b;
  const runnerScore = Math.max(0, pts - 6);

  match.winner = side;
  match.sets = [
    { score: side === 'a' ? [pts, runnerScore] : [runnerScore, pts], winner: side },
    { score: side === 'a' ? [pts, runnerScore] : [runnerScore, pts], winner: side }
  ];
  match.durationSeconds = 600;

  recordMatchStats(match);
  logAdminAudit(`Quick Win recorded: ${winName} won match ${match.id} (2-0)`);
  const qModal = document.getElementById('quickScoreModal'); if (qModal && qModal.open) qModal.close();

  if (match.pool === 'KO') {
    advanceKnockoutRounds();
  }

  saveState();
  broadcastStateChange();
  renderGroups();
  renderBracket();
  renderAdminDashboard();
  renderScheduleScreen();
  showToast(`${winName} recorded as match winner (2-0)!`);
  sendAppNotification(
    '🏆 Match Winner!',
    `${winName} ` + ('has won the match (2-0)!')
  );
}

function saveQuickCustomScore() {
  const matchId = document.getElementById('quickMatchId').value;
  const match = state.matches.find(m => m.id === matchId);
  if (!match) return;

  const ptsA = parseInt(document.getElementById('quickScoreInputA').value) || 0;
  const ptsB = parseInt(document.getElementById('quickScoreInputB').value) || 0;

  if (ptsA === ptsB) {
    showToast('Scores cannot be tied. One side must win.');
    return;
  }

  const winSide = ptsA > ptsB ? 'a' : 'b';
  const winName = winSide === 'a' ? match.a : match.b;

  match.winner = winSide;
  match.sets = [
    { score: [ptsA, ptsB], winner: winSide },
    { score: winSide === 'a' ? [21, Math.max(0, ptsB - 3)] : [Math.max(0, ptsA - 3), 21], winner: winSide }
  ];
  match.durationSeconds = 720;

  recordMatchStats(match);
  logAdminAudit(`Quick custom score: ${match.a} ${ptsA} - ${ptsB} ${match.b} (Winner: ${winName})`);
  const qModal = document.getElementById('quickScoreModal'); if (qModal && qModal.open) qModal.close();

  if (match.pool === 'KO') {
    advanceKnockoutRounds();
  }

  saveState();
  broadcastStateChange();
  renderGroups();
  renderBracket();
  renderAdminDashboard();
  renderScheduleScreen();
  showToast(`Final score saved: ${winName} won!`);
}

/* ═══════════════════════════════════════════════════
   OPEN CHALLENGES FEATURE (Foosball Superpower)
═══════════════════════════════════════════════════ */
const STORAGE_KEY_CHALLENGES = 'badminton_cup_challenges_v4';

function getChallengesDB() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY_CHALLENGES)) || [];
  } catch (e) {
    return [];
  }
}

function saveChallengesDB(list) {
  localStorage.setItem(STORAGE_KEY_CHALLENGES, JSON.stringify(list));
}

function openNewChallengeModal() {
  document.getElementById('challengeCreatorName').value = currentUser ? currentUser.name : '';
  document.getElementById('newChallengeModal').showModal();
}

function postNewChallenge() {
  const name = document.getElementById('challengeCreatorName').value.trim();
  if (!name) {
    showToast('Please enter your name.');
    return;
  }
  const category = document.getElementById('challengeCategorySelect').value;
  const points = parseInt(document.getElementById('challengePointsSelect').value) || 21;
  const note = document.getElementById('challengeNoteInput').value.trim() || 'Court 1';

  const list = getChallengesDB();
  const newChal = {
    id: 'ch_' + Date.now().toString(36),
    creator: name,
    category,
    points,
    note,
    status: 'open',
    opponent: null,
    createdAt: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
  };

  list.unshift(newChal);
  saveChallengesDB(list);
  document.getElementById('newChallengeModal').close();
  renderChallengesBoard();
  showToast('Challenge opened! Waiting for a challenger.');
}

let activeChallengeFilter = 'all';

function filterChallenges(type) {
  activeChallengeFilter = type;
  ['All', 'Open', 'Accepted'].forEach(t => {
    const b = document.getElementById('chalFilter' + t);
    if (b) b.classList.toggle('active', t.toLowerCase() === type);
  });
  renderChallengesBoard();
}

function acceptChallenge(id) {
  const list = getChallengesDB();
  const chal = list.find(c => c.id === id);
  if (!chal) return;

  const joinerName = prompt('Enter your name to accept this challenge:');
  if (!joinerName || !joinerName.trim()) return;

  chal.opponent = joinerName.trim();
  chal.status = 'accepted';
  saveChallengesDB(list);

  // Automatically create match and start live umpire session!
  const newMatch = createMatchObj(chal.creator, chal.opponent, 'CHALLENGE');
  state.matches.push(newMatch);
  saveState();
  renderChallengesBoard();
  showToast(`${joinerName} accepted the challenge! Launching match...`);
  
  setTimeout(() => {
    startUmpireMatch(newMatch.id);
  }, 400);
}

function renderChallengesBoard() {
  const container = document.getElementById('challengeBoardList');
  if (!container) return;

  const list = getChallengesDB();
  document.getElementById('chalCountAll').textContent = list.length;
  document.getElementById('chalCountOpen').textContent = list.filter(c => c.status === 'open').length;
  document.getElementById('chalCountAccepted').textContent = list.filter(c => c.status === 'accepted').length;

  let filtered = list;
  if (activeChallengeFilter === 'open') filtered = list.filter(c => c.status === 'open');
  if (activeChallengeFilter === 'accepted') filtered = list.filter(c => c.status === 'accepted');

  if (!filtered.length) {
    container.innerHTML = `
      <div class="empty-state-card" style="grid-column:1/-1;">
        <div class="empty-state-icon">${svgIcon("swords", "icon-3xl")}</div>
        <div class="empty-state-title">${'No Challenges Found'}</div>
        <div class="empty-state-desc">${'Be the first to post a public badminton challenge for others to join!'}</div>
        <button class="btn btn-primary btn-sm" onclick="openNewChallengeModal()">${'+ Open a Challenge'}</button>
      </div>
    `;
    return;
  }

  container.innerHTML = filtered.map(c => `
    <div class="challenge-card ${c.status === 'open' ? 'open-status' : 'accepted-status'}">
      <div>
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
          <span class="challenge-badge ${c.status === 'open' ? 'open' : 'accepted'}">${c.status.toUpperCase()}</span>
          <span style="font-size:0.75rem;color:var(--clr-text-muted);">${c.createdAt}</span>
        </div>
        <div style="font-weight:700;font-size:1.05rem;color:var(--clr-text);margin-bottom:4px;">
          ${c.creator} ${c.opponent ? `<span style="color:var(--clr-green);">vs</span> ${c.opponent}` : ''}
        </div>
        <div style="font-size:0.8rem;color:var(--clr-text-muted);display:flex;gap:8px;margin-top:6px;">
          <span>${c.category === 'doubles' ? 'Doubles (2v2)' : 'Singles (1v1)'}</span>
          <span>·</span>
          <span>${c.points} Points</span>
          <span>·</span>
          <span>${c.note}</span>
        </div>
      </div>
      <div>
        ${c.status === 'open' ? `
          <button class="btn btn-primary btn-sm" style="width:100%;" onclick="acceptChallenge('${c.id}')">
            ${'Accept Challenge &rarr;'}
          </button>
        ` : `
          <div style="font-size:0.78rem;color:var(--clr-green);font-weight:600;text-align:center;">
            ${'Match In Progress / Accepted'}
          </div>
        `}
      </div>
    </div>
  `).join('');
}

/* ═══════════════════════════════════════════════════
   FULL DATA RESET & START OVER LOGIC
═══════════════════════════════════════════════════ */
function openDataResetModal() {
  document.getElementById('dataResetModal').showModal();
}

function resetCurrentTournamentOnly() {
  if (!confirm('Wipe all fixtures for the current tournament and start over at setup?')) return;
  state.matches = [];
  state.koRounds = [];
  state.champion = null;
  state.runnerUp = null;
  state.thirdPlace = null;
  state.currentMatchId = null;
  saveState();
  document.getElementById('dataResetModal').close();
  showScreen('setupScreen');
  showToast('Tournament matches reset to setup.');
}

function resetEverythingFullFactory() {
  if (!confirm('WARNING: Complete Factory Reset will wipe all tournaments, challenges, and stats. Are you sure?')) return;
  localStorage.clear();
  showToast('All data successfully reset!');
  setTimeout(() => {
    window.location.reload();
  }, 500);
}

window.svgIcon = function(name, cls) {
  const c = cls ? `icon ${cls}` : 'icon';
  switch (name) {
    case 'shuttle':
      return `<svg class="${c}" viewBox="0 0 24 24"><path d="M12 2l3 7h-6l3-7zM7 9l-4 8 7 5 3-4-6-9zM17 9l4 8-7 5-3-4 6-9z"/></svg>`;
    case 'trophy':
      return `<svg class="${c}" viewBox="0 0 24 24"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6M18 9h1.5a2.5 2.5 0 0 0 0-5H18M4 22h16M10 14.66V17c0 .55-.45 1-1 1H8c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1h8c.55 0 1-.45 1-1v-1c0-.55-.45-1-1-1h-1c-.55 0-1-.45-1-1v-2.34c3.38-.6 6-3.5 6-6.99V4H4v3.67c0 3.49 2.62 6.39 6 6.99z"/></svg>`;
    case 'calendar':
      return `<svg class="${c}" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>`;
    case 'scale':
      return `<svg class="${c}" viewBox="0 0 24 24"><path d="M16 16l3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1zM2 16l3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1zM7 21h10M12 3v18M3 7h18"/></svg>`;
    case 'clipboard':
      return `<svg class="${c}" viewBox="0 0 24 24"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/></svg>`;
    case 'swords':
      return `<svg class="${c}" viewBox="0 0 24 24"><line x1="6" y1="3" x2="6" y2="15"/><circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M18 9a9 9 0 0 1-9 9"/></svg>`;
    case 'check':
      return `<svg class="${c}" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>`;
    case 'x':
      return `<svg class="${c}" viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>`;
    case 'alert':
      return `<svg class="${c}" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>`;
    case 'zap':
      return `<svg class="${c}" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>`;
    case 'mail':
      return `<svg class="${c}" viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>`;
    case 'printer':
      return `<svg class="${c}" viewBox="0 0 24 24"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>`;
    case 'copy':
      return `<svg class="${c}" viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>`;
    case 'download':
      return `<svg class="${c}" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>`;
    case 'coin':
      return `<svg class="${c}" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/></svg>`;
    case 'users':
      return `<svg class="${c}" viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>`;
    case 'user':
      return `<svg class="${c}" viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>`;
    case 'dot':
      return `<span style="display:inline-block;width:6px;height:6px;border-radius:50%;background:currentColor;vertical-align:middle;"></span>`;
    default:
      return '';
  }
};
/* ═══════════════════════════════════════════════════
   STORAGE KEYS & GLOBAL CONSTANTS
═══════════════════════════════════════════════════ */
const STORAGE_KEY_STATE = 'badminton_cup_state_v4';
const STORAGE_KEY_USERS = 'badminton_cup_users_v4';
const STORAGE_KEY_STATS = 'badminton_cup_stats_v4';
const STORAGE_KEY_AUTH = 'badminton_cup_cur_user_v4';
const STORAGE_KEY_THEME = 'badminton_cup_theme_pref';
const STORAGE_KEY_BETS = 'badminton_cup_bets_v4';
const STORAGE_KEY_WALLETS = 'badminton_cup_wallets_v4';
const STORAGE_KEY_TXS = 'badminton_cup_txs_v4';
const STORAGE_KEY_SUGGESTIONS = 'badminton_cup_suggestions_v4';
const STORAGE_KEY_SETTINGS = 'badminton_cup_settings_v4';
const STORAGE_KEY_TOURNAMENTS = 'badminton_cup_tournaments_v4';

/* ═══════════════════════════════════════════════════
   GLOBAL STATE
═══════════════════════════════════════════════════ */
const state = {
  title: 'The Badminton Cup 2026',
  category: 'singles', // 'singles' or 'doubles'
  ptsToWin: 21,
  bestOf: 3,
  stageFormat: 'rr',   // 'rr' or 'ko'
  courtNumber: 2,
  selectedCourtFilter: 'all',
  audioEnabled: true,
  handicapEnabled: false,
  courtFlipped: false,
  entryFee: '$20.00',
  poolA: [],
  poolB: [],
  matches: [],
  koRounds: [],
  bronzeMatchId: null,
  currentMatchId: null,
  currentSetIdx: 0,
  servingSide: 'a',
  doublesPositions: {
    a: { right: '', left: '' },
    b: { right: '', left: '' }
  },
  undoStack: [],
  champion: null,
  runnerUp: null,
  thirdPlace: null,
  matchStartTime: null,
  stopwatchInterval: null,
  intervalTimer: null,
  endsSwitchedInDecidingSet: false,
  auditLogs: []
};

let currentUser = null;
let audioCtx = null;
let masterGainNode = null;
let activeBetMatch = null;
let activeBetSide = 'a';
let activeWalkoverType = null;
let broadcastSync = null;
let currentPickerTargetPool = 'A';
let pendingInviteUser = null;

// Settings
const appSettings = {
  masterVolume: 0.8,
  voiceURI: null,
  buzzerEnabled: true
};

try {
  const loadedSettings = JSON.parse(localStorage.getItem(STORAGE_KEY_SETTINGS));
  if (loadedSettings) Object.assign(appSettings, loadedSettings);
} catch (e) {}

function saveAppSettings() {
  try {
    localStorage.setItem(STORAGE_KEY_SETTINGS, JSON.stringify(appSettings));
  } catch (e) {}
}

/* ═══════════════════════════════════════════════════
   MULTI-TAB REAL-TIME BROADCAST SYNC (ITEM 55)
═══════════════════════════════════════════════════ */
if ('BroadcastChannel' in window) {
  try {
    broadcastSync = new BroadcastChannel('badminton_cup_live_sync');
    broadcastSync.onmessage = (e) => {
      if (e.data && e.data.type === 'STATE_UPDATED') {
        loadSavedState(false);
        refreshCurrentViews();
      }
    };
  } catch (e) {}
}

function broadcastStateChange() {
  if (broadcastSync) {
    try {
      broadcastSync.postMessage({ type: 'STATE_UPDATED', timestamp: Date.now() });
    } catch (e) {}
  }
}

/* ═══════════════════════════════════════════════════
   MULTI-TOURNAMENT SWITCHER & ISOLATION (ITEM 19)
═══════════════════════════════════════════════════ */
function getTournamentsDB() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY_TOURNAMENTS);
    if (raw) {
      const parsed = JSON.parse(raw);
      if (Array.isArray(parsed) && parsed.length > 0) return parsed;
    }
  } catch (e) {}
  return [{ id: 'main', title: state.title || 'The Badminton Cup 2026', updatedAt: Date.now() }];
}

function saveTournamentsDB(list) {
  try {
    localStorage.setItem(STORAGE_KEY_TOURNAMENTS, JSON.stringify(list));
  } catch (e) {}
}

function renderTournamentSwitcher() {
  const select = document.getElementById('tournamentSelectHeader');
  if (!select) return;
  const list = getTournamentsDB();
  const currentId = state.tournamentId || 'main';

  select.innerHTML = list.map(t =>
    `<option value="${t.id}" ${t.id === currentId ? 'selected' : ''}>${t.title}</option>`
  ).join('') + `<option value="__NEW__">+ New Tournament...</option>`;
}

function switchActiveTournament(targetId) {
  if (targetId === '__NEW__') {
    const title = prompt('Enter New Tournament Name:', 'Summer Badminton Open 2026');
    if (!title || !title.trim()) {
      renderTournamentSwitcher();
      return;
    }
    const newId = 't_' + Date.now();
    const list = getTournamentsDB();
    saveState();
    list.push({ id: newId, title: title.trim(), updatedAt: Date.now() });
    saveTournamentsDB(list);

    Object.assign(state, {
      tournamentId: newId,
      title: title.trim(),
      poolA: [],
      poolB: [],
      matches: [],
      koRounds: [],
      bronzeMatchId: null,
      currentMatchId: null,
      currentSetIdx: 0,
      servingSide: 'a',
      doublesPositions: { a: { right: '', left: '' }, b: { right: '', left: '' } },
      undoStack: [],
      champion: null,
      runnerUp: null,
      thirdPlace: null,
      matchStartTime: null,
      endsSwitchedInDecidingSet: false
    });

    saveState();
    renderTournamentSwitcher();
    refreshCurrentViews();
    showScreen('setupScreen');
    showToast(`Created and switched to ${title}!`);
    broadcastStateChange();
    return;
  }

  const currentId = state.tournamentId || 'main';
  if (currentId === targetId) return;

  // Persist current tournament state
  try {
    localStorage.setItem(STORAGE_KEY_STATE + '_' + currentId, JSON.stringify(state));
  } catch (e) {}

  // Load target tournament state
  let targetState = null;
  try {
    const raw = localStorage.getItem(STORAGE_KEY_STATE + '_' + targetId);
    if (raw) targetState = JSON.parse(raw);
  } catch (e) {}

  if (targetState) {
    Object.assign(state, targetState);
    state.tournamentId = targetId;
  } else {
    const list = getTournamentsDB();
    const meta = list.find(t => t.id === targetId);
    state.tournamentId = targetId;
    if (meta) state.title = meta.title;
    state.matches = [];
    state.poolA = [];
    state.poolB = [];
    state.koRounds = [];
    state.currentMatchId = null;
  }

  saveState();
  renderTournamentSwitcher();
  refreshCurrentViews();
  showToast(`Switched to ${state.title}`);
  broadcastStateChange();
}

/* ═══════════════════════════════════════════════════
   AUDIO & WEB SPEECH ENGINE
═══════════════════════════════════════════════════ */
function initAudioContext() {
  if (!audioCtx) {
    const AudioCtxClass = window.AudioContext || window.webkitAudioContext;
    if (AudioCtxClass) {
      audioCtx = new AudioCtxClass();
      masterGainNode = audioCtx.createGain();
      masterGainNode.gain.setValueAtTime(appSettings.masterVolume, audioCtx.currentTime);
      masterGainNode.connect(audioCtx.destination);
    }
  }
  if (audioCtx && audioCtx.state === 'suspended') {
    audioCtx.resume();
  }
}

// User first gesture audio unlock
['click', 'touchstart', 'keydown'].forEach(evt => {
  document.addEventListener(evt, () => initAudioContext(), { once: true, passive: true });
});

function playSound(type) {
  if (!state.audioEnabled) return;
  try {
    initAudioContext();
    if (!audioCtx || !masterGainNode) return;

    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.connect(gain);
    gain.connect(masterGainNode);

    const now = audioCtx.currentTime;

    if (type === 'point') {
      osc.frequency.setValueAtTime(587.33, now); // D5
      osc.frequency.exponentialRampToValueAtTime(880, now + 0.08); // A5
      gain.gain.setValueAtTime(0.3, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.14);
      osc.start(now);
      osc.stop(now + 0.14);
    } else if (type === 'buzzer') {
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(580, now);
      osc.frequency.setValueAtTime(620, now + 0.18);
      gain.gain.setValueAtTime(0.4, now);
      gain.gain.exponentialRampToValueAtTime(0.01, now + 0.55);
      osc.start(now);
      osc.stop(now + 0.55);
    } else if (type === 'win') {
      [523.25, 659.25, 783.99, 1046.50].forEach((freq, idx) => {
        const o = audioCtx.createOscillator();
        const g = audioCtx.createGain();
        o.connect(g);
        g.connect(masterGainNode);
        const t = now + idx * 0.12;
        o.frequency.setValueAtTime(freq, t);
        g.gain.setValueAtTime(0.3, t);
        g.gain.exponentialRampToValueAtTime(0.001, t + 0.35);
        o.start(t);
        o.stop(t + 0.35);
      });
    }
  } catch (e) {}
}

function updateMasterVolume(val) {
  const norm = Math.max(0, Math.min(1, val / 100));
  appSettings.masterVolume = norm;
  if (masterGainNode && audioCtx) {
    masterGainNode.gain.setValueAtTime(norm, audioCtx.currentTime);
  }
  document.getElementById('masterVolumeDisplay').textContent = `${val}%`;
  saveAppSettings();
}

function toggleBuzzerSound(enabled) {
  appSettings.buzzerEnabled = enabled;
  saveAppSettings();
}

function updateUmpireVoice(voiceURI) {
  appSettings.voiceURI = voiceURI;
  saveAppSettings();
}

function populateVoiceOptions() {
  if (!('speechSynthesis' in window)) return;
  const select = document.getElementById('umpireVoiceSelect');
  if (!select) return;

  const voices = window.speechSynthesis.getVoices();
  select.innerHTML = voices
    .filter(v => v.lang.startsWith('en'))
    .map(v => `<option value="${v.voiceURI}" ${v.voiceURI === appSettings.voiceURI ? 'selected' : ''}>${v.name} (${v.lang})</option>`)
    .join('');
}

if ('speechSynthesis' in window) {
  window.speechSynthesis.onvoiceschanged = populateVoiceOptions;
  setTimeout(populateVoiceOptions, 500);
}

function testUmpireVoice() {
  speakScoreAnnouncement("15 all. Play!");
}

function speakScoreAnnouncement(customText = null) {
  if (!state.audioEnabled || !('speechSynthesis' in window)) return;
  try {
    window.speechSynthesis.cancel();

    let textToSpeak = customText;
    if (!textToSpeak) {
      const match = state.matches.find(m => m.id === state.currentMatchId);
      if (!match) return;
      const set = match.sets[state.currentSetIdx];
      const serverScore = state.servingSide === 'a' ? set.score[0] : set.score[1];
      const receiverScore = state.servingSide === 'a' ? set.score[1] : set.score[0];

      if (serverScore === receiverScore) {
        textToSpeak = `${serverScore} all`;
      } else {
        textToSpeak = `${serverScore}, ${receiverScore}`;
      }

      const pts = state.ptsToWin;
      const leadingScore = Math.max(serverScore, receiverScore);
      const trailingScore = Math.min(serverScore, receiverScore);
      if (leadingScore >= pts - 1 && leadingScore - trailingScore >= 1) {
        const setsNeeded = Math.ceil(state.bestOf / 2);
        const leaderSide = set.score[0] > set.score[1] ? 'a' : 'b';
        const wonSoFar = getMatchSetsWon(match, leaderSide);
        if (wonSoFar + 1 >= setsNeeded) {
          textToSpeak += match.pool === 'KO' && state.koRounds.length && state.koRounds[state.koRounds.length - 1].length === 1
            ? ". Championship point"
            : ". Match point";
        } else {
          textToSpeak += ". Game point";
        }
      }
    }

    const utterance = new SpeechSynthesisUtterance(textToSpeak);
    utterance.rate = 1.05;
    utterance.pitch = 1.0;

    if (appSettings.voiceURI) {
      const voices = window.speechSynthesis.getVoices();
      const chosen = voices.find(v => v.voiceURI === appSettings.voiceURI);
      if (chosen) utterance.voice = chosen;
    }

    window.speechSynthesis.speak(utterance);
  } catch (e) {}
}

/* ═══════════════════════════════════════════════════
   PASSWORD SECURITY & AUTHENTICATION
═══════════════════════════════════════════════════ */
async function hashPassword(plainText) {
  try {
    const enc = new TextEncoder();
    const data = enc.encode(plainText + '_salt_badminton_cup_2026');
    const hashBuf = await crypto.subtle.digest('SHA-256', data);
    return Array.from(new Uint8Array(hashBuf)).map(b => b.toString(16).padStart(2, '0')).join('');
  } catch (e) {
    return 'h_' + btoa(plainText);
  }
}

function getUsersDB() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY_USERS)) || [];
  } catch (e) { return []; }
}
function saveUsersDB(users) {
  try {
    localStorage.setItem(STORAGE_KEY_USERS, JSON.stringify(users));
  } catch (e) {}
}

let authMode = 'login';


function loginAsUser(name) {
  const users = getUsersDB();
  const target = users.find(u => u.name.toLowerCase() === name.toLowerCase());
  if (target) {
    setCurrentUser(target);
    closeAuthModal();
    showToast(`Signed in as ${target.name} (${target.role.toUpperCase()})!`, 'success');
  } else {
    showToast(`User ${name} not found.`, 'warning');
  }
}

function openAuthModal() {
  if (currentUser) {
    if (confirm(`Currently signed in as ${currentUser.name} (${currentUser.role}). Sign out?`)) {
      logoutUser();
    }
    return;
  }
  switchAuthTab('login');
  document.getElementById('authModal').showModal();
}
function closeAuthModal() {
  document.getElementById('authModal').close();
}
function switchAuthTab(mode) {
  authMode = mode;
  document.getElementById('tabAuthLogin').classList.toggle('active', mode === 'login');
  document.getElementById('tabAuthRegister').classList.toggle('active', mode === 'register');
  document.getElementById('authSubmitBtn').textContent = mode === 'login' ? 'Sign In' : 'Create Account';
}

async function handleAuthSubmit(e) {
  e.preventDefault();
  const identifier = document.getElementById('authUsernameInput').value.trim();
  const pass = document.getElementById('authPasswordInput').value.trim();
  if (!identifier || !pass) return;

  const users = getUsersDB();
  const hashed = await hashPassword(pass);

  if (authMode === 'register') {
    if (users.some(u => u.name.toLowerCase() === identifier.toLowerCase() || (u.email && u.email.toLowerCase() === identifier.toLowerCase()))) {
      showToast('Name or email already registered.');
      return;
    }
    const isFirstUser = users.length === 0;
    const newUser = {
      id: Date.now(),
      name: identifier,
      email: identifier.includes('@') ? identifier.toLowerCase() : `${identifier.replace(/\s+/g, '').toLowerCase()}@badminton.local`,
      passHash: hashed,
      role: isFirstUser ? 'admin' : 'player',
      status: 'active',
      feeStatus: 'paid',
      elo: 1200,
      dominantHand: 'Right-Handed',
      club: 'Independent',
      avatar: 'U',
      createdAt: new Date().toLocaleDateString()
    };
    users.push(newUser);
    saveUsersDB(users);

    // Guest wallet transfer prompt
    const wallets = getWalletsDB();
    if (wallets['Guest'] && wallets['Guest'] > 0) {
      if (confirm(`Transfer your ${wallets['Guest'].toLocaleString()} Guest coins to your new account '${newUser.name}'?`)) {
        wallets[newUser.name] = (wallets[newUser.name] || 0) + wallets['Guest'];
        recordTransaction(newUser.name, 'guest_migration', wallets['Guest'], wallets[newUser.name], 'Transferred Guest wallet balance');
        wallets['Guest'] = 0;
        saveWalletsDB(wallets);
      }
    }

    setCurrentUser(newUser);
    showToast(`Account created! Welcome, ${newUser.name}!`);
  } else {
    // Login by Name or Email
    const user = users.find(u =>
      u.name.toLowerCase() === identifier.toLowerCase() ||
      (u.email && u.email.toLowerCase() === identifier.toLowerCase())
    );
    if (!user) {
      showToast('User not found.');
      return;
    }
    const isValid = user.passHash ? (user.passHash === hashed) : (user.pass === pass);
    if (!isValid) {
      showToast('Invalid passcode.');
      return;
    }
    if (!user.passHash) {
      user.passHash = hashed;
      delete user.pass;
      saveUsersDB(users);
    }
    setCurrentUser(user);
    showToast(`Welcome back, ${user.name}!`);
  }

  closeAuthModal();
}

function setCurrentUser(user) {
  currentUser = user;
  try {
    localStorage.setItem(STORAGE_KEY_AUTH, JSON.stringify(user));
  } catch (e) {}
  updateUserUI();
  updateBettingUI();
  updateBettingUI();
  renderPlayerHub();
}


function ensureDemoUsersSeeded() {
  const users = getUsersDB();
  const demoList = [
    { name: 'Rashed', email: 'rashed@badminton.local', role: 'admin', club: 'Tournament Director', elo: 1650, avatar: 'R' },
    { name: 'Parag Das', email: 'parag@badminton.local', role: 'player', club: 'Dhaka Smashers', elo: 1610, avatar: 'P' },
    { name: 'Rifat Haque', email: 'rifat.haque@badminton.local', role: 'player', club: 'Uttara Shuttlers', elo: 1590, avatar: 'R' },
    { name: 'Rifat Tariq', email: 'rifat.tariq@badminton.local', role: 'player', club: 'Banani BC', elo: 1580, avatar: 'R' },
    { name: 'Jobayer', email: 'jobayer@badminton.local', role: 'player', club: 'Gulshan Aces', elo: 1570, avatar: 'J' },
    { name: 'Shewa', email: 'shewa@badminton.local', role: 'player', club: 'Mirpur Warriors', elo: 1560, avatar: 'S' },
    { name: 'Sazedul', email: 'sazedul@badminton.local', role: 'player', club: 'Dhanmondi Club', elo: 1550, avatar: 'S' },
    { name: 'Nur', email: 'nur@badminton.local', role: 'player', club: 'Mohakhali Spikers', elo: 1540, avatar: 'N' },
    { name: 'Ofi', email: 'ofi@badminton.local', role: 'player', club: 'Bashundhara BC', elo: 1530, avatar: 'O' },
    { name: 'Sifat', email: 'sifat@badminton.local', role: 'player', club: 'Foosball & Shuttlers', elo: 1620, avatar: 'S' },
    { name: 'Sajeeb', email: 'sajeeb@badminton.local', role: 'player', club: 'Paltan Smashers', elo: 1520, avatar: 'S' },
    { name: 'Jakir', email: 'jakir@badminton.local', role: 'player', club: 'Rampura Rackets', elo: 1510, avatar: 'J' },
    { name: 'Saiful', email: 'saiful@badminton.local', role: 'player', club: 'Khilgaon Shuttlers', elo: 1500, avatar: 'S' },
    { name: 'Al Emran', email: 'emran@badminton.local', role: 'player', club: 'Chittagong Aces', elo: 1580, avatar: 'A' },
    { name: 'Toufiq', email: 'toufiq@badminton.local', role: 'player', club: 'Sylhet Smashers', elo: 1540, avatar: 'T' },
    { name: 'Abir', email: 'abir@badminton.local', role: 'player', club: 'Rajshahi Smashers', elo: 1560, avatar: 'A' }
  ];

  let added = false;
  demoList.forEach((d, idx) => {
    let existing = users.find(u => u.name.toLowerCase() === d.name.toLowerCase());
    if (!existing) {
      users.push({
        id: 3000 + idx,
        name: d.name,
        email: d.email,
        role: d.role,
        status: 'active',
        feeStatus: 'paid',
        elo: d.elo,
        dominantHand: 'Right-Handed',
        club: d.club,
        avatar: d.avatar,
        createdAt: new Date().toLocaleDateString()
      });
      added = true;
    } else {
      if (d.name === 'Rashed' && existing.role !== 'admin') {
        existing.role = 'admin';
        added = true;
      }
    }
  });

  if (added) {
    saveUsersDB(users);
  }

  // Pre-seed sample open challenges if empty
  const chalList = getChallengesDB();
  if (!chalList.length) {
    chalList.push({
      id: 'chal_seed_1',
      creator: 'Parag Das',
      opponent: null,
      category: 'singles',
      points: 21,
      note: 'Court 1 · Friendly Singles Match',
      status: 'open',
      createdAt: 'Today'
    });
    chalList.push({
      id: 'chal_seed_2',
      creator: 'Sifat',
      opponent: null,
      category: 'singles',
      points: 21,
      note: 'Court 2 · Ready for high-paced match!',
      status: 'open',
      createdAt: 'Today'
    });
    saveChallengesDB(chalList);
  }

  // If no currentUser is saved, default to Rashed as Admin
  if (!currentUser) {
    const rashed = users.find(u => u.name.toLowerCase() === 'rashed');
    if (rashed) {
      setCurrentUser(rashed);
    }
  }
}

function loadAuthUser() {
  try {
    const saved = JSON.parse(localStorage.getItem(STORAGE_KEY_AUTH));
    if (saved) {
      const users = getUsersDB();
      const verified = users.find(u => u.id === saved.id || (u.email && u.email === saved.email));
      if (verified) currentUser = verified;
    }
  } catch (e) {}
  updateUserUI();
  updateBettingUI();
  renderPlayerHub();
}

function logoutUser() {
  currentUser = null;
  localStorage.removeItem(STORAGE_KEY_AUTH);
  updateUserUI();
  updateBettingUI();
  updateBettingUI();
  showToast('Logged out.');
}

function updateUserUI() {
  const nameLabel = document.getElementById('headerUsername');
  const roleBadge = document.getElementById('headerUserRole');
  const avatar = document.getElementById('headerAvatar');
  const authBtn = document.getElementById('authBtn');
  const navHub = document.getElementById('navPlayerHubBtn');
  const tabHub = document.getElementById('tabNavPlayerHub');

  if (currentUser) {
    nameLabel.textContent = currentUser.name;
    avatar.textContent = currentUser.avatar || currentUser.name.charAt(0).toUpperCase();
    avatar.style.background = (currentUser.role === 'admin' || currentUser.role === 'super_admin') ? 'var(--clr-gold)' : 'var(--clr-green)';
    roleBadge.style.display = 'inline-block';
    roleBadge.textContent = currentUser.role.toUpperCase();
    authBtn.textContent = 'Sign Out';
    if (navHub) navHub.style.display = 'inline-flex';
    if (tabHub) tabHub.style.display = 'inline-flex';
  } else {
    nameLabel.textContent = 'Guest Player';
    avatar.textContent = '?';
    avatar.style.background = 'var(--clr-green)';
    roleBadge.style.display = 'none';
    authBtn.textContent = 'Sign In';
    if (navHub) navHub.style.display = 'none';
    if (tabHub) tabHub.style.display = 'none';
  }
}

// RBAC Guard for Admin Dashboard (Item 36)
function openAdminDashboardWithGuard() {
  if (!currentUser) {
    showToast('Please sign in with an Admin account.');
    openAuthModal();
    return;
  }
  if (currentUser.role !== 'admin' && currentUser.role !== 'super_admin') {
    showToast('Access Denied: Only Tournament Directors have admin privileges.');
    return;
  }
  renderAdminDashboard();
  showScreen('adminDashboardScreen');
}

/* ═══════════════════════════════════════════════════
   ADMIN INVITATION & USER MANAGEMENT ENGINE (ITEMS 1–10)
═══════════════════════════════════════════════════ */
function openInviteUserModal() {
  document.getElementById('inviteFullNameInput').value = '';
  document.getElementById('inviteEmailInput').value = '';
  document.getElementById('inviteClubInput').value = '';
  document.getElementById('inviteUserModal').showModal();
}

function handleInviteUserSubmit(e) {
  e.preventDefault();
  const name = document.getElementById('inviteFullNameInput').value.trim();
  const email = document.getElementById('inviteEmailInput').value.trim().toLowerCase();
  const role = document.getElementById('inviteRoleSelect').value;
  const club = document.getElementById('inviteClubInput').value.trim() || 'Club Athlete';
  const elo = parseInt(document.getElementById('inviteEloInput').value) || 1200;
  const feeStatus = document.getElementById('inviteFeeStatusSelect').value;

  if (!name || !email) return;

  const users = getUsersDB();
  if (users.some(u => u.email && u.email.toLowerCase() === email)) {
    showToast('A user with this email address is already in the directory.');
    return;
  }

  // Generate secure token (Item 2)
  const token = 'tok_' + Date.now() + '_' + Math.random().toString(36).substr(2, 6);
  const newUser = {
    id: Date.now(),
    name,
    email,
    role,
    status: 'invited', // 'invited' | 'active' | 'suspended' | 'declined'
    inviteToken: token,
    expiresAt: Date.now() + 7 * 24 * 60 * 60 * 1000,
    feeStatus,
    elo,
    dominantHand: 'Right-Handed',
    club,
    avatar: 'U',
    invitedBy: currentUser ? currentUser.name : 'Tournament Director',
    createdAt: new Date().toLocaleDateString()
  };

  users.push(newUser);
  saveUsersDB(users);
  logAdminAudit(`Dispatched invitation to ${name} (${email}) as ${role.toUpperCase()}`);

  document.getElementById('inviteUserModal').close();

  // Generate magic link & mailto (Item 3)
  const origin = window.location.origin + window.location.pathname;
  const magicLink = `${origin}?invite=${token}`;
  document.getElementById('magicInviteLinkDisplay').textContent = magicLink;

  const subject = encodeURIComponent(`Official Tournament Invitation: ${state.title}`);
  const bodyText = `Hi ${name},\n\nYou have been invited to participate in ${state.title} as an official ${role.toUpperCase()}.\n\nClick the link below to accept your invitation, confirm your registration, and choose your account passcode:\n\n${magicLink}\n\nTournament Venue: Centre Court Arena\nStatus: Verified BWF SaaS Registry\n\nSee you on court!`;
  
  document.getElementById('mailtoInviteBtn').href = `mailto:${email}?subject=${subject}&body=${encodeURIComponent(bodyText)}`;
  document.getElementById('simulatedEmailSubject').textContent = `Subject: Official Tournament Invitation: ${state.title}`;
  document.getElementById('simulatedEmailBody').textContent = `To: ${email}\nFrom: director@badmintoncup.org\n\n${bodyText}`;

  document.getElementById('inviteSuccessModal').showModal();
  renderAdminDashboard();
  showToast(`Invitation created for ${name}!`);
}

function copyMagicInviteLink() {
  const link = document.getElementById('magicInviteLinkDisplay').textContent;
  if (navigator.clipboard) {
    navigator.clipboard.writeText(link).then(() => {
      showToast('Magic invitation link copied to clipboard!');
    });
  } else {
    showToast('Copied link.');
  }
}

function resendInvitationEmail(userId) {
  const users = getUsersDB();
  const user = users.find(u => u.id === userId);
  if (!user) return;

  user.expiresAt = Date.now() + 7 * 24 * 60 * 60 * 1000;
  if (!user.inviteToken) {
    user.inviteToken = 'tok_' + Date.now() + '_' + Math.random().toString(36).substr(2, 6);
  }
  saveUsersDB(users);

  const origin = window.location.origin + window.location.pathname;
  const magicLink = `${origin}?invite=${user.inviteToken}`;
  document.getElementById('magicInviteLinkDisplay').textContent = magicLink;

  const subject = encodeURIComponent(`Reminder: Tournament Invitation for ${state.title}`);
  const bodyText = `Hi ${user.name},\n\nThis is a reminder to accept your invitation for ${state.title}.\n\nJoin here: ${magicLink}`;
  document.getElementById('mailtoInviteBtn').href = `mailto:${user.email}?subject=${subject}&body=${encodeURIComponent(bodyText)}`;
  document.getElementById('simulatedEmailSubject').textContent = `Reminder: Invitation for ${state.title}`;
  document.getElementById('simulatedEmailBody').textContent = `To: ${user.email}\n\n${bodyText}`;

  document.getElementById('inviteSuccessModal').showModal();
  logAdminAudit(`Resent invitation link to ${user.name}`);
  showToast(`Resending invite to ${user.email}...`);
}

function revokeInvitation(userId) {
  const users = getUsersDB();
  const user = users.find(u => u.id === userId);
  if (!user) return;
  if (confirm(`Revoke invitation for ${user.name}? They will not be able to join.`)) {
    saveUsersDB(users.filter(u => u.id !== userId));
    logAdminAudit(`Revoked invitation for ${user.name} (${user.email})`);
    renderAdminDashboard();
    showToast(`Invitation for ${user.name} revoked.`);
  }
}

function deleteUserRecord(userId) {
  const users = getUsersDB();
  const user = users.find(u => u.id === userId);
  if (!user) return;
  if (confirm(`Delete user ${user.name} completely from tournament registry?`)) {
    saveUsersDB(users.filter(u => u.id !== userId));
    logAdminAudit(`Deleted user record for ${user.name}`);
    renderAdminDashboard();
    showToast('User record deleted.');
  }
}

function toggleUserFeePayment(userId) {
  const users = getUsersDB();
  const user = users.find(u => u.id === userId);
  if (user) {
    user.feeStatus = (user.feeStatus === 'paid') ? 'unpaid' : 'paid';
    saveUsersDB(users);
    logAdminAudit(`Updated registration fee payment status for ${user.name} to ${user.feeStatus.toUpperCase()}`);
    renderAdminDashboard();
    showToast(`${user.name} fee status updated.`);
  }
}

// Bulk CSV User Invitation (Item 6)
function openBulkInviteModal() {
  document.getElementById('bulkInviteModal').showModal();
}

function processBulkInviteCsv() {
  const raw = document.getElementById('bulkInviteCsvTextarea').value;
  const lines = raw.split('\n').map(l => l.trim()).filter(l => l.length > 0);
  if (!lines.length) {
    showToast('Please paste CSV lines.');
    return;
  }

  const users = getUsersDB();
  let added = 0;

  lines.forEach(line => {
    const parts = line.split(',').map(p => p.trim());
    if (parts.length >= 2) {
      const name = parts[0];
      const email = parts[1].toLowerCase();
      const role = parts[2] ? parts[2].toLowerCase() : 'player';
      const club = parts[3] || 'Club Athlete';

      if (!users.some(u => u.email && u.email.toLowerCase() === email)) {
        users.push({
          id: Date.now() + Math.floor(Math.random() * 1000),
          name,
          email,
          role: ['admin', 'umpire', 'player'].includes(role) ? role : 'player',
          status: 'invited',
          inviteToken: 'tok_' + Date.now() + '_' + Math.random().toString(36).substr(2, 6),
          expiresAt: Date.now() + 7 * 24 * 60 * 60 * 1000,
          feeStatus: 'unpaid',
          elo: 1200,
          dominantHand: 'Right-Handed',
          club,
          avatar: 'U',
          invitedBy: currentUser ? currentUser.name : 'Director',
          createdAt: new Date().toLocaleDateString()
        });
        added++;
      }
    }
  });

  saveUsersDB(users);
  logAdminAudit(`Processed batch CSV: invited ${added} users.`);
  document.getElementById('bulkInviteModal').close();
  renderAdminDashboard();
  showToast(`Batch dispatched: ${added} invitations created!`);
}

// Check URL for ?invite=token Onboarding (Item 4)
function checkUrlInvitationToken() {
  const params = new URLSearchParams(window.location.search);
  const token = params.get('invite');
  if (!token) return;

  const users = getUsersDB();
  const user = users.find(u => u.inviteToken === token);
  if (!user) {
    showToast('Invitation link is expired or invalid.');
    return;
  }

  if (user.status === 'declined') {
    showToast('This invitation was previously declined. Contact the tournament director for a new invite.');
    return;
  }

  if (user.expiresAt && Date.now() > user.expiresAt) {
    showToast('This invitation link has expired.');
    return;
  }

  if (user.status === 'active') {
    showToast(`Account for ${user.name} is already active. Please sign in.`);
    openAuthModal();
    return;
  }

  pendingInviteUser = user;
  document.getElementById('acceptAthleteName').value = user.name;
  document.getElementById('acceptAthleteEmail').value = user.email;
  document.getElementById('acceptInviteSubtitle').textContent =
    `You are invited by ${user.invitedBy || 'Tournament Director'} to compete in ${state.title}!`;
  document.getElementById('acceptInviteModal').showModal();
}

function handleDeclineInvite() {
  if (pendingInviteUser) {
    const users = getUsersDB();
    const user = users.find(u => u.id === pendingInviteUser.id);
    if (user) {
      user.status = 'declined';
      saveUsersDB(users);
      logAdminAudit(`User ${user.name} (${user.email}) declined tournament invitation.`);
    }
  }
  document.getElementById('acceptInviteModal').close();
  showToast('Invitation declined.');
}

async function handleAcceptInviteSubmit(e) {
  e.preventDefault();
  if (!pendingInviteUser) return;

  const pass = document.getElementById('acceptPasswordInput').value.trim();
  const hand = document.getElementById('acceptHandSelect').value;
  const avatar = document.getElementById('acceptAvatarSelect').value;

  if (!pass) return;

  const users = getUsersDB();
  const user = users.find(u => u.id === pendingInviteUser.id);
  if (!user) return;

  user.passHash = await hashPassword(pass);
  user.dominantHand = hand;
  user.avatar = avatar;
  user.status = 'active'; // Account activated!
  saveUsersDB(users);

  setCurrentUser(user);
  document.getElementById('acceptInviteModal').close();
  showScreen('playerHubScreen');
  playSound('win');
  showToast(`Welcome to the tournament, ${user.name}! Profile activated.`);
}

/* ═══════════════════════════════════════════════════
   REGISTERED PLAYER PICKER MODAL (ITEM 11)
═══════════════════════════════════════════════════ */
let selectedPickerIds = new Set();

function openPlayerPickerModal(targetPool = 'A') {
  currentPickerTargetPool = targetPool;
  selectedPickerIds.clear();
  const doublesHint = state.category === 'doubles' ? ' (Doubles: Auto-paired as Player 1 / Player 2)' : '';
  document.getElementById('pickerTargetPoolLabel').textContent = `Pool ${targetPool}${doublesHint}`;
  document.getElementById('playerPickerSearch').value = '';
  renderPlayerPickerItems('');
  document.getElementById('playerPickerModal').showModal();
}

function filterPlayerPickerList(query) {
  renderPlayerPickerItems(query.toLowerCase());
}

function renderPlayerPickerItems(filter) {
  const container = document.getElementById('playerPickerListContainer');
  const users = getUsersDB().filter(u => u.role === 'player' || u.role === 'admin');

  const filtered = users.filter(u =>
    u.name.toLowerCase().includes(filter) ||
    (u.email && u.email.toLowerCase().includes(filter)) ||
    (u.club && u.club.toLowerCase().includes(filter))
  );

  if (!filtered.length) {
    container.innerHTML = `<div style="text-align:center;padding:20px;color:var(--clr-text-muted);">No athletes match search.</div>`;
    return;
  }

  container.innerHTML = filtered.map(u => {
    const isSelected = selectedPickerIds.has(u.name);
    return `
      <div class="player-picker-item ${isSelected ? 'selected' : ''}" onclick="togglePickerSelection('${u.name.replace(/'/g, "\\'")}')">
        <div style="display:flex;align-items:center;gap:10px;">
          <div class="user-avatar" style="width:28px;height:28px;">${u.avatar || u.name.charAt(0)}</div>
          <div>
            <div style="font-weight:bold;font-size:0.9rem;">${u.name}</div>
            <div style="font-size:0.75rem;color:var(--clr-text-muted);">${u.club || 'Independent'} · Elo ${u.elo || 1200}</div>
          </div>
        </div>
        <div style="display:flex;align-items:center;gap:8px;">
          <span class="user-role-badge ${u.status === 'active' ? 'badge-active' : 'badge-invited'}">${u.status}</span>
          <span style="display:inline-flex;align-items:center;justify-content:center;width:18px;height:18px;border-radius:4px;border:1px solid var(--clr-border);background:${isSelected ? 'var(--clr-green)' : 'transparent'};color:#fff;">${isSelected ? svgIcon('check', 'icon-xs') : ''}</span>
        </div>
      </div>
    `;
  }).join('');

  document.getElementById('pickerSelectedCount').textContent = `${selectedPickerIds.size} athletes selected`;
}

function togglePickerSelection(name) {
  if (selectedPickerIds.has(name)) {
    selectedPickerIds.delete(name);
  } else {
    selectedPickerIds.add(name);
  }
  const q = document.getElementById('playerPickerSearch').value.toLowerCase();
  renderPlayerPickerItems(q);
}

function confirmPlayerPickerSelection() {
  if (!selectedPickerIds.size) {
    showToast('Please select at least 1 athlete.');
    return;
  }

  const targetTextarea = document.getElementById(currentPickerTargetPool === 'A' ? 'rosterAInput' : 'rosterBInput');
  const existing = targetTextarea.value.split('\n').map(s => s.trim()).filter(s => s.length > 0);
  const selectedArr = Array.from(selectedPickerIds);

  if (state.category === 'doubles') {
    for (let i = 0; i < selectedArr.length; i += 2) {
      if (i + 1 < selectedArr.length) {
        const pair = `${selectedArr[i]} / ${selectedArr[i + 1]}`;
        if (!existing.includes(pair)) existing.push(pair);
      } else {
        if (!existing.includes(selectedArr[i])) existing.push(selectedArr[i]);
      }
    }
  } else {
    selectedArr.forEach(name => {
      if (!existing.includes(name)) existing.push(name);
    });
  }

  targetTextarea.value = existing.join('\n');
  updatePlayerCounts();
  document.getElementById('playerPickerModal').close();
  showToast(`Added ${selectedPickerIds.size} registered athletes to Pool ${currentPickerTargetPool}!`);
}

/* ═══════════════════════════════════════════════════
   PERSONALIZED PLAYER HUB (ITEM 13)
═══════════════════════════════════════════════════ */

function openProfileSettingsModal() {
  if (!currentUser) return;
  const newHand = prompt('Dominant Hand (Right-Handed / Left-Handed):', currentUser.dominantHand || 'Right-Handed');
  if (newHand) {
    currentUser.dominantHand = newHand;
    const users = getUsersDB();
    const u = users.find(x => x.id === currentUser.id);
    if (u) {
      u.dominantHand = newHand;
      saveUsersDB(users);
    }
    renderPlayerHub();
    showToast('Profile updated!');
  }
}

function renderPlayerHub() {
  if (!currentUser) return;

  const titleSub = document.getElementById('playerHubSubtitle');
  if (titleSub) titleSub.textContent = `${currentUser.name} (${currentUser.club || 'Club Athlete'}) · BWF SaaS Registered`;

  const eloEl = document.getElementById('playerHubElo');
  if (eloEl) eloEl.textContent = currentUser.elo || 1200;

  // Career match metrics for this player
  const myMatches = state.matches.filter(m => m.winner && (m.a === currentUser.name || m.b === currentUser.name));
  const wonCount = myMatches.filter(m => (m.winner === 'a' && m.a === currentUser.name) || (m.winner === 'b' && m.b === currentUser.name)).length;
  const lostCount = myMatches.length - wonCount;
  const rate = myMatches.length > 0 ? Math.round((wonCount / myMatches.length) * 100) : 0;

  const winRateEl = document.getElementById('playerHubWinRate');
  if (winRateEl) winRateEl.textContent = `${rate}%`;
  const mCountEl = document.getElementById('playerHubMatchesCount');
  if (mCountEl) mCountEl.textContent = `${myMatches.length} matches (${wonCount}W - ${lostCount}L)`;

  // Form guide (last 5)
  const formGuideEl = document.getElementById('playerHubFormGuide');
  if (formGuideEl) {
    if (!myMatches.length) {
      formGuideEl.textContent = '—';
    } else {
      formGuideEl.innerHTML = myMatches.slice(-5).map(m => {
        const isWin = (m.winner === 'a' && m.a === currentUser.name) || (m.winner === 'b' && m.b === currentUser.name);
        return `<span style="color:${isWin ? 'var(--clr-green)' : 'var(--clr-red)'};margin:0 2px;">${isWin ? 'W' : 'L'}</span>`;
      }).join(' ');
    }
  }

  // Next scheduled match
  const nextMatch = state.matches.find(m => !m.winner && (m.a === currentUser.name || m.b === currentUser.name));
  const nextCard = document.getElementById('playerNextFixtureCard');
  if (nextCard) {
    if (nextMatch) {
      const opp = (nextMatch.a === currentUser.name) ? nextMatch.b : nextMatch.a;
      nextCard.innerHTML = `
        <div style="font-size:0.75rem;font-weight:900;color:var(--clr-gold);letter-spacing:0.1em;text-transform:uppercase;margin-bottom:6px;">Your Next Scheduled Fixture</div>
        <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;">
          <div>
            <div style="font-size:1.3rem;font-weight:900;">${currentUser.name} <span style="font-size:0.9rem;color:var(--clr-text-muted);">vs</span> ${opp}</div>
            <div style="font-size:0.85rem;color:var(--clr-text-muted);">Stage: Pool ${nextMatch.pool} · Assigned to <strong>Court ${nextMatch.court || 1}</strong></div>
          </div>
          <div>
            <button class="btn btn-primary" onclick="startUmpireMatch('${nextMatch.id}')">Start Match Live &rarr;</button>
          </div>
        </div>
      `;
    } else {
      nextCard.innerHTML = `
        <div style="text-align:center;padding:10px;color:var(--clr-text-muted);">
          No upcoming scheduled fixtures for ${currentUser.name} right now. Check back when the next round is seeded.
        </div>
      `;
    }
  }

  // Match History Table
  const tbody = document.getElementById('playerHubMatchesTableBody');
  if (tbody) {
    if (!myMatches.length) {
      tbody.innerHTML = `<tr><td colspan="5" style="text-align:center;padding:16px;color:var(--clr-text-muted);">No completed matches yet.</td></tr>`;
    } else {
      tbody.innerHTML = myMatches.reverse().map(m => {
        const isWin = (m.winner === 'a' && m.a === currentUser.name) || (m.winner === 'b' && m.b === currentUser.name);
        const opp = (m.a === currentUser.name) ? m.b : m.a;
        const scoreStr = m.sets.map(s => `${s.score[0]}-${s.score[1]}`).join(' | ');
        return `
          <tr>
            <td>Pool ${m.pool}</td>
            <td><strong>${opp}</strong></td>
            <td><span style="font-family:monospace;color:var(--clr-gold);">${scoreStr}</span></td>
            <td><span style="font-weight:bold;color:${isWin ? 'var(--clr-green)' : 'var(--clr-red)'};">${isWin ? 'VICTORY' : 'DEFEAT'}</span></td>
            <td>Court ${m.court || 1}</td>
          </tr>
        `;
      }).join('');
    }
  }
}

/* ═══════════════════════════════════════════════════
   STADIUM ARENA MULTI-COURT TV (ITEM 28)
═══════════════════════════════════════════════════ */
function renderStadiumScreen() {
  const container = document.getElementById('stadiumCourtsContainer');
  if (!container) return;

  const totalCourts = state.courtNumber || 2;
  let html = '';

  for (let c = 1; c <= totalCourts; c++) {
    // Find active match on this court
    const liveMatch = state.matches.find(m => m.court === c && !m.winner && (m.id === state.currentMatchId || m.status === 'in_progress' || (m.sets[0] && (m.sets[0].score[0] > 0 || m.sets[0].score[1] > 0))));
    const nextMatch = state.matches.find(m => m.court === c && !m.winner && m.id !== (liveMatch ? liveMatch.id : null));

    if (liveMatch) {
      const curSet = liveMatch.sets[liveMatch.sets.length - 1];
      const isServingA = state.currentMatchId === liveMatch.id ? (state.servingSide === 'a') : true;
      html += `
        <div class="stadium-court-card live-court">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
            <span style="font-family:'Anton',sans-serif;font-size:1.3rem;color:var(--clr-gold);">COURT ${c}</span>
            <span class="status-badge-live badge-game-point">${svgIcon("dot")} IN PLAY</span>
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;text-align:center;margin-bottom:14px;">
            <div style="background:rgba(59,130,246,0.15);padding:14px;border-radius:var(--radius-sm);border:${isServingA ? '2px solid #3b82f6' : '1px solid transparent'};">
              <div style="font-size:0.9rem;font-weight:800;color:#93c5fd;">${liveMatch.a}</div>
              <div style="font-family:'Anton',sans-serif;font-size:3.5rem;color:#fff;">${curSet.score[0]}</div>
              ${isServingA ? '<div style="font-size:0.7rem;color:#93c5fd;font-weight:bold;">● SERVING</div>' : ''}
            </div>
            <div style="background:rgba(239,68,68,0.15);padding:14px;border-radius:var(--radius-sm);border:${!isServingA ? '2px solid #ef4444' : '1px solid transparent'};">
              <div style="font-size:0.9rem;font-weight:800;color:#fca5a5;">${liveMatch.b}</div>
              <div style="font-family:'Anton',sans-serif;font-size:3.5rem;color:#fff;">${curSet.score[1]}</div>
              ${!isServingA ? '<div style="font-size:0.7rem;color:#fca5a5;font-weight:bold;">● SERVING</div>' : ''}
            </div>
          </div>
          <div style="display:flex;justify-content:space-between;align-items:center;font-size:0.8rem;color:var(--clr-text-muted);">
            <span>Stage: Pool ${liveMatch.pool}</span>
            <span>Set ${liveMatch.sets.length} of ${state.bestOf}</span>
          </div>
        </div>
      `;
    } else if (nextMatch) {
      html += `
        <div class="stadium-court-card">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
            <span style="font-family:'Anton',sans-serif;font-size:1.3rem;color:var(--clr-text-muted);">COURT ${c}</span>
            <span style="font-size:0.75rem;color:var(--clr-text-muted);font-weight:bold;">NEXT UP</span>
          </div>
          <div style="padding:24px 10px;text-align:center;">
            <div style="font-size:1.15rem;font-weight:900;margin-bottom:6px;">${nextMatch.a} <span style="color:var(--clr-text-muted);font-size:0.8rem;">vs</span> ${nextMatch.b}</div>
            <div style="font-size:0.8rem;color:var(--clr-text-muted);margin-bottom:14px;">Pool ${nextMatch.pool} Scheduled Fixture</div>
            <button class="btn btn-primary btn-sm" onclick="startUmpireMatch('${nextMatch.id}')">Call to Court &rarr;</button>
          </div>
        </div>
      `;
    } else {
      html += `
        <div class="stadium-court-card" style="opacity:0.7;text-align:center;padding:40px 20px;">
          <div style="font-family:'Anton',sans-serif;font-size:1.3rem;color:var(--clr-text-muted);margin-bottom:8px;">COURT ${c}</div>
          <div style="color:var(--clr-green);font-weight:600;font-size:0.85rem;display:flex;align-items:center;gap:4px;">${svgIcon("check", "icon-xs")} Court Available</div>
          <div style="font-size:0.8rem;color:var(--clr-text-muted);margin-top:4px;">No fixtures currently waiting</div>
        </div>
      `;
    }
  }

  container.innerHTML = html;
}

/* ═══════════════════════════════════════════════════
   ADMIN COURT QUEUE & DISPATCHER (ITEM 21)
═══════════════════════════════════════════════════ */
function renderAdminCourtQueue() {
  const container = document.getElementById('adminCourtQueueGrid');
  if (!container) return;

  const totalCourts = state.courtNumber || 2;
  let html = '';

  for (let c = 1; c <= totalCourts; c++) {
    const live = state.matches.find(m => m.court === c && !m.winner && (m.sets[0].score[0] > 0 || m.sets[0].score[1] > 0));
    const next = state.matches.find(m => m.court === c && !m.winner && m.sets[0].score[0] === 0 && m.sets[0].score[1] === 0);

    html += `
      <div style="background:rgba(0,0,0,0.25);border:1px solid var(--clr-border);border-radius:var(--radius-sm);padding:14px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
          <strong style="color:var(--clr-gold);">Court ${c}</strong>
          ${live ? '<span class="status-badge-live badge-game-point">IN PLAY</span>' : '<span style="color:var(--clr-green);font-weight:bold;font-size:0.75rem;">FREE</span>'}
        </div>
        ${live ? `
          <div style="font-size:0.85rem;font-weight:bold;margin-bottom:4px;">${live.a} vs ${live.b}</div>
          <div style="font-size:0.75rem;color:var(--clr-text-muted);">Set ${live.sets.length}: ${live.sets[live.sets.length - 1].score[0]}-${live.sets[live.sets.length - 1].score[1]}</div>
        ` : (next ? `
          <div style="font-size:0.85rem;font-weight:bold;margin-bottom:6px;">Next: ${next.a} vs ${next.b}</div>
          <button class="btn btn-ghost btn-xs" onclick="dispatchCourtAudioAnnouncement(${c}, '${next.a.replace(/'/g, "\\'")}', '${next.b.replace(/'/g, "\\'")}')">Announce Call</button>
        ` : '<div style="font-size:0.78rem;color:var(--clr-text-muted);">No waiting matches</div>')}
      </div>
    `;
  }

  container.innerHTML = html;
}

function dispatchCourtAudioAnnouncement(courtNum, playerA, playerB) {
  speakScoreAnnouncement(`Attention please. Match on Court ${courtNum}: ${playerA} versus ${playerB}. Please report to court immediately.`);
  showToast(`Announced: ${playerA} vs ${playerB} on Court ${courtNum}`);
}

/* ═══════════════════════════════════════════════════
   OFFICIAL BWF PRINTABLE SCORECARD (ITEM 23)
═══════════════════════════════════════════════════ */
function openScorecardModal() {
  const match = state.matches.find(m => m.id === state.currentMatchId) || state.matches[0];
  if (!match) {
    showToast('No active match available for scorecard.');
    return;
  }

  const container = document.getElementById('scorecardPrintContainer');
  const dur = match.durationSeconds ? `${Math.floor(match.durationSeconds / 60)}m ${match.durationSeconds % 60}s` : '—';
  const cardsList = (match.cards && match.cards.length) 
    ? match.cards.map(c => `[${c.type.toUpperCase()}] ${c.player} (Game ${c.set}, ${c.time})`).join(' · ')
    : 'None recorded (Clean conduct)';
  
  container.innerHTML = `
    <div style="text-align:center;border-bottom:2px solid #000;padding-bottom:12px;margin-bottom:16px;">
      <h2 style="font-size:1.3rem;font-weight:800;letter-spacing:-0.02em;margin:0;">OFFICIAL BWF TOURNAMENT SCORECARD (FORM 4)</h2>
      <div style="font-size:0.82rem;color:#475569;margin-top:4px;"><strong>${state.title}</strong> · Court ${match.court || 1} · Date: ${new Date().toLocaleDateString()} · Shuttle Speed: 77</div>
    </div>

    <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px;font-size:0.85rem;">
      <div><strong>TEAM / ATHLETE A:</strong> ${match.a}</div>
      <div><strong>TEAM / ATHLETE B:</strong> ${match.b}</div>
      <div><strong>STAGE:</strong> Pool ${match.pool}</div>
      <div><strong>MATCH DURATION:</strong> ${dur}</div>
      <div style="grid-column:span 2;"><strong>DISCIPLINARY CODE:</strong> ${cardsList}</div>
    </div>

    <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:16px;font-size:0.9rem;">
      <div><strong>TEAM / ATHLETE A:</strong> ${match.a}</div>
      <div><strong>TEAM / ATHLETE B:</strong> ${match.b}</div>
      <div><strong>STAGE:</strong> Pool ${match.pool}</div>
      <div><strong>MATCH DURATION:</strong> ${dur}</div>
    </div>

    <table class="scorecard-table">
      <thead>
        <tr>
          <th>GAME / SET</th>
          <th>${match.a}</th>
          <th>${match.b}</th>
          <th>SET WINNER</th>
        </tr>
      </thead>
      <tbody>
        ${match.sets.map((s, idx) => `
          <tr>
            <td>Game ${idx + 1}</td>
            <td style="font-size:1.1rem;font-weight:bold;">${s.score[0]}</td>
            <td style="font-size:1.1rem;font-weight:bold;">${s.score[1]}</td>
            <td>${s.winner ? (s.winner === 'a' ? match.a : match.b) : 'In Progress'}</td>
          </tr>
        `).join('')}
      </tbody>
    </table>

    <div style="margin-top:20px;padding:10px;background:#f8f9fa;border:1px solid #ddd;font-size:0.85rem;">
      <strong>MATCH WINNER:</strong> ${match.winner ? (match.winner === 'a' ? match.a : match.b) : 'Pending Final Score'}
    </div>

    <div style="margin-top:24px;">
      <div style="font-size:0.8rem;font-weight:600;margin-bottom:6px;">Official Digital Signatures & Sign-Off:</div>
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;font-size:0.75rem;text-align:center;">
        <div>
          <div class="signature-canvas-container">
            <canvas id="umpireSignPad" class="signature-canvas"></canvas>
          </div>
          <div style="margin-top:4px;">Umpire Signature</div>
        </div>
        <div>
          <div class="signature-canvas-container">
            <canvas id="captainASignPad" class="signature-canvas"></canvas>
          </div>
          <div style="margin-top:4px;">Team A Captain</div>
        </div>
        <div>
          <div class="signature-canvas-container">
            <canvas id="captainBSignPad" class="signature-canvas"></canvas>
          </div>
          <div style="margin-top:4px;">Team B Captain</div>
        </div>
      </div>
    </div>
  `;

  document.getElementById('scorecardModal').showModal();
}

/* ═══════════════════════════════════════════════════
   ADMIN DASHBOARD RENDERING
═══════════════════════════════════════════════════ */
function logAdminAudit(action) {
  const adminName = currentUser ? currentUser.name : 'admin';
  state.auditLogs = state.auditLogs || [];
  state.auditLogs.push({
    id: 'log_' + Date.now(),
    adminName,
    action,
    timestamp: new Date().toLocaleTimeString()
  });
  if (state.auditLogs.length > 200) state.auditLogs.shift();
  saveState();
}

function renderAdminDashboard() {
  const users = getUsersDB();

  // Metrics
  const total = users.length;
  const active = users.filter(u => u.status === 'active').length;
  const pending = users.filter(u => u.status === 'invited').length;
  const completedMatches = state.matches ? state.matches.filter(m => !!m.winner).length : 0;

  document.getElementById('adminTotalAthletes').textContent = total;
  document.getElementById('adminActiveAthletes').textContent = active;
  document.getElementById('adminPendingInvites').textContent = pending;
  document.getElementById('adminFeesCollected').textContent = completedMatches;

  // 1. Users Directory Table (Items 1–10)
  const userBody = document.getElementById('adminUsersTableBody');
  if (userBody) {
    if (!users.length) {
      userBody.innerHTML = `<tr><td colspan="7" style="text-align:center;padding:16px;color:var(--clr-text-muted);">No users in directory.</td></tr>`;
    } else {
      userBody.innerHTML = users.map(u => `
        <tr>
          <td><code style="font-size:0.75rem;">${u.id}</code></td>
          <td>
            <div style="display:flex;align-items:center;gap:8px;">
              <div class="user-avatar" style="width:24px;height:24px;font-size:0.75rem;">${u.avatar || u.name.charAt(0)}</div>
              <strong>${u.name}</strong>
            </div>
          </td>
          <td style="color:var(--clr-text-muted);">${u.email || '—'}</td>
          <td><span class="user-role-badge">${u.role}</span></td>
          <td><span class="${u.status === 'active' ? 'badge-active' : 'badge-invited'}">${u.status || 'active'}</span></td>
          <td>
            <span class="badge-active" style="background:rgba(255,255,255,0.08);color:var(--clr-text-muted);border-color:transparent;">
              ${u.feeStatus === 'seeded' ? 'Top Seed' : (u.feeStatus === 'qualifier' ? 'Qualifier' : 'Standard')}
            </span>
          </td>
          <td>
            <div style="display:flex;gap:4px;">
              ${u.status === 'invited' ? `<button class="btn btn-ghost btn-xs" onclick="resendInvitationEmail(${u.id})" title="Resend Invite">Resend</button>` : ''}
              <button class="btn btn-ghost btn-xs" onclick="toggleUserRole(${u.id})" title="Toggle Role">Role</button>
              <button class="btn btn-danger btn-xs" onclick="deleteUserRecord(${u.id})" title="Delete">${svgIcon("x", "icon-xs")}</button>
            </div>
          </td>
        </tr>
      `).join('');
    }
  }

  // 2. Court Dispatcher Grid
  renderAdminCourtQueue();

  // 3. Matches Oversight Table
  const matchBody = document.getElementById('adminMatchesTableBody');
  if (matchBody) {
    matchBody.innerHTML = state.matches.map(m => {
      const dur = m.durationSeconds ? `${Math.floor(m.durationSeconds / 60)}m ${m.durationSeconds % 60}s` : '—';
      const scoreStr = m.sets.map(s => `${s.score[0]}–${s.score[1]}`).join(' | ');
      return `
        <tr>
          <td><code style="font-size:0.75rem;">${m.id}</code></td>
          <td>${m.pool}</td>
          <td><strong>${m.a}</strong></td>
          <td><strong>${m.b}</strong></td>
          <td><span style="font-family:monospace;color:var(--clr-gold);">${scoreStr}</span></td>
          <td>${dur}</td>
          <td>${m.winner ? '<span style="color:var(--clr-green);font-weight:bold;">COMPLETED</span>' : '<span>PENDING</span>'}</td>
          <td>
            <button class="btn btn-ghost btn-xs" onclick="resetSingleMatch('${m.id}')" title="Reset match back to pending">↺ Reset</button>
          </td>
        </tr>
      `;
    }).join('');
  }

  // 4. Suggestions Review Queue
  const suggBody = document.getElementById('adminSuggestionsTableBody');
  if (suggBody) {
    const suggestions = getSuggestionsDB();
    if (!suggestions.length) {
      suggBody.innerHTML = `<tr><td colspan="6" style="text-align:center;padding:16px;color:var(--clr-text-muted);">No pending score suggestions.</td></tr>`;
    } else {
      suggBody.innerHTML = suggestions.map(s => `
        <tr>
          <td>${s.matchTitle}</td>
          <td><strong>${s.setsStr}</strong></td>
          <td>${s.winnerName}</td>
          <td>${s.submittedBy}</td>
          <td>${s.timestamp}</td>
          <td>
            <button class="btn btn-primary btn-xs" onclick="approveScoreSuggestion('${s.id}')">Approve</button>
            <button class="btn btn-danger btn-xs" onclick="rejectScoreSuggestion('${s.id}')">Reject</button>
          </td>
        </tr>
      `).join('');
    }
  }

  // 5. Audit Log
  const logCont = document.getElementById('adminAuditLogContainer');
  if (logCont) {
    if (!state.auditLogs || !state.auditLogs.length) {
      logCont.innerHTML = `<div>No administrative operations logged yet.</div>`;
    } else {
      logCont.innerHTML = state.auditLogs.slice(-20).reverse().map(l => `
        <div><span style="color:var(--clr-gold);font-weight:bold;">${l.adminName}</span>: ${l.action} <span style="font-size:0.75rem;opacity:0.6;">(${l.timestamp})</span></div>
      `).join('');
    }
  }
}

function resetSingleMatch(matchId) {
  const match = state.matches.find(m => m.id === matchId);
  if (!match) return;
  if (confirm(`Reset match ${match.a} vs ${match.b} back to pending? Any wagers will be refunded.`)) {
    // Reverse stats from leaderboard
    if (match.winner) {
      try {
        const db = getLeaderboardDB();
        const winName = match.winner === 'a' ? match.a : match.b;
        const loseName = match.winner === 'a' ? match.b : match.a;
        if (db[winName]) db[winName].won = Math.max(0, (db[winName].won || 1) - 1);
        if (db[loseName]) db[loseName].lost = Math.max(0, (db[loseName].lost || 1) - 1);
        saveLeaderboardDB(db);
      } catch (e) {}
    }
    match.winner = null;
    match.sets = [{ score: [0, 0], winner: null }];
    match.durationSeconds = 0;
    match.history = [];
    match.cards = [];

    const bets = getBetsDB();
    const wallets = getWalletsDB();
    bets.filter(b => b.matchId === matchId && b.status === 'pending').forEach(b => {
      b.status = 'refunded';
      wallets[b.username] = (wallets[b.username] || 0) + b.stake;
      recordTransaction(b.username, 'refund', b.stake, wallets[b.username], `Refund on reset of ${match.a} vs ${match.b}`);
    });
    saveBetsDB(bets);
    saveWalletsDB(wallets);

    logAdminAudit(`Reset match ${match.a} vs ${match.b} to pending`);
    saveState();
    renderGroups();
    renderBracket();
    renderAdminDashboard();
    updateBettingUI();
    showToast('↺ Match reset to pending.');
  }
}

function openScoreOverrideModal() {
  const sel = document.getElementById('overrideMatchSelect');
  sel.innerHTML = state.matches.map(m => `<option value="${m.id}">${m.a} vs ${m.b} (${m.pool})</option>`).join('');
  document.getElementById('scoreOverrideModal').showModal();
}

function saveManualScoreOverride() {
  const matchId = document.getElementById('overrideMatchSelect').value;
  const setsRaw = document.getElementById('overrideSetsInput').value.trim();
  const winSide = document.getElementById('overrideWinnerSelect').value;
  const match = state.matches.find(m => m.id === matchId);
  if (!match) return;

  if (setsRaw) {
    const setsParsed = setsRaw.split(',').map(s => {
      const parts = s.trim().split(/[-–]/).map(n => parseInt(n.trim()) || 0);
      return { score: [parts[0] || 0, parts[1] || 0], winner: parts[0] > parts[1] ? 'a' : 'b' };
    });
    match.sets = setsParsed;
  }
  match.winner = winSide;

  settleMatchBets(match);

  if (state.currentMatchId === match.id) {
    state.currentSetIdx = match.sets.length - 1;
    updateLiveScoreboardUI();
  }

  if (match.pool === 'KO') {
    advanceKnockoutRounds();
  }

  logAdminAudit(`Overrode score for ${match.a} vs ${match.b} (Winner: ${winSide})`);
  saveState();
  broadcastStateChange();
  renderGroups();
  renderBracket();
  renderAdminDashboard();
  document.getElementById('scoreOverrideModal').close();
  showToast('Match score overridden.');
}

function toggleUserRole(userId) {
  const users = getUsersDB();
  const user = users.find(u => u.id === userId);
  if (user) {
    user.role = user.role === 'admin' ? 'player' : 'admin';
    saveUsersDB(users);
    logAdminAudit(`Changed role for user ${user.name} to ${user.role}`);
    renderAdminDashboard();
    updateUserUI();
  updateBettingUI();
    showToast(`User ${user.name} is now ${user.role}.`);
  }
}

function getSuggestionsDB() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY_SUGGESTIONS)) || [];
  } catch (e) { return []; }
}
function saveSuggestionsDB(suggs) {
  try {
    localStorage.setItem(STORAGE_KEY_SUGGESTIONS, JSON.stringify(suggs));
  } catch (e) {}
}

function openSuggestScoreModal() {
  const sel = document.getElementById('suggestMatchSelect');
  sel.innerHTML = state.matches.filter(m => !m.winner && m.a !== 'BYE' && m.b !== 'BYE')
    .map(m => `<option value="${m.id}">${m.a} vs ${m.b} (${m.pool})</option>`).join('');
  document.getElementById('suggestScoreModal').showModal();
}

function submitSuggestedScore() {
  const matchId = document.getElementById('suggestMatchSelect').value;
  const setsStr = document.getElementById('suggestSetsInput').value.trim();
  const winner = document.getElementById('suggestWinnerSelect').value;
  const match = state.matches.find(m => m.id === matchId);
  if (!match) return;

  const username = currentUser ? currentUser.name : 'Guest';

  if (currentUser && currentUser.role === 'admin') {
    const sets = setsStr.split(',').map(s => {
      const parts = s.trim().split(/[-–]/).map(n => parseInt(n.trim()) || 0);
      return { score: [parts[0] || 0, parts[1] || 0], winner: parts[0] > parts[1] ? 'a' : 'b' };
    });
    match.sets = sets;
    match.winner = winner;
    recordMatchStats(match);
    settleMatchBets(match);
    saveState();
    renderGroups();
    renderBracket();
    updateGoldenAwards();
    renderAdminDashboard();
    document.getElementById('suggestScoreModal').close();
    showToast('Score approved directly by Admin!');
    return;
  }

  const suggs = getSuggestionsDB();
  suggs.push({
    id: 'sugg_' + Date.now(),
    matchId,
    matchTitle: `${match.a} vs ${match.b}`,
    setsStr,
    winner,
    winnerName: winner === 'a' ? match.a : match.b,
    submittedBy: username,
    timestamp: new Date().toLocaleTimeString()
  });
  saveSuggestionsDB(suggs);

  document.getElementById('suggestScoreModal').close();
  showToast('Score suggestion submitted for Admin review!');
}

function approveScoreSuggestion(suggId) {
  const suggs = getSuggestionsDB();
  const sugg = suggs.find(s => s.id === suggId);
  if (!sugg) return;

  const match = state.matches.find(m => m.id === sugg.matchId);
  if (match) {
    const sets = sugg.setsStr.split(',').map(s => {
      const parts = s.trim().split(/[-–]/).map(n => parseInt(n.trim()) || 0);
      return { score: [parts[0] || 0, parts[1] || 0], winner: parts[0] > parts[1] ? 'a' : 'b' };
    });
    match.sets = sets;
    match.winner = sugg.winner;
    recordMatchStats(match);
    settleMatchBets(match);
    logAdminAudit(`Approved score suggestion for ${match.a} vs ${match.b} from ${sugg.submittedBy}`);
  }

  saveSuggestionsDB(suggs.filter(s => s.id !== suggId));
  saveState();
  broadcastStateChange();
  renderGroups();
  renderBracket();
  updateGoldenAwards();
  renderAdminDashboard();
  showToast('Suggestion approved.');
}

function rejectScoreSuggestion(suggId) {
  const suggs = getSuggestionsDB();
  saveSuggestionsDB(suggs.filter(s => s.id !== suggId));
  logAdminAudit(`Rejected score suggestion ID ${suggId}`);
  renderAdminDashboard();
  showToast('Suggestion rejected.');
}

function downloadTournamentBackupJSON() {
  const backup = {
    version: '4.0',
    exportDate: new Date().toISOString(),
    state,
    users: getUsersDB(),
    wallets: getWalletsDB(),
    bets: getBetsDB(),
    txs: getTxLedgerDB()
  };
  const blob = new Blob([JSON.stringify(backup, null, 2)], { type: 'application/json' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = `badminton_cup_backup_${new Date().toISOString().slice(0, 10)}.json`;
  a.click();
  showToast('Backup JSON downloaded.');
}

function triggerRestoreBackupJSON() {
  document.getElementById('restoreBackupInput').click();
}

function handleRestoreBackupFile(e) {
  const file = e.target.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = (evt) => {
    try {
      const data = JSON.parse(evt.target.result);
      if (data.state) {
        Object.assign(state, data.state);
        saveState();
      }
      if (data.users) saveUsersDB(data.users);
      if (data.wallets) saveWalletsDB(data.wallets);
      if (data.bets) saveBetsDB(data.bets);
      if (data.txs) localStorage.setItem(STORAGE_KEY_TXS, JSON.stringify(data.txs));

      refreshCurrentViews();
      showToast('Full tournament data restored!');
    } catch (err) {
      showToast('Invalid backup JSON file.');
    }
  };
  reader.readAsText(file);
}

/* ═══════════════════════════════════════════════════
   BETTING & WALLET ENGINE
═══════════════════════════════════════════════════ */
function getWalletsDB() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY_WALLETS)) || {};
  } catch (e) { return {}; }
}
function saveWalletsDB(wallets) {
  try {
    localStorage.setItem(STORAGE_KEY_WALLETS, JSON.stringify(wallets));
  } catch (e) {}
}

function getBetsDB() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY_BETS)) || [];
  } catch (e) { return []; }
}
function saveBetsDB(bets) {
  try {
    localStorage.setItem(STORAGE_KEY_BETS, JSON.stringify(bets));
  } catch (e) {}
}

function getTxLedgerDB() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY_TXS)) || [];
  } catch (e) { return []; }
}
function recordTransaction(username, type, amount, balanceAfter, desc) {
  try {
    const txs = getTxLedgerDB();
    txs.push({
      id: 'tx_' + Date.now() + '_' + Math.random().toString(36).substr(2, 4),
      username,
      type,
      amount,
      balanceAfter,
      desc,
      timestamp: new Date().toLocaleTimeString()
    });
    if (txs.length > 500) txs.shift();
    localStorage.setItem(STORAGE_KEY_TXS, JSON.stringify(txs));
  } catch (e) {}
}


/* ═══════════════════════════════════════════════════
   VIRTUAL COIN WALLET & MATCH PREDICTION ENGINE
   - General Users & Everyone can predict match winners and place wagers with virtual coins.
═══════════════════════════════════════════════════ */
function getUserCoins() {
  const username = currentUser ? currentUser.name : 'Guest';
  const wallets = getWalletsDB();
  if (wallets[username] === undefined) {
    wallets[username] = 100; // 100 free starter coins for everyone!
    saveWalletsDB(wallets);
  }
  return wallets[username];
}

function setUserCoins(amount) {
  const username = currentUser ? currentUser.name : 'Guest';
  const wallets = getWalletsDB();
  wallets[username] = Math.max(0, amount);
  saveWalletsDB(wallets);
  updateBettingUI();
}

function claimDailyBonus() {
  const current = getUserCoins();
  const bonus = 50;
  setUserCoins(current + bonus);
  recordTransaction(currentUser ? currentUser.name : 'Guest', 'bonus', bonus, current + bonus, 'Daily reward bonus');
  const bigCount = document.getElementById('coinModalBigCount');
  if (bigCount) bigCount.textContent = (current + bonus).toLocaleString();
  showToast('🎁 Claimed 50 Free Bonus Coins!', 'success');
  playChimeSound('win');
}

function openCoinBalanceModal() {
  const coins = getUserCoins();
  const bigCount = document.getElementById('coinModalBigCount');
  if (bigCount) bigCount.textContent = coins.toLocaleString();
  const modal = document.getElementById('coinBalanceModal');
  if (modal) modal.showModal();
}

function updateBettingUI() {
  const coins = getUserCoins();
  const headerCoinEl = document.getElementById('headerCoinCount');
  if (headerCoinEl) headerCoinEl.textContent = coins.toLocaleString();
  const betBalanceEl = document.getElementById('bettingModalUserBalance');
  if (betBalanceEl) betBalanceEl.textContent = coins.toLocaleString();
}

function openBettingModal(matchId) {
  const match = state.matches.find(m => m.id === matchId);
  if (!match) return;

  activeBetMatch = match;
  activeBetSide = 'a';

  document.getElementById('betModalMatchId').value = match.id;
  document.getElementById('betModalTeamAName').textContent = match.a;
  document.getElementById('betModalTeamBName').textContent = match.b;
  document.getElementById('betModalTeamABtn').textContent = `Predict ${match.a} (1.90x)`;
  document.getElementById('betModalTeamBBtn').textContent = `Predict ${match.b} (1.90x)`;
  selectBetSide('a');
  setBetAmount(25);
  updateBettingUI();
  document.getElementById('matchBettingModal').showModal();
}

function selectBetSide(side) {
  activeBetSide = side;
  const btnA = document.getElementById('betModalTeamABtn');
  const btnB = document.getElementById('betModalTeamBBtn');
  if (btnA && btnB) {
    btnA.classList.toggle('active', side === 'a');
    btnB.classList.toggle('active', side === 'b');
    if (side === 'a') {
      btnA.style.borderColor = 'var(--clr-green)';
      btnA.style.background = 'rgba(16, 185, 129, 0.15)';
      btnB.style.borderColor = '';
      btnB.style.background = '';
    } else {
      btnB.style.borderColor = 'var(--clr-green)';
      btnB.style.background = 'rgba(16, 185, 129, 0.15)';
      btnA.style.borderColor = '';
      btnA.style.background = '';
    }
  }
}

function setBetAmount(amount) {
  const input = document.getElementById('betModalAmountInput');
  if (input) input.value = amount;
}

function placeBet() {
  if (!activeBetMatch) return;
  const amount = parseInt(document.getElementById('betModalAmountInput')?.value, 10);
  if (isNaN(amount) || amount <= 0) {
    showToast('Please enter a valid coin amount.', 'warning');
    return;
  }

  const coins = getUserCoins();
  if (coins < amount) {
    showToast(`Insufficient coins! You have ${coins} coins. Claim bonus coins in your wallet.`, 'warning');
    return;
  }

  const username = currentUser ? currentUser.name : 'Guest';
  const teamName = (activeBetSide === 'a') ? activeBetMatch.a : activeBetMatch.b;
  const odds = 1.90;

  setUserCoins(coins - amount);
  recordTransaction(username, 'bet_placed', amount, coins - amount, `Placed prediction on ${teamName}`);

  const bets = getBetsDB();
  bets.push({
    id: 'bet_' + Date.now(),
    matchId: activeBetMatch.id,
    username,
    teamName,
    side: activeBetSide,
    amount,
    odds,
    status: 'pending',
    placedAt: new Date().toLocaleTimeString()
  });
  saveBetsDB(bets);

  document.getElementById('matchBettingModal').close();
  showToast(`Placed ${amount} coin prediction on ${teamName}!`, 'success');
  updateBettingUI();
}

function settleMatchBets(match) {
  if (!match || !match.winner) return;
  const bets = getBetsDB();
  let updated = false;
  const currentUsername = currentUser ? currentUser.name : 'Guest';

  bets.forEach(b => {
    if (b.matchId === match.id && b.status === 'pending') {
      b.settledAt = new Date().toLocaleTimeString();
      if (b.side === match.winner) {
        b.status = 'won';
        const payout = Math.round(b.amount * (b.odds || 1.90));
        b.payout = payout;

        const wallets = getWalletsDB();
        wallets[b.username] = (wallets[b.username] || 0) + payout;
        saveWalletsDB(wallets);
        recordTransaction(b.username, 'bet_won', payout, wallets[b.username], `Won prediction on match ${match.a} vs ${match.b}`);

        if (b.username === currentUsername) {
          showToast(`🎉 Congratulations! You won ${payout} coins on ${b.teamName}!`, 'success');
          playChimeSound('win');
        }
      } else {
        b.status = 'lost';
        b.payout = 0;
        recordTransaction(b.username, 'bet_lost', b.amount, getUserCoins(), `Lost prediction on match ${match.a} vs ${match.b}`);
      }
      updated = true;
    }
  });

  if (updated) {
    saveBetsDB(bets);
    updateBettingUI();
  }
}


/* ═══════════════════════════════════════════════════
   TOURNAMENT SCHEDULE & TIMETABLE ENGINE
═══════════════════════════════════════════════════ */
function renderScheduleScreen() {
  const container = document.getElementById('scheduleTimelineContainer');
  if (!container) return;

  const courtFilter = document.getElementById('scheduleCourtFilter')?.value || 'all';
  const statusFilter = document.getElementById('scheduleStatusFilter')?.value || 'all';
  const stageFilter = document.getElementById('scheduleStageFilter')?.value || 'all';

  let list = [...state.matches];

  // Stage filter
  if (stageFilter === 'groups') {
    list = list.filter(m => m.pool === 'A' || m.pool === 'B');
  } else if (stageFilter === 'knockout') {
    list = list.filter(m => m.pool === 'KO');
  }

  // Court filter
  if (courtFilter !== 'all') {
    list = list.filter(m => m.court === parseInt(courtFilter, 10));
  }

  // Status filter
  if (statusFilter === 'live') {
    list = list.filter(m => !m.winner && (m.id === state.currentMatchId || m.status === 'in_progress' || (m.sets && m.sets.some(s => s.score[0] > 0 || s.score[1] > 0))));
  } else if (statusFilter === 'upcoming') {
    list = list.filter(m => !m.winner && m.id !== state.currentMatchId && (!m.sets || m.sets.every(s => s.score[0] === 0 && s.score[1] === 0)));
  } else if (statusFilter === 'completed') {
    list = list.filter(m => !!m.winner);
  }

  if (!list.length) {
    container.innerHTML = `
      <div class="empty-state-card">
        <div class="empty-state-icon">${svgIcon("calendar", "icon-3xl")}</div>
        <div class="empty-state-title">No Fixtures Match Selected Filter</div>
        <div class="empty-state-desc">Try selecting 'All Courts' or 'All Statuses' to view the complete tournament timetable.</div>
      </div>
    `;
    return;
  }

  container.innerHTML = list.map((m, idx) => {
    const isLive = !m.winner && (m.id === state.currentMatchId || m.status === 'in_progress' || (m.sets && m.sets.some(s => s.score[0] > 0 || s.score[1] > 0)));
    const isCompleted = !!m.winner;
    const scoreStr = m.sets.map(s => `${s.score[0]}–${s.score[1]}`).join('  |  ');
    const winnerName = m.winner ? (m.winner === 'a' ? m.a : m.b) : null;

    let statusPill = `<span class="badge-active" style="background:rgba(255,255,255,0.08);color:var(--clr-text-muted);border-color:transparent;">UPCOMING</span>`;
    if (isLive) {
      statusPill = `<span class="status-badge-live badge-game-point">${svgIcon("dot")} LIVE NOW</span>`;
    } else if (isCompleted) {
      statusPill = `<span class="badge-active">COMPLETED</span>`;
    }

    return `
      <div class="schedule-card ${isLive ? 'live-fixture' : ''}">
        <div style="display:flex;align-items:center;gap:14px;flex-wrap:wrap;">
          <span class="court-pill">COURT ${m.court || 1}</span>
          <div>
            <div style="font-size:0.75rem;color:var(--clr-text-muted);font-weight:700;letter-spacing:0.06em;text-transform:uppercase;">
              ${m.pool === 'KO' ? 'Playoff Knockout' : `Pool ${m.pool} Fixture`} · Match #${idx + 1}
            </div>
            <div style="font-size:1.05rem;font-weight:900;margin-top:2px;">
              <span style="color:${m.winner === 'a' ? 'var(--clr-green)' : '#60a5fa'};">${m.a}</span>
              <span style="color:var(--clr-text-muted);font-size:0.8rem;margin:0 6px;">vs</span>
              <span style="color:${m.winner === 'b' ? 'var(--clr-green)' : '#f87171'};">${m.b}</span>
            </div>
          </div>
        </div>

        <div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap;">
          <div style="text-align:right;">
            <div style="font-family:monospace;font-size:1.05rem;font-weight:bold;color:var(--clr-gold);">${scoreStr || '0–0'}</div>
            ${winnerName ? `<div style="font-size:0.75rem;color:var(--clr-text-muted);">Winner: <strong style="color:var(--clr-green);">${winnerName}</strong></div>` : ''}
          </div>
          <div>${statusPill}</div>
          <div>
            ${!isCompleted ?
              `<button class="btn btn-primary btn-xs" onclick="startUmpireMatch('${m.id}')">Umpire Match &rarr;</button>` :
              `<button class="btn btn-ghost btn-xs" onclick="openScorecardModal('${m.id}')">Scorecard</button>`
            }
          </div>
        </div>
      </div>
    `;
  }).join('');
}

/* ═══════════════════════════════════════════════════
   HEAD-TO-HEAD (H2H) & ANALYTICS ENGINE
═══════════════════════════════════════════════════ */
function renderAnalyticsScreen() {
  const selA = document.getElementById('analyticsPlayerASelect');
  const selB = document.getElementById('analyticsPlayerBSelect');
  if (!selA || !selB) return;

  const db = getLeaderboardDB();
  const allNames = Array.from(new Set([
    ...Object.keys(db),
    ...state.poolA,
    ...state.poolB
  ])).filter(n => n && n !== 'BYE');

  if (!allNames.length) {
    document.getElementById('analyticsComparisonResult').innerHTML = `
      <div class="empty-state-card">
        <div class="empty-state-icon">${svgIcon("scale", "icon-3xl")}</div>
        <div class="empty-state-title">No Athlete Profiles Available</div>
        <div class="empty-state-desc">Configure your roster and kick off a tournament to view head-to-head records.</div>
      </div>
    `;
    return;
  }

  const curA = selA.value;
  const curB = selB.value;

  selA.innerHTML = allNames.map(n => `<option value="${n}" ${n === curA ? 'selected' : ''}>${n}</option>`).join('');
  selB.innerHTML = allNames.map(n => `<option value="${n}" ${n === (curB || allNames[1] || allNames[0]) ? 'selected' : ''}>${n}</option>`).join('');

  runAnalyticsComparison();
}

function runAnalyticsComparison() {
  const selA = document.getElementById('analyticsPlayerASelect');
  const selB = document.getElementById('analyticsPlayerBSelect');
  const resultDiv = document.getElementById('analyticsComparisonResult');
  if (!selA || !selB || !resultDiv) return;

  const pA = selA.value;
  const pB = selB.value;
  if (!pA || !pB) return;

  const db = getLeaderboardDB();
  const statsA = db[pA] || { name: pA, elo: 1200, won: 0, lost: 0, totalPts: 0, ptsDiff: 0 };
  const statsB = db[pB] || { name: pB, elo: 1200, won: 0, lost: 0, totalPts: 0, ptsDiff: 0 };

  const h2hMatches = state.matches.filter(m =>
    m.winner && ((m.a === pA && m.b === pB) || (m.a === pB && m.b === pA))
  );

  let winsA = 0;
  let winsB = 0;
  h2hMatches.forEach(m => {
    const winner = m.winner === 'a' ? m.a : m.b;
    if (winner === pA) winsA++;
    else if (winner === pB) winsB++;
  });

  const totalMatchesA = (statsA.won || 0) + (statsA.lost || 0);
  const winRateA = totalMatchesA > 0 ? Math.round((statsA.won / totalMatchesA) * 100) : 0;
  const totalMatchesB = (statsB.won || 0) + (statsB.lost || 0);
  const winRateB = totalMatchesB > 0 ? Math.round((statsB.won / totalMatchesB) * 100) : 0;

  const eloA = statsA.elo || 1200;
  const eloB = statsB.elo || 1200;
  const totalElo = eloA + eloB;
  const eloPctA = Math.round((eloA / totalElo) * 100);

  resultDiv.innerHTML = `
    <!-- Top Level Scorecard -->
    <div style="display:grid;grid-template-columns:1fr 140px 1fr;align-items:center;background:rgba(0,0,0,0.3);border-radius:var(--radius-md);padding:24px;margin-bottom:20px;border:1px solid var(--clr-border);">
      <div style="text-align:center;">
        <div style="font-size:1.3rem;font-weight:900;color:#60a5fa;">${pA}</div>
        <div style="font-family:'Anton',sans-serif;font-size:3rem;color:var(--clr-gold);">${winsA}</div>
        <div style="font-size:0.75rem;color:var(--clr-text-muted);font-weight:700;">H2H VICTORIES</div>
      </div>

      <div style="text-align:center;">
        <div style="font-size:0.8rem;color:var(--clr-text-muted);font-weight:bold;">TOTAL MEETINGS</div>
        <div style="font-family:'Anton',sans-serif;font-size:2rem;color:#ffffff;">${h2hMatches.length}</div>
        <div style="font-size:0.75rem;color:var(--clr-gold);">${winsA > winsB ? `${pA} leads` : (winsB > winsA ? `${pB} leads` : 'Tied')}</div>
      </div>

      <div style="text-align:center;">
        <div style="font-size:1.3rem;font-weight:900;color:#f87171;">${pB}</div>
        <div style="font-family:'Anton',sans-serif;font-size:3rem;color:var(--clr-gold);">${winsB}</div>
        <div style="font-size:0.75rem;color:var(--clr-text-muted);font-weight:700;">H2H VICTORIES</div>
      </div>
    </div>

    <!-- Comparative Metric Bars -->
    <div style="display:flex;flex-direction:column;gap:16px;">
      <!-- Elo -->
      <div>
        <div style="display:flex;justify-content:space-between;font-size:0.85rem;font-weight:bold;margin-bottom:4px;">
          <span style="color:#60a5fa;">${pA}: ${eloA} Elo</span>
          <span style="color:var(--clr-text-muted);">Skill Rating (Elo)</span>
          <span style="color:#f87171;">${pB}: ${eloB} Elo</span>
        </div>
        <div style="background:rgba(255,255,255,0.1);height:8px;border-radius:var(--radius-full);overflow:hidden;display:flex;">
          <div style="width:${eloPctA}%;background:#3b82f6;"></div>
          <div style="width:${100 - eloPctA}%;background:#ef4444;"></div>
        </div>
      </div>

      <!-- Win Rate -->
      <div>
        <div style="display:flex;justify-content:space-between;font-size:0.85rem;font-weight:bold;margin-bottom:4px;">
          <span style="color:#60a5fa;">${winRateA}% (${statsA.won}W / ${statsA.lost}L)</span>
          <span style="color:var(--clr-text-muted);">Tournament Win Rate</span>
          <span style="color:#f87171;">${winRateB}% (${statsB.won}W / ${statsB.lost}L)</span>
        </div>
        <div style="background:rgba(255,255,255,0.1);height:8px;border-radius:var(--radius-full);overflow:hidden;display:flex;">
          <div style="width:${winRateA + winRateB > 0 ? Math.round((winRateA / (winRateA + winRateB)) * 100) : 50}%;background:#3b82f6;"></div>
          <div style="width:${winRateA + winRateB > 0 ? 100 - Math.round((winRateA / (winRateA + winRateB)) * 100) : 50}%;background:#ef4444;"></div>
        </div>
      </div>

      <!-- Total Points -->
      <div>
        <div style="display:flex;justify-content:space-between;font-size:0.85rem;font-weight:bold;margin-bottom:4px;">
          <span style="color:#60a5fa;">${statsA.totalPts || 0} pts</span>
          <span style="color:var(--clr-text-muted);">Total Points Scored</span>
          <span style="color:#f87171;">${statsB.totalPts || 0} pts</span>
        </div>
      </div>
    </div>
  `;
}

/* ═══════════════════════════════════════════════════
   BWF RULES INTERACTIVE SERVICE COURT TESTER
═══════════════════════════════════════════════════ */

function switchGuideTab(tabName) {
  const tabs = ['app', 'rules', 'roles', 'faq'];
  tabs.forEach(t => {
    const sec = document.getElementById('guideSection' + t.charAt(0).toUpperCase() + t.slice(1));
    const btn = document.getElementById('guideTab' + t.charAt(0).toUpperCase() + t.slice(1) + 'Btn');
    if (sec) sec.style.display = (t === tabName) ? 'block' : 'none';
    if (btn) btn.classList.toggle('active', t === tabName);
  });
}

function testRuleServiceCourt(val) {
  const score = parseInt(val, 10);
  const res = document.getElementById('ruleScoreTestResult');
  if (!res) return;
  if (isNaN(score) || score < 0) {
    res.textContent = 'Please enter a valid non-negative score.';
    return;
  }
  const isEven = (score % 2 === 0);
  res.innerHTML = isEven ?
    `Score ${score} is <strong style="color:var(--clr-green);">EVEN</strong> &rarr; Server serves from <strong style="color:var(--clr-gold);">RIGHT Court</strong> diagonally to receiver's right half.` :
    `Score ${score} is <strong style="color:var(--clr-gold);">ODD</strong> &rarr; Server serves from <strong style="color:var(--clr-green);">LEFT Court</strong> diagonally to receiver's left half.`;
}

/* ═══════════════════════════════════════════════════
   MATCH SCORECARDS GALLERY
═══════════════════════════════════════════════════ */
function renderScorecardsScreen() {
  const container = document.getElementById('scorecardsGalleryContainer');
  if (!container) return;

  if (!state.matches.length) {
    container.innerHTML = `
      <div class="empty-state-card" style="grid-column:1/-1;">
        <div class="empty-state-icon">${svgIcon("clipboard", "icon-3xl")}</div>
        <div class="empty-state-title">No Match Records Created Yet</div>
        <div class="empty-state-desc">Generate fixtures to produce official printable BWF scorecards.</div>
        <button class="btn btn-primary btn-sm" onclick="showScreen('setupScreen')">Setup Tournament &rarr;</button>
      </div>
    `;
    return;
  }

  container.innerHTML = state.matches.map((m, idx) => {
    const isCompleted = !!m.winner;
    const scoreStr = m.sets.map(s => `${s.score[0]}–${s.score[1]}`).join('  |  ');
    return `
      <div class="card" style="padding:16px;background:rgba(0,0,0,0.3);border:1px solid ${isCompleted ? 'rgba(34,197,94,0.3)' : 'var(--clr-border)'};">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
          <span style="font-size:0.75rem;font-weight:800;color:var(--clr-text-muted);">
            Court ${m.court || 1} · ${m.pool === 'KO' ? 'Knockout' : `Pool ${m.pool}`}
          </span>
          <span class="badge-active" style="${isCompleted ? '' : 'background:rgba(255,255,255,0.06);color:var(--clr-text-muted);'}">
            ${isCompleted ? 'OFFICIAL RESULT' : 'SCHEDULED'}
          </span>
        </div>
        <div style="font-size:1.05rem;font-weight:900;margin-bottom:8px;">
          <span style="color:#60a5fa;">${m.a}</span> vs <span style="color:#f87171;">${m.b}</span>
        </div>
        <div style="font-family:monospace;font-size:0.95rem;color:var(--clr-gold);margin-bottom:14px;">
          ${scoreStr || '0–0'}
        </div>
        <button class="btn btn-ghost btn-sm" style="width:100%;" onclick="openScorecardModal('${m.id}')">
          View & Print Scorecard
        </button>
      </div>
    `;
  }).join('');
}

/* ═══════════════════════════════════════════════════
   TOURNAMENT SETUP & DATA HELPERS
═══════════════════════════════════════════════════ */

/* ═══════════════════════════════════════════════════
   CAPABILITIES & ROLE-BASED ACCESS CONTROL (RBAC)
   - General Users: Open challenges, accept & play matches, referee casual games, coin betting & predictions.
   - Admin Users: Full control over tournament setup, pool draw, score overrides, and data reset.
═══════════════════════════════════════════════════ */
function isAdminUser() {
  return !!(currentUser && (currentUser.role === 'admin' || currentUser.role === 'super_admin'));
}

function requireAdmin(actionName, onAllowed) {
  if (isAdminUser()) {
    onAllowed();
    return;
  }
  const nameEl = document.getElementById('guardActionName');
  if (nameEl) nameEl.textContent = actionName;
  const guardModal = document.getElementById('adminAuthGuardModal');
  if (guardModal) guardModal.showModal();
}

function handleSetupNav() {
  requireAdmin('Tournament Setup & Roster', () => showScreen('setupScreen'));
}

function handleDraftNav() {
  requireAdmin('Pool Draw Machine', () => showScreen('draftScreen'));
}

function handleResetNav() {
  requireAdmin('Reset Tournament Data', () => openDataResetModal());
}

function quickSwitchToAdmin() {
  const users = getUsersDB();
  let admin = users.find(u => u.name.toLowerCase() === 'rashed');
  if (!admin) {
    admin = {
      id: 1001,
      name: 'Rashed',
      email: 'rashed@badminton.local',
      role: 'admin',
      status: 'active',
      avatar: 'R',
      club: 'Tournament Director',
      elo: 1650,
      createdAt: new Date().toLocaleDateString()
    };
    users.unshift(admin);
    saveUsersDB(users);
  } else {
    admin.role = 'admin';
    saveUsersDB(users);
  }
  setCurrentUser(admin);
  const guardModal = document.getElementById('adminAuthGuardModal');
  if (guardModal && guardModal.open) guardModal.close();
  showToast('Signed in as Rashed (Admin & Tournament Director)!', 'success');
}

function quickSwitchToGeneralUser() {
  const player = {
    id: 10001,
    name: 'Player User',
    email: 'player@badminton.local',
    role: 'player',
    status: 'active',
    avatar: 'P',
    createdAt: new Date().toLocaleDateString()
  };
  setCurrentUser(player);
  showToast('Switched to General User mode (Open challenges, betting, play).', 'info');
}

function toggleRoleDemo() {
  if (isAdminUser()) {
    quickSwitchToGeneralUser();
  } else {
    quickSwitchToAdmin();
  }
}

function showScreen(screenId) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  const target = document.getElementById(screenId);
  if (target) {
    target.classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // Auto-sync Stage Navigation Tabs (Desktop & Mobile)
  const tabMap = {
    groupsScreen: 'tabNavMatches',
    challengesScreen: 'tabNavChallenges',
    knockoutScreen: 'tabNavKnockout',
    championScreen: 'tabNavKnockout',
    leaderboardScreen: 'tabNavLeaderboard',
    setupScreen: 'tabNavMore',
    draftScreen: 'tabNavMore',
    scheduleScreen: 'tabNavMore',
    analyticsScreen: 'tabNavMore',
    rulesScreen: 'tabNavMore',
    scorecardsScreen: 'tabNavMore',
    stadiumScreen: 'tabNavMore',
    playerHubScreen: 'tabNavMore',
    adminDashboardScreen: 'tabNavMore'
  };

  const mobMap = {
    groupsScreen: 'mobNavMatches',
    challengesScreen: 'mobNavChallenges',
    knockoutScreen: 'mobNavKnockout',
    championScreen: 'mobNavKnockout',
    leaderboardScreen: 'mobNavLeaderboard',
    setupScreen: 'mobNavMore',
    draftScreen: 'mobNavMore',
    scheduleScreen: 'mobNavMore',
    analyticsScreen: 'mobNavMore',
    rulesScreen: 'mobNavMore',
    scorecardsScreen: 'mobNavMore',
    stadiumScreen: 'mobNavMore',
    playerHubScreen: 'mobNavMore',
    adminDashboardScreen: 'mobNavMore'
  };

  document.querySelectorAll('.stage-tab').forEach(t => t.classList.remove('active'));
  const activeTabId = tabMap[screenId] || 'tabNavMore';
  const activeTab = document.getElementById(activeTabId);
  if (activeTab) {
    activeTab.classList.add('active');
    activeTab.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
  }

  document.querySelectorAll('.mobile-nav-btn').forEach(b => b.classList.remove('active'));
  const activeMobId = mobMap[screenId] || 'mobNavMore';
  const activeMobBtn = document.getElementById(activeMobId);
  if (activeMobBtn) {
    activeMobBtn.classList.add('active');
  }

  // Hide stage nav & mobile nav during live umpire match for distraction-free refereeing
  const stageNav = document.getElementById('appStageNav');
  if (stageNav) {
    stageNav.style.display = (screenId === 'liveUmpireScreen' || screenId === 'stadiumScreen') ? 'none' : 'block';
  }
  const mobNav = document.getElementById('mobileBottomNav');
  if (mobNav) {
    mobNav.style.display = (screenId === 'liveUmpireScreen' || screenId === 'stadiumScreen') ? 'none' : '';
  }

  if (screenId === 'stadiumScreen') renderStadiumScreen();
  if (screenId === 'playerHubScreen') renderPlayerHub();
  if (screenId === 'scheduleScreen') renderScheduleScreen();
  if (screenId === 'analyticsScreen') renderAnalyticsScreen();
  if (screenId === 'scorecardsScreen') renderScorecardsScreen();
  if (screenId === 'challengesScreen') renderChallengesBoard();
  if (screenId === 'groupsScreen') renderGroups();
}

function updateTournamentTitle(val) {
  state.title = val || 'The Badminton Cup 2026';
}
function selectCategory(cat) {
  state.category = cat;
  document.getElementById('btnCatSingles').classList.toggle('active', cat === 'singles');
  document.getElementById('btnCatDoubles').classList.toggle('active', cat === 'doubles');
  document.getElementById('playerPoolLabelA').textContent = cat === 'doubles' ? 'Pool A Pairs' : 'Pool A Roster';
  document.getElementById('playerPoolLabelB').textContent = cat === 'doubles' ? 'Pool B Pairs' : 'Pool B Roster';
}
function selectPoints(pts) {
  state.ptsToWin = pts;
  [11, 15, 21, 30].forEach(p => {
    const el = document.getElementById(`ptsBtn${p}`);
    if (el) el.classList.toggle('active', p === pts);
  });
}
function selectBestOf(bo) {
  state.bestOf = bo;
  [1, 3, 5].forEach(b => {
    const el = document.getElementById(`bestOfBtn${b}`);
    if (el) el.classList.toggle('active', b === bo);
  });
}
function selectCourtNum(c) {
  state.courtNumber = parseInt(c) || 2;
}
function toggleAudioFx(enabled) {
  state.audioEnabled = enabled;
}
function toggleHandicapMode(enabled) {
  state.handicapEnabled = enabled;
}

function updatePlayerCounts() {
  const a = getCleanRoster('rosterAInput');
  const b = getCleanRoster('rosterBInput');
  document.getElementById('countA').textContent = a.length;
  document.getElementById('countB').textContent = b.length;
}

function getCleanRoster(textareaId) {
  const txt = document.getElementById(textareaId).value;
  return txt.split('\n').map(s => s.trim()).filter(s => s.length > 0);
}

function loadDemoData() {
  if (state.category === 'doubles') {
    document.getElementById('rosterAInput').value = "Parag Das / Rifat Haque\nRifat Tariq / Jobayer\nShewa / Sazedul\nNur / Ofi";
    document.getElementById('rosterBInput').value = "Sifat / Sajeeb\nJakir / Saiful\nAl Emran / Toufiq\nAbir / Rashed";
  } else {
    document.getElementById('rosterAInput').value = "Parag Das\nRifat Haque\nRifat Tariq\nJobayer\nShewa\nSazedul\nNur\nOfi";
    document.getElementById('rosterBInput').value = "Sifat\nSajeeb\nJakir\nSaiful\nAl Emran\nToufiq\nAbir\nRashed";
  }
  updatePlayerCounts();
  showToast('Roster loaded with Rashed (Admin) & 15 players!');
}

function openBulkRosterModal() {
  document.getElementById('bulkRosterModal').showModal();
}
function exportCurrentRosterToBulk() {
  const a = getCleanRoster('rosterAInput');
  const b = getCleanRoster('rosterBInput');
  document.getElementById('bulkRosterTextarea').value = [...a, ...b].join('\n');
}
function applyBulkRoster() {
  const raw = document.getElementById('bulkRosterTextarea').value;
  const list = raw.split(/[\n,]/).map(s => s.trim()).filter(s => s.length > 0);
  if (!list.length) {
    showToast('No names detected.');
    return;
  }
  const mid = Math.ceil(list.length / 2);
  document.getElementById('rosterAInput').value = list.slice(0, mid).join('\n');
  document.getElementById('rosterBInput').value = list.slice(mid).join('\n');
  updatePlayerCounts();
  document.getElementById('bulkRosterModal').close();
  showToast(`Applied ${list.length} athletes to pools.`);
}

/* ═══════════════════════════════════════════════════
   TOURNAMENT DRAFT & ROUND ROBIN
═══════════════════════════════════════════════════ */
function initiateTournament() {
  const a = getCleanRoster('rosterAInput');
  const b = getCleanRoster('rosterBInput');

  if (a.length < 2 && b.length < 2) {
    showToast('Please add at least 2 players or pairs to start.');
    return;
  }

  state.poolA = a;
  state.poolB = b;
  state.matches = [];
  state.koRounds = [];
  state.champion = null;
  state.runnerUp = null;
  state.thirdPlace = null;
  state.entryFee = document.getElementById('tournamentFeeInput').value || '$20.00';

  saveState();
  showScreen('draftScreen');
  setupDraftDrums();
}

let draftIntervalA = null;
let draftIntervalB = null;

function setupDraftDrums() {
  const slotA = document.getElementById('drumSlotA');
  const slotB = document.getElementById('drumSlotB');
  const summaryBox = document.getElementById('draftSummaryBox');
  const confirmBtn = document.getElementById('confirmDraftBtn');
  const skipBtn = document.getElementById('skipDraftBtn');

  summaryBox.style.display = 'none';
  confirmBtn.style.display = 'none';
  skipBtn.style.display = 'inline-block';

  let count = 0;
  draftIntervalA = setInterval(() => {
    slotA.textContent = state.poolA[Math.floor(Math.random() * state.poolA.length)] || '...';
    slotB.textContent = state.poolB[Math.floor(Math.random() * state.poolB.length)] || '...';
    count++;
    if (count > 20) {
      clearInterval(draftIntervalA);
      clearInterval(draftIntervalB);
      finishDraft();
    }
  }, 100);
}

function skipDraftAnimation() {
  if (draftIntervalA) clearInterval(draftIntervalA);
  if (draftIntervalB) clearInterval(draftIntervalB);
  finishDraft();
}

function finishDraft() {
  state.poolA = shuffleArray([...state.poolA]);
  state.poolB = shuffleArray([...state.poolB]);

  document.getElementById('drumSlotA').textContent = `${state.poolA.length} Seeded`;
  document.getElementById('drumSlotB').textContent = `${state.poolB.length} Seeded`;

  const summary = document.getElementById('draftSummaryBox');
  summary.innerHTML = `
    <div style="font-weight:bold;margin-bottom:6px;color:var(--clr-gold);">Draft Completed!</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.85rem;">
      <div><strong style="color:#60a5fa;">Pool A:</strong> ${state.poolA.join(', ')}</div>
      <div><strong style="color:#f87171;">Pool B:</strong> ${state.poolB.join(', ')}</div>
    </div>
  `;
  summary.style.display = 'block';

  document.getElementById('skipDraftBtn').style.display = 'none';
  document.getElementById('confirmDraftBtn').style.display = 'inline-block';
}

function confirmDraftAndAdvance() {
  const matchesA = generateRoundRobinMatches(state.poolA, 'A');
  const matchesB = generateRoundRobinMatches(state.poolB, 'B');
  state.matches = [...matchesA, ...matchesB];

  saveState();
  renderGroups();
  updateGoldenAwards();
  showScreen('groupsScreen');
  showToast('Stage fixtures generated!');
}

function shuffleArray(arr) {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

function createMatchObj(playerA, playerB, poolTag) {
  const totalCourts = state.courtNumber || 2;
  const court = ((state.matches.length % totalCourts) + 1);

  // Link to user IDs if in registry (Item 12)
  const users = getUsersDB();
  const userA = users.find(u => u.name === playerA);
  const userB = users.find(u => u.name === playerB);

  return {
    id: 'm_' + Math.random().toString(36).substr(2, 9),
    a: playerA,
    b: playerB,
    playerAId: userA ? userA.id : null,
    playerBId: userB ? userB.id : null,
    pool: poolTag,
    court,
    sets: [{ score: [0, 0], winner: null }],
    winner: null,
    history: [],
    durationSeconds: 0
  };
}

function generateRoundRobinMatches(players, poolTag) {
  const list = [];
  for (let i = 0; i < players.length; i++) {
    for (let j = i + 1; j < players.length; j++) {
      list.push(createMatchObj(players[i], players[j], poolTag));
    }
  }
  return list;
}

function computePoolStandings(poolPlayers, poolTag) {
  const stats = {};
  poolPlayers.forEach(p => {
    stats[p] = { name: p, W: 0, L: 0, gamesWon: 0, gamesLost: 0, ptsWon: 0, ptsLost: 0, h2h: {} };
  });

  state.matches.filter(m => m.pool === poolTag && m.winner).forEach(m => {
    const winPlayer = m.winner === 'a' ? m.a : m.b;
    const losePlayer = m.winner === 'a' ? m.b : m.a;
    if (stats[winPlayer]) {
      stats[winPlayer].W++;
      stats[winPlayer].h2h[losePlayer] = 1;
    }
    if (stats[losePlayer]) {
      stats[losePlayer].L++;
      stats[losePlayer].h2h[winPlayer] = -1;
    }

    m.sets.forEach(s => {
      if (stats[m.a]) {
        stats[m.a].ptsWon += (s.score[0] || 0);
        stats[m.a].ptsLost += (s.score[1] || 0);
        if (s.winner === 'a') stats[m.a].gamesWon++;
        if (s.winner === 'b') stats[m.a].gamesLost++;
      }
      if (stats[m.b]) {
        stats[m.b].ptsWon += (s.score[1] || 0);
        stats[m.b].ptsLost += (s.score[0] || 0);
        if (s.winner === 'b') stats[m.b].gamesWon++;
        if (s.winner === 'a') stats[m.b].gamesLost++;
      }
    });
  });

  return poolPlayers.map(p => stats[p]).sort((x, y) => {
    if (y.W !== x.W) return y.W - x.W;
    // BWF General Competition Regulations (GCR 16.2.4):
    // If two teams are tied, the winner of the head-to-head match between them ranks higher.
    if (x.h2h[y.name]) return -x.h2h[y.name];
    const gDiffX = x.gamesWon - x.gamesLost;
    const gDiffY = y.gamesWon - y.gamesLost;
    if (gDiffY !== gDiffX) return gDiffY - gDiffX;
    const ptDiffX = x.ptsWon - x.ptsLost;
    const ptDiffY = y.ptsWon - y.ptsLost;
    if (ptDiffY !== ptDiffX) return ptDiffY - ptDiffX;
    const ratioX = x.ptsWon / Math.max(1, x.ptsLost);
    const ratioY = y.ptsWon / Math.max(1, y.ptsLost);
    if (Math.abs(ratioY - ratioX) > 0.001) return ratioY - ratioX;
    return 0;
  });
}

function renderGroups() {
  const standingsA = computePoolStandings(state.poolA, 'A');
  const standingsB = computePoolStandings(state.poolB, 'B');

  const renderTable = (tbodyId, list) => {
    const el = document.getElementById(tbodyId);
    if (!el) return;
    if (!list.length) {
      el.innerHTML = `<tr><td colspan="6" style="text-align:center;padding:12px;color:var(--clr-text-muted);">No players in pool</td></tr>`;
      return;
    }
    el.innerHTML = list.map((s, idx) => `
      <tr>
        <td style="font-weight:900;color:${idx === 0 ? 'var(--clr-gold)' : 'var(--clr-text-muted)'};">${idx + 1}</td>
        <td><strong>${s.name}</strong></td>
        <td style="color:var(--clr-green);font-weight:bold;">${s.W}</td>
        <td style="color:var(--clr-red);">${s.L}</td>
        <td>${(s.ptsWon - s.ptsLost) > 0 ? '+' : ''}${s.ptsWon - s.ptsLost}</td>
        <td style="font-weight:bold;color:var(--clr-gold);">${s.W * 2}</td>
      </tr>
    `).join('');
  };

  renderTable('poolATableBody', standingsA);
  renderTable('poolBTableBody', standingsB);
  renderGroupMatches();
}

function renderGroupMatches() {
  const container = document.getElementById('groupMatchesContainer');
  if (!container) return;

  const filterCourt = document.getElementById('groupCourtFilter')?.value || 'all';
  let matches = state.matches.filter(m => m.pool === 'A' || m.pool === 'B');
  if (filterCourt !== 'all') {
    matches = matches.filter(m => m.court === parseInt(filterCourt));
  }

  if (!matches.length) {
    container.innerHTML = `
      <div class="card" style="grid-column:1/-1;text-align:center;padding:36px 20px;border:1px solid var(--clr-border);border-radius:var(--radius-md);">
        <div style="width:48px;height:48px;border-radius:50%;background:rgba(16,185,129,0.1);color:var(--clr-green);display:inline-flex;align-items:center;justify-content:center;margin-bottom:12px;border:1px solid rgba(16,185,129,0.25);">
          <svg class="icon icon-md" viewBox="0 0 24 24"><path d="M12 2l3 7h-6l3-7zM7 9l-4 8 7 5 3-4-6-9zM17 9l4 8-7 5-3-4 6-9z"/></svg>
        </div>
        <div style="font-size:1.05rem;font-weight:700;margin-bottom:6px;color:var(--clr-text);">No Tournament Matches Found</div>
        <p style="color:var(--clr-text-muted);font-size:0.84rem;margin-bottom:18px;max-width:420px;margin-left:auto;margin-right:auto;line-height:1.45;">
          No fixtures match the selected court filter, or the tournament has not been generated yet.
        </p>
        <div style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap;">
          <button class="btn btn-primary btn-sm" onclick="quickInitializeDemoTournament()" style="display:inline-flex;align-items:center;gap:6px;">
            <span>🚀 Load Tournament (Rashed + 15 Players)</span>
          </button>
          <button class="btn btn-ghost btn-sm" onclick="handleSetupNav()">
            <span>⚙ Tournament Setup</span>
          </button>
        </div>
      </div>`;
    return;
  }

  container.innerHTML = matches.map(m => {
    const isLive = (m.id === state.currentMatchId);
    const scoreStr = (m.sets && m.sets.length) ? m.sets.map(s => `${s.score[0]}–${s.score[1]}`).join(' | ') : 'VS';
    const winnerName = m.winner ? (m.winner === 'a' ? m.a : m.b) : null;
    return `
      <div class="card" style="padding:16px;border:1.5px solid ${isLive ? 'var(--clr-green)' : (m.winner ? 'rgba(16,185,129,0.3)' : 'var(--clr-border)')};">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;font-size:0.75rem;">
          <span style="font-weight:700;color:var(--clr-text-muted);background:rgba(255,255,255,0.05);padding:3px 8px;border-radius:var(--radius-xs);">
            Pool ${m.pool} · Court ${m.court}
          </span>
          ${isLive ?
            '<span class="status-badge-live badge-game-point" style="display:inline-flex;align-items:center;gap:4px;color:#34d399;font-weight:700;">● LIVE</span>' :
            (m.winner ?
              '<span style="color:var(--clr-green);font-weight:700;font-size:0.72rem;text-transform:uppercase;">COMPLETED</span>' :
              '<span style="color:var(--clr-text-muted);font-size:0.72rem;">UPCOMING</span>'
            )}
        </div>

        <div style="display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:10px;margin-bottom:14px;">
          <div style="text-align:left;">
            <div style="font-weight:800;font-size:1.05rem;color:${m.winner === 'a' ? 'var(--clr-green)' : 'var(--clr-text)'};">${m.a}</div>
            <div style="font-size:0.72rem;color:var(--clr-text-muted);">Team A</div>
          </div>
          <div style="text-align:center;padding:0 8px;">
            <div style="font-family:monospace;font-size:1.1rem;font-weight:800;color:var(--clr-gold);">${m.winner ? scoreStr : 'VS'}</div>
          </div>
          <div style="text-align:right;">
            <div style="font-weight:800;font-size:1.05rem;color:${m.winner === 'b' ? 'var(--clr-green)' : 'var(--clr-text)'};">${m.b}</div>
            <div style="font-size:0.72rem;color:var(--clr-text-muted);">Team B</div>
          </div>
        </div>

        <div class="quick-match-row">
          ${m.winner ? `
            <div style="width:100%;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;">
              <span style="font-size:0.82rem;color:var(--clr-green);font-weight:700;">🏆 Winner: ${winnerName}</span>
              <div style="display:flex;gap:6px;">
                <button class="btn btn-ghost btn-xs" onclick="openScorecardModal('${m.id}')">Scorecard</button>
                <button class="btn btn-ghost btn-xs" onclick="openQuickScoreModal('${m.id}')">Edit Score</button>
              </div>
            </div>
          ` : `
            <button class="quick-win-btn" onclick="awardInstantWinner('a', '${m.id}')" title="Award instant 2-0 win to ${m.a}">
              🏆 ${m.a} Won
            </button>
            <button class="quick-score-btn" onclick="openQuickScoreModal('${m.id}')" title="Enter manual final score">
              ⚡ Score
            </button>
            <button class="quick-win-btn" onclick="awardInstantWinner('b', '${m.id}')" title="Award instant 2-0 win to ${m.b}">
              🏆 ${m.b} Won
            </button>
            <button class="btn btn-secondary btn-xs" onclick="openBettingModal('${m.id}')" title="Place virtual coin prediction on this match">
              🎲 Predict
            </button>
            <button class="btn btn-ghost btn-xs" onclick="startUmpireMatch('${m.id}')" title="Open live court umpire referee">
              🏸 Referee
            </button>
          `}
        </div>
      </div>
    `;
  }).join('');
}

function simulateAllGroupGames() {
  state.matches.filter(m => (m.pool === 'A' || m.pool === 'B') && !m.winner).forEach(m => {
    const aWins = Math.random() > 0.5;
    m.winner = aWins ? 'a' : 'b';
    m.durationSeconds = Math.floor(900 + Math.random() * 900);
    m.sets = [
      { score: aWins ? [state.ptsToWin, Math.floor(state.ptsToWin * 0.75)] : [Math.floor(state.ptsToWin * 0.75), state.ptsToWin], winner: m.winner },
      { score: aWins ? [state.ptsToWin, Math.floor(state.ptsToWin * 0.85)] : [Math.floor(state.ptsToWin * 0.85), state.ptsToWin], winner: m.winner }
    ];
    recordMatchStats(m);
    settleMatchBets(m);
  });

  saveState();
  renderGroups();
  updateGoldenAwards();
  renderAdminDashboard();
  renderPlayerHub();
  showToast('Group matches simulated.');
}

/* ═══════════════════════════════════════════════════
   KNOCKOUT BRACKET GENERATION
═══════════════════════════════════════════════════ */
function generateKnockoutFromGroups() {
  const standingsA = computePoolStandings(state.poolA, 'A');
  const standingsB = computePoolStandings(state.poolB, 'B');

  const topA = standingsA.slice(0, Math.max(1, Math.floor(state.poolA.length / 2))).map(s => s.name);
  const topB = standingsB.slice(0, Math.max(1, Math.floor(state.poolB.length / 2))).map(s => s.name);

  const seeded = [];
  const maxLen = Math.max(topA.length, topB.length);
  for (let i = 0; i < maxLen; i++) {
    if (topA[i]) seeded.push(topA[i]);
    if (topB[maxLen - 1 - i]) seeded.push(topB[maxLen - 1 - i]);
  }

  buildBracketFromRoster(seeded);
  showScreen('knockoutScreen');
  showToast('Knockout bracket generated!');
}

function buildBracketFromRoster(players) {
  let size = 2;
  while (size < players.length) size *= 2;

  const roster = new Array(size).fill(null);
  for (let i = 0; i < players.length; i++) {
    const slot = (i % 2 === 0) ? Math.floor(i / 2) : (size - 1 - Math.floor(i / 2));
    roster[slot] = players[i];
  }
  for (let i = 0; i < size; i++) {
    if (!roster[i]) roster[i] = 'BYE';
  }

  state.matches = state.matches.filter(m => m.pool !== 'KO' && m.pool !== 'BRONZE');
  state.koRounds = [];

  const round1 = [];
  for (let i = 0; i < roster.length; i += 2) {
    const match = createMatchObj(roster[i], roster[i + 1], 'KO');
    if (roster[i] === 'BYE' || roster[i + 1] === 'BYE') {
      match.winner = roster[i] === 'BYE' ? 'b' : 'a';
      match.sets[0].winner = match.winner;
      match.sets[0].score = match.winner === 'a' ? [state.ptsToWin, 0] : [0, state.ptsToWin];
    }
    state.matches.push(match);
    round1.push(match.id);
  }

  state.koRounds.push(round1);
  saveState();
  advanceKnockoutRounds();
  renderBracket();
}

function advanceKnockoutRounds() {
  if (!state.koRounds.length) return;
  const lastRound = state.koRounds[state.koRounds.length - 1];

  if (lastRound.length === 1) {
    const finalMatch = state.matches.find(m => m.id === lastRound[0]);
    if (finalMatch && finalMatch.winner) {
      state.champion = finalMatch.winner === 'a' ? finalMatch.a : finalMatch.b;
      state.runnerUp = finalMatch.winner === 'a' ? finalMatch.b : finalMatch.a;
      recordTournamentChampion();
    }
    return;
  }

  const allCompleted = lastRound.every(id => state.matches.find(m => m.id === id)?.winner);
  if (!allCompleted) return;

  if (lastRound.length === 2 && !state.bronzeMatchId) {
    const semi1 = state.matches.find(m => m.id === lastRound[0]);
    const semi2 = state.matches.find(m => m.id === lastRound[1]);
    const loser1 = semi1.winner === 'a' ? semi1.b : semi1.a;
    const loser2 = semi2.winner === 'a' ? semi2.b : semi2.a;
    const bronzeMatch = createMatchObj(loser1, loser2, 'BRONZE');
    state.matches.push(bronzeMatch);
    state.bronzeMatchId = bronzeMatch.id;
  }

  const nextRound = [];
  for (let i = 0; i < lastRound.length; i += 2) {
    const m1 = state.matches.find(m => m.id === lastRound[i]);
    const m2 = state.matches.find(m => m.id === lastRound[i + 1]);
    const win1 = m1.winner === 'a' ? m1.a : m1.b;
    const win2 = m2.winner === 'a' ? m2.a : m2.b;
    const nextMatch = createMatchObj(win1, win2, 'KO');
    state.matches.push(nextMatch);
    nextRound.push(nextMatch.id);
  }
  state.koRounds.push(nextRound);
  saveState();
}

function renderBracket() {
  const container = document.getElementById('bracketTreeContainer');
  if (!container) return;

  if (!state.koRounds || state.koRounds.length === 0) {
    container.innerHTML = `
      <div class="empty-state-card" style="grid-column:1/-1;width:100%;max-width:540px;margin:30px auto;">
        <div class="empty-state-icon">${svgIcon("swords", "icon-3xl")}</div>
        <div class="empty-state-title">Championship Bracket Not Seeded Yet</div>
        <div class="empty-state-desc">Play or auto-simulate group stage fixtures, then click 'Proceed to Knockout' to seed the single-elimination playoff tree.</div>
        <button class="btn btn-primary btn-sm" onclick="showScreen('groupsScreen')">Go to Group Matches &rarr;</button>
      </div>
    `;
    return;
  }

  let html = '';
  state.koRounds.forEach((roundMatches, roundIdx) => {
    const roundTitle = (roundMatches.length === 1) ? 'Grand Final' :
                       (roundMatches.length === 2) ? 'Semi-Finals' :
                       (roundMatches.length === 4) ? 'Quarter-Finals' : `Round ${roundIdx + 1}`;

    html += `<div class="bracket-round">`;
    html += `<div class="bracket-round-header">${roundTitle}</div>`;

    roundMatches.forEach(matchId => {
      const m = state.matches.find(x => x.id === matchId);
      if (!m) return;
      const scoreA = m.sets.map(s => s.score[0]).join('-');
      const scoreB = m.sets.map(s => s.score[1]).join('-');
      html += `
        <div class="bracket-match-card ${m.winner ? 'completed' : ''}">
          <div class="bracket-team-row ${m.winner === 'a' ? 'winner' : ''}">
            <span>${m.a}</span>
            <span>${scoreA}</span>
          </div>
          <div class="bracket-team-row ${m.winner === 'b' ? 'winner' : ''}">
            <span>${m.b}</span>
            <span>${scoreB}</span>
          </div>
          ${!m.winner && m.a !== 'BYE' && m.b !== 'BYE' ?
            `<button class="btn btn-primary btn-xs" style="width:100%;margin-top:8px;" onclick="startUmpireMatch('${m.id}')">Start Match &rarr;</button>` : ''
          }
        </div>
      `;
    });
    html += `</div>`;
  });

  if (state.bronzeMatchId) {
    const bm = state.matches.find(m => m.id === state.bronzeMatchId);
    if (bm) {
      const scoreA = bm.sets.map(s => s.score[0]).join('-');
      const scoreB = bm.sets.map(s => s.score[1]).join('-');
      html += `
        <div class="bracket-round">
          <div class="bracket-round-header" style="color:var(--clr-bronze);">3rd Place Playoff</div>
          <div class="bracket-match-card ${bm.winner ? 'completed' : ''}">
            <div class="bracket-team-row ${bm.winner === 'a' ? 'winner' : ''}">
              <span>${bm.a}</span>
              <span>${scoreA}</span>
            </div>
            <div class="bracket-team-row ${bm.winner === 'b' ? 'winner' : ''}">
              <span>${bm.b}</span>
              <span>${scoreB}</span>
            </div>
            ${!bm.winner ? `<button class="btn btn-primary btn-xs" style="width:100%;margin-top:8px;" onclick="startUmpireMatch('${bm.id}')">Play Bronze &rarr;</button>` : ''}
          </div>
        </div>
      `;
    }
  }

  container.innerHTML = html;
}

function simulateAllKnockout() {
  state.matches.filter(m => (m.pool === 'KO' || m.pool === 'BRONZE') && !m.winner && m.a !== 'BYE' && m.b !== 'BYE').forEach(m => {
    const aWins = Math.random() > 0.5;
    m.winner = aWins ? 'a' : 'b';
    m.durationSeconds = Math.floor(1200 + Math.random() * 800);
    m.sets = [
      { score: aWins ? [state.ptsToWin, Math.floor(state.ptsToWin * 0.8)] : [Math.floor(state.ptsToWin * 0.8), state.ptsToWin], winner: m.winner },
      { score: aWins ? [state.ptsToWin, Math.floor(state.ptsToWin * 0.9)] : [Math.floor(state.ptsToWin * 0.9), state.ptsToWin], winner: m.winner }
    ];
    recordMatchStats(m);
    settleMatchBets(m);

    if (m.pool === 'BRONZE') {
      state.thirdPlace = aWins ? m.a : m.b;
    }
  });

  advanceKnockoutRounds();
  saveState();
  renderBracket();
  updateGoldenAwards();
  renderAdminDashboard();
  renderPlayerHub();
  showToast('Knockout matches resolved.');
}

/* ═══════════════════════════════════════════════════
   SCREEN WAKE LOCK (KEEP UMPIRE TABLET ACTIVE)
═══════════════════════════════════════════════════ */
let wakeLockSentinel = null;
async function acquireWakeLock() {
  try {
    if ('wakeLock' in navigator && !wakeLockSentinel) {
      wakeLockSentinel = await navigator.wakeLock.request('screen');
      wakeLockSentinel.addEventListener('release', () => {
        wakeLockSentinel = null;
      });
    }
  } catch (e) {}
}

function releaseWakeLock() {
  if (wakeLockSentinel) {
    wakeLockSentinel.release().catch(() => {});
    wakeLockSentinel = null;
  }
}

/* ═══════════════════════════════════════════════════
   LIVE UMPIRE SCOREBOARD
═══════════════════════════════════════════════════ */
function startUmpireMatch(matchId) {
  const match = state.matches.find(m => m.id === matchId);
  if (!match) return;

  state.currentMatchId = matchId;
  state.currentSetIdx = match.sets.length - 1;
  state.servingSide = 'a';
  state.endsSwitchedInDecidingSet = false;

  if (state.category === 'doubles') {
    const splitA = match.a.split('/').map(s => s.trim());
    const splitB = match.b.split('/').map(s => s.trim());
    state.doublesPositions = {
      a: { right: splitA[0] || match.a, left: splitA[1] || match.a },
      b: { right: splitB[0] || match.b, left: splitB[1] || match.b }
    };
  }

  acquireWakeLock();
  startStopwatch();
  updateLiveScoreboardUI();
  showScreen('liveUmpireScreen');
  playSound('point');
}

function startStopwatch() {
  if (state.stopwatchInterval) clearInterval(state.stopwatchInterval);
  state.matchStartTime = Date.now();
  state.stopwatchInterval = setInterval(() => {
    const elapsed = Math.floor((Date.now() - state.matchStartTime) / 1000);
    const m = Math.floor(elapsed / 60).toString().padStart(2, '0');
    const s = (elapsed % 60).toString().padStart(2, '0');
    const clock = document.getElementById('matchDurationClock');
    if (clock) clock.textContent = `${m}:${s}`;
  }, 1000);
}

function toggleCourtFlip() {
  state.courtFlipped = !state.courtFlipped;
  const container = document.getElementById('courtContainer');
  if (container) {
    container.classList.toggle('court-flipped', state.courtFlipped);
  }
  showToast(state.courtFlipped ? 'Court Display Flipped 180°' : 'Court Display Standard');
}

function updateLiveScoreboardUI() {
  const match = state.matches.find(m => m.id === state.currentMatchId);
  if (!match) return;

  const currentSet = match.sets[state.currentSetIdx];
  document.getElementById('nameSideA').textContent = match.a;
  document.getElementById('nameSideB').textContent = match.b;
  document.getElementById('scoreDigitA').textContent = currentSet.score[0];
  document.getElementById('scoreDigitB').textContent = currentSet.score[1];
  document.getElementById('currentSetNumber').textContent = state.currentSetIdx + 1;

  document.getElementById('panelSideA').classList.toggle('serving', state.servingSide === 'a');
  document.getElementById('panelSideB').classList.toggle('serving', state.servingSide === 'b');

  document.getElementById('umpireMatchHeader').textContent =
    `Court ${match.court || 1} · ${match.pool === 'KO' ? 'Knockout Match' : `Pool ${match.pool || 'Stage'}`} · ${match.a} vs ${match.b}`;

  renderSetPips(match);
  updateCourtVisualizer(currentSet);
  updateLiveStatusBadges(match, currentSet);
  renderMatchRallyLog(match);
}

function renderSetPips(match) {
  const setsNeeded = Math.ceil(state.bestOf / 2);
  const wonA = getMatchSetsWon(match, 'a');
  const wonB = getMatchSetsWon(match, 'b');

  const pipsA = document.getElementById('pipsA');
  const pipsB = document.getElementById('pipsB');
  if (pipsA) pipsA.innerHTML = Array.from({ length: setsNeeded }, (_, i) => `<span class="set-pip ${i < wonA ? 'won' : ''}"></span>`).join('');
  if (pipsB) pipsB.innerHTML = Array.from({ length: setsNeeded }, (_, i) => `<span class="set-pip ${i < wonB ? 'won' : ''}"></span>`).join('');
}

function getMatchSetsWon(match, side) {
  return match.sets.filter(s => s.winner === side).length;
}

function updateCourtVisualizer(currentSet) {
  ['courtA_left', 'courtA_right', 'courtB_left', 'courtB_right'].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.className = 'court-box';
  });

  const serverScore = state.servingSide === 'a' ? currentSet.score[0] : currentSet.score[1];
  const isEven = (serverScore % 2 === 0);

  const serverBoxId = state.servingSide === 'a' ? (isEven ? 'courtA_right' : 'courtA_left') : (isEven ? 'courtB_right' : 'courtB_left');
  const receiverBoxId = state.servingSide === 'a' ? (isEven ? 'courtB_right' : 'courtB_left') : (isEven ? 'courtA_right' : 'courtA_left');

  const serverBox = document.getElementById(serverBoxId);
  const receiverBox = document.getElementById(receiverBoxId);

  if (serverBox) serverBox.classList.add('active-service');
  if (receiverBox) receiverBox.classList.add('active-receiver');

  const match = state.matches.find(m => m.id === state.currentMatchId);
  if (state.category === 'doubles') {
    document.getElementById('posA_right').textContent = state.doublesPositions.a.right;
    document.getElementById('posA_left').textContent = state.doublesPositions.a.left;
    document.getElementById('posB_right').textContent = state.doublesPositions.b.right;
    document.getElementById('posB_left').textContent = state.doublesPositions.b.left;

    const serverPlayer = state.doublesPositions[state.servingSide][isEven ? 'right' : 'left'];
    const oppSide = state.servingSide === 'a' ? 'b' : 'a';
    const receiverPlayer = state.doublesPositions[oppSide][isEven ? 'right' : 'left'];

    document.getElementById('serviceCalloutText').textContent =
      `Server: ${serverPlayer} (${isEven ? 'Right Court' : 'Left Court'})`;
    document.getElementById('serviceReceiverCallout').textContent =
      `Diagonal Receiver: ${receiverPlayer}`;
  } else {
    if (state.servingSide === 'a') {
      document.getElementById('posA_right').textContent = isEven ? match.a : '';
      document.getElementById('posA_left').textContent = isEven ? '' : match.a;
      document.getElementById('posB_right').textContent = isEven ? match.b : '';
      document.getElementById('posB_left').textContent = isEven ? '' : match.b;
    } else {
      document.getElementById('posB_right').textContent = isEven ? match.b : '';
      document.getElementById('posB_left').textContent = isEven ? '' : match.b;
      document.getElementById('posA_right').textContent = isEven ? match.a : '';
      document.getElementById('posA_left').textContent = isEven ? '' : match.a;
    }

    const servingPlayer = state.servingSide === 'a' ? match.a : match.b;
    document.getElementById('serviceCalloutText').textContent =
      `Serving: ${servingPlayer} from ${isEven ? 'RIGHT (Even)' : 'LEFT (Odd)'} Court`;
    document.getElementById('serviceReceiverCallout').textContent = '';
  }
}

function updateLiveStatusBadges(match, set) {
  const banner = document.getElementById('liveStatusBanner');
  if (!banner) return;

  const [scoreA, scoreB] = set.score;
  const pts = state.ptsToWin;

  if (scoreA === 29 && scoreB === 29) {
    banner.innerHTML = `<span class="status-badge-live badge-sudden-death">${svgIcon('zap', 'icon-xs')} SUDDEN DEATH · 30TH POINT WINS</span>`;
  } else if (scoreA >= pts - 1 && scoreB >= pts - 1 && scoreA === scoreB) {
    banner.innerHTML = `<span class="status-badge-live badge-deuce">DEUCE · 2-POINT LEAD REQUIRED</span>`;
  } else if ((scoreA >= pts - 1 || scoreB >= pts - 1) && Math.abs(scoreA - scoreB) >= 1) {
    const leader = scoreA > scoreB ? 'a' : 'b';
    const wonSoFar = getMatchSetsWon(match, leader);
    const setsNeeded = Math.ceil(state.bestOf / 2);
    if (wonSoFar + 1 >= setsNeeded) {
      banner.innerHTML = `<span class="status-badge-live badge-match-point">${svgIcon('dot')} MATCH POINT (${scoreA > scoreB ? match.a : match.b})</span>`;
    } else {
      banner.innerHTML = `<span class="status-badge-live badge-game-point">${svgIcon('shuttle', 'icon-xs')} GAME POINT (${scoreA > scoreB ? match.a : match.b})</span>`;
    }
  } else {
    banner.innerHTML = '';
  }
}

function scorePoint(side) {
  const match = state.matches.find(m => m.id === state.currentMatchId);
  if (!match || match.winner) return;

  const set = match.sets[state.currentSetIdx];
  if (set.winner) return;

  state.undoStack.push(JSON.parse(JSON.stringify({
    sets: match.sets,
    setIdx: state.currentSetIdx,
    servingSide: state.servingSide,
    doublesPositions: state.doublesPositions,
    winner: match.winner,
    endsSwitchedInDecidingSet: state.endsSwitchedInDecidingSet,
    courtFlipped: state.courtFlipped
  })));

  if ('vibrate' in navigator) navigator.vibrate(30);
  playSound('point');

  if (state.category === 'doubles' && state.servingSide === side) {
    const p = state.doublesPositions[side];
    const tmp = p.right;
    p.right = p.left;
    p.left = tmp;
  }

  const idx = side === 'a' ? 0 : 1;
  set.score[idx]++;
  state.servingSide = side;

  if (!match.history) match.history = [];
  match.history.push({
    set: state.currentSetIdx + 1,
    score: [set.score[0], set.score[1]],
    scorer: side === 'a' ? match.a : match.b,
    time: new Date().toLocaleTimeString()
  });

  const el = document.getElementById(side === 'a' ? 'scoreDigitA' : 'scoreDigitB');
  if (el) {
    el.classList.add('pop');
    setTimeout(() => el.classList.remove('pop'), 160);
  }

  const isDecidingSet = (state.bestOf === 3 && state.currentSetIdx === 2) || (state.bestOf === 5 && state.currentSetIdx === 4);
  const midpoint = Math.ceil(state.ptsToWin / 2);
  if (isDecidingSet && !state.endsSwitchedInDecidingSet && (set.score[0] >= midpoint || set.score[1] >= midpoint)) {
    state.endsSwitchedInDecidingSet = true;
    triggerEndsSwitch();
  }

  if ((set.score[0] === 11 || set.score[1] === 11) && Math.max(set.score[0], set.score[1]) === 11) {
    triggerIntervalTimer(60);
  }

  evaluateSetStatus(match, set);
  updateLiveScoreboardUI();
  saveState();
  broadcastStateChange();
  speakScoreAnnouncement();
  const annEl = document.getElementById('ariaLiveAnnouncer');
  if (annEl) {
    const curS = match.sets[state.currentSetIdx];
    annEl.textContent = `Score: ${match.a} ${curS.score[0]}, ${match.b} ${curS.score[1]}. Serving: ${state.servingSide === 'a' ? match.a : match.b}`;
  }
}

function undoPoint() {
  if (!state.undoStack.length) {
    showToast('Nothing to undo.');
    return;
  }
  const prev = state.undoStack.pop();
  const match = state.matches.find(m => m.id === state.currentMatchId);
  match.sets = prev.sets;
  match.winner = prev.winner;
  state.currentSetIdx = prev.setIdx;
  state.servingSide = prev.servingSide;
  if (prev.doublesPositions) {
    state.doublesPositions = JSON.parse(JSON.stringify(prev.doublesPositions));
  }
  if (prev.endsSwitchedInDecidingSet !== undefined) {
    state.endsSwitchedInDecidingSet = prev.endsSwitchedInDecidingSet;
  }
  if (prev.courtFlipped !== undefined && prev.courtFlipped !== state.courtFlipped) {
    state.courtFlipped = prev.courtFlipped;
    const cont = document.getElementById('courtContainer');
    if (cont) cont.classList.toggle('court-flipped', state.courtFlipped);
  }

  if (match.history && match.history.length) match.history.pop();

  updateLiveScoreboardUI();
  saveState();
  broadcastStateChange();
  showToast('Rally undone.');
  const ann = document.getElementById('ariaLiveAnnouncer');
  if (ann) ann.textContent = 'Rally undone.';
}

function evaluateSetStatus(match, set) {
  const [scoreA, scoreB] = set.score;
  const pts = state.ptsToWin;
  const maxCap = (pts === 21) ? 30 : (pts === 11 ? 15 : pts + 5);

  let setWinner = null;
  if (scoreA >= pts && scoreA - scoreB >= 2) setWinner = 'a';
  else if (scoreB >= pts && scoreB - scoreA >= 2) setWinner = 'b';
  else if (scoreA === maxCap) setWinner = 'a';
  else if (scoreB === maxCap) setWinner = 'b';

  if (setWinner) {
    set.winner = setWinner;
    const winnerName = setWinner === 'a' ? match.a : match.b;
    showToast(`${winnerName} won Set ${state.currentSetIdx + 1}!`);
    playSound('win');

    const setsNeeded = Math.ceil(state.bestOf / 2);
    const wonA = getMatchSetsWon(match, 'a');
    const wonB = getMatchSetsWon(match, 'b');

    if (wonA >= setsNeeded || wonB >= setsNeeded) {
      match.winner = wonA >= setsNeeded ? 'a' : 'b';
      if (state.stopwatchInterval) clearInterval(state.stopwatchInterval);
      if (state.matchStartTime) {
        match.durationSeconds = Math.floor((Date.now() - state.matchStartTime) / 1000);
      }
      showWinCelebrationModal(match);
      recordMatchStats(match);
      settleMatchBets(match);
      if (match.pool === 'BRONZE') {
        state.thirdPlace = match.winner === 'a' ? match.a : match.b;
      }
      renderAdminDashboard();
      renderPlayerHub();
    } else {
      triggerIntervalTimer(120);
      match.sets.push({ score: [0, 0], winner: null });
      state.currentSetIdx = match.sets.length - 1;
      state.servingSide = setWinner;
    }
  }
}

function openWalkoverModal(type) {
  activeWalkoverType = type;
  const match = state.matches.find(m => m.id === state.currentMatchId);
  if (!match) return;

  const title = document.getElementById('walkoverModalTitle');
  const desc = document.getElementById('walkoverModalDesc');
  const roleA = document.getElementById('walkoverRoleA');
  const roleB = document.getElementById('walkoverRoleB');

  document.getElementById('walkoverNameA').textContent = match.a;
  document.getElementById('walkoverNameB').textContent = match.b;

  if (type === 'yellow') {
    title.innerHTML = '<span style="display:inline-block;width:10px;height:14px;background:#f59e0b;border-radius:2px;vertical-align:-2px;margin-right:6px;"></span> Official Umpire Warning';
    desc.textContent = 'Select which side receives the yellow card warning.';
    roleA.textContent = 'Issue Warning to Side A';
    roleB.textContent = 'Issue Warning to Side B';
  } else if (type === 'red') {
    title.innerHTML = '<span style="display:inline-block;width:10px;height:14px;background:#ef4444;border-radius:2px;vertical-align:-2px;margin-right:6px;"></span> Red Card Penalty Point';
    desc.textContent = 'Select which side committed the fault. Opponent will be awarded 1 penalty point.';
    roleA.textContent = 'Fault by Side A (+1 Pt to B)';
    roleB.textContent = 'Fault by Side B (+1 Pt to A)';
  } else if (type === 'black') {
    title.textContent = '⬛ Black Card (Disqualification)';
    desc.textContent = 'Select which side is disqualified. Opponent will be awarded the match.';
    roleA.textContent = 'Disqualify Side A (B Wins)';
    roleB.textContent = 'Disqualify Side B (A Wins)';
  } else if (type === 'wo') {
    title.textContent = 'Walkover / Forfeit Concession (W.O.)';
    desc.textContent = 'Select which side is forfeiting the match.';
    roleA.textContent = 'Side A Forfeits (B Wins)';
    roleB.textContent = 'Side B Forfeits (A Wins)';
  }

  document.getElementById('walkoverModal').showModal();
}

function confirmWalkoverSelection(offendingSide) {
  document.getElementById('walkoverModal').close();
  const match = state.matches.find(m => m.id === state.currentMatchId);
  if (!match) return;

  const nonOffendingSide = offendingSide === 'a' ? 'b' : 'a';

  const offendingName = offendingSide === 'a' ? match.a : match.b;
  if (!match.cards) match.cards = [];
  match.cards.push({
    type: activeWalkoverType,
    player: offendingName,
    set: state.currentSetIdx + 1,
    time: new Date().toLocaleTimeString()
  });

  if (activeWalkoverType === 'yellow') {
    showToast(`Yellow Card (Warning) issued to ${offendingName} (BWF Law 16).`);
    logAdminAudit(`Issued Yellow Card to ${offendingName} in Match ${match.id}`);
  } else if (activeWalkoverType === 'red') {
    showToast(`Red Card (Fault Point) on ${offendingName}! +1 penalty point to opponent.`);
    logAdminAudit(`Issued Red Card to ${offendingName} in Match ${match.id}`);
    scorePoint(nonOffendingSide);
  } else if (activeWalkoverType === 'black' || activeWalkoverType === 'wo') {
    const isBlack = (activeWalkoverType === 'black');
    logAdminAudit(`Issued ${isBlack ? 'Black Card (Disqualification)' : 'Walkover Forfeit'} to ${offendingName}`);
    showToast(`${isBlack ? 'Black Card Disqualification' : 'Walkover Forfeit'} recorded for ${offendingName}.`);
    match.winner = nonOffendingSide;
    const setsNeeded = Math.ceil(state.bestOf / 2);
    while (getMatchSetsWon(match, nonOffendingSide) < setsNeeded) {
      if (!match.sets[state.currentSetIdx]) {
        match.sets.push({ score: [0, 0], winner: null });
      }
      const cur = match.sets[state.currentSetIdx];
      cur.winner = nonOffendingSide;
      cur.score = nonOffendingSide === 'a' ? [state.ptsToWin, 0] : [0, state.ptsToWin];
      state.currentSetIdx++;
    }
    state.currentSetIdx = match.sets.length - 1;

    if (state.stopwatchInterval) clearInterval(state.stopwatchInterval);
    if (state.matchStartTime) {
      match.durationSeconds = Math.floor((Date.now() - state.matchStartTime) / 1000);
    }

    recordMatchStats(match);
    settleMatchBets(match);
    saveState();
    broadcastStateChange();
    showWinCelebrationModal(match);
  }
}

function triggerIntervalTimer(seconds) {
  if (state.intervalTimer) clearInterval(state.intervalTimer);
  const overlay = document.getElementById('intervalTimerOverlay');
  const disp = document.getElementById('intervalSecondsDisplay');
  overlay.style.display = 'block';

  let remaining = seconds;
  disp.textContent = `${remaining}s`;

  state.intervalTimer = setInterval(() => {
    remaining--;
    disp.textContent = `${remaining}s`;
    if (remaining <= 0) {
      clearInterval(state.intervalTimer);
      overlay.style.display = 'none';
      if (appSettings.buzzerEnabled) playSound('buzzer');
      showToast('Interval ended! Athletes report back to court.');
    }
  }, 1000);
}

function dismissInterval() {
  if (state.intervalTimer) clearInterval(state.intervalTimer);
  document.getElementById('intervalTimerOverlay').style.display = 'none';
}

function toggleServerManual() {
  state.servingSide = state.servingSide === 'a' ? 'b' : 'a';
  updateLiveScoreboardUI();
  playSound('point');
  showToast(`⇄ Serve switched to ${state.servingSide.toUpperCase()}`);
}

function triggerEndsSwitch() {
  state.courtFlipped = !state.courtFlipped;
  const container = document.getElementById('courtContainer');
  if (container) {
    container.classList.toggle('court-flipped', state.courtFlipped);
  }
  showToast('Switch Ends: Players swap court sides (BWF Law 8).');
  playSound('point');
  speakUmpire('Change ends');
  const ann = document.getElementById('ariaLiveAnnouncer');
  if (ann) ann.textContent = 'Change ends. Players swap court sides.';
}

function renderMatchRallyLog(match) {
  const container = document.getElementById('matchRallyLog');
  if (!container) return;
  if (!match.history || !match.history.length) {
    container.innerHTML = `<div>No rallies logged for this match yet.</div>`;
    return;
  }
  container.innerHTML = match.history.slice(-15).reverse().map(h => `
    <div>Set ${h.set} · <strong>${h.scorer}</strong> scored &rarr; ${h.score[0]}–${h.score[1]} <span style="font-size:0.75rem;opacity:0.7;">(${h.time})</span></div>
  `).join('');
}

function showWinCelebrationModal(match) {
  const dlg = document.getElementById('matchWinModal');
  const winnerName = match.winner === 'a' ? match.a : match.b;
  document.getElementById('winSubtitle').textContent = `${winnerName} wins the match!`;
  document.getElementById('winScoreSummary').textContent =
    match.sets.filter(s => s.winner).map(s => `${s.score[0]}–${s.score[1]}`).join(' | ');

  triggerVictoryConfetti();
  dlg.showModal();
}

function closeWinModal() {
  document.getElementById('matchWinModal').close();
  exitLiveScoreboard();
}

function advanceToNextMatch() {
  document.getElementById('matchWinModal').close();
  exitLiveScoreboard();

  const next = state.matches.find(m => !m.winner && m.a !== 'BYE' && m.b !== 'BYE');
  if (next) {
    startUmpireMatch(next.id);
  } else {
    showToast('All scheduled matches completed!');
  }
}

function exitLiveScoreboard() {
  releaseWakeLock();
  if (state.stopwatchInterval) clearInterval(state.stopwatchInterval);
  if (state.intervalTimer) clearInterval(state.intervalTimer);

  if (state.champion) {
    showScreen('championScreen');
    document.getElementById('championNameBanner').textContent = state.champion;
    document.getElementById('podiumGoldName').textContent = state.champion;
    document.getElementById('podiumSilverName').textContent = state.runnerUp || 'Runner-Up';
    document.getElementById('podiumBronzeName').textContent = state.thirdPlace || '3rd Place';
  } else if (state.koRounds.length > 0) {
    showScreen('knockoutScreen');
  } else {
    showScreen('groupsScreen');
  }
  refreshCurrentViews();
}

function triggerVictoryConfetti() {
  if (typeof confetti === 'function') {
    confetti({ particleCount: 120, spread: 80, origin: { y: 0.6 } });
  }
}

/* ═══════════════════════════════════════════════════
   GOLDEN AWARDS
═══════════════════════════════════════════════════ */
function updateGoldenAwards() {
  const rLeader = document.getElementById('goldenRacketLeader');
  const rStats = document.getElementById('goldenRacketStats');
  const gLeader = document.getElementById('goldenGloveLeader');
  const gStats = document.getElementById('goldenGloveStats');
  if (!rLeader || !gLeader) return;

  const pointsScored = {};
  const pointsConceded = {};
  const matchesCount = {};

  let allPlayers = [...state.poolA, ...state.poolB];
  if (!allPlayers.length && state.matches.length) {
    const set = new Set();
    state.matches.forEach(m => {
      if (m.a && m.a !== 'BYE') set.add(m.a);
      if (m.b && m.b !== 'BYE') set.add(m.b);
    });
    allPlayers = Array.from(set);
  }

  allPlayers.forEach(p => {
    pointsScored[p] = 0;
    pointsConceded[p] = 0;
    matchesCount[p] = 0;
  });

  state.matches.filter(m => m.winner).forEach(m => {
    if (matchesCount[m.a] !== undefined) matchesCount[m.a]++;
    if (matchesCount[m.b] !== undefined) matchesCount[m.b]++;

    m.sets.forEach(s => {
      if (pointsScored[m.a] !== undefined) {
        pointsScored[m.a] += (s.score[0] || 0);
        pointsConceded[m.a] += (s.score[1] || 0);
      }
      if (pointsScored[m.b] !== undefined) {
        pointsScored[m.b] += (s.score[1] || 0);
        pointsConceded[m.b] += (s.score[0] || 0);
      }
    });
  });

  let bestRacket = 'None';
  let maxPts = 0;
  Object.keys(pointsScored).forEach(p => {
    if (pointsScored[p] > maxPts) {
      maxPts = pointsScored[p];
      bestRacket = p;
    }
  });

  let bestGlove = 'None';
  let minConcededAvg = 999;
  Object.keys(pointsConceded).forEach(p => {
    if (matchesCount[p] > 0) {
      const avg = pointsConceded[p] / matchesCount[p];
      if (avg < minConcededAvg) {
        minConcededAvg = avg;
        bestGlove = p;
      }
    }
  });

  rLeader.textContent = bestRacket;
  rStats.textContent = `${maxPts} smash points scored`;

  gLeader.textContent = bestGlove;
  gStats.textContent = (minConcededAvg === 999) ? '0.0 points conceded' : `${minConcededAvg.toFixed(1)} points conceded / match`;
}

/* ═══════════════════════════════════════════════════
   VICTORY POSTER GENERATOR
═══════════════════════════════════════════════════ */
async function openSharePosterModal() {
  const canvas = document.getElementById('victoryShareCanvas');
  const ctx = canvas.getContext('2d');

  if (document.fonts) {
    try { await document.fonts.ready; } catch (e) {}
  }

  const dpr = window.devicePixelRatio || 1;
  canvas.width = 1200 * dpr;
  canvas.height = 1200 * dpr;
  ctx.scale(dpr, dpr);

  const bgGrad = ctx.createLinearGradient(0, 0, 1200, 1200);
  bgGrad.addColorStop(0, '#091e14');
  bgGrad.addColorStop(0.5, '#05110a');
  bgGrad.addColorStop(1, '#020704');
  ctx.fillStyle = bgGrad;
  ctx.fillRect(0, 0, 1200, 1200);

  ctx.strokeStyle = '#f59e0b';
  ctx.lineWidth = 16;
  ctx.strokeRect(32, 32, 1136, 1136);

  ctx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
  ctx.lineWidth = 2;
  ctx.strokeRect(48, 48, 1104, 1104);

  ctx.strokeStyle = 'rgba(34, 197, 94, 0.2)';
  ctx.lineWidth = 4;
  ctx.beginPath();
  ctx.moveTo(100, 600);
  ctx.lineTo(1100, 600);
  ctx.moveTo(600, 200);
  ctx.lineTo(600, 1000);
  ctx.stroke();

  ctx.textAlign = 'center';
  ctx.fillStyle = '#22c55e';
  ctx.font = 'bold 36px "Inter", sans-serif';
  ctx.fillText('OFFICIAL BWF TOURNAMENT POSTER', 600, 140);

  ctx.fillStyle = '#ffffff';
  ctx.font = '900 64px "Anton", sans-serif';
  ctx.fillText((state.title || 'THE BADMINTON CUP').toUpperCase(), 600, 230);

  ctx.font = '140px sans-serif';
  ctx.fillText('CHAMPION', 600, 420);

  ctx.fillStyle = '#f59e0b';
  ctx.font = 'bold 38px "Inter", sans-serif';
  ctx.fillText('TOURNAMENT CHAMPION', 600, 520);

  const champName = (state.champion || 'VICTORIOUS ATHLETE').toUpperCase();
  let champFontSize = 82;
  ctx.font = `900 ${champFontSize}px "Anton", sans-serif`;
  while (ctx.measureText(champName).width > 960 && champFontSize > 36) {
    champFontSize -= 4;
    ctx.font = `900 ${champFontSize}px "Anton", sans-serif`;
  }
  ctx.fillStyle = '#ffffff';
  ctx.fillText(champName, 600, 620);

  ctx.fillStyle = '#94a3b8';
  ctx.font = 'bold 34px "Inter", sans-serif';
  ctx.fillText(`Runner-Up: ${state.runnerUp || 'Silver Medalist'}`, 600, 720);
  if (state.thirdPlace) {
    ctx.fillStyle = '#cd7f32';
    ctx.fillText(`3rd Place: ${state.thirdPlace}`, 600, 775);
  }

  ctx.fillStyle = 'rgba(255, 255, 255, 0.05)';
  ctx.fillRect(150, 840, 900, 180);
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
  ctx.lineWidth = 2;
  ctx.strokeRect(150, 840, 900, 180);

  ctx.fillStyle = '#fde68a';
  ctx.font = 'bold 30px "Inter", sans-serif';
  ctx.fillText('INDIVIDUAL HONOURS', 600, 890);

  ctx.fillStyle = '#ffffff';
  ctx.font = '26px "Inter", sans-serif';
  const rLead = document.getElementById('goldenRacketLeader')?.textContent || '';
  const gLead = document.getElementById('goldenGloveLeader')?.textContent || '';
  ctx.fillText(`Golden Racket: ${rLead.replace('Leader: ', '') || 'Top Smashing Athlete'}`, 600, 940);
  ctx.fillText(`Iron Net: ${gLead.replace('Leader: ', '') || 'Best Defense Record'}`, 600, 985);

  ctx.fillStyle = '#64748b';
  ctx.font = '600 24px "Inter", sans-serif';
  ctx.fillText(`Generated on ${new Date().toLocaleDateString()} · BWF Verified Tournament Suite`, 600, 1080);

  document.getElementById('shareCanvasModal').showModal();
}

function downloadVictoryPoster() {
  const canvas = document.getElementById('victoryShareCanvas');
  const a = document.createElement('a');
  a.download = `badminton_cup_victory_${Date.now()}.png`;
  a.href = canvas.toDataURL('image/png');
  a.click();
  showToast('Victory poster downloaded!');
}

async function copyVictoryPosterToClipboard() {
  const canvas = document.getElementById('victoryShareCanvas');
  if (canvas.toBlob && navigator.clipboard && window.ClipboardItem) {
    try {
      canvas.toBlob(async blob => {
        const item = new ClipboardItem({ 'image/png': blob });
        await navigator.clipboard.write([item]);
        showToast('Poster copied to clipboard!');
      });
    } catch (e) {
      showToast('Clipboard copy not supported by browser.');
    }
  } else {
    showToast('Clipboard copy unavailable.');
  }
}

async function shareVictoryPosterOS() {
  const canvas = document.getElementById('victoryShareCanvas');
  if (navigator.share && canvas.toBlob) {
    canvas.toBlob(async blob => {
      const file = new File([blob], 'victory_poster.png', { type: 'image/png' });
      try {
        await navigator.share({
          title: state.title,
          text: `Tournament Champion: ${state.champion}!`,
          files: [file]
        });
      } catch (err) {}
    });
  } else {
    downloadVictoryPoster();
  }
}

/* ═══════════════════════════════════════════════════
   HEAD-TO-HEAD (H2H) COMPARISON
═══════════════════════════════════════════════════ */
function openH2HModal(playerA, playerB) {
  const modal = document.getElementById('h2hModal');
  const body = document.getElementById('h2hModalBody');

  const encounters = state.matches.filter(m =>
    m.winner && ((m.a === playerA && m.b === playerB) || (m.a === playerB && m.b === playerA))
  );

  let winsA = 0;
  let winsB = 0;
  let ptsA = 0;
  let ptsB = 0;

  encounters.forEach(m => {
    const isMainA = (m.a === playerA);
    if (m.winner === (isMainA ? 'a' : 'b')) winsA++; else winsB++;
    m.sets.forEach(s => {
      ptsA += (isMainA ? s.score[0] : s.score[1]);
      ptsB += (isMainA ? s.score[1] : s.score[0]);
    });
  });

  body.innerHTML = `
    <div style="display:grid;grid-template-columns:1fr auto 1fr;gap:16px;align-items:center;margin-bottom:20px;text-align:center;">
      <div style="background:rgba(59,130,246,0.12);padding:14px;border-radius:var(--radius-sm);border:1px solid #3b82f6;">
        <div style="font-weight:900;font-size:1.1rem;color:#93c5fd;">${playerA}</div>
        <div style="font-family:'Anton',sans-serif;font-size:2.2rem;color:#fff;">${winsA}</div>
        <div style="font-size:0.75rem;color:var(--clr-text-muted);">${ptsA} Total Points</div>
      </div>
      <div style="font-size:1.2rem;font-weight:900;color:var(--clr-text-muted);">VS</div>
      <div style="background:rgba(239,68,68,0.12);padding:14px;border-radius:var(--radius-sm);border:1px solid #ef4444;">
        <div style="font-weight:900;font-size:1.1rem;color:#fca5a5;">${playerB}</div>
        <div style="font-family:'Anton',sans-serif;font-size:2.2rem;color:#fff;">${winsB}</div>
        <div style="font-size:0.75rem;color:var(--clr-text-muted);">${ptsB} Total Points</div>
      </div>
    </div>
    <div style="font-weight:bold;margin-bottom:8px;">Past Match Results (${encounters.length}):</div>
    <div style="max-height:160px;overflow-y:auto;display:flex;flex-direction:column;gap:6px;">
      ${encounters.length ? encounters.map(m => `
        <div style="background:rgba(0,0,0,0.25);padding:8px 12px;border-radius:4px;display:flex;justify-content:space-between;font-size:0.85rem;">
          <span>${m.pool === 'KO' ? 'Knockout' : `Pool ${m.pool}`} · Won by <strong>${m.winner === 'a' ? m.a : m.b}</strong></span>
          <span style="font-family:monospace;color:var(--clr-gold);">${m.sets.map(s => `${s.score[0]}-${s.score[1]}`).join(' | ')}</span>
        </div>
      `).join('') : '<div style="color:var(--clr-text-muted);">No recorded past matches between these athletes yet.</div>'}
    </div>
  `;

  modal.showModal();
}

/* ═══════════════════════════════════════════════════
   GLOBAL STATS & LEADERBOARD
═══════════════════════════════════════════════════ */
function getLeaderboardDB() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY_STATS)) || {};
  } catch (e) { return {}; }
}
function saveLeaderboardDB(db) {
  try {
    localStorage.setItem(STORAGE_KEY_STATS, JSON.stringify(db));
  } catch (e) {}
}

function recordMatchStats(match) {
  const db = getLeaderboardDB();
  const winner = match.winner === 'a' ? match.a : match.b;
  const loser = match.winner === 'a' ? match.b : match.a;

  [winner, loser].forEach(name => {
    if (!db[name]) {
      db[name] = { name, gold: 0, silver: 0, bronze: 0, won: 0, lost: 0, ptsDiff: 0, totalPts: 0, elo: 1200 };
    }
  });

  db[winner].won++;
  db[loser].lost++;

  // Standard Elo Rating System with Expected Win Probability (BWF / FIDE standard)
  const eloW = db[winner].elo || 1200;
  const eloL = db[loser].elo || 1200;
  const expectedW = 1 / (1 + Math.pow(10, (eloL - eloW) / 400));
  const expectedL = 1 - expectedW;
  const K = 32; // Standard tournament K-factor
  const delta = Math.round(K * (1 - expectedW));
  db[winner].elo = Math.min(3000, eloW + Math.max(4, delta));
  db[loser].elo = Math.max(600, eloL - Math.max(4, delta));

  match.sets.forEach(s => {
    db[match.a].totalPts += (s.score[0] || 0);
    db[match.b].totalPts += (s.score[1] || 0);
    db[match.a].ptsDiff += ((s.score[0] || 0) - (s.score[1] || 0));
    db[match.b].ptsDiff += ((s.score[1] || 0) - (s.score[0] || 0));
  });

  saveLeaderboardDB(db);

  // Synchronize updated Elo directly to registered user accounts
  try {
    const users = getUsersDB();
    let updated = false;
    [winner, loser].forEach(n => {
      const athleteNames = n.includes('/') ? n.split('/').map(s => s.trim()) : [n];
      athleteNames.forEach(an => {
        const u = users.find(usr => usr.name.toLowerCase() === an.toLowerCase());
        if (u) {
          u.elo = db[n].elo;
          updated = true;
          if (currentUser && currentUser.id === u.id) {
            currentUser.elo = u.elo;
            setCurrentUser(currentUser);
          }
        }
      });
    });
    if (updated) saveUsersDB(users);
  } catch (e) {}
}

function recordTournamentChampion() {
  const db = getLeaderboardDB();
  if (state.champion && db[state.champion]) {
    db[state.champion].gold = (db[state.champion].gold || 0) + 1;
  }
  if (state.runnerUp && db[state.runnerUp]) {
    db[state.runnerUp].silver = (db[state.runnerUp].silver || 0) + 1;
  }
  // Check if bronze match already completed or resolve now
  if (!state.thirdPlace && state.bronzeMatchId) {
    const bm = state.matches.find(m => m.id === state.bronzeMatchId);
    if (bm && bm.winner) {
      state.thirdPlace = bm.winner === 'a' ? bm.a : bm.b;
    }
  }
  if (state.thirdPlace && db[state.thirdPlace]) {
    db[state.thirdPlace].bronze = (db[state.thirdPlace].bronze || 0) + 1;
  }
  saveLeaderboardDB(db);
}

function renderLeaderboard() {
  const db = getLeaderboardDB();
  const tbody = document.getElementById('globalLeaderboardTableBody');
  if (!tbody) return;

  const players = Object.values(db).sort((x, y) => {
    if (y.gold !== x.gold) return y.gold - x.gold;
    if (y.won !== x.won) return y.won - x.won;
    return y.ptsDiff - x.ptsDiff;
  });

  if (!players.length) {
    tbody.innerHTML = `<tr><td colspan="12" style="text-align:center;padding:24px;color:var(--clr-text-muted);">No tournament records yet. Complete fixtures to populate the Hall of Fame.</td></tr>`;
    return;
  }

  tbody.innerHTML = players.map((p, idx) => {
    const total = p.won + p.lost;
    const rate = total > 0 ? Math.round((p.won / total) * 100) : 0;
    const opponent = players[idx === 0 ? 1 : 0]?.name || p.name;
    return `
      <tr>
        <td style="font-weight:900;color:${idx === 0 ? 'var(--clr-gold)' : (idx === 1 ? 'var(--clr-silver)' : (idx === 2 ? 'var(--clr-bronze)' : 'inherit'))};">${idx + 1}</td>
        <td><strong>${p.name}</strong></td>
        <td><strong style="color:var(--clr-gold);">${p.elo || 1200}</strong></td>
        <td style="color:var(--clr-gold);font-weight:bold;">${p.gold || 0}</td>
        <td style="color:var(--clr-silver);">${p.silver || 0}</td>
        <td style="color:var(--clr-bronze);">${p.bronze || 0}</td>
        <td>${total}</td>
        <td style="color:var(--clr-green);">${p.won}</td>
        <td style="color:var(--clr-red);">${p.lost}</td>
        <td style="font-weight:bold;">${rate}%</td>
        <td style="color:${p.ptsDiff >= 0 ? 'var(--clr-green)' : 'var(--clr-red)'};">${p.ptsDiff > 0 ? '+' : ''}${p.ptsDiff}</td>
        <td>
          <button class="btn btn-ghost btn-xs" onclick="openH2HModal('${p.name}', '${opponent}')">Compare</button>
        </td>
      </tr>
    `;
  }).join('');
}

function exportStandingsCSV() {
  const db = getLeaderboardDB();
  const rows = [['Rank', 'Player', 'Elo', 'Gold', 'Silver', 'Bronze', 'Won', 'Lost', 'PointsDiff']];
  Object.values(db).forEach((p, idx) => {
    rows.push([idx + 1, `"${p.name}"`, p.elo || 1200, p.gold || 0, p.silver || 0, p.bronze || 0, p.won, p.lost, p.ptsDiff]);
  });
  const csv = rows.map(r => r.join(',')).join('\n');
  const blob = new Blob([csv], { type: 'text/csv' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = `badminton_cup_rankings_${Date.now()}.csv`;
  a.click();
  showToast('Rankings CSV exported.');
}

/* ═══════════════════════════════════════════════════
   PERSISTENCE & RESET
═══════════════════════════════════════════════════ */
function saveState() {
  const currentTId = state.tournamentId || 'main';
  try {
    localStorage.setItem(STORAGE_KEY_STATE, JSON.stringify(state));
    localStorage.setItem(STORAGE_KEY_STATE + '_' + currentTId, JSON.stringify(state));
  } catch (e) {
    state.matches.forEach(m => { if (m.history) m.history = m.history.slice(-10); });
    try {
      localStorage.setItem(STORAGE_KEY_STATE, JSON.stringify(state));
      localStorage.setItem(STORAGE_KEY_STATE + '_' + currentTId, JSON.stringify(state));
    } catch (e2) {}
  }
}

function quickInitializeDemoTournament() {
  const poolA = ['Parag Das', 'Rifat Haque', 'Rifat Tariq', 'Jobayer', 'Shewa', 'Sazedul', 'Nur', 'Ofi'];
  const poolB = ['Sifat', 'Sajeeb', 'Jakir', 'Saiful', 'Al Emran', 'Toufiq', 'Abir', 'Rashed'];
  state.poolA = poolA;
  state.poolB = poolB;
  const matchesA = generateRoundRobinMatches(state.poolA, 'A');
  const matchesB = generateRoundRobinMatches(state.poolB, 'B');
  state.matches = [...matchesA, ...matchesB];
  saveState();
  renderGroups();
  renderBracket();
  updateGoldenAwards();
  refreshCurrentViews();
  showToast('Tournament loaded with Rashed (Admin) & 15 athletes!');
}

function loadSavedState(autoRender = true) {
  try {
    const raw = localStorage.getItem(STORAGE_KEY_STATE);
    if (raw) {
      const parsed = JSON.parse(raw);
      Object.assign(state, parsed);
    }
  } catch (e) {}

  if (!state.matches || state.matches.length === 0) {
    const poolA = ['Parag Das', 'Rifat Haque', 'Rifat Tariq', 'Jobayer', 'Shewa', 'Sazedul', 'Nur', 'Ofi'];
    const poolB = ['Sifat', 'Sajeeb', 'Jakir', 'Saiful', 'Al Emran', 'Toufiq', 'Abir', 'Rashed'];
    state.poolA = poolA;
    state.poolB = poolB;
    const matchesA = generateRoundRobinMatches(state.poolA, 'A');
    const matchesB = generateRoundRobinMatches(state.poolB, 'B');
    state.matches = [...matchesA, ...matchesB];
    saveState();
  }

  renderTournamentSwitcher();
  if (autoRender) refreshCurrentViews();
}

function refreshCurrentViews() {
  if (state.matches.length > 0) {
    renderGroups();
    renderBracket();
    updateGoldenAwards();
  }
  renderLeaderboard();
  renderAdminDashboard();
  renderPlayerHub();
  updateBettingUI();
}

function resetTournamentState() {
  if (confirm('Clear current tournament data? Active pending bets will be refunded.')) {
    const bets = getBetsDB();
    const wallets = getWalletsDB();
    bets.filter(b => b.status === 'pending').forEach(b => {
      b.status = 'refunded';
      wallets[b.username] = (wallets[b.username] || 0) + b.stake;
      recordTransaction(b.username, 'refund', b.stake, wallets[b.username], 'Tournament reset refund');
    });
    saveBetsDB(bets);
    saveWalletsDB(wallets);

    localStorage.removeItem(STORAGE_KEY_STATE);
    location.reload();
  }
}

/* ═══════════════════════════════════════════════════
   THEME & FULLSCREEN
═══════════════════════════════════════════════════ */
function toggleThemeMode() {
  const body = document.body;
  const isLight = body.classList.contains('theme-light');
  if (isLight) {
    body.className = '';
    localStorage.setItem(STORAGE_KEY_THEME, '');
    showToast('Stadium Dark Theme Activated', 'info');
  } else {
    body.className = 'theme-light';
    localStorage.setItem(STORAGE_KEY_THEME, 'theme-light');
    showToast('Light Gymnasium Theme Activated', 'success');
  }
  updateThemeIcons();
}

function updateThemeIcons() {
  const isLight = document.body.classList.contains('theme-light');
  const sun = document.getElementById('themeIconSun');
  const moon = document.getElementById('themeIconMoon');
  if (sun && moon) {
    if (isLight) {
      sun.style.display = 'none';
      moon.style.display = 'block';
    } else {
      sun.style.display = 'block';
      moon.style.display = 'none';
    }
  }
}

function cycleTheme() {
  const body = document.body;
  if (!body.classList.contains('theme-light') && !body.classList.contains('theme-contrast')) {
    body.className = 'theme-light';
    localStorage.setItem(STORAGE_KEY_THEME, 'theme-light');
    showToast('Light Gymnasium Theme');
  } else if (body.classList.contains('theme-light')) {
    body.className = 'theme-contrast';
    localStorage.setItem(STORAGE_KEY_THEME, 'theme-contrast');
    showToast('High Contrast Umpire Theme');
  } else {
    body.className = '';
    localStorage.setItem(STORAGE_KEY_THEME, '');
    showToast('Stadium Dark Theme');
  }
  updateThemeIcons();
}

function toggleFullScreen() {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen().catch(() => {});
  } else {
    document.exitFullscreen().catch(() => {});
  }
}

function openCoinTossModal() {
  document.getElementById('coinTossModal').showModal();
}
function openSoundSettingsModal() {
  populateVoiceOptions();
  document.getElementById('soundSettingsModal').showModal();
}

function flipCoin() {
  const coin = document.getElementById('coinGraphic');
  const res = document.getElementById('coinResultText');
  coin.style.transform = 'rotateY(720deg) scale(1.2)';
  res.textContent = 'Flipping...';
  playSound('point');

  setTimeout(() => {
    const isHeads = Math.random() > 0.5;
    coin.style.transform = 'rotateY(0deg) scale(1)';
    coin.innerHTML = isHeads ? svgIcon('shuttle', 'icon-3xl') : svgIcon('coin', 'icon-3xl');
    res.textContent = isHeads ? 'HEADS (SHUTTLE) — Serve First!' : 'TAILS (COIN) — Choose Side!';
    playSound('point');
  }, 600);
}

function showToast(msg) {
  const t = document.getElementById('appToast');
  t.textContent = msg;
  t.classList.add('show');
  clearTimeout(t._timer);
  t._timer = setTimeout(() => t.classList.remove('show'), 2800);
}

/* ═══════════════════════════════════════════════════
   KEYBOARD HOTKEYS SCORING ENGINE
═══════════════════════════════════════════════════ */
document.addEventListener('keydown', e => {
  if (['INPUT', 'TEXTAREA', 'SELECT'].includes(e.target.tagName)) return;

  const isLive = document.getElementById('liveUmpireScreen').classList.contains('active');
  if (isLive) {
    if (e.key === '1' || e.key === 'a' || e.key === 'A') {
      scorePoint('a');
    } else if (e.key === '2' || e.key === 'd' || e.key === 'D') {
      scorePoint('b');
    } else if (e.key === 'u' || e.key === 'U' || ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'z')) {
      e.preventDefault();
      undoPoint();
    } else if (e.key === ' ' || e.code === 'Space') {
      e.preventDefault();
      toggleServerManual();
    } else if (e.key === 's' || e.key === 'S') {
      e.preventDefault();
      speakScoreAnnouncement();
  const annEl = document.getElementById('ariaLiveAnnouncer');
  if (annEl) {
    const curS = match.sets[state.currentSetIdx];
    annEl.textContent = `Score: ${match.a} ${curS.score[0]}, ${match.b} ${curS.score[1]}. Serving: ${state.servingSide === 'a' ? match.a : match.b}`;
  }
    } else if (e.key === 'f' || e.key === 'F') {
      e.preventDefault();
      toggleCourtFlip();
    } else if (e.key === 'Escape') {
      exitLiveScoreboard();
    }
  }
});

/* ═══════════════════════════════════════════════════
   OBS STREAMING OVERLAY CONTROLLER (ITEM 38)
═══════════════════════════════════════════════════ */
function checkObsOverlayRoute() {
  const params = new URLSearchParams(window.location.search);
  const overlayParam = params.get('overlay') || params.get('obs');
  if (!overlayParam) return;

  document.body.classList.add('obs-mode');
  const container = document.getElementById('obsOverlayContainer');
  if (container) container.style.display = 'block';

  renderObsOverlay(overlayParam);
  setInterval(() => renderObsOverlay(overlayParam), 1000);
}

function renderObsOverlay(param) {
  const courtNum = parseInt(String(param).replace(/\D/g, ''), 10) || 1;
  const match = (state.matches && state.matches.length > 0)
    ? (state.matches.find(m => m.court === courtNum && m.status === 'in_progress') ||
       state.matches.find(m => m.status === 'in_progress') ||
       state.matches[0])
    : null;

  if (!match) return;

  const curSet = (match.sets && match.sets[match.currentSet || 0]) || { score: [0, 0] };
  const titleEl = document.getElementById('obsTournamentTitle');
  if (titleEl) titleEl.textContent = state.title || 'Badminton Cup';
  const playerAEl = document.getElementById('obsPlayerA');
  if (playerAEl) playerAEl.textContent = match.a;
  const playerBEl = document.getElementById('obsPlayerB');
  if (playerBEl) playerBEl.textContent = match.b;
  const scoreAEl = document.getElementById('obsScoreA');
  if (scoreAEl) scoreAEl.textContent = curSet.score[0] || 0;
  const scoreBEl = document.getElementById('obsScoreB');
  if (scoreBEl) scoreBEl.textContent = curSet.score[1] || 0;
  const courtEl = document.getElementById('obsCourtLabel');
  if (courtEl) courtEl.textContent = `COURT ${match.court || courtNum}`;
  const setEl = document.getElementById('obsSetLabel');
  if (setEl) setEl.textContent = `SET ${(match.currentSet || 0) + 1}`;
}

/* ═══════════════════════════════════════════════════
   INITIALIZATION ON DOM LOAD
═══════════════════════════════════════════════════ */
window.addEventListener('DOMContentLoaded', async () => {
  const savedTheme = localStorage.getItem(STORAGE_KEY_THEME);
  if (savedTheme) document.body.className = savedTheme;
  updateThemeIcons();

  // Pre-seed admin and verified demo athletes
  try {
    const users = getUsersDB();
    if (!users.some(u => u.name.toLowerCase() === 'admin')) {
      const adminHash = await hashPassword('admin123');
      users.push({
        id: 1001,
        name: 'Rashed',
        email: 'rashed@badminton.local',
        passHash: adminHash,
        role: 'admin',
        status: 'active',
        feeStatus: 'paid',
        elo: 1600,
        dominantHand: 'Right-Handed',
        club: 'Tournament Director',
        avatar: 'R',
        createdAt: 'Initial'
      });

      // Seed verified demo players requested by user
      const demoAthletes = [
        { name: 'Parag Das', email: 'parag@badminton.local', club: 'Dhaka Smashers', elo: 1610, role: 'player', status: 'active' },
        { name: 'Rifat Haque', email: 'rifat.haque@badminton.local', club: 'Uttara Shuttlers', elo: 1590, role: 'player', status: 'active' },
        { name: 'Rifat Tariq', email: 'rifat.tariq@badminton.local', club: 'Banani BC', elo: 1580, role: 'player', status: 'active' },
        { name: 'Jobayer', email: 'jobayer@badminton.local', club: 'Gulshan Aces', elo: 1570, role: 'player', status: 'active' },
        { name: 'Shewa', email: 'shewa@badminton.local', club: 'Mirpur Warriors', elo: 1560, role: 'player', status: 'active' },
        { name: 'Sazedul', email: 'sazedul@badminton.local', club: 'Dhanmondi Club', elo: 1550, role: 'player', status: 'active' },
        { name: 'Nur', email: 'nur@badminton.local', club: 'Mohakhali Spikers', elo: 1540, role: 'player', status: 'active' },
        { name: 'Ofi', email: 'ofi@badminton.local', club: 'Bashundhara BC', elo: 1530, role: 'player', status: 'active' },
        { name: 'Sifat', email: 'sifat@badminton.local', club: 'Foosball & Shuttlers', elo: 1620, role: 'player', status: 'active' },
        { name: 'Sajeeb', email: 'sajeeb@badminton.local', club: 'Paltan Smashers', elo: 1520, role: 'player', status: 'active' },
        { name: 'Jakir', email: 'jakir@badminton.local', club: 'Rampura Rackets', elo: 1510, role: 'player', status: 'active' },
        { name: 'Saiful', email: 'saiful@badminton.local', club: 'Khilgaon Shuttlers', elo: 1500, role: 'player', status: 'active' },
        { name: 'Al Emran', email: 'emran@badminton.local', club: 'Chittagong Aces', elo: 1580, role: 'player', status: 'active' },
        { name: 'Toufiq', email: 'toufiq@badminton.local', club: 'Sylhet Smashers', elo: 1540, role: 'player', status: 'active' },
        { name: 'Abir', email: 'abir@badminton.local', club: 'Rajshahi Smashers', elo: 1560, role: 'player', status: 'active' }
      ];

      for (let i = 0; i < demoAthletes.length; i++) {
        const da = demoAthletes[i];
        const hash = await hashPassword('pass123');
        users.push({
          id: 2000 + i,
          name: da.name,
          email: da.email,
          passHash: hash,
          role: da.role,
          status: da.status,
          inviteToken: 'tok_' + da.name.replace(/\s+/g, '').toLowerCase(),
          feeStatus: 'paid',
          elo: da.elo,
          dominantHand: 'Right-Handed',
          club: da.club,
          avatar: 'U',
          invitedBy: 'admin',
          createdAt: new Date().toLocaleDateString()
        });
      }
      saveUsersDB(users);
    }
  } catch (e) {}

  ensureDemoUsersSeeded();
  loadAuthUser();
  loadSavedState();
  renderTournamentSwitcher();
  updatePlayerCounts();
  checkUrlInvitationToken();
  checkObsOverlayRoute();

  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('sw.js').catch(() => {});
  }
});


/* ═══════════════════════════════════════════════════
   OFFLINE & NETWORK RESILIENCY MONITOR
═══════════════════════════════════════════════════ */
function updateNetworkStatusPill() {
  const pill = document.getElementById('networkSyncPill');
  const label = document.getElementById('syncStatusLabel');
  if (!pill || !label) return;
  if (navigator.onLine) {
    pill.classList.remove('offline');
    label.textContent = 'Online (Synced)';
  } else {
    pill.classList.add('offline');
    label.textContent = 'Offline (PWA Cache)';
  }
}
window.addEventListener('online', updateNetworkStatusPill);
window.addEventListener('offline', updateNetworkStatusPill);
document.addEventListener('DOMContentLoaded', () => {
  updateNetworkStatusPill();
  });


/* ═══════════════════════════════════════════════════
   PWA & PUSH NOTIFICATION SYSTEM
═══════════════════════════════════════════════════ */
let deferredInstallPrompt = null;
window.addEventListener('beforeinstallprompt', e => {
  e.preventDefault();
  deferredInstallPrompt = e;
  const btn = document.getElementById('installAppBtn');
  if (btn) btn.style.display = 'inline-flex';
  const moreBtn = document.getElementById('moreInstallBtn');
  if (moreBtn) moreBtn.style.display = 'flex';
});

window.addEventListener('appinstalled', () => {
  deferredInstallPrompt = null;
  const btn = document.getElementById('installAppBtn');
  if (btn) btn.style.display = 'none';
  showToast('Badminton Cup app installed successfully!', 'success');
});

function promptInstallPWA() {
  if (deferredInstallPrompt) {
    deferredInstallPrompt.prompt();
    deferredInstallPrompt.userChoice.then(choice => {
      if (choice.outcome === 'accepted') {
        showToast('Installation starting...', 'success');
      }
      deferredInstallPrompt = null;
    });
  } else {
    showToast('Tap browser menu (⋮ or Share) and select "Add to Home Screen"', 'info');
  }
}

function openMoreMenu() {
  const modal = document.getElementById('moreMenuModal');
  if (modal) modal.showModal();
}

function playChimeSound(type = 'ping') {
  try {
    const AudioCtx = window.AudioContext || window.webkitAudioContext;
    if (!AudioCtx) return;
    const ctx = new AudioCtx();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.connect(gain);
    gain.connect(ctx.destination);

    if (type === 'win') {
      const now = ctx.currentTime;
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(523.25, now);
      osc.frequency.setValueAtTime(659.25, now + 0.1);
      osc.frequency.setValueAtTime(783.99, now + 0.2);
      osc.frequency.setValueAtTime(1046.50, now + 0.3);
      gain.gain.setValueAtTime(0.3, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.6);
      osc.start(now);
      osc.stop(now + 0.6);
    } else {
      const now = ctx.currentTime;
      osc.type = 'sine';
      osc.frequency.setValueAtTime(880, now);
      osc.frequency.exponentialRampToValueAtTime(440, now + 0.25);
      gain.gain.setValueAtTime(0.2, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.3);
      osc.start(now);
      osc.stop(now + 0.3);
    }
  } catch (err) {}
}

function updateNotificationUI() {
  const notifyBtn = document.getElementById('notifyBtn');
  if (!notifyBtn) return;
  const isGranted = ('Notification' in window) && Notification.permission === 'granted';
  notifyBtn.classList.toggle('active', isGranted);
  notifyBtn.title = isGranted 
    ? ('Notifications Active') 
    : ('Enable Notifications');
}

function openNotificationModal() {
  updateNotificationModalUI();
  const modal = document.getElementById('notificationSettingsModal');
  if (modal) modal.showModal();
}

function updateNotificationModalUI() {
  const heading = document.getElementById('notifyStatusHeading');
  const desc = document.getElementById('notifyStatusDesc');
  const btn = document.getElementById('btnRequestNotification');
  if (!('Notification' in window)) {
    if (heading) heading.textContent = 'Notifications Not Supported';
    if (desc) desc.textContent = 'This browser does not support Web Push Notifications.';
    if (btn) btn.style.display = 'none';
    return;
  }

  const perm = Notification.permission;
  if (perm === 'granted') {
    if (heading) heading.textContent = 'Notifications Active ✓';
    if (desc) desc.textContent = 'Awesome! You will receive live alerts for challenges, match wins, and champion announcements.';
    if (btn) {
      btn.innerHTML = '<svg class="icon icon-xs" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg> ' + ('Notifications Enabled');
      btn.classList.remove('btn-primary');
      btn.classList.add('btn-ghost');
    }
  } else if (perm === 'denied') {
    if (heading) heading.textContent = 'Notifications Blocked';
    if (desc) desc.textContent = 'Notifications were blocked in your browser settings. Please allow notifications in site permissions.';
    if (btn) btn.style.display = 'none';
  } else {
    if (heading) heading.textContent = 'Enable Notifications';
    if (desc) desc.textContent = 'Stay updated! Get instant notifications when a challenge is posted or match results are recorded.';
    if (btn) {
      btn.style.display = 'flex';
      btn.innerHTML = '<svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg> ' + ('Turn On Push Notifications');
      btn.classList.add('btn-primary');
      btn.classList.remove('btn-ghost');
    }
  }
  updateNotificationUI();
}

function requestNotificationPermission() {
  if (!('Notification' in window)) {
    showToast('Notifications not supported in this browser', 'warning');
    return;
  }
  Notification.requestPermission().then(permission => {
    updateNotificationModalUI();
    updateNotificationUI();
    if (permission === 'granted') {
      sendAppNotification(
        'Badminton Cup Notifications Active!',
        'Welcome! You will now receive alerts for challenges and match updates.'
      );
      showToast('Notifications enabled successfully!', 'success');
    } else {
      showToast('Notification permission not granted.', 'warning');
    }
  });
}

function testPushNotification() {
  sendAppNotification(
    '🏸 Badminton Cup Test Alert',
    'Push notifications are working smoothly on your device!'
  );
  showToast('Test notification triggered!', 'info');
}

function sendAppNotification(title, body, tag = 'badminton-alert') {
  playChimeSound(tag === 'champion' ? 'win' : 'ping');
  if (!('Notification' in window) || Notification.permission !== 'granted') return;

  if (navigator.serviceWorker && navigator.serviceWorker.controller) {
    navigator.serviceWorker.ready.then(reg => {
      reg.showNotification(title, {
        body: body,
        icon: 'icons/icon-192.png',
        badge: 'icons/icon-192.png',
        tag: tag,
        vibrate: [120, 60, 120]
      });
    }).catch(() => {
      try { new Notification(title, { body, icon: 'icons/icon-192.png' }); } catch (e) {}
    });
  } else {
    try { new Notification(title, { body, icon: 'icons/icon-192.png' }); } catch (e) {}
  }
}

</script>
"""
