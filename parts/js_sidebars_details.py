# parts/js_sidebars_details.py

def get_sidebars_details_js():
    return """
    /* =====================================================================
       9. LEFT ANALYTICS SIDEBAR & CHART ENGINES (DYNAMIC PER MODE)
       ===================================================================== */
    function updateSidebarAnalytics() {
      const tabsNav = document.getElementById('sidebar-tabs-nav');
      const content = document.getElementById('sidebar-dynamic-content');
      const mobileTitle = document.getElementById('sidebar-mobile-title');
      if (!tabsNav || !content) return;

      if (currentMapMode === 'election') {
        if (mobileTitle) mobileTitle.textContent = 'Election Results Analytics';
        tabsNav.innerHTML = `
          <button class="sidebar-tab-btn active" onclick="switchSidebarTab('tab-elec-overview')">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 20V10M12 20V4M6 20v-6"/></svg>
            <span>Overview</span>
          </button>
          <button class="sidebar-tab-btn" onclick="switchSidebarTab('tab-elec-states')">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"/></svg>
            <span>State Wise</span>
          </button>
          <button class="sidebar-tab-btn" onclick="switchSidebarTab('tab-elec-margins')">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="m4.93 4.93 4.24 4.24M14.83 9.17l4.24-4.24"/></svg>
            <span>Battlegrounds</span>
          </button>
        `;

        content.innerHTML = `
          <div id="tab-elec-overview" class="sidebar-tab-pane">
            <div class="analytics-card">
              <div class="card-header"><span class="card-title">Parliamentary Majority Bar</span><span class="card-badge">272 to Form Govt</span></div>
              <div class="majority-meter-container">
                <div class="majority-scale-header"><span>NDA: <b>293</b></span><span>INDIA: <b>234</b></span><span>Others: <b>16</b></span></div>
                <div class="majority-track">
                  <div class="majority-target-label">272</div>
                  <div class="majority-target-line"></div>
                  <div class="majority-segment" style="background:#f97316; width:54%;"></div>
                  <div class="majority-segment" style="background:#2563eb; width:43%;"></div>
                  <div class="majority-segment" style="background:#64748b; width:3%;"></div>
                </div>
              </div>
            </div>

            <div class="analytics-card">
              <div class="card-header"><span class="card-title">Party-Wise Seat Distribution</span></div>
              <div style="position:relative; height:190px;"><canvas id="chart-party-seats"></canvas></div>
            </div>

            <div class="analytics-card" style="padding:10px;">
              <div class="card-header"><span class="card-title">National Party Leaderboard</span><span class="card-badge">42 Parties</span></div>
              <div style="max-height:240px; overflow-y:auto;">
                <table class="analytics-table">
                  <thead><tr><th>Party</th><th>Seats</th><th>Share</th><th>Alliance</th></tr></thead>
                  <tbody id="party-leaderboard-tbody"></tbody>
                </table>
              </div>
            </div>
          </div>

          <div id="tab-elec-states" class="sidebar-tab-pane" style="display:none;">
            <div class="analytics-card">
              <div class="card-header"><span class="card-title">Select State / UT</span></div>
              <select id="state-tab-selector" class="filter-select" style="width:100%; margin-bottom:10px;" onchange="loadStateElectionStats(this.value)"></select>
              <div id="state-summary-stats" style="display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-bottom:10px;"></div>
              <button class="btn btn-primary" style="width:100%; justify-content:center;" onclick="zoomToSelectedState()">Zoom to State</button>
            </div>
            <div class="analytics-card">
              <div class="card-header"><span class="card-title">State Seat Breakdown</span></div>
              <div style="position:relative; height:180px;"><canvas id="chart-state-seats"></canvas></div>
            </div>
            <div class="analytics-card" style="padding:10px;">
              <div class="card-header"><span class="card-title">Elected MPs in State</span></div>
              <div style="max-height:220px; overflow-y:auto;" id="state-mps-list"></div>
            </div>
          </div>

          <div id="tab-elec-margins" class="sidebar-tab-pane" style="display:none;">
            <div class="analytics-card">
              <div class="card-header"><span class="card-title">Victory Margin Distribution</span></div>
              <div style="position:relative; height:170px;"><canvas id="chart-margin-distribution"></canvas></div>
            </div>
            <div class="analytics-card">
              <div class="card-header"><span class="card-title">Narrowest Wins (Top 10)</span><span class="card-badge" style="background:#fef2f2; color:#b91c1c;">Razor-Thin</span></div>
              <div id="closest-contests-list"></div>
            </div>
            <div class="analytics-card">
              <div class="card-header"><span class="card-title">Widest Landslides (Top 10)</span><span class="card-badge" style="background:#f0fdf4; color:#15803d;">Mega Margins</span></div>
              <div id="highest-margins-list"></div>
            </div>
          </div>
        `;

        renderElectionCharts();
        populateElectionLeaderboard();
        populateStateSelectors();
      } else if (currentMapMode === 'voters') {
        if (mobileTitle) mobileTitle.textContent = 'Voter Turnout Analytics';
        tabsNav.innerHTML = `
          <button class="sidebar-tab-btn active" onclick="switchSidebarTab('tab-voters-overview')">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
            <span>National Turnout</span>
          </button>
          <button class="sidebar-tab-btn" onclick="switchSidebarTab('tab-voters-rankings')">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
            <span>State Rankings</span>
          </button>
        `;

        content.innerHTML = `
          <div id="tab-voters-overview" class="sidebar-tab-pane">
            <div class="analytics-card" style="background:#f0fdf4; border-color:#bbf7d0;">
              <div style="font-size:11px; font-weight:800; color:#15803d; text-transform:uppercase;">National Polling Turnout</div>
              <div style="font-size:24px; font-weight:900; color:#14532d; margin:4px 0;">66.10%</div>
              <div style="font-size:11.5px; color:#166534;">64.64 Crore out of 97.80 Crore registered electors cast their votes.</div>
            </div>

            <div class="analytics-card">
              <div class="card-header"><span class="card-title">Turnout by Gender</span></div>
              <div style="position:relative; height:180px;"><canvas id="chart-voter-gender-national"></canvas></div>
            </div>

            <div class="analytics-card">
              <div class="card-header"><span class="card-title">Constituency Type Turnout</span></div>
              <table class="analytics-table">
                <thead><tr><th>Category</th><th>Seats</th><th>Electors</th><th>Turnout %</th></tr></thead>
                <tbody>
                  <tr><td><b>GEN</b> (General)</td><td>412</td><td>74.2 Cr</td><td><b style="color:#15803d;">65.8%</b></td></tr>
                  <tr><td><b>SC</b> (Scheduled Castes)</td><td>84</td><td>15.4 Cr</td><td><b style="color:#15803d;">67.4%</b></td></tr>
                  <tr><td><b>ST</b> (Scheduled Tribes)</td><td>47</td><td>8.2 Cr</td><td><b style="color:#15803d;">68.1%</b></td></tr>
                </tbody>
              </table>
            </div>

            <div class="analytics-card">
              <div class="card-header"><span class="card-title">NOTA (None of the Above)</span></div>
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <div>
                  <div style="font-size:18px; font-weight:800; color:var(--text-navy);">63,71,839</div>
                  <div style="font-size:10.5px; color:var(--text-muted);">Total NOTA Votes Polled across India (0.99%)</div>
                </div>
                <div style="background:#f1f5f9; padding:6px 10px; border-radius:6px; font-weight:800; color:#475569; font-size:12px;">
                  Rank #1: Indore (2.18L NOTA)
                </div>
              </div>
            </div>
          </div>

          <div id="tab-voters-rankings" class="sidebar-tab-pane" style="display:none;">
            <div class="analytics-card" style="padding:10px;">
              <div class="card-header"><span class="card-title">State-Wise Turnout Leaderboard</span><span class="card-badge">36 States & UTs</span></div>
              <div style="max-height:450px; overflow-y:auto;" id="voters-state-rankings-list"></div>
            </div>
          </div>
        `;

        renderVoterNationalCharts();
        populateVoterStateRankings();
      } else {
        if (mobileTitle) mobileTitle.textContent = 'State Electors Analytics';
        tabsNav.innerHTML = `
          <button class="sidebar-tab-btn active" onclick="switchSidebarTab('tab-electors-overview')">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><line x1="20" y1="8" x2="20" y2="14"/><line x1="23" y1="11" x2="17" y2="11"/></svg>
            <span>Demographics</span>
          </button>
          <button class="sidebar-tab-btn" onclick="switchSidebarTab('tab-electors-rankings')">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
            <span>Elector Rankings</span>
          </button>
        `;

        content.innerHTML = `
          <div id="tab-electors-overview" class="sidebar-tab-pane">
            <div class="analytics-card" style="background:#eff6ff; border-color:#bfdbfe;">
              <div style="font-size:11px; font-weight:800; color:#1d4ed8; text-transform:uppercase;">National Registered Electorate</div>
              <div style="font-size:24px; font-weight:900; color:#1e3a8a; margin:4px 0;">97,79,65,560</div>
              <div style="font-size:11.5px; color:#1e40af;">97.80 Crore Total Electors across 28 States and 8 Union Territories.</div>
            </div>

            <div class="analytics-card">
              <div class="card-header"><span class="card-title">National Elector Categories</span></div>
              <div style="position:relative; height:180px;"><canvas id="chart-elector-categories"></canvas></div>
            </div>

            <div class="analytics-card">
              <div class="card-header"><span class="card-title">Top 5 vs Bottom 5 Elector States</span></div>
              <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:8px;">
                  <div style="font-size:10px; font-weight:800; color:#166534; text-transform:uppercase;">Top 5 Mega States</div>
                  <div style="font-size:11px; line-height:1.6; margin-top:4px;">
                    1. UP (15.4 Cr)<br>
                    2. MH (9.3 Cr)<br>
                    3. BR (7.7 Cr)<br>
                    4. WB (7.6 Cr)<br>
                    5. TN (6.2 Cr)
                  </div>
                </div>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:8px;">
                  <div style="font-size:10px; font-weight:800; color:#991b1b; text-transform:uppercase;">Bottom 5 States/UTs</div>
                  <div style="font-size:11px; line-height:1.6; margin-top:4px;">
                    1. Lakshadweep (57k)<br>
                    2. Ladakh (1.9 L)<br>
                    3. Daman/Diu (3.1 L)<br>
                    4. Andaman (3.1 L)<br>
                    5. Sikkim (4.6 L)
                  </div>
                </div>
              </div>
            </div>

            <div class="analytics-card">
              <div class="card-header"><span class="card-title">Overseas & Service Electors</span></div>
              <table class="analytics-table">
                <tbody>
                  <tr><td><b>Service Electors</b> (Armed Forces)</td><td><b style="color:#2563eb;">19,16,559</b></td></tr>
                  <tr><td><b>Overseas / NRI Electors</b></td><td><b style="color:#059669;">1,19,374</b></td></tr>
                  <tr><td><b>Third Gender Electors</b></td><td><b style="color:#7c3aed;">48,194</b></td></tr>
                </tbody>
              </table>
            </div>
          </div>

          <div id="tab-electors-rankings" class="sidebar-tab-pane" style="display:none;">
            <div class="analytics-card" style="padding:10px;">
              <div class="card-header"><span class="card-title">State Elector Population Table</span><span class="card-badge">36 States</span></div>
              <div style="max-height:450px; overflow-y:auto;" id="electors-state-rankings-list"></div>
            </div>
          </div>
        `;

        renderElectorNationalCharts();
        populateElectorStateRankings();
      }
    }

    function switchSidebarTab(tabId) {
      document.querySelectorAll('.sidebar-tab-btn').forEach(btn => btn.classList.remove('active'));
      const activeBtn = Array.from(document.querySelectorAll('.sidebar-tab-btn')).find(b => b.getAttribute('onclick')?.includes(tabId));
      if (activeBtn) activeBtn.classList.add('active');

      document.querySelectorAll('.sidebar-tab-pane').forEach(p => p.style.display = 'none');
      const targetPane = document.getElementById(tabId);
      if (targetPane) {
        targetPane.style.display = 'flex';
        targetPane.style.flexDirection = 'column';
      }
    }

    /* =====================================================================
       10. RIGHT CONTEXTUAL DETAILS PANEL (MODE SPECIFIC)
       ===================================================================== */
    function closeDetailsPanel() {
      const panel = document.getElementById('sidebar-right');
      if (panel) {
        panel.classList.remove('open');
        panel.classList.add('collapsed');
      }
      const backdrop = document.getElementById('mobile-backdrop');
      if (backdrop) backdrop.classList.remove('active');

      if (selectedPolygonLayer) {
        restoreFeatureStyle(selectedPolygonLayer);
        selectedPolygonLayer = null;
      }
      if (selectedStateLayers.length > 0) {
        selectedStateLayers.forEach(l => restoreFeatureStyle(l));
        selectedStateLayers = [];
      }
      selectedStateName = null;
    }

    // Mode 1: Select Constituency
    function selectConstituencyByRecord(state, pcName) {
      const key = cleanStr(state) + '_' + cleanStr(pcName);
      const data = constituencyIndex.get(key);
      if (!data) return;

      selectedConstituencyKey = key;

      if (geojsonLayer) {
        if (selectedPolygonLayer) restoreFeatureStyle(selectedPolygonLayer);
        geojsonLayer.eachLayer(l => {
          if (l.feature && l.feature.electionData) {
            const lKey = cleanStr(l.feature.electionData.state) + '_' + cleanStr(l.feature.electionData.constituency);
            if (lKey === key) {
              selectedPolygonLayer = l;
              l.setStyle({
                weight: 3.5,
                color: '#0f172a',
                fillOpacity: 0.95
              });
              l.bringToFront();
              leafletMap.flyToBounds(l.getBounds(), { maxZoom: 10, padding: [30, 30], duration: 0.5 });
            }
          }
        });
      }

      renderConstituencyDetailsPanel(data);

      const rightPanel = document.getElementById('sidebar-right');
      rightPanel.classList.remove('collapsed');
      rightPanel.classList.add('open');

      if (window.innerWidth <= 768) {
        document.getElementById('mobile-backdrop').classList.add('active');
      }
    }

    function renderConstituencyDetailsPanel(d) {
      const container = document.getElementById('details-panel-content');
      const winPartyMeta = getPartyMeta(d.winner.party);
      const runPartyMeta = getPartyMeta(d.runnerUp.party);

      let verdictClass = 'comfortable';
      let verdictTitle = 'Comfortable Victory';
      let verdictDesc = `Won by ${d.margin.toLocaleString('en-IN')} votes (${d.marginPct}%)`;

      if (d.uncontested) {
        verdictClass = 'landslide';
        verdictTitle = 'Uncontested Victory (Surat)';
        verdictDesc = 'All other candidate nominations rejected or withdrawn.';
      } else if (d.marginCategory === 'RAZOR') {
        verdictClass = 'narrow';
        verdictTitle = 'Razor-Thin Battleground Win';
      } else if (d.marginCategory === 'LANDSLIDE') {
        verdictClass = 'landslide';
        verdictTitle = 'Massive Landslide Victory';
      }

      container.innerHTML = `
        <div class="details-header">
          <div class="details-title-group">
            <div class="details-badge-row">
              <span class="kpi-chip" style="background:#eff6ff; color:#1d4ed8; font-weight:800;">${d.category}</span>
              <span style="font-size:11px; font-weight:600; color:var(--text-muted);">${d.state} · PC #${d.constNo}</span>
            </div>
            <div class="details-pc-name">${d.constituency}</div>
          </div>
          <button class="btn-close-details" onclick="closeDetailsPanel()">&times;</button>
        </div>

        <div class="verdict-banner ${verdictClass}">
          <div>
            <div style="font-weight:800;">${verdictTitle}</div>
            <div style="font-size:10.5px; opacity:0.9;">${verdictDesc}</div>
          </div>
        </div>

        <div class="candidate-card winner" style="border-left-color:${winPartyMeta.color};">
          <div style="display:flex; justify-content:space-between; align-items:flex-start;">
            <div>
              <div style="font-size:9.5px; font-weight:800; text-transform:uppercase; color:#15803d; letter-spacing:0.04em;">Elected Member of Parliament (Winner)</div>
              <div style="font-size:15px; font-weight:900; color:var(--text-navy); margin:2px 0;">${d.winner.name}</div>
              <div style="font-size:11.5px; font-weight:700; color:${winPartyMeta.color}; display:flex; align-items:center; gap:4px;">
                <span>${d.winner.party}</span> · <span style="color:var(--text-muted); font-size:10.5px;">Symbol: ${winPartyMeta.symbol}</span>
              </div>
            </div>
            <div style="text-align:right;">
              <div style="font-size:16px; font-weight:900; color:var(--text-navy);">${d.winner.votes.toLocaleString('en-IN')}</div>
              <div style="font-size:10.5px; font-weight:700; color:var(--text-muted);">${d.winner.pct}% of votes</div>
            </div>
          </div>
          <div style="display:flex; gap:12px; font-size:10.5px; color:var(--text-muted); margin-top:4px; padding-top:4px; border-top:1px dashed #e2e8f0;">
            <span>Gender: <b>${d.winner.gender}</b></span>
            <span>Category: <b>${d.category}</b></span>
          </div>
        </div>

        <div class="candidate-card runner" style="border-left-color:${runPartyMeta.color};">
          <div style="display:flex; justify-content:space-between; align-items:flex-start;">
            <div>
              <div style="font-size:9.5px; font-weight:800; text-transform:uppercase; color:#b91c1c; letter-spacing:0.04em;">Runner-Up Candidate</div>
              <div style="font-size:13.5px; font-weight:800; color:var(--text-navy); margin:2px 0;">${d.runnerUp.name}</div>
              <div style="font-size:11px; font-weight:700; color:${runPartyMeta.color};">${d.runnerUp.party} · <span style="color:var(--text-muted); font-size:10px;">Symbol: ${runPartyMeta.symbol}</span></div>
            </div>
            <div style="text-align:right;">
              <div style="font-size:14px; font-weight:800; color:var(--text-navy);">${d.runnerUp.votes.toLocaleString('en-IN')}</div>
              <div style="font-size:10px; font-weight:700; color:var(--text-muted);">${d.runnerUp.pct}%</div>
            </div>
          </div>
        </div>

        <div class="analytics-card">
          <div class="card-header"><span class="card-title">Total Valid Votes Polled</span></div>
          <div style="font-size:18px; font-weight:900; color:var(--text-navy);">${d.totalVotes.toLocaleString('en-IN')}</div>
          <div style="height:8px; background:#e2e8f0; border-radius:4px; display:flex; overflow:hidden; margin:8px 0 4px;">
            <div style="background:${winPartyMeta.color}; width:${d.winner.pct}%;"></div>
            <div style="background:${runPartyMeta.color}; width:${d.runnerUp.pct}%;"></div>
          </div>
          <div style="display:flex; justify-content:space-between; font-size:10px; color:var(--text-muted);">
            <span>Winner: ${d.winner.pct}%</span>
            <span>Runner-Up: ${d.runnerUp.pct}%</span>
          </div>
        </div>
      `;
    }

    // Mode 2: Select State Voter Information
    function selectStateVoterInfo(stateName) {
      const normState = normalizeStateName(stateName);
      const vList = votersByState.get(normState) || [];
      const totalRow = vList.find(r => r.type === 'Total') || vList[0];
      if (!totalRow) return;

      selectedStateName = stateName;

      // Highlight all constituencies in this state on the map
      if (geojsonLayer) {
        if (selectedStateLayers.length > 0) {
          selectedStateLayers.forEach(l => restoreFeatureStyle(l));
          selectedStateLayers = [];
        }

        geojsonLayer.eachLayer(l => {
          if (l.feature && l.feature.voterData && normalizeStateName(l.feature.voterData.state) === normState) {
            selectedStateLayers.push(l);
            l.setStyle({ weight: 2.2, color: '#0f172a', fillOpacity: 0.95 });
            l.bringToFront();
          }
        });

        if (selectedStateLayers.length > 0) {
          const group = L.featureGroup(selectedStateLayers);
          leafletMap.flyToBounds(group.getBounds(), { padding: [20, 20], maxZoom: 8, duration: 0.5 });
        }
      }

      renderStateVoterDetailsPanel(totalRow, vList);

      const rightPanel = document.getElementById('sidebar-right');
      rightPanel.classList.remove('collapsed');
      rightPanel.classList.add('open');

      if (window.innerWidth <= 768) {
        document.getElementById('mobile-backdrop').classList.add('active');
      }
    }

    function renderStateVoterDetailsPanel(totalRow, allRows) {
      const container = document.getElementById('details-panel-content');
      const color = getTurnoutColor(totalRow.pollPct);

      let categoryRowsHtml = '';
      allRows.forEach(r => {
        if (r.type === 'Total') return;
        categoryRowsHtml += `
          <tr>
            <td><b>${r.type}</b></td>
            <td>${r.seats}</td>
            <td>${r.electorsTotal.toLocaleString('en-IN')}</td>
            <td>${r.votersTotal.toLocaleString('en-IN')}</td>
            <td><b style="color:${getTurnoutColor(r.pollPct)};">${r.pollPct}%</b></td>
          </tr>
        `;
      });

      container.innerHTML = `
        <div class="details-header">
          <div class="details-title-group">
            <span class="kpi-chip" style="background:#f0fdf4; color:#166534; font-weight:800;">ECI TABLE 10</span>
            <div class="details-pc-name">${totalRow.state}</div>
            <div style="font-size:11.5px; color:var(--text-muted); font-weight:600;">Total Parliamentary Seats: <b>${totalRow.seats}</b></div>
          </div>
          <button class="btn-close-details" onclick="closeDetailsPanel()">&times;</button>
        </div>

        <div style="background:#ffffff; border:2px solid ${color}; border-radius:8px; padding:12px; display:flex; justify-content:space-between; align-items:center;">
          <div>
            <div style="font-size:11px; font-weight:700; color:var(--text-muted); text-transform:uppercase;">State Polling Turnout</div>
            <div style="font-size:24px; font-weight:900; color:#0f172a;">${totalRow.pollPct}%</div>
            <div style="font-size:11px; color:#15803d; font-weight:700;">${totalRow.votersTotal.toLocaleString('en-IN')} Actual Voters</div>
          </div>
          <div style="width:50px; height:50px; border-radius:50%; background:${color}; color:#fff; display:flex; align-items:center; justify-content:center; font-weight:900; font-size:13px;">
            ${totalRow.pollPct}%
          </div>
        </div>

        <div class="analytics-card">
          <div class="card-header"><span class="card-title">Registered Electors vs Actual Voters</span></div>
          <table class="analytics-table">
            <thead><tr><th>Demographic</th><th>Electors</th><th>Voters Polled</th><th>Turnout</th></tr></thead>
            <tbody>
              <tr>
                <td><b>Male</b></td>
                <td>${totalRow.electorsM.toLocaleString('en-IN')}</td>
                <td>${totalRow.votersM.toLocaleString('en-IN')}</td>
                <td><b>${totalRow.electorsM > 0 ? ((totalRow.votersM / totalRow.electorsM) * 100).toFixed(2) : '--'}%</b></td>
              </tr>
              <tr>
                <td><b>Female</b></td>
                <td>${totalRow.electorsF.toLocaleString('en-IN')}</td>
                <td>${totalRow.votersF.toLocaleString('en-IN')}</td>
                <td><b>${totalRow.electorsF > 0 ? ((totalRow.votersF / totalRow.electorsF) * 100).toFixed(2) : '--'}%</b></td>
              </tr>
              <tr>
                <td><b>Third Gender</b></td>
                <td>${totalRow.electorsTG.toLocaleString('en-IN')}</td>
                <td>${totalRow.votersTG.toLocaleString('en-IN')}</td>
                <td><b>${totalRow.electorsTG > 0 ? ((totalRow.votersTG / totalRow.electorsTG) * 100).toFixed(2) : '--'}%</b></td>
              </tr>
              <tr style="background:#f8fafc; font-weight:800;">
                <td>Grand Total</td>
                <td>${totalRow.electorsTotal.toLocaleString('en-IN')}</td>
                <td>${totalRow.votersTotal.toLocaleString('en-IN')}</td>
                <td><b style="color:#15803d;">${totalRow.pollPct}%</b></td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="analytics-card">
          <div class="card-header"><span class="card-title">Male vs Female Voter Distribution</span></div>
          <div style="position:relative; height:180px;"><canvas id="chart-state-voter-gender"></canvas></div>
        </div>

        <div class="analytics-card">
          <div class="card-header"><span class="card-title">Constituency Type Breakdown</span></div>
          <table class="analytics-table">
            <thead><tr><th>Type</th><th>Seats</th><th>Electors</th><th>Voters</th><th>Turnout</th></tr></thead>
            <tbody>${categoryRowsHtml}</tbody>
          </table>
        </div>

        <div class="analytics-card">
          <div class="card-header"><span class="card-title">Postal & NOTA Votes</span></div>
          <div style="display:flex; justify-content:space-between; font-size:12px;">
            <span>Postal Votes: <b>${totalRow.postalVotes.toLocaleString('en-IN')}</b></span>
            <span>NOTA Votes: <b>${totalRow.notaVotes.toLocaleString('en-IN')}</b></span>
          </div>
        </div>
      `;

      // Render chart
      setTimeout(() => {
        const ctx = document.getElementById('chart-state-voter-gender')?.getContext('2d');
        if (ctx) {
          if (chartVoterGender) chartVoterGender.destroy();
          chartVoterGender = new Chart(ctx, {
            type: 'bar',
            data: {
              labels: ['Male', 'Female', 'Third Gender'],
              datasets: [
                { label: 'Electors', data: [totalRow.electorsM, totalRow.electorsF, totalRow.electorsTG], backgroundColor: '#94a3b8' },
                { label: 'Actual Voters', data: [totalRow.votersM, totalRow.votersF, totalRow.votersTG], backgroundColor: '#10b981' }
              ]
            },
            options: {
              responsive: true,
              maintainAspectRatio: false,
              plugins: { legend: { position: 'top', labels: { boxWidth: 10, font: { size: 10 } } } },
              scales: { y: { display: false } }
            }
          });
        }
      }, 100);
    }

    // Mode 3: Select State Elector Information
    function selectStateElectorInfo(stateName) {
      const normState = normalizeStateName(stateName);
      const e = electorsByState.get(normState);
      if (!e) return;

      selectedStateName = stateName;

      // Highlight all constituencies in this state
      if (geojsonLayer) {
        if (selectedStateLayers.length > 0) {
          selectedStateLayers.forEach(l => restoreFeatureStyle(l));
          selectedStateLayers = [];
        }

        geojsonLayer.eachLayer(l => {
          if (l.feature && l.feature.electorData && normalizeStateName(l.feature.electorData.state) === normState) {
            selectedStateLayers.push(l);
            l.setStyle({ weight: 2.2, color: '#0f172a', fillOpacity: 0.95 });
            l.bringToFront();
          }
        });

        if (selectedStateLayers.length > 0) {
          const group = L.featureGroup(selectedStateLayers);
          leafletMap.flyToBounds(group.getBounds(), { padding: [20, 20], maxZoom: 8, duration: 0.5 });
        }
      }

      renderStateElectorDetailsPanel(e);

      const rightPanel = document.getElementById('sidebar-right');
      rightPanel.classList.remove('collapsed');
      rightPanel.classList.add('open');

      if (window.innerWidth <= 768) {
        document.getElementById('mobile-backdrop').classList.add('active');
      }
    }

    function renderStateElectorDetailsPanel(e) {
      const container = document.getElementById('details-panel-content');
      const ratio = e.grandM > 0 ? Math.round((e.grandF / e.grandM) * 1000) : 0;

      container.innerHTML = `
        <div class="details-header">
          <div class="details-title-group">
            <span class="kpi-chip" style="background:#eff6ff; color:#1d4ed8; font-weight:800;">ECI TABLE 9</span>
            <div class="details-pc-name">${e.state}</div>
            <div style="font-size:11.5px; color:var(--text-muted); font-weight:600;">Elector Demographics Intelligence</div>
          </div>
          <button class="btn-close-details" onclick="closeDetailsPanel()">&times;</button>
        </div>

        <div style="background:#ffffff; border:2px solid #2563eb; border-radius:8px; padding:12px; display:flex; justify-content:space-between; align-items:center;">
          <div>
            <div style="font-size:11px; font-weight:700; color:var(--text-muted); text-transform:uppercase;">Grand Total Electorate</div>
            <div style="font-size:22px; font-weight:900; color:#1e3a8a;">${e.grandTotal.toLocaleString('en-IN')}</div>
            <div style="font-size:11px; color:#2563eb; font-weight:700;">${(e.grandTotal / 10000000).toFixed(2)} Crore Citizens</div>
          </div>
          <div style="background:#eff6ff; padding:8px 12px; border-radius:6px; text-align:right;">
            <div style="font-size:9.5px; font-weight:800; color:var(--text-muted); text-transform:uppercase;">Gender Ratio</div>
            <div style="font-size:14px; font-weight:900; color:#1d4ed8;">${ratio} F / 1000 M</div>
          </div>
        </div>

        <div class="analytics-card">
          <div class="card-header"><span class="card-title">Gender Distribution</span></div>
          <div style="position:relative; height:180px;"><canvas id="chart-state-elector-demog"></canvas></div>
        </div>

        <div class="analytics-card">
          <div class="card-header"><span class="card-title">Comprehensive Category Breakdown</span></div>
          <table class="analytics-table">
            <thead><tr><th>Category</th><th>Male</th><th>Female</th><th>TG</th><th>Total</th></tr></thead>
            <tbody>
              <tr>
                <td><b>General</b> (Inc. NRIs)</td>
                <td>${e.genM.toLocaleString('en-IN')}</td>
                <td>${e.genF.toLocaleString('en-IN')}</td>
                <td>${e.genTG.toLocaleString('en-IN')}</td>
                <td><b>${e.genTotal.toLocaleString('en-IN')}</b></td>
              </tr>
              <tr>
                <td><b>Service</b> (Armed Forces)</td>
                <td>${e.serviceM.toLocaleString('en-IN')}</td>
                <td>${e.serviceF.toLocaleString('en-IN')}</td>
                <td>--</td>
                <td><b>${e.serviceTotal.toLocaleString('en-IN')}</b></td>
              </tr>
              <tr>
                <td><b>Overseas / NRIs</b></td>
                <td>${e.nriM.toLocaleString('en-IN')}</td>
                <td>${e.nriF.toLocaleString('en-IN')}</td>
                <td>${e.nriTG.toLocaleString('en-IN')}</td>
                <td><b>${e.nriTotal.toLocaleString('en-IN')}</b></td>
              </tr>
              <tr style="background:#f8fafc; font-weight:800;">
                <td>Grand Total</td>
                <td>${e.grandM.toLocaleString('en-IN')}</td>
                <td>${e.grandF.toLocaleString('en-IN')}</td>
                <td>${e.grandTG.toLocaleString('en-IN')}</td>
                <td><b style="color:#1d4ed8;">${e.grandTotal.toLocaleString('en-IN')}</b></td>
              </tr>
            </tbody>
          </table>
        </div>
      `;

      // Render chart
      setTimeout(() => {
        const ctx = document.getElementById('chart-state-elector-demog')?.getContext('2d');
        if (ctx) {
          if (chartElectorDemog) chartElectorDemog.destroy();
          chartElectorDemog = new Chart(ctx, {
            type: 'doughnut',
            data: {
              labels: ['Male', 'Female', 'Third Gender'],
              datasets: [{
                data: [e.grandM, e.grandF, e.grandTG],
                backgroundColor: ['#2563eb', '#ec4899', '#8b5cf6']
              }]
            },
            options: {
              responsive: true,
              maintainAspectRatio: false,
              plugins: { legend: { position: 'right', labels: { boxWidth: 10, font: { size: 10 } } } }
            }
          });
        }
      }, 100);
    }
    """

