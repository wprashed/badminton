SCRIPTS_CONTENT = r"""<script>
/* ═══════════════════════════════════════════════════
   GLOBAL UTILITIES & RESILIENCE HELPERS
═══════════════════════════════════════════════════ */
function escapeHtml(str) {
  if (str === null || str === undefined) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}
window.escapeHtml = escapeHtml;

/* Vector Single-Color Flat Icons Helper */
function svgIcon(name, cls) {
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

window.svgIcon = svgIcon;

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
const STORAGE_KEY_CHALLENGES = 'badminton_challenges_v4';

/* ═══════════════════════════════════════════════════
   GLOBAL STATE & SESSION DATA
═══════════════════════════════════════════════════ */
const state = {
  title: 'The Badminton Cup 2026',
  category: 'singles', // 'singles' or 'doubles'
  ptsToWin: 15,
  bestOf: 3,
  stageFormat: 'rr',   // 'rr' or 'ko'
  courtNumber: 2,
  selectedCourtFilter: 'all',
  audioEnabled: true,
  handicapEnabled: false,
  courtFlipped: false,
  entryFee: 50,
  nillSystemEnabled: true,
  nillThreshold: 10,
  nillPenalty: 10,
  poolA: [],
  poolB: [],
  players: [],
  matches: [],
  koRounds: [],
  plateMatches: [],
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

/* Refund pending bets when a match is cancelled or ends in walkover */
function refundMatchBets(matchId) {
  try {
    const bets = getBetsDB();
    const pendingBets = bets.filter(b => b.matchId === matchId && !b.settled);
    if (!pendingBets.length) return;

    const wallets = getWalletsDB();
    const txs = getTransactionsDB();

    pendingBets.forEach(b => {
      if (!wallets[b.username]) wallets[b.username] = { balance: 100, earned: 0, spent: 0 };
      wallets[b.username].balance += b.amount;
      b.settled = true;
      b.refunded = true;
      txs.unshift({
        id: 'tx_ref_' + Date.now().toString(36) + '_' + Math.random().toString(36).substr(2, 4),
        username: b.username,
        amount: b.amount,
        type: 'refund',
        desc: `Bet refund (Match cancelled/walkover)`,
        time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      });
    });

    saveBetsDB(bets);
    saveWalletsDB(wallets);
    saveTransactionsDB(txs);
    updateCoinBalanceUI();
  } catch (e) {
    console.error('Error refunding bets:', e);
  }
}

/* Quick referee fault calls in live scoreboard */
function awardFaultPoint(faultType) {
  const match = state.matches.find(m => m.id === state.currentMatchId);
  if (!match || match.winner) return;

  const offendingSide = state.servingSide;
  const receivingSide = offendingSide === 'a' ? 'b' : 'a';
  const label = faultType === 'service' ? 'Service Fault' : (faultType === 'net' ? 'Net Touch Fault' : 'Shuttle Out Fault');

  showToast(`⚠️ ${label} called on ${offendingSide === 'a' ? match.a : match.b}! Point awarded to ${receivingSide === 'a' ? match.a : match.b}.`, 'warning');
  scorePoint(receivingSide);
}

/* Instant Rematch from Completed Challenge */
function instantRematchChallenge(chalId) {
  const list = getChallengesDB();
  const oldChal = list.find(c => c.id === chalId);
  if (!oldChal) return;

  const newChal = {
    id: 'ch_' + Date.now().toString(36),
    creator: oldChal.opponent || oldChal.creator,
    opponent: oldChal.opponent ? oldChal.creator : null,
    category: oldChal.category || 'singles',
    points: oldChal.points || 15,
    note: 'Rematch: ' + (oldChal.note || 'Court 1'),
    status: oldChal.opponent ? 'accepted' : 'open',
    createdAt: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
  };

  list.unshift(newChal);
  saveChallengesDB(list);

  if (newChal.status === 'accepted') {
    const newMatch = createMatchObj(newChal.creator, newChal.opponent, 'CHALLENGE');
    newChal.matchId = newMatch.id;
    state.matches.push(newMatch);
    saveState();
  }

  renderChallengesBoard();
  showToast('⚡ Rematch created! Jump right back in.', 'success');
}

/* WhatsApp Match Invitation Generator */
function shareChallengeWhatsApp(chalId) {
  const list = getChallengesDB();
  const chal = list.find(c => c.id === chalId);
  if (!chal) return;

  const url = window.location.origin + window.location.pathname + '#challenge=' + chal.id;
  const text = `🏸 Badminton Cup Challenge!
${chal.creator} invites you to a ${chal.category || 'singles'} match to ${chal.points || 15} points at ${chal.note || 'Court 1'}.

Accept challenge here: ${url}`;
  window.open(`https://api.whatsapp.com/send?text=${encodeURIComponent(text)}`, '_blank');
}

/* Update Live Tournament Progress Bar */
function updateTournamentProgressUI() {
  const textEl = document.getElementById('tournamentProgressText');
  const fillEl = document.getElementById('tournamentProgressBarFill');
  if (!textEl || !fillEl) return;

  const matches = (state.matches || []).filter(m => m.pool === 'A' || m.pool === 'B');
  if (!matches.length) {
    textEl.textContent = '0 / 0 Matches Completed (0%)';
    fillEl.style.width = '0%';
    return;
  }

  const completed = matches.filter(m => m.winner).length;
  const pct = Math.round((completed / matches.length) * 100);
  textEl.textContent = `${completed} / ${matches.length} Matches Completed (${pct}%)`;
  fillEl.style.width = `${pct}%`;
}

/* Safe LocalStorage with Quota Eviction Protection */
function safeLocalStorageSet(key, value) {
  try {
    localStorage.setItem(key, value);
    return true;
  } catch (e) {
    if (e.name === 'QuotaExceededError' || e.code === 22) {
      console.warn('LocalStorage quota limit reached. Clearing temporary caches...');
      try {
        localStorage.removeItem('badminton_cup_theme_pref');
        localStorage.setItem(key, value);
        return true;
      } catch (inner) {
        showToast('Device storage limit reached. Please clear older completed matches.', 'warning');
        return false;
      }
    }
    return false;
  }
}

/* ═══════════════════════════════════════════════════
   GLOBAL UTILITIES & RESILIENCE HELPERS
═══════════════════════════════════════════════════ */
window.escapeHtml = function(str) {
  if (str === null || str === undefined) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
};

/* Modern Accessible Non-Blocking Modals replacing native window.confirm & prompt */
function appConfirm(message, title = 'Confirmation Required', okText = 'Confirm', danger = false) {
  return new Promise((resolve) => {
    const modal = document.getElementById('appConfirmModal');
    if (!modal) {
      resolve(window.confirm(message));
      return;
    }
    const titleEl = document.getElementById('appConfirmTitle');
    const msgEl = document.getElementById('appConfirmMsg');
    const okBtn = document.getElementById('appConfirmOkBtn');
    const cancelBtn = document.getElementById('appConfirmCancelBtn');

    if (titleEl) titleEl.textContent = title;
    if (msgEl) msgEl.textContent = message;
    if (okBtn) {
      okBtn.textContent = okText;
      okBtn.className = danger ? 'btn btn-danger btn-sm' : 'btn btn-primary btn-sm';
    }

    const onOk = () => { cleanup(); modal.close(); resolve(true); };
    const onCancel = () => { cleanup(); modal.close(); resolve(false); };
    const onEsc = (e) => { if (e.key === 'Escape') { cleanup(); resolve(false); } };

    function cleanup() {
      if (okBtn) okBtn.removeEventListener('click', onOk);
      if (cancelBtn) cancelBtn.removeEventListener('click', onCancel);
      modal.removeEventListener('keydown', onEsc);
    }

    if (okBtn) okBtn.addEventListener('click', onOk);
    if (cancelBtn) cancelBtn.addEventListener('click', onCancel);
    modal.addEventListener('keydown', onEsc);

    modal.showModal();
  });
}

function appPrompt(message, defaultValue = '', title = 'Input Required') {
  return new Promise((resolve) => {
    const modal = document.getElementById('appPromptModal');
    if (!modal) {
      resolve(window.prompt(message, defaultValue));
      return;
    }
    const titleEl = document.getElementById('appPromptTitle');
    const msgEl = document.getElementById('appPromptMsg');
    const inputEl = document.getElementById('appPromptInput');
    const okBtn = document.getElementById('appPromptOkBtn');
    const cancelBtn = document.getElementById('appPromptCancelBtn');

    if (titleEl) titleEl.textContent = title;
    if (msgEl) msgEl.textContent = message;
    if (inputEl) {
      inputEl.value = defaultValue;
      setTimeout(() => { inputEl.focus(); inputEl.select(); }, 50);
    }

    const onOk = () => {
      const val = inputEl ? inputEl.value : '';
      cleanup();
      modal.close();
      resolve(val);
    };
    const onCancel = () => { cleanup(); modal.close(); resolve(null); };
    const onKey = (e) => {
      if (e.key === 'Enter') { e.preventDefault(); onOk(); }
      else if (e.key === 'Escape') { cleanup(); resolve(null); }
    };

    function cleanup() {
      if (okBtn) okBtn.removeEventListener('click', onOk);
      if (cancelBtn) cancelBtn.removeEventListener('click', onCancel);
      if (inputEl) inputEl.removeEventListener('keydown', onKey);
    }

    if (okBtn) okBtn.addEventListener('click', onOk);
    if (cancelBtn) cancelBtn.addEventListener('click', onCancel);
    if (inputEl) inputEl.addEventListener('keydown', onKey);

    modal.showModal();
  });
}

/* Web Audio API unlocking on iOS / Safari first interaction */
let audioCtxUnlocked = false;
function unlockAudioContext() {
  if (audioCtxUnlocked) return;
  try {
    const AudioCtx = window.AudioContext || window.webkitAudioContext;
    if (AudioCtx) {
      if (!window.__appAudioCtx) window.__appAudioCtx = new AudioCtx();
      if (window.__appAudioCtx.state === 'suspended') {
        window.__appAudioCtx.resume();
      }
      audioCtxUnlocked = true;
    }
  } catch (e) {}
}
['click', 'touchstart', 'keydown'].forEach(evt => {
  document.addEventListener(evt, unlockAudioContext, { once: true, passive: true });
});

/* Global Audio Mute Controller */
let isAppAudioMuted = localStorage.getItem('badminton_sound_muted') === 'true';

function toggleMuteAudio() {
  isAppAudioMuted = !isAppAudioMuted;
  localStorage.setItem('badminton_sound_muted', isAppAudioMuted ? 'true' : 'false');
  updateSoundIconUI();
  showToast(isAppAudioMuted ? 'Audio chime muted 🔇' : 'Audio chime enabled 🔊', 'info');
}

function updateSoundIconUI() {
  const onIcon = document.getElementById('soundIconOn');
  const offIcon = document.getElementById('soundIconOff');
  if (onIcon && offIcon) {
    onIcon.style.display = isAppAudioMuted ? 'none' : 'block';
    offIcon.style.display = isAppAudioMuted ? 'block' : 'none';
  }
}

/* Online / Offline Connectivity Tracker */
function updateNetworkStatus() {
  const pill = document.getElementById('offlineStatusPill');
  if (!pill) return;
  if (!navigator.onLine) {
    pill.style.display = 'inline-flex';
    showToast('Offline Mode: matches, bets and scores are saved in local cache.', 'warning');
  } else {
    pill.style.display = 'none';
  }
}
window.addEventListener('online', updateNetworkStatus);
window.addEventListener('offline', updateNetworkStatus);

/* CSV Export Functions */
function exportMatchesCSV() {
  if (!state.matches || !state.matches.length) {
    showToast('No matches to export.', 'warning');
    return;
  }
  let csv = 'Match ID,Pool,Court,Team A,Team B,Winner,Set Scores,Duration (s),Status\n';
  state.matches.forEach(m => {
    const scores = (m.sets || []).map(s => `${s.score[0]}-${s.score[1]}`).join(' | ');
    const winnerName = m.winner ? (m.winner === 'a' ? m.a : m.b) : 'Pending';
    csv += `"${m.id}","${m.pool}","${m.court || 1}","${m.a}","${m.b}","${winnerName}","${scores}","${m.durationSeconds || 0}","${m.winner ? 'Completed' : 'Scheduled'}"\n`;
  });
  downloadFile(csv, `${(state.title || 'Badminton_Cup').replace(/\\s+/g, '_')}_matches.csv`, 'text/csv');
  showToast('Match records exported to CSV!', 'success');
}

function exportStandingsCSV() {
  const standingsA = computePoolStandings(state.poolA, 'A');
  const standingsB = computePoolStandings(state.poolB, 'B');
  let csv = 'Pool,Rank,Athlete,Played,Wins,Losses,Games Won,Games Lost,Points Won,Points Lost,Point Diff\n';
  standingsA.forEach((s, idx) => {
    csv += `"A",${idx + 1},"${s.name}",${s.W + s.L},${s.W},${s.L},${s.gamesWon},${s.gamesLost},${s.ptsWon},${s.ptsLost},${s.ptsWon - s.ptsLost}\n`;
  });
  standingsB.forEach((s, idx) => {
    csv += `"B",${idx + 1},"${s.name}",${s.W + s.L},${s.W},${s.L},${s.gamesWon},${s.gamesLost},${s.ptsWon},${s.ptsLost},${s.ptsWon - s.ptsLost}\n`;
  });
  downloadFile(csv, `${(state.title || 'Badminton_Cup').replace(/\\s+/g, '_')}_standings.csv`, 'text/csv');
  showToast('Pool standings exported to CSV!', 'success');
}

function downloadFile(content, fileName, mimeType) {
  const blob = new Blob([content], { type: mimeType });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = fileName;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

/* Dynamic ELO Rating Calculation (FIDE / BWF K=32) */
function updateMatchELO(match) {
  if (!match || !match.winner) return;
  const users = getUsersDB();
  const playerA = users.find(u => u.name.toLowerCase() === match.a.toLowerCase());
  const playerB = users.find(u => u.name.toLowerCase() === match.b.toLowerCase());
  if (!playerA || !playerB) return;

  const rA = playerA.elo || 1500;
  const rB = playerB.elo || 1500;
  const eA = 1 / (1 + Math.pow(10, (rB - rA) / 400));
  const eB = 1 / (1 + Math.pow(10, (rA - rB) / 400));
  const sA = match.winner === 'a' ? 1 : 0;
  const sB = match.winner === 'b' ? 1 : 0;
  const K = 32;

  const deltaA = Math.round(K * (sA - eA));
  const deltaB = Math.round(K * (sB - eB));

  playerA.elo = Math.max(1000, rA + deltaA);
  playerB.elo = Math.max(1000, rB + deltaB);
  saveUsersDB(users);
  renderLeaderboardScreen();
}

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
  document.getElementById('quickScoreInputA').value = state.ptsToWin || 15;
  document.getElementById('quickScoreInputB').value = Math.max(0, (state.ptsToWin || 15) - 2);
  document.getElementById('quickScoreModal').showModal();
}

function awardInstantWinner(side, specificMatchId = null) {
  if (!requireAuthUser('play or record match scores')) return;
  const matchId = specificMatchId || document.getElementById('quickMatchId')?.value;
  const match = state.matches.find(m => m.id === matchId);
  if (!match) return;

  const pts = state.ptsToWin || 15;
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
  if (!requireAuthUser('record match scores')) return;
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

  match.sets.forEach(s => {
    if (typeof checkAndApplyNill === 'function') checkAndApplyNill(match, s);
  });

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

function getChallengesDB() {
  try {
    const list = JSON.parse(localStorage.getItem(STORAGE_KEY_CHALLENGES)) || [];
    const now = Date.now();
    let changed = false;
    list.forEach(c => {
      if (c.status === 'open' && c.createdTimestamp && (now - c.createdTimestamp > 86400000)) {
        c.status = 'expired';
        changed = true;
      }
    });
    if (changed) safeLocalStorageSet(STORAGE_KEY_CHALLENGES, JSON.stringify(list));
    return list;
  } catch (e) {
    return [];
  }
}

function saveChallengesDB(list) {
  safeLocalStorageSet(STORAGE_KEY_CHALLENGES, JSON.stringify(list));
}

function openNewChallengeModal() {
  if (!requireAuthUser('create or accept challenges')) return;
  const card = document.getElementById('challengeCreatorIdentityCard');
  const hiddenInput = document.getElementById('challengeCreatorName');

  const name = currentUser ? currentUser.name : 'Athlete';
  if (hiddenInput) hiddenInput.value = name;

  if (card) {
    const avatarHtml = typeof getPlayerAvatarHtml === 'function' ? getPlayerAvatarHtml(name, 42) : '';
    card.innerHTML = `
      <div style="display:flex;align-items:center;justify-content:space-between;padding:12px 14px;background:rgba(16,185,129,0.08);border:1px solid rgba(16,185,129,0.25);border-radius:var(--radius-sm);">
        <div style="display:flex;align-items:center;gap:12px;min-width:0;">
          ${avatarHtml}
          <div style="min-width:0;">
            <div style="font-weight:800;font-size:1.02rem;color:var(--clr-text);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">${escapeHtml(name)}</div>
            <div style="font-size:0.75rem;color:var(--clr-green);display:flex;align-items:center;gap:4px;">
              <span>✓ Verified Profile</span> · <span>${currentUser && (currentUser.role === 'admin' || currentUser.role === 'super_admin') ? 'Director' : 'Athlete'}</span>
            </div>
          </div>
        </div>
        <button type="button" class="btn btn-ghost btn-xs" onclick="switchChallengeAthleteProfile()" style="font-size:0.72rem;padding:4px 8px;">Switch Profile</button>
      </div>
      <span style="font-size:0.72rem;color:var(--clr-text-muted);display:block;margin-top:6px;">Your name is automatically verified from your active profile.</span>
    `;
  }

  document.getElementById('newChallengeModal').showModal();
}

function switchChallengeAthleteProfile() {
  document.getElementById('newChallengeModal').close();
  openAuthModal();
}

function toggleCustomChallengePointsInput(val) {
  const container = document.getElementById('challengeCustomPointsContainer');
  if (container) {
    container.style.display = (val === 'custom') ? 'block' : 'none';
  }
}

function updateCustomDoublePreview(val) {
  const preview = document.getElementById('challengeCustomDoublePreview');
  const pts = parseInt(val) || 0;
  if (preview) {
    preview.textContent = pts > 0 ? `Winner gets ${pts * 2} PTS` : 'Friendly';
  }
}

function getSelectedChallengeBuyIn() {
  const select = document.getElementById('challengeBuyInSelect');
  if (!select) return 5;
  if (select.value === 'custom') {
    const customInput = document.getElementById('challengeCustomPointsInput');
    return Math.max(0, parseInt(customInput?.value) || 5);
  }
  return parseInt(select.value) || 0;
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
  const buyIn = getSelectedChallengeBuyIn();

  const partnerInput = document.getElementById('challengePartnerName');
  const partnerName = (category === 'doubles' && partnerInput) ? partnerInput.value.trim() : '';
  const hasOpenPartner = (category === 'doubles' && !partnerName);
  const isPrivate = document.getElementById('challengePrivateToggle')?.checked || false;
  const pin = isPrivate ? (document.getElementById('challengePinInput')?.value.trim() || '') : '';

  const creatorDisplayName = partnerName ? `${name} / ${partnerName}` : name;
  const payerName = currentUser ? currentUser.name : name;

  // Staked players list for exact deduction and refund tracking
  const stakedPlayers = [];

  // Deduct points from creator (and partner if logged in with separate wallet):
  // "if they select 5 then 5 points will be deduct from each player winner team memebers will get 10 points"
  if (buyIn > 0) {
    if (category === 'doubles' && partnerName) {
      const wallets = getWalletsDB();
      if (wallets[partnerName] !== undefined && partnerName.toLowerCase() !== payerName.toLowerCase()) {
        const p1Bal = getUserCoins(payerName);
        const p2Bal = getUserCoins(partnerName);
        if (p1Bal < buyIn) {
          showToast(`⚠️ Insufficient points for ${payerName}! Has ${p1Bal} PTS, needs ${buyIn} PTS.`, 'warning');
          return;
        }
        if (p2Bal < buyIn) {
          showToast(`⚠️ Insufficient points for partner ${partnerName}! Has ${p2Bal} PTS, needs ${buyIn} PTS.`, 'warning');
          return;
        }
        setUserCoins(p1Bal - buyIn, payerName);
        setUserCoins(p2Bal - buyIn, partnerName);
        recordTransaction(payerName, 'challenge_stake', buyIn, p1Bal - buyIn, `Staked ${buyIn} PTS for challenge (Playing for ${buyIn * 2} PTS)`);
        recordTransaction(partnerName, 'challenge_stake', buyIn, p2Bal - buyIn, `Staked ${buyIn} PTS for challenge (Playing for ${buyIn * 2} PTS)`);
        stakedPlayers.push({ name: payerName, amount: buyIn }, { name: partnerName, amount: buyIn });
      } else {
        const curBalance = getUserCoins(payerName);
        if (curBalance < buyIn) {
          showToast(`⚠️ Insufficient points to open this challenge! You have ${curBalance} PTS, but need ${buyIn} PTS.`, 'warning');
          return;
        }
        setUserCoins(curBalance - buyIn, payerName);
        recordTransaction(payerName, 'challenge_stake', buyIn, curBalance - buyIn, `Staked ${buyIn} PTS for challenge (Playing for ${buyIn * 2} PTS)`);
        stakedPlayers.push({ name: payerName, amount: buyIn });
      }
    } else {
      const curBalance = getUserCoins(payerName);
      if (curBalance < buyIn) {
        showToast(`⚠️ Insufficient points to open this challenge! You have ${curBalance} PTS, but need ${buyIn} PTS.`, 'warning');
        return;
      }
      setUserCoins(curBalance - buyIn, payerName);
      recordTransaction(payerName, 'challenge_stake', buyIn, curBalance - buyIn, `Staked ${buyIn} PTS for challenge (Playing for ${buyIn * 2} PTS)`);
      stakedPlayers.push({ name: payerName, amount: buyIn });
    }
  }

  const list = getChallengesDB();
  const newChal = {
    id: 'ch_' + Date.now().toString(36),
    creator: creatorDisplayName,
    creatorPayer: payerName,
    partner: partnerName || null,
    hasOpenPartner,
    category,
    points,
    buyIn,
    stakedPlayers,
    note,
    isPrivate,
    pin,
    createdTimestamp: Date.now(),
    status: 'open',
    opponent: null,
    opponentPayer: null,
    stakedOpponents: [],
    createdAt: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
  };

  list.unshift(newChal);
  saveChallengesDB(list);
  document.getElementById('newChallengeModal').close();
  renderChallengesBoard();
  updateBettingUI();
  showToast(`Challenge opened! ${buyIn > 0 ? buyIn + ' PTS deducted from each player. Winner gets ' + (buyIn * 2) + ' PTS! ' : ''}Waiting for a challenger.`, 'success');
}

let activeChallengeFilter = 'all';

function filterChallenges(type) {
  activeChallengeFilter = type;
  const filterIds = {
    all: 'chalFilterAll',
    my: 'chalFilterMy',
    open: 'chalFilterOpen',
    partner: 'chalFilterPartner',
    accepted: 'chalFilterAccepted',
    expired: 'chalFilterExpired'
  };
  Object.keys(filterIds).forEach(key => {
    const b = document.getElementById(filterIds[key]);
    if (b) b.classList.toggle('active', key === type);
  });
  renderChallengesBoard();
}

function getOrCreateChallengeMatch(chal) {
  if (!chal || !chal.opponent) return null;
  let match = null;
  if (chal.matchId) {
    match = state.matches.find(m => m.id === chal.matchId);
  }
  if (!match) {
    match = state.matches.find(m =>
      (m.pool === 'CHALLENGE' || !m.pool || m.pool === 'A' || m.pool === 'B') &&
      ((m.a.toLowerCase() === chal.creator.toLowerCase() && m.b.toLowerCase() === chal.opponent.toLowerCase()) ||
       (m.b.toLowerCase() === chal.creator.toLowerCase() && m.a.toLowerCase() === chal.opponent.toLowerCase()))
    );
  }
  if (!match) {
    match = createMatchObj(chal.creator, chal.opponent, 'CHALLENGE');
    match.court = 1;
    state.matches.push(match);
    chal.matchId = match.id;
    saveState();
    const list = getChallengesDB();
    const target = list.find(x => x.id === chal.id);
    if (target) {
      target.matchId = match.id;
      saveChallengesDB(list);
    }
  } else if (!chal.matchId) {
    chal.matchId = match.id;
    const list = getChallengesDB();
    const target = list.find(x => x.id === chal.id);
    if (target) {
      target.matchId = match.id;
      saveChallengesDB(list);
    }
  }
  return match;
}

function launchChallengeUmpire(chalId) {
  if (!requireAuthUser('referee or score matches')) return;
  const list = getChallengesDB();
  const chal = list.find(c => c.id === chalId);
  if (!chal) return;

  const match = getOrCreateChallengeMatch(chal);
  if (!match) return;

  startUmpireMatch(match.id);
}

function enterChallengeQuickScore(chalId) {
  if (!requireAuthUser('enter scores')) return;
  const list = getChallengesDB();
  const chal = list.find(c => c.id === chalId);
  if (!chal) return;

  const match = getOrCreateChallengeMatch(chal);
  if (!match) return;

  openQuickScoreModal(match.id);
}

async function cancelChallenge(chalId) {
  const list = getChallengesDB();
  const chal = list.find(c => c.id === chalId);
  if (!chal) return;

  const canManage = !currentUser || (
    currentUser.name.toLowerCase() === chal.creator.toLowerCase() ||
    (chal.opponent && currentUser.name.toLowerCase() === chal.opponent.toLowerCase()) ||
    currentUser.role === 'admin' || currentUser.role === 'super_admin'
  );

  if (!canManage) {
    showToast('Only challenge participants or an Admin can cancel this challenge.', 'warning');
    return;
  }

  const confirmed = await appConfirm(`Cancel challenge between ${chal.creator}${chal.opponent ? ' and ' + chal.opponent : ''}?`, 'Cancel Challenge', 'Cancel Match', true);
  if (!confirmed) return;

  // Refund points buy-in to participants if not yet concluded
  if (chal.buyIn && chal.buyIn > 0 && !chal.payoutProcessed) {
    if (chal.stakedPlayers && chal.stakedPlayers.length > 0) {
      chal.stakedPlayers.forEach(p => {
        const bal = getUserCoins(p.name);
        setUserCoins(bal + p.amount, p.name);
        recordTransaction(p.name, 'challenge_refund', p.amount, bal + p.amount, `Refunded ${p.amount} PTS for cancelled challenge`);
      });
    } else {
      const creatorPayer = chal.creatorPayer || chal.creator;
      const curCBal = getUserCoins(creatorPayer);
      setUserCoins(curCBal + chal.buyIn, creatorPayer);
      recordTransaction(creatorPayer, 'challenge_refund', chal.buyIn, curCBal + chal.buyIn, `Refunded ${chal.buyIn} PTS for cancelled challenge`);
    }

    if (chal.stakedOpponents && chal.stakedOpponents.length > 0) {
      chal.stakedOpponents.forEach(p => {
        const bal = getUserCoins(p.name);
        setUserCoins(bal + p.amount, p.name);
        recordTransaction(p.name, 'challenge_refund', p.amount, bal + p.amount, `Refunded ${p.amount} PTS for cancelled challenge`);
      });
    } else if (chal.opponent) {
      const oppPayer = chal.opponentPayer || chal.opponent;
      const curOBal = getUserCoins(oppPayer);
      setUserCoins(curOBal + chal.buyIn, oppPayer);
      recordTransaction(oppPayer, 'challenge_refund', chal.buyIn, curOBal + chal.buyIn, `Refunded ${chal.buyIn} PTS for cancelled challenge`);
    }
  }

  if (chal.matchId) refundMatchBets(chal.matchId);
  const updatedList = list.filter(c => c.id !== chalId);
  saveChallengesDB(updatedList);

  if (chal.matchId) {
    state.matches = state.matches.filter(m => m.id !== chal.matchId || m.winner);
    saveState();
  }

  renderChallengesBoard();
  updateBettingUI();
  showToast('Challenge cancelled successfully. Points refunded.', 'info');
}

function copyChallengeInviteLink(chalId) {
  const url = window.location.origin + window.location.pathname + '#challenge=' + chalId;
  if (navigator.clipboard) {
    navigator.clipboard.writeText(url).then(() => {
      showToast('Challenge link copied to clipboard! Share with your opponent.', 'success');
    }).catch(() => {
      prompt('Copy this challenge link:', url);
    });
  } else {
    prompt('Copy this challenge link:', url);
  }
}

function acceptChallenge(id) {
  if (!requireAuthUser('accept challenges')) return;
  const list = getChallengesDB();
  const chal = list.find(c => c.id === id);
  if (!chal) return;

  if (chal.isPrivate && chal.pin) {
    const pinModal = document.getElementById('challengePinPromptModal');
    if (pinModal) {
      document.getElementById('challengePinTargetId').value = id;
      document.getElementById('challengeAcceptPinInput').value = '';
      pinModal.showModal();
      return;
    }
  }
  executeAcceptChallenge(id);
}

function executeAcceptChallenge(id) {
  const list = getChallengesDB();
  const chal = list.find(c => c.id === id);
  if (!chal) return;

  const joinerName = currentUser ? currentUser.name : '';
  if (!joinerName || !joinerName.trim()) {
    showToast('Please sign in to accept challenges.', 'warning');
    return;
  }

  const creatorNames = (chal.creator || '').toLowerCase().split('/').map(s => s.trim());
  const hostPayer = (chal.creatorPayer || '').toLowerCase();
  if (creatorNames.includes(joinerName.toLowerCase()) || hostPayer === joinerName.toLowerCase()) {
    showToast('You are on the challenger team! You cannot play against yourself.', 'warning');
    return;
  }

  // Deduct points buy-in from contender: "if they select 5 then 5 points will be deduct from each player"
  const stakedOpponents = [];
  if (chal.buyIn && chal.buyIn > 0) {
    const curBal = getUserCoins(joinerName);
    if (curBal < chal.buyIn) {
      showToast(`⚠️ Insufficient points to accept this challenge! You need ${chal.buyIn} PTS to join (Your balance: ${curBal} PTS).`, 'warning');
      return;
    }
    setUserCoins(curBal - chal.buyIn, joinerName);
    recordTransaction(joinerName, 'challenge_stake', chal.buyIn, curBal - chal.buyIn, `Staked ${chal.buyIn} PTS to accept challenge vs ${chal.creator} (Playing for ${chal.buyIn * 2} PTS)`);
    stakedOpponents.push({ name: joinerName, amount: chal.buyIn });
  }

  chal.opponent = joinerName.trim();
  chal.opponentPayer = joinerName.trim();
  chal.stakedOpponents = stakedOpponents;

  if (chal.hasOpenPartner) {
    // Challenger team still needs 1 partner to start the doubles match!
    chal.status = 'open';
    saveChallengesDB(list);
    renderChallengesBoard();
    updateBettingUI();
    showToast(`⚔️ Accepted as opponent! Waiting for 1 player to join as ${chal.creator}'s partner to launch match.`, 'success');
    return;
  }

  chal.status = 'accepted';

  // Automatically create match and link
  const newMatch = createMatchObj(chal.creator, chal.opponent, 'CHALLENGE');
  chal.matchId = newMatch.id;
  state.matches.push(newMatch);

  saveChallengesDB(list);
  saveState();
  renderChallengesBoard();
  updateBettingUI();
  showToast(`⚡ Match Accepted! Launching live referee court for ${chal.creator} vs ${joinerName}...`, 'success');
  
  setTimeout(() => {
    startUmpireMatch(newMatch.id);
  }, 400);
}

function joinChallengeAsPartner(id) {
  if (!requireAuthUser('join as doubles partner')) return;
  const list = getChallengesDB();
  const chal = list.find(c => c.id === id);
  if (!chal) return;
  if (chal.status === 'completed' || chal.status === 'expired') {
    showToast('This challenge is no longer open.', 'warning');
    return;
  }
  if (!chal.hasOpenPartner) {
    showToast('This challenge already has a partner!', 'warning');
    return;
  }

  const joinerName = currentUser ? currentUser.name : '';
  if (!joinerName || !joinerName.trim()) {
    showToast('Please sign in to join as partner.', 'warning');
    return;
  }

  const hostName = chal.creatorPayer || chal.creator.split('/')[0].trim();
  if (joinerName.toLowerCase() === hostName.toLowerCase()) {
    showToast('You are the host of this challenge! You cannot join as your own partner.', 'warning');
    return;
  }

  if (chal.opponent && chal.opponent.toLowerCase().split('/').map(s => s.trim()).includes(joinerName.toLowerCase())) {
    showToast('You are already on the opponent team! You cannot be on both sides.', 'warning');
    return;
  }

  // Deduct points buy-in from partner if challenge has a stake
  if (chal.buyIn && chal.buyIn > 0) {
    const curBal = getUserCoins(joinerName);
    if (curBal < chal.buyIn) {
      showToast(`⚠️ Insufficient points to join as partner! You need ${chal.buyIn} PTS (Your balance: ${curBal} PTS).`, 'warning');
      return;
    }
    setUserCoins(curBal - chal.buyIn, joinerName);
    recordTransaction(joinerName, 'challenge_stake', chal.buyIn, curBal - chal.buyIn, `Staked ${chal.buyIn} PTS to join as partner with ${hostName} (Playing for ${chal.buyIn * 2} PTS)`);
    if (!chal.stakedPlayers) chal.stakedPlayers = [];
    chal.stakedPlayers.push({ name: joinerName, amount: chal.buyIn });
  }

  chal.partner = joinerName;
  chal.creator = `${hostName} / ${joinerName}`;
  chal.hasOpenPartner = false;

  // Check if opponent is already present
  if (chal.opponent) {
    chal.status = 'accepted';
    const newMatch = createMatchObj(chal.creator, chal.opponent, 'CHALLENGE');
    chal.matchId = newMatch.id;
    state.matches.push(newMatch);
    saveChallengesDB(list);
    saveState();
    renderChallengesBoard();
    updateBettingUI();
    showToast(`⚡ Team complete! Joined as partner with ${hostName}. Starting match vs ${chal.opponent}!`, 'success');
    setTimeout(() => {
      startUmpireMatch(newMatch.id);
    }, 400);
  } else {
    saveChallengesDB(list);
    renderChallengesBoard();
    updateBettingUI();
    showToast(`🤝 You joined as partner with ${hostName}! Waiting for an opponent team to accept...`, 'success');
  }
}

function renderChallengesBoard() {
  const container = document.getElementById('challengeBoardList');
  if (!container) return;

  const list = getChallengesDB();
  const curUserLower = (currentUser && currentUser.name) ? currentUser.name.toLowerCase() : '';

  const isChallengeParticipant = (c) => {
    if (!curUserLower) return false;
    const cLower = (c.creator || '').toLowerCase();
    const oLower = (c.opponent || '').toLowerCase();
    const pLower = (c.partner || '').toLowerCase();
    const cpLower = (c.creatorPayer || '').toLowerCase();
    const opLower = (c.opponentPayer || '').toLowerCase();
    return cLower.includes(curUserLower) || oLower.includes(curUserLower) || pLower.includes(curUserLower) || cpLower === curUserLower || opLower === curUserLower;
  };

  // Update top metrics dashboard
  const mTotal = list.length;
  const mOpen = list.filter(c => c.status === 'open' && !c.opponent).length;
  const mPartners = list.filter(c => c.status === 'open' && c.category === 'doubles' && c.hasOpenPartner).length;
  const mPoints = list.reduce((acc, c) => {
    const buyIn = c.buyIn || 0;
    const pCount = (c.stakedPlayers ? c.stakedPlayers.length : 1) + (c.stakedOpponents ? c.stakedOpponents.length : 0);
    return acc + (buyIn * pCount);
  }, 0);

  const elTot = document.getElementById('chalMetricTotal');
  const elOpn = document.getElementById('chalMetricOpen');
  const elPrt = document.getElementById('chalMetricPartners');
  const elPts = document.getElementById('chalMetricPointsPool');
  if (elTot) elTot.textContent = mTotal;
  if (elOpn) elOpn.textContent = mOpen;
  if (elPrt) elPrt.textContent = mPartners;
  if (elPts) elPts.textContent = `${mPoints} PTS`;

  // Update filter pill counts
  const cAll = document.getElementById('chalCountAll');
  const cMy = document.getElementById('chalCountMy');
  const cOpen = document.getElementById('chalCountOpen');
  const cPart = document.getElementById('chalCountPartner');
  const cAcc = document.getElementById('chalCountAccepted');
  const cExp = document.getElementById('chalCountExpired');

  if (cAll) cAll.textContent = list.length;
  if (cMy) cMy.textContent = list.filter(isChallengeParticipant).length;
  if (cOpen) cOpen.textContent = list.filter(c => c.status === 'open').length;
  if (cPart) cPart.textContent = list.filter(c => c.status === 'open' && c.hasOpenPartner).length;
  if (cAcc) cAcc.textContent = list.filter(c => c.status === 'accepted').length;
  if (cExp) cExp.textContent = list.filter(c => c.status === 'completed' || c.status === 'expired').length;

  let filtered = [...list];
  const searchInput = document.getElementById('challengeSearchInput');
  const query = (searchInput ? searchInput.value : '').trim().toLowerCase();
  if (query) {
    filtered = filtered.filter(c =>
      (c.creator && c.creator.toLowerCase().includes(query)) ||
      (c.opponent && c.opponent.toLowerCase().includes(query)) ||
      (c.note && c.note.toLowerCase().includes(query)) ||
      (c.court && String(c.court).toLowerCase().includes(query))
    );
  }

  // Active status / view filter
  if (activeChallengeFilter === 'my') {
    filtered = filtered.filter(isChallengeParticipant);
  } else if (activeChallengeFilter === 'open') {
    filtered = filtered.filter(c => c.status === 'open');
  } else if (activeChallengeFilter === 'partner') {
    filtered = filtered.filter(c => c.status === 'open' && c.hasOpenPartner);
  } else if (activeChallengeFilter === 'accepted') {
    filtered = filtered.filter(c => c.status === 'accepted');
  } else if (activeChallengeFilter === 'expired') {
    filtered = filtered.filter(c => c.status === 'completed' || c.status === 'expired');
  }

  // Category filter dropdown
  const catFilter = document.getElementById('chalCategoryFilter');
  if (catFilter && catFilter.value !== 'all') {
    filtered = filtered.filter(c => c.category === catFilter.value);
  }

  // Sort selector
  const sortSelect = document.getElementById('chalSortSelect');
  const sortBy = sortSelect ? sortSelect.value : 'newest';
  if (sortBy === 'points_desc') {
    filtered.sort((a, b) => (b.buyIn || 0) - (a.buyIn || 0));
  } else if (sortBy === 'points_asc') {
    filtered.sort((a, b) => (a.buyIn || 0) - (b.buyIn || 0));
  } else {
    filtered.sort((a, b) => (b.createdTimestamp || 0) - (a.createdTimestamp || 0));
  }

  if (!filtered.length) {
    container.innerHTML = `
      <div class="empty-state-card" style="grid-column:1/-1;padding:44px 20px;text-align:center;background:rgba(0,0,0,0.22);border:1.5px dashed var(--clr-border);border-radius:var(--radius-md);">
        <div class="empty-state-icon" style="font-size:3.2rem;margin-bottom:12px;">🏸</div>
        <div class="empty-state-title" style="font-size:1.2rem;font-weight:900;color:var(--clr-text);margin-bottom:6px;">No Challenges Found</div>
        <div class="empty-state-desc" style="font-size:0.86rem;color:var(--clr-text-muted);max-width:460px;margin:0 auto 16px;line-height:1.5;">
          ${query ? 'No challenges match your search. Try clearing the search query or switching filter tabs.' : 'No active matches in this view. Post a public challenge and invite players to compete!'}
        </div>
        <button class="btn btn-primary btn-sm" style="font-weight:800;gap:8px;padding:8px 20px;background:linear-gradient(135deg, #10b981, #059669);" onclick="openNewChallengeModal()">
          <svg class="icon icon-xs" viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
          <span>Open a Challenge</span>
        </button>
      </div>
    `;
    return;
  }

  container.innerHTML = filtered.map(c => {
    let match = null;
    if (c.status === 'accepted' || c.status === 'completed') {
      match = getOrCreateChallengeMatch(c);
      if (match && match.winner && c.status !== 'completed') {
        c.status = 'completed';
        c.winner = match.winner === 'a' ? match.a : match.b;
      }
      if (match && match.winner && (c.buyIn || 0) > 0 && !c.payoutProcessed) {
        c.payoutProcessed = true;
        c.status = 'completed';
        c.winner = match.winner === 'a' ? match.a : match.b;
        const winPoints = c.buyIn * 2;
        const winnerMembers = c.winner.includes('/') ? c.winner.split('/').map(s => s.trim()).filter(Boolean) : [c.winner.trim()];
        const wallets = getWalletsDB();
        winnerMembers.forEach(mem => {
          wallets[mem] = (wallets[mem] || 0) + winPoints;
          recordTransaction(mem, 'challenge_win', winPoints, wallets[mem], `🏆 Won challenge prize (${winPoints} PTS)`);
        });
        saveWalletsDB(wallets);
        saveChallengesDB(list);
        updateBettingUI();
      }
    }

    const curName = (currentUser && currentUser.name) ? currentUser.name.toLowerCase() : '';
    const creatorNames = (c.creator || '').toLowerCase().split('/').map(s => s.trim());
    const isCreator = curName && (creatorNames.includes(curName) || (c.creatorPayer && c.creatorPayer.toLowerCase() === curName));
    const opponentNames = (c.opponent || '').toLowerCase().split('/').map(s => s.trim());
    const isOpponent = curName && (opponentNames.includes(curName) || (c.opponentPayer && c.opponentPayer.toLowerCase() === curName));
    const isMyMatch = isCreator || isOpponent;
    const isAdmin = currentUser && (currentUser.role === 'admin' || currentUser.role === 'super_admin');
    const canCancel = isMyMatch || isAdmin;
    const scoreStr = (match && match.sets && match.sets.length) ? match.sets.map(s => `${s.score[0]}–${s.score[1]}`).join(' | ') : '';
    const winnerName = c.winner || (match ? (match.winner === 'a' ? match.a : match.b) : null);

    const avatarA = typeof getPlayerAvatarHtml === 'function' ? getPlayerAvatarHtml(c.creator, 38, winnerName === c.creator) : '';
    const avatarB = c.opponent && typeof getPlayerAvatarHtml === 'function' ? getPlayerAvatarHtml(c.opponent, 38, winnerName === c.opponent) : '';

    const statusBorderClass = c.status === 'open' ? (c.hasOpenPartner && !c.opponent ? 'open-status partner-status' : 'open-status') : (c.status === 'completed' ? 'completed-status' : 'accepted-status');
    const badgeType = c.status === 'open' ? (c.hasOpenPartner && !c.opponent ? 'partner' : 'open') : c.status;
    const badgeText = c.status === 'open' ? (c.hasOpenPartner && c.opponent ? '⏳ Needs Partner' : (c.hasOpenPartner ? '🤝 Open Partner Slot' : '● Open')) : (c.status === 'completed' ? '✓ Completed' : '⚡ In Progress');

    return `
      <div class="challenge-card ${statusBorderClass}" data-challenge-id="${c.id}">
        <!-- Top Meta Header -->
        <div class="challenge-card-header">
          <div class="challenge-badges-row">
            <span class="challenge-badge ${badgeType}">
              ${badgeText}
            </span>
            <span style="font-weight:700;color:var(--clr-text);font-size:0.75rem;background:rgba(255,255,255,0.06);padding:3px 8px;border-radius:4px;border:1px solid rgba(255,255,255,0.08);display:inline-flex;align-items:center;gap:4px;">
              🏸 ${c.category === 'doubles' ? 'Doubles (2v2)' : 'Singles (1v1)'} · ${c.points || 15} pts
            </span>
            ${(c.buyIn && c.buyIn > 0) ? `
              <span style="font-weight:800;color:var(--clr-gold);font-size:0.75rem;background:rgba(245,158,11,0.15);padding:3px 8px;border-radius:4px;border:1px solid rgba(245,158,11,0.35);display:inline-flex;align-items:center;gap:4px;">
                💰 ${c.buyIn} PTS each · Winner gets ${c.buyIn * 2} PTS
              </span>
            ` : `
              <span style="font-weight:700;color:var(--clr-text-muted);font-size:0.75rem;background:rgba(255,255,255,0.06);padding:3px 8px;border-radius:4px;border:1px solid rgba(255,255,255,0.08);display:inline-flex;align-items:center;gap:4px;">
                🤝 Friendly (0 PTS)
              </span>
            `}
            ${isMyMatch ? '<span style="font-size:0.72rem;color:var(--clr-gold);font-weight:800;background:rgba(245,158,11,0.14);padding:3px 8px;border-radius:4px;border:1px solid rgba(245,158,11,0.3);">★ YOUR MATCH</span>' : ''}
            ${c.isPrivate ? '<span class="challenge-pin-badge" style="font-size:0.72rem;padding:3px 8px;border-radius:4px;">🔒 PIN</span>' : ''}
          </div>
          <div class="challenge-meta-actions">
            <span class="challenge-timestamp">🕒 ${escapeHtml(c.createdAt || 'Today')}</span>
            <button onclick="openChallengeQrModal('${c.id}')" title="Scan QR Code to join" class="btn btn-ghost btn-xs" style="padding:4px 8px;border:1px solid var(--clr-border);">
              📱 QR
            </button>
            ${canCancel ? `
              <button onclick="cancelChallenge('${c.id}')" title="Cancel challenge" class="btn btn-ghost btn-xs" style="padding:4px 8px;color:#f87171;border:1px solid rgba(239,68,68,0.25);" onmouseover="this.style.background='rgba(239,68,68,0.15)'" onmouseout="this.style.background='transparent'">
                <svg class="icon icon-xs" viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
              </button>
            ` : ''}
          </div>
        </div>

        ${c.court ? `
          <div style="font-size:0.78rem;font-weight:700;color:var(--clr-cyan);display:flex;align-items:center;gap:6px;background:rgba(6,182,212,0.08);padding:4px 10px;border-radius:5px;border:1px solid rgba(6,182,212,0.2);width:fit-content;">
            <svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
            <span>Court ${escapeHtml(c.court)} · Ready for match</span>
          </div>
        ` : ''}

        <!-- Competitor Matchup Arena (Vertical Two-Row Stacked Layout) -->
        <div class="challenge-arena">
          <!-- Challenger Row -->
          <div class="challenge-competitor-row">
            <div class="challenge-player-meta">
              ${avatarA}
              <div class="challenge-player-text">
                <div class="challenge-player-name">
                  <span>${escapeHtml(c.creator)}</span>
                  ${winnerName === c.creator ? '<span title="Winner" style="color:var(--clr-gold);">👑</span>' : ''}
                </div>
                <div class="challenge-player-role">
                  <span style="color:var(--clr-green);font-weight:700;">● Challenger</span>
                  <span>· Host${c.partner ? ' & Partner' : ''}</span>
                </div>
              </div>
            </div>
            ${c.category === 'doubles' && c.hasOpenPartner ? `
              <div style="flex-shrink:0;">
                ${!isCreator && !isOpponent ? `
                  <button class="btn btn-primary btn-xs" style="gap:5px;background:linear-gradient(135deg, #10b981, #059669);font-weight:800;box-shadow:0 2px 8px rgba(16,185,129,0.3);" onclick="event.stopPropagation();joinChallengeAsPartner('${c.id}')">
                    <span>🤝 Join as Partner${c.buyIn > 0 ? ` (${c.buyIn} PTS)` : ''}</span>
                  </button>
                ` : `
                  <span class="badge" style="background:rgba(16,185,129,0.12);color:var(--clr-green);border:1px dashed var(--clr-green);font-size:0.72rem;padding:3px 8px;">
                    ${isCreator ? '⏳ Open Partner Slot (Waiting...)' : 'Open Partner Slot'}
                  </span>
                `}
              </div>
            ` : ''}
            ${match && match.sets && match.sets.length ? `
              <div style="font-family:monospace;font-size:1.15rem;font-weight:800;color:${winnerName === c.creator ? 'var(--clr-green)' : 'var(--clr-text)'};">
                ${match.sets.map(s => s.score[0]).join('-')}
              </div>
            ` : ''}
          </div>

          <!-- Divider -->
          <div class="challenge-vs-divider">
            <span class="challenge-vs-pill">
              ${c.status === 'completed' && scoreStr ? scoreStr : `VS · FIRST TO ${c.points || 15} PTS`}
            </span>
          </div>

          <!-- Opponent Row OR Open Slot -->
          ${c.opponent ? `
            <div class="challenge-competitor-row">
              <div class="challenge-player-meta">
                ${avatarB}
                <div class="challenge-player-text">
                  <div class="challenge-player-name">
                    <span>${escapeHtml(c.opponent)}</span>
                    ${winnerName === c.opponent ? '<span title="Winner" style="color:var(--clr-gold);">👑</span>' : ''}
                  </div>
                  <div class="challenge-player-role">
                    <span style="color:#60a5fa;font-weight:700;">● Contender</span>
                    <span>· Accepted</span>
                  </div>
                </div>
              </div>
              ${match && match.sets && match.sets.length ? `
                <div style="font-family:monospace;font-size:1.15rem;font-weight:800;color:${winnerName === c.opponent ? 'var(--clr-green)' : 'var(--clr-text)'};">
                  ${match.sets.map(s => s.score[1]).join('-')}
                </div>
              ` : ''}
            </div>
          ` : `
            <div class="challenge-open-slot-box" ${(!isCreator && !isOpponent) ? `onclick="acceptChallenge('${c.id}')" style="cursor:pointer;"` : ''}>
              <div style="display:flex;align-items:center;gap:12px;min-width:0;">
                <div style="width:38px;height:38px;border-radius:50%;border:1.5px dashed var(--clr-green);display:flex;align-items:center;justify-content:center;color:var(--clr-green);font-weight:800;font-size:1.1rem;flex-shrink:0;background:rgba(16,185,129,0.08);">
                  +
                </div>
                <div style="min-width:0;">
                  <div style="font-weight:800;font-size:0.92rem;color:var(--clr-green);">
                    Open Slot — Waiting for Opponent${c.category === 'doubles' ? ' Team' : ''}
                  </div>
                  <div style="font-size:0.74rem;color:var(--clr-text-muted);">
                    ${isCreator ? 'Share your invite link with a player or opponent' : 'Click to accept this challenge & take the court!'}
                  </div>
                </div>
              </div>
              ${(!isCreator && !isOpponent) ? `
                <button class="btn btn-primary btn-xs" style="flex-shrink:0;gap:4px;" onclick="event.stopPropagation();acceptChallenge('${c.id}')">
                  <span>Accept${c.buyIn > 0 ? ` (${c.buyIn} PTS)` : ''}</span>
                </button>
              ` : `
                <span style="font-size:0.7rem;font-weight:700;color:var(--clr-text-muted);background:rgba(255,255,255,0.06);padding:3px 8px;border-radius:4px;flex-shrink:0;">
                  Waiting...
                </span>
              `}
            </div>
          `}
        </div>

        ${c.note ? `
          <div style="font-size:0.8rem;color:var(--clr-text-muted);display:flex;align-items:flex-start;gap:8px;background:rgba(255,255,255,0.02);padding:8px 12px;border-radius:var(--radius-xs);border-left:2px solid var(--clr-border);">
            <span style="font-size:0.9rem;">💬</span>
            <span style="line-height:1.4;">${escapeHtml(c.note)}</span>
          </div>
        ` : ''}

        ${c.status === 'completed' && winnerName ? `
          <div style="padding:8px 12px;background:rgba(16,185,129,0.12);border-radius:var(--radius-xs);color:var(--clr-green);font-size:0.88rem;font-weight:700;display:flex;justify-content:space-between;align-items:center;border:1px solid rgba(16,185,129,0.25);">
            <span style="display:flex;align-items:center;gap:6px;">
              <span>🏆</span>
              <span>Winner: <strong>${escapeHtml(winnerName)}</strong></span>
              ${c.buyIn > 0 ? `<span style="font-size:0.75rem;color:var(--clr-gold);background:rgba(245,158,11,0.15);padding:2px 7px;border-radius:4px;border:1px solid rgba(245,158,11,0.3);margin-left:4px;">+${c.buyIn * 2} PTS Pot Won</span>` : ''}
            </span>
            ${scoreStr ? `<span style="font-family:monospace;font-weight:800;font-size:1rem;color:var(--clr-gold);">${scoreStr}</span>` : ''}
          </div>
        ` : ''}

        <!-- Action Toolbar -->
        <div style="display:flex;gap:10px;align-items:center;margin-top:auto;padding-top:12px;border-top:1px solid rgba(255,255,255,0.06);">
          ${c.status === 'open' ? `
            ${c.hasOpenPartner && c.opponent ? `
              ${!isCreator && !isOpponent ? `
                <button class="btn btn-primary btn-sm" style="flex:1;justify-content:center;font-weight:800;gap:8px;font-size:0.92rem;background:#10b981;border-color:#10b981;" onclick="joinChallengeAsPartner('${c.id}')">
                  <span>🤝 Join as Partner & Play Now${c.buyIn > 0 ? ` (${c.buyIn} PTS)` : ''}</span>
                </button>
              ` : `
                <button class="btn btn-primary btn-sm" style="flex:1;gap:6px;justify-content:center;font-weight:700;" onclick="copyChallengeInviteLink('${c.id}')">
                  <svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>
                  <span>Invite Partner to Complete Match</span>
                </button>
              `}
            ` : (c.hasOpenPartner && !c.opponent ? `
              ${!isCreator ? `
                <div style="display:flex;gap:8px;flex:1;flex-wrap:wrap;">
                  <button class="btn btn-primary btn-sm" style="flex:1;min-width:140px;justify-content:center;font-weight:800;gap:6px;font-size:0.86rem;background:linear-gradient(135deg, #10b981, #059669);border-color:#10b981;" onclick="joinChallengeAsPartner('${c.id}')">
                    <span>🤝 Join as Partner${c.buyIn > 0 ? ` (${c.buyIn} PTS)` : ''}</span>
                  </button>
                  <button class="btn btn-ghost btn-sm" style="flex:1;min-width:140px;justify-content:center;font-weight:800;gap:6px;font-size:0.86rem;border:1px solid #3b82f6;color:#60a5fa;" onclick="acceptChallenge('${c.id}')">
                    <span>⚔️ Accept vs Team${c.buyIn > 0 ? ` (${c.buyIn} PTS)` : ''}</span>
                  </button>
                </div>
              ` : `
                <button class="btn btn-primary btn-sm" style="flex:1;gap:6px;justify-content:center;font-weight:700;" onclick="copyChallengeInviteLink('${c.id}')">
                  <svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>
                  <span>Share Invite Link</span>
                </button>
                <button class="btn btn-ghost btn-sm" style="gap:6px;border:1px solid var(--clr-border);" onclick="openChallengeQrModal('${c.id}')" title="Scan QR Code to join">
                  <span>📱 QR</span>
                </button>
              `}
            ` : `
              ${isCreator ? `
                <button class="btn btn-primary btn-sm" style="flex:1;gap:6px;justify-content:center;font-weight:700;" onclick="copyChallengeInviteLink('${c.id}')">
                  <svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>
                  <span>Share Invite Link</span>
                </button>
                <button class="btn btn-ghost btn-sm" style="gap:6px;border:1px solid var(--clr-border);" onclick="openChallengeQrModal('${c.id}')" title="Scan QR Code to join">
                  <span>📱 QR</span>
                </button>
              ` : `
                <button class="btn btn-primary btn-sm" style="flex:1;justify-content:center;font-weight:800;gap:8px;font-size:0.92rem;background:#10b981;border-color:#10b981;" onclick="acceptChallenge('${c.id}')">
                  <svg class="icon icon-xs" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
                  <span>Accept Challenge & Play Now${c.buyIn > 0 ? ` (${c.buyIn} PTS)` : ''}</span>
                </button>
              `}
            `)}
          ` : (c.status === 'completed' ? `
            <button class="btn btn-ghost btn-sm" style="flex:1;min-width:120px;gap:6px;justify-content:center;border:1px solid var(--clr-border);" onclick="openScorecardModal('${match ? match.id : ''}')">
              <svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
              <span>Scorecard</span>
            </button>
            <button class="btn btn-primary btn-sm" style="gap:6px;font-weight:700;" onclick="instantRematchChallenge('${c.id}')" title="Play an instant rematch">
              <span>⚡ Rematch</span>
            </button>
            <button class="btn btn-ghost btn-sm" style="gap:6px;border:1px solid var(--clr-border);" onclick="shareChallengeWhatsApp('${c.id}')" title="Share via WhatsApp">
              <span>💬 WhatsApp</span>
            </button>
            <button class="btn btn-ghost btn-sm" style="gap:6px;border:1px solid var(--clr-border);" onclick="copyChallengeInviteLink('${c.id}')" title="Share Match Result">
              <svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>
              <span>Share</span>
            </button>
          ` : `
            <button class="btn btn-primary btn-sm" style="flex:1;min-width:130px;gap:6px;font-weight:800;justify-content:center;" onclick="launchChallengeUmpire('${c.id}')">
              <svg class="icon icon-xs" viewBox="0 0 24 24"><polygon points="12 2 15 8 22 9 17 14 18 21 12 17 6 21 7 14 2 9 9 8 12 2"/></svg>
              <span>Score / Referee Live</span>
            </button>
            <button class="btn btn-ghost btn-sm" style="gap:6px;font-weight:700;justify-content:center;border:1px solid var(--clr-border);" onclick="enterChallengeQuickScore('${c.id}')" title="Enter Final Score">
              <svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M11 4H4a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
              <span>Quick Score</span>
            </button>
          `)}
        </div>
      </div>
    `;
  }).join('');
}
let liveSyncChannel = null;
if ('BroadcastChannel' in window) {
  try {
    liveSyncChannel = new BroadcastChannel('badminton_cup_live_sync');
    liveSyncChannel.onmessage = (e) => {
      if (e.data && e.data.type === 'STATE_UPDATED') {
        if (typeof loadSavedState === 'function') loadSavedState(false);
        if (typeof refreshCurrentViews === 'function') refreshCurrentViews();
      }
    };
  } catch (e) {}
}

function broadcastStateChange() {
  if (liveSyncChannel) {
    try {
      liveSyncChannel.postMessage({ type: 'STATE_UPDATED', timestamp: Date.now() });
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
  const selects = [
    document.getElementById('tournamentSelectMore'),
    document.getElementById('tournamentSelectHeader')
  ].filter(Boolean);
  if (!selects.length) return;
  const list = getTournamentsDB();
  const currentId = state.tournamentId || 'main';

  const html = list.map(t =>
    `<option value="${t.id}" ${t.id === currentId ? 'selected' : ''}>${window.escapeHtml ? window.escapeHtml(t.title) : t.title}</option>`
  ).join('') + `<option value="__NEW__">+ New Tournament...</option>`;

  selects.forEach(s => { s.innerHTML = html; });
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
      if (pts === 15) {
        if (leadingScore === 14) {
          textToSpeak += ". Game ball";
        } else if (leadingScore === 13) {
          textToSpeak += ". Hope ball";
        }
      } else {
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
    safeLocalStorageSet(STORAGE_KEY_USERS, JSON.stringify(users));
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
  populateQuickLoginUsers();
  document.getElementById('authModal').showModal();
}

function populateQuickLoginUsers() {
  const container = document.getElementById('quickLoginUsersList');
  const section = document.getElementById('quickLoginUsersSection');
  if (!container) return;
  const users = (typeof getUsersDB === 'function') ? getUsersDB() : [];
  const players = users.filter(u => u.name && u.name.toLowerCase() !== 'rashed');
  if (players.length > 0) {
    if (section) section.style.display = 'block';
    container.innerHTML = players.map(p => `
      <button type="button" class="btn btn-ghost btn-xs" onclick="loginAsUser('${escapeHtml(p.name)}')">${escapeHtml(p.name)}</button>
    `).join('');
  } else {
    if (section) section.style.display = 'none';
    container.innerHTML = '';
  }
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
  let users = getUsersDB();
  const dummyNames = new Set([
    'parag das', 'rifat haque', 'rifat tariq', 'jobayer', 'shewa', 'sazedul',
    'nur', 'ofi', 'sifat', 'sajeeb', 'jakir', 'saiful', 'al emran', 'toufiq', 'abir',
    'parag', 'rifat'
  ]);

  // Purge any pre-seeded dummy users so only real registered users & admin exist
  users = users.filter(u => !dummyNames.has((u.name || '').trim().toLowerCase()));

  // Ensure Rashed (Admin) exists
  let rashed = users.find(u => (u.name || '').toLowerCase() === 'rashed');
  if (!rashed) {
    rashed = {
      id: 1001,
      name: 'Rashed',
      email: 'rashed@badminton.local',
      role: 'admin',
      status: 'active',
      feeStatus: 'paid',
      elo: 1650,
      dominantHand: 'Right-Handed',
      club: 'Tournament Director',
      avatar: 'R',
      createdAt: 'Initial'
    };
    users.unshift(rashed);
  } else {
    rashed.role = 'admin';
    rashed.club = 'Tournament Director';
  }

  saveUsersDB(users);

  // Purge any dummy seeded challenges
  let chalList = getChallengesDB();
  chalList = chalList.filter(c => {
    const cLower = (c.creator || '').toLowerCase();
    const oLower = (c.opponent || '').toLowerCase();
    const isDummy = Array.from(dummyNames).some(dn => cLower.includes(dn) || oLower.includes(dn)) || (c.id && c.id.startsWith('chal_seed_'));
    return !isDummy;
  });
  saveChallengesDB(chalList);

  // If no currentUser is saved, default to Rashed as Admin
  if (!currentUser) {
    setCurrentUser(rashed);
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

function handleUserAvatarClick() {
  if (currentUser) {
    showScreen('playerHubScreen');
  } else {
    openAuthModal();
  }
}

function handleAuthBtnClick() {
  if (currentUser) {
    logoutUser();
  } else {
    openAuthModal();
  }
}

function updateUserUI() {
  updateRoleVisibility();
  const nameLabel = document.getElementById('headerUsername');
  const roleBadge = document.getElementById('headerUserRole');
  const avatar = document.getElementById('headerAvatar');
  const authBtn = document.getElementById('authBtn');
  const userInfo = document.getElementById('headerUserInfo');
  const userPill = document.getElementById('headerUserPill');
  const navHub = document.getElementById('navPlayerHubBtn');
  const tabHub = document.getElementById('tabNavPlayerHub');
  const mobHub = document.getElementById('mobNavPlayerHub');

  if (currentUser) {
    if (userPill) userPill.style.display = 'inline-flex';
    if (nameLabel) {
      nameLabel.textContent = currentUser.name;
      nameLabel.style.display = 'inline-block';
    }
    if (userInfo) userInfo.style.display = 'flex';
    if (avatar) {
      avatar.style.display = 'inline-flex';
      if (currentUser.photoUrl) {
        avatar.innerHTML = `<img src="${currentUser.photoUrl}" style="width:100%;height:100%;object-fit:cover;border-radius:inherit;" alt="${escapeHtml(currentUser.name)}">`;
        avatar.style.background = 'transparent';
      } else {
        avatar.textContent = currentUser.avatar || currentUser.name.charAt(0).toUpperCase();
        avatar.style.background = (currentUser.role === 'admin' || currentUser.role === 'super_admin') ? 'var(--clr-gold)' : 'var(--clr-green)';
      }
      avatar.style.color = '#ffffff';
    }
    if (roleBadge) {
      roleBadge.style.display = 'inline-block';
      roleBadge.textContent = (currentUser.role || 'PLAYER').toUpperCase();
      roleBadge.style.color = (currentUser.role === 'admin' || currentUser.role === 'super_admin') ? 'var(--clr-gold)' : 'var(--clr-green)';
    }
    if (authBtn) {
      authBtn.textContent = 'Sign Out';
      authBtn.className = 'btn btn-ghost btn-xs';
      authBtn.title = 'Sign Out of Badminton Cup';
      authBtn.style.display = 'inline-flex';
    }
    if (navHub) navHub.style.display = 'inline-flex';
    if (tabHub) tabHub.style.display = 'inline-flex';
    if (mobHub) mobHub.style.display = 'inline-flex';
  } else {
    if (userPill) userPill.style.display = 'none';
    if (nameLabel) {
      nameLabel.textContent = 'Guest';
      nameLabel.style.display = 'none';
    }
    if (userInfo) userInfo.style.display = 'none';
    if (avatar) {
      avatar.style.display = 'none';
    }
    if (roleBadge) {
      roleBadge.style.display = 'none';
    }
    if (authBtn) {
      authBtn.textContent = 'Sign In';
      authBtn.className = 'btn btn-primary btn-xs';
      authBtn.title = 'Sign In to Badminton Cup';
      authBtn.style.display = 'inline-flex';
    }
    if (navHub) navHub.style.display = 'none';
    if (tabHub) tabHub.style.display = 'none';
    if (mobHub) mobHub.style.display = 'none';
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

async function deleteUserRecord(userId) {
  const users = getUsersDB();
  const user = users.find(u => u.id === userId);
  if (!user) return;

  const inActiveMatches = state.matches && state.matches.some(m => m.a.toLowerCase() === user.name.toLowerCase() || m.b.toLowerCase() === user.name.toLowerCase());
  if (inActiveMatches) {
    showToast(`Cannot delete ${user.name}: athlete has scheduled matches in the current tournament. Forfeit matches or reset tournament first.`, 'error');
    return;
  }

  const confirmed = await appConfirm(`Delete athlete '${user.name}' completely from tournament registry?`, 'Delete Athlete Record', 'Delete Athlete', true);
  if (confirmed) {
    saveUsersDB(users.filter(u => u.id !== userId));
    logAdminAudit(`Deleted user record for ${user.name}`);
    renderAdminDashboard();
    showToast(`Athlete ${user.name} deleted.`);
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

  const otherPool = currentPickerTargetPool === 'A' ? 'rosterBInput' : 'rosterAInput';
  const otherPoolPlayers = new Set(
    (typeof extractIndividualPlayers === 'function' ? extractIndividualPlayers(getCleanRoster(otherPool)) : getCleanRoster(otherPool)).map(p => p.toLowerCase())
  );
  const currentPool = currentPickerTargetPool === 'A' ? 'rosterAInput' : 'rosterBInput';
  const currentPoolPlayers = new Set(
    (typeof extractIndividualPlayers === 'function' ? extractIndividualPlayers(getCleanRoster(currentPool)) : getCleanRoster(currentPool)).map(p => p.toLowerCase())
  );

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
    const inOtherPool = otherPoolPlayers.has(u.name.toLowerCase());
    const inCurrentPool = currentPoolPlayers.has(u.name.toLowerCase());
    const disabled = inOtherPool || inCurrentPool;

    return `
      <div class="player-picker-item ${isSelected ? 'selected' : ''} ${disabled ? 'disabled' : ''}"
        style="${disabled ? 'opacity:0.5;background:rgba(239,68,68,0.05);border-color:rgba(239,68,68,0.25);cursor:not-allowed;' : ''}"
        onclick="handlePickerItemClick('${u.name.replace(/'/g, "\\'")}', ${inOtherPool}, ${inCurrentPool})">
        <div style="display:flex;align-items:center;gap:10px;min-width:0;flex:1;">
          <div class="user-avatar" style="width:28px;height:28px;flex-shrink:0;">${u.avatar || u.name.charAt(0)}</div>
          <div style="min-width:0;">
            <div style="font-weight:bold;font-size:0.9rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">${escapeHtml(u.name)}</div>
            <div style="font-size:0.75rem;color:var(--clr-text-muted);">${escapeHtml(u.club || 'Independent')} · Elo ${u.elo || 1200}</div>
          </div>
        </div>
        <div style="display:flex;align-items:center;gap:8px;flex-shrink:0;">
          ${inOtherPool ? `
            <span class="badge" style="background:rgba(239,68,68,0.18);color:#f87171;font-size:0.68rem;font-weight:800;">ALREADY IN POOL ${currentPickerTargetPool === 'A' ? 'B' : 'A'}</span>
          ` : (inCurrentPool ? `
            <span class="badge" style="background:rgba(16,185,129,0.18);color:#34d399;font-size:0.68rem;font-weight:800;">IN POOL ${currentPickerTargetPool}</span>
          ` : `
            <span class="user-role-badge ${u.status === 'active' ? 'badge-active' : 'badge-invited'}">${u.status}</span>
            <span style="display:inline-flex;align-items:center;justify-content:center;width:18px;height:18px;border-radius:4px;border:1px solid var(--clr-border);background:${isSelected ? 'var(--clr-green)' : 'transparent'};color:#fff;">${isSelected ? svgIcon('check', 'icon-xs') : ''}</span>
          `)}
        </div>
      </div>
    `;
  }).join('');

  document.getElementById('pickerSelectedCount').textContent = `${selectedPickerIds.size} athletes selected`;
}

function handlePickerItemClick(name, inOtherPool, inCurrentPool) {
  if (inOtherPool) {
    showToast(`Athlete "${name}" is already in Pool ${currentPickerTargetPool === 'A' ? 'B' : 'A'}. The same player cannot be added to both sides!`, 'error');
    return;
  }
  if (inCurrentPool) {
    showToast(`Athlete "${name}" is already in Pool ${currentPickerTargetPool}.`, 'warning');
    return;
  }
  togglePickerSelection(name);
}

function togglePickerSelection(name) {
  const otherPool = currentPickerTargetPool === 'A' ? 'rosterBInput' : 'rosterAInput';
  const otherPoolPlayers = new Set(
    (typeof extractIndividualPlayers === 'function' ? extractIndividualPlayers(getCleanRoster(otherPool)) : getCleanRoster(otherPool)).map(p => p.toLowerCase())
  );
  if (otherPoolPlayers.has(name.toLowerCase())) {
    showToast(`Athlete "${name}" is already in Pool ${currentPickerTargetPool === 'A' ? 'B' : 'A'} and cannot be added to both sides!`, 'error');
    return;
  }

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

  const otherPool = currentPickerTargetPool === 'A' ? 'rosterBInput' : 'rosterAInput';
  const otherPoolPlayers = new Set(
    (typeof extractIndividualPlayers === 'function' ? extractIndividualPlayers(getCleanRoster(otherPool)) : getCleanRoster(otherPool)).map(p => p.toLowerCase())
  );

  const selectedArr = Array.from(selectedPickerIds);
  const duplicates = selectedArr.filter(p => otherPoolPlayers.has(p.toLowerCase()));
  if (duplicates.length > 0) {
    showToast(`Cannot add: Athlete(s) ${duplicates.join(', ')} are already in Pool ${currentPickerTargetPool === 'A' ? 'B' : 'A'}. The same player cannot be added to both sides!`, 'error');
    return;
  }

  const targetTextarea = document.getElementById(currentPickerTargetPool === 'A' ? 'rosterAInput' : 'rosterBInput');
  const existing = targetTextarea.value.split('\n').map(s => s.trim()).filter(s => s.length > 0);

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

let tempProfilePhotoDataUrl = null;

function renderProfileAvatarPreview() {
  const preview = document.getElementById('profileEditAvatarPreview');
  const editAvatar = document.getElementById('profileEditAvatar');
  const badgeVal = (editAvatar ? editAvatar.value.trim() : '') || (currentUser?.name?.charAt(0) || 'U');

  if (!preview) return;
  if (tempProfilePhotoDataUrl) {
    preview.innerHTML = `<img src="${tempProfilePhotoDataUrl}" style="width:100%;height:100%;object-fit:cover;border-radius:inherit;" alt="Avatar">`;
    preview.style.background = 'transparent';
  } else {
    preview.innerHTML = escapeHtml(badgeVal);
    preview.style.background = (currentUser && (currentUser.role === 'admin' || currentUser.role === 'super_admin')) ? 'var(--clr-gold)' : 'var(--clr-green)';
  }
}

function updateProfileAvatarPreview(val) {
  tempProfilePhotoDataUrl = '';
  renderProfileAvatarPreview();
}

function selectPresetAvatarBadge(badge) {
  const editAvatar = document.getElementById('profileEditAvatar');
  if (editAvatar) editAvatar.value = badge;
  tempProfilePhotoDataUrl = '';
  renderProfileAvatarPreview();
}

function removeProfilePhoto() {
  tempProfilePhotoDataUrl = '';
  renderProfileAvatarPreview();
  showToast('Profile photo removed. Badge/initial will be displayed.', 'info');
}

function handleProfilePhotoSelected(event) {
  const file = event.target.files && event.target.files[0];
  if (!file) return;

  if (!file.type.startsWith('image/')) {
    showToast('Please select a valid image file (PNG, JPG, or WebP).', 'warning');
    return;
  }

  const reader = new FileReader();
  reader.onload = function(e) {
    const img = new Image();
    img.onload = function() {
      try {
        const canvas = document.createElement('canvas');
        const MAX_SIZE = 256;
        const minDim = Math.min(img.width, img.height);
        const startX = (img.width - minDim) / 2;
        const startY = (img.height - minDim) / 2;

        canvas.width = MAX_SIZE;
        canvas.height = MAX_SIZE;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(img, startX, startY, minDim, minDim, 0, 0, MAX_SIZE, MAX_SIZE);

        tempProfilePhotoDataUrl = canvas.toDataURL('image/jpeg', 0.88);
        renderProfileAvatarPreview();
        showToast('Photo uploaded! Tap "Save Changes" to save to your profile.', 'info');
      } catch (err) {
        showToast('Error processing image.', 'error');
      }
    };
    img.src = e.target.result;
  };
  reader.readAsDataURL(file);
}

function openProfileSettingsModal() {
  if (!currentUser) {
    showToast('Please sign in to update your profile.', 'warning');
    openAuthModal();
    return;
  }
  const modal = document.getElementById('userProfileSettingsModal');
  if (!modal) return;

  tempProfilePhotoDataUrl = currentUser.photoUrl || null;

  const editAvatar = document.getElementById('profileEditAvatar');
  const editName = document.getElementById('profileEditName');
  const editEmail = document.getElementById('profileEditEmail');
  const editClub = document.getElementById('profileEditClub');
  const editHand = document.getElementById('profileEditHand');
  const editStyle = document.getElementById('profileEditStyle');
  const editPass = document.getElementById('profileEditPasscode');

  if (editAvatar) editAvatar.value = currentUser.avatar || currentUser.name.charAt(0).toUpperCase();
  if (editName) editName.value = currentUser.name;
  if (editEmail) editEmail.value = currentUser.email || '';
  if (editClub) editClub.value = currentUser.club || '';
  if (editHand) editHand.value = currentUser.dominantHand || 'Right-Handed';
  if (editStyle) editStyle.value = currentUser.style || 'All-Rounder';
  if (editPass) editPass.value = '';

  renderProfileAvatarPreview();

  modal.showModal();
}

function saveProfileSettings(e) {
  if (e && e.preventDefault) e.preventDefault();
  if (!currentUser) return;

  const editName = document.getElementById('profileEditName');
  const editEmail = document.getElementById('profileEditEmail');
  const editClub = document.getElementById('profileEditClub');
  const editHand = document.getElementById('profileEditHand');
  const editStyle = document.getElementById('profileEditStyle');
  const editAvatar = document.getElementById('profileEditAvatar');
  const editPass = document.getElementById('profileEditPasscode');

  const newName = (editName ? editName.value.trim() : '') || currentUser.name;
  const oldName = currentUser.name;

  currentUser.name = newName;
  currentUser.email = editEmail ? editEmail.value.trim() : (currentUser.email || '');
  currentUser.club = editClub ? editClub.value.trim() : (currentUser.club || '');
  currentUser.dominantHand = editHand ? editHand.value : (currentUser.dominantHand || 'Right-Handed');
  currentUser.style = editStyle ? editStyle.value : (currentUser.style || 'All-Rounder');
  currentUser.avatar = (editAvatar && editAvatar.value.trim()) ? editAvatar.value.trim() : newName.charAt(0).toUpperCase();

  if (tempProfilePhotoDataUrl !== null) {
    currentUser.photoUrl = tempProfilePhotoDataUrl || null;
  }

  if (editPass && editPass.value.trim()) {
    currentUser.passcode = editPass.value.trim();
  }

  // Update Users DB
  const users = getUsersDB();
  const uIdx = users.findIndex(u => u.id === currentUser.id || u.name.toLowerCase() === oldName.toLowerCase());
  if (uIdx !== -1) {
    users[uIdx] = { ...users[uIdx], ...currentUser };
  } else {
    users.push(currentUser);
  }
  saveUsersDB(users);

  // If name changed, keep roster and match references in sync
  if (oldName !== newName) {
    if (state.players) state.players = state.players.map(p => p === oldName ? newName : p);
    if (state.poolA) state.poolA = state.poolA.map(p => p === oldName ? newName : p);
    if (state.poolB) state.poolB = state.poolB.map(p => p === oldName ? newName : p);
    state.matches.forEach(m => {
      if (m.a === oldName) m.a = newName;
      if (m.b === oldName) m.b = newName;
    });
    saveState();
  }

  localStorage.setItem(STORAGE_KEY_AUTH, JSON.stringify(currentUser));
  updateUserUI();
  renderPlayerHub();
  renderLeaderboard();

  const modal = document.getElementById('userProfileSettingsModal');
  if (modal) modal.close();
  showToast('Profile photo and details saved successfully!', 'success');
}

function renderPlayerHub() {
  if (!currentUser) {
    const nextCard = document.getElementById('playerNextFixtureCard');
    if (nextCard) {
      nextCard.innerHTML = `
        <div style="text-align:center;padding:24px;">
          <div style="font-size:1.1rem;font-weight:700;color:var(--clr-text);margin-bottom:8px;">Sign in to view your personal hub</div>
          <p style="color:var(--clr-text-muted);font-size:0.85rem;margin-bottom:16px;">Track your Elo rating, upcoming matches, coin balance, and match records.</p>
          <button class="btn btn-primary btn-sm" onclick="openAuthModal()">Sign In Now</button>
        </div>
      `;
    }
    return;
  }

  // Profile Header Elements
  const pName = document.getElementById('playerHubName');
  const pSubtitle = document.getElementById('playerHubSubtitle');
  const pAvatar = document.getElementById('playerHubAvatarLarge');
  const pRoleBadge = document.getElementById('playerHubRoleBadge');

  if (pName) pName.textContent = currentUser.name;
  if (pSubtitle) {
    pSubtitle.textContent = `${currentUser.club || 'Independent Athlete'} · ${currentUser.dominantHand || 'Right-Handed'} · ${currentUser.style || 'All-Rounder'}`;
  }
  if (pAvatar) {
    if (currentUser.photoUrl) {
      pAvatar.innerHTML = `<img src="${currentUser.photoUrl}" style="width:100%;height:100%;object-fit:cover;border-radius:inherit;" alt="${escapeHtml(currentUser.name)}">`;
      pAvatar.style.background = 'transparent';
    } else {
      pAvatar.textContent = currentUser.avatar || currentUser.name.charAt(0).toUpperCase();
      pAvatar.style.background = (currentUser.role === 'admin' || currentUser.role === 'super_admin') ? 'var(--clr-gold)' : 'var(--clr-green)';
    }
  }
  if (pRoleBadge) {
    pRoleBadge.textContent = (currentUser.role || 'PLAYER').toUpperCase();
    pRoleBadge.className = (currentUser.role === 'admin' || currentUser.role === 'super_admin') ? 'badge badge-gold' : 'badge badge-green';
  }

  // 1. Elo Rating Stack
  const eloVal = currentUser.elo || 1200;
  const eloEl = document.getElementById('playerHubElo');
  const tierBadge = document.getElementById('playerHubTierBadge');
  const eloBar = document.getElementById('playerHubEloBar');
  const eloSub = document.getElementById('playerHubEloSub');

  let tier = 'SILVER';
  let tierColor = 'var(--clr-silver)';
  if (eloVal >= 1350) { tier = 'MASTER'; tierColor = 'var(--clr-red)'; }
  else if (eloVal >= 1280) { tier = 'DIAMOND'; tierColor = 'var(--clr-blue)'; }
  else if (eloVal >= 1200) { tier = 'GOLD'; tierColor = 'var(--clr-gold)'; }

  if (eloEl) eloEl.textContent = eloVal;
  if (tierBadge) {
    tierBadge.textContent = tier;
    tierBadge.style.color = tierColor;
  }
  if (eloBar) {
    const pct = Math.min(100, Math.max(10, Math.round(((eloVal - 900) / 700) * 100)));
    eloBar.style.width = `${pct}%`;
    eloBar.style.background = tierColor;
  }

  // Career match metrics for this player
  const myMatches = state.matches.filter(m => m.winner && (m.a === currentUser.name || m.b === currentUser.name));
  const wonCount = myMatches.filter(m => (m.winner === 'a' && m.a === currentUser.name) || (m.winner === 'b' && m.b === currentUser.name)).length;
  const lostCount = myMatches.length - wonCount;
  const winRate = myMatches.length > 0 ? Math.round((wonCount / myMatches.length) * 100) : 0;

  // 2. Match Records & Win Rate Stack
  const winRateEl = document.getElementById('playerHubWinRate');
  const mCountEl = document.getElementById('playerHubMatchesCount');
  const winRateBar = document.getElementById('playerHubWinRateBar');
  const streakBadge = document.getElementById('playerHubStreakBadge');

  if (winRateEl) winRateEl.textContent = `${winRate}%`;
  if (mCountEl) mCountEl.textContent = `${myMatches.length} played (${wonCount}W - ${lostCount}L)`;
  if (winRateBar) winRateBar.style.width = `${winRate}%`;

  // Streak calculation
  let currentStreak = 0;
  let streakType = '';
  for (let i = myMatches.length - 1; i >= 0; i--) {
    const m = myMatches[i];
    const isWin = (m.winner === 'a' && m.a === currentUser.name) || (m.winner === 'b' && m.b === currentUser.name);
    const type = isWin ? 'W' : 'L';
    if (!streakType) {
      streakType = type;
      currentStreak = 1;
    } else if (streakType === type) {
      currentStreak++;
    } else {
      break;
    }
  }
  if (streakBadge) {
    if (streakType === 'W' && currentStreak > 1) {
      streakBadge.textContent = `🔥 ${currentStreak}W Streak`;
      streakBadge.style.background = 'rgba(34,197,94,0.18)';
      streakBadge.style.color = 'var(--clr-green)';
    } else if (streakType === 'L' && currentStreak > 1) {
      streakBadge.textContent = `${currentStreak}L Cold`;
      streakBadge.style.background = 'rgba(239,68,68,0.18)';
      streakBadge.style.color = 'var(--clr-red)';
    } else {
      streakBadge.textContent = 'Active Contender';
      streakBadge.style.background = 'rgba(255,255,255,0.08)';
      streakBadge.style.color = 'var(--clr-text-muted)';
    }
  }

  // 3. Points Differential Stack
  let ptsScored = 0;
  let ptsConceded = 0;
  myMatches.forEach(m => {
    (m.sets || []).forEach(s => {
      const score = s.score || [0, 0];
      if (m.a === currentUser.name) {
        ptsScored += Number(score[0]) || 0;
        ptsConceded += Number(score[1]) || 0;
      } else {
        ptsScored += Number(score[1]) || 0;
        ptsConceded += Number(score[0]) || 0;
      }
    });
  });
  const netDiff = ptsScored - ptsConceded;
  const pDiffEl = document.getElementById('playerHubPointDiff');
  const pBreakdownEl = document.getElementById('playerHubPointBreakdown');
  const pBar = document.getElementById('playerHubPointBar');

  if (pDiffEl) {
    pDiffEl.textContent = (netDiff > 0 ? `+${netDiff}` : `${netDiff}`);
    pDiffEl.style.color = netDiff >= 0 ? 'var(--clr-green)' : 'var(--clr-red)';
  }
  if (pBreakdownEl) {
    pBreakdownEl.textContent = `${ptsScored} pts scored · ${ptsConceded} conceded`;
  }
  if (pBar) {
    const totalPts = ptsScored + ptsConceded;
    const scoredPct = totalPts > 0 ? Math.round((ptsScored / totalPts) * 100) : 50;
    pBar.style.width = `${scoredPct}%`;
    pBar.style.background = netDiff >= 0 ? 'var(--clr-green)' : 'var(--clr-red)';
  }

  // 4. Coins & Predictions Stack
  const coinBal = getUserCoins();
  const coinEl = document.getElementById('playerHubCoinWallet');
  const betSub = document.getElementById('playerHubBettingSub');
  const betBar = document.getElementById('playerHubBettingBar');

  const bets = typeof getBetsDB === 'function' ? getBetsDB() : [];
  const userBets = bets.filter(b => b.userId === currentUser.id || !b.userId);
  const finishedBets = userBets.filter(b => b.status === 'won' || b.status === 'lost');
  const wonBets = finishedBets.filter(b => b.status === 'won').length;
  const betAccuracy = finishedBets.length > 0 ? Math.round((wonBets / finishedBets.length) * 100) : 0;

  if (coinEl) coinEl.textContent = coinBal.toLocaleString();
  if (betSub) {
    betSub.textContent = `${userBets.length} wagers · ${betAccuracy}% win accuracy`;
  }
  if (betBar) betBar.style.width = `${betAccuracy}%`;

  // 5. Form Guide Stack (last 5)
  const formGuideEl = document.getElementById('playerHubFormGuide');
  if (formGuideEl) {
    if (!myMatches.length) {
      formGuideEl.textContent = '—';
    } else {
      formGuideEl.innerHTML = myMatches.slice(-5).map(m => {
        const isWin = (m.winner === 'a' && m.a === currentUser.name) || (m.winner === 'b' && m.b === currentUser.name);
        return `<span style="display:inline-block;padding:2px 7px;border-radius:4px;font-weight:800;font-size:0.85rem;margin:0 2px;background:${isWin ? 'rgba(34,197,94,0.18)' : 'rgba(239,68,68,0.18)'};color:${isWin ? 'var(--clr-green)' : 'var(--clr-red)'};border:1px solid ${isWin ? 'rgba(34,197,94,0.35)' : 'rgba(239,68,68,0.35)'};">${isWin ? 'W' : 'L'}</span>`;
      }).join(' ');
    }
  }

  // 6. Medals Stack
  const lbDb = getLeaderboardDB();
  const myLb = lbDb[currentUser.name] || {};
  const goldCount = myLb.gold || 0;
  const silverCount = myLb.silver || 0;
  const bronzeCount = myLb.bronze || 0;

  const gEl = document.getElementById('playerHubGoldCount');
  const sEl = document.getElementById('playerHubSilverCount');
  const bEl = document.getElementById('playerHubBronzeCount');
  if (gEl) gEl.textContent = goldCount;
  if (sEl) sEl.textContent = silverCount;
  if (bEl) bEl.textContent = bronzeCount;

  // Rank in tournament
  const allPlayersSorted = Object.values(lbDb).sort((x, y) => (y.gold || 0) - (x.gold || 0) || (y.won || 0) - (x.won || 0) || (y.ptsDiff || 0) - (x.ptsDiff || 0));
  const myRankIdx = allPlayersSorted.findIndex(p => p.name === currentUser.name);
  if (eloSub) {
    eloSub.textContent = `BWF SaaS Rating · Rank #${myRankIdx !== -1 ? myRankIdx + 1 : '--'}`;
  }

  // Tournament Registration & Points Buy-In Card
  const buyInCard = document.getElementById('playerTournamentBuyInCard');
  if (buyInCard) {
    const fee = typeof state.entryFee === 'number' ? state.entryFee : (parseInt(state.entryFee) || 50);
    const inA = (state.poolA || []).some(p => p.toLowerCase().includes(currentUser.name.toLowerCase()));
    const inB = (state.poolB || []).some(p => p.toLowerCase().includes(currentUser.name.toLowerCase()));
    const rosterA = getCleanRoster('rosterAInput');
    const rosterB = getCleanRoster('rosterBInput');
    const inRosterA = rosterA.some(p => p.toLowerCase().includes(currentUser.name.toLowerCase()));
    const inRosterB = rosterB.some(p => p.toLowerCase().includes(currentUser.name.toLowerCase()));
    const isEnrolled = inA || inB || inRosterA || inRosterB;
    const enrolledPool = (inA || inRosterA) ? 'Pool A' : ((inB || inRosterB) ? 'Pool B' : 'Registered');

    if (isEnrolled) {
      buyInCard.innerHTML = `
        <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;padding:4px 0;">
          <div>
            <div style="font-size:0.75rem;font-weight:900;color:var(--clr-green);letter-spacing:0.08em;text-transform:uppercase;">Tournament Registration Status</div>
            <div style="font-size:1.15rem;font-weight:800;color:var(--clr-text);margin-top:2px;">✅ Enrolled in Official Tournament (${enrolledPool})</div>
            <div style="font-size:0.82rem;color:var(--clr-text-muted);">Entry buy-in: ${fee} PTS paid from wallet</div>
          </div>
          <span class="badge badge-green" style="font-size:0.8rem;padding:6px 12px;">ACTIVE ATHLETE</span>
        </div>
      `;
    } else {
      buyInCard.innerHTML = `
        <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;padding:4px 0;">
          <div>
            <div style="font-size:0.75rem;font-weight:900;color:var(--clr-gold);letter-spacing:0.08em;text-transform:uppercase;">Tournament Registration & Buy-in</div>
            <div style="font-size:1.15rem;font-weight:800;color:var(--clr-text);margin-top:2px;">Join the Upcoming Badminton Cup</div>
            <div style="font-size:0.82rem;color:var(--clr-text-muted);">Entry Buy-in: <strong>${fee} PTS</strong> · Your Balance: <strong>${getUserCoins(currentUser.name)} PTS</strong></div>
          </div>
          <button class="btn btn-primary btn-sm" onclick="joinTournamentWithPoints()" style="display:inline-flex;align-items:center;gap:6px;">
            <span>🪙 Join Tournament (${fee} PTS)</span>
          </button>
        </div>
      `;
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
            <div style="font-size:0.85rem;color:var(--clr-text-muted);margin-top:2px;">Stage: Pool ${nextMatch.pool || 'A'} · Assigned to <strong>Court ${nextMatch.court || 1}</strong></div>
          </div>
          <div style="display:flex;gap:8px;">
            <button class="btn btn-primary btn-sm" onclick="startUmpireMatch('${nextMatch.id}')">Start Match Live &rarr;</button>
          </div>
        </div>
      `;
    } else {
      nextCard.innerHTML = `
        <div style="text-align:center;padding:12px;color:var(--clr-text-muted);font-size:0.86rem;">
          No active fixtures scheduled for <strong>${currentUser.name}</strong> right now. Check back when the next round is seeded!
        </div>
      `;
    }
  }

  // Complete Match History Table
  const tbody = document.getElementById('playerHubMatchesTableBody');
  if (tbody) {
    if (!myMatches.length) {
      tbody.innerHTML = `<tr><td colspan="6" style="text-align:center;padding:20px;color:var(--clr-text-muted);">No completed matches yet. Play matches or referee fixtures to record scores!</td></tr>`;
    } else {
      tbody.innerHTML = myMatches.slice().reverse().map(m => {
        const isWin = (m.winner === 'a' && m.a === currentUser.name) || (m.winner === 'b' && m.b === currentUser.name);
        const opp = (m.a === currentUser.name) ? m.b : m.a;
        const scoreStr = (m.sets || []).map(s => `${s.score[0]}-${s.score[1]}`).join(' | ');
        return `
          <tr>
            <td>Pool ${m.pool || 'A'}</td>
            <td><strong>${opp}</strong></td>
            <td><span style="font-family:monospace;color:var(--clr-gold);font-weight:700;">${scoreStr || '—'}</span></td>
            <td>
              <span style="display:inline-block;padding:2px 8px;border-radius:4px;font-weight:800;font-size:0.75rem;background:${isWin ? 'rgba(34,197,94,0.18)' : 'rgba(239,68,68,0.18)'};color:${isWin ? 'var(--clr-green)' : 'var(--clr-red)'};">
                ${isWin ? 'VICTORY' : 'DEFEAT'}
              </span>
            </td>
            <td>Court ${m.court || 1}</td>
            <td>
              <button class="btn btn-ghost btn-xs" onclick="openScorecardModal('${m.id}')">View</button>
            </td>
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
function getUserCoins(targetUsername = null) {
  const username = targetUsername || (currentUser ? currentUser.name : 'Guest');
  const wallets = getWalletsDB();
  if (wallets[username] === undefined) {
    const stats = getLeaderboardDB()[username];
    const matchPts = (stats && stats.totalPts) ? stats.totalPts : 0;
    wallets[username] = 100 + matchPts; // 100 free starter coins/points + match points earned
    saveWalletsDB(wallets);
  }
  return wallets[username];
}

function setUserCoins(amount, targetUsername = null) {
  const username = targetUsername || (currentUser ? currentUser.name : 'Guest');
  const wallets = getWalletsDB();
  wallets[username] = Math.max(0, amount);
  saveWalletsDB(wallets);
  updateBettingUI();
}

const STORAGE_KEY_DAILY_CLAIM = 'badminton_cup_daily_claim_v4';
const DAILY_CLAIM_COOLDOWN_MS = 24 * 60 * 60 * 1000; // 24 hours cooldown

function getDailyClaimsDB() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY_DAILY_CLAIM)) || {};
  } catch (e) {
    return {};
  }
}

function saveDailyClaimsDB(db) {
  try {
    localStorage.setItem(STORAGE_KEY_DAILY_CLAIM, JSON.stringify(db));
  } catch (e) {}
}

function getRemainingDailyClaimTime(username) {
  if (!username) return 0;
  const db = getDailyClaimsDB();
  const lastClaim = db[username];
  if (!lastClaim) return 0;
  const elapsed = Date.now() - Number(lastClaim);
  if (elapsed >= DAILY_CLAIM_COOLDOWN_MS) return 0;
  return DAILY_CLAIM_COOLDOWN_MS - elapsed;
}

function formatRemainingTime(ms) {
  const totalSec = Math.floor(ms / 1000);
  const hours = Math.floor(totalSec / 3600);
  const mins = Math.floor((totalSec % 3600) / 60);
  if (hours > 0) {
    return `${hours}h ${mins}m`;
  }
  return `${Math.max(1, mins)}m`;
}

function updateClaimButtonUI() {
  const modal = document.getElementById('coinBalanceModal');
  if (!modal) return;
  const claimBtn = document.getElementById('btnClaimDailyBonus') || modal.querySelector('button[onclick*="claimDailyBonus"]') || modal.querySelector('button[onclick*="openAuthModal"]');
  if (!claimBtn) return;

  if (!currentUser) {
    claimBtn.disabled = false;
    claimBtn.className = 'btn btn-primary btn-md';
    claimBtn.style.opacity = '1';
    claimBtn.style.cursor = 'pointer';
    claimBtn.innerHTML = '<span>🔒 Sign In to Claim 50 Free Bonus Coins</span>';
    claimBtn.setAttribute('onclick', "document.getElementById('coinBalanceModal').close();openAuthModal();");
    return;
  }

  const remaining = getRemainingDailyClaimTime(currentUser.name);
  if (remaining > 0) {
    const formatted = formatRemainingTime(remaining);
    claimBtn.disabled = true;
    claimBtn.className = 'btn btn-ghost btn-md';
    claimBtn.style.opacity = '0.65';
    claimBtn.style.cursor = 'not-allowed';
    claimBtn.innerHTML = `<span>⏳ Claimed Today · Next in ${formatted}</span>`;
    claimBtn.setAttribute('onclick', `showToast('⏳ Daily bonus already claimed! Next bonus available in ${formatted}.', 'info')`);
  } else {
    claimBtn.disabled = false;
    claimBtn.className = 'btn btn-primary btn-md';
    claimBtn.style.opacity = '1';
    claimBtn.style.cursor = 'pointer';
    claimBtn.innerHTML = '<span>🎁 Claim Daily Bonus (+50 Free Coins)</span>';
    claimBtn.setAttribute('onclick', 'claimDailyBonus()');
  }
}

function claimDailyBonus() {
  if (!requireAuthUser('claim daily bonus coins')) return;
  const username = currentUser.name;
  const remaining = getRemainingDailyClaimTime(username);
  if (remaining > 0) {
    const formatted = formatRemainingTime(remaining);
    showToast(`⏳ Daily bonus already claimed! Next bonus in ${formatted}.`, 'warning');
    updateClaimButtonUI();
    return;
  }

  const current = getUserCoins();
  const bonus = 50;
  setUserCoins(current + bonus);

  // Record claim timestamp in database
  const claims = getDailyClaimsDB();
  claims[username] = Date.now();
  saveDailyClaimsDB(claims);

  recordTransaction(username, 'bonus', bonus, current + bonus, 'Daily reward bonus (+50 coins)');
  const bigCount = document.getElementById('coinModalBigCount');
  if (bigCount) bigCount.textContent = (current + bonus).toLocaleString();

  updateClaimButtonUI();
  showToast('🎁 Claimed 50 Free Bonus Coins! Next bonus in 24 hours.', 'success');
  playChimeSound('win');
}

function openCoinBalanceModal() {
  const modal = document.getElementById('coinBalanceModal');
  if (!modal) return;
  const coins = getUserCoins();
  const bigCount = document.getElementById('coinModalBigCount');
  if (bigCount) bigCount.textContent = coins.toLocaleString();

  updateClaimButtonUI();
  modal.showModal();
}

function updateBettingUI() {
  const coins = getUserCoins();
  const headerCoinEl = document.getElementById('headerCoinCount');
  if (headerCoinEl) headerCoinEl.textContent = coins.toLocaleString();
  const betBalanceEl = document.getElementById('bettingModalUserBalance');
  if (betBalanceEl) betBalanceEl.textContent = coins.toLocaleString();
}

function openBettingModal(matchId) {
  if (!requireAuthUser('place match predictions')) return;
  const match = state.matches.find(m => m.id === matchId);
  if (!match) return;

  if (match.winner) {
    showToast('Predictions are closed: match already completed.', 'warning');
    return;
  }
  if (match.id === state.currentMatchId || (match.sets && match.sets.some(s => (s.score[0] > 0 || s.score[1] > 0)))) {
    showToast('Predictions are closed: match is currently live on court.', 'warning');
    return;
  }

  activeBetMatch = match;
  activeBetSide = 'a';

  document.getElementById('betModalMatchId').value = match.id;
  document.getElementById('betModalTeamAName').textContent = match.a;
  document.getElementById('betModalTeamBName').textContent = match.b;
  document.getElementById('betModalTeamABtn').textContent = `Predict ${match.a} (2.0x Double)`;
  document.getElementById('betModalTeamBBtn').textContent = `Predict ${match.b} (2.0x Double)`;
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
  if (!requireAuthUser('place match predictions')) return;
  if (!activeBetMatch) return;

  if (activeBetMatch.winner || (activeBetMatch.sets && activeBetMatch.sets.some(s => s.score[0] > 0 || s.score[1] > 0))) {
    showToast('Predictions are closed for this match.', 'warning');
    return;
  }

  const amount = Math.floor(parseInt(document.getElementById('betModalAmountInput')?.value, 10));
  if (isNaN(amount) || amount < 1) {
    showToast('Minimum prediction wager is 1 point.', 'warning');
    return;
  }

  const coins = getUserCoins();
  if (coins < amount) {
    showToast(`Insufficient points! You have ${coins} PTS. Claim bonus points in your wallet.`, 'warning');
    return;
  }

  const username = currentUser ? currentUser.name : 'Guest';
  const teamName = (activeBetSide === 'a') ? activeBetMatch.a : activeBetMatch.b;
  // Guaranteed Double Points (2.0x) for match predictions
  const odds = 2.0;

  setUserCoins(coins - amount);
  recordTransaction(username, 'bet_placed', amount, coins - amount, `Placed prediction wager of ${amount} PTS on ${teamName} (Playing for ${amount * 2} PTS)`);

  const bets = getBetsDB();
  bets.push({
    id: 'bet_' + Date.now(),
    matchId: activeBetMatch.id,
    username,
    teamName,
    side: activeBetSide,
    amount,
    odds: 2.0,
    status: 'pending',
    placedAt: new Date().toLocaleTimeString()
  });
  saveBetsDB(bets);

  document.getElementById('matchBettingModal').close();
  showToast(`Placed ${amount} PTS prediction on ${teamName}! Double payout (${amount * 2} PTS) on win.`, 'success');
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
        // Double points payout
        const payout = Math.round(b.amount * 2);
        b.payout = payout;

        const wallets = getWalletsDB();
        wallets[b.username] = (wallets[b.username] || 0) + payout;
        saveWalletsDB(wallets);
        recordTransaction(b.username, 'bet_won', payout, wallets[b.username], `🎉 Won double points prediction (${payout} PTS) on match ${match.a} vs ${match.b}`);

        if (b.username === currentUsername) {
          showToast(`🎉 Congratulations! You won double points (${payout} PTS) on ${b.teamName}!`, 'success');
          playChimeSound('win');
        }
      } else {
        b.status = 'lost';
        b.payout = 0;
        recordTransaction(b.username, 'bet_lost', b.amount, getUserCoins(b.username), `Lost prediction on match ${match.a} vs ${match.b}`);
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

  // 1. Tournament Overview KPIs
  const totalMatches = state.matches.length;
  const completedMatches = state.matches.filter(m => !!m.winner).length;
  const pctCompleted = totalMatches > 0 ? Math.round((completedMatches / totalMatches) * 100) : 0;

  let totalPts = 0;
  state.matches.forEach(m => {
    (m.sets || []).forEach(s => {
      totalPts += (Number(s.score[0]) || 0) + (Number(s.score[1]) || 0);
    });
  });

  const kpiMatches = document.getElementById('analyticsKpiMatches');
  const kpiMatchesSub = document.getElementById('analyticsKpiMatchesSub');
  const kpiPoints = document.getElementById('analyticsKpiPoints');
  const kpiPlayers = document.getElementById('analyticsKpiPlayers');

  if (kpiMatches) kpiMatches.textContent = `${completedMatches} / ${totalMatches}`;
  if (kpiMatchesSub) kpiMatchesSub.textContent = `${pctCompleted}% fixtures completed`;
  if (kpiPoints) kpiPoints.textContent = `${totalPts} pts`;
  if (kpiPlayers) kpiPlayers.textContent = `${state.players ? state.players.length : 16}`;

  // 2. Dropdowns Roster
  const db = getLeaderboardDB();
  const allNames = Array.from(new Set([
    ...Object.keys(db),
    ...(state.poolA || []),
    ...(state.poolB || []),
    ...(state.players || [])
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
    <div style="display:grid;grid-template-columns:1fr 140px 1fr;align-items:center;background:rgba(255,255,255,0.03);border:1px solid var(--clr-border);border-radius:var(--radius-sm);padding:20px;margin-bottom:20px;">
      <div style="text-align:center;">
        <div style="width:48px;height:48px;border-radius:50%;background:var(--clr-green);color:#fff;display:inline-flex;align-items:center;justify-content:center;font-size:1.3rem;font-weight:900;margin-bottom:8px;">${pA.charAt(0).toUpperCase()}</div>
        <div style="font-size:1.15rem;font-weight:900;color:var(--clr-text);">${pA}</div>
        <div style="font-size:0.8rem;color:var(--clr-gold);font-weight:700;">${eloA} Elo Rating</div>
        <div style="font-size:1.6rem;font-weight:900;color:var(--clr-green);margin-top:6px;">${winsA}</div>
        <div style="font-size:0.72rem;color:var(--clr-text-muted);text-transform:uppercase;">H2H Wins</div>
      </div>

      <div style="text-align:center;border-left:1px solid var(--clr-border);border-right:1px solid var(--clr-border);padding:0 12px;">
        <div style="font-size:0.75rem;font-weight:800;color:var(--clr-text-muted);text-transform:uppercase;">Direct Meetings</div>
        <div style="font-family:var(--font-display);font-size:2rem;font-weight:900;color:var(--clr-gold);">${h2hMatches.length}</div>
        <div style="font-size:0.75rem;color:var(--clr-text-muted);">Matches Played</div>
      </div>

      <div style="text-align:center;">
        <div style="width:48px;height:48px;border-radius:50%;background:var(--clr-blue);color:#fff;display:inline-flex;align-items:center;justify-content:center;font-size:1.3rem;font-weight:900;margin-bottom:8px;">${pB.charAt(0).toUpperCase()}</div>
        <div style="font-size:1.15rem;font-weight:900;color:var(--clr-text);">${pB}</div>
        <div style="font-size:0.8rem;color:var(--clr-gold);font-weight:700;">${eloB} Elo Rating</div>
        <div style="font-size:1.6rem;font-weight:900;color:var(--clr-blue);margin-top:6px;">${winsB}</div>
        <div style="font-size:0.72rem;color:var(--clr-text-muted);text-transform:uppercase;">H2H Wins</div>
      </div>
    </div>

    <!-- Comparative Metric Gauges -->
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:20px;">
      <div class="card" style="padding:14px;">
        <div style="display:flex;justify-content:space-between;font-size:0.75rem;font-weight:700;margin-bottom:6px;">
          <span>${winRateA}% Win Rate</span>
          <span style="color:var(--clr-text-muted);">Career Win %</span>
          <span>${winRateB}% Win Rate</span>
        </div>
        <div style="height:8px;background:rgba(255,255,255,0.08);border-radius:999px;overflow:hidden;display:flex;">
          <div style="width:${winRateA + winRateB > 0 ? (winRateA / (winRateA + winRateB)) * 100 : 50}%;background:var(--clr-green);"></div>
          <div style="flex:1;background:var(--clr-blue);"></div>
        </div>
      </div>

      <div class="card" style="padding:14px;">
        <div style="display:flex;justify-content:space-between;font-size:0.75rem;font-weight:700;margin-bottom:6px;">
          <span>${statsA.ptsDiff >= 0 ? '+' : ''}${statsA.ptsDiff || 0} Diff</span>
          <span style="color:var(--clr-text-muted);">Points Differential</span>
          <span>${statsB.ptsDiff >= 0 ? '+' : ''}${statsB.ptsDiff || 0} Diff</span>
        </div>
        <div style="height:8px;background:rgba(255,255,255,0.08);border-radius:999px;overflow:hidden;display:flex;">
          <div style="width:${eloPctA}%;background:var(--clr-gold);"></div>
          <div style="flex:1;background:rgba(255,255,255,0.2);"></div>
        </div>
      </div>
    </div>

    <!-- Historical Direct Encounters -->
    <div>
      <div style="font-size:0.8rem;font-weight:800;color:var(--clr-text);text-transform:uppercase;letter-spacing:0.04em;margin-bottom:10px;">Encounter Logs (${pA} vs ${pB})</div>
      ${!h2hMatches.length ? `
        <div style="text-align:center;padding:16px;background:rgba(255,255,255,0.02);border:1px dashed var(--clr-border);border-radius:var(--radius-sm);color:var(--clr-text-muted);font-size:0.82rem;">
          No previous direct head-to-head matches on record between these two athletes yet.
        </div>
      ` : `
        <div style="display:flex;flex-direction:column;gap:8px;">
          ${h2hMatches.map(m => {
            const winnerName = m.winner === 'a' ? m.a : m.b;
            const scoreStr = (m.sets || []).map(s => `${s.score[0]}-${s.score[1]}`).join(' | ');
            return `
              <div style="display:flex;justify-content:space-between;align-items:center;background:rgba(255,255,255,0.03);border:1px solid var(--clr-border);border-radius:var(--radius-sm);padding:10px 14px;flex-wrap:wrap;gap:8px;">
                <div>
                  <span style="font-weight:800;color:${winnerName === pA ? 'var(--clr-green)' : 'var(--clr-blue)'};">${winnerName} won</span>
                  <span style="font-size:0.75rem;color:var(--clr-text-muted);margin-left:8px;">Pool ${m.pool || 'A'} · Court ${m.court || 1}</span>
                </div>
                <div style="font-family:monospace;font-size:0.9rem;font-weight:700;color:var(--clr-gold);">${scoreStr}</div>
                <button class="btn btn-ghost btn-xs" onclick="openScorecardModal('${m.id}')">Scorecard</button>
              </div>
            `;
          }).join('')}
        </div>
      `}
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

/* ═══════════════════════════════════════════════════
   AUTHENTICATION & ROLE-BASED ACCESS CONTROL
═══════════════════════════════════════════════════ */
function requireAuthUser(actionName, callback) {
  if (!currentUser) {
    showToast(`Please sign in to ${actionName}.`, 'warning');
    openAuthModal();
    return false;
  }
  if (callback && typeof callback === 'function') {
    callback(currentUser);
  }
  return true;
}

function updateRoleVisibility() {
  const isAdmin = isAdminUser();
  const isLogged = !!currentUser;

  document.body.classList.toggle('role-admin', isAdmin);
  document.body.classList.toggle('role-player', isLogged && !isAdmin);
  document.body.classList.toggle('role-guest', !isLogged);

  document.querySelectorAll('.admin-only-item').forEach(el => {
    if (isAdmin) {
      if (el.tagName === 'BUTTON' && el.classList.contains('more-card-item')) {
        el.style.display = 'flex';
      } else if (el.tagName === 'BUTTON' && el.classList.contains('btn')) {
        el.style.display = 'inline-flex';
      } else {
        el.style.display = '';
      }
    } else {
      el.style.setProperty('display', 'none', 'important');
    }
  });
}

function isAdminUser() {
  return !!(currentUser && (currentUser.role === 'admin' || currentUser.role === 'super_admin'));
}

function requireAdmin(actionName, onAllowed) {
  if (isAdminUser()) {
    onAllowed();
    return;
  }
  showToast(`${actionName} is restricted to Admin (Rashed).`, 'error');
}

function handleSetupNav() {
  requireAdmin('Tournament Setup & Roster', () => showScreen('setupScreen'));
}

function handleDraftNav() {
  requireAdmin('Pool Draw Machine', () => showScreen('draftScreen'));
}

function handleResetNav() {
  if (!isAdminUser()) {
    showToast('Only Admin (Rashed) can reset tournament data.', 'error');
    return;
  }
  openDataResetModal();
}

function quickSwitchToAdmin() {
  const guardModal = document.getElementById('adminAuthGuardModal');
  if (guardModal && guardModal.open) guardModal.close();
  showToast('Please sign in with Director credentials.');
  openAuthModal();
}

function quickSwitchToGeneralUser() {
  logoutUser();
}

function toggleRoleDemo() {
  if (isAdminUser()) {
    logoutUser();
  } else {
    openAuthModal();
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
  if (screenId === 'leaderboardScreen') renderLeaderboard();
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

function extractIndividualPlayers(lines) {
  const players = [];
  (lines || []).forEach(line => {
    if (!line) return;
    // Split by slash, ampersand, or comma (for doubles partners)
    const parts = line.split(/[/&,]/).map(s => s.trim()).filter(Boolean);
    parts.forEach(p => {
      if (p.length > 0) players.push(p);
    });
  });
  return players;
}

function findArrayDuplicates(arr) {
  const seen = new Set();
  const duplicates = new Set();
  (arr || []).forEach(item => {
    const key = item.toLowerCase();
    if (seen.has(key)) {
      duplicates.add(item);
    } else {
      seen.add(key);
    }
  });
  return Array.from(duplicates);
}

function checkRosterDuplicates() {
  const linesA = getCleanRoster('rosterAInput');
  const linesB = getCleanRoster('rosterBInput');
  const playersA = extractIndividualPlayers(linesA);
  const playersB = extractIndividualPlayers(linesB);

  const aMap = new Map();
  playersA.forEach(p => aMap.set(p.toLowerCase(), p));

  const crossDuplicates = [];
  playersB.forEach(p => {
    const key = p.toLowerCase();
    if (aMap.has(key)) {
      const orig = aMap.get(key);
      if (!crossDuplicates.includes(orig)) {
        crossDuplicates.push(orig);
      }
    }
  });

  const internalA = findArrayDuplicates(playersA);
  const internalB = findArrayDuplicates(playersB);

  return {
    crossDuplicates,
    internalA,
    internalB,
    hasDuplicates: crossDuplicates.length > 0 || internalA.length > 0 || internalB.length > 0
  };
}

function updatePlayerCounts() {
  const a = getCleanRoster('rosterAInput');
  const b = getCleanRoster('rosterBInput');
  const countAEl = document.getElementById('countA');
  const countBEl = document.getElementById('countB');
  if (countAEl) countAEl.textContent = a.length;
  if (countBEl) countBEl.textContent = b.length;

  const dup = checkRosterDuplicates();
  const warningBox = document.getElementById('rosterDuplicateWarning');
  const warningText = document.getElementById('rosterDuplicateWarningText');
  const inputA = document.getElementById('rosterAInput');
  const inputB = document.getElementById('rosterBInput');
  const startBtn = document.getElementById('startTournamentBtn');

  if (dup.crossDuplicates.length > 0) {
    if (warningBox && warningText) {
      warningBox.style.display = 'flex';
      const names = dup.crossDuplicates.map(n => `"${n}"`).join(', ');
      warningText.textContent = `The same player cannot be added to both sides! Duplicate player(s) found in Pool A and Pool B: ${names}. Please remove duplicate player(s) to proceed.`;
    }
    if (inputA) inputA.style.borderColor = '#ef4444';
    if (inputB) inputB.style.borderColor = '#ef4444';
    if (startBtn) {
      startBtn.disabled = true;
      startBtn.style.opacity = '0.5';
      startBtn.style.cursor = 'not-allowed';
      startBtn.title = 'Remove duplicate players to start tournament';
    }
  } else if (dup.internalA.length > 0 || dup.internalB.length > 0) {
    if (warningBox && warningText) {
      warningBox.style.display = 'flex';
      const listA = dup.internalA.length ? `Pool A: ${dup.internalA.map(n => `"${n}"`).join(', ')}` : '';
      const listB = dup.internalB.length ? `Pool B: ${dup.internalB.map(n => `"${n}"`).join(', ')}` : '';
      const combined = [listA, listB].filter(Boolean).join(' | ');
      warningText.textContent = `Duplicate player detected within the same pool: ${combined}. Each athlete can only be entered once.`;
    }
    if (inputA) inputA.style.borderColor = dup.internalA.length ? '#ef4444' : '';
    if (inputB) inputB.style.borderColor = dup.internalB.length ? '#ef4444' : '';
    if (startBtn) {
      startBtn.disabled = true;
      startBtn.style.opacity = '0.5';
      startBtn.style.cursor = 'not-allowed';
      startBtn.title = 'Remove duplicate players to start tournament';
    }
  } else {
    if (warningBox) warningBox.style.display = 'none';
    if (inputA) inputA.style.borderColor = '';
    if (inputB) inputB.style.borderColor = '';
    if (startBtn) {
      startBtn.disabled = false;
      startBtn.style.opacity = '1';
      startBtn.style.cursor = 'pointer';
      startBtn.title = '';
    }
  }
}

function getCleanRoster(textareaId) {
  const el = document.getElementById(textareaId);
  if (!el) return [];
  const txt = el.value || '';
  return txt.split('\n').map(s => s.trim()).filter(s => s.length > 0);
}

function clearRosters() {
  const rA = document.getElementById('rosterAInput');
  const rB = document.getElementById('rosterBInput');
  if (rA) rA.value = '';
  if (rB) rB.value = '';
  updatePlayerCounts();
  showToast('Rosters cleared.');
}

function loadDemoData() {
  // Load registered athletes into rosters if any exist
  const users = (typeof getUsersDB === 'function') ? getUsersDB() : [];
  const athletes = users.filter(u => u.name && u.name.toLowerCase() !== 'admin');
  if (athletes.length >= 2) {
    const half = Math.ceil(athletes.length / 2);
    const rA = document.getElementById('rosterAInput');
    const rB = document.getElementById('rosterBInput');
    if (rA) rA.value = athletes.slice(0, half).map(p => p.name).join('\n');
    if (rB) rB.value = athletes.slice(half).map(p => p.name).join('\n');
    updatePlayerCounts();
    showToast(`Loaded ${athletes.length} registered athletes into rosters.`);
  } else {
    const rA = document.getElementById('rosterAInput');
    const rB = document.getElementById('rosterBInput');
    if (rA) rA.value = '';
    if (rB) rB.value = '';
    updatePlayerCounts();
    showToast('No pre-seeded dummy players. Enter player names above or pick from registry.', 'info');
  }
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
  const dup = checkRosterDuplicates();
  if (dup.crossDuplicates.length > 0) {
    const names = dup.crossDuplicates.map(n => `"${n}"`).join(', ');
    showToast(`Cannot start tournament: Player ${names} cannot be added to both Pool A and Pool B!`, 'error');
    updatePlayerCounts();
    return;
  }
  if (dup.internalA.length > 0 || dup.internalB.length > 0) {
    const name = dup.internalA[0] || dup.internalB[0];
    showToast(`Cannot start tournament: Duplicate player "${name}" detected in the same pool!`, 'error');
    updatePlayerCounts();
    return;
  }

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
  const feeInput = document.getElementById('tournamentFeeInput');
  state.entryFee = feeInput ? (parseInt(feeInput.value) || 0) : 50;
  const nillToggle = document.getElementById('nillSystemToggle');
  state.nillSystemEnabled = nillToggle ? nillToggle.checked : true;
  state.nillThreshold = parseInt(document.getElementById('nillThresholdInput')?.value) || 10;
  state.nillPenalty = parseInt(document.getElementById('nillPenaltyInput')?.value) || 10;

  // Deduct tournament entry points from registered player wallets
  if (state.entryFee > 0) {
    try {
      const wallets = getWalletsDB();
      const allEntries = [...a, ...b];
      allEntries.forEach(entry => {
        const ind = entry.split('/').map(s => s.trim()).filter(Boolean);
        ind.forEach(name => {
          if (wallets[name] !== undefined && wallets[name] >= state.entryFee) {
            wallets[name] -= state.entryFee;
            recordTransaction(name, 'tournament_entry', state.entryFee, wallets[name], `Tournament entry buy-in (${state.entryFee} PTS)`);
          }
        });
      });
      saveWalletsDB(wallets);
      updateBettingUI();
    } catch (e) {}
  }

  saveState();
  showScreen('draftScreen');
  setupDraftDrums();
}

function joinTournamentWithPoints() {
  if (!requireAuthUser('join the tournament with points')) return;
  const username = currentUser.name;
  const fee = typeof state.entryFee === 'number' ? state.entryFee : (parseInt(state.entryFee) || 50);

  const inA = (state.poolA || []).some(p => p.toLowerCase().includes(username.toLowerCase()));
  const inB = (state.poolB || []).some(p => p.toLowerCase().includes(username.toLowerCase()));
  const rosterA = getCleanRoster('rosterAInput');
  const rosterB = getCleanRoster('rosterBInput');
  const inRosterA = rosterA.some(p => p.toLowerCase().includes(username.toLowerCase()));
  const inRosterB = rosterB.some(p => p.toLowerCase().includes(username.toLowerCase()));

  if (inA || inB || inRosterA || inRosterB) {
    showToast('You are already registered in the tournament roster!', 'info');
    return;
  }

  if (fee > 0) {
    const curBalance = getUserCoins(username);
    if (curBalance < fee) {
      showToast(`⚠️ Insufficient points to join! You have ${curBalance} PTS, but need ${fee} PTS.`, 'warning');
      return;
    }
    setUserCoins(curBalance - fee, username);
    recordTransaction(username, 'tournament_entry', fee, curBalance - fee, `Tournament entry buy-in (${fee} PTS)`);
  }

  const countA = (state.poolA && state.poolA.length > 0) ? state.poolA.length : rosterA.length;
  const countB = (state.poolB && state.poolB.length > 0) ? state.poolB.length : rosterB.length;
  const targetPool = countA <= countB ? 'A' : 'B';

  const inputId = targetPool === 'A' ? 'rosterAInput' : 'rosterBInput';
  const inputEl = document.getElementById(inputId);
  if (inputEl) {
    const currentVal = inputEl.value.trim();
    inputEl.value = currentVal ? currentVal + '\n' + username : username;
    updatePlayerCounts();
  }

  if (state.matches.length > 0) {
    if (targetPool === 'A') {
      if (!state.poolA) state.poolA = [];
      state.poolA.push(username);
    } else {
      if (!state.poolB) state.poolB = [];
      state.poolB.push(username);
    }
  }

  saveState();
  showToast(`🎉 Welcome to the Tournament, ${username}! Enrolled in Pool ${targetPool}${fee > 0 ? ' (' + fee + ' PTS buy-in deducted)' : ''}.`, 'success');
  renderPlayerHub();
  updateBettingUI();
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

  // Find tied win groups to apply BWF 16.2.4 (2-way H2H) vs 16.2.5 (3-way game/point diff)
  const winCounts = {};
  poolPlayers.forEach(p => {
    const w = stats[p] ? stats[p].W : 0;
    winCounts[w] = (winCounts[w] || 0) + 1;
  });

  return poolPlayers.map(p => stats[p]).sort((x, y) => {
    if (y.W !== x.W) return y.W - x.W;
    
    // If exactly two athletes are tied with same wins, BWF H2H decides:
    if (winCounts[x.W] === 2 && x.h2h && x.h2h[y.name]) {
      return -x.h2h[y.name];
    }

    // If 3 or more tied (or H2H unplayed), decide by net game/set difference:
    const gDiffX = x.gamesWon - x.gamesLost;
    const gDiffY = y.gamesWon - y.gamesLost;
    if (gDiffY !== gDiffX) return gDiffY - gDiffX;

    // Then decide by net point difference:
    const ptDiffX = x.ptsWon - x.ptsLost;
    const ptDiffY = y.ptsWon - y.ptsLost;
    if (ptDiffY !== ptDiffX) return ptDiffY - ptDiffX;

    // Then by point ratio:
    const ratioX = x.ptsWon / Math.max(1, x.ptsLost);
    const ratioY = y.ptsWon / Math.max(1, y.ptsLost);
    if (Math.abs(ratioY - ratioX) > 0.001) return ratioY - ratioX;

    return 0;
  });
}

function renderGroups() {
  updateTournamentProgressUI();
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
      <tr style="${idx < 2 ? 'border-left: 3px solid var(--clr-green);' : 'border-left: 3px solid transparent;'}">
        <td style="font-weight:800;color:${idx === 0 ? 'var(--clr-gold)' : (idx === 1 ? 'var(--clr-green)' : 'var(--clr-text-muted)')};padding:10px 8px;font-variant-numeric:tabular-nums;text-align:center;">${idx + 1}</td>
        <td style="padding:10px 10px;">
          <div style="font-weight:700;color:var(--clr-text);">${escapeHtml(s.name)}</div>
          ${idx < 2 ? '<div style="font-size:0.65rem;font-weight:800;color:var(--clr-green);text-transform:uppercase;letter-spacing:0.04em;">● Top 2 Qualifier</div>' : ''}
        </td>
        <td style="color:var(--clr-green);font-weight:700;text-align:center;font-variant-numeric:tabular-nums;padding:10px 8px;">${s.W}</td>
        <td style="color:var(--clr-red);text-align:center;font-variant-numeric:tabular-nums;padding:10px 8px;">${s.L}</td>
        <td style="text-align:center;font-variant-numeric:tabular-nums;padding:10px 8px;color:var(--clr-text-muted);">${(s.ptsWon - s.ptsLost) > 0 ? '+' : ''}${s.ptsWon - s.ptsLost}</td>
        <td style="font-weight:800;color:var(--clr-gold);text-align:center;font-variant-numeric:tabular-nums;padding:10px 8px;">${s.W * 2}</td>
      </tr>
    `).join('');
  };

  renderTable('poolATableBody', standingsA);
  renderTable('poolBTableBody', standingsB);
  renderGroupMatches();
}


function getPlayerAvatarHtml(playerName, size = 34, isWinner = false) {
  const users = (typeof getUsersDB === 'function') ? getUsersDB() : [];
  if (!playerName) playerName = '?';

  // Handle Doubles pairs formatted as "Player 1 / Player 2"
  if (playerName.includes('/')) {
    const parts = playerName.split('/').map(p => p.trim()).filter(Boolean);
    if (parts.length >= 2) {
      const subSize = Math.max(24, Math.round(size * 0.82));
      const av1 = getSinglePlayerAvatarHtml(parts[0], subSize, isWinner, users);
      const av2 = getSinglePlayerAvatarHtml(parts[1], subSize, isWinner, users);
      const overlap = Math.round(subSize * 0.38);
      const totalWidth = (subSize * 2) - overlap;
      return `<div style="display:inline-flex;align-items:center;position:relative;width:${totalWidth}px;height:${subSize}px;flex-shrink:0;" title="${escapeHtml(playerName)}">
        <div style="position:relative;z-index:1;display:flex;">${av1}</div>
        <div style="position:relative;z-index:2;margin-left:-${overlap}px;display:flex;border-radius:50%;box-shadow:0 0 0 2px var(--clr-surface-card);">${av2}</div>
      </div>`;
    }
  }

  return getSinglePlayerAvatarHtml(playerName, size, isWinner, users);
}

function getSinglePlayerAvatarHtml(name, size, isWinner, users) {
  const user = users.find(u => (u.name || '').toLowerCase() === (name || '').toLowerCase());
  const initial = (name || '?').trim().charAt(0).toUpperCase();
  if (user && user.photoUrl) {
    return `<img src="${user.photoUrl}" style="width:${size}px;height:${size}px;border-radius:50%;object-fit:cover;border:1.5px solid ${isWinner ? 'var(--clr-green)' : 'var(--clr-border)'};flex-shrink:0;" alt="${escapeHtml(name)}">`;
  }
  const bg = isWinner ? 'rgba(16,185,129,0.18)' : 'rgba(255,255,255,0.08)';
  const color = isWinner ? 'var(--clr-green)' : 'var(--clr-text)';
  const border = isWinner ? 'rgba(16,185,129,0.45)' : 'var(--clr-border)';
  return `<div style="width:${size}px;height:${size}px;border-radius:50%;background:${bg};color:${color};display:flex;align-items:center;justify-content:center;font-weight:800;font-size:${Math.round(size * 0.42)}px;border:1px solid ${border};flex-shrink:0;">${escapeHtml(initial)}</div>`;
}

function formatCompetitorNameHtml(name, isWinner = false) {
  if (!name) return '—';
  const crown = isWinner ? '<span title="Match Winner" style="color:#f59e0b;font-size:0.85rem;margin-left:4px;flex-shrink:0;">👑</span>' : '';
  if (name.includes('/')) {
    const parts = name.split('/').map(p => p.trim());
    return `<div style="display:flex;align-items:center;gap:4px;min-width:0;max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">
      <span style="font-weight:700;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">${escapeHtml(parts[0])}</span>
      <span style="color:var(--clr-text-muted);font-size:0.75rem;font-weight:400;margin:0 1px;flex-shrink:0;">&amp;</span>
      <span style="font-weight:700;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">${escapeHtml(parts[1])}</span>
      ${crown}
    </div>`;
  }
  return `<div style="display:flex;align-items:center;gap:4px;min-width:0;max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">
    <span style="font-weight:700;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">${escapeHtml(name)}</span>
    ${crown}
  </div>`;
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
    const isAdmin = (typeof isAdminUser === 'function') ? isAdminUser() : false;
    container.innerHTML = `
      <div class="card" style="grid-column:1/-1;text-align:center;padding:36px 20px;border:1px solid var(--clr-border);border-radius:var(--radius-md);">
        <div style="width:48px;height:48px;border-radius:50%;background:rgba(16,185,129,0.1);color:var(--clr-green);display:inline-flex;align-items:center;justify-content:center;margin-bottom:12px;border:1px solid rgba(16,185,129,0.25);">
          <svg class="icon icon-md" viewBox="0 0 24 24"><path d="M12 2l3 7h-6l3-7zM7 9l-4 8 7 5 3-4-6-9zM17 9l4 8-7 5-3-4 6-9z"/></svg>
        </div>
        <div style="font-size:1.05rem;font-weight:700;margin-bottom:6px;color:var(--clr-text);">No Tournament Matches Found</div>
        <p style="color:var(--clr-text-muted);font-size:0.84rem;margin-bottom:18px;max-width:420px;margin-left:auto;margin-right:auto;line-height:1.45;">
          ${isAdmin ? 'No fixtures have been generated yet. Configure your player roster in Tournament Setup to schedule matches.' : 'Round-robin fixtures will appear here once scheduled by the Tournament Director.'}
        </p>
        ${isAdmin ? `
        <div style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap;">
          <button class="btn btn-primary btn-sm" onclick="handleSetupNav()" style="display:inline-flex;align-items:center;gap:6px;">
            <span>⚙ Configure Tournament Setup</span>
          </button>
        </div>` : ''}
      </div>`;
    return;
  }

  const isAdmin = (typeof isAdminUser === 'function') ? isAdminUser() : false;
  container.innerHTML = matches.map(m => {
    const isLive = !m.winner && (m.id === state.currentMatchId);
    const isCompleted = !!m.winner;
    const winnerName = isCompleted ? (m.winner === 'a' ? m.a : m.b) : null;
    const sets = m.sets || [];

    // Calculate sets won accurately
    let setsWonA = 0;
    let setsWonB = 0;
    sets.forEach(s => {
      if (s.winner === 'a') setsWonA++;
      else if (s.winner === 'b') setsWonB++;
    });
    if (isCompleted && setsWonA === 0 && setsWonB === 0) {
      if (m.winner === 'a') setsWonA = 2; else setsWonB = 2;
    }

    const hasStarted = isLive || isCompleted || sets.some(s => s.score[0] > 0 || s.score[1] > 0);

    // Set points display for Competitor A and B
    let setPointsHtmlA = '';
    let setPointsHtmlB = '';
    if (hasStarted && sets.length > 0) {
      setPointsHtmlA = sets.map((s, idx) => {
        const isSetWinner = s.winner === 'a';
        return `<span class="mfc-score-pill ${isSetWinner ? 'is-set-winner' : ''}" title="Set ${idx+1}">${s.score[0]}</span>`;
      }).join('');
      setPointsHtmlB = sets.map((s, idx) => {
        const isSetWinner = s.winner === 'b';
        return `<span class="mfc-score-pill ${isSetWinner ? 'is-set-winner' : ''}" title="Set ${idx+1}">${s.score[1]}</span>`;
      }).join('');
    }

    const avatarA = getPlayerAvatarHtml(m.a, 34, m.winner === 'a');
    const avatarB = getPlayerAvatarHtml(m.b, 34, m.winner === 'b');
    const nameHtmlA = formatCompetitorNameHtml(m.a, m.winner === 'a');
    const nameHtmlB = formatCompetitorNameHtml(m.b, m.winner === 'b');
    const isDoubles = (m.a && m.a.includes('/')) || (m.b && m.b.includes('/')) || (state.category === 'doubles');

    return `
      <div class="match-fixture-card ${isLive ? 'is-live' : (isCompleted ? 'is-completed' : '')}">
        <div class="mfc-header">
          <div class="mfc-court-pill">
            <span class="mfc-badge-court">Court ${m.court}</span>
            <span class="mfc-badge-pool">Pool ${m.pool}</span>
            ${isDoubles ? '<span style="font-size:0.68rem;color:var(--clr-text-muted);background:rgba(255,255,255,0.05);padding:2px 6px;border-radius:4px;">Doubles</span>' : ''}
          </div>
          <div>
            ${isLive ?
              '<span class="status-badge-live" style="display:inline-flex;align-items:center;gap:4px;color:#34d399;font-weight:800;background:rgba(16,185,129,0.12);padding:2px 8px;border-radius:12px;">● LIVE</span>' :
              (isCompleted ?
                '<span class="mfc-badge-completed">✓ COMPLETED</span>' :
                '<span class="mfc-badge-scheduled">⏳ SCHEDULED</span>'
              )}
          </div>
        </div>

        <div class="mfc-body">
          <!-- Competitor A Row -->
          <div class="mfc-competitor-row ${m.winner === 'a' ? 'is-winner' : (isCompleted ? 'is-defeated' : '')}">
            <div class="mfc-player-info">
              ${avatarA}
              <div class="mfc-name-group">
                <div class="mfc-name">${nameHtmlA}</div>
                <div class="mfc-role">${isDoubles ? 'Team A' : 'Player A'}</div>
              </div>
            </div>
            <div class="mfc-score-group">
              ${setPointsHtmlA}
              ${hasStarted ?
                `<span class="mfc-games-won ${m.winner === 'a' ? 'winner-games' : ''}">${setsWonA}</span>` :
                `<span style="color:var(--clr-text-muted);font-size:0.85rem;font-weight:700;padding:0 6px;">—</span>`
              }
            </div>
          </div>

          <!-- Competitor B Row -->
          <div class="mfc-competitor-row ${m.winner === 'b' ? 'is-winner' : (isCompleted ? 'is-defeated' : '')}">
            <div class="mfc-player-info">
              ${avatarB}
              <div class="mfc-name-group">
                <div class="mfc-name">${nameHtmlB}</div>
                <div class="mfc-role">${isDoubles ? 'Team B' : 'Player B'}</div>
              </div>
            </div>
            <div class="mfc-score-group">
              ${setPointsHtmlB}
              ${hasStarted ?
                `<span class="mfc-games-won ${m.winner === 'b' ? 'winner-games' : ''}">${setsWonB}</span>` :
                `<span style="color:var(--clr-text-muted);font-size:0.85rem;font-weight:700;padding:0 6px;">—</span>`
              }
            </div>
          </div>
        </div>

        <div class="mfc-footer">
          ${isCompleted ? `
            <div class="mfc-winner-banner">
              <span>🏆 <strong>${escapeHtml(winnerName)}</strong> won</span>
            </div>
            <div class="mfc-footer-actions">
              <button class="btn btn-ghost btn-xs" onclick="openScorecardModal('${m.id}')" style="gap:4px;">
                <svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
                <span>Scorecard</span>
              </button>
              ${isAdmin ? `
                <button class="btn btn-ghost btn-xs" onclick="openQuickScoreModal('${m.id}')" title="Edit Score">
                  <svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M11 4H4a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
                </button>
              ` : ''}
            </div>
          ` : `
            <button class="btn btn-primary btn-sm mfc-action-main" onclick="startUmpireMatch('${m.id}')">
              <svg class="icon icon-xs" viewBox="0 0 24 24"><polygon points="12 2 15 8 22 9 17 14 18 21 12 17 6 21 7 14 2 9 9 8 12 2"/></svg>
              <span>${isLive ? 'Resume Match' : 'Score / Referee'}</span>
            </button>
            <button class="btn btn-ghost btn-sm mfc-action-predict" onclick="openBettingModal('${m.id}')" title="Predict match winner with coins">
              <svg class="gold-coin-icon" viewBox="0 0 24 24" width="14" height="14"><circle cx="12" cy="12" r="10" fill="url(#headerGoldCoinGrad)"/><path d="M12 6.5l1.6 3.3 3.6.5-2.6 2.6.6 3.6-3.2-1.7-3.2 1.7.6-3.6-2.6-2.6 3.6-.5z" fill="#78350f"/></svg>
              <span>Predict</span>
            </button>
            ${isAdmin ? `
              <button class="btn btn-ghost btn-sm admin-only-item" style="padding:6px 10px;color:var(--clr-text-muted);" onclick="openQuickScoreModal('${m.id}')" title="Manual Quick Score">
                <svg class="icon icon-xs" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
              </button>
            ` : ''}
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
    const m2 = (i + 1 < lastRound.length) ? state.matches.find(m => m.id === lastRound[i + 1]) : null;
    const win1 = m1 ? (m1.winner === 'a' ? m1.a : m1.b) : 'BYE';

    // Auto advance if odd seed / no opponent (BYE)
    if (!m2) {
      const byeMatch = createMatchObj(win1, 'BYE (Automatic Advance)', 'KO');
      byeMatch.winner = 'a';
      state.matches.push(byeMatch);
      nextRound.push(byeMatch.id);
      continue;
    }

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
  if (!requireAuthUser('referee or score matches')) return;
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

  // 13 Hope Ball · 14 Game Ball · 15 Win Rules
  if (pts === 15) {
    if (scoreA === 14 && scoreB === 14) {
      banner.innerHTML = `<span class="status-badge-live badge-game-ball" style="background:rgba(239,68,68,0.18);color:#f87171;border:1px solid rgba(239,68,68,0.45);font-weight:800;padding:4px 14px;border-radius:20px;">🔥 DUAL GAME BALL (14-14) · NEXT RALLY WINS OR DOWNGRADE</span>`;
    } else if (scoreA === 14) {
      banner.innerHTML = `<span class="status-badge-live badge-game-ball" style="background:rgba(239,68,68,0.16);color:#f87171;border:1px solid rgba(239,68,68,0.4);font-weight:800;padding:4px 14px;border-radius:20px;">🔥 GAME BALL — ${escapeHtml(match.a)} (14 PTS)</span>`;
    } else if (scoreB === 14) {
      banner.innerHTML = `<span class="status-badge-live badge-game-ball" style="background:rgba(239,68,68,0.16);color:#f87171;border:1px solid rgba(239,68,68,0.4);font-weight:800;padding:4px 14px;border-radius:20px;">🔥 GAME BALL — ${escapeHtml(match.b)} (14 PTS)</span>`;
    } else if (scoreA === 13 && scoreB === 13) {
      banner.innerHTML = `<span class="status-badge-live badge-hope-ball" style="background:rgba(245,158,11,0.16);color:#fbbf24;border:1px solid rgba(245,158,11,0.4);font-weight:800;padding:4px 14px;border-radius:20px;">🎾 HOPE BALL (13-13) · BOTH AT HOPE BALL</span>`;
    } else if (scoreA === 13) {
      banner.innerHTML = `<span class="status-badge-live badge-hope-ball" style="background:rgba(245,158,11,0.16);color:#fbbf24;border:1px solid rgba(245,158,11,0.4);font-weight:800;padding:4px 14px;border-radius:20px;">🎾 HOPE BALL — ${escapeHtml(match.a)} (13 PTS)</span>`;
    } else if (scoreB === 13) {
      banner.innerHTML = `<span class="status-badge-live badge-hope-ball" style="background:rgba(245,158,11,0.16);color:#fbbf24;border:1px solid rgba(245,158,11,0.4);font-weight:800;padding:4px 14px;border-radius:20px;">🎾 HOPE BALL — ${escapeHtml(match.b)} (13 PTS)</span>`;
    } else {
      banner.innerHTML = '';
    }
    return;
  }

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

/* ═══════════════════════════════════════════════════
   NILL SYSTEM (SHUTOUT WHITEWASH PENALTY ENGINE)
   - When a team reaches Nill Threshold (e.g. 10 pts) while opponent is at 0:
   - Penalty points are deducted from the losing team and awarded to the scoring team.
   - DOUBLE points are deducted and earned on Open Challenge matches!
═══════════════════════════════════════════════════ */
function updateNillPreview(val) {
  const p = Math.max(1, parseInt(val) || 10);
  const tEl = document.getElementById('nillPreviewTourney');
  const cEl = document.getElementById('nillPreviewChallenge');
  if (tEl) tEl.textContent = `${p} PTS`;
  if (cEl) cEl.textContent = `${p * 2} PTS (DOUBLE)`;
}

function checkAndApplyNill(match, set) {
  if (!match || !set || set.nillTriggered) return false;
  if (state.nillSystemEnabled === false) return false;

  const threshold = state.nillThreshold || 10;
  const scoreA = set.score ? (set.score[0] || 0) : 0;
  const scoreB = set.score ? (set.score[1] || 0) : 0;

  let winnerSide = null;
  let loserSide = null;
  if (scoreA >= threshold && scoreB === 0) {
    winnerSide = 'a';
    loserSide = 'b';
  } else if (scoreB >= threshold && scoreA === 0) {
    winnerSide = 'b';
    loserSide = 'a';
  }

  if (!winnerSide) return false;

  set.nillTriggered = true;
  const isChallenge = match.pool === 'CHALLENGE' || (match.id && match.id.startsWith('ch_')) || (typeof getChallengesDB === 'function' && getChallengesDB().some(c => c.matchId === match.id));
  const basePenalty = state.nillPenalty || 10;
  // Double points deducted and earned on challenge match!
  const penalty = isChallenge ? (basePenalty * 2) : basePenalty;

  const winnerTeam = winnerSide === 'a' ? match.a : match.b;
  const loserTeam = loserSide === 'a' ? match.a : match.b;
  const winnerMembers = winnerTeam.includes('/') ? winnerTeam.split('/').map(s => s.trim()).filter(Boolean) : [winnerTeam.trim()];
  const loserMembers = loserTeam.includes('/') ? loserTeam.split('/').map(s => s.trim()).filter(Boolean) : [loserTeam.trim()];

  // Deduct penalty points from each loser team member
  loserMembers.forEach(mem => {
    const curBal = getUserCoins(mem);
    const newBal = Math.max(0, curBal - penalty);
    setUserCoins(newBal, mem);
    recordTransaction(mem, 'nill_penalty', penalty, newBal, `⚡ Nill whitewash penalty (-${penalty} PTS) at ${Math.max(scoreA, scoreB)}–0 shutout vs ${winnerTeam}`);
  });

  // Award bonus points to each winner team member
  winnerMembers.forEach(mem => {
    const curBal = getUserCoins(mem);
    const newBal = curBal + penalty;
    setUserCoins(newBal, mem);
    recordTransaction(mem, 'nill_bonus', penalty, newBal, `⚡ Nill shutout bonus (+${penalty} PTS) for ${Math.max(scoreA, scoreB)}–0 shutout vs ${loserTeam}`);
  });

  updateBettingUI();

  // Notification and announcements
  showToast(`⚡ NILL DECLARED! ${winnerTeam} shutout ${loserTeam} ${Math.max(scoreA, scoreB)}–0! ${penalty} PTS deducted from ${loserTeam} & awarded to ${winnerTeam}${isChallenge ? ' (🔥 DOUBLE Points on Challenge Match!)' : ''}.`, 'warning');
  if (typeof speakScoreAnnouncement === 'function') {
    speakScoreAnnouncement(`Nill declared! ${winnerTeam} leads ${Math.max(scoreA, scoreB)} to zero. Whitewash penalty applied.`);
  }
  if (typeof playSound === 'function') playSound('win');
  if ('vibrate' in navigator) navigator.vibrate([120, 60, 120, 60, 240]);

  // Scoreboard banner
  showNillScoreboardBanner(winnerTeam, loserTeam, Math.max(scoreA, scoreB), penalty, isChallenge);
  return true;
}

function showNillScoreboardBanner(winnerTeam, loserTeam, score, penalty, isChallenge) {
  let banner = document.getElementById('liveNillBanner');
  if (!banner) {
    const container = document.getElementById('liveScoreboardContainer') || document.querySelector('.umpire-court');
    if (container) {
      banner = document.createElement('div');
      banner.id = 'liveNillBanner';
      banner.className = 'nill-live-banner';
      container.prepend(banner);
    }
  }
  if (banner) {
    banner.style.display = 'block';
    banner.innerHTML = `
      <div style="background:linear-gradient(135deg, rgba(239,68,68,0.25), rgba(245,158,11,0.25));border:2px solid #ef4444;border-radius:8px;padding:10px 16px;margin:8px auto 14px;display:flex;align-items:center;justify-content:space-between;gap:12px;width:95%;max-width:600px;box-shadow:0 4px 16px rgba(239,68,68,0.3);">
        <div style="display:flex;align-items:center;gap:10px;">
          <span style="font-size:1.6rem;">⚡</span>
          <div>
            <div style="font-family:var(--font-display);font-size:1.05rem;font-weight:900;color:#f87171;letter-spacing:0.04em;">NILL DECLARED (WHITEWASH)!</div>
            <div style="font-size:0.8rem;color:var(--clr-text);">${escapeHtml(winnerTeam)} earned ${score}–0 shutout over ${escapeHtml(loserTeam)}!</div>
          </div>
        </div>
        <div style="text-align:right;">
          <span style="font-family:monospace;font-size:1.1rem;font-weight:900;color:var(--clr-gold);">${isChallenge ? '🔥 DOUBLE: ' : ''}${penalty} PTS</span>
          <div style="font-size:0.7rem;color:var(--clr-text-muted);">Deducted & Awarded</div>
        </div>
      </div>
    `;
    setTimeout(() => {
      if (banner) banner.style.display = 'none';
    }, 9000);
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
    courtFlipped: state.courtFlipped,
    historyLen: match.history ? match.history.length : 0,
    eventLogLen: match.eventLog ? match.eventLog.length : 0
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
  const oppIdx = side === 'a' ? 1 : 0;
  const scorerName = side === 'a' ? match.a : match.b;
  const oppName = side === 'a' ? match.b : match.a;

  // BWF Deciding 3rd Set Court Switch Threshold (8 pts for 15-pt match, 11 pts for 21-pt match)
  if (state.currentSetIdx === 2 && !state.endsSwitchedInDecidingSet) {
    const threshold = state.ptsToWin === 15 ? 8 : 11;
    if (set.score[0] >= threshold || set.score[1] >= threshold) {
      state.endsSwitchedInDecidingSet = true;
      toggleCourtFlip();
      speakScoreAnnouncement('Change ends. Interval.');
      showToast('🔄 Deciding Set Threshold reached! Change Ends.');
    }
  }

  // Record Rally Shot Count
  if (match.currentRallyShots) {
    if (!match.rallyHistory) match.rallyHistory = [];
    match.rallyHistory.push(match.currentRallyShots);
    match.currentRallyShots = 0;
    const rVal = document.getElementById('rallyShotsVal');
    if (rVal) rVal.textContent = '0';
  }

  // 13 Hope Ball · 14 Game Ball · 15 Win Rule
  // If opponent has 14 points (Game Ball) and current player scores a point:
  // Opponent is downgraded from Game Ball (14) back to Hope Ball (13)!
  let downgraded = false;
  const isHopeGameSystem = (state.ptsToWin === 15);
  if (isHopeGameSystem && set.score[oppIdx] === 14) {
    set.score[oppIdx] = 13;
    downgraded = true;
  }

  set.score[idx]++;
  state.servingSide = side;

  if (!match.history) match.history = [];
  match.history.push({
    set: state.currentSetIdx + 1,
    score: [set.score[0], set.score[1]],
    scorer: scorerName,
    downgraded: downgraded ? oppName : null,
    time: new Date().toLocaleTimeString()
  });

  const el = document.getElementById(side === 'a' ? 'scoreDigitA' : 'scoreDigitB');
  if (el) {
    el.classList.add('pop');
    setTimeout(() => el.classList.remove('pop'), 160);
  }

  if (downgraded) {
    const oppEl = document.getElementById(side === 'a' ? 'scoreDigitB' : 'scoreDigitA');
    if (oppEl) {
      oppEl.classList.add('pop');
      setTimeout(() => oppEl.classList.remove('pop'), 260);
    }
    showToast(`⚠️ DOWNGRADE! ${oppName} lost Game Ball and dropped back to Hope Ball (13)!`, 'warning');
    if ('vibrate' in navigator) navigator.vibrate([60, 40, 60]);
  }

  const isDecidingSet = (state.bestOf === 3 && state.currentSetIdx === 2) || (state.bestOf === 5 && state.currentSetIdx === 4);
  const midpoint = Math.ceil(state.ptsToWin / 2);
  if (isDecidingSet && !state.endsSwitchedInDecidingSet && (set.score[0] >= midpoint || set.score[1] >= midpoint)) {
    state.endsSwitchedInDecidingSet = true;
    triggerEndsSwitch();
  }

  const intervalPt = isHopeGameSystem ? 8 : 11;
  if ((set.score[0] === intervalPt || set.score[1] === intervalPt) && Math.max(set.score[0], set.score[1]) === intervalPt) {
    triggerIntervalTimer(60);
  }

  evaluateSetStatus(match, set);
  checkAndApplyNill(match, set);
  updateLiveScoreboardUI();
  saveState();
  broadcastStateChange();

  if (downgraded) {
    speakScoreAnnouncement(`Point to ${scorerName}. Downgrade! ${oppName} back to Hope Ball, 13.`);
  } else {
    speakScoreAnnouncement();
  }
  const annEl = document.getElementById('ariaLiveAnnouncer');
  if (annEl) {
    const curS = match.sets[state.currentSetIdx];
    annEl.textContent = `Score: ${match.a} ${curS.score[0]}, ${match.b} ${curS.score[1]}. Serving: ${state.servingSide === 'a' ? match.a : match.b}`;
  }
}

function undoPoint() {
  if (!state.undoStack || !state.undoStack.length) {
    showToast('Nothing to undo.', 'info');
    return;
  }
  const match = state.matches.find(m => m.id === state.currentMatchId);
  if (!match) {
    showToast('No active match loaded to undo.', 'warning');
    return;
  }
  const prev = state.undoStack.pop();
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
  if (match.history && prev.historyLen !== undefined) {
    match.history = match.history.slice(0, prev.historyLen);
  }
  if (match.eventLog && prev.eventLogLen !== undefined) {
    match.eventLog = match.eventLog.slice(0, prev.eventLogLen);
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

  let setWinner = null;
  if (pts === 15) {
    // 13 Hope Ball · 14 Game Ball · 15 Win (First to 15 wins!)
    if (scoreA >= 15) setWinner = 'a';
    else if (scoreB >= 15) setWinner = 'b';
  } else {
    const maxCap = (pts === 21) ? 30 : (pts === 11 ? 15 : pts + 5);
    if (scoreA >= pts && scoreA - scoreB >= 2) setWinner = 'a';
    else if (scoreB >= pts && scoreB - scoreA >= 2) setWinner = 'b';
    else if (scoreA === maxCap) setWinner = 'a';
    else if (scoreB === maxCap) setWinner = 'b';
  }

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

  try {
    const chList = getChallengesDB();
    const target = chList.find(c => c.matchId === match.id ||
      ((c.creator.toLowerCase() === match.a.toLowerCase() && c.opponent && c.opponent.toLowerCase() === match.b.toLowerCase()) ||
       (c.creator.toLowerCase() === match.b.toLowerCase() && c.opponent && c.opponent.toLowerCase() === match.a.toLowerCase()))
    );
    if (target) {
      target.status = 'completed';
      target.winner = winnerName;
      target.matchId = match.id;
      saveChallengesDB(chList);
      renderChallengesBoard();
    }
  } catch (e) {}

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
  state.currentMatchId = null; // Clear active live match so completed matches don't stay marked ● LIVE
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

  // Award match victory bonus & point coins to players
  try {
    const wallets = getWalletsDB();
    if (wallets[winner] === undefined) wallets[winner] = 100;
    if (wallets[loser] === undefined) wallets[loser] = 100;
    wallets[winner] += 50; // +50 bonus coins for victory
    let ptsA = 0, ptsB = 0;
    (match.sets || []).forEach(s => {
      ptsA += (s.score[0] || 0);
      ptsB += (s.score[1] || 0);
    });
    wallets[match.a] = (wallets[match.a] || 100) + ptsA;
    wallets[match.b] = (wallets[match.b] || 100) + ptsB;
    saveWalletsDB(wallets);
    updateBettingUI();
  } catch (e) {}

  // Award open challenge buy-in: winner team members receive double points (chal.buyIn * 2)
  try {
    const list = getChallengesDB();
    const chal = list.find(c => c.matchId === match.id ||
      (c.creator && c.opponent && ((c.creator.toLowerCase() === match.a.toLowerCase() && c.opponent.toLowerCase() === match.b.toLowerCase()) || (c.creator.toLowerCase() === match.b.toLowerCase() && c.opponent.toLowerCase() === match.a.toLowerCase())))
    );
    if (chal && (chal.buyIn || 0) > 0 && !chal.payoutProcessed) {
      chal.payoutProcessed = true;
      chal.status = 'completed';
      chal.winner = winner;
      const winPoints = chal.buyIn * 2; // e.g. 5 PTS -> 10 PTS!

      // Award double points (winPoints) to all winner team members
      const winnerMembers = winner.includes('/') ? winner.split('/').map(s => s.trim()).filter(Boolean) : [winner.trim()];
      const wallets = getWalletsDB();
      winnerMembers.forEach(mem => {
        wallets[mem] = (wallets[mem] || 0) + winPoints;
        recordTransaction(mem, 'challenge_win', winPoints, wallets[mem], `🏆 Won challenge prize of ${winPoints} PTS vs ${loser}`);
      });
      saveWalletsDB(wallets);
      saveChallengesDB(list);
      showToast(`🏆 ${winner} won the challenge! Winner team members received ${winPoints} PTS each.`, 'success');
      updateBettingUI();
    }
  } catch (e) {}

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

let currentLeaderboardFilter = 'all';

function setLeaderboardFilter(filter) {
  currentLeaderboardFilter = filter;
  ['all', 'poolA', 'poolB', 'elo', 'winrate', 'predictors'].forEach(f => {
    const btn = document.getElementById(`lbFilter${f.charAt(0).toUpperCase() + f.slice(1)}`);
    if (btn) btn.classList.toggle('active', f === filter);
  });
  renderLeaderboard();
}

function renderLeaderboard() {
  const db = getLeaderboardDB();
  const tbody = document.getElementById('globalLeaderboardTableBody');
  const podiumContainer = document.getElementById('leaderboardPodiumContainer');
  if (!tbody) return;

  // Gather all players
  let players = Object.values(db);

  // If DB is sparse, ensure pool A & pool B players exist
  const existingNames = new Set(players.map(p => p.name));
  (state.poolA || []).forEach(name => {
    if (name && name !== 'BYE' && !existingNames.has(name)) {
      players.push({ name, elo: 1200, gold: 0, silver: 0, bronze: 0, won: 0, lost: 0, totalPts: 0, ptsDiff: 0, pool: 'A' });
      existingNames.add(name);
    }
  });
  (state.poolB || []).forEach(name => {
    if (name && name !== 'BYE' && !existingNames.has(name)) {
      players.push({ name, elo: 1200, gold: 0, silver: 0, bronze: 0, won: 0, lost: 0, totalPts: 0, ptsDiff: 0, pool: 'B' });
      existingNames.add(name);
    }
  });

  // Assign pool tags
  players.forEach(p => {
    if (!p.pool) {
      if ((state.poolA || []).includes(p.name)) p.pool = 'A';
      else if ((state.poolB || []).includes(p.name)) p.pool = 'B';
    }
  });

  // Apply Filter
  if (currentLeaderboardFilter === 'poolA') {
    players = players.filter(p => p.pool === 'A');
  } else if (currentLeaderboardFilter === 'poolB') {
    players = players.filter(p => p.pool === 'B');
  }

  // Sorting
  if (currentLeaderboardFilter === 'elo') {
    players.sort((x, y) => (y.elo || 1200) - (x.elo || 1200));
  } else if (currentLeaderboardFilter === 'winrate') {
    players.sort((x, y) => {
      const tx = (x.won || 0) + (x.lost || 0);
      const ty = (y.won || 0) + (y.lost || 0);
      const rx = tx > 0 ? (x.won / tx) : 0;
      const ry = ty > 0 ? (y.won / ty) : 0;
      return ry - rx || (y.won || 0) - (x.won || 0);
    });
  } else {
    // Default 'all' or by championships / wins
    players.sort((x, y) => {
      if ((y.gold || 0) !== (x.gold || 0)) return (y.gold || 0) - (x.gold || 0);
      if ((y.won || 0) !== (x.won || 0)) return (y.won || 0) - (x.won || 0);
      if ((y.ptsDiff || 0) !== (x.ptsDiff || 0)) return (y.ptsDiff || 0) - (x.ptsDiff || 0);
      return (y.elo || 1200) - (x.elo || 1200);
    });
  }

  // Render Podium for Top 3
  if (podiumContainer) {
    if (players.length >= 3) {
      const first = players[0];
      const second = players[1];
      const third = players[2];

      const getPodiumRate = p => {
        const t = (p.won || 0) + (p.lost || 0);
        return t > 0 ? Math.round((p.won / t) * 100) : 0;
      };

      podiumContainer.innerHTML = `
        <!-- 2nd Place: Silver -->
        <div class="podium-card podium-silver">
          <div style="font-size:0.75rem;font-weight:800;color:var(--clr-silver);text-transform:uppercase;margin-bottom:8px;">🥈 2nd Place</div>
          <div class="podium-avatar">${(second.name || 'P').charAt(0).toUpperCase()}</div>
          <div style="font-size:1.1rem;font-weight:800;color:var(--clr-text);">${second.name}</div>
          <div style="font-size:0.78rem;color:var(--clr-text-muted);margin:4px 0;">${second.elo || 1200} Elo · ${getPodiumRate(second)}% Win</div>
          <div style="font-size:0.72rem;color:var(--clr-silver);font-weight:700;">${second.won || 0}W - ${second.lost || 0}L (${second.ptsDiff >= 0 ? '+' : ''}${second.ptsDiff || 0})</div>
        </div>

        <!-- 1st Place: Gold -->
        <div class="podium-card podium-gold">
          <div style="font-size:0.8rem;font-weight:900;color:var(--clr-gold);text-transform:uppercase;margin-bottom:6px;">👑 1st Champion</div>
          <div class="podium-avatar">${(first.name || 'P').charAt(0).toUpperCase()}</div>
          <div style="font-size:1.25rem;font-weight:900;color:var(--clr-text);">${first.name}</div>
          <div style="font-size:0.82rem;color:var(--clr-gold);font-weight:700;margin:4px 0;">${first.elo || 1200} Elo · ${getPodiumRate(first)}% Win</div>
          <div style="font-size:0.75rem;color:var(--clr-text-muted);font-weight:600;">${first.won || 0}W - ${first.lost || 0}L (${first.ptsDiff >= 0 ? '+' : ''}${first.ptsDiff || 0} Diff)</div>
        </div>

        <!-- 3rd Place: Bronze -->
        <div class="podium-card podium-bronze">
          <div style="font-size:0.75rem;font-weight:800;color:var(--clr-bronze);text-transform:uppercase;margin-bottom:8px;">🥉 3rd Place</div>
          <div class="podium-avatar">${(third.name || 'P').charAt(0).toUpperCase()}</div>
          <div style="font-size:1.1rem;font-weight:800;color:var(--clr-text);">${third.name}</div>
          <div style="font-size:0.78rem;color:var(--clr-text-muted);margin:4px 0;">${third.elo || 1200} Elo · ${getPodiumRate(third)}% Win</div>
          <div style="font-size:0.72rem;color:var(--clr-bronze);font-weight:700;">${third.won || 0}W - ${third.lost || 0}L (${third.ptsDiff >= 0 ? '+' : ''}${third.ptsDiff || 0})</div>
        </div>
      `;
    } else {
      podiumContainer.innerHTML = '';
    }
  }

  // Update Golden Racket / Iron Net Awards
  const topAttacker = players.slice().sort((a, b) => (b.totalPts || 0) - (a.totalPts || 0))[0];
  const gRacketLead = document.getElementById('goldenRacketLeader');
  const gRacketStats = document.getElementById('goldenRacketStats');
  if (gRacketLead && topAttacker) {
    gRacketLead.textContent = `Leader: ${topAttacker.name}`;
    if (gRacketStats) gRacketStats.textContent = `${topAttacker.totalPts || 0} points scored`;
  }

  const topDefender = players.slice().filter(p => (p.won || 0) + (p.lost || 0) > 0).sort((a, b) => (b.ptsDiff || 0) - (a.ptsDiff || 0))[0];
  const gGloveLead = document.getElementById('goldenGloveLeader');
  const gGloveStats = document.getElementById('goldenGloveStats');
  if (gGloveLead && topDefender) {
    gGloveLead.textContent = `Leader: ${topDefender.name}`;
    if (gGloveStats) gGloveStats.textContent = `+${topDefender.ptsDiff || 0} point differential`;
  }

  if (!players.length) {
    tbody.innerHTML = `<tr><td colspan="12" style="text-align:center;padding:24px;color:var(--clr-text-muted);">No athlete records match the selected filter.</td></tr>`;
    return;
  }

  tbody.innerHTML = players.map((p, idx) => {
    const total = (p.won || 0) + (p.lost || 0);
    const rate = total > 0 ? Math.round((p.won / total) * 100) : 0;
    const opponent = players[idx === 0 ? 1 : 0]?.name || p.name;
    const rankBadge = idx === 0 ? '🥇 1' : (idx === 1 ? '🥈 2' : (idx === 2 ? '🥉 3' : `#${idx + 1}`));
    return `
      <tr>
        <td style="font-weight:900;color:${idx === 0 ? 'var(--clr-gold)' : (idx === 1 ? 'var(--clr-silver)' : (idx === 2 ? 'var(--clr-bronze)' : 'inherit'))};">${rankBadge}</td>
        <td>
          <div style="display:flex;align-items:center;gap:8px;">
            <div style="width:26px;height:26px;border-radius:4px;background:var(--clr-surface-hi);color:var(--clr-text);display:flex;align-items:center;justify-content:center;font-size:0.75rem;font-weight:800;border:1px solid var(--clr-border);">
              ${(p.name || 'P').charAt(0).toUpperCase()}
            </div>
            <div>
              <strong>${p.name}</strong>
              ${p.pool ? `<span style="font-size:0.7rem;color:var(--clr-text-muted);margin-left:4px;">(Pool ${p.pool})</span>` : ''}
            </div>
          </div>
        </td>
        <td><strong style="color:var(--clr-gold);">${p.elo || 1200}</strong></td>
        <td style="color:var(--clr-gold);font-weight:bold;">${p.gold || 0}</td>
        <td style="color:var(--clr-silver);">${p.silver || 0}</td>
        <td style="color:var(--clr-bronze);">${p.bronze || 0}</td>
        <td>${total}</td>
        <td style="color:var(--clr-green);">${p.won || 0}</td>
        <td style="color:var(--clr-red);">${p.lost || 0}</td>
        <td style="font-weight:bold;">${rate}%</td>
        <td style="color:${(p.ptsDiff || 0) >= 0 ? 'var(--clr-green)' : 'var(--clr-red)'};font-weight:700;">${(p.ptsDiff || 0) > 0 ? '+' : ''}${p.ptsDiff || 0}</td>
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
  showToast('Demo tournament disabled. Use Tournament Setup to generate official fixtures.', 'info');
}

function loadSavedState(autoRender = true) {
  try {
    const raw = localStorage.getItem(STORAGE_KEY_STATE);
    if (raw) {
      const parsed = JSON.parse(raw);
      Object.assign(state, parsed);
    }
  } catch (e) {}

  state.poolA = state.poolA || [];
  state.poolB = state.poolB || [];
  state.matches = state.matches || [];
  state.players = state.players || [];

  // Active purge of dummy matches from previous sessions
  const dummyNames = [
    'parag das', 'rifat haque', 'rifat tariq', 'jobayer', 'shewa', 'sazedul',
    'nur', 'ofi', 'sifat', 'sajeeb', 'jakir', 'saiful', 'al emran', 'toufiq', 'abir',
    'parag', 'rifat'
  ];
  const hasDummyMatches = state.matches.some(m => {
    const aLower = (m.a || '').toLowerCase();
    const bLower = (m.b || '').toLowerCase();
    return dummyNames.some(dn => aLower.includes(dn) || bLower.includes(dn));
  });

  if (hasDummyMatches) {
    state.matches = [];
    state.poolA = [];
    state.poolB = [];
    state.players = [];
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

async function resetTournamentState() {
  if (!isAdminUser()) {
    showToast('Only Admin (Rashed) can reset tournament data.', 'error');
    return;
  }
  const confirmed = await appConfirm('Clear current tournament data? Active pending predictions will be refunded.', 'Clear Tournament Data', 'Confirm Reset', true);
  if (!confirmed) return;
  if (true) {
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

  // Pre-seed admin account
  try {
    const users = getUsersDB();
    if (!users.some(u => (u.name || '').toLowerCase() === 'rashed')) {
      const adminHash = await hashPassword('admin123');
      users.unshift({
        id: 1001,
        name: 'Rashed',
        email: 'rashed@badminton.local',
        passHash: adminHash,
        role: 'admin',
        status: 'active',
        feeStatus: 'paid',
        elo: 1650,
        dominantHand: 'Right-Handed',
        club: 'Tournament Director',
        avatar: 'R',
        createdAt: 'Initial'
      });
      saveUsersDB(users);
    }
  } catch (e) {}

  ensureDemoUsersSeeded();
  loadAuthUser();
  loadSavedState();
  renderTournamentSwitcher();
  checkWelcomeBanner();
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
  renderTournamentSwitcher();
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
  const btnRequest = document.getElementById('btnRequestNotification');
  const btnTest = document.getElementById('btnTestNotification');
  const activeBadge = document.getElementById('notifyActiveBadge');
  const dot = document.getElementById('notifyStatusDot');

  if (!('Notification' in window)) {
    if (heading) heading.textContent = 'Notifications Not Supported';
    if (desc) desc.textContent = 'This browser does not support Web Push Notifications.';
    if (btnRequest) btnRequest.style.display = 'none';
    if (btnTest) btnTest.style.display = 'none';
    if (activeBadge) activeBadge.style.display = 'none';
    if (dot) dot.style.display = 'none';
    return;
  }

  const perm = Notification.permission;
  if (perm === 'granted') {
    if (heading) heading.textContent = 'Notifications Active';
    if (desc) desc.textContent = 'Instant alerts for challenges, match scores, and winners.';
    if (activeBadge) activeBadge.style.display = 'inline-flex';
    if (btnRequest) btnRequest.style.display = 'none';
    if (btnTest) btnTest.style.display = 'flex';
    if (dot) {
      dot.style.display = 'block';
      dot.style.background = 'var(--clr-green)';
    }
  } else if (perm === 'denied') {
    if (heading) heading.textContent = 'Notifications Blocked';
    if (desc) desc.textContent = 'Notifications are blocked in your browser settings. Please allow permissions in your site URL bar.';
    if (activeBadge) activeBadge.style.display = 'none';
    if (btnRequest) btnRequest.style.display = 'none';
    if (btnTest) btnTest.style.display = 'none';
    if (dot) {
      dot.style.display = 'block';
      dot.style.background = 'var(--clr-red)';
    }
  } else {
    if (heading) heading.textContent = 'Enable Notifications';
    if (desc) desc.textContent = 'Stay updated with live alerts for challenges, match scores, and winners.';
    if (activeBadge) activeBadge.style.display = 'none';
    if (btnRequest) btnRequest.style.display = 'flex';
    if (btnTest) btnTest.style.display = 'none';
    if (dot) dot.style.display = 'none';
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


// Modal Body Scroll Lock Observer
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('dialog').forEach(d => {
    d.addEventListener('close', () => {
      const anyOpen = Array.from(document.querySelectorAll('dialog')).some(x => x.open);
      if (!anyOpen) document.body.classList.remove('modal-open');
    });
  });
  updateSoundIconUI();
  updateNetworkStatus();
});

if (typeof HTMLDialogElement !== 'undefined') {
  const originalShowModal = HTMLDialogElement.prototype.showModal;
  HTMLDialogElement.prototype.showModal = function() {
    document.body.classList.add('modal-open');
    originalShowModal.call(this);
  };
}


function dismissWelcomeBanner() {
  const el = document.getElementById('groupsWelcomeBanner');
  if (el) el.style.display = 'none';
  try { sessionStorage.setItem('badminton_welcome_dismissed', 'true'); } catch (e) {}
}

function checkWelcomeBanner() {
  try {
    if (sessionStorage.getItem('badminton_welcome_dismissed') === 'true') {
      const el = document.getElementById('groupsWelcomeBanner');
      if (el) el.style.display = 'none';
    }
  } catch (e) {}
}

/* Deep-Link Challenge URL Handler */
function handleUrlHashRouting() {
  const hash = window.location.hash || '';
  if (hash.startsWith('#challenge=') || hash.startsWith('#challenge-')) {
    const chalId = hash.replace(/^#challenge[-=]/, '');
    if (chalId) {
      showScreen('challengesScreen');
      setTimeout(() => {
        const list = getChallengesDB();
        const chal = list.find(c => c.id === chalId);
        if (chal) {
          filterChallenges('all');
          const cards = document.querySelectorAll('.challenge-card');
          cards.forEach(card => {
            if (card.textContent.includes(chal.creator)) {
              card.scrollIntoView({ behavior: 'smooth', block: 'center' });
              card.style.outline = '3px solid var(--clr-gold)';
              card.style.boxShadow = '0 0 24px rgba(245, 158, 11, 0.4)';
              setTimeout(() => {
                card.style.outline = '';
                card.style.boxShadow = '';
              }, 3500);
            }
          });
          showToast(`Found challenge from ${chal.creator}!`, 'info');
        }
      }, 350);
    }
  }
}
window.addEventListener('hashchange', handleUrlHashRouting);
window.addEventListener('DOMContentLoaded', () => {
  setTimeout(handleUrlHashRouting, 500);
});

/* Umpire Keyboard Hotkeys */
window.addEventListener('keydown', (e) => {
  const umpireScreen = document.getElementById('liveUmpireScreen');
  if (!umpireScreen || umpireScreen.style.display === 'none') return;
  const activeEl = document.activeElement;
  if (activeEl && (activeEl.tagName === 'INPUT' || activeEl.tagName === 'TEXTAREA' || activeEl.tagName === 'SELECT')) return;

  if (e.code === 'Space') {
    e.preventDefault();
    if (e.shiftKey || e.altKey) {
      scorePoint(state.servingSide === 'a' ? 'b' : 'a');
    } else {
      scorePoint(state.servingSide);
    }
  } else if (e.code === 'KeyU' || (e.ctrlKey && e.code === 'KeyZ')) {
    e.preventDefault();
    undoPoint();
  } else if (e.code === 'KeyF') {
    e.preventDefault();
    toggleCourtFlip();
  } else if (e.code === 'KeyI') {
    e.preventDefault();
    triggerIntervalTimer(60);
  }
});

/* Visibility Change WakeLock Re-acquisition */
document.addEventListener('visibilitychange', () => {
  if (!document.hidden && state.currentMatchId) {
    if (typeof requestWakeLock === 'function') requestWakeLock();
  }
});


/* ═══════════════════════════════════════════════════════════════
   50+ AUDIT IMPLEMENTATIONS: I18N, BROADCAST, A11Y, STATS & MORE
   ═══════════════════════════════════════════════════════════════ */

/* ── 1. Translation Dictionary & i18n Engine ── */
const APP_TRANSLATIONS = {
  en: {
    navMatches: 'Matches & Courts',
    navChallenges: 'Open Challenges',
    navBracket: 'Playoff Bracket',
    navRanking: 'Standings & Ranks',
    navMore: 'More Tools',
    installApp: 'Install',
    createChalBtn: 'Open Challenge',
    chalScreenTitle: 'School & Club Open Challenge Board',
    chalScreenSub: 'Anyone can open a challenge here! Other students or players can accept and jump straight into the match.',
    openChallengeTitle: 'Open a Badminton Challenge',
    openChallengeDesc: 'Post a challenge on the public board. Any school student or player can accept your challenge and play!',
    challengeCategoryLabel: 'Format',
    challengePointsLabel: 'Points Target',
    challengeNoteLabel: 'Note / Venue',
    postChallengeBtn: 'Post Challenge →',
    cancelBtn: 'Cancel',
    saveScoreBtn: 'Save Score',
    quickScoreTitle: 'Quick Score & Win',
    quickScoreDesc: 'Directly record the final match score or click a player to award an instant win without scoring rally-by-rally.',
    orCustomScore: 'or enter manual final score:',
    winsLabel: 'Wins',
    moreMenuTitle: 'Tournament Navigation & Tools',
    resetAllTitle: 'Reset Tournament & Cache',
    resetAllSub: 'Clear fixtures and restart fresh',
    resetTourneyTitle: 'Reset Tournament Only',
    resetTourneySub: 'Clears matches and pool standings',
    resetDataTitle: 'Reset Storage Cache',
    resetDataDesc: 'Removes local cache data'
  },
  bn: {
    navMatches: 'ম্যাচ ও কোর্ট',
    navChallenges: 'ওপেন চ্যালেঞ্জ',
    navBracket: 'নকআউট ব্র্যাকেট',
    navRanking: 'র‌্যাঙ্কিং ও পয়েন্ট',
    navMore: 'আরও টুলস',
    installApp: 'ইনস্টল',
    createChalBtn: 'নতুন চ্যালেঞ্জ',
    chalScreenTitle: 'স্কুল ও ক্লাব ওপেন চ্যালেঞ্জ বোর্ড',
    chalScreenSub: 'এখানে যে কেউ চ্যালেঞ্জ খুলতে পারেন! অন্য খেলোয়াড়রা গ্রহণ করে সাথে সাথে খেলতে পারবে।',
    openChallengeTitle: 'ব্যাডমিন্টন চ্যালেঞ্জ তৈরি করুন',
    openChallengeDesc: 'পাবলিক বোর্ডে চ্যালেঞ্জ পোস্ট করুন। যেকোনো খেলোয়াড় গ্রহণ করে ম্যাচে নামতে পারবে!',
    challengeCategoryLabel: 'ম্যাচ ফরম্যাট',
    challengePointsLabel: 'টার্গেট পয়েন্ট',
    challengeNoteLabel: 'কোর্ট / নোট',
    postChallengeBtn: 'চ্যালেঞ্জ পোস্ট করুন →',
    cancelBtn: 'বাতিল',
    saveScoreBtn: 'স্কোর সংরক্ষণ করুন',
    quickScoreTitle: 'কুইক স্কোর ও বিজয়ী',
    quickScoreDesc: 'র‌্যালি গণনা না করে সরাসরি ফাইনাল স্কোর নির্ধারণ করুন অথবা এক ক্লিকে বিজয়ী ঘোষণা করুন।',
    orCustomScore: 'অথবা ম্যানুয়াল স্কোর লিখুন:',
    winsLabel: 'জয়ী',
    moreMenuTitle: 'টুর্নামেন্ট মেনু ও টুলস',
    resetAllTitle: 'টুর্নামেন্ট রিসেট করুন',
    resetAllSub: 'সব ম্যাচ মুছে নতুন করে শুরু করুন',
    resetTourneyTitle: 'শুধু টুর্নামেন্ট রিসেট',
    resetTourneySub: 'ম্যাচ ও পয়েন্ট টেবিল খালি করে',
    resetDataTitle: 'ক্যাশ ডেটা রিসেট',
    resetDataDesc: 'ব্রাউজারের লোকাল স্টোরেজ পরিষ্কার করুন'
  },
  es: {
    navMatches: 'Partidos y Pistas',
    navChallenges: 'Retos Abiertos',
    navBracket: 'Cuadro Playoff',
    navRanking: 'Clasificación',
    navMore: 'Más Herramientas',
    installApp: 'Instalar',
    createChalBtn: 'Abrir Reto',
    chalScreenTitle: 'Tablón de Retos Abiertos del Club',
    chalScreenSub: '¡Cualquiera puede publicar un reto aquí! Otros jugadores pueden aceptarlo y jugar al instante.',
    openChallengeTitle: 'Publicar Reto de Bádminton',
    openChallengeDesc: 'Publica un reto en el tablón abierto. ¡Cualquier jugador o estudiante puede aceptarlo!',
    challengeCategoryLabel: 'Modalidad',
    challengePointsLabel: 'Puntos Objetivo',
    challengeNoteLabel: 'Pista / Nota',
    postChallengeBtn: 'Publicar Reto →',
    cancelBtn: 'Cancelar',
    saveScoreBtn: 'Guardar Puntuación',
    quickScoreTitle: 'Puntuación Rápida y Victoria',
    quickScoreDesc: 'Registra el resultado final directamente o declara un ganador inmediato sin puntuar punto a punto.',
    orCustomScore: 'o introduce la puntuación manual:',
    winsLabel: 'Gana',
    moreMenuTitle: 'Navegación y Herramientas',
    resetAllTitle: 'Reiniciar Torneo y Caché',
    resetAllSub: 'Borra partidos y reinicia desde cero',
    resetTourneyTitle: 'Reiniciar Solo Torneo',
    resetTourneySub: 'Limpia partidos y clasificaciones',
    resetDataTitle: 'Reiniciar Almacenamiento',
    resetDataDesc: 'Elimina los datos locales en caché'
  }
};

let currentAppLanguage = 'en';

function setAppLanguage(lang) {
  currentAppLanguage = 'en';
  localStorage.setItem('badminton_app_lang', 'en');
  applyTranslations('en');
}

function applyTranslations(lang = 'en') {
  const dict = APP_TRANSLATIONS.en || {};
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (dict[key]) el.textContent = dict[key];
  });
}

/* ── 2. Coin Toss Player Linkage ── */
let coinSelectedPlayer = 'a';

function selectCoinPlayer(side) {
  coinSelectedPlayer = side;
  const btnA = document.getElementById('coinPlayerABtn');
  const btnB = document.getElementById('coinPlayerBBtn');
  if (btnA && btnB) {
    btnA.className = side === 'a' ? 'btn btn-primary btn-sm' : 'btn btn-outline btn-sm';
    btnB.className = side === 'b' ? 'btn btn-primary btn-sm' : 'btn btn-outline btn-sm';
  }
}

function assignTossWinnerServer() {
  state.servingSide = coinSelectedPlayer;
  updateLiveScoreboardUI();
  document.getElementById('coinTossModal').close();
  const match = state.matches.find(m => m.id === state.currentMatchId);
  const sName = match ? (coinSelectedPlayer === 'a' ? match.a : match.b) : `Player ${coinSelectedPlayer.toUpperCase()}`;
  showToast(`🎯 Initial serve assigned to ${sName}`);
}

/* ── 3. 7-Day Daily Claim Streak ── */
function getDailyStreak(username) {
  const data = JSON.parse(localStorage.getItem('badminton_daily_streaks') || '{}');
  return data[username] || { streak: 0, lastClaim: 0 };
}

function saveDailyStreak(username, streakObj) {
  const data = JSON.parse(localStorage.getItem('badminton_daily_streaks') || '{}');
  data[username] = streakObj;
  localStorage.setItem('badminton_daily_streaks', JSON.stringify(data));
}

// Override / Enhance claimDailyBonus for progressive 7-day rewards
const originalClaimDailyBonus = window.claimDailyBonus;
window.claimDailyBonus = function() {
  if (!requireAuthUser('claim daily bonus coins')) return;
  const username = currentUser.name;
  const remaining = getRemainingDailyClaimTime(username);
  if (remaining > 0) {
    const formatted = formatRemainingTime(remaining);
    showToast(`⏳ Daily bonus already claimed! Next bonus in ${formatted}.`, 'warning');
    updateClaimButtonUI();
    return;
  }

  const streakData = getDailyStreak(username);
  const now = Date.now();
  const hoursSinceLast = (now - streakData.lastClaim) / (1000 * 3600);

  let currentStreak = streakData.streak;
  if (hoursSinceLast > 48) {
    currentStreak = 1; // reset streak if missed a day
  } else {
    currentStreak = (currentStreak % 7) + 1;
  }

  const bonusSchedule = [50, 75, 100, 125, 150, 200, 300];
  const bonus = bonusSchedule[currentStreak - 1] || 50;

  const currentCoins = getUserCoins();
  setUserCoins(currentCoins + bonus);

  saveDailyStreak(username, { streak: currentStreak, lastClaim: now });

  const claims = getDailyClaimsDB();
  claims[username] = now;
  saveDailyClaimsDB(claims);

  recordTransaction(username, 'bonus', bonus, currentCoins + bonus, `Day ${currentStreak} streak bonus (+${bonus} coins)`);
  const bigCount = document.getElementById('coinModalBigCount');
  if (bigCount) bigCount.textContent = (currentCoins + bonus).toLocaleString();

  updateClaimButtonUI();
  showToast(`🎁 Day ${currentStreak} Streak! Claimed ${bonus} bonus coins! 🎉`);
  if (typeof confetti === 'function') confetti({ particleCount: 40, spread: 60 });
};

/* ── 4. Private Challenge Verification & QR Code ── */
function verifyAndAcceptChallengePin() {
  const targetId = document.getElementById('challengePinTargetId')?.value;
  const enteredPin = document.getElementById('challengeAcceptPinInput')?.value.trim();
  const list = getChallengesDB();
  const ch = list.find(c => c.id === targetId);
  if (!ch) {
    showToast('Challenge not found', 'warning');
    return;
  }
  if (ch.pin && ch.pin !== enteredPin) {
    showToast('❌ Incorrect 4-digit PIN! Please try again.', 'error');
    return;
  }
  document.getElementById('challengePinPromptModal').close();
  executeAcceptChallenge(targetId);
}

function openChallengeQrModal(chalId) {
  const modal = document.getElementById('challengeQrModal');
  if (!modal) return;
  const deepUrl = `${window.location.origin}${window.location.pathname}#challenge=${chalId}`;
  
  const linkText = document.getElementById('challengeDeepLinkText');
  if (linkText) linkText.textContent = deepUrl;

  // Render high-contrast inline SVG QR code
  const container = document.getElementById('challengeQrSvgContainer');
  if (container) {
    container.innerHTML = `
      <svg viewBox="0 0 100 100" width="180" height="180" style="shape-rendering:crispEdges;">
        <rect width="100" height="100" fill="#ffffff"/>
        <!-- Corners Finder Patterns -->
        <rect x="10" y="10" width="28" height="28" fill="#111827"/>
        <rect x="14" y="14" width="20" height="20" fill="#ffffff"/>
        <rect x="18" y="18" width="12" height="12" fill="#111827"/>
        <rect x="62" y="10" width="28" height="28" fill="#111827"/>
        <rect x="66" y="14" width="20" height="20" fill="#ffffff"/>
        <rect x="70" y="18" width="12" height="12" fill="#111827"/>
        <rect x="10" y="62" width="28" height="28" fill="#111827"/>
        <rect x="14" y="66" width="20" height="20" fill="#ffffff"/>
        <rect x="18" y="70" width="12" height="12" fill="#111827"/>
        <!-- Data Sync Dots -->
        <rect x="44" y="14" width="8" height="8" fill="#111827"/>
        <rect x="44" y="28" width="8" height="8" fill="#111827"/>
        <rect x="44" y="44" width="12" height="12" fill="#10b981"/>
        <rect x="24" y="44" width="8" height="8" fill="#111827"/>
        <rect x="68" y="44" width="8" height="8" fill="#111827"/>
        <rect x="44" y="68" width="8" height="8" fill="#111827"/>
        <rect x="62" y="62" width="12" height="12" fill="#111827"/>
        <rect x="78" y="78" width="12" height="12" fill="#111827"/>
      </svg>
    `;
  }
  modal.showModal();
}

function copyChallengeQrLink() {
  const linkText = document.getElementById('challengeDeepLinkText')?.textContent;
  if (linkText && navigator.clipboard) {
    navigator.clipboard.writeText(linkText);
    showToast('📋 Match link copied to clipboard!');
  }
}

/* ── 5. Cross-Tab Sync via BroadcastChannel ── */
let syncBroadcastChannel = null;
try {
  if (typeof BroadcastChannel !== 'undefined') {
    syncBroadcastChannel = new BroadcastChannel('badminton_cup_realtime_sync');
    syncBroadcastChannel.onmessage = (e) => {
      if (e.data === 'sync_challenges') {
        renderChallengesBoard();
      } else if (e.data === 'sync_scores') {
        if (typeof renderStadiumScreen === 'function') renderStadiumScreen();
      }
    };
  }
} catch (err) {
  console.log('BroadcastChannel not supported in this environment');
}

function broadcastSync(eventType) {
  if (syncBroadcastChannel) {
    syncBroadcastChannel.postMessage(eventType);
  }
}

/* ── 6. Court Conflict Scheduling Alerts ── */
function checkCourtScheduleConflicts() {
  const alertContainer = document.getElementById('scheduleConflictAlerts');
  if (!alertContainer) return;
  const conflicts = [];
  const matches = state.matches.filter(m => !m.winner && m.court && m.scheduledTime);

  for (let i = 0; i < matches.length; i++) {
    for (let j = i + 1; j < matches.length; j++) {
      const m1 = matches[i];
      const m2 = matches[j];
      if (m1.scheduledTime === m2.scheduledTime) {
        // Player overlapping across courts
        const players1 = [m1.a, m1.b];
        const players2 = [m2.a, m2.b];
        const overlap = players1.find(p => players2.includes(p));
        if (overlap) {
          conflicts.push(`⚠️ Conflict: <strong>${overlap}</strong> is scheduled on Court ${m1.court} and Court ${m2.court} at ${m1.scheduledTime}!`);
        }
      }
    }
  }

  if (conflicts.length > 0) {
    alertContainer.innerHTML = conflicts.map(c => `
      <div class="court-conflict-badge" style="display:block;margin-bottom:6px;padding:8px 12px;font-size:0.8rem;">${c}</div>
    `).join('');
    alertContainer.style.display = 'block';
  } else {
    alertContainer.style.display = 'none';
  }
}

/* ── 7. Athlete Elo Sparkline Renderer ── */
function drawEloSparkline(history) {
  const canvas = document.getElementById('playerEloSparkline');
  if (!canvas || !canvas.getContext) return;
  const ctx = canvas.getContext('2d');
  const w = canvas.width;
  const h = canvas.height;
  ctx.clearRect(0, 0, w, h);

  const points = (history && history.length >= 2) ? history : [1200, 1210, 1195, 1220, 1240, 1235, 1250];
  const min = Math.min(...points) - 10;
  const max = Math.max(...points) + 10;
  const step = w / (points.length - 1);

  ctx.beginPath();
  ctx.strokeStyle = '#10b981';
  ctx.lineWidth = 2.5;

  points.forEach((pt, idx) => {
    const x = idx * step;
    const y = h - ((pt - min) / (max - min)) * (h - 12) - 6;
    if (idx === 0) ctx.moveTo(x, y);
    else ctx.lineTo(x, y);
  });
  ctx.stroke();

  // Draw dot on latest point
  const lastX = w;
  const lastY = h - ((points[points.length - 1] - min) / (max - min)) * (h - 12) - 6;
  ctx.beginPath();
  ctx.arc(lastX - 4, lastY, 4, 0, Math.PI * 2);
  ctx.fillStyle = '#f59e0b';
  ctx.fill();
}

/* ── 8. Dual-Court Arena Split & Fullscreen ── */
let isDualCourtArena = false;

function toggleDualCourtArenaView() {
  const container = document.getElementById('stadiumCourtsContainer');
  const btn = document.getElementById('stadiumDualCourtBtn');
  if (!container) return;
  isDualCourtArena = !isDualCourtArena;

  if (isDualCourtArena) {
    container.classList.add('dual-court-container');
    if (btn) btn.textContent = 'Standard Grid View';
    showToast('🏟️ Dual-Court Arena View Enabled');
  } else {
    container.classList.remove('dual-court-container');
    if (btn) btn.textContent = 'Dual-Court Arena';
    showToast('Multi-Court Grid Restored');
  }
}

function toggleFullScreen() {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen().then(() => {
      showToast('⛶ Fullscreen Display Enabled');
      if (screen.orientation && screen.orientation.lock) {
        screen.orientation.lock('landscape').catch(() => {});
      }
    }).catch(() => {
      showToast('Fullscreen not permitted by browser');
    });
  } else {
    document.exitFullscreen().then(() => showToast('Fullscreen Exited'));
  }
}

/* ── 9. Transparent OBS Lower-Third Score Overlay ── */
function updateObsTicker() {
  const ticker = document.getElementById('obsTickerOverlay');
  if (!ticker || !state.currentMatchId) return;
  const match = state.matches.find(m => m.id === state.currentMatchId);
  if (!match) return;

  const set = match.sets[state.currentSetIdx];
  const scoreText = set ? `${set.score[0]} - ${set.score[1]}` : '0 - 0';

  const titleEl = document.getElementById('obsMatchTitle');
  const scoreEl = document.getElementById('obsScoreDisplay');
  const courtEl = document.getElementById('obsCourtLabel');

  if (titleEl) titleEl.textContent = `${match.a} vs ${match.b}`;
  if (scoreEl) scoreEl.textContent = scoreText;
  if (courtEl) courtEl.textContent = `COURT ${match.court || 1}`;
}

/* ── 10. Official BWF Printable Scorecard Generator ── */
function renderPrintableScorecard() {
  const container = document.getElementById('printableScorecardContent');
  if (!container) return;
  const match = state.matches.find(m => m.id === state.currentMatchId) || state.matches[0];
  if (!match) {
    container.innerHTML = '<p style="text-align:center;padding:20px;">No match loaded to print.</p>';
    return;
  }

  const s1 = match.sets[0] ? `${match.sets[0].score[0]} - ${match.sets[0].score[1]}` : '—';
  const s2 = match.sets[1] ? `${match.sets[1].score[0]} - ${match.sets[1].score[1]}` : '—';
  const s3 = match.sets[2] ? `${match.sets[2].score[0]} - ${match.sets[2].score[1]}` : '—';

  container.innerHTML = `
    <div style="border-bottom:2px solid #111827;padding-bottom:12px;margin-bottom:16px;display:flex;justify-content:space-between;align-items:flex-end;">
      <div>
        <h1 style="font-size:1.6rem;font-weight:900;margin:0;color:#111827;">BADMINTON CUP · OFFICIAL MATCH SCORE SHEET</h1>
        <div style="font-size:0.85rem;color:#4b5563;margin-top:2px;">Sanctioned Club & School Championship Fixture</div>
      </div>
      <div style="text-align:right;font-size:0.85rem;color:#4b5563;">
        <div><strong>Date:</strong> ${new Date().toLocaleDateString()}</div>
        <div><strong>Court:</strong> ${match.court || 1} · <strong>Pool:</strong> ${match.pool || 'Knockout'}</div>
      </div>
    </div>

    <table style="width:100%;border-collapse:collapse;margin-bottom:20px;font-size:0.95rem;">
      <thead>
        <tr style="background:#f3f4f6;border-bottom:2px solid #374151;">
          <th style="padding:10px;text-align:left;">Competitor</th>
          <th style="padding:10px;text-align:center;">Game 1</th>
          <th style="padding:10px;text-align:center;">Game 2</th>
          <th style="padding:10px;text-align:center;">Game 3</th>
          <th style="padding:10px;text-align:center;">Result</th>
        </tr>
      </thead>
      <tbody>
        <tr style="border-bottom:1px solid #e5e7eb;">
          <td style="padding:12px 10px;font-weight:700;">${match.a} (Team A)</td>
          <td style="padding:12px 10px;text-align:center;font-weight:800;">${match.sets[0] ? match.sets[0].score[0] : 0}</td>
          <td style="padding:12px 10px;text-align:center;font-weight:800;">${match.sets[1] ? match.sets[1].score[0] : '—'}</td>
          <td style="padding:12px 10px;text-align:center;font-weight:800;">${match.sets[2] ? match.sets[2].score[0] : '—'}</td>
          <td style="padding:12px 10px;text-align:center;font-weight:900;color:${match.winner === 'a' ? '#059669' : '#4b5563'};">${match.winner === 'a' ? 'WINNER' : ''}</td>
        </tr>
        <tr style="border-bottom:2px solid #374151;">
          <td style="padding:12px 10px;font-weight:700;">${match.b} (Team B)</td>
          <td style="padding:12px 10px;text-align:center;font-weight:800;">${match.sets[0] ? match.sets[0].score[1] : 0}</td>
          <td style="padding:12px 10px;text-align:center;font-weight:800;">${match.sets[1] ? match.sets[1].score[1] : '—'}</td>
          <td style="padding:12px 10px;text-align:center;font-weight:800;">${match.sets[2] ? match.sets[2].score[1] : '—'}</td>
          <td style="padding:12px 10px;text-align:center;font-weight:900;color:${match.winner === 'b' ? '#059669' : '#4b5563'};">${match.winner === 'b' ? 'WINNER' : ''}</td>
        </tr>
      </tbody>
    </table>

    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px;margin-top:36px;padding-top:20px;border-top:1px dashed #9ca3af;">
      <div>
        <div style="border-bottom:1px solid #111827;height:32px;"></div>
        <div style="font-size:0.75rem;font-weight:700;color:#374151;margin-top:4px;">Lead Umpire Signature</div>
      </div>
      <div>
        <div style="border-bottom:1px solid #111827;height:32px;"></div>
        <div style="font-size:0.75rem;font-weight:700;color:#374151;margin-top:4px;">Service Judge Signature</div>
      </div>
      <div>
        <div style="border-bottom:1px solid #111827;height:32px;"></div>
        <div style="font-size:0.75rem;font-weight:700;color:#374151;margin-top:4px;">Captain / Athlete Signature</div>
      </div>
    </div>
  `;
}

/* ── 11. Tournament Snapshot & Multi-Archive Switcher ── */
function saveTournamentSnapshot() {
  const input = document.getElementById('archiveTourneyNameInput');
  const name = (input && input.value.trim()) ? input.value.trim() : `Tournament ${new Date().toLocaleDateString()}`;
  const archives = JSON.parse(localStorage.getItem('badminton_tourney_archives') || '[]');

  archives.unshift({
    id: 'arch_' + Date.now(),
    name,
    date: new Date().toLocaleString(),
    stateSnapshot: JSON.stringify(state)
  });

  localStorage.setItem('badminton_tourney_archives', JSON.stringify(archives.slice(0, 10)));
  if (input) input.value = '';
  showToast(`📁 Tournament snapshot "${name}" saved!`);
  renderTournamentsArchiveList();
}

function renderTournamentsArchiveList() {
  const container = document.getElementById('tournamentsArchiveList');
  if (!container) return;
  const archives = JSON.parse(localStorage.getItem('badminton_tourney_archives') || '[]');

  if (archives.length === 0) {
    container.innerHTML = '<div style="color:var(--clr-text-muted);font-size:0.8rem;text-align:center;padding:12px;">No historical snapshots saved yet.</div>';
    return;
  }

  container.innerHTML = archives.map(a => `
    <div style="display:flex;justify-content:space-between;align-items:center;padding:8px;border-bottom:1px solid var(--clr-border);font-size:0.83rem;">
      <div>
        <strong style="color:var(--clr-text);">${a.name}</strong>
        <div style="font-size:0.72rem;color:var(--clr-text-muted);">${a.date}</div>
      </div>
      <button class="btn btn-outline btn-xs" onclick="restoreTournamentSnapshot('${a.id}')">Restore</button>
    </div>
  `).join('');
}

function restoreTournamentSnapshot(archId) {
  const archives = JSON.parse(localStorage.getItem('badminton_tourney_archives') || '[]');
  const target = archives.find(a => a.id === archId);
  if (!target) return;
  if (!confirm(`Restore snapshot "${target.name}"? Current unsaved tournament progress will be replaced.`)) return;

  try {
    const restoredState = JSON.parse(target.stateSnapshot);
    Object.assign(state, restoredState);
    saveState();
    renderAll();
    document.getElementById('tournamentArchiveModal').close();
    showToast(`✅ Successfully restored "${target.name}"`);
  } catch (err) {
    showToast('Failed to restore archive snapshot', 'error');
  }
}

/* ── 12. Modal Escape Key Dismissal & Global Focus Trap ── */
window.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    const openModals = document.querySelectorAll('dialog[open]');
    openModals.forEach(m => m.close());
  }
});

/* ── 13. Universal Hash Router & Manifest Shortcuts ── */
function handleAppHashRouting() {
  const hash = window.location.hash;
  if (!hash) return;

  if (hash === '#obs-ticker') {
    document.body.classList.add('obs-mode');
    document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
    const obsEl = document.getElementById('obsTickerOverlay');
    if (obsEl) obsEl.style.display = 'flex';
    setInterval(updateObsTicker, 800);
    return;
  }

  if (hash.startsWith('#challenge=')) {
    const cId = hash.replace('#challenge=', '');
    showScreen('challengesScreen');
    setTimeout(() => {
      const item = document.querySelector(`[data-challenge-id="${cId}"]`);
      if (item) {
        item.scrollIntoView({ behavior: 'smooth', block: 'center' });
        item.style.outline = '2px solid var(--clr-gold)';
      }
    }, 400);
    return;
  }

  const cleanScreenId = hash.slice(1);
  const targetScreen = document.getElementById(cleanScreenId);
  if (targetScreen && targetScreen.classList.contains('screen')) {
    showScreen(cleanScreenId);
  }
}

window.addEventListener('hashchange', handleAppHashRouting);

/* ── 14. Initialize Translations & Routing on Load ── */
document.addEventListener('DOMContentLoaded', () => {
  applyTranslations(currentAppLanguage);
  handleAppHashRouting();
  checkCourtScheduleConflicts();
});



/* ═══════════════════════════════════════════════════════════════
   ADVANCED BWF, BROADCAST, CERTIFICATES & HARDWARE LOGIC
   ═══════════════════════════════════════════════════════════════ */

/* ── 1. Disciplinary Sanctions (Yellow / Red / Black Card) ── */
let currentCardType = 'YELLOW';

function selectCardType(type) {
  currentCardType = type;
  document.getElementById('selectedCardType').value = type;
  ['Yellow', 'Red', 'Black'].forEach(t => {
    const btn = document.getElementById(`cardBtn${t}`);
    if (btn) btn.className = (t.toUpperCase() === type) ? 'btn btn-primary btn-sm' : 'btn btn-outline btn-sm';
  });
}

function confirmIssueDisciplinaryCard() {
  const match = state.matches.find(m => m.id === state.currentMatchId);
  if (!match) return;

  const side = document.getElementById('disciplinarySideSelect').value;
  const cardType = currentCardType;
  const reason = document.getElementById('disciplinaryReasonInput').value.trim() || 'Unsportsmanlike conduct';
  const targetName = side === 'a' ? match.a : match.b;
  const oppSide = side === 'a' ? 'b' : 'a';

  if (!match.disciplinaryCards) match.disciplinaryCards = [];
  match.disciplinaryCards.push({ side, card: cardType, reason, timestamp: Date.now() });

  if (!match.eventLog) match.eventLog = [];
  match.eventLog.push({ side, type: 'DISCIPLINARY', card: cardType, reason, timestamp: Date.now() });

  document.getElementById('disciplinaryCardModal').close();

  if (cardType === 'YELLOW') {
    showToast(`⚠️ Yellow Card issued to ${targetName} (${reason})`, 'warning');
    speakScoreAnnouncement(`Warning. Yellow card, ${targetName}.`);
  } else if (cardType === 'RED') {
    showToast(`🛑 Red Card issued to ${targetName}! 1 Penalty Point awarded to opponent.`, 'error');
    speakScoreAnnouncement(`Fault. Red card, ${targetName}.`);
    scorePoint(oppSide); // Red Card awards point to opponent under BWF 16.7
  } else if (cardType === 'BLACK') {
    showToast(`⬛ Black Card! ${targetName} Disqualified from match!`, 'error');
    speakScoreAnnouncement(`Disqualification. Black card, ${targetName}.`);
    match.winner = oppSide;
    match.winType = 'DISQUALIFIED';
    saveState();
    updateLiveScoreboardUI();
  }
}

/* ── 2. Medical Timeout Timer (5 Minutes) ── */
let medicalInterval = null;
let medicalSecondsLeft = 300;

function startMedicalTimeout() {
  const modal = document.getElementById('medicalTimeoutModal');
  if (!modal) return;
  medicalSecondsLeft = 300;
  updateMedicalClockUI();
  modal.showModal();

  if (medicalInterval) clearInterval(medicalInterval);
  medicalInterval = setInterval(() => {
    medicalSecondsLeft--;
    updateMedicalClockUI();
    if (medicalSecondsLeft <= 0) {
      clearInterval(medicalInterval);
      showToast('⏰ Medical Recovery Timeout Expired! Play must resume.');
      speakScoreAnnouncement('Time. Play must resume.');
      playSound('point');
    }
  }, 1000);
}

function updateMedicalClockUI() {
  const m = Math.floor(medicalSecondsLeft / 60).toString().padStart(2, '0');
  const s = (medicalSecondsLeft % 60).toString().padStart(2, '0');
  const clock = document.getElementById('medicalTimerClock');
  if (clock) clock.textContent = `${m}:${s}`;
}

function stopMedicalTimeout() {
  if (medicalInterval) clearInterval(medicalInterval);
  const note = document.getElementById('medicalInjuryNote')?.value.trim();
  const match = state.matches.find(m => m.id === state.currentMatchId);
  if (match && note) {
    if (!match.eventLog) match.eventLog = [];
    match.eventLog.push({ type: 'MEDICAL_TIMEOUT', note, timestamp: Date.now() });
  }
  document.getElementById('medicalTimeoutModal').close();
  showToast('Medical break concluded. Resuming match.');
}

function addMedicalMinute() {
  medicalSecondsLeft += 60;
  updateMedicalClockUI();
  showToast('+1 Minute added to recovery interval');
}

/* ── 3. Shuttlecock & Rally Shot Counters ── */
function incrementShuttleCount() {
  const match = state.matches.find(m => m.id === state.currentMatchId);
  if (!match) return;
  match.shuttlesUsed = (match.shuttlesUsed || 1) + 1;
  const val = document.getElementById('shuttleCountVal');
  if (val) val.textContent = match.shuttlesUsed;
  showToast(`🏸 Shuttlecock changed. Total used: ${match.shuttlesUsed}`);
}

function incrementRallyShots() {
  const match = state.matches.find(m => m.id === state.currentMatchId);
  if (!match) return;
  match.currentRallyShots = (match.currentRallyShots || 0) + 1;
  const val = document.getElementById('rallyShotsVal');
  if (val) val.textContent = match.currentRallyShots;
}

/* ── 4. Bluetooth Remote Shutter / Media Clicker ── */
window.addEventListener('keydown', (e) => {
  const umpireScreen = document.getElementById('liveUmpireScreen');
  if (!umpireScreen || !umpireScreen.classList.contains('active')) return;

  // Handle standard Bluetooth selfie remote & media presentation clicker keycodes
  if (e.key === 'VolumeUp' || e.code === 'AudioVolumeUp') {
    e.preventDefault();
    scorePoint(state.servingSide); // Score for Server
  } else if (e.key === 'VolumeDown' || e.code === 'AudioVolumeDown') {
    e.preventDefault();
    scorePoint(state.servingSide === 'a' ? 'b' : 'a'); // Score for Receiver
  } else if (e.key === 'MediaPlayPause' || e.key === 'AudioVolumeMute') {
    e.preventDefault();
    undoPoint(); // Remote Undo
  }
});

/* ── 5. Official Printable Certificate Generator ── */
function openAthleteCertificateModal(playerName) {
  const name = playerName || (currentUser ? currentUser.name : 'Tournament Athlete');
  const modal = document.getElementById('certificatePrintModal');
  const container = document.getElementById('certificateContainerContent');
  if (!modal || !container) return;

  container.innerHTML = `
    <div class="certificate-frame">
      <div style="font-size:2.8rem;margin-bottom:8px;">🏸</div>
      <h1 style="font-family:'Anton',serif;font-size:2.4rem;letter-spacing:1px;color:#111827;margin:0 0 6px;">CERTIFICATE OF ACHIEVEMENT</h1>
      <p style="font-size:0.95rem;text-transform:uppercase;letter-spacing:2px;color:#059669;font-weight:700;margin:0 0 24px;">Annual Badminton Cup Championship</p>
      
      <p style="font-size:1.05rem;color:#4b5563;margin-bottom:8px;">This is proudly presented to</p>
      <div style="font-size:2.2rem;font-weight:900;color:#111827;border-bottom:2px solid #10b981;display:inline-block;padding:0 32px 6px;margin-bottom:16px;">
        ${name}
      </div>
      
      <p style="font-size:0.95rem;color:#4b5563;max-width:580px;margin:0 auto 36px;line-height:1.6;">
        In recognition of outstanding athletic excellence, competitive integrity, and exceptional performance displayed in the official badminton tournament.
      </p>

      <div style="display:flex;justify-content:space-between;align-items:flex-end;margin-top:40px;padding:0 40px;">
        <div style="text-align:center;">
          <div style="font-weight:700;color:#111827;font-size:0.95rem;">${new Date().toLocaleDateString()}</div>
          <div style="border-top:1px solid #9ca3af;padding-top:4px;font-size:0.75rem;color:#6b7280;margin-top:4px;">Date of Issue</div>
        </div>
        <div style="text-align:center;">
          <div style="font-family:cursive;font-size:1.3rem;color:#10b981;">Rashed Khan</div>
          <div style="border-top:1px solid #9ca3af;padding-top:4px;font-size:0.75rem;color:#6b7280;margin-top:4px;">Tournament Director</div>
        </div>
      </div>
    </div>
  `;

  modal.showModal();
}

/* ── 6. Printable Tournament ID Badges Generator ── */
function openPlayerIdBadgesModal() {
  const modal = document.getElementById('playerIdBadgesModal');
  const container = document.getElementById('idBadgesGridContainer');
  if (!modal || !container) return;

  const users = (typeof getUsersDB === 'function') ? getUsersDB() : [];
  const players = (state.players && state.players.length) ? state.players : users.map(u => u.name);

  if (!players || !players.length) {
    container.innerHTML = `
      <div style="grid-column:1/-1;text-align:center;padding:36px;color:var(--clr-text-muted);">
        No registered athletes found. Add players in Tournament Setup or Member Registry to generate passes.
      </div>
    `;
    modal.showModal();
    return;
  }

  container.innerHTML = players.map(p => {
    const avatarHtml = typeof getPlayerAvatarHtml === 'function' ? getPlayerAvatarHtml(p, 48) : '';
    return `
      <div style="border:2px solid #111827;border-radius:10px;padding:16px;background:#ffffff;color:#111827;text-align:center;box-shadow:0 2px 6px rgba(0,0,0,0.1);">
        <div style="font-size:0.7rem;font-weight:900;letter-spacing:1px;color:#059669;text-transform:uppercase;">BADMINTON CUP · OFFICIAL PASS</div>
        <div style="margin:12px auto;display:flex;justify-content:center;">${avatarHtml}</div>
        <div style="font-size:1.15rem;font-weight:900;color:#111827;">${escapeHtml(p)}</div>
        <div style="font-size:0.75rem;color:#4b5563;font-weight:700;margin-top:2px;">ATHLETE · BWF REGISTERED</div>
        <div style="margin-top:12px;border-top:1px dashed #d1d5db;padding-top:8px;font-family:monospace;font-size:0.7rem;letter-spacing:4px;color:#6b7280;">||| | |||| | ||| ||</div>
      </div>
    `;
  }).join('');

  modal.showModal();
}

/* ── 7. Consolation / Plate Bracket Generator ── */
function generateConsolationBracket() {
  if (!state.koRounds || state.koRounds.length === 0) {
    showToast('Generate main knockout bracket first!', 'warning');
    return;
  }
  const round1 = state.koRounds[0];
  const round1Matches = round1.map(id => state.matches.find(m => m.id === id)).filter(Boolean);
  const completed = round1Matches.filter(m => m.winner);
  if (completed.length < 2) {
    showToast('Round 1 matches must be played before generating consolation bracket.', 'warning');
    return;
  }

  const losers = round1Matches.map(m => m.winner === 'a' ? m.b : m.a).filter(Boolean);
  state.plateMatches = [];
  for (let i = 0; i < losers.length; i += 2) {
    if (i + 1 < losers.length) {
      const match = createMatchObj(losers[i], losers[i + 1], 'PLATE');
      state.matches.push(match);
      state.plateMatches.push(match.id);
    }
  }

  saveState();
  showToast(`🏅 Consolation Plate bracket generated with ${state.plateMatches.length} fixtures!`);
  showScreen('knockoutScreen');
}

/* ── 8. Schedule Court Matrix Timetable ── */
let currentScheduleView = 'list';

function toggleScheduleViewMode(mode) {
  currentScheduleView = mode;
  const listEl = document.getElementById('scheduleMatchesList');
  const matrixEl = document.getElementById('scheduleMatrixContainer');
  const btnList = document.getElementById('schedViewListBtn');
  const btnMatrix = document.getElementById('schedViewMatrixBtn');

  if (mode === 'matrix') {
    if (listEl) listEl.style.display = 'none';
    if (matrixEl) {
      matrixEl.style.display = 'block';
      renderScheduleMatrix();
    }
    if (btnList) btnList.classList.remove('active');
    if (btnMatrix) btnMatrix.classList.add('active');
  } else {
    if (listEl) listEl.style.display = 'grid';
    if (matrixEl) matrixEl.style.display = 'none';
    if (btnList) btnList.classList.add('active');
    if (btnMatrix) btnMatrix.classList.remove('active');
  }
}

function renderScheduleMatrix() {
  const container = document.getElementById('scheduleMatrixContainer');
  if (!container) return;

  const courts = [1, 2];
  const times = ['10:00 AM', '10:30 AM', '11:00 AM', '11:30 AM', '12:00 PM', '12:30 PM'];

  let html = `
    <table class="schedule-matrix-table">
      <thead>
        <tr>
          <th style="width:120px;">Time Slot</th>
          <th>Court 1</th>
          <th>Court 2</th>
        </tr>
      </thead>
      <tbody>
  `;

  times.forEach((t, idx) => {
    html += `<tr><td style="font-weight:700;color:var(--clr-gold);">${t}</td>`;
    courts.forEach(c => {
      const match = state.matches.find(m => m.court === c && m.scheduledTime === t) || state.matches[idx * 2 + (c - 1)];
      if (match) {
        html += `
          <td>
            <div class="schedule-matrix-cell-match" onclick="startUmpireMatch('${match.id}')">
              <strong>${match.a}</strong> vs <strong>${match.b}</strong>
              <div style="font-size:0.7rem;color:var(--clr-text-muted);margin-top:2px;">${match.winner ? '✓ Completed' : 'Tap to Referee'}</div>
            </div>
          </td>
        `;
      } else {
        html += `<td style="color:var(--clr-text-muted);opacity:0.5;">— Available —</td>`;
      }
    });
    html += `</tr>`;
  });

  html += `</tbody></table>`;
  container.innerHTML = html;
}

/* ── 9. Interactive Pool Draw Ceremony Wheel ── */
let poolWheelAngle = 0;
let isWheelSpinning = false;

function initPoolDrawCanvas() {
  const canvas = document.getElementById('poolDrawCanvas');
  if (!canvas || !canvas.getContext) return;
  const ctx = canvas.getContext('2d');
  const users = (typeof getUsersDB === 'function') ? getUsersDB() : [];
  const players = (state.players && state.players.length) ? state.players : users.map(u => u.name);

  if (!players || players.length === 0) {
    ctx.clearRect(0, 0, 240, 240);
    ctx.fillStyle = 'rgba(255, 255, 255, 0.04)';
    ctx.beginPath();
    ctx.arc(120, 120, 110, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = 'var(--clr-border)';
    ctx.stroke();
    ctx.fillStyle = 'var(--clr-text-muted)';
    ctx.font = '12px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('No players in roster', 120, 125);
    return;
  }

  const numSlices = players.length;
  const sliceAngle = (2 * Math.PI) / numSlices;
  const colors = ['#10b981', '#06b6d4', '#f59e0b', '#3b82f6', '#ec4899', '#8b5cf6', '#14b8a6', '#f97316'];

  ctx.clearRect(0, 0, 240, 240);
  ctx.save();
  ctx.translate(120, 120);
  ctx.rotate(poolWheelAngle);

  for (let i = 0; i < numSlices; i++) {
    ctx.beginPath();
    ctx.fillStyle = colors[i % colors.length];
    ctx.moveTo(0, 0);
    ctx.arc(0, 0, 120, i * sliceAngle, (i + 1) * sliceAngle);
    ctx.lineTo(0, 0);
    ctx.fill();

    ctx.save();
    ctx.rotate(i * sliceAngle + sliceAngle / 2);
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 11px sans-serif';
    ctx.textAlign = 'right';
    ctx.fillText(players[i].slice(0, 8), 108, 4);
    ctx.restore();
  }

  ctx.restore();
}

function spinPoolDrawWheel() {
  if (isWheelSpinning) return;
  const users = (typeof getUsersDB === 'function') ? getUsersDB() : [];
  const players = (state.players && state.players.length) ? state.players : users.map(u => u.name);

  if (!players || players.length === 0) {
    showToast('Add players to roster before spinning the draw wheel.', 'warning');
    return;
  }

  isWheelSpinning = true;
  const resText = document.getElementById('wheelCurrentDrawnText');
  if (resText) resText.textContent = 'Spinning...';

  const totalRotations = Math.PI * 2 * 5 + Math.random() * Math.PI * 2;
  const startTime = Date.now();
  const duration = 3000;

  function animate() {
    const elapsed = Date.now() - startTime;
    const progress = Math.min(1, elapsed / duration);
    const easeOut = 1 - Math.pow(1 - progress, 3);
    poolWheelAngle = easeOut * totalRotations;
    initPoolDrawCanvas();

    if (progress < 1) {
      requestAnimationFrame(animate);
    } else {
      isWheelSpinning = false;
      const picked = players[Math.floor(Math.random() * players.length)];
      if (resText) resText.textContent = `🎯 Selected: ${picked}!`;
      playSound('point');
      if (typeof confetti === 'function') confetti({ particleCount: 50, spread: 70 });
    }
  }
  requestAnimationFrame(animate);
}

/* ── 10. AMOLED Battery Saver Mode ── */
function toggleAmoledBatterySaver() {
  const isEnabled = document.body.classList.toggle('battery-saver');
  localStorage.setItem('badminton_battery_saver', isEnabled ? 'true' : 'false');
  showToast(isEnabled ? '🔋 AMOLED Battery Saver Enabled (OLED Black)' : 'Standard Theme Restored');
}

/* ── 11. Storage Prune & Clean Exporter ── */
function pruneOldMatchHistory() {
  const completed = state.matches.filter(m => m.winner);
  if (completed.length === 0) {
    showToast('No completed matches to prune.', 'info');
    return;
  }

  // Backup state to JSON file download first
  const dataStr = 'data:text/json;charset=utf-8,' + encodeURIComponent(JSON.stringify(state));
  const downloadAnchor = document.createElement('a');
  downloadAnchor.setAttribute('href', dataStr);
  downloadAnchor.setAttribute('download', `badminton_cup_backup_${Date.now()}.json`);
  document.body.appendChild(downloadAnchor);
  downloadAnchor.click();
  downloadAnchor.remove();

  // Strip excessive rally events from historical matches to free storage
  state.matches.forEach(m => {
    if (m.winner) {
      delete m.history;
      delete m.eventLog;
    }
  });

  saveState();
  showToast('🧹 Storage compressed! Full JSON backup downloaded.');
}

/* ── 12. Floating Spectator Cheer Reactions ── */
function sendSpectatorCheer(emoji) {
  const bubble = document.createElement('div');
  bubble.className = 'cheer-reaction-bubble';
  bubble.textContent = emoji || '👏';
  bubble.style.left = `${Math.random() * 80 + 10}%`;
  bubble.style.bottom = '80px';
  document.body.appendChild(bubble);
  setTimeout(() => bubble.remove(), 1200);
  broadcastSync('sync_cheer');
}

/* ── 13. Horizontal Touch Swipe Gestures for Mobile Navigation ── */
let touchStartX = 0;
let touchEndX = 0;

document.addEventListener('touchstart', (e) => {
  touchStartX = e.changedTouches[0].screenX;
}, { passive: true });

document.addEventListener('touchend', (e) => {
  touchEndX = e.changedTouches[0].screenX;
  handleSwipeGesture();
}, { passive: true });

function handleSwipeGesture() {
  const diff = touchEndX - touchStartX;
  if (Math.abs(diff) < 90) return; // Ignore small swipes

  const screens = ['groupsScreen', 'challengesScreen', 'knockoutScreen', 'leaderboardScreen'];
  const currentActive = screens.find(id => document.getElementById(id)?.classList.contains('active'));
  if (!currentActive) return;

  const idx = screens.indexOf(currentActive);
  if (diff < 0 && idx < screens.length - 1) {
    showScreen(screens[idx + 1]); // Swipe Left -> Next Screen
  } else if (diff > 0 && idx > 0) {
    showScreen(screens[idx - 1]); // Swipe Right -> Prev Screen
  }
}

</script>
"""
