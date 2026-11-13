# Dialogs module for Badminton Cup
DIALOGS_CONTENT = """
<!-- ═══════════════════════════════════════════════════
     DIALOGS & MODALS
═══════════════════════════════════════════════════ -->

<!-- 1. Authentication Modal -->
<dialog id="authModal" closedby="any" aria-labelledby="authModalHeading">
  <div class="modal-card">
    <h2 id="authModalHeading" style="font-size:1.4rem;font-weight:900;margin-bottom:6px;">Player Account</h2>
    <p style="color:var(--clr-text-muted);font-size:0.85rem;margin-bottom:20px;">Sign in to access your personal tournament hub, wagers, and medals.</p>
    
    <div style="display:flex;justify-content:center;gap:8px;margin-bottom:18px;">
      <button class="btn btn-xs btn-ghost active" id="tabAuthLogin" onclick="switchAuthTab('login')">Log In</button>
      <button class="btn btn-xs btn-ghost" id="tabAuthRegister" onclick="switchAuthTab('register')">Register</button>
    </div>

    <form method="dialog" id="authForm" onsubmit="handleAuthSubmit(event)">
      <div class="modal-form-item">
        <label for="authUsernameInput">Player / Team Name or Email</label>
        <input type="text" id="authUsernameInput" class="modal-input" placeholder="e.g. Lin Dan or player@example.com" required autofocus>
      </div>
      <div class="modal-form-item">
        <label for="authPasswordInput">Passcode (PIN or Password)</label>
        <input type="password" id="authPasswordInput" class="modal-input" placeholder="••••••••" required>
      </div>

      <div style="display:flex;justify-content:space-between;margin-top:20px;">
        <button type="button" class="btn btn-ghost btn-sm" onclick="closeAuthModal()">Cancel</button>
        <button type="submit" class="btn btn-primary btn-sm" id="authSubmitBtn">Sign In</button>
      </div>
    </form>
    <!-- 1-Click User Switcher -->
    <div style="margin-top:20px;padding-top:14px;border-top:1px solid var(--clr-border);">
      <div style="font-size:0.75rem;font-weight:700;color:var(--clr-text-muted);text-transform:uppercase;letter-spacing:0.04em;margin-bottom:8px;">
        1-Click Quick Sign In
      </div>
      <div style="margin-bottom:8px;">
        <button type="button" class="btn btn-primary btn-xs" onclick="loginAsUser('Rashed')" style="width:100%;font-weight:800;background:var(--clr-gold);color:#000;border-color:var(--clr-gold);">
          👑 Sign in as Rashed (Tournament Admin)
        </button>
      </div>
      <div id="quickLoginUsersSection" style="display:none;">
        <div style="font-size:0.72rem;color:var(--clr-text-muted);margin-bottom:6px;">Or sign in as registered athlete:</div>
        <div id="quickLoginUsersList" style="display:flex;flex-wrap:wrap;gap:4px;max-height:110px;overflow-y:auto;"></div>
      </div>
    </div>

  </div>
</dialog>

<!-- 2. Admin Invite User Modal (Items 1, 2, 3) -->
<dialog id="inviteUserModal" closedby="any">
  <div class="modal-card">
    <h2 style="font-size:1.35rem;font-weight:900;margin-bottom:6px;"><svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg> Invite New User / Player</h2>
    <p style="color:var(--clr-text-muted);font-size:0.85rem;margin-bottom:16px;">The user will be created and receive an invitation email with an acceptance token.</p>
    
    <form method="dialog" id="inviteUserForm" onsubmit="handleInviteUserSubmit(event)">
      <div class="modal-form-item">
        <label for="inviteFullNameInput">Athlete / User Full Name</label>
        <input type="text" id="inviteFullNameInput" class="modal-input" placeholder="e.g. Viktor Axelsen" required>
      </div>

      <div class="modal-form-item">
        <label for="inviteEmailInput">Email Address (for notifications)</label>
        <input type="email" id="inviteEmailInput" class="modal-input" placeholder="e.g. viktor@badminton.dk" required>
      </div>

      <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:14px;">
        <div>
          <label style="font-size:0.8rem;font-weight:700;color:var(--clr-text-muted);margin-bottom:4px;display:block;">Assigned Role</label>
          <select id="inviteRoleSelect" class="modal-input">
            <option value="player">Player / Athlete</option>
            <option value="umpire">Official Umpire</option>
            <option value="admin">Tournament Director</option>
          </select>
        </div>
        <div>
          <label style="font-size:0.8rem;font-weight:700;color:var(--clr-text-muted);margin-bottom:4px;display:block;">Club / Department</label>
          <input type="text" id="inviteClubInput" class="modal-input" placeholder="e.g. Odense BK">
        </div>
      </div>

      <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:20px;">
        <div>
          <label style="font-size:0.8rem;font-weight:700;color:var(--clr-text-muted);margin-bottom:4px;display:block;">Initial Rating / Elo</label>
          <input type="number" id="inviteEloInput" class="modal-input" value="1200" step="25">
        </div>
        <div>
          <label style="font-size:0.8rem;font-weight:700;color:var(--clr-text-muted);margin-bottom:4px;display:block;">Seeding / Ranking Tier</label>
          <select id="inviteFeeStatusSelect" class="modal-input">
            <option value="seeded">Top Seeded</option>
            <option value="standard">Standard Entry</option>
            <option value="qualifier">Qualifier</option>
          </select>
        </div>
      </div>

      <div style="display:flex;justify-content:space-between;">
        <button type="button" class="btn btn-ghost btn-sm" onclick="document.getElementById('inviteUserModal').close()">Cancel</button>
        <button type="submit" class="btn btn-gold btn-sm">Send Invitation &rarr;</button>
      </div>
    </form>
  </div>
</dialog>

<!-- 3. Invitation Success & Magic Link Modal (Item 3) -->
<dialog id="inviteSuccessModal" closedby="any" style="max-width:600px;">
  <div class="modal-card">
    <div style="display:flex;justify-content:center;color:var(--clr-gold);margin-bottom:8px;"><svg class="icon icon-3xl" viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg></div>
    <h2 style="font-size:1.35rem;font-weight:900;text-align:center;margin-bottom:4px;">Invitation Dispatched!</h2>
    <p style="color:var(--clr-text-muted);font-size:0.85rem;text-align:center;margin-bottom:16px;">
      An invitation record has been created. You can share the magic link directly or use the automated email notification.
    </p>

    <!-- Magic Link Box -->
    <div style="background:rgba(0,0,0,0.3);border:1px solid var(--clr-border);padding:12px;border-radius:var(--radius-sm);margin-bottom:16px;">
      <div style="font-size:0.75rem;color:var(--clr-text-muted);font-weight:bold;margin-bottom:4px;">MAGIC INVITATION LINK</div>
      <div id="magicInviteLinkDisplay" style="font-family:monospace;font-size:0.82rem;word-break:break-all;color:var(--clr-gold);margin-bottom:8px;"></div>
      <div style="display:flex;gap:8px;">
        <button class="btn btn-ghost btn-xs" onclick="copyMagicInviteLink()"><svg class="icon icon-xs" viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy Link</button>
        <a id="mailtoInviteBtn" class="btn btn-ghost btn-xs" target="_blank"><svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg> Open in Email Client</a>
      </div>
    </div>

    <!-- Simulated Email Preview -->
    <div style="background:rgba(255,255,255,0.03);border:1px dashed var(--clr-border);padding:14px;border-radius:var(--radius-sm);margin-bottom:20px;font-size:0.82rem;">
      <div style="font-weight:bold;color:var(--clr-green);margin-bottom:6px;">Simulated Outgoing Email Notification:</div>
      <div id="simulatedEmailSubject" style="font-weight:bold;color:#fff;margin-bottom:4px;"></div>
      <div id="simulatedEmailBody" style="color:var(--clr-text-muted);line-height:1.4;white-space:pre-line;"></div>
    </div>

    <div style="text-align:right;">
      <button class="btn btn-primary btn-sm" onclick="document.getElementById('inviteSuccessModal').close()">Done</button>
    </div>
  </div>
</dialog>

<!-- 4. Accept Invitation Onboarding Modal (Item 4) -->
<dialog id="acceptInviteModal" closedby="any" style="max-width:540px;">
  <div class="modal-card">
    <div style="display:flex;justify-content:center;color:var(--clr-green);margin-bottom:8px;"><svg class="icon icon-3xl" viewBox="0 0 24 24"><path d="M12 2l3 7h-6l3-7zM7 9l-4 8 7 5 3-4-6-9zM17 9l4 8-7 5-3-4 6-9z"/></svg></div>
    <h2 style="font-size:1.4rem;font-weight:900;text-align:center;margin-bottom:4px;">Tournament Invitation</h2>
    <p id="acceptInviteSubtitle" style="color:var(--clr-gold);font-weight:bold;text-align:center;font-size:0.95rem;margin-bottom:16px;">
      You have been invited to compete in The Badminton Cup!
    </p>

    <form method="dialog" id="acceptInviteForm" onsubmit="handleAcceptInviteSubmit(event)">
      <div class="modal-form-item">
        <label for="acceptAthleteName">Your Name</label>
        <input type="text" id="acceptAthleteName" class="modal-input" readonly style="opacity:0.8;">
      </div>

      <div class="modal-form-item">
        <label for="acceptAthleteEmail">Your Email</label>
        <input type="email" id="acceptAthleteEmail" class="modal-input" readonly style="opacity:0.8;">
      </div>

      <div class="modal-form-item">
        <label for="acceptPasswordInput">Create a Personal Passcode / PIN</label>
        <input type="password" id="acceptPasswordInput" class="modal-input" placeholder="••••••••" required>
      </div>

      <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:20px;">
        <div>
          <label style="font-size:0.8rem;font-weight:700;color:var(--clr-text-muted);margin-bottom:4px;display:block;">Dominant Hand</label>
          <select id="acceptHandSelect" class="modal-input">
            <option value="Right-Handed">Right-Handed</option>
            <option value="Left-Handed">Left-Handed</option>
          </select>
        </div>
        <div>
          <label style="font-size:0.8rem;font-weight:700;color:var(--clr-text-muted);margin-bottom:4px;display:block;">Preferred Avatar Icon</label>
          <select id="acceptAvatarSelect" class="modal-input">
            <option value="Racket">Racket</option>
            <option value="Lightning">Lightning</option>
            <option value="Eagle">Eagle</option>
            <option value="Fire">Fire</option>
          </select>
        </div>
      </div>

      <div style="display:flex;justify-content:space-between;">
        <button type="button" class="btn btn-ghost btn-sm" onclick="handleDeclineInvite()">Decline Invitation</button>
        <button type="submit" class="btn btn-primary btn-sm">Accept & Activate Profile &rarr;</button>
      </div>
    </form>
  </div>
</dialog>

<!-- 5. Registered Player Picker Modal (Item 11) -->
<dialog id="playerPickerModal" closedby="any" style="max-width:640px;">
  <div class="modal-card">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
      <h2 style="font-size:1.35rem;font-weight:900;"><svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg> Select Registered Athletes</h2>
      <button class="modal-close" onclick="document.getElementById(\'playerPickerModal\').close()" aria-label="Close Athlete Picker"><svg class="icon icon-xs" viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></button>
    </div>
    <p style="color:var(--clr-text-muted);font-size:0.82rem;margin-bottom:12px;">
      Choose active registered or invited athletes to assign to <strong id="pickerTargetPoolLabel">Pool A</strong>.
    </p>

    <input type="text" id="playerPickerSearch" class="modal-input" placeholder="Search by name, email, or club..." oninput="filterPlayerPickerList(this.value)" style="margin-bottom:12px;">

    <div class="player-picker-list" id="playerPickerListContainer"></div>

    <div style="display:flex;justify-content:space-between;align-items:center;margin-top:16px;">
      <span style="font-size:0.8rem;color:var(--clr-text-muted);" id="pickerSelectedCount">0 selected</span>
      <div style="display:flex;gap:8px;">
        <button class="btn btn-ghost btn-sm" onclick="document.getElementById('playerPickerModal').close()">Cancel</button>
        <button class="btn btn-primary btn-sm" onclick="confirmPlayerPickerSelection()">Add to Pool &rarr;</button>
      </div>
    </div>
  </div>
</dialog>

<!-- 6. Bulk Invite CSV Modal (Item 6) -->
<dialog id="bulkInviteModal" closedby="any">
  <div class="modal-card">
    <h2 style="font-size:1.35rem;font-weight:900;margin-bottom:8px;"><svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/></svg> Bulk CSV User Invitations</h2>
    <p style="color:var(--clr-text-muted);font-size:0.85rem;margin-bottom:12px;">
      Paste lines in format: <code>Full Name, Email, Role, Club</code>
    </p>
    <textarea id="bulkInviteCsvTextarea" class="modal-input" rows="8" placeholder="Lin Dan, lindan@china.cn, player, Beijing Club&#10;Lee Chong Wei, lcw@malaysia.my, player, KL Club&#10;Official John, umpire@bwf.org, umpire, BWF"></textarea>
    
    <div style="display:flex;justify-content:space-between;margin-top:16px;">
      <button class="btn btn-ghost btn-sm" onclick="document.getElementById('bulkInviteModal').close()">Cancel</button>
      <button class="btn btn-gold btn-sm" onclick="processBulkInviteCsv()">Dispatch Batch Invitations</button>
    </div>
  </div>
</dialog>

<!-- 7. Official BWF Printable Scorecard Modal (Item 23) -->
<dialog id="scorecardModal" closedby="any" style="max-width:760px;">
  <div class="modal-card">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
      <h2 style="font-size:1.35rem;font-weight:900;"><svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/></svg> Official BWF Match Scorecard</h2>
      <div style="display:flex;gap:6px;">
        <button class="btn btn-primary btn-xs" onclick="window.print()"><svg class="icon icon-xs" viewBox="0 0 24 24"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg> Print Sheet</button>
        <button class="modal-close" onclick="document.getElementById(\'scorecardModal\').close()" aria-label="Close Scorecard"><svg class="icon icon-xs" viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></button>
      </div>
    </div>
    
    <div id="scorecardPrintContainer" class="scorecard-sheet"></div>
  </div>
</dialog>

<!-- 8. Manual Score Override Modal (Admin) -->
<dialog id="scoreOverrideModal" closedby="any">
  <div class="modal-card">
    <h2 style="font-size:1.4rem;font-weight:900;margin-bottom:6px;">Manual Match Score Override</h2>
    <p style="color:var(--clr-text-muted);font-size:0.85rem;margin-bottom:16px;">Correct an official score, overturn a call, or mark a forfeit.</p>
    
    <div class="modal-form-item">
      <label for="overrideMatchSelect">Select Fixture</label>
      <select id="overrideMatchSelect" class="modal-input"></select>
    </div>
    <div class="modal-form-item">
      <label for="overrideSetsInput">Sets Score (comma separated, e.g. 21-18, 19-21, 21-14)</label>
      <input type="text" id="overrideSetsInput" class="modal-input" placeholder="21-18, 21-15">
    </div>
    <div class="modal-form-item">
      <label for="overrideWinnerSelect">Winner</label>
      <select id="overrideWinnerSelect" class="modal-input">
        <option value="a">Side A Wins</option>
        <option value="b">Side B Wins</option>
      </select>
    </div>

    <div style="display:flex;justify-content:space-between;margin-top:20px;">
      <button class="btn btn-ghost btn-sm" onclick="document.getElementById('scoreOverrideModal').close()">Cancel</button>
      <button class="btn btn-primary btn-sm" onclick="saveManualScoreOverride()">Save Override</button>
    </div>
  </div>
</dialog>

<!-- 9. Coin Toss Modal -->
<dialog id="coinTossModal" closedby="any">
  <div class="modal-card" style="text-align:center;">
    <h2 style="font-size:1.4rem;font-weight:900;margin-bottom:8px;"><svg class="icon icon-sm" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/></svg> BWF Official Coin Toss</h2>
    <p style="color:var(--clr-text-muted);font-size:0.85rem;margin-bottom:20px;">Decides initial serve or court end preference before match start.</p>
    
    <div id="coinGraphic" style="display:flex;justify-content:center;color:var(--clr-gold);margin:16px auto;user-select:none;transition:transform 600ms cubic-bezier(0.175, 0.885, 0.32, 1.275);"><svg class="icon icon-3xl" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/></svg></div>
    <div id="coinTossPlayersBar" style="display:flex;justify-content:center;gap:10px;margin-bottom:14px;">
      <button type="button" id="coinPlayerABtn" class="btn btn-outline btn-sm" onclick="selectCoinPlayer('a')">Player A</button>
      <button type="button" id="coinPlayerBBtn" class="btn btn-outline btn-sm" onclick="selectCoinPlayer('b')">Player B</button>
    </div>

    <div id="coinResultText" style="font-size:1.2rem;font-weight:900;color:var(--clr-gold);margin-bottom:20px;">Tap Flip to Begin</div>

    <div style="display:flex;flex-direction:column;align-items:center;gap:10px;">
      <div style="display:flex;justify-content:center;gap:12px;">
        <button class="btn btn-primary btn-lg" onclick="flipCoin()">Flip Coin</button>
        <button class="btn btn-ghost btn-lg" onclick="document.getElementById('coinTossModal').close()">Close</button>
      </div>
      <button id="btnAssignTossServer" class="btn btn-gold btn-sm" style="display:none;margin-top:6px;" onclick="assignTossWinnerServer()">Assign Winner as Initial Server</button>
    </div>
  </div>
</dialog>

<!-- 10. Match Win Modal -->
<dialog id="matchWinModal" closedby="any">
  <div class="modal-card" style="text-align:center;">
    <div style="display:flex;justify-content:center;color:var(--clr-green);margin-bottom:8px;"><svg class="icon icon-3xl" viewBox="0 0 24 24"><path d="M12 2l3 7h-6l3-7zM7 9l-4 8 7 5 3-4-6-9zM17 9l4 8-7 5-3-4 6-9z"/></svg></div>
    <h2 style="font-size:1.6rem;font-weight:900;margin-bottom:4px;">Match Completed!</h2>
    <p id="winSubtitle" style="color:var(--clr-gold);font-size:1.1rem;font-weight:800;margin-bottom:12px;"></p>
    <div id="winScoreSummary" style="font-family:var(--font-display);font-size:2rem;margin-bottom:20px;color:#fff;"></div>
    
    <div style="display:flex;justify-content:center;gap:10px;flex-wrap:wrap;">
      <button class="btn btn-primary" onclick="advanceToNextMatch()">Next Fixture &rarr;</button>
      <button class="btn btn-ghost" onclick="closeWinModal()">Close</button>
    </div>
  </div>
</dialog>

<!-- 11. Victory Poster Modal -->
<dialog id="shareCanvasModal" closedby="any" style="max-width:680px;">
  <div class="modal-card" style="text-align:center;">
    <h2 style="font-size:1.3rem;font-weight:900;margin-bottom:6px;"><svg class="icon icon-sm" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg> Official Tournament Celebration Poster</h2>
    <p style="color:var(--clr-text-muted);font-size:0.82rem;margin-bottom:14px;">High-resolution 1200x1200px graphic suitable for Slack, WhatsApp, and Instagram.</p>
    
    <div style="border-radius:var(--radius-md);overflow:hidden;border:2px solid var(--clr-border);margin-bottom:16px;background:#000;">
      <canvas id="victoryShareCanvas" width="1200" height="1200" style="width:100%;height:auto;display:block;"></canvas>
    </div>

    <div style="display:flex;justify-content:center;gap:10px;flex-wrap:wrap;">
      <button class="btn btn-gold" onclick="downloadVictoryPoster()"><svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg> Download Poster</button>
      <button class="btn btn-primary" onclick="copyVictoryPosterToClipboard()"><svg class="icon icon-xs" viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy to Clipboard</button>
      <button class="btn btn-ghost" onclick="shareVictoryPosterOS()"><svg class="icon icon-xs" viewBox="0 0 24 24"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/></svg> Share Sheet</button>
      <button class="btn btn-ghost" onclick="document.getElementById('shareCanvasModal').close()">Close</button>
    </div>
  </div>
</dialog>

<!-- 12. Crowdsourced Score Suggestion Modal -->
<dialog id="suggestScoreModal" closedby="any">
  <div class="modal-card">
    <h2 style="font-size:1.3rem;font-weight:900;margin-bottom:6px;"><svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg> Suggest Completed Match Score</h2>
    <p style="color:var(--clr-text-muted);font-size:0.85rem;margin-bottom:16px;">Spectators & athletes can submit scores. Admins verify submissions.</p>

    <div class="modal-form-item">
      <label for="suggestMatchSelect">Select Encounter</label>
      <select id="suggestMatchSelect" class="modal-input"></select>
    </div>
    <div class="modal-form-item">
      <label for="suggestSetsInput">Finished Sets Score (e.g. 21-17, 21-19)</label>
      <input type="text" id="suggestSetsInput" class="modal-input" placeholder="21-17, 21-19" required>
    </div>
    <div class="modal-form-item">
      <label for="suggestWinnerSelect">Match Winner</label>
      <select id="suggestWinnerSelect" class="modal-input">
        <option value="a">Player / Team A</option>
        <option value="b">Player / Team B</option>
      </select>
    </div>

    <div style="display:flex;justify-content:space-between;margin-top:20px;">
      <button class="btn btn-ghost btn-sm" onclick="document.getElementById('suggestScoreModal').close()">Cancel</button>
      <button class="btn btn-primary btn-sm" onclick="submitSuggestedScore()">Submit Score</button>
    </div>
  </div>
</dialog>

<!-- 13. Walkover / Penalty Modal (Items 1, 2, 3, 4) -->
<dialog id="walkoverModal" closedby="any">
  <div class="modal-card">
    <h2 id="walkoverModalTitle" style="font-size:1.3rem;font-weight:900;margin-bottom:6px;">Record Match Penalty / Walkover</h2>
    <p id="walkoverModalDesc" style="color:var(--clr-text-muted);font-size:0.85rem;margin-bottom:16px;">Specify which side committed the offense or requested forfeit.</p>
    
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:20px;">
      <button class="btn btn-ghost" id="walkoverSideABtn" style="padding:14px;display:flex;flex-direction:column;gap:4px;" onclick="confirmWalkoverSelection('a')">
        <span style="font-weight:900;font-size:1rem;" id="walkoverNameA">Side A</span>
        <span style="font-size:0.75rem;color:var(--clr-text-muted);" id="walkoverRoleA">Action Side A</span>
      </button>
      <button class="btn btn-ghost" id="walkoverSideBBtn" style="padding:14px;display:flex;flex-direction:column;gap:4px;" onclick="confirmWalkoverSelection('b')">
        <span style="font-weight:900;font-size:1rem;" id="walkoverNameB">Side B</span>
        <span style="font-size:0.75rem;color:var(--clr-text-muted);" id="walkoverRoleB">Action Side B</span>
      </button>
    </div>

    <div style="text-align:right;">
      <button class="btn btn-ghost btn-sm" onclick="document.getElementById('walkoverModal').close()">Cancel</button>
    </div>
  </div>
</dialog>

<!-- 16. Head-to-Head (H2H) Comparison Modal (Item 53) -->
<dialog id="h2hModal" closedby="any" style="max-width:640px;">
  <div class="modal-card">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
      <h2 style="font-size:1.3rem;font-weight:900;"><svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M16 16l3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1zM2 16l3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1zM7 21h10M12 3v18M3 7h18"/></svg> Head-to-Head Encounter History</h2>
      <button class="modal-close" onclick="document.getElementById(\'h2hModal\').close()" aria-label="Close H2H Analytics"><svg class="icon icon-xs" viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></button>
    </div>
    <div id="h2hModalBody"></div>
    <div style="text-align:right;margin-top:16px;">
      <button class="btn btn-ghost btn-sm" onclick="document.getElementById('h2hModal').close()">Close</button>
    </div>
  </div>
</dialog>

<!-- 17. Umpire Audio & Voice Settings Modal (Items 39 & 40) -->
<dialog id="soundSettingsModal" closedby="any">
  <div class="modal-card">
    <h2 style="font-size:1.3rem;font-weight:900;margin-bottom:12px;"><svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/></svg> Umpire Audio & Speech Settings</h2>
    
    <div class="modal-form-item">
      <div style="display:flex;justify-content:space-between;margin-bottom:6px;">
        <label for="masterVolumeRange" style="margin:0;">Sound Effects Volume</label>
        <span id="masterVolumeDisplay" style="font-weight:bold;color:var(--clr-green);">80%</span>
      </div>
      <input type="range" id="masterVolumeRange" min="0" max="100" value="80" oninput="updateMasterVolume(this.value)" style="width:100%;">
    </div>

    <div class="modal-form-item">
      <label for="umpireVoiceSelect">Umpire Speech Voice / Accent</label>
      <select id="umpireVoiceSelect" class="modal-input" onchange="updateUmpireVoice(this.value)"></select>
    </div>

    <div class="modal-form-item">
      <label style="display:flex;align-items:center;gap:8px;cursor:pointer;">
        <input type="checkbox" id="buzzerSoundCheck" checked onchange="toggleBuzzerSound(this.checked)">
        <span>Play dual 600Hz buzzer on interval expiry (60s / 120s)</span>
      </label>
    </div>

    <div style="display:flex;justify-content:space-between;margin-top:20px;">
      <button class="btn btn-ghost btn-sm" onclick="testUmpireVoice()"><svg class="icon icon-xs" viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg> Test Voice</button>
      <button class="btn btn-primary btn-sm" onclick="document.getElementById('soundSettingsModal').close()">Save & Close</button>
    </div>
  </div>
</dialog>

<!-- 18. Bulk Roster Import / Export Modal (Item 34) -->
<dialog id="bulkRosterModal" closedby="any">
  <div class="modal-card">
    <h2 style="font-size:1.3rem;font-weight:900;margin-bottom:8px;"><svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/></svg> Bulk Roster Import / Export</h2>
    <p style="color:var(--clr-text-muted);font-size:0.85rem;margin-bottom:12px;">Paste names (one per line or comma-separated). They will be split into Pool A & Pool B.</p>
    
    <textarea id="bulkRosterTextarea" class="modal-input" rows="8" placeholder="Lin Dan&#10;Lee Chong Wei&#10;Viktor Axelsen&#10;Kento Momota"></textarea>

    <div style="display:flex;justify-content:space-between;margin-top:16px;">
      <button class="btn btn-ghost btn-sm" onclick="exportCurrentRosterToBulk()">Copy Current</button>
      <div style="display:flex;gap:8px;">
        <button class="btn btn-ghost btn-sm" onclick="document.getElementById('bulkRosterModal').close()">Cancel</button>
        <button class="btn btn-primary btn-sm" onclick="applyBulkRoster()">Apply Roster</button>
      </div>
    </div>
  </div>
</dialog>

<!-- App Toast Notification -->
<div id="appToast" role="alert" aria-live="polite"></div>


<!-- ═══════════════════════════════════════════════════
   QUICK SCORE & INSTANT WIN MODAL (NO ONE-BY-ONE SCORING)
═══════════════════════════════════════════════════ -->
<dialog id="quickScoreModal" closedby="any" style="max-width:460px;">
  <div class="modal-card">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
      <h2 style="font-size:1.2rem;font-weight:700;"><svg class="icon icon-sm" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg> <span data-i18n="quickScoreTitle">Quick Score & Win</span></h2>
      <button class="modal-close" onclick="document.getElementById(\'quickScoreModal\').close()" aria-label="Close Quick Score"><svg class="icon icon-xs" viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></button>
    </div>
    <p style="color:var(--clr-text-muted);font-size:0.83rem;margin-bottom:16px;" data-i18n="quickScoreDesc">Directly record the final match score or click a player to award an instant win without scoring rally-by-rally.</p>

    <input type="hidden" id="quickMatchId">
    
    <div style="background:rgba(0,0,0,0.25);border:1px solid var(--clr-border);border-radius:var(--radius-sm);padding:14px;margin-bottom:16px;">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
        <button class="btn btn-primary btn-sm" id="quickWinABtn" style="flex:1;margin-right:6px;" onclick="awardInstantWinner('a')">
          <span id="quickTeamAName">Side A</span> <span data-i18n="winsLabel">Wins (2-0)</span>
        </button>
        <button class="btn btn-primary btn-sm" id="quickWinBBtn" style="flex:1;margin-left:6px;" onclick="awardInstantWinner('b')">
          <span id="quickTeamBName">Side B</span> <span data-i18n="winsLabel">Wins (2-0)</span>
        </button>
      </div>

      <div style="margin-bottom:12px;">
        <label style="font-size:0.75rem;color:var(--clr-text-muted);display:block;margin-bottom:4px;">Target Points</label>
        <select id="quickScoreTargetSelect" class="modal-input" style="width:100%;">
          <option value="15" selected>15 Points (13 Hope Ball · 14 Game Ball · 15 Win)</option>
          <option value="21">21 Points (Standard BWF)</option>
          <option value="11">11 Points (Express)</option>
          <option value="30">30 Points (Single Decider)</option>
        </select>
      </div>
      <div style="text-align:center;font-size:0.75rem;color:var(--clr-text-muted);margin-bottom:8px;" data-i18n="orCustomScore">or enter manual final score:</div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
        <div>
          <label style="font-size:0.75rem;color:var(--clr-text-muted);display:block;margin-bottom:4px;" id="quickScoreLabelA">Side A Points</label>
          <input type="number" id="quickScoreInputA" class="modal-input" placeholder="21" value="21" min="0" max="30">
        </div>
        <div>
          <label style="font-size:0.75rem;color:var(--clr-text-muted);display:block;margin-bottom:4px;" id="quickScoreLabelB">Side B Points</label>
          <input type="number" id="quickScoreInputB" class="modal-input" placeholder="15" value="15" min="0" max="30">
        </div>
      </div>
    </div>

    <div style="display:flex;justify-content:space-between;align-items:center;">
      <button class="btn btn-ghost btn-sm" onclick="document.getElementById('quickScoreModal').close()" data-i18n="cancelBtn">Cancel</button>
      <button class="btn btn-primary btn-sm" onclick="saveQuickCustomScore()" data-i18n="saveScoreBtn">Save Final Score &rarr;</button>
    </div>
  </div>
</dialog>

<!-- ═══════════════════════════════════════════════════
   OPEN CHALLENGE MODAL (Anyone Can Challenge & Join)
═══════════════════════════════════════════════════ -->
<dialog id="newChallengeModal" closedby="any" style="max-width:480px;">
  <div class="modal-card">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
      <h2 style="font-size:1.25rem;font-weight:700;"><svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M14.5 17.5 3 6 3 3 6 3 17.5 14.5"/><line x1="13" y1="19" x2="19" y2="13"/><line x1="16" y1="16" x2="20" y2="20"/><line x1="19" y1="21" x2="21" y2="19"/></svg> <span data-i18n="openChallengeTitle">Open a Badminton Challenge</span></h2>
      <button class="modal-close" onclick="document.getElementById(\'newChallengeModal\').close()" aria-label="Close New Challenge"><svg class="icon icon-xs" viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></button>
    </div>
    <p style="color:var(--clr-text-muted);font-size:0.83rem;margin-bottom:16px;" data-i18n="openChallengeDesc">Post a challenge on the public board. Any school student or player can accept your challenge and play!</p>

    <!-- Auto Athlete Profile Identity (No Typing Required) -->
    <div id="challengeCreatorIdentityCard" style="margin-bottom:14px;"></div>
    <input type="hidden" id="challengeCreatorName">

    <div class="modal-form-item">
      <label data-i18n="challengeCategoryLabel">Format</label>
      <select id="challengeCategorySelect" class="modal-input" onchange="document.getElementById('challengePartnerField').style.display = (this.value === 'doubles' ? 'block' : 'none');">
        <option value="singles">Singles (1 vs 1)</option>
        <option value="doubles">Doubles (2 vs 2)</option>
      </select>
    </div>

    <div id="challengePartnerField" class="modal-form-item" style="display:none;">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;">
        <label style="margin:0;">Doubles Partner / Teammate</label>
        <span style="font-size:0.72rem;color:var(--clr-green);font-weight:700;">Optional · Open Partner Slot</span>
      </div>
      <input type="text" id="challengePartnerName" class="modal-input" placeholder="e.g. Sifat (or leave empty so anyone can join as partner)">
      <p style="font-size:0.74rem;color:var(--clr-text-muted);margin-top:4px;">
        💡 If you don't select a partner, an <strong>Open Partner Slot</strong> will be published so any player can join your team on the challenge board.
      </p>
    </div>

    <div class="modal-form-item">
      <label data-i18n="challengePointsLabel">Points Target</label>
      <select id="challengePointsSelect" class="modal-input">
        <option value="15" selected>15 Points (13 Hope Ball · 14 Game Ball · 15 Win)</option>
        <option value="21">21 Points (Standard BWF)</option>
        <option value="11">11 Points (Express Knockout)</option>
      </select>
    </div>

    <div class="modal-form-item">
      <label style="display:flex;justify-content:space-between;align-items:center;">
        <span>Points to Play For (Stake per Player)</span>
        <span style="font-size:0.75rem;color:var(--clr-gold);font-weight:700;">Winner team members get double!</span>
      </label>
      <select id="challengeBuyInSelect" class="modal-input" onchange="toggleCustomChallengePointsInput(this.value)">
        <option value="5" selected>5 Points (Deduct 5 PTS from each player · Winner gets 10 PTS)</option>
        <option value="10">10 Points (Deduct 10 PTS from each player · Winner gets 20 PTS)</option>
        <option value="15">15 Points (Deduct 15 PTS from each player · Winner gets 30 PTS)</option>
        <option value="20">20 Points (Deduct 20 PTS from each player · Winner gets 40 PTS)</option>
        <option value="25">25 Points (Deduct 25 PTS from each player · Winner gets 50 PTS)</option>
        <option value="50">50 Points (Deduct 50 PTS from each player · Winner gets 100 PTS)</option>
        <option value="100">100 Points (Deduct 100 PTS from each player · Winner gets 200 PTS)</option>
        <option value="0">Friendly (0 PTS - Free)</option>
        <option value="custom">Custom Points Amount...</option>
      </select>
    </div>
    <div id="challengeCustomPointsContainer" class="modal-form-item" style="display:none;margin-top:6px;">
      <label style="display:flex;justify-content:space-between;align-items:center;">
        <span>Custom Points per Player</span>
        <span id="challengeCustomDoublePreview" style="font-size:0.75rem;color:var(--clr-gold);font-weight:700;">Winner gets 10 PTS</span>
      </label>
      <input type="number" id="challengeCustomPointsInput" class="modal-input" min="1" max="10000" value="5" oninput="updateCustomDoublePreview(this.value)">
    </div>

    <div class="modal-form-item">
      <label data-i18n="challengeNoteLabel">Note / Venue</label>
      <input type="text" id="challengeNoteInput" class="modal-input" placeholder="e.g. Court 1 / School ground after tiffin">
    </div>

    <div class="modal-form-item" style="margin-top:12px;padding:10px;background:rgba(255,255,255,0.03);border:1px solid var(--clr-border);border-radius:8px;">
      <label style="display:flex;align-items:center;gap:8px;cursor:pointer;margin:0;">
        <input type="checkbox" id="challengePrivateToggle" onchange="document.getElementById('challengePinContainer').style.display = this.checked ? 'block' : 'none';">
        <span style="font-weight:600;font-size:0.83rem;">🔒 Require 4-Digit PIN to Accept (Private)</span>
      </label>
      <div id="challengePinContainer" style="display:none;margin-top:8px;">
        <input type="password" id="challengePinInput" maxlength="4" class="modal-input" placeholder="Set 4-digit PIN (e.g. 1234)" style="width:180px;">
      </div>
    </div>

    <div style="display:flex;justify-content:flex-end;gap:8px;margin-top:20px;">
      <button class="btn btn-ghost btn-sm" onclick="document.getElementById('newChallengeModal').close()" data-i18n="cancelBtn">Cancel</button>
      <button class="btn btn-primary btn-sm" onclick="postNewChallenge()" data-i18n="postChallengeBtn">Post Challenge &rarr;</button>
    </div>
  </div>
</dialog>

<!-- ═══════════════════════════════════════════════════
   FULL DATA RESET & START OVER MODAL (School Simple)
═══════════════════════════════════════════════════ -->
<dialog id="dataResetModal" closedby="any" style="max-width:440px;">
  <div class="modal-card">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
      <h2 style="font-size:1.2rem;font-weight:700;color:#f87171;"><svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg> <span data-i18n="resetDataTitle">Reset Tournament Data</span></h2>
      <button class="modal-close" onclick="document.getElementById(\'dataResetModal\').close()" aria-label="Close Data Reset"><svg class="icon icon-xs" viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></button>
    </div>
    <p style="color:var(--clr-text-muted);font-size:0.83rem;margin-bottom:16px;" data-i18n="resetDataDesc">Choose what to clear. This is very useful when starting a brand new school match or cup from scratch.</p>

    <div style="display:flex;flex-direction:column;gap:10px;margin-bottom:20px;">
      <button class="btn btn-ghost" style="justify-content:flex-start;text-align:left;padding:12px;" onclick="resetCurrentTournamentOnly()">
        <div>
          <div style="font-weight:700;color:var(--clr-text);" data-i18n="resetTourneyTitle">1. Clear Current Tournament Matches Only</div>
          <div style="font-size:0.75rem;color:var(--clr-text-muted);" data-i18n="resetTourneySub">Wipes current match scores and bracket back to setup. Keeps players registered.</div>
        </div>
      </button>

      <button class="btn btn-danger-reset" style="justify-content:flex-start;text-align:left;padding:12px;border-radius:var(--radius-sm);" onclick="resetEverythingFullFactory()">
        <div>
          <div style="font-weight:700;" data-i18n="resetAllTitle">2. Complete Factory Reset (Start Completely Over)</div>
          <div style="font-size:0.75rem;opacity:0.85;" data-i18n="resetAllSub">Wipes all tournament fixtures, challenges, and cumulative leaderboard stats.</div>
        </div>
      </button>
    </div>

    <div style="text-align:right;">
      <button class="btn btn-ghost btn-sm" onclick="document.getElementById('dataResetModal').close()" data-i18n="cancelBtn">Cancel</button>
    </div>
  </div>
</dialog>
<!-- ═══════════════════════════════════════════════════
     MORE MENU MODAL (Streamlined Secondary Tools)
═══════════════════════════════════════════════════ -->
<dialog id="moreMenuModal" class="modal" aria-labelledby="moreMenuTitle" style="max-width:720px;width:92%;">
  <div class="modal-box" style="max-width:720px;max-height:90vh;overflow-y:auto;">
    <div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid var(--clr-border);padding-bottom:12px;margin-bottom:14px;">
      <h3 id="moreMenuTitle" style="font-family:var(--font-display);font-size:1.25rem;display:flex;align-items:center;gap:8px;margin:0;">
        <svg class="icon icon-sm" viewBox="0 0 24 24"><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/><circle cx="5" cy="12" r="1"/></svg>
        <span data-i18n="moreMenuTitle">All Features & Tools</span>
      </h3>
      <button class="modal-close" onclick="document.getElementById('moreMenuModal').close()" aria-label="Close" style="background:transparent!important;border:none!important;color:var(--clr-text-muted);cursor:pointer;padding:0;width:32px;height:32px;display:inline-flex;align-items:center;justify-content:center;border-radius:6px;outline:none;">
        <svg class="icon icon-xs" viewBox="0 0 24 24" style="stroke:currentColor;stroke-width:2.2;"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
    </div>

    <!-- Sound & Atmosphere Settings Strip -->
    <div style="background:rgba(255,255,255,0.03);border:1px solid var(--clr-border);border-radius:var(--radius-sm);padding:8px 14px;margin-bottom:14px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;">
      <div style="display:flex;align-items:center;gap:8px;font-size:0.82rem;color:var(--clr-text-muted);">
        <svg class="icon icon-xs" viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
        <span style="font-weight:600;">Match Atmosphere & Sound Effects:</span>
      </div>
      <button class="btn btn-ghost btn-xs" id="moreMenuSoundBtn" onclick="toggleMuteAudio()" style="display:inline-flex;align-items:center;gap:6px;font-weight:600;">
        <span id="moreMenuSoundLabel">Sound: ON</span>
      </button>
    </div>

    <!-- Active Tournament Quick Selection -->
    <div class="active-tournament-card" style="background:linear-gradient(135deg, rgba(255,255,255,0.04), rgba(255,255,255,0.015));border:1px solid var(--clr-border);border-radius:var(--radius-md);padding:12px 16px;margin-bottom:18px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
      <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;">
        <div style="display:inline-flex;align-items:center;gap:6px;font-size:0.76rem;font-weight:700;color:var(--clr-text-muted);text-transform:uppercase;letter-spacing:0.04em;">
          <svg class="icon icon-xs" viewBox="0 0 24 24" style="color:var(--clr-gold);stroke:currentColor;fill:none;stroke-width:2;"><circle cx="12" cy="8" r="6"/><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"/></svg>
          <span>Active Tournament:</span>
        </div>
        <div style="position:relative;display:inline-flex;align-items:center;">
          <select id="tournamentSelectMore" class="modal-input app-custom-select" style="min-width:220px;padding:7px 38px 7px 12px;font-size:0.86rem;font-weight:600;background-color:rgba(0,0,0,0.3);border-color:var(--clr-border);border-radius:var(--radius-sm);cursor:pointer;" onchange="switchActiveTournament(this.value)">
            <option value="main">The Badminton Cup 2026</option>
          </select>
        </div>
      </div>
      <button class="btn btn-primary btn-xs admin-only-item" onclick="document.getElementById('moreMenuModal').close();handleSetupNav();" style="display:inline-flex;align-items:center;gap:6px;font-weight:600;padding:6px 14px;border-radius:var(--radius-sm);">
        <svg class="icon icon-xs" viewBox="0 0 24 24" style="stroke:currentColor;stroke-width:2.2;"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
        <span>New Tournament</span>
      </button>
    </div>

    <!-- Grid of Features -->
    <div class="more-grid">
      <!-- 1. Tournament Setup -->
      <button class="more-card-item admin-only-item" onclick="document.getElementById('moreMenuModal').close();handleSetupNav();">
        <div class="more-card-icon" style="color:#f87171;">
          <svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M12 2l3 7h-6l3-7zM7 9l-4 8 7 5 3-4-6-9zM17 9l4 8-7 5-3-4 6-9z"/></svg>
        </div>
        <div class="more-card-text" style="flex:1;">
          <span class="more-card-title">Setup & Roster</span>
          <span class="more-card-desc">Configure players, categories & courts</span>
        </div>
      </button>

      <!-- 2. Pool Draw -->
      <button class="more-card-item admin-only-item" onclick="document.getElementById('moreMenuModal').close();handleDraftNav();">
        <div class="more-card-icon" style="color:#f87171;">
          <svg class="icon icon-sm" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M14.31 8l5.74 9.94M9.69 8h11.48M7.38 12l5.74-9.94M9.69 16L3.95 6.06M14.31 16H2.83M16.62 12l-5.74 9.94"/></svg>
        </div>
        <div class="more-card-text" style="flex:1;">
          <span class="more-card-title">Pool Draw</span>
          <span class="more-card-desc">Interactive live group seed machine</span>
        </div>
      </button>

      <!-- 3. Schedule -->
      <button class="more-card-item" onclick="document.getElementById('moreMenuModal').close();showScreen('scheduleScreen');">
        <div class="more-card-icon">
          <svg class="icon icon-sm" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
        </div>
        <div class="more-card-text">
          <span class="more-card-title">Full Schedule</span>
          <span class="more-card-desc">Court time slots and match order</span>
        </div>
      </button>

      <!-- 4. Scorecards -->
      <button class="more-card-item" onclick="document.getElementById('moreMenuModal').close();showScreen('scorecardsScreen');">
        <div class="more-card-icon">
          <svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
        </div>
        <div class="more-card-text">
          <span class="more-card-title">Scorecards</span>
          <span class="more-card-desc">Detailed match scores & exports</span>
        </div>
      </button>

      <!-- 5. Head-to-Head Analytics -->
      <button class="more-card-item" onclick="document.getElementById('moreMenuModal').close();showScreen('analyticsScreen');">
        <div class="more-card-icon">
          <svg class="icon icon-sm" viewBox="0 0 24 24"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
        </div>
        <div class="more-card-text">
          <span class="more-card-title">H2H Analytics</span>
          <span class="more-card-desc">Player stats, win rates & streaks</span>
        </div>
      </button>

      <!-- 6. BWF Rules & Guide -->
      <button class="more-card-item" onclick="document.getElementById('moreMenuModal').close();showScreen('rulesScreen');">
        <div class="more-card-icon">
          <svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
        </div>
        <div class="more-card-text">
          <span class="more-card-title">Complete User Guide & Rules</span>
          <span class="more-card-desc">Step-by-step app guide, betting, challenge rules & BWF laws</span>
        </div>
      </button>

      <!-- 7. Stadium Arena TV -->
      <button class="more-card-item" onclick="document.getElementById('moreMenuModal').close();showScreen('stadiumScreen');">
        <div class="more-card-icon">
          <svg class="icon icon-sm" viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="15" rx="2" ry="2"/><polyline points="17 2 12 7 7 2"/></svg>
        </div>
        <div class="more-card-text">
          <span class="more-card-title">Stadium Arena TV</span>
          <span class="more-card-desc">Multi-court projector / big screen mode</span>
        </div>
      </button>

      <!-- 8. Coin Toss -->
      <button class="more-card-item" onclick="document.getElementById('moreMenuModal').close();openCoinTossModal();">
        <div class="more-card-icon">
          <svg class="icon icon-sm" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/></svg>
        </div>
        <div class="more-card-text">
          <span class="more-card-title">Digital Coin Toss</span>
          <span class="more-card-desc">Flip to decide serve or court side</span>
        </div>
      </button>

      <!-- 9. Push Notifications -->
      <button class="more-card-item" onclick="document.getElementById('moreMenuModal').close();openNotificationModal();">
        <div class="more-card-icon">
          <svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg>
        </div>
        <div class="more-card-text">
          <span class="more-card-title">Push Notifications</span>
          <span class="more-card-desc">Get match finish & challenge alerts</span>
        </div>
      </button>

      <!-- 10. Install App (PWA) -->
      <button class="more-card-item" id="moreInstallBtn" onclick="promptInstallPWA();">
        <div class="more-card-icon">
          <svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
        </div>
        <div class="more-card-text">
          <span class="more-card-title">Install App (PWA)</span>
          <span class="more-card-desc">Add to phone home screen & offline use</span>
        </div>
      </button>

      
      <!-- Role Switcher -->
      <button class="more-card-item admin-only-item" onclick="document.getElementById('moreMenuModal').close();toggleRoleDemo();">
        <div class="more-card-icon" style="color:var(--clr-gold);">
          <svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><line x1="20" y1="8" x2="20" y2="14"/><line x1="23" y1="11" x2="17" y2="11"/></svg>
        </div>
        <div class="more-card-text">
          <span class="more-card-title">Switch Role (Admin / Player)</span>
          <span class="more-card-desc">Toggle Director vs General User permissions</span>
        </div>
      </button>

      <!-- Athlete Profile & Stacks -->
      <button class="more-card-item" onclick="document.getElementById('moreMenuModal').close();if(currentUser){showScreen('playerHubScreen');}else{openAuthModal();}">
        <div class="more-card-icon" style="color:var(--clr-green);">
          <svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
        </div>
        <div class="more-card-text">
          <span class="more-card-title">My Profile & Stacks</span>
          <span class="more-card-desc">Personal stats, Elo rating & settings</span>
        </div>
      </button>

      <!-- Coin Wallet & Betting -->
      <button class="more-card-item" onclick="document.getElementById('moreMenuModal').close();openCoinBalanceModal();">
        <div class="more-card-icon" style="color:var(--clr-gold);">
          <svg class="gold-coin-icon" viewBox="0 0 24 24" width="22" height="22" style="filter:drop-shadow(0 1px 2px rgba(245,158,11,0.4));"><circle cx="12" cy="12" r="10" fill="#f59e0b" stroke="#78350f" stroke-width="1.2"/><path d="M12 6.5l1.6 3.3 3.6.5-2.6 2.6.6 3.6-3.2-1.7-3.2 1.7.6-3.6-2.6-2.6 3.6-.5z" fill="#78350f"/></svg>
        </div>
        <div class="more-card-text">
          <span class="more-card-title">Coin Wallet & Betting</span>
          <span class="more-card-desc">Free bonus coins & match prediction balance</span>
        </div>
      </button>
<!-- 11. Theme Switcher -->
      <button class="more-card-item" onclick="cycleTheme();">
        <div class="more-card-icon">
          <svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
        </div>
        <div class="more-card-text">
          <span class="more-card-title">Toggle Theme</span>
          <span class="more-card-desc">Switch Dark / Light / High Contrast</span>
        </div>
      </button>

      <!-- 12. Admin Dashboard -->
      <button class="more-card-item admin-only-item" onclick="document.getElementById('moreMenuModal').close();openAdminDashboardWithGuard();">
        <div class="more-card-icon" style="color:#f87171;">
          <svg class="icon icon-sm" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
        </div>
        <div class="more-card-text" style="flex:1;">
          <span class="more-card-title">Admin Dashboard</span>
          <span class="more-card-desc">Director oversight & security audit</span>
        </div>
      </button>

      <!-- 13. Reset Tournament Data -->
      <button class="more-card-item admin-only-item" onclick="document.getElementById('moreMenuModal').close();handleResetNav();" style="border-color:rgba(239,68,68,0.25);">
        <div class="more-card-icon" style="color:#f87171;background:rgba(239,68,68,0.1);">
          <svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M3 6h18"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/><line x1="10" y1="11" x2="10" y2="17"/><line x1="14" y1="11" x2="14" y2="17"/></svg>
        </div>
        <div class="more-card-text" style="flex:1;">
          <span class="more-card-title" style="color:#f87171;">Reset Tournament Data</span>
          <span class="more-card-desc">Factory reset & purge scores/roster</span>
        </div>
      </button>

      <!-- 13. Reset Tournament Data -->
      <button class="more-card-item admin-only-item" onclick="document.getElementById('moreMenuModal').close();handleResetNav();" style="border-color:rgba(239,68,68,0.3);">
        <div class="more-card-icon" style="color:#f87171;">
          <svg class="icon icon-sm" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
        </div>
        <div class="more-card-text">
          <span class="more-card-title" style="color:#f87171;">Reset / Start Over</span>
          <span class="more-card-desc">Clear tournament matches or factory reset</span>
        </div>
      </button>
    </div>

    <div style="text-align:right;">
      <button class="btn btn-ghost btn-sm" onclick="document.getElementById('moreMenuModal').close()" data-i18n="cancelBtn">Close Menu</button>
    </div>
  </div>
</dialog>

<!-- ═══════════════════════════════════════════════════
     PUSH NOTIFICATIONS MODAL
═══════════════════════════════════════════════════ -->
<dialog id="notificationSettingsModal" class="modal" aria-labelledby="notifyModalTitle" style="max-width:390px;width:92%;">
  <div class="modal-box" style="max-width:390px;width:100%;padding:20px 22px;">
    <!-- Minimal Header -->
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;padding-bottom:10px;border-bottom:1px solid var(--clr-border);">
      <div style="display:flex;align-items:center;gap:8px;">
        <svg class="icon icon-xs" viewBox="0 0 24 24" style="color:var(--clr-green);"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg>
        <span id="notifyModalTitle" style="font-family:var(--font-display);font-size:0.95rem;font-weight:700;color:var(--clr-text);">Push Notifications</span>
      </div>
      <button class="modal-close" onclick="document.getElementById('notificationSettingsModal').close()" aria-label="Close" style="background:transparent!important;border:none!important;color:var(--clr-text-muted);cursor:pointer;padding:0;width:28px;height:28px;display:inline-flex;align-items:center;justify-content:center;border-radius:6px;outline:none;">
        <svg class="icon icon-xs" viewBox="0 0 24 24" style="stroke:currentColor;stroke-width:2.2;"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
    </div>

    <!-- Centered Minimal Hero -->
    <div style="text-align:center;padding:10px 0 14px;">
      <div id="notifyStatusIcon" style="position:relative;display:inline-flex;align-items:center;justify-content:center;width:48px;height:48px;border-radius:50%;background:rgba(34,197,94,0.12);color:var(--clr-green);margin-bottom:12px;">
        <svg class="icon icon-md" viewBox="0 0 24 24"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg>
        <span id="notifyStatusDot" style="position:absolute;top:2px;right:2px;width:9px;height:9px;border-radius:50%;background:var(--clr-green);border:2px solid var(--clr-surface-card);"></span>
      </div>

      <h4 id="notifyStatusHeading" style="font-size:1.05rem;font-weight:700;margin:0 0 4px;color:var(--clr-text);">Notifications Active</h4>
      <p id="notifyStatusDesc" style="font-size:0.8rem;color:var(--clr-text-muted);line-height:1.45;margin:0 auto 16px;max-width:290px;">
        Instant alerts for challenges, match wins, and champion finishes.
      </p>

      <!-- Active Status Badge -->
      <div id="notifyActiveBadge" style="display:inline-flex;align-items:center;gap:6px;padding:3px 12px;border-radius:999px;background:rgba(34,197,94,0.12);color:var(--clr-green);font-size:0.75rem;font-weight:700;margin-bottom:14px;border:1px solid rgba(34,197,94,0.25);">
        <span style="width:6px;height:6px;border-radius:50%;background:var(--clr-green);"></span>
        <span>Alerts Active</span>
      </div>

      <!-- Actions -->
      <div style="display:flex;flex-direction:column;gap:8px;">
        <button class="btn btn-primary btn-sm" id="btnRequestNotification" onclick="requestNotificationPermission()" style="width:100%;min-height:38px;font-weight:600;display:none;align-items:center;justify-content:center;gap:6px;">
          <svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg>
          <span>Turn On Notifications</span>
        </button>

        <button class="btn btn-ghost btn-sm" id="btnTestNotification" onclick="testPushNotification()" style="width:100%;min-height:36px;display:flex;align-items:center;justify-content:center;gap:6px;font-size:0.82rem;font-weight:600;">
          <svg class="icon icon-xs" viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
          <span>Send Test Alert</span>
        </button>
      </div>
    </div>

    <!-- Minimal Footer -->
    <div style="display:flex;justify-content:center;padding-top:10px;border-top:1px solid var(--clr-border);">
      <button class="btn btn-ghost btn-xs" onclick="document.getElementById('notificationSettingsModal').close()" style="color:var(--clr-text-muted);min-width:100px;">Done</button>
    </div>
  </div>
</dialog>
<!-- ═══════════════════════════════════════════════════
     MATCH PREDICTION & BETTING MODAL (General User Capability)
═══════════════════════════════════════════════════ -->
<dialog id="matchBettingModal" class="modal" aria-labelledby="betModalTitle" style="max-width:440px;width:92%;">
  <div class="modal-box" style="max-width:440px;">
    <div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid var(--clr-border);padding-bottom:12px;margin-bottom:14px;">
      <h3 id="betModalTitle" style="font-family:var(--font-display);font-size:1.15rem;display:flex;align-items:center;gap:8px;margin:0;">
        <span style="font-size:1.2rem;">🎲</span>
        <span>Match Prediction & Wager</span>
      </h3>
      <button class="modal-close" onclick="document.getElementById('matchBettingModal').close()" aria-label="Close" style="background:transparent!important;border:none!important;color:var(--clr-text-muted);cursor:pointer;padding:0;width:32px;height:32px;display:inline-flex;align-items:center;justify-content:center;border-radius:6px;outline:none;">
        <svg class="icon icon-xs" viewBox="0 0 24 24" style="stroke:currentColor;stroke-width:2.2;"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
    </div>

    <input type="hidden" id="betModalMatchId">

    <div style="background:rgba(255,255,255,0.03);border:1px solid var(--clr-border);border-radius:var(--radius-sm);padding:12px;margin-bottom:14px;text-align:center;">
      <div style="font-size:0.75rem;color:var(--clr-text-muted);text-transform:uppercase;letter-spacing:0.04em;margin-bottom:4px;">Match Fixture</div>
      <div style="font-size:1.05rem;font-weight:800;color:var(--clr-text);">
        <span id="betModalTeamAName">Team A</span> <span style="color:var(--clr-text-muted);font-size:0.85rem;">vs</span> <span id="betModalTeamBName">Team B</span>
      </div>
      <div style="font-size:0.8rem;color:var(--clr-gold);margin-top:4px;font-weight:700;">🎁 Payout: Double Points (2.0x) on correct prediction!</div>
    </div>

    <!-- Select Prediction Side -->
    <div style="margin-bottom:16px;">
      <label style="display:block;font-size:0.8rem;color:var(--clr-text-muted);margin-bottom:6px;">Select Predicted Winner:</label>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
        <button type="button" id="betModalTeamABtn" class="btn btn-secondary" onclick="selectBetSide('a')" style="font-size:0.82rem;padding:10px;">
          Predict Team A
        </button>
        <button type="button" id="betModalTeamBBtn" class="btn btn-secondary" onclick="selectBetSide('b')" style="font-size:0.82rem;padding:10px;">
          Predict Team B
        </button>
      </div>
    </div>

    <!-- Wager Amount -->
    <div style="margin-bottom:16px;">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
        <label style="font-size:0.8rem;color:var(--clr-text-muted);">Prediction Wager (Coins):</label>
        <span style="font-size:0.78rem;color:var(--clr-gold);font-weight:700;">Balance: <span id="bettingModalUserBalance">100</span> PTS</span>
      </div>
      <input type="number" id="betModalAmountInput" class="modal-input" min="1" max="10000" value="25" style="font-family:monospace;font-size:1.1rem;font-weight:700;margin-bottom:8px;">
      <div style="display:flex;gap:6px;">
        <button type="button" class="btn btn-ghost btn-xs" onclick="setBetAmount(10)">10 PTS</button>
        <button type="button" class="btn btn-ghost btn-xs" onclick="setBetAmount(25)">25 PTS</button>
        <button type="button" class="btn btn-ghost btn-xs" onclick="setBetAmount(50)">50 PTS</button>
        <button type="button" class="btn btn-ghost btn-xs" onclick="setBetAmount(getUserCoins())">All In</button>
      </div>
    </div>

    <div style="display:flex;justify-content:flex-end;gap:8px;border-top:1px solid var(--clr-border);padding-top:12px;">
      <button class="btn btn-ghost btn-sm" onclick="document.getElementById('matchBettingModal').close()">Cancel</button>
      <button class="btn btn-primary btn-sm" onclick="placeBet()">Confirm Prediction Wager</button>
    </div>
  </div>
</dialog>

<!-- ═══════════════════════════════════════════════════
     ADMIN ACCESS GUARD MODAL (Capability Protection)
═══════════════════════════════════════════════════ -->
<dialog id="adminAuthGuardModal" class="modal" aria-labelledby="guardModalTitle" style="max-width:460px;width:92%;">
  <div class="modal-box" style="max-width:460px;">
    <div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid var(--clr-border);padding-bottom:12px;margin-bottom:16px;">
      <h3 id="guardModalTitle" style="font-family:var(--font-display);font-size:1.15rem;display:flex;align-items:center;gap:8px;margin:0;color:var(--clr-text);">
        <svg class="icon icon-sm" viewBox="0 0 24 24" style="color:var(--clr-gold);"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        <span>Admin Access Required</span>
      </h3>
      <button class="modal-close" onclick="document.getElementById('adminAuthGuardModal').close()" aria-label="Close" style="background:transparent!important;border:none!important;color:var(--clr-text-muted);cursor:pointer;padding:0;width:32px;height:32px;display:inline-flex;align-items:center;justify-content:center;border-radius:6px;outline:none;">
        <svg class="icon icon-xs" viewBox="0 0 24 24" style="stroke:currentColor;stroke-width:2.2;"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
    </div>

    <div style="padding:4px 0 16px;">
      <div style="font-size:0.9rem;color:var(--clr-text);line-height:1.5;margin-bottom:14px;">
        The section <strong id="guardActionName" style="color:var(--clr-gold);">Tournament Setup & Roster</strong> is restricted to Tournament Directors & Admins.
      </div>

      <div style="background:rgba(255,255,255,0.03);border:1px solid var(--clr-border);border-left:3px solid var(--clr-green);border-radius:var(--radius-sm);padding:14px;font-size:0.82rem;color:var(--clr-text-muted);line-height:1.45;margin-bottom:18px;">
        <div style="font-weight:700;color:var(--clr-green);margin-bottom:4px;display:flex;align-items:center;gap:6px;">
          <span>✓</span> <span>General User Capabilities:</span>
        </div>
        Open challenges, accept & play matches, referee casual games, and place prediction bets with virtual coins.
      </div>

      <div style="display:flex;flex-direction:column;gap:10px;">
        <button class="btn btn-primary" onclick="document.getElementById('adminAuthGuardModal').close();openAuthModal();" style="width:100%;min-height:44px;font-weight:700;font-size:0.92rem;display:flex;align-items:center;justify-content:center;gap:8px;">
          <svg class="icon icon-xs" viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
          <span>Sign In with Director Credentials</span>
        </button>
      </div>
    </div>

    <div style="display:flex;justify-content:center;border-top:1px solid var(--clr-border);padding-top:12px;margin-top:6px;">
      <button class="btn btn-ghost btn-xs" onclick="document.getElementById('adminAuthGuardModal').close()" style="color:var(--clr-text-muted);">Cancel</button>
    </div>
  </div>
</dialog>

<!-- ═══════════════════════════════════════════════════
     COIN WALLET & BONUS MODAL
═══════════════════════════════════════════════════ -->
<dialog id="coinBalanceModal" class="modal" aria-labelledby="coinModalTitle" style="max-width:440px;width:92%;">
  <div class="modal-box" style="max-width:440px;">
    <div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid var(--clr-border);padding-bottom:12px;margin-bottom:16px;">
      <h3 id="coinModalTitle" style="font-family:var(--font-display);font-size:1.15rem;font-weight:700;display:flex;align-items:center;gap:8px;margin:0;color:var(--clr-text);">
        <svg class="icon icon-sm" viewBox="0 0 24 24" style="color:var(--clr-gold);"><circle cx="12" cy="12" r="10"/><path d="M12 6v12M15 9.5a3 3 0 0 0-3-2.5h-1a2.5 2.5 0 0 0 0 5h2a2.5 2.5 0 0 1 0 5h-1a3 3 0 0 1-3-2.5"/></svg>
        <span>Virtual Coin Wallet</span>
      </h3>
      <button class="modal-close" onclick="document.getElementById('coinBalanceModal').close()" aria-label="Close" style="background:transparent!important;border:none!important;color:var(--clr-text-muted);cursor:pointer;padding:0;width:32px;height:32px;display:inline-flex;align-items:center;justify-content:center;border-radius:6px;outline:none;">
        <svg class="icon icon-xs" viewBox="0 0 24 24" style="stroke:currentColor;stroke-width:2.2;"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
    </div>

    <!-- Hero Balance Display -->
    <div style="background:rgba(245,158,11,0.06);border:1px solid rgba(245,158,11,0.25);border-radius:var(--radius-sm);padding:20px 16px;text-align:center;margin-bottom:18px;">
      <div style="font-size:0.75rem;font-weight:700;color:var(--clr-gold);text-transform:uppercase;letter-spacing:0.06em;margin-bottom:8px;">Available Points & Coin Balance</div>
      <div style="display:flex;align-items:center;justify-content:center;gap:10px;">
        <svg class="gold-coin-icon" viewBox="0 0 24 24" width="34" height="34" style="flex-shrink:0;filter:drop-shadow(0 2px 4px rgba(245,158,11,0.5));" aria-hidden="true">
          <circle cx="12" cy="12" r="10" fill="#f59e0b" stroke="#78350f" stroke-width="1.3"/>
          <circle cx="12" cy="12" r="7.5" fill="none" stroke="#fef9c3" stroke-width="0.8" stroke-dasharray="2 1.5"/>
          <path d="M12 6.5l1.6 3.3 3.6.5-2.6 2.6.6 3.6-3.2-1.7-3.2 1.7.6-3.6-2.6-2.6 3.6-.5z" fill="#78350f"/>
        </svg>
        <span style="font-family:var(--font-display);font-size:2.8rem;font-weight:900;color:var(--clr-text);line-height:1;" id="coinModalBigCount">100</span>
        <span style="font-size:0.9rem;font-weight:700;color:var(--clr-gold);">PTS / COINS</span>
      </div>
      <div style="font-size:0.82rem;color:var(--clr-text-muted);margin-top:8px;">
        Earned from tournament match scoring, victories (+50 bonus), and daily rewards.
      </div>
    </div>

    <!-- Action Buttons -->
    <div style="display:flex;flex-direction:column;gap:10px;margin-bottom:16px;">
      <button class="btn btn-primary btn-md" id="btnClaimDailyBonus" onclick="claimDailyBonus()" style="width:100%;min-height:44px;font-size:0.92rem;font-weight:700;display:flex;align-items:center;justify-content:center;gap:8px;">
        <span>🎁 Claim Daily Bonus (+50 Free Coins)</span>
      </button>
      <button class="btn btn-ghost btn-sm" onclick="document.getElementById('coinBalanceModal').close();showScreen('groupsScreen');" style="width:100%;min-height:38px;display:flex;align-items:center;justify-content:center;gap:6px;">
        <span>🎲 Explore Live Matches to Predict</span>
      </button>
    </div>

    <!-- Info Banner -->
    <div style="background:rgba(255,255,255,0.03);border:1px solid var(--clr-border);border-radius:var(--radius-sm);padding:12px 14px;font-size:0.8rem;color:var(--clr-text-muted);line-height:1.45;text-align:center;">
      Coins are 100% free virtual points for sports predictions. Correct match predictions earn 1.90x coin payouts!
    </div>

    <!-- Footer -->
    <div style="display:flex;justify-content:center;border-top:1px solid var(--clr-border);padding-top:14px;margin-top:16px;">
      <button class="btn btn-ghost btn-sm" onclick="document.getElementById('coinBalanceModal').close()" style="min-width:140px;">Done</button>
    </div>
  </div>
</dialog>
<!-- ═══════════════════════════════════════════════════
     GENERIC CUSTOM CONFIRM & PROMPT MODALS (PWA NATIVE ALTERNATIVES)
═══════════════════════════════════════════════════ -->
<dialog id="appConfirmModal" class="modal" aria-labelledby="appConfirmTitle" style="max-width:420px;width:92%;">
  <div class="modal-box" style="max-width:440px;text-align:center;">
    <div style="display:flex;justify-content:flex-end;">
      <button class="modal-close" onclick="document.getElementById('appConfirmModal').close()" aria-label="Close">
        <svg class="icon icon-xs" viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
    </div>
    <div style="width:48px;height:48px;border-radius:50%;background:rgba(239,68,68,0.12);color:#ef4444;display:inline-flex;align-items:center;justify-content:center;margin-bottom:12px;border:1px solid rgba(239,68,68,0.25);">
      <svg class="icon icon-md" viewBox="0 0 24 24"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
    </div>
    <h3 id="appConfirmTitle" style="font-family:var(--font-display);font-size:1.25rem;font-weight:800;margin:0 0 8px;color:var(--clr-text);">Confirmation Required</h3>
    <p id="appConfirmMsg" style="color:var(--clr-text-muted);font-size:0.88rem;margin:0 auto 20px;max-width:360px;line-height:1.45;">Are you sure you want to proceed?</p>
    <div style="display:flex;gap:10px;justify-content:center;">
      <button type="button" class="btn btn-ghost btn-sm" id="appConfirmCancelBtn" style="min-width:110px;">Cancel</button>
      <button type="button" class="btn btn-primary btn-sm" id="appConfirmOkBtn" style="min-width:130px;">Confirm</button>
    </div>
  </div>
</dialog>

<dialog id="appPromptModal" class="modal" aria-labelledby="appPromptTitle" style="max-width:440px;width:92%;">
  <div class="modal-box" style="max-width:440px;">
    <div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid var(--clr-border);padding-bottom:12px;margin-bottom:14px;">
      <h3 id="appPromptTitle" style="font-family:var(--font-display);font-size:1.15rem;font-weight:700;margin:0;color:var(--clr-text);">Input Required</h3>
      <button class="modal-close" onclick="document.getElementById('appPromptModal').close()" aria-label="Close">
        <svg class="icon icon-xs" viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
    </div>
    <p id="appPromptMsg" style="color:var(--clr-text-muted);font-size:0.85rem;margin:0 0 12px;line-height:1.4;"></p>
    <input type="text" id="appPromptInput" class="modal-input" style="width:100%;margin-bottom:18px;">
    <div style="display:flex;gap:10px;justify-content:flex-end;">
      <button type="button" class="btn btn-ghost btn-sm" id="appPromptCancelBtn">Cancel</button>
      <button type="button" class="btn btn-primary btn-sm" id="appPromptOkBtn">Submit</button>
    </div>
  </div>
</dialog>


<!-- User Profile Settings Modal -->
<dialog id="userProfileSettingsModal" class="modal" aria-labelledby="profileSettingsTitle" style="max-width:520px;width:92%;">
  <div class="modal-box" style="max-width:520px;max-height:90vh;overflow-y:auto;">
    <div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid var(--clr-border);padding-bottom:12px;margin-bottom:16px;">
      <h3 id="profileSettingsTitle" style="font-family:var(--font-display);font-size:1.2rem;font-weight:700;display:flex;align-items:center;gap:8px;margin:0;color:var(--clr-text);">
        <svg class="icon icon-sm" viewBox="0 0 24 24" style="color:var(--clr-green);"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
        <span>Athlete Profile Settings</span>
      </h3>
      <button class="modal-close" onclick="document.getElementById('userProfileSettingsModal').close()" aria-label="Close" style="background:transparent!important;border:none!important;color:var(--clr-text-muted);cursor:pointer;padding:0;width:32px;height:32px;display:inline-flex;align-items:center;justify-content:center;border-radius:6px;outline:none;">
        <svg class="icon icon-xs" viewBox="0 0 24 24" style="stroke:currentColor;stroke-width:2.2;"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
    </div>

    <form id="profileSettingsForm" onsubmit="saveProfileSettings(event)">
      <!-- Profile Photo & Avatar Customization -->
      <div style="background:rgba(255,255,255,0.03);border:1px solid var(--clr-border);border-radius:var(--radius-md);padding:16px;margin-bottom:18px;">
        <div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap;">
          <!-- Avatar / Photo Circle Preview -->
          <div id="profileEditAvatarPreview" style="width:68px;height:68px;border-radius:50%;background:var(--clr-green);color:#fff;display:flex;align-items:center;justify-content:center;font-size:1.6rem;font-weight:900;flex-shrink:0;overflow:hidden;border:2px solid var(--clr-border);box-shadow:0 2px 8px rgba(0,0,0,0.25);">
            R
          </div>

          <!-- Photo Upload Action Group -->
          <div style="flex:1;min-width:200px;">
            <div style="font-size:0.88rem;font-weight:700;color:var(--clr-text);margin-bottom:3px;">Profile Photo</div>
            <div style="font-size:0.74rem;color:var(--clr-text-muted);margin-bottom:10px;">Upload a custom portrait from your phone or computer.</div>
            <div style="display:flex;gap:8px;flex-wrap:wrap;align-items:center;">
              <input type="file" id="profilePhotoFileInput" accept="image/png, image/jpeg, image/webp" style="display:none;" onchange="handleProfilePhotoSelected(event)">
              <button type="button" class="btn btn-primary btn-xs" onclick="document.getElementById('profilePhotoFileInput').click()" style="display:inline-flex;align-items:center;gap:6px;font-weight:600;">
                <svg class="icon icon-xs" viewBox="0 0 24 24"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>
                <span>Upload Photo</span>
              </button>
              <button type="button" class="btn btn-ghost btn-xs" id="removeProfilePhotoBtn" onclick="removeProfilePhoto()" style="color:var(--clr-text-muted);">
                <span>Remove</span>
              </button>
            </div>
          </div>
        </div>

        <!-- Preset Athlete Badges & Custom Initials -->
        <div style="margin-top:14px;padding-top:12px;border-top:1px solid rgba(255,255,255,0.06);">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;flex-wrap:wrap;gap:8px;">
            <span style="font-size:0.74rem;font-weight:700;color:var(--clr-text-muted);text-transform:uppercase;letter-spacing:0.04em;">Or Quick Badges / Emojis:</span>
            <div style="display:flex;align-items:center;gap:6px;">
              <span style="font-size:0.72rem;color:var(--clr-text-muted);">Custom Initial:</span>
              <input type="text" id="profileEditAvatar" maxlength="2" class="modal-input" style="width:52px;padding:3px 6px;text-align:center;font-weight:900;text-transform:uppercase;font-size:0.82rem;" oninput="updateProfileAvatarPreview(this.value)">
            </div>
          </div>
          <div style="display:flex;gap:6px;flex-wrap:wrap;">
            <button type="button" class="btn btn-ghost btn-xs" onclick="selectPresetAvatarBadge('🏸')" style="font-size:1rem;padding:4px 8px;" title="Badminton Shuttle">🏸</button>
            <button type="button" class="btn btn-ghost btn-xs" onclick="selectPresetAvatarBadge('🥇')" style="font-size:1rem;padding:4px 8px;" title="Gold Medal">🥇</button>
            <button type="button" class="btn btn-ghost btn-xs" onclick="selectPresetAvatarBadge('⚡')" style="font-size:1rem;padding:4px 8px;" title="Lightning">⚡</button>
            <button type="button" class="btn btn-ghost btn-xs" onclick="selectPresetAvatarBadge('👑')" style="font-size:1rem;padding:4px 8px;" title="Champion Crown">👑</button>
            <button type="button" class="btn btn-ghost btn-xs" onclick="selectPresetAvatarBadge('🦁')" style="font-size:1rem;padding:4px 8px;" title="Lionheart">🦁</button>
            <button type="button" class="btn btn-ghost btn-xs" onclick="selectPresetAvatarBadge('🐯')" style="font-size:1rem;padding:4px 8px;" title="Tiger">🐯</button>
            <button type="button" class="btn btn-ghost btn-xs" onclick="selectPresetAvatarBadge('🚀')" style="font-size:1rem;padding:4px 8px;" title="Rocket">🚀</button>
            <button type="button" class="btn btn-ghost btn-xs" onclick="selectPresetAvatarBadge('🎯')" style="font-size:1rem;padding:4px 8px;" title="Target Bullseye">🎯</button>
          </div>
        </div>
      </div>

      <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px;">
        <div>
          <label style="display:block;font-size:0.75rem;font-weight:700;color:var(--clr-text-muted);text-transform:uppercase;margin-bottom:4px;">Full Name *</label>
          <input type="text" id="profileEditName" required class="modal-input" style="width:100%;">
        </div>
        <div>
          <label style="display:block;font-size:0.75rem;font-weight:700;color:var(--clr-text-muted);text-transform:uppercase;margin-bottom:4px;">Email</label>
          <input type="email" id="profileEditEmail" class="modal-input" style="width:100%;">
        </div>
      </div>

      <div style="margin-bottom:12px;">
        <label style="display:block;font-size:0.75rem;font-weight:700;color:var(--clr-text-muted);text-transform:uppercase;margin-bottom:4px;">Club / Team Affiliation</label>
        <input type="text" id="profileEditClub" placeholder="e.g. Dhaka Smashers, National Academy" class="modal-input" style="width:100%;">
      </div>

      <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px;">
        <div>
          <label style="display:block;font-size:0.75rem;font-weight:700;color:var(--clr-text-muted);text-transform:uppercase;margin-bottom:4px;">Dominant Hand</label>
          <select id="profileEditHand" class="modal-input" style="width:100%;">
            <option value="Right-Handed">Right-Handed</option>
            <option value="Left-Handed">Left-Handed</option>
            <option value="Ambidextrous">Ambidextrous</option>
          </select>
        </div>
        <div>
          <label style="display:block;font-size:0.75rem;font-weight:700;color:var(--clr-text-muted);text-transform:uppercase;margin-bottom:4px;">Playing Style</label>
          <select id="profileEditStyle" class="modal-input" style="width:100%;">
            <option value="Attacking / Smasher">Attacking / Smasher</option>
            <option value="Defensive / Counter">Defensive / Counter</option>
            <option value="Tactical / Playmaker">Tactical / Playmaker</option>
            <option value="Speed & Net Play">Speed & Net Play</option>
            <option value="All-Rounder">All-Rounder</option>
          </select>
        </div>
        <div>
          <label style="display:block;font-size:0.75rem;font-weight:700;color:var(--clr-text-muted);text-transform:uppercase;margin-bottom:4px;">Dominant Hand</label>
          <select id="profileEditDominantHand" class="modal-input" style="width:100%;">
            <option value="Right-handed">Right-handed (Standard)</option>
            <option value="Left-handed">Left-handed (Lefty)</option>
          </select>
        </div>
      </div>

      <div style="margin-bottom:18px;">
        <label style="display:block;font-size:0.75rem;font-weight:700;color:var(--clr-text-muted);text-transform:uppercase;margin-bottom:4px;">Change Passcode / PIN (Leave blank to keep current)</label>
        <input type="password" id="profileEditPasscode" placeholder="New 4-digit PIN or password" class="modal-input" style="width:100%;">
      </div>

      <div style="display:flex;gap:10px;justify-content:flex-end;border-top:1px solid var(--clr-border);padding-top:14px;">
        <button type="button" class="btn btn-ghost btn-sm" onclick="document.getElementById('userProfileSettingsModal').close()">Cancel</button>
        <button type="submit" class="btn btn-primary btn-sm" style="display:inline-flex;align-items:center;gap:6px;">
          <span>Save Changes</span>
        </button>
      </div>
    </form>
  </div>
</dialog>


<!-- Keyboard Shortcuts Help Modal -->
<dialog id="shortcutsHelpModal" closedby="any" style="max-width:440px;">
  <div class="modal-card">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;">
      <h2 style="font-size:1.15rem;font-weight:700;display:flex;align-items:center;gap:8px;">
        <svg class="icon icon-sm" viewBox="0 0 24 24"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="M6 8h.001M10 8h.001M14 8h.001M18 8h.001M8 12h.001M12 12h.001M16 12h.001M7 16h10"/></svg>
        Referee Keyboard Shortcuts
      </h2>
      <button class="modal-close" onclick="document.getElementById('shortcutsHelpModal').close()" aria-label="Close Shortcuts"><svg class="icon icon-xs" viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></button>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;font-size:0.83rem;">
      <div style="background:rgba(255,255,255,0.04);border:1px solid var(--clr-border);padding:10px;border-radius:8px;">
        <kbd style="background:var(--clr-surface-hi);padding:2px 6px;border-radius:4px;font-weight:700;color:var(--clr-gold);">Space</kbd>
        <div style="margin-top:4px;color:var(--clr-text-muted);">Score point for Server</div>
      </div>
      <div style="background:rgba(255,255,255,0.04);border:1px solid var(--clr-border);padding:10px;border-radius:8px;">
        <kbd style="background:var(--clr-surface-hi);padding:2px 6px;border-radius:4px;font-weight:700;color:var(--clr-gold);">Shift + Space</kbd>
        <div style="margin-top:4px;color:var(--clr-text-muted);">Score point for Receiver</div>
      </div>
      <div style="background:rgba(255,255,255,0.04);border:1px solid var(--clr-border);padding:10px;border-radius:8px;">
        <kbd style="background:var(--clr-surface-hi);padding:2px 6px;border-radius:4px;font-weight:700;color:var(--clr-green);">U</kbd>
        <div style="margin-top:4px;color:var(--clr-text-muted);">Undo last rally point</div>
      </div>
      <div style="background:rgba(255,255,255,0.04);border:1px solid var(--clr-border);padding:10px;border-radius:8px;">
        <kbd style="background:var(--clr-surface-hi);padding:2px 6px;border-radius:4px;font-weight:700;color:var(--clr-cyan);">F</kbd>
        <div style="margin-top:4px;color:var(--clr-text-muted);">Flip court ends</div>
      </div>
      <div style="background:rgba(255,255,255,0.04);border:1px solid var(--clr-border);padding:10px;border-radius:8px;">
        <kbd style="background:var(--clr-surface-hi);padding:2px 6px;border-radius:4px;font-weight:700;color:var(--clr-text);">I</kbd>
        <div style="margin-top:4px;color:var(--clr-text-muted);">Call 60s / 120s interval</div>
      </div>
      <div style="background:rgba(255,255,255,0.04);border:1px solid var(--clr-border);padding:10px;border-radius:8px;">
        <kbd style="background:var(--clr-surface-hi);padding:2px 6px;border-radius:4px;font-weight:700;color:#f87171;">Esc</kbd>
        <div style="margin-top:4px;color:var(--clr-text-muted);">Dismiss modal / Dialog</div>
      </div>
    </div>
    <div style="margin-top:16px;text-align:right;">
      <button class="btn btn-primary btn-sm" onclick="document.getElementById('shortcutsHelpModal').close()">Got it</button>
    </div>
  </div>
</dialog>

<!-- Challenge PIN Verification Modal -->
<dialog id="challengePinPromptModal" closedby="any" style="max-width:380px;">
  <div class="modal-card" style="text-align:center;">
    <div style="font-size:2rem;margin-bottom:8px;">🔒</div>
    <h2 style="font-size:1.2rem;font-weight:700;margin-bottom:6px;">Private Challenge</h2>
    <p style="color:var(--clr-text-muted);font-size:0.83rem;margin-bottom:16px;">This challenge is password protected. Enter the 4-digit PIN provided by the creator to accept:</p>
    <input type="password" id="challengeAcceptPinInput" maxlength="4" class="modal-input" placeholder="4-digit PIN" style="width:160px;margin:0 auto 16px;text-align:center;font-size:1.4rem;letter-spacing:6px;">
    <input type="hidden" id="challengePinTargetId">
    <div style="display:flex;justify-content:center;gap:10px;">
      <button class="btn btn-ghost btn-sm" onclick="document.getElementById('challengePinPromptModal').close()">Cancel</button>
      <button class="btn btn-primary btn-sm" onclick="verifyAndAcceptChallengePin()">Unlock & Accept</button>
    </div>
  </div>
</dialog>

<!-- Challenge QR Code Modal -->
<dialog id="challengeQrModal" closedby="any" style="max-width:400px;">
  <div class="modal-card" style="text-align:center;">
    <h2 style="font-size:1.2rem;font-weight:700;margin-bottom:6px;">Scan to Join Match</h2>
    <p style="color:var(--clr-text-muted);font-size:0.83rem;margin-bottom:16px;">Point any phone camera to instantly open and accept this challenge.</p>
    <div id="challengeQrSvgContainer" style="display:flex;justify-content:center;padding:16px;background:#ffffff;border-radius:12px;margin:0 auto 16px;width:220px;height:220px;"></div>
    <div id="challengeDeepLinkText" style="font-size:0.75rem;word-break:break-all;color:var(--clr-text-muted);margin-bottom:14px;background:rgba(255,255,255,0.04);padding:8px;border-radius:6px;"></div>
    <div style="display:flex;justify-content:center;gap:10px;">
      <button class="btn btn-outline btn-sm" onclick="copyChallengeQrLink()">Copy Link</button>
      <button class="btn btn-primary btn-sm" onclick="document.getElementById('challengeQrModal').close()">Done</button>
    </div>
  </div>
</dialog>

<!-- Official Printable Scorecard Modal -->
<dialog id="printableScorecardModal" closedby="any" style="max-width:720px;width:95%;">
  <div class="modal-card" style="padding:24px;">
    <div class="no-print" style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
      <h2 style="font-size:1.2rem;font-weight:700;">Official Match Scorecard (BWF Standard)</h2>
      <div style="display:flex;gap:8px;">
        <button class="btn btn-primary btn-sm" onclick="window.print()">🖨️ Print / Save PDF</button>
        <button class="btn btn-ghost btn-sm" onclick="document.getElementById('printableScorecardModal').close()">Close</button>
      </div>
    </div>
    <div id="printableScorecardContent" style="background:#ffffff;color:#111827;padding:24px;border-radius:8px;font-family:'Poppins',sans-serif;">
      <!-- Populated dynamically via renderPrintableScorecard() -->
    </div>
  </div>
</dialog>

<!-- Tournament Archive Management Modal -->
<dialog id="tournamentArchiveModal" closedby="any" style="max-width:540px;">
  <div class="modal-card">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;">
      <h2 style="font-size:1.2rem;font-weight:700;">📁 Tournament Archives & Switcher</h2>
      <button class="modal-close" onclick="document.getElementById('tournamentArchiveModal').close()" aria-label="Close Archive"><svg class="icon icon-xs" viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></button>
    </div>
    <p style="color:var(--clr-text-muted);font-size:0.83rem;margin-bottom:16px;">Save snapshots of current tournament or restore past tournaments without losing data.</p>
    <div style="display:flex;gap:10px;margin-bottom:16px;">
      <input type="text" id="archiveTourneyNameInput" class="modal-input" placeholder="Tournament Name (e.g. Winter Cup 2026)" style="flex:1;">
      <button class="btn btn-primary btn-sm" onclick="saveTournamentSnapshot()">Save Snapshot</button>
    </div>
    <div id="tournamentsArchiveList" style="max-height:240px;overflow-y:auto;border:1px solid var(--clr-border);border-radius:8px;padding:8px;">
      <!-- Populated via renderTournamentsArchiveList() -->
    </div>
  </div>
</dialog>


<!-- 1. Disciplinary Sanctions Modal (Yellow / Red / Black Card) -->
<dialog id="disciplinaryCardModal" closedby="any" style="max-width:440px;">
  <div class="modal-card">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;">
      <h2 style="font-size:1.15rem;font-weight:700;display:flex;align-items:center;gap:8px;">
        <span class="card-chip card-yellow"></span>
        BWF Official Disciplinary Sanction
      </h2>
      <button class="modal-close" onclick="document.getElementById('disciplinaryCardModal').close()"><svg class="icon icon-xs" viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></button>
    </div>
    <p style="color:var(--clr-text-muted);font-size:0.83rem;margin-bottom:14px;">Issue formal warning or penalty under BWF Law 16.7 for delay of play, misconduct, or equipment abuse.</p>
    
    <div class="modal-form-item">
      <label>Target Athlete / Side</label>
      <select id="disciplinarySideSelect" class="modal-input" style="width:100%;">
        <option value="a">Player A / Team A</option>
        <option value="b">Player B / Team B</option>
      </select>
    </div>

    <div class="modal-form-item">
      <label>Sanction Level</label>
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-top:6px;">
        <button type="button" class="btn btn-outline btn-sm" onclick="selectCardType('YELLOW')" id="cardBtnYellow" style="border-color:#eab308;color:#eab308;">
          <span class="card-chip card-yellow"></span> Yellow (Warning)
        </button>
        <button type="button" class="btn btn-outline btn-sm" onclick="selectCardType('RED')" id="cardBtnRed" style="border-color:#ef4444;color:#ef4444;">
          <span class="card-chip card-red"></span> Red (Fault + 1 Pt)
        </button>
        <button type="button" class="btn btn-outline btn-sm" onclick="selectCardType('BLACK')" id="cardBtnBlack" style="border-color:#6b7280;color:#9ca3af;">
          <span class="card-chip card-black"></span> Black (Disqualify)
        </button>
      </div>
      <input type="hidden" id="selectedCardType" value="YELLOW">
    </div>

    <div class="modal-form-item">
      <label>Reason / Infraction</label>
      <input type="text" id="disciplinaryReasonInput" class="modal-input" placeholder="e.g. Deliberate delay / Racket throwing / Dissent">
    </div>

    <div style="display:flex;justify-content:flex-end;gap:10px;margin-top:16px;">
      <button class="btn btn-ghost btn-sm" onclick="document.getElementById('disciplinaryCardModal').close()">Cancel</button>
      <button class="btn btn-primary btn-sm" onclick="confirmIssueDisciplinaryCard()">Confirm Sanction</button>
    </div>
  </div>
</dialog>

<!-- 2. Medical Timeout Countdown Modal -->
<dialog id="medicalTimeoutModal" closedby="any" style="max-width:400px;">
  <div class="modal-card" style="text-align:center;">
    <div style="font-size:2rem;margin-bottom:6px;">🩹</div>
    <h2 style="font-size:1.25rem;font-weight:700;margin-bottom:4px;">Medical Recovery Break</h2>
    <p style="color:var(--clr-text-muted);font-size:0.82rem;margin-bottom:14px;">BWF official 5-minute injury recovery interval.</p>
    
    <div id="medicalTimerClock" style="font-family:'Anton',monospace;font-size:3.5rem;color:#ef4444;margin:12px 0;">05:00</div>
    <input type="text" id="medicalInjuryNote" class="modal-input" placeholder="Injury note (e.g. Left ankle strain)" style="margin-bottom:14px;text-align:center;">

    <div style="display:flex;justify-content:center;gap:10px;">
      <button class="btn btn-ghost btn-sm" onclick="stopMedicalTimeout()">Resume Match</button>
      <button class="btn btn-primary btn-sm" onclick="addMedicalMinute()">+1 Minute</button>
    </div>
  </div>
</dialog>

<!-- 3. Official Printable Certificate Modal -->
<dialog id="certificatePrintModal" closedby="any" style="max-width:860px;width:95%;">
  <div class="modal-card" style="padding:24px;">
    <div class="no-print" style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
      <h2 style="font-size:1.2rem;font-weight:700;">Certificate of Athletic Achievement</h2>
      <div style="display:flex;gap:8px;">
        <button class="btn btn-primary btn-sm" onclick="window.print()">🖨️ Print / Save PDF</button>
        <button class="btn btn-ghost btn-sm" onclick="document.getElementById('certificatePrintModal').close()">Close</button>
      </div>
    </div>
    <div id="certificateContainerContent"></div>
  </div>
</dialog>

<!-- 4. Player & Umpire ID Badges Modal -->
<dialog id="playerIdBadgesModal" closedby="any" style="max-width:800px;width:95%;">
  <div class="modal-card" style="padding:24px;">
    <div class="no-print" style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
      <h2 style="font-size:1.2rem;font-weight:700;">🪪 Printable Official Tournament Badges</h2>
      <div style="display:flex;gap:8px;">
        <button class="btn btn-primary btn-sm" onclick="window.print()">🖨️ Print All Badges</button>
        <button class="btn btn-ghost btn-sm" onclick="document.getElementById('playerIdBadgesModal').close()">Close</button>
      </div>
    </div>
    <div id="idBadgesGridContainer" style="display:grid;grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));gap:16px;"></div>
  </div>
</dialog>

<!-- 5. Interactive Pool Draw Ceremony Wheel Modal -->
<dialog id="poolDrawWheelModal" closedby="any" style="max-width:480px;">
  <div class="modal-card" style="text-align:center;">
    <h2 style="font-size:1.3rem;font-weight:800;margin-bottom:6px;">🎡 Live Pool Draw Ceremony</h2>
    <p style="color:var(--clr-text-muted);font-size:0.83rem;margin-bottom:16px;">Spin the wheel to assign teams randomly into tournament pools in front of spectators!</p>
    
    <div style="position:relative;width:240px;height:240px;margin:0 auto 16px;">
      <canvas id="poolDrawCanvas" width="240" height="240" style="border-radius:50%;box-shadow:0 4px 20px rgba(0,0,0,0.5);"></canvas>
      <div style="position:absolute;top:-10px;left:50%;transform:translateX(-50%);font-size:1.6rem;color:#f59e0b;">▼</div>
    </div>
    
    <div id="wheelCurrentDrawnText" style="font-size:1.15rem;font-weight:900;color:var(--clr-gold);min-height:28px;">Tap Spin to Draw</div>

    <div style="display:flex;justify-content:center;gap:10px;margin-top:14px;">
      <button class="btn btn-primary btn-lg" onclick="spinPoolDrawWheel()">Spin Wheel</button>
      <button class="btn btn-ghost btn-lg" onclick="document.getElementById('poolDrawWheelModal').close()">Close</button>
    </div>
  </div>
</dialog>

<!-- 6. Score Edit & Tamper Audit Trail Modal -->
<dialog id="auditTrailModal" closedby="any" style="max-width:680px;width:95%;">
  <div class="modal-card">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;">
      <h2 style="font-size:1.2rem;font-weight:700;">🛡️ Score Modification Audit Trail</h2>
      <button class="modal-close" onclick="document.getElementById('auditTrailModal').close()"><svg class="icon icon-xs" viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></button>
    </div>
    <p style="color:var(--clr-text-muted);font-size:0.83rem;margin-bottom:14px;">Transparent, immutable history of all referee score corrections and admin overrides.</p>
    <div id="auditTrailListContainer" style="max-height:340px;overflow-y:auto;border:1px solid var(--clr-border);border-radius:8px;padding:8px;"></div>
  </div>
</dialog>

"""