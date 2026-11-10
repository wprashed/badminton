# HTML Screens module for Badminton Cup
SCREENS_CONTENT = """
<header class="top-bar">
  <div class="brand-title">
    <button class="btn btn-ghost btn-xs" onclick="showScreen('groupsScreen')" title="Badminton Cup Home" style="padding:4px;border:none;">
      <svg class="icon icon-md" viewBox="0 0 24 24" style="color:var(--clr-green);"><path d="M12 2l3 7h-6l3-7zM7 9l-4 8 7 5 3-4-6-9zM17 9l4 8-7 5-3-4 6-9z"/></svg>
    </button>
    <h1 class="brand-heading" onclick="showScreen('groupsScreen')" style="cursor:pointer;">Badminton <span class="accent">Cup</span></h1>
    <span class="sync-pill" id="networkSyncPill" title="Application Network and Sync Status">
      <svg class="icon icon-xs" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 14 14"/></svg>
      <span id="syncStatusLabel">Online</span>
    </span>
  </div>
  <div id="ariaLiveAnnouncer" class="sr-only" aria-live="polite" aria-atomic="true" style="position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0;"></div>

  <div style="display:flex;align-items:center;gap:6px;flex-shrink:0;">
    <!-- Push Notification Bell -->
    <button class="notify-btn" id="notifyBtn" onclick="openNotificationModal()" title="Push Notifications">
      <svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg>
      <span class="notify-badge-dot"></span>
    </button>

    <!-- Theme Toggle (Light / Dark) -->
    <button class="notify-btn" id="headerThemeBtn" onclick="toggleThemeMode()" title="Toggle Light / Dark Mode" aria-label="Toggle Light / Dark Mode">
      <svg class="icon icon-xs" id="themeIconSun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
      <svg class="icon icon-xs" id="themeIconMoon" viewBox="0 0 24 24" style="display:none;"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
    </button>

    <!-- PWA Install Button -->
    
    <!-- Virtual Coin Wallet for General Users -->
    <button class="btn btn-ghost btn-xs" id="headerCoinBtn" onclick="openCoinBalanceModal()" title="Virtual Coin Balance & Predictions" style="color:var(--clr-gold);font-weight:700;border-color:rgba(245,158,11,0.3);background:rgba(245,158,11,0.08);">
      <span style="font-size:0.9rem;">🪙</span> <span id="headerCoinCount">100</span>
    </button>
<button class="install-app-pill" id="installAppBtn" onclick="promptInstallPWA()" style="display:none;" title="Install Badminton Cup App">
      <svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
      <span data-i18n="installApp">Install</span>
    </button>

    <!-- More / Menu Button -->
    <button class="btn btn-ghost btn-xs" id="headerMoreBtn" onclick="openMoreMenu()" title="More Tools & Menu">
      <svg class="icon icon-xs" viewBox="0 0 24 24"><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/><circle cx="5" cy="12" r="1"/></svg>
      <span data-i18n="navMore">Menu</span>
    </button>

    <!-- User Panel / Sign In -->
    <div class="user-panel" id="userStatusPanel">
      <div class="user-avatar" id="headerAvatar">?</div>
      <span class="user-name-label" id="headerUsername" style="display:none;">Guest</span>
      <button class="btn btn-primary btn-xs" id="authBtn" onclick="openAuthModal()">Sign In</button>
    </div>
  </div>
</header>

<!-- Global Tournament Stage Navigation (Desktop 5-Tab Bar) -->
<nav class="app-stage-nav" id="appStageNav" aria-label="Tournament Stages">
  <div class="stage-nav-inner">
    <button class="stage-tab active" id="tabNavMatches" onclick="showScreen('groupsScreen')">
      <span class="tab-icon"><svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M12 2l3 7h-6l3-7zM7 9l-4 8 7 5 3-4-6-9zM17 9l4 8-7 5-3-4 6-9z"/></svg></span>
      <span data-i18n="navMatches">Matches & Courts</span>
    </button>
    <button class="stage-tab" id="tabNavChallenges" onclick="showScreen('challengesScreen')">
      <span class="tab-icon"><svg class="icon icon-xs" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg></span>
      <span data-i18n="navChallenges">Open Challenges</span>
    </button>
    <button class="stage-tab" id="tabNavKnockout" onclick="showScreen('knockoutScreen')">
      <span class="tab-icon"><svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6M18 9h1.5a2.5 2.5 0 0 0 0-5H18M4 22h16M10 14.66V17c0 .55-.45 1-1 1H8c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1h8c.55 0 1-.45 1-1v-1c0-.55-.45-1-1-1h-1c-.55 0-1-.45-1-1v-2.34c3.38-.6 6-3.5 6-6.99V4H4v3.67c0 3.49 2.62 6.39 6 6.99z"/></svg></span>
      <span data-i18n="navBracket">Playoff Bracket</span>
    </button>
    <button class="stage-tab" id="tabNavLeaderboard" onclick="showScreen('leaderboardScreen')">
      <span class="tab-icon"><svg class="icon icon-xs" viewBox="0 0 24 24"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg></span>
      <span data-i18n="navRanking">Standings & Ranks</span>
    </button>
    <button class="stage-tab" id="tabNavMore" onclick="openMoreMenu()">
      <span class="tab-icon"><svg class="icon icon-xs" viewBox="0 0 24 24"><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/><circle cx="5" cy="12" r="1"/></svg></span>
      <span data-i18n="navMore">More Tools</span>
    </button>
  </div>
</nav>

<main class="main-content">

  <!-- ═══════════════════════════════════════════════════
       1. SETUP SCREEN (ENHANCED WITH REGISTERED USERS)
  ═══════════════════════════════════════════════════ -->
  <section id="setupScreen" class="screen">
    <div class="card" style="max-width:880px;margin:0 auto;">
      <div class="card-header">
        <div>
          <h2 class="card-title"><svg class="icon icon-md" viewBox="0 0 24 24"><path d="M12 2l3 7h-6l3-7zM7 9l-4 8 7 5 3-4-6-9zM17 9l4 8-7 5-3-4 6-9z"/></svg> Tournament Registration & Configuration</h2>
          <p style="color:var(--clr-text-muted);font-size:0.88rem;margin-top:4px;">Multi-court scheduling, category formats, registered player selection, and fees.</p>
        </div>
        <div style="display:flex;gap:8px;flex-wrap:wrap;">
          <button class="btn btn-primary btn-xs" onclick="openPlayerPickerModal()"><svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg> Pick Registered Users</button>
          <button class="btn btn-ghost btn-xs" onclick="openBulkRosterModal()"><svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/></svg> Bulk Roster</button>
          <button class="btn btn-ghost btn-xs" onclick="loadDemoData()"><svg class="icon icon-xs" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg> Demo Roster</button>
        </div>
      </div>

      <!-- Quick Launch Banner -->
      <div style="background:var(--clr-surface-card);border:1px solid var(--clr-border);border-left:3px solid var(--clr-green);border-radius:var(--radius-sm);padding:14px 18px;margin-bottom:20px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;">
        <div>
          <div style="font-weight:900;font-size:0.95rem;color:var(--clr-green);display:flex;align-items:center;gap:6px;">
            <span><svg class="icon icon-xs" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg></span>
            <span>Quick Start Launcher</span>
          </div>
          <div style="font-size:0.8rem;color:var(--clr-text-muted);margin-top:2px;">
            Kick off a tournament instantly with pre-seeded BWF champions or pick from your active registry.
          </div>
        </div>
        <div style="display:flex;gap:8px;flex-wrap:wrap;">
          <button class="btn btn-primary btn-xs" onclick="loadDemoData()"><svg class="icon icon-xs" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg> Load Pro Demo Roster</button>
          <button class="btn btn-ghost btn-xs" onclick="openPlayerPickerModal('A')"><svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg> Pick Athletes</button>
        </div>
      </div>

      <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(min(100%, 240px), 1fr));gap:16px;margin-bottom:20px;">
        <div>
          <label style="font-size:0.8rem;font-weight:700;color:var(--clr-text-muted);display:block;margin-bottom:6px;">Tournament Name</label>
          <input type="text" id="tournamentTitleInput" class="modal-input" value="The Badminton Cup 2026" oninput="updateTournamentTitle(this.value)">
        </div>
        <div>
          <label style="font-size:0.8rem;font-weight:700;color:var(--clr-text-muted);display:block;margin-bottom:6px;">Category Mode</label>
          <div style="display:flex;gap:8px;">
            <button class="btn btn-ghost btn-sm active" id="btnCatSingles" onclick="selectCategory('singles')" style="flex:1;">Singles (1v1)</button>
            <button class="btn btn-ghost btn-sm" id="btnCatDoubles" onclick="selectCategory('doubles')" style="flex:1;">Doubles (2v2)</button>
          </div>
        </div>
        <div>
          <label style="font-size:0.8rem;font-weight:700;color:var(--clr-text-muted);display:block;margin-bottom:6px;">Registration Fee / Athlete</label>
          <input type="text" id="tournamentFeeInput" class="modal-input" value="$20.00" placeholder="$20.00 or 250 Coins">
        </div>
      </div>

      <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(min(100%, 200px), 1fr));gap:16px;margin-bottom:20px;">
        <div>
          <label style="font-size:0.8rem;font-weight:700;color:var(--clr-text-muted);display:block;margin-bottom:6px;">Points to Win Set</label>
          <div style="display:flex;gap:6px;">
            <button class="btn btn-ghost btn-xs" onclick="selectPoints(11)" id="ptsBtn11">11 pts</button>
            <button class="btn btn-ghost btn-xs" onclick="selectPoints(15)" id="ptsBtn15">15 pts</button>
            <button class="btn btn-ghost btn-xs active" onclick="selectPoints(21)" id="ptsBtn21">21 pts (BWF)</button>
            <button class="btn btn-ghost btn-xs" onclick="selectPoints(30)" id="ptsBtn30">30 pts</button>
          </div>
        </div>
        <div>
          <label style="font-size:0.8rem;font-weight:700;color:var(--clr-text-muted);display:block;margin-bottom:6px;">Match Format</label>
          <div style="display:flex;gap:6px;">
            <button class="btn btn-ghost btn-xs" onclick="selectBestOf(1)" id="bestOfBtn1">Best of 1</button>
            <button class="btn btn-ghost btn-xs active" onclick="selectBestOf(3)" id="bestOfBtn3">Best of 3</button>
            <button class="btn btn-ghost btn-xs" onclick="selectBestOf(5)" id="bestOfBtn5">Best of 5</button>
          </div>
        </div>
        <div>
          <label style="font-size:0.8rem;font-weight:700;color:var(--clr-text-muted);display:block;margin-bottom:6px;">Courts Available in Arena</label>
          <select id="courtSelectInput" class="modal-input" onchange="selectCourtNum(this.value)">
            <option value="1">1 Court (Centre Court)</option>
            <option value="2">2 Courts Parallel</option>
            <option value="3">3 Courts</option>
            <option value="4">4 Courts Arena</option>
          </select>
        </div>
      </div>

      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:20px;">
        <div>
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
            <label style="font-size:0.8rem;font-weight:700;color:var(--clr-text-muted);margin:0;">
              <span id="playerPoolLabelA">Pool A Roster</span> (<span id="countA">0</span>)
            </label>
            <button class="btn btn-ghost btn-xs" onclick="openPlayerPickerModal('A')">+ Add Registered</button>
          </div>
          <textarea id="rosterAInput" class="modal-input" rows="7" placeholder="Enter player or pair names, one per line..." oninput="updatePlayerCounts()"></textarea>
        </div>
        <div>
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
            <label style="font-size:0.8rem;font-weight:700;color:var(--clr-text-muted);margin:0;">
              <span id="playerPoolLabelB">Pool B Roster</span> (<span id="countB">0</span>)
            </label>
            <button class="btn btn-ghost btn-xs" onclick="openPlayerPickerModal('B')">+ Add Registered</button>
          </div>
          <textarea id="rosterBInput" class="modal-input" rows="7" placeholder="Enter player or pair names, one per line..." oninput="updatePlayerCounts()"></textarea>
        </div>
      </div>

      <div style="display:flex;justify-content:space-between;align-items:center;border-top:1px solid var(--clr-border);padding-top:16px;flex-wrap:wrap;gap:12px;">
        <div style="display:flex;align-items:center;gap:14px;flex-wrap:wrap;">
          <label style="font-size:0.82rem;font-weight:700;display:flex;align-items:center;gap:6px;cursor:pointer;">
            <input type="checkbox" id="audioToggleCheckbox" checked onchange="toggleAudioFx(this.checked)">
            <span>Sound Effects & Speech</span>
          </label>
          <label style="font-size:0.82rem;font-weight:700;display:flex;align-items:center;gap:6px;cursor:pointer;" title="Allow starting point handicap">
            <input type="checkbox" id="handicapToggleCheckbox" onchange="toggleHandicapMode(this.checked)">
            <span>Starting Point Handicap</span>
          </label>
        </div>
        <div style="display:flex;gap:10px;">
          <button class="btn btn-ghost" onclick="resetTournamentState()">Reset</button>
          <button class="btn btn-primary btn-lg" onclick="initiateTournament()">Start Tournament &rarr;</button>
        </div>
      </div>
    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════
       2. DRAFT ANIMATION SCREEN
  ═══════════════════════════════════════════════════ -->
  <section id="draftScreen" class="screen">
    <div class="card" style="text-align:center;max-width:750px;margin:0 auto;">
      <h2 class="card-title" style="justify-content:center;margin-bottom:8px;"><svg class="icon icon-md" viewBox="0 0 24 24"><polyline points="16 3 21 3 21 8"/><line x1="4" y1="20" x2="21" y2="3"/><polyline points="21 16 21 21 16 21"/><line x1="15" y1="15" x2="21" y2="21"/><line x1="4" y1="4" x2="9" y2="9"/></svg> Drum Slot Team Draft</h2>
      <p style="color:var(--clr-text-muted);font-size:0.88rem;margin-bottom:24px;">Shuffling athletes and seeding into balanced tournament brackets.</p>

      <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:24px;">
        <div style="background:rgba(0,0,0,0.3);border:2px solid var(--clr-border);border-radius:var(--radius-md);padding:20px;">
          <h3 style="color:#60a5fa;font-family:var(--font-display);font-size:1.3rem;margin-bottom:12px;">POOL A DRUM</h3>
          <div id="drumSlotA" style="font-size:1.4rem;font-weight:900;min-height:50px;display:flex;align-items:center;justify-content:center;color:#fff;">READY</div>
        </div>
        <div style="background:rgba(0,0,0,0.3);border:2px solid var(--clr-border);border-radius:var(--radius-md);padding:20px;">
          <h3 style="color:#f87171;font-family:var(--font-display);font-size:1.3rem;margin-bottom:12px;">POOL B DRUM</h3>
          <div id="drumSlotB" style="font-size:1.4rem;font-weight:900;min-height:50px;display:flex;align-items:center;justify-content:center;color:#fff;">READY</div>
        </div>
      </div>

      <div id="draftSummaryBox" style="display:none;margin-bottom:24px;text-align:left;background:rgba(0,0,0,0.2);padding:16px;border-radius:var(--radius-sm);"></div>

      <div style="display:flex;justify-content:center;gap:12px;">
        <button class="btn btn-ghost" id="skipDraftBtn" onclick="skipDraftAnimation()">Skip Animation &rarr;</button>
        <button class="btn btn-primary btn-lg" id="confirmDraftBtn" onclick="confirmDraftAndAdvance()" style="display:none;">Proceed to Stage Matches &rarr;</button>
      </div>
    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════
       3. GROUP STAGES SCREEN
  ═══════════════════════════════════════════════════ -->
  <section id="groupsScreen" class="screen active">
    <!-- Friendly Quick Start / Welcome Launcher for School Students & Players -->
    <div id="groupsWelcomeBanner" style="background:var(--clr-surface-card);border:1px solid var(--clr-border);border-left:3px solid var(--clr-green);border-radius:var(--radius-sm);padding:14px 18px;margin-bottom:20px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;">
      <div>
        <div style="font-weight:900;font-size:1rem;color:var(--clr-green);display:flex;align-items:center;gap:6px;">
          <svg class="icon icon-xs" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
          <span>Welcome to Badminton Cup!</span>
        </div>
        <div style="font-size:0.82rem;color:var(--clr-text-muted);margin-top:2px;">
          Jump straight into matches, challenge anyone on the open board, or start a new tournament.
        </div>
      </div>
      <div style="display:flex;gap:8px;flex-wrap:wrap;">
        <button class="btn btn-primary btn-xs" onclick="openNewChallengeModal()">
          <svg class="icon icon-xs" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
          <span data-i18n="createChalBtn">+ Open Challenge</span>
        </button>
        <button class="btn btn-ghost btn-xs" onclick="handleSetupNav()">
          <svg class="icon icon-xs" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
          <span>Tournament Setup</span>
          <span style="font-size:0.6rem;font-weight:700;color:#f87171;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);padding:1px 5px;border-radius:3px;">🛡️ Admin</span>
        </button>
        <button class="btn btn-ghost btn-xs" onclick="loadDemoData()">
          <svg class="icon icon-xs" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
          <span>Load Demo</span>
        </button>
      </div>
    </div>



    <!-- Navigation & Action bar -->
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:20px;flex-wrap:wrap;gap:12px;">
      <div style="display:flex;gap:12px;align-items:center;flex-wrap:wrap;">
        <h2 style="font-family:var(--font-display);font-size:1.45rem;font-weight:800;color:var(--clr-text);letter-spacing:-0.01em;margin:0;">Group Stage & Standings</h2>
        <select id="groupCourtFilter" style="padding:6px 14px;font-size:0.82rem;font-weight:600;background:rgba(255,255,255,0.05);border:1px solid var(--clr-border);border-radius:var(--radius-sm);color:var(--clr-text);font-family:inherit;cursor:pointer;" onchange="renderGroupMatches()">
          <option value="all">Court: All Courts</option>
          <option value="1">Court 1</option>
          <option value="2">Court 2</option>
          <option value="3">Court 3</option>
          <option value="4">Court 4</option>
        </select>
      </div>
      <div style="display:flex;gap:8px;flex-wrap:wrap;">
        <button class="btn btn-ghost btn-sm" onclick="showScreen('scheduleScreen')"><svg class="icon icon-xs" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg> Match Schedule</button>
        <button class="btn btn-ghost btn-sm" onclick="showScreen('analyticsScreen')"><svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M16 16l3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1zM2 16l3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1zM7 21h10M12 3v18M3 7h18"/></svg> H2H Analytics</button>
        <button class="btn btn-ghost btn-sm" onclick="openSuggestScoreModal()"><svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg> Suggest Score</button>
        <button class="btn btn-ghost btn-sm" onclick="simulateAllGroupGames()"><svg class="icon icon-xs" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg> Auto-Simulate Group</button>
        <button class="btn btn-primary btn-sm" onclick="generateKnockoutFromGroups()">Proceed to Knockout &rarr;</button>
      </div>
    </div>

    <!-- Pools Grid -->
    <div class="pools-grid" style="display:grid;grid-template-columns:repeat(auto-fit, minmax(min(100%, 320px), 1fr));gap:16px;margin-bottom:24px;">
      <!-- Pool A -->
      <div class="card">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
          <h3 style="font-family:var(--font-display);font-size:1.05rem;font-weight:700;color:var(--clr-text);margin:0;">Pool A Standings</h3>
          <span style="background:rgba(96,165,250,0.15);color:#60a5fa;border:1px solid rgba(96,165,250,0.3);font-size:0.68rem;padding:2px 8px;border-radius:4px;font-weight:700;">Group A · BWF Rules</span>
        </div>
        <div class="data-table-container">
          <table class="data-table">
            <thead>
              <tr>
                <th>#</th>
                <th>Athlete / Pair</th>
                <th>W</th>
                <th>L</th>
                <th>Diff</th>
                <th>Pts</th>
              </tr>
            </thead>
            <tbody id="poolATableBody"></tbody>
          </table>
        </div>
      </div>

      <!-- Pool B -->
      <div class="card">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
          <h3 style="font-family:var(--font-display);font-size:1.05rem;font-weight:700;color:var(--clr-text);margin:0;">Pool B Standings</h3>
          <span style="background:rgba(248,113,113,0.15);color:#f87171;border:1px solid rgba(248,113,113,0.3);font-size:0.68rem;padding:2px 8px;border-radius:4px;font-weight:700;">Group B · BWF Rules</span>
        </div>
        <div class="data-table-container">
          <table class="data-table">
            <thead>
              <tr>
                <th>#</th>
                <th>Athlete / Pair</th>
                <th>W</th>
                <th>L</th>
                <th>Diff</th>
                <th>Pts</th>
              </tr>
            </thead>
            <tbody id="poolBTableBody"></tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Match Schedule List -->
    <div class="card">
      <div class="card-header">
        <h3 class="card-title"><svg class="icon icon-md" viewBox="0 0 24 24"><path d="M12 2l3 7h-6l3-7zM7 9l-4 8 7 5 3-4-6-9zM17 9l4 8-7 5-3-4 6-9z"/></svg> Group Stage Fixtures & Live Matches</h3>
        <span style="font-size:0.78rem;color:var(--clr-text-muted);">Tap "Referee" on any match for live court scoring</span>
      </div>
      <div id="groupMatchesContainer" style="display:grid;grid-template-columns:repeat(auto-fill, minmax(min(100%, 300px), 1fr));gap:14px;"></div>
    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════
       4. LIVE UMPIRE SCOREBOARD SCREEN
  ═══════════════════════════════════════════════════ -->
  <section id="liveUmpireScreen" class="screen">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;flex-wrap:wrap;gap:10px;">
      <div style="display:flex;align-items:center;gap:10px;">
        <button class="btn btn-ghost btn-xs" onclick="exitLiveScoreboard()">&larr; Exit Umpire View</button>
        <span id="umpireMatchHeader" style="font-size:0.9rem;font-weight:800;color:var(--clr-text-muted);">Court 1 · Official Umpire Scoreboard</span>
      </div>
      <div style="display:flex;align-items:center;gap:8px;">
        <span id="matchDurationClock" style="font-family:monospace;font-size:0.95rem;background:rgba(0,0,0,0.3);padding:4px 8px;border-radius:4px;border:1px solid var(--clr-border);">00:00</span>
        <button class="btn btn-ghost btn-xs" onclick="toggleCourtFlip()" id="flipCourtBtn" title="Flip court display 180° for umpire sitting opposite"><svg class="icon icon-xs" viewBox="0 0 24 24"><polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/></svg> Flip Court</button>
        <button class="btn btn-ghost btn-xs" onclick="openScorecardModal()" title="Print Signable BWF Scorecard"><svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/></svg> Scorecard</button>
        <button class="btn btn-ghost btn-xs" onclick="openSoundSettingsModal()" title="Voice & Volume Settings"><svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/></svg> Audio</button>
      </div>
    </div>

    <!-- Live Status Banner (Game Point / Match Point / Deuce / Sudden Death) -->
    <div id="liveStatusBanner" style="text-align:center;margin-bottom:14px;min-height:30px;"></div>

    <!-- Mini Court Visualizer -->
    <div class="court-container" id="courtContainer">
      <div class="badminton-court">
        <!-- Side A -->
        <div class="court-side" id="sideA_box">
          <div class="court-box" id="courtA_left">
            <span class="court-box-label">LEFT (ODD)</span>
            <span class="court-player-name" id="posA_left"></span>
          </div>
          <div class="court-box" id="courtA_right">
            <span class="court-box-label">RIGHT (EVEN)</span>
            <span class="court-player-name" id="posA_right"></span>
          </div>
        </div>

        <!-- Net -->
        <div class="court-net-line"></div>

        <!-- Side B -->
        <div class="court-side court-side-b" id="sideB_box">
          <div class="court-box" id="courtB_right">
            <span class="court-box-label">RIGHT (EVEN)</span>
            <span class="court-player-name" id="posB_right"></span>
          </div>
          <div class="court-box" id="courtB_left">
            <span class="court-box-label">LEFT (ODD)</span>
            <span class="court-player-name" id="posB_left"></span>
          </div>
        </div>
      </div>
    </div>

    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;flex-wrap:wrap;gap:8px;">
      <div class="diagonal-indicator" id="serviceCalloutText">Serving: Player A from RIGHT (Even) Court</div>
      <div id="serviceReceiverCallout" style="font-size:0.78rem;color:var(--clr-text-muted);font-weight:700;"></div>
    </div>

    <!-- Scoreboard Panels -->
    <div class="score-board-grid">
      <!-- Side A -->
      <div class="score-side-panel" id="panelSideA">
        <div class="player-name-main" id="nameSideA" style="color:#60a5fa;">Athlete A</div>
        <div class="score-digit" id="scoreDigitA">0</div>
        <div class="set-pips" id="pipsA"></div>
        <div style="margin-top:16px;">
          <button class="btn btn-primary btn-lg" style="width:100%;font-size:1.15rem;padding:16px;" onclick="scorePoint('a')" title="Award point to Side A (Hotkey: 1 or A)">
            <span>+ Point Side A</span>
            <kbd class="kbd-hint">[1]</kbd>
          </button>
        </div>
      </div>

      <!-- Center Vs / Set Counter -->
      <div style="text-align:center;">
        <div style="font-size:0.75rem;font-weight:800;color:var(--clr-text-muted);letter-spacing:0.1em;text-transform:uppercase;">Set</div>
        <div id="currentSetNumber" style="font-family:var(--font-display);font-size:2.8rem;color:var(--clr-gold);">1</div>
        <button class="btn btn-ghost btn-xs" onclick="toggleServerManual()" title="Toggle serving side manually (Hotkey: Space)">
          <span>Switch Serve</span>
          <kbd class="kbd-hint">[Space]</kbd>
        </button>
      </div>

      <!-- Side B -->
      <div class="score-side-panel" id="panelSideB">
        <div class="player-name-main" id="nameSideB" style="color:#f87171;">Athlete B</div>
        <div class="score-digit" id="scoreDigitB">0</div>
        <div class="set-pips" id="pipsB"></div>
        <div style="margin-top:16px;">
          <button class="btn btn-primary btn-lg" style="width:100%;font-size:1.15rem;padding:16px;" onclick="scorePoint('b')" title="Award point to Side B (Hotkey: 2 or D)">
            <span>+ Point Side B</span>
            <kbd class="kbd-hint">[2]</kbd>
          </button>
        </div>
      </div>
    </div>

    <!-- Umpire Tools Bar -->
    <div style="display:flex;justify-content:center;gap:10px;flex-wrap:wrap;margin-bottom:20px;">
      <button class="btn btn-ghost btn-sm" onclick="undoPoint()" title="Undo last scored point (Hotkey: U or Ctrl+Z)">
        <span>Undo</span>
        <kbd class="kbd-hint">[U]</kbd>
      </button>
      <button class="btn btn-ghost btn-sm" onclick="triggerEndsSwitch()" title="Switch court sides (Hotkey: F)">⇄ Change Ends</button>
      <button class="btn btn-ghost btn-sm" onclick="triggerIntervalTimer(60)"><svg class="icon icon-xs" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> 60s Break</button>
      <button class="btn btn-ghost btn-sm" onclick="triggerIntervalTimer(120)"><svg class="icon icon-xs" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> 120s Interval</button>
      <button class="btn btn-ghost btn-sm" onclick="speakScoreAnnouncement()" title="Repeat speech score callout (Hotkey: S)">
        <span><svg class="icon icon-xs" viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg> Callout</span>
        <kbd class="kbd-hint">[S]</kbd>
      </button>
      <button class="btn btn-ghost btn-sm" style="color:#fde047;" onclick="openWalkoverModal('yellow')"><span style="display:inline-block;width:10px;height:14px;background:#f59e0b;border-radius:2px;vertical-align:-2px;margin-right:4px;"></span>Warning</button>
      <button class="btn btn-danger btn-sm" onclick="openWalkoverModal('red')"><span style="display:inline-block;width:10px;height:14px;background:#ef4444;border-radius:2px;vertical-align:-2px;margin-right:4px;"></span>Red Card</button>
      <button class="btn btn-ghost btn-sm" style="border-color:#334155;color:#94a3b8;" onclick="openWalkoverModal('black')"><span style="display:inline-block;width:10px;height:14px;background:#0f172a;border:1px solid #64748b;border-radius:2px;vertical-align:-2px;margin-right:4px;"></span>Black Card</button>
      <button class="btn btn-ghost btn-sm" onclick="triggerLetCall()"><svg class="icon icon-xs" viewBox="0 0 24 24"><polyline points="1 4 1 10 7 10"/><path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"/></svg> Let (Re-serve)</button>
      <button class="btn btn-danger btn-sm" onclick="openWalkoverModal('black')">⬛ Black Card (DQ)</button>
      <button class="btn btn-ghost btn-sm" style="color:#f87171;" onclick="openWalkoverModal('wo')">Walkover (W.O.)</button>
    </div>

    <!-- Interval Countdown Overlay -->
    <div id="intervalTimerOverlay" style="display:none;background:rgba(0,0,0,0.85);border:2px solid var(--clr-gold);border-radius:var(--radius-md);padding:18px;text-align:center;margin-bottom:20px;">
      <div style="font-size:0.8rem;color:var(--clr-gold);font-weight:900;text-transform:uppercase;letter-spacing:0.1em;">BWF Umpire Interval</div>
      <div id="intervalSecondsDisplay" style="font-family:var(--font-display);font-size:3rem;color:#fff;">60s</div>
      <button class="btn btn-ghost btn-xs" onclick="dismissInterval()">Resume Match Now</button>
    </div>

    <!-- Hotkeys Legend -->
    <div class="hotkey-legend">
      <span><kbd>1</kbd> / <kbd>A</kbd> Point A</span>
      <span><kbd>2</kbd> / <kbd>D</kbd> Point B</span>
      <span><kbd>Ctrl+Z</kbd> / <kbd>U</kbd> Undo</span>
      <span><kbd>Space</kbd> Toggle Serve</span>
      <span><kbd>S</kbd> Announce Voice</span>
      <span><kbd>F</kbd> Flip Court 180°</span>
    </div>

    <!-- Match History Log -->
    <div class="card" style="margin-top:20px;">
      <h3 class="card-title" style="font-size:1.1rem;margin-bottom:12px;">Point-by-Point Timeline</h3>
      <div id="matchRallyLog" style="max-height:160px;overflow-y:auto;font-size:0.82rem;color:var(--clr-text-muted);display:flex;flex-direction:column;gap:6px;"></div>
    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════
       5. TOURNAMENT SCHEDULE & TIMETABLE SCREEN
  ═══════════════════════════════════════════════════ -->
  <section id="scheduleScreen" class="screen">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:20px;flex-wrap:wrap;gap:12px;">
      <div>
        <h2 style="font-family:var(--font-display);font-size:1.6rem;text-transform:uppercase;"><svg class="icon icon-md" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg> Tournament Match Schedule & Timetable</h2>
        <p style="color:var(--clr-text-muted);font-size:0.85rem;">Chronological order of play, court assignments, and match status.</p>
      </div>
      <div style="display:flex;gap:8px;flex-wrap:wrap;">
        <button class="btn btn-ghost btn-sm" onclick="showScreen('groupsScreen')">&larr; Back to Groups</button>
        <button class="btn btn-primary btn-sm" onclick="showScreen('stadiumScreen')"><svg class="icon icon-xs" viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="15" rx="2" ry="2"/><polyline points="17 2 12 7 7 2"/></svg> Arena TV</button>
      </div>
    </div>

    <!-- Filter Bar -->
    <div class="schedule-filter-bar">
      <div style="display:flex;align-items:center;gap:8px;">
        <span style="font-size:0.8rem;font-weight:700;color:var(--clr-text-muted);">Court:</span>
        <select id="scheduleCourtFilter" class="modal-input" style="width:auto;padding:4px 10px;font-size:0.82rem;" onchange="renderScheduleScreen()">
          <option value="all">All Courts</option>
          <option value="1">Court 1 (Centre Court)</option>
          <option value="2">Court 2</option>
          <option value="3">Court 3</option>
          <option value="4">Court 4</option>
        </select>
      </div>

      <div style="display:flex;align-items:center;gap:8px;">
        <span style="font-size:0.8rem;font-weight:700;color:var(--clr-text-muted);">Status:</span>
        <select id="scheduleStatusFilter" class="modal-input" style="width:auto;padding:4px 10px;font-size:0.82rem;" onchange="renderScheduleScreen()">
          <option value="all">All Matches</option>
          <option value="live">Live Now</option>
          <option value="upcoming">Scheduled / Upcoming</option>
          <option value="completed">Completed</option>
        </select>
      </div>

      <div style="display:flex;align-items:center;gap:8px;">
        <span style="font-size:0.8rem;font-weight:700;color:var(--clr-text-muted);">Stage:</span>
        <select id="scheduleStageFilter" class="modal-input" style="width:auto;padding:4px 10px;font-size:0.82rem;" onchange="renderScheduleScreen()">
          <option value="all">All Stages</option>
          <option value="groups">Group Stage (Pool A & B)</option>
          <option value="knockout">Playoff Elimination</option>
        </select>
      </div>
    </div>

    <!-- Match List Timeline Container -->
    <div id="scheduleTimelineContainer" style="display:flex;flex-direction:column;gap:12px;"></div>
  </section>

  <!-- ═══════════════════════════════════════════════════
       6. ANALYTICS & HEAD-TO-HEAD (H2H) SCREEN
  ═══════════════════════════════════════════════════ -->
  <section id="analyticsScreen" class="screen">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:20px;flex-wrap:wrap;gap:12px;">
      <div>
        <h2 style="font-family:var(--font-display);font-size:1.25rem;font-weight:700;"><svg class="icon icon-md" viewBox="0 0 24 24"><path d="M16 16l3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1zM2 16l3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1zM7 21h10M12 3v18M3 7h18"/></svg> Head-to-Head & Player Analytics</h2>
        <p style="color:var(--clr-text-muted);font-size:0.85rem;">Compare athlete records, Elo ratings, point differential, and historical matchups.</p>
      </div>
      <div style="display:flex;gap:8px;">
        <button class="btn btn-ghost btn-sm" onclick="showScreen('leaderboardScreen')"><svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6M18 9h1.5a2.5 2.5 0 0 0 0-5H18M4 22h16M10 14.66V17c0 .55-.45 1-1 1H8c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1h8c.55 0 1-.45 1-1v-1c0-.55-.45-1-1-1h-1c-.55 0-1-.45-1-1v-2.34c3.38-.6 6-3.5 6-6.99V4H4v3.67c0 3.49 2.62 6.39 6 6.99z"/></svg> View Hall of Fame</button>
      </div>
    </div>

    <div class="card" style="margin-bottom:24px;">
      <div style="display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:16px;margin-bottom:20px;">
        <div>
          <label style="font-size:0.8rem;font-weight:700;color:var(--clr-text-muted);display:block;margin-bottom:6px;">Select Athlete A</label>
          <select id="analyticsPlayerASelect" class="modal-input" onchange="runAnalyticsComparison()"></select>
        </div>
        <div style="font-family:var(--font-display);font-size:1.6rem;color:var(--clr-gold);text-align:center;padding-top:16px;">VS</div>
        <div>
          <label style="font-size:0.8rem;font-weight:700;color:var(--clr-text-muted);display:block;margin-bottom:6px;">Select Athlete B</label>
          <select id="analyticsPlayerBSelect" class="modal-input" onchange="runAnalyticsComparison()"></select>
        </div>
      </div>

      <div id="analyticsComparisonResult"></div>
    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════
       7. OFFICIAL BWF RULES & REGULATIONS HUB
  ═══════════════════════════════════════════════════ -->
    <!-- ═══════════════════════════════════════════════════
       7. COMPLETE USER GUIDE & BWF RULES HUB
  ═══════════════════════════════════════════════════ -->
  <section id="rulesScreen" class="screen">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:20px;flex-wrap:wrap;gap:12px;">
      <div>
        <h2 style="font-family:var(--font-display);font-size:1.3rem;font-weight:800;display:flex;align-items:center;gap:8px;">
          <svg class="icon icon-md" viewBox="0 0 24 24"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
          <span>Complete User Guide & BWF Rules</span>
        </h2>
        <p style="color:var(--clr-text-muted);font-size:0.85rem;margin-top:2px;">
          Everything you need to know about playing, scoring, challenges, betting, and official BWF laws.
        </p>
      </div>
      <button class="btn btn-ghost btn-sm" onclick="showScreen('groupsScreen')">&larr; Back to Matches</button>
    </div>

    <!-- Guide Sub-Navigation Tabs -->
    <div style="display:flex;gap:8px;margin-bottom:20px;overflow-x:auto;padding-bottom:6px;border-bottom:1px solid var(--clr-border);">
      <button class="btn btn-ghost btn-sm active" id="guideTabAppBtn" onclick="switchGuideTab('app')">
        📱 App User Guide
      </button>
      <button class="btn btn-ghost btn-sm" id="guideTabRulesBtn" onclick="switchGuideTab('rules')">
        🏸 Official BWF Rules
      </button>
      <button class="btn btn-ghost btn-sm" id="guideTabRolesBtn" onclick="switchGuideTab('roles')">
        🛡️ Roles & Permissions
      </button>
      <button class="btn btn-ghost btn-sm" id="guideTabFaqBtn" onclick="switchGuideTab('faq')">
        ❓ Frequently Asked Questions
      </button>
    </div>

    <!-- ── TAB 1: APP USER GUIDE ── -->
    <div id="guideSectionApp" class="guide-content-section">
      <!-- Quick Start Overview -->
      <div class="card" style="margin-bottom:20px;background:var(--clr-surface-card);border:1px solid var(--clr-border);border-left:3px solid var(--clr-green);">
        <h3 style="font-size:1.1rem;font-weight:800;color:var(--clr-green);margin-bottom:8px;display:flex;align-items:center;gap:6px;">
          <svg class="icon icon-sm" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
          Quick Start: Get Started in 30 Seconds
        </h3>
        <p style="font-size:0.88rem;color:var(--clr-text);line-height:1.5;">
          Badminton Cup is built for casual players, school students, and professional tournament directors. 
          You can jump directly into matches, open challenges for classmates or colleagues, bet virtual coins on match winners, or manage full multi-court tournament brackets.
        </p>
      </div>

      <!-- Step-by-Step Grid -->
      <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(min(100%, 280px), 1fr));gap:16px;margin-bottom:24px;">
        <!-- Step 1 -->
        <div class="card" style="padding:18px;">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
            <span style="width:28px;height:28px;border-radius:50%;background:rgba(16,185,129,0.15);color:var(--clr-green);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:0.85rem;">1</span>
            <h4 style="font-size:0.95rem;font-weight:700;color:var(--clr-text);margin:0;">Open Challenges</h4>
          </div>
          <p style="font-size:0.82rem;color:var(--clr-text-muted);line-height:1.45;margin-bottom:10px;">
            Head to the <strong>Challenges</strong> tab to post an open match invite. Enter your name, choose Singles or Doubles, set target points (e.g. 21 pts), and write your court location.
          </p>
          <div style="font-size:0.75rem;color:var(--clr-green);font-weight:600;">✓ Open to all general users & students</div>
        </div>

        <!-- Step 2 -->
        <div class="card" style="padding:18px;">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
            <span style="width:28px;height:28px;border-radius:50%;background:rgba(16,185,129,0.15);color:var(--clr-green);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:0.85rem;">2</span>
            <h4 style="font-size:0.95rem;font-weight:700;color:var(--clr-text);margin:0;">Instant Winner & Scoring</h4>
          </div>
          <p style="font-size:0.82rem;color:var(--clr-text-muted);line-height:1.45;margin-bottom:10px;">
            On any match card on the <strong>Matches</strong> tab, you can record a game in 3 ways:
          </p>
          <ul style="font-size:0.8rem;color:var(--clr-text-muted);padding-left:18px;line-height:1.4;">
            <li><strong>[🏆 Team Won]</strong>: 1-tap instant 2-0 victory.</li>
            <li><strong>[⚡ Score]</strong>: Type exact final set scores (e.g. 21–18).</li>
            <li><strong>[🏸 Referee]</strong>: Point-by-point live umpire with speech.</li>
          </ul>
        </div>

        <!-- Step 3 -->
        <div class="card" style="padding:18px;">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
            <span style="width:28px;height:28px;border-radius:50%;background:rgba(245,158,11,0.15);color:var(--clr-gold);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:0.85rem;">3</span>
            <h4 style="font-size:0.95rem;font-weight:700;color:var(--clr-text);margin:0;">Virtual Coin Betting</h4>
          </div>
          <p style="font-size:0.82rem;color:var(--clr-text-muted);line-height:1.45;margin-bottom:10px;">
            Every user starts with <strong>100 free coins</strong>. Tap <strong>[🎲 Predict]</strong> on any scheduled match to wager coins on Team A or Team B at 1.90x odds.
          </p>
          <div style="font-size:0.75rem;color:var(--clr-gold);font-weight:600;">✓ Instant automatic coin payouts on match win!</div>
        </div>

        <!-- Step 4 -->
        <div class="card" style="padding:18px;">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
            <span style="width:28px;height:28px;border-radius:50%;background:rgba(6,182,212,0.15);color:var(--clr-cyan);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:0.85rem;">4</span>
            <h4 style="font-size:0.95rem;font-weight:700;color:var(--clr-text);margin:0;">PWA & Push Notifications</h4>
          </div>
          <p style="font-size:0.82rem;color:var(--clr-text-muted);line-height:1.45;margin-bottom:10px;">
            Install the app on your phone via the <strong>+ Install</strong> button or browser menu. Tap the 🔔 bell in the top bar to enable live alerts for match finishes and open challenges.
          </p>
          <div style="font-size:0.75rem;color:var(--clr-cyan);font-weight:600;">✓ Works 100% offline with cached service worker</div>
        </div>
      </div>
    </div>

    <!-- ── TAB 2: OFFICIAL BWF RULES & LAWS ── -->
    <div id="guideSectionRules" class="guide-content-section" style="display:none;">
      <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(min(100%, 300px), 1fr));gap:18px;margin-bottom:24px;">
        <div class="rules-card">
          <h3>21-Point Rally Scoring System</h3>
          <p style="font-size:0.85rem;color:var(--clr-text-muted);">
            A match consists of the best of 3 games of 21 points. The side winning a rally adds a point to its score regardless of who served.
          </p>
          <div class="rules-callout">
            <strong>Deuce Rule:</strong> At 20-all, the side which gains a 2-point lead first wins the game (e.g. 22-20, 24-22).
          </div>
          <div class="rules-callout">
            <strong>Sudden Death Cap:</strong> At 29-all, the side scoring the 30th point wins the game (30-29 max cap).
          </div>
        </div>

        <div class="rules-card">
          <h3>Service Courts & Diagonal Serving</h3>
          <p style="font-size:0.85rem;color:var(--clr-text-muted);">
            Service court position is determined strictly by the server's score:
          </p>
          <div class="rules-callout">
            <strong>0 or Even Score (0, 2, 4, 6...):</strong> Serve from the <strong>RIGHT</strong> service court into the diagonal right court.
          </div>
          <div class="rules-callout">
            <strong>Odd Score (1, 3, 5, 7...):</strong> Serve from the <strong>LEFT</strong> service court into the diagonal left court.
          </div>
        </div>

        <div class="rules-card">
          <h3>Intervals & Change of Ends</h3>
          <p style="font-size:0.85rem;color:var(--clr-text-muted);">
            Standard rest and coaching intervals:
          </p>
          <div class="rules-callout">
            <strong>11-Point Interval:</strong> A 60-second break occurs when the leading score reaches 11 points in any game.
          </div>
          <div class="rules-callout">
            <strong>Between Games:</strong> A 120-second (2-minute) interval is allowed between games.
          </div>
          <div class="rules-callout">
            <strong>Deciding 3rd Game:</strong> Players change ends when the leading score reaches 11 points.
          </div>
        </div>

        <div class="rules-card">
          <h3>Card Penalties & Disciplinary Code</h3>
          <p style="font-size:0.85rem;color:var(--clr-text-muted);">
            The umpire administers official cards for misconduct or intentional delay:
          </p>
          <div class="rules-callout" style="border-color:#fde047;">
            <strong style="color:#fde047;">🟨 Yellow Card:</strong> Warning for misconduct or time wasting.
          </div>
          <div class="rules-callout" style="border-color:#ef4444;">
            <strong style="color:#fca5a5;">🟥 Red Card:</strong> Fault awarded against offender; 1 point awarded to opponent.
          </div>
          <div class="rules-callout" style="border-color:#94a3b8;">
            <strong style="color:#f1f5f9;">⬛ Black Card:</strong> Disqualification from tournament (awarded by Referee).
          </div>
        </div>
      </div>

      <!-- Interactive Service Court Simulator -->
      <div class="card" style="margin-bottom:24px;">
        <h3 class="card-title" style="margin-bottom:12px;">Interactive Service Court Calculator</h3>
        <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;">
          <label for="ruleScoreTestInput" style="font-size:0.85rem;font-weight:700;">Enter Server's Current Score:</label>
          <input type="number" id="ruleScoreTestInput" class="modal-input" style="width:120px;" value="14" min="0" max="30" oninput="testRuleServiceCourt(this.value)">
          <div id="ruleScoreTestResult" style="font-weight:800;font-size:0.95rem;color:var(--clr-gold);">Right (Even) Court &rarr; Serving diagonally to Right Court</div>
        </div>
      </div>
    </div>

    <!-- ── TAB 3: ROLES & CAPABILITIES REFERENCE ── -->
    <div id="guideSectionRoles" class="guide-content-section" style="display:none;">
      <div class="card" style="margin-bottom:20px;overflow-x:auto;">
        <h3 class="card-title" style="margin-bottom:14px;">Capabilities & Permissions Matrix</h3>
        <table class="table" style="width:100%;font-size:0.86rem;">
          <thead>
            <tr>
              <th style="text-align:left;">Feature / Capability</th>
              <th style="text-align:center;">General User (Player / Guest)</th>
              <th style="text-align:center;">Tournament Director (Admin)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Open Public Challenges</strong></td>
              <td style="text-align:center;color:var(--clr-green);font-weight:700;">✓ Allowed</td>
              <td style="text-align:center;color:var(--clr-green);font-weight:700;">✓ Allowed</td>
            </tr>
            <tr>
              <td><strong>Accept & Play Matches</strong></td>
              <td style="text-align:center;color:var(--clr-green);font-weight:700;">✓ Allowed</td>
              <td style="text-align:center;color:var(--clr-green);font-weight:700;">✓ Allowed</td>
            </tr>
            <tr>
              <td><strong>Virtual Coin Betting & Predictions</strong></td>
              <td style="text-align:center;color:var(--clr-green);font-weight:700;">✓ Allowed (100 free coins)</td>
              <td style="text-align:center;color:var(--clr-green);font-weight:700;">✓ Allowed</td>
            </tr>
            <tr>
              <td><strong>Live Referee Umpire Mode</strong></td>
              <td style="text-align:center;color:var(--clr-green);font-weight:700;">✓ Allowed</td>
              <td style="text-align:center;color:var(--clr-green);font-weight:700;">✓ Allowed</td>
            </tr>
            <tr>
              <td><strong>View Standings, Bracket & Stats</strong></td>
              <td style="text-align:center;color:var(--clr-green);font-weight:700;">✓ Allowed</td>
              <td style="text-align:center;color:var(--clr-green);font-weight:700;">✓ Allowed</td>
            </tr>
            <tr>
              <td><strong>Configure Tournament & Roster</strong></td>
              <td style="text-align:center;color:var(--clr-red);font-weight:750;">✕ Admin Guard</td>
              <td style="text-align:center;color:var(--clr-green);font-weight:700;">✓ Full Control</td>
            </tr>
            <tr>
              <td><strong>Run / Re-shuffle Pool Draw</strong></td>
              <td style="text-align:center;color:var(--clr-red);font-weight:750;">✕ Admin Guard</td>
              <td style="text-align:center;color:var(--clr-green);font-weight:700;">✓ Full Control</td>
            </tr>
            <tr>
              <td><strong>Override Official Match Scores</strong></td>
              <td style="text-align:center;color:var(--clr-red);font-weight:750;">✕ Admin Guard</td>
              <td style="text-align:center;color:var(--clr-green);font-weight:700;">✓ Full Control</td>
            </tr>
            <tr>
              <td><strong>Reset Data / Factory Reset</strong></td>
              <td style="text-align:center;color:var(--clr-red);font-weight:750;">✕ Admin Guard</td>
              <td style="text-align:center;color:var(--clr-green);font-weight:700;">✓ Full Control</td>
            </tr>
            <tr>
              <td><strong>Director Dashboard & Audit Logs</strong></td>
              <td style="text-align:center;color:var(--clr-red);font-weight:750;">✕ Admin Guard</td>
              <td style="text-align:center;color:var(--clr-green);font-weight:700;">✓ Full Control</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div style="text-align:center;margin-top:14px;">
        <button class="btn btn-primary btn-sm" onclick="toggleRoleDemo()">
          ⚡ Quick Switch Role (Toggle Admin / Player)
        </button>
      </div>
    </div>

    <!-- ── TAB 4: FREQUENTLY ASKED QUESTIONS (FAQ) ── -->
    <div id="guideSectionFaq" class="guide-content-section" style="display:none;">
      <div style="display:flex;flex-direction:column;gap:12px;margin-bottom:24px;">
        <div class="card" style="padding:16px;">
          <h4 style="font-size:0.95rem;font-weight:700;color:var(--clr-text);margin-bottom:6px;">
            Q: How do I start a tournament from scratch?
          </h4>
          <p style="font-size:0.84rem;color:var(--clr-text-muted);line-height:1.45;">
            Switch to Admin mode (or sign in as Director), open the Menu, and select <strong>Setup & Roster</strong>. You can click <strong>"Load Pro Demo Roster"</strong> to instantly populate 8 world champions, or enter your own custom player roster and click <strong>"Start Tournament"</strong>.
          </p>
        </div>

        <div class="card" style="padding:16px;">
          <h4 style="font-size:0.95rem;font-weight:700;color:var(--clr-text);margin-bottom:6px;">
            Q: Can I use this app without an internet connection?
          </h4>
          <p style="font-size:0.84rem;color:var(--clr-text-muted);line-height:1.45;">
            Yes! Badminton Cup is a full Progressive Web App (PWA) with a Service Worker cache. Once loaded, you can score matches, flip coins, view rules, and record results completely offline in a gym or school court.
          </p>
        </div>

        <div class="card" style="padding:16px;">
          <h4 style="font-size:0.95rem;font-weight:700;color:var(--clr-text);margin-bottom:6px;">
            Q: Are coins real money?
          </h4>
          <p style="font-size:0.84rem;color:var(--clr-text-muted);line-height:1.45;">
            No. Coins are 100% virtual fun points for fan predictions and school friendly competitions. There are no real money payments or microtransactions. You receive 100 free coins and can claim 50 bonus coins anytime.
          </p>
        </div>

        <div class="card" style="padding:16px;">
          <h4 style="font-size:0.95rem;font-weight:700;color:var(--clr-text);margin-bottom:6px;">
            Q: How does the Playoff Bracket work?
          </h4>
          <p style="font-size:0.84rem;color:var(--clr-text-muted);line-height:1.45;">
            After group matches finish, top players from Pool A and Pool B are seeded into the knockout bracket (Quarter-Finals, Semi-Finals, and Grand Final). Tap the winner on each bracket match card to automatically advance them to the next round until the Champion is crowned!
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════
       8. MATCH SCORECARDS & OFFICIAL DOSSIERS SCREEN
  ═══════════════════════════════════════════════════ -->
  <section id="scorecardsScreen" class="screen">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:20px;flex-wrap:wrap;gap:12px;">
      <div>
        <h2 style="font-family:var(--font-display);font-size:1.6rem;text-transform:uppercase;"><svg class="icon icon-md" viewBox="0 0 24 24"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/></svg> Signable BWF Match Scorecards</h2>
        <p style="color:var(--clr-text-muted);font-size:0.85rem;">Official printable match sheets with umpire signature blocks and rally records.</p>
      </div>
      <div style="display:flex;gap:8px;">
        <button class="btn btn-ghost btn-sm" onclick="showScreen('groupsScreen')">&larr; Back to Groups</button>
      </div>
    </div>

    <div id="scorecardsGalleryContainer" style="display:grid;grid-template-columns:repeat(auto-fill, minmax(min(100%, 320px), 1fr));gap:16px;"></div>
  </section>

  <!-- ═══════════════════════════════════════════════════
       6. KNOCKOUT BRACKET SCREEN
  ═══════════════════════════════════════════════════ -->
  <section id="knockoutScreen" class="screen">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:20px;flex-wrap:wrap;gap:12px;">
      <div>
        <h2 style="font-family:var(--font-display);font-size:1.6rem;text-transform:uppercase;"><svg class="icon icon-md" viewBox="0 0 24 24"><line x1="6" y1="3" x2="6" y2="15"/><circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M18 9a9 9 0 0 1-9 9"/></svg> Knockout Elimination Stage</h2>
        <p style="color:var(--clr-text-muted);font-size:0.85rem;">Single elimination tree leading to the Championship Final and Bronze Playoff.</p>
      </div>
      <div style="display:flex;gap:8px;flex-wrap:wrap;">
        <button class="btn btn-ghost btn-sm" onclick="showScreen('groupsScreen')">&larr; Back to Groups</button>
        <button class="btn btn-ghost btn-sm" onclick="window.print()"><svg class="icon icon-xs" viewBox="0 0 24 24"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg> Print Bracket</button>
        <button class="btn btn-ghost btn-sm" onclick="simulateAllKnockout()"><svg class="icon icon-xs" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg> Auto-Resolve Knockouts</button>
      </div>
    </div>

    <div class="card" style="overflow-x:auto;">
      <div class="bracket-container" id="bracketTreeContainer"></div>
    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════
       7. CHAMPION SCREEN
  ═══════════════════════════════════════════════════ -->
  <section id="championScreen" class="screen">
    <div class="card" style="text-align:center;max-width:800px;margin:0 auto;">
      <div style="display:flex;justify-content:center;color:var(--clr-gold);margin-bottom:8px;"><svg class="icon icon-3xl" viewBox="0 0 24 24"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6M18 9h1.5a2.5 2.5 0 0 0 0-5H18M4 22h16M10 14.66V17c0 .55-.45 1-1 1H8c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1h8c.55 0 1-.45 1-1v-1c0-.55-.45-1-1-1h-1c-.55 0-1-.45-1-1v-2.34c3.38-.6 6-3.5 6-6.99V4H4v3.67c0 3.49 2.62 6.39 6 6.99z"/></svg></div>
      <div style="font-size:0.85rem;font-weight:900;color:var(--clr-gold);letter-spacing:0.15em;text-transform:uppercase;">Tournament Champion Crowned</div>
      <h2 id="championNameBanner" style="font-family:var(--font-display);font-size:3rem;text-transform:uppercase;margin:10px 0;color:#fff;">VICTORIOUS ATHLETE</h2>

      <!-- Podium -->
      <div style="display:flex;justify-content:center;align-items:flex-end;gap:16px;margin:32px 0 24px;">
        <!-- Silver (2nd) -->
        <div style="flex:1;max-width:180px;">
          <div style="font-size:0.85rem;font-weight:700;color:var(--clr-silver);">RUNNER-UP</div>
          <div id="podiumSilverName" style="font-weight:800;font-size:0.95rem;margin:6px 0;">Runner-Up</div>
          <div style="background:linear-gradient(to top, rgba(148,163,184,0.3), rgba(148,163,184,0.1));height:100px;border-radius:var(--radius-sm);border:1px solid var(--clr-silver);display:flex;align-items:center;justify-content:center;font-weight:900;">2nd</div>
        </div>
        <!-- Gold (1st) -->
        <div style="flex:1;max-width:200px;">
          <div style="font-size:1rem;font-weight:800;color:var(--clr-gold);">CHAMPION</div>
          <div id="podiumGoldName" style="font-weight:900;font-size:1.1rem;margin:6px 0;color:var(--clr-gold);">Champion</div>
          <div style="background:linear-gradient(to top, rgba(245,158,11,0.4), rgba(245,158,11,0.15));height:140px;border-radius:var(--radius-sm);border:2px solid var(--clr-gold);display:flex;align-items:center;justify-content:center;font-weight:900;font-size:1.4rem;">1st</div>
        </div>
        <!-- Bronze (3rd) -->
        <div style="flex:1;max-width:180px;">
          <div style="font-size:0.85rem;font-weight:700;color:var(--clr-bronze);">3RD PLACE</div>
          <div id="podiumBronzeName" style="font-weight:800;font-size:0.95rem;margin:6px 0;">3rd Place</div>
          <div style="background:linear-gradient(to top, rgba(205,127,50,0.3), rgba(205,127,50,0.1));height:80px;border-radius:var(--radius-sm);border:1px solid var(--clr-bronze);display:flex;align-items:center;justify-content:center;font-weight:900;">3rd</div>
        </div>
      </div>

      <div style="display:flex;justify-content:center;gap:12px;margin-top:20px;flex-wrap:wrap;">
        <button class="btn btn-gold btn-lg" onclick="openSharePosterModal()"><svg class="icon icon-xs" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg> Generate Victory Poster</button>
        <button class="btn btn-ghost" onclick="showScreen('leaderboardScreen')">View Global Leaderboard</button>
        <button class="btn btn-ghost" onclick="handleSetupNav()">Start New Cup</button>
      </div>
    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════
       8. GLOBAL LEADERBOARD & HALL OF FAME
  ═══════════════════════════════════════════════════ -->
  <section id="leaderboardScreen" class="screen">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:20px;flex-wrap:wrap;gap:12px;">
      <div>
        <h2 style="font-family:var(--font-display);font-size:1.25rem;font-weight:700;"><svg class="icon icon-md" viewBox="0 0 24 24"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6M18 9h1.5a2.5 2.5 0 0 0 0-5H18M4 22h16M10 14.66V17c0 .55-.45 1-1 1H8c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1h8c.55 0 1-.45 1-1v-1c0-.55-.45-1-1-1h-1c-.55 0-1-.45-1-1v-2.34c3.38-.6 6-3.5 6-6.99V4H4v3.67c0 3.49 2.62 6.39 6 6.99z"/></svg> Global Hall of Fame & Rankings</h2>
        <p style="color:var(--clr-text-muted);font-size:0.85rem;">All-time match records, medals, win percentages, Elo ratings, and point differentials.</p>
      </div>
      <div style="display:flex;gap:8px;">
        <button class="btn btn-ghost btn-sm" onclick="showScreen('groupsScreen')">&larr; Back to Tournament</button>
        <button class="btn btn-primary btn-sm" onclick="exportStandingsCSV()"><svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg> Export CSV</button>
      </div>
    <!-- Special Awards & Records -->
    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(min(100%, 260px), 1fr));gap:14px;margin-bottom:20px;">
      <div class="card" style="display:flex;align-items:center;gap:14px;padding:14px;border-left:3px solid var(--clr-gold);">
        <div style="color:var(--clr-gold);flex-shrink:0;">
          <svg class="icon icon-2xl" viewBox="0 0 24 24"><path d="M12 2l3 7h-6l3-7zM7 9l-4 8 7 5 3-4-6-9zM17 9l4 8-7 5-3-4 6-9z"/></svg>
        </div>
        <div>
          <div style="font-size:0.72rem;font-weight:700;color:var(--clr-gold);text-transform:uppercase;letter-spacing:0.04em;">Golden Racket (Top Attack)</div>
          <div id="goldenRacketLeader" style="font-size:1.05rem;font-weight:800;color:var(--clr-text);">Leader: None</div>
          <div id="goldenRacketStats" style="font-size:0.75rem;color:var(--clr-text-muted);">0 smash points scored</div>
        </div>
      </div>
      <div class="card" style="display:flex;align-items:center;gap:14px;padding:14px;border-left:3px solid var(--clr-green);">
        <div style="color:var(--clr-green);flex-shrink:0;">
          <svg class="icon icon-2xl" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        </div>
        <div>
          <div style="font-size:0.72rem;font-weight:700;color:var(--clr-green);text-transform:uppercase;letter-spacing:0.04em;">Iron Net (Best Defense)</div>
          <div id="goldenGloveLeader" style="font-size:1.05rem;font-weight:800;color:var(--clr-text);">Leader: None</div>
          <div id="goldenGloveStats" style="font-size:0.75rem;color:var(--clr-text-muted);">0.0 points conceded / match</div>
        </div>
      </div>
    </div>

    </div>

    <div class="card">
      <div class="data-table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Rank</th>
              <th>Player / Pair</th>
              <th>Rating / Elo</th>
              <th>Gold</th>
              <th>Silver</th>
              <th>Bronze</th>
              <th>Matches</th>
              <th>Won</th>
              <th>Lost</th>
              <th>Win %</th>
              <th>Pts Diff</th>
              <th>Head-to-Head</th>
            </tr>
          </thead>
          <tbody id="globalLeaderboardTableBody"></tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════
       9. PERSONALIZED PLAYER HUB (ITEM 13)
  ═══════════════════════════════════════════════════ -->
  <section id="playerHubScreen" class="screen">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:20px;flex-wrap:wrap;gap:12px;">
      <div>
        <h2 style="font-family:var(--font-display);font-size:1.25rem;font-weight:700;"><svg class="icon icon-md" viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg> Athlete Personal Tournament Hub</h2>
        <p id="playerHubSubtitle" style="color:var(--clr-text-muted);font-size:0.85rem;">Personal upcoming fixtures, assigned courts, rating, and match history.</p>
      </div>
      <div style="display:flex;gap:8px;">
        <button class="btn btn-ghost btn-sm" onclick="showScreen('groupsScreen')">&larr; Back to Tournament</button>
        <button class="btn btn-primary btn-sm" onclick="openProfileSettingsModal()">Edit My Profile</button>
      </div>
    </div>

    <!-- Next Fixture Callout Card -->
    <div id="playerNextFixtureCard" class="card" style="background:linear-gradient(135deg, rgba(34,197,94,0.15), rgba(13,31,45,0.8));border-color:var(--clr-green);margin-bottom:24px;"></div>

    <!-- Career Dossier Stats -->
    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(min(100%, 200px), 1fr));gap:16px;margin-bottom:24px;">
      <div class="card" style="padding:16px;text-align:center;">
        <div style="font-size:0.75rem;color:var(--clr-text-muted);font-weight:700;">PLAYER SKILL RATING</div>
        <div id="playerHubElo" style="font-family:var(--font-display);font-size:2.2rem;color:var(--clr-gold);">1200</div>
        <div style="font-size:0.75rem;color:var(--clr-text-muted);">BWF SaaS Elo</div>
      </div>
      <div class="card" style="padding:16px;text-align:center;">
        <div style="font-size:0.75rem;color:var(--clr-text-muted);font-weight:700;">WIN PERCENTAGE</div>
        <div id="playerHubWinRate" style="font-family:var(--font-display);font-size:2.2rem;color:var(--clr-green);">0%</div>
        <div id="playerHubMatchesCount" style="font-size:0.75rem;color:var(--clr-text-muted);">0 matches played</div>
      </div>
      <div class="card" style="padding:16px;text-align:center;">
        <div style="font-size:0.75rem;color:var(--clr-text-muted);font-weight:700;">MEDALS WON</div>
        <div id="playerHubMedals" style="font-size:0.95rem;font-weight:600;margin:6px 0;color:var(--clr-text-muted);">Gold: 0 · Silver: 0 · Bronze: 0</div>
        <div style="font-size:0.75rem;color:var(--clr-text-muted);">Tournament Podiums</div>
      </div>
      <div class="card" style="padding:16px;text-align:center;">
        <div style="font-size:0.75rem;color:var(--clr-text-muted);font-weight:700;">FORM GUIDE</div>
        <div id="playerHubFormGuide" style="font-weight:900;font-size:1.2rem;margin:8px 0;letter-spacing:0.1em;">—</div>
        <div style="font-size:0.75rem;color:var(--clr-text-muted);">Last 5 Matches</div>
      </div>
    </div>

    <!-- Personal Matches History -->
    <div class="card">
      <h3 class="card-title" style="margin-bottom:14px;">My Tournament Encounters</h3>
      <div class="data-table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Stage</th>
              <th>Opponent</th>
              <th>Score (Sets)</th>
              <th>Result</th>
              <th>Court</th>
            </tr>
          </thead>
          <tbody id="playerHubMatchesTableBody"></tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════
       10. STADIUM ARENA MULTI-COURT TV (ITEM 28)
  ═══════════════════════════════════════════════════ -->
  <section id="stadiumScreen" class="screen">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:20px;flex-wrap:wrap;gap:12px;">
      <div style="display:flex;align-items:center;gap:10px;">
        <button class="btn btn-ghost btn-xs" onclick="showScreen('groupsScreen')">&larr; Back to Groups</button>
        <h2 style="font-family:var(--font-display);font-size:1.8rem;text-transform:uppercase;"><svg class="icon icon-md" viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="15" rx="2" ry="2"/><polyline points="17 2 12 7 7 2"/></svg> Arena Stadium Multi-Court TV Display</h2>
      </div>
      <div style="display:flex;align-items:center;gap:10px;">
        <span class="status-badge-live badge-game-point"><span style="display:inline-block;width:6px;height:6px;border-radius:50%;background:currentColor;"></span> LIVE BROADCAST</span>
        <button class="btn btn-ghost btn-sm" onclick="toggleFullScreen()"><svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/></svg> Fullscreen</button>
      </div>
    </div>

    <!-- Multi-Court Grid Container -->
    <div class="stadium-grid" id="stadiumCourtsContainer"></div>
  </section>

  <!-- ═══════════════════════════════════════════════════
       11. ENHANCED ADMIN DASHBOARD SCREEN
  ═══════════════════════════════════════════════════ -->
  <section id="adminDashboardScreen" class="screen">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:20px;flex-wrap:wrap;gap:12px;">
      <div>
        <h2 style="font-family:var(--font-display);font-size:1.25rem;font-weight:700;"><svg class="icon icon-md" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg> Commercial Tournament Director & Admin Suite</h2>
        <p style="color:var(--clr-text-muted);font-size:0.85rem;">Athlete invitation dispatch, court dispatcher, score overrides, and financial fee auditing.</p>
      </div>
      <div style="display:flex;gap:8px;flex-wrap:wrap;">
        <button class="btn btn-ghost btn-sm" onclick="showScreen('groupsScreen')">&larr; Back to Tournament</button>
        <button class="btn btn-gold btn-sm" onclick="openInviteUserModal()"><svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg> Invite New User</button>
        <button class="btn btn-ghost btn-sm" onclick="downloadTournamentBackupJSON()"><svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"/><polyline points="17 21 17 13 7 13 7 21"/><polyline points="7 3 7 8 15 8"/></svg> Backup JSON</button>
        <button class="btn btn-ghost btn-sm" onclick="triggerRestoreBackupJSON()"><svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg> Restore JSON</button>
        <input type="file" id="restoreBackupInput" style="display:none;" accept=".json" onchange="handleRestoreBackupFile(event)">
      </div>
    </div>

    <!-- Dynamic Court Queue & Dispatcher Panel (Item 21) -->
    <div class="card" style="margin-bottom:24px;background:rgba(0,0,0,0.3);border-color:rgba(34,197,94,0.3);">
      <div class="card-header">
        <h3 class="card-title"><svg class="icon icon-md" viewBox="0 0 24 24"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/></svg> Automated Court Queue & Athlete Dispatcher</h3>
        <span style="font-size:0.8rem;color:var(--clr-text-muted);">Real-time court occupation & call-to-court audio dispatch</span>
      </div>
      <div id="adminCourtQueueGrid" style="display:grid;grid-template-columns:repeat(auto-fit, minmax(min(100%, 260px), 1fr));gap:14px;"></div>
    </div>

    <!-- Financial Fees & Payment Tracker (Item 26) -->
    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(min(100%, 220px), 1fr));gap:16px;margin-bottom:24px;">
      <div class="card" style="padding:16px;">
        <div style="font-size:0.75rem;color:var(--clr-text-muted);font-weight:700;">TOTAL ATHLETES</div>
        <div id="adminTotalAthletes" style="font-family:var(--font-display);font-size:2rem;color:#60a5fa;">0</div>
        <div style="font-size:0.75rem;color:var(--clr-text-muted);">Registered & Invited</div>
      </div>
      <div class="card" style="padding:16px;">
        <div style="font-size:0.75rem;color:var(--clr-text-muted);font-weight:700;">ACTIVE VERIFIED</div>
        <div id="adminActiveAthletes" style="font-family:var(--font-display);font-size:2rem;color:var(--clr-green);">0</div>
        <div style="font-size:0.75rem;color:var(--clr-text-muted);">Accepted Invitations</div>
      </div>
      <div class="card" style="padding:16px;">
        <div style="font-size:0.75rem;color:var(--clr-text-muted);font-weight:700;">PENDING INVITATIONS</div>
        <div id="adminPendingInvites" style="font-family:var(--font-display);font-size:2rem;color:var(--clr-gold);">0</div>
        <div style="font-size:0.75rem;color:var(--clr-text-muted);">Awaiting Acceptance</div>
      </div>
      <div class="card" style="padding:16px;">
        <div style="font-size:0.75rem;color:var(--clr-text-muted);font-weight:700;">COMPLETED MATCHES</div>
        <div id="adminFeesCollected" style="font-family:var(--font-display);font-size:2rem;color:#fde047;">0</div>
        <div style="font-size:0.75rem;color:var(--clr-text-muted);">Matches Concluded</div>
      </div>
    </div>

    <!-- User & Athlete Directory with Invitation Engine (Items 1–10) -->
    <div class="card" style="margin-bottom:24px;">
      <div class="card-header">
        <div>
          <h3 class="card-title"><svg class="icon icon-md" viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg> Registered Users & Email Invitation Directory</h3>
          <p style="font-size:0.8rem;color:var(--clr-text-muted);margin-top:2px;">Manage players, umpires, invitations, seeded tiers, and roles.</p>
        </div>
        <div style="display:flex;gap:8px;flex-wrap:wrap;">
          <button class="btn btn-gold btn-xs" onclick="openInviteUserModal()">+ Invite User</button>
          <button class="btn btn-ghost btn-xs" onclick="openBulkInviteModal()">Bulk Invite CSV</button>
        </div>
      </div>

      <div class="data-table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Athlete / Name</th>
              <th>Email Address</th>
              <th>Role</th>
              <th>Status</th>
              <th>Seeding Tier</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody id="adminUsersTableBody"></tbody>
        </table>
      </div>
    </div>

    <!-- Live Matches Management Table -->
    <div class="card" style="margin-bottom:24px;">
      <div class="card-header">
        <h3 class="card-title">Live Match Score Oversight</h3>
        <button class="btn btn-primary btn-xs" onclick="openScoreOverrideModal()">Manual Score Override</button>
      </div>
      <div class="data-table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Match ID</th>
              <th>Stage</th>
              <th>Team A</th>
              <th>Team B</th>
              <th>Score (Sets)</th>
              <th>Duration</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody id="adminMatchesTableBody"></tbody>
        </table>
      </div>
    </div>

    <!-- Crowdsourced Score Suggestions Review Queue (Item 29) -->
    <div class="card" style="margin-bottom:24px;">
      <h3 class="card-title" style="margin-bottom:12px;"><svg class="icon icon-md" viewBox="0 0 24 24"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg> Crowdsourced Score & Dispute Review Queue</h3>
      <div class="data-table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Match</th>
              <th>Suggested Score</th>
              <th>Winner</th>
              <th>Submitted By</th>
              <th>Time</th>
              <th>Review Actions</th>
            </tr>
          </thead>
          <tbody id="adminSuggestionsTableBody">
            <tr><td colspan="6" style="text-align:center;padding:16px;color:var(--clr-text-muted);">No pending score suggestions.</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Admin Audit Log (Item 35) -->
    <div class="card">
      <h3 class="card-title" style="margin-bottom:12px;"><svg class="icon icon-md" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg> Administrative Audit Log</h3>
      <div id="adminAuditLogContainer" style="max-height:160px;overflow-y:auto;font-size:0.8rem;color:var(--clr-text-muted);display:flex;flex-direction:column;gap:6px;">
        <div>No administrative operations logged yet.</div>
      </div>
    </div>
  </section>

  <!-- OBS Streaming Lower-Third Overlay (Item 38) -->
  <section id="obsOverlayContainer" style="display:none;">
    <div class="obs-lower-third" id="obsLowerThirdContent">
      <div style="display:flex;align-items:center;color:var(--clr-green);"><svg class="icon icon-xl" viewBox="0 0 24 24"><path d="M12 2l3 7h-6l3-7zM7 9l-4 8 7 5 3-4-6-9zM17 9l4 8-7 5-3-4 6-9z"/></svg></div>
      <div>
        <div id="obsTournamentTitle" style="font-size:0.75rem;color:var(--clr-gold);text-transform:uppercase;font-weight:900;letter-spacing:1px;">The Badminton Cup 2026</div>
        <div style="display:flex;align-items:center;gap:12px;margin-top:2px;">
          <span id="obsPlayerA" style="font-weight:900;font-size:1.15rem;color:#ffffff;">Player A</span>
          <span id="obsScoreA" style="font-size:1.35rem;font-weight:900;color:var(--clr-gold);min-width:24px;text-align:center;">0</span>
          <span style="color:var(--clr-text-muted);font-weight:bold;">VS</span>
          <span id="obsScoreB" style="font-size:1.35rem;font-weight:900;color:var(--clr-gold);min-width:24px;text-align:center;">0</span>
          <span id="obsPlayerB" style="font-weight:900;font-size:1.15rem;color:#ffffff;">Player B</span>
        </div>
      </div>
      <div style="border-left:1px solid rgba(255,255,255,0.2);padding-left:14px;text-align:center;">
        <div id="obsCourtLabel" style="font-size:0.7rem;color:var(--clr-text-muted);font-weight:700;">COURT 1</div>
        <div id="obsSetLabel" style="font-size:0.85rem;color:var(--clr-green);font-weight:900;">SET 1</div>
      </div>
    </div>
  </section>


  <!-- ═══════════════════════════════════════════════════
       SCREEN 12: OPEN CHALLENGES BOARD (FOOSBALL STYLE)
  ═══════════════════════════════════════════════════ -->
  <section id="challengesScreen" class="screen">
    <div class="card" style="margin-bottom:20px;">
      <div class="card-header">
        <div>
          <h2 class="card-title"><svg class="icon icon-md" viewBox="0 0 24 24"><path d="M14.5 17.5 3 6 3 3 6 3 17.5 14.5"/><line x1="13" y1="19" x2="19" y2="13"/><line x1="16" y1="16" x2="20" y2="20"/><line x1="19" y1="21" x2="21" y2="19"/></svg> <span data-i18n="chalScreenTitle">School & Club Open Challenge Board</span></h2>
          <p style="color:var(--clr-text-muted);font-size:0.83rem;margin-top:4px;" data-i18n="chalScreenSub">Anyone can open a challenge here! Other students or players can accept and jump straight into the match.</p>
        </div>
        <div style="display:flex;gap:8px;">
          <button class="btn btn-primary btn-sm" onclick="openNewChallengeModal()"><svg class="icon icon-xs" viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg> <span data-i18n="createChalBtn">+ Open a Challenge</span></button>
        </div>
      </div>

      <!-- Filter tabs -->
      <div style="display:flex;gap:6px;margin-bottom:14px;border-bottom:1px solid var(--clr-border);padding-bottom:10px;">
        <button class="btn btn-ghost btn-xs active" id="chalFilterAll" onclick="filterChallenges('all')">All Challenges (<span id="chalCountAll">0</span>)</button>
        <button class="btn btn-ghost btn-xs" id="chalFilterOpen" onclick="filterChallenges('open')">Open / Waiting (<span id="chalCountOpen">0</span>)</button>
        <button class="btn btn-ghost btn-xs" id="chalFilterAccepted" onclick="filterChallenges('accepted')">Accepted / In Progress (<span id="chalCountAccepted">0</span>)</button>
      </div>

      <div class="challenge-grid" id="challengeBoardList"></div>
    </div>
  </section>

</main>
<!-- Mobile Bottom Navigation Bar (100% Mobile Responsive) -->
<nav class="mobile-bottom-nav" id="mobileBottomNav" aria-label="Mobile Navigation">
  <div class="mobile-bottom-nav-inner">
    <button class="mobile-nav-btn active" id="mobNavMatches" onclick="showScreen('groupsScreen')">
      <svg class="icon" viewBox="0 0 24 24"><path d="M12 2l3 7h-6l3-7zM7 9l-4 8 7 5 3-4-6-9zM17 9l4 8-7 5-3-4 6-9z"/></svg>
      <span data-i18n="navMatches">Matches</span>
    </button>
    <button class="mobile-nav-btn" id="mobNavChallenges" onclick="showScreen('challengesScreen')">
      <svg class="icon" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
      <span data-i18n="navChallenges">Challenges</span>
    </button>
    <button class="mobile-nav-btn" id="mobNavKnockout" onclick="showScreen('knockoutScreen')">
      <svg class="icon" viewBox="0 0 24 24"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6M18 9h1.5a2.5 2.5 0 0 0 0-5H18M4 22h16M10 14.66V17c0 .55-.45 1-1 1H8c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1h8c.55 0 1-.45 1-1v-1c0-.55-.45-1-1-1h-1c-.55 0-1-.45-1-1v-2.34c3.38-.6 6-3.5 6-6.99V4H4v3.67c0 3.49 2.62 6.39 6 6.99z"/></svg>
      <span data-i18n="navBracket">Bracket</span>
    </button>
    <button class="mobile-nav-btn" id="mobNavLeaderboard" onclick="showScreen('leaderboardScreen')">
      <svg class="icon" viewBox="0 0 24 24"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>
      <span data-i18n="navRanking">Ranking</span>
    </button>
    <button class="mobile-nav-btn" id="mobNavMore" onclick="openMoreMenu()">
      <svg class="icon" viewBox="0 0 24 24"><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/><circle cx="5" cy="12" r="1"/></svg>
      <span data-i18n="navMore">More</span>
    </button>
  </div>
</nav>

"""
