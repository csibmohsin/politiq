# parts/html_layout.py

def get_html_body():
    return """
  <!-- =====================================================================
       PREMIUM CIVIC INTELLIGENCE LOADING SCREEN
       Responsive on PC & Mobile with Live Civic Analytics Ticker
       ===================================================================== -->
  <div class="app-loader" id="app-loader">
    <div class="loader-backdrop"></div>
    <div class="loader-content">
      <!-- Radar Pulse Emblem -->
      <div class="loader-emblem-wrap">
        <div class="loader-radar-pulse"></div>
        <div class="loader-radar-pulse-2"></div>
        <div class="loader-radar-sweep"></div>
        <div class="loader-chakra-emblem">
          <svg viewBox="0 0 24 24" width="40" height="40">
            <circle cx="12" cy="12" r="10" stroke="#38bdf8" stroke-width="1.8" fill="none"/>
            <circle cx="12" cy="12" r="3" fill="#f59e0b"/>
            <line x1="12" y1="2" x2="12" y2="22" stroke="#38bdf8" stroke-width="1.2" opacity="0.6"/>
            <line x1="2" y1="12" x2="22" y2="12" stroke="#38bdf8" stroke-width="1.2" opacity="0.6"/>
            <line x1="4.93" y1="4.93" x2="19.07" y2="19.07" stroke="#38bdf8" stroke-width="1.2" opacity="0.6"/>
            <line x1="4.93" y1="19.07" x2="19.07" y2="4.93" stroke="#38bdf8" stroke-width="1.2" opacity="0.6"/>
          </svg>
        </div>
      </div>

      <!-- Title & Branding -->
      <div class="loader-brand-title">
        POLITIQ <span class="badge-gov">IQ</span>
      </div>
      <div class="loader-brand-sub">Political Intelligence &amp; Information Quotient</div>

      <!-- Progress Section -->
      <div class="loader-progress-box">
        <div class="loader-status-row">
          <span class="loader-status-text" id="loader-status-text">Connecting to Civic Intelligence Repositories...</span>
          <span class="loader-percent" id="loader-percent">0%</span>
        </div>
        <div class="loader-bar-track">
          <div class="loader-bar-fill" id="loader-bar-fill"></div>
        </div>
      </div>

      <!-- Live Civic Intelligence Analytics Ticker -->
      <div class="loader-ticker-card">
        <div class="ticker-header">
          <span class="ticker-dot"></span>
          <span class="ticker-tag">CIVIC INTELLIGENCE BRIEFING</span>
        </div>
        <div class="ticker-quote" id="loader-ticker-quote">
          India's 2024 General Election encompassed 543 Lok Sabha seats with over 64.2 Crore votes cast.
        </div>
      </div>

      <div class="loader-footer-note">
        Official Open Data: Election Commission of India (ECI) &amp; Parliament of India
      </div>
    </div>
  </div>

  <!-- MOBILE BACKDROP OVERLAY -->
  <div class="mobile-backdrop" id="mobile-backdrop"></div>

  <!-- =====================================================================
       TOP APP HEADER
       ===================================================================== -->
  <header class="top-header">
    <div class="brand-group">
      <button class="btn" id="btn-toggle-left" title="Toggle Sidebar">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12h18M3 6h18M3 18h18"/></svg>
      </button>
      <div class="brand-emblem">
        <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" stroke="#000080" stroke-width="2" fill="none"/><circle cx="12" cy="12" r="3" fill="#000080"/></svg>
      </div>
      <div class="brand-titles">
        <div class="brand-name">
          POLITIQ <span class="badge-gov">IQ</span>
        </div>
        <div class="brand-subtitle">Political Intelligence &amp; Information Quotient • Understand Politics Through Data.</div>
      </div>
    </div>

    <!-- Navigation Tabs -->
    <nav class="header-nav-tabs">
      <button class="header-nav-btn active" id="nav-btn-map" onclick="switchMainView('map')">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"/><line x1="8" y1="2" x2="8" y2="18"/><line x1="16" y1="6" x2="16" y2="22"/></svg>
        <span>Map Intelligence</span>
      </button>
      <button class="header-nav-btn" id="nav-btn-bills" onclick="switchMainView('bills')">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
        <span>Legislative Intelligence</span>
        <span class="header-nav-badge">727 Bills</span>
      </button>
      <button class="header-nav-btn" id="nav-btn-sources" onclick="openDataSourcesModal()">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
        <span>Data Sources</span>
      </button>
    </nav>

    <!-- Dynamic National Metrics Bar (Updates according to active mode) -->
    <div class="national-kpis" id="top-national-kpis">
      <!-- Dynamic KPI chips rendered by JS -->
    </div>

    <!-- Header Tools -->
    <div class="header-actions">
      <button class="btn btn-bills-mobile-toggle" id="btn-bills-mobile-header" onclick="switchMainView(currentMainView === 'bills' ? 'map' : 'bills')" title="Toggle Rajya Sabha Bills Passed">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
        <span id="mobile-header-bills-text">Bills Passed</span>
      </button>
      <button class="btn" id="btn-toggle-right" title="Toggle Details Panel">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M15 3v18"/></svg>
      </button>
    </div>
  </header>

  <!-- =====================================================================
       MAIN WORKSPACE
       ===================================================================== -->
  <main class="app-workspace">

    <!-- VIEW 1: MAP INTELLIGENCE (ONE MAP - MULTIPLE MODES) -->
    <section class="view-container" id="view-map">
      
      <!-- LEFT SIDEBAR: ANALYTICS ENGINE -->
      <aside class="sidebar-left collapsed" id="sidebar-left">
        <div class="sidebar-header-mobile">
          <div class="sidebar-header-mobile-title" id="sidebar-mobile-title">POLITIQ Intelligence</div>
          <button class="btn" id="btn-close-sidebar-mobile" style="padding:4px 8px;">&times;</button>
        </div>

        <!-- DATA MODE SELECTOR HUB (Instant touch & desktop segmented switcher) -->
        <div class="sidebar-mobile-mode-hub">
          <div class="mobile-mode-hub-header">
            <span>INTELLIGENCE MODE</span>
            <span class="mode-hub-badge">3 DATASETS</span>
          </div>
          <div class="mobile-mode-btn-group">
            <button class="mobile-mode-btn active" id="mobile-mode-btn-election" onclick="setMapModeFromMobile('election')">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 20V10M12 20V4M6 20v-6"/></svg>
              <span>Elections</span>
            </button>
            <button class="mobile-mode-btn" id="mobile-mode-btn-voters" onclick="setMapModeFromMobile('voters')">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><polyline points="16 11 18 13 22 9"/></svg>
              <span>Turnout</span>
            </button>
            <button class="mobile-mode-btn" id="mobile-mode-btn-electors" onclick="setMapModeFromMobile('electors')">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/></svg>
              <span>Electors</span>
            </button>
          </div>
        </div>

        <!-- LEGISLATIVE INTELLIGENCE / BILLS PASSED LINK IN SIDEBAR -->
        <div class="sidebar-bills-link-banner" onclick="switchMainView('bills'); closeSidebarLeft();">
          <div class="bills-banner-icon">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
          </div>
          <div class="bills-banner-text">
            <div class="bills-banner-title">Rajya Sabha Bills Passed</div>
            <div class="bills-banner-sub">727 Acts Passed (1952–2016)</div>
          </div>
          <span class="bills-banner-action">Open &rarr;</span>
        </div>

        <nav class="sidebar-tabs" id="sidebar-tabs-nav">
          <!-- Dynamically populated per mode -->
        </nav>

        <div class="sidebar-content" id="sidebar-dynamic-content">
          <!-- Dynamically populated analytics per mode -->
        </div>
      </aside>

      <!-- CENTER MAP CONTAINER -->
      <div class="map-container">
        
        <!-- MAP SUBHEADER CONTROLS & VISUALIZATION SELECTOR -->
        <div class="map-subheader" id="map-subheader-bar">
          <div class="map-mode-selector-wrapper">
            <label for="map-mode-select" class="map-mode-label">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
              <span>DATA:</span>
            </label>
            <select id="map-mode-select" class="map-mode-dropdown" onchange="onMapModeChange(this.value)">
              <option value="election" selected>1. Election Results</option>
              <option value="voters">2. Voter Turnout</option>
              <option value="electors">3. State Electors</option>
            </select>
          </div>

          <!-- Mode 1 Filter Tray: Election Results -->
          <div class="filter-tray" id="filter-tray-election">
            <div class="search-wrapper">
              <svg class="search-icon" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
              <input type="text" id="election-search-input" class="search-input" placeholder="Search..." autocomplete="off" />
              <button class="search-clear" id="election-search-clear">&times;</button>
              <div class="search-results-dropdown" id="election-search-dropdown"></div>
            </div>

            <select id="filter-election-state" class="filter-select">
              <option value="ALL">All States (36)</option>
            </select>

            <select id="filter-election-party" class="filter-select">
              <option value="ALL">All Parties</option>
            </select>

            <select id="filter-election-margin" class="filter-select">
              <option value="ALL">All Margins</option>
              <option value="RAZOR">Razor-Thin (< 5k)</option>
              <option value="COMPETITIVE">Competitive (5k - 20k)</option>
              <option value="MODERATE">Moderate (20k - 50k)</option>
              <option value="DECISIVE">Decisive (50k - 100k)</option>
              <option value="LANDSLIDE">Landslide (> 100k)</option>
            </select>

            <select id="filter-election-category" class="filter-select">
              <option value="ALL">All Categories</option>
              <option value="GEN">General (GEN)</option>
              <option value="SC">Scheduled Castes (SC)</option>
              <option value="ST">Scheduled Tribes (ST)</option>
            </select>

            <label class="toggle-labels-container" title="Toggle party badges/flags visibility on map">
              <input type="checkbox" id="toggle-map-labels" checked onchange="toggleMapLabels(this.checked)" />
              <span>Party Labels</span>
            </label>

            <button class="btn-reset-filters" id="btn-reset-election-filters" onclick="resetElectionFilters()">
              <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/></svg>
              Clear
            </button>
          </div>

          <!-- Mode 2 Filter Tray: Voter Information -->
          <div class="filter-tray hidden" id="filter-tray-voters">
            <select id="filter-voter-state" class="filter-select" onchange="onVoterFilterChange()">
              <option value="ALL">All States (36)</option>
            </select>

            <select id="filter-voter-category" class="filter-select" onchange="onVoterFilterChange()">
              <option value="Total">Total (All Seats)</option>
              <option value="GEN">GEN Seats</option>
              <option value="SC">SC Seats</option>
              <option value="ST">ST Seats</option>
            </select>

            <label class="toggle-labels-container" title="Toggle turnout percentage labels on map">
              <input type="checkbox" id="toggle-voter-labels" checked onchange="toggleMapLabels(this.checked)" />
              <span>Turnout Labels</span>
            </label>
          </div>

          <!-- Mode 3 Filter Tray: State-wise Electors -->
          <div class="filter-tray hidden" id="filter-tray-electors">
            <select id="filter-elector-state" class="filter-select" onchange="onElectorFilterChange()">
              <option value="ALL">All States (36)</option>
            </select>

            <select id="filter-elector-metric" class="filter-select" onchange="onElectorFilterChange()">
              <option value="grand_total">Grand Total Electors</option>
              <option value="female">Female Electors</option>
              <option value="service">Service Electors</option>
              <option value="nri">Overseas / NRI Electors</option>
            </select>

            <label class="toggle-labels-container" title="Toggle elector population labels on map">
              <input type="checkbox" id="toggle-elector-labels" checked onchange="toggleMapLabels(this.checked)" />
              <span>Elector Labels</span>
            </label>
          </div>
        </div>

        <!-- LEAFLET MAP ELEMENT -->
        <div id="india-map"></div>

        <!-- Floating Map Control Tools -->
        <div class="map-tools-top">
          <button class="map-tool-btn" id="btn-fit-india" onclick="fitMapToIndia()" title="Reset View to India">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
          </button>
          <button class="map-tool-btn" id="btn-toggle-legend" onclick="toggleMapLegend()" title="Toggle Legend">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
          </button>
        </div>

        <!-- Floating Dynamic Mode Legend -->
        <div class="map-legend-card" id="map-legend-card">
          <div class="legend-title" id="legend-title-box">
            <span id="legend-title-text">Major Parties</span>
            <span style="font-size:10px; color:var(--text-muted);" id="legend-subtitle-text">2024</span>
          </div>
          <div id="legend-content-box">
            <!-- Dynamically populated per mode -->
          </div>
        </div>

        <!-- Bottom Credit Bar -->
        <div class="bottom-credit-container">
          <div class="bottom-credit-pill">
            <span class="source-badge">
              <span class="source-full">Source: <b>ECI &amp; Rajya Sabha</b></span>
              <span class="source-short"><b>ECI &amp; RS</b></span>
            </span>
            <span class="credit-sep credit-sep-brand">•</span>
            <span class="credit-brand-name">POLITIQ</span>
            <span class="credit-sep">•</span>
            <a href="https://www.instagram.com/csib.mohsin/" target="_blank" rel="noopener noreferrer" class="dev-link" title="Follow Mohsin Khawaja on Instagram">
              <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
              <span>Dev By <b>Mohsin Khawaja</b> <span class="handle-text">(@csib.mohsin)</span></span>
            </a>
          </div>
        </div>

      </div>

      <!-- RIGHT DETAILS PANEL -->
      <aside class="sidebar-right collapsed" id="sidebar-right">
        <div class="mobile-handle-bar" onclick="closeDetailsPanel()"></div>
        <div class="details-body" id="details-panel-content">
          <!-- Dynamically populated on selection -->
        </div>
      </aside>

    </section>

    <!-- VIEW 2: LEGISLATIVE INTELLIGENCE (DEDICATED BILLS EXPLORER) -->
    <section class="view-container hidden" id="view-bills">
      <div class="view-bills-workspace">
        
        <!-- Header Banner -->
        <div class="bills-header-banner">
          <div>
            <div class="bills-header-title">📜 Rajya Sabha Legislative Intelligence</div>
            <div class="bills-header-subtitle">Search, track, and inspect 727 parliamentary bills passed and assented into law (1952 – 2016)</div>
          </div>
          <div class="bills-header-kpis">
            <div class="bills-header-kpi-box">
              <div class="bills-header-kpi-val" id="bills-stat-total">727</div>
              <div class="bills-header-kpi-label">Bills Enacted</div>
            </div>
            <div class="bills-header-kpi-box">
              <div class="bills-header-kpi-val">64 Years</div>
              <div class="bills-header-kpi-label">1952 – 2016</div>
            </div>
            <div class="bills-header-kpi-box">
              <div class="bills-header-kpi-val">100%</div>
              <div class="bills-header-kpi-label">Assented</div>
            </div>
          </div>
        </div>

        <!-- Controls & Filters Bar -->
        <div class="bills-controls-bar">
          <div class="bills-filter-group">
            <div class="search-wrapper" style="width: 280px;">
              <svg class="search-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
              <input type="text" id="bill-search-input" class="search-input" placeholder="Search bill title, number, act..." oninput="onBillFilterChange()" autocomplete="off" />
            </div>

            <div class="decade-pills" id="decade-pills-container">
              <button class="decade-pill-btn active" data-decade="ALL" onclick="selectDecade('ALL')">All Decades</button>
              <button class="decade-pill-btn" data-decade="2010" onclick="selectDecade('2010')">2010s</button>
              <button class="decade-pill-btn" data-decade="2000" onclick="selectDecade('2000')">2000s</button>
              <button class="decade-pill-btn" data-decade="1990" onclick="selectDecade('1990')">1990s</button>
              <button class="decade-pill-btn" data-decade="1980" onclick="selectDecade('1980')">1980s</button>
              <button class="decade-pill-btn" data-decade="1970" onclick="selectDecade('1970')">1970s</button>
              <button class="decade-pill-btn" data-decade="1960" onclick="selectDecade('1960')">1960s</button>
              <button class="decade-pill-btn" data-decade="1950" onclick="selectDecade('1950')">1950s</button>
            </div>
          </div>

          <div class="bills-filter-group">
            <select id="bill-year-select" class="filter-select" onchange="onBillFilterChange()">
              <option value="ALL">All Years (1952–2016)</option>
            </select>

            <select id="bill-sort-select" class="filter-select" onchange="onBillFilterChange()">
              <option value="newest">Newest Year First</option>
              <option value="oldest">Oldest Year First</option>
              <option value="title">Bill Title (A–Z)</option>
            </select>

            <span id="bills-count-badge" class="badge-year" style="font-size:11px;">Showing 727 Bills</span>
          </div>
        </div>

        <!-- Bills Cards Grid Container -->
        <div class="bills-grid-container" id="bills-grid-container">
          <!-- Dynamically populated bill cards -->
        </div>

      </div>
    </section>

  </main>

  <!-- =====================================================================
       ANIMATED BILL TIMELINE & DOSSIER MODAL
       ===================================================================== -->
  <div class="modal-overlay" id="bill-timeline-modal">
    <div class="modal-card">
      <div class="modal-header">
        <div>
          <div style="font-size:11px; font-weight:800; color:var(--accent-blue); text-transform:uppercase; margin-bottom:4px;">Legislative Bill Intelligence Dossier</div>
          <div class="bill-title" id="modal-bill-title" style="font-size:16px;"></div>
          <div class="bill-badge-group" style="margin-top:8px;" id="modal-bill-badges"></div>
        </div>
        <button class="btn" onclick="closeBillModal()" style="padding:4px 10px; font-size:18px;">&times;</button>
      </div>

      <div class="modal-body">
        
        <!-- Animated 5-Stage Stepper Timeline -->
        <div class="timeline-container">
          <div class="timeline-title">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
            <span>Legislative Passage Timeline (Animated Milestones)</span>
          </div>

          <div class="timeline-stepper">
            <div class="timeline-track-bg"></div>
            <div class="timeline-track-fill" id="timeline-fill-bar"></div>

            <!-- Milestone 1: Introduced -->
            <div class="timeline-step completed" id="step-1" onclick="showMilestoneDetail('intro')">
              <div class="timeline-node">1</div>
              <div class="timeline-step-label">Bill Introduced</div>
              <div class="timeline-step-date" id="step-intro-date">--</div>
              <div class="timeline-step-status" id="step-intro-status">Completed</div>
            </div>

            <!-- Milestone 2: Passed in Rajya Sabha -->
            <div class="timeline-step completed" id="step-2" onclick="showMilestoneDetail('rs')">
              <div class="timeline-node">2</div>
              <div class="timeline-step-label">Rajya Sabha</div>
              <div class="timeline-step-date" id="step-rs-date">--</div>
              <div class="timeline-step-status" id="step-rs-status">Passed</div>
            </div>

            <!-- Milestone 3: Passed in Lok Sabha -->
            <div class="timeline-step completed" id="step-3" onclick="showMilestoneDetail('ls')">
              <div class="timeline-node">3</div>
              <div class="timeline-step-label">Lok Sabha</div>
              <div class="timeline-step-date" id="step-ls-date">--</div>
              <div class="timeline-step-status" id="step-ls-status">Passed</div>
            </div>

            <!-- Milestone 4: Committee Review -->
            <div class="timeline-step bypassed" id="step-4" onclick="showMilestoneDetail('committee')">
              <div class="timeline-node">4</div>
              <div class="timeline-step-label">Committee</div>
              <div class="timeline-step-date" id="step-comm-date">Not Available</div>
              <div class="timeline-step-status" id="step-comm-status">Bypassed/NA</div>
            </div>

            <!-- Milestone 5: Presidential Assent -->
            <div class="timeline-step completed" id="step-5" onclick="showMilestoneDetail('assent')">
              <div class="timeline-node">5</div>
              <div class="timeline-step-label">Presidential Assent</div>
              <div class="timeline-step-date" id="step-assent-date">--</div>
              <div class="timeline-step-status" id="step-assent-status">Enacted</div>
            </div>
          </div>
        </div>

        <!-- Google Search Button Section -->
        <div class="google-search-section">
          <div class="google-search-info">
            <span style="font-size:10px; font-weight:700; color:var(--accent-blue); text-transform:uppercase;">Official Research Query</span>
            <div class="google-search-bill-title" id="google-search-title-display"></div>
            <div class="google-search-desc">Open an authoritative Google query targeting Indian Parliamentary records, debates, and official gazette notifications.</div>
          </div>
          <button class="btn-google-search" id="btn-google-search-action">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/><path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/><path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z" fill="#FBBC05"/><path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z" fill="#EA4335"/></svg>
            <span>Search This Bill on Google</span>
          </button>
        </div>

        <!-- Full Legislative Bill Dossier Table -->
        <div class="analytics-card" style="padding:16px;">
          <div class="card-header">
            <span class="card-title">Complete Parliamentary Records</span>
          </div>
          <table class="bill-full-table" id="modal-bill-table"></table>
        </div>

      </div>
    </div>
  </div>

  <!-- =====================================================================
       DATA SOURCES & AUDIT MODAL
       ===================================================================== -->
  <div class="modal-overlay" id="sources-modal">
    <div class="modal-card" style="max-width: 600px;">
      <div class="modal-header">
        <div>
          <div style="font-size:11px; font-weight:800; color:var(--accent-blue); text-transform:uppercase;">Official Data Sources</div>
          <div style="font-size:16px; font-weight:800; color:var(--text-navy);">POLITIQ Provenance</div>
        </div>
        <button class="btn" onclick="closeDataSourcesModal()" style="padding:4px 10px; font-size:18px;">&times;</button>
      </div>
      <div class="modal-body" style="padding:20px;">
        
        <div style="background:#f0fdf4; border:1px solid #bbf7d0; border-radius:8px; padding:16px; display:flex; align-items:flex-start; gap:12px; margin-bottom:14px;">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#16a34a" stroke-width="2" style="flex-shrink:0; margin-top:2px;"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
          <div>
            <div style="font-weight:800; color:#15803d; font-size:14px; margin-bottom:4px;">Official Election Commission of India (ECI) Records</div>
            <div style="color:#166534; font-size:13px; line-height:1.5;">
              All election results, voter turnout statistics, and elector demographics are sourced directly from the <b>Election Commission of India (ECI)</b>.
            </div>
          </div>
        </div>

        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:16px; display:flex; align-items:flex-start; gap:12px;">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2" style="flex-shrink:0; margin-top:2px;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
          <div>
            <div style="font-weight:800; color:#1e40af; font-size:14px; margin-bottom:4px;">Rajya Sabha Secretariat Records</div>
            <div style="color:#334155; font-size:13px; line-height:1.5;">
              Legislative intelligence records and bill enactment histories are sourced from the <b>Rajya Sabha Secretariat</b> (Parliament of India).
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>

  <!-- =====================================================================
       MOBILE BOTTOM DOCK (TOUCH FRIENDLY)
       ===================================================================== -->
  <nav class="mobile-bottom-dock">
    <button class="dock-item-btn active" id="dock-btn-map" onclick="handleMobileDockClick('map')">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"/><line x1="8" y1="2" x2="8" y2="18"/><line x1="16" y1="6" x2="16" y2="22"/></svg>
      <span>Map View</span>
    </button>
    <button class="dock-item-btn" id="dock-btn-analytics" onclick="handleMobileDockClick('analytics')">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 20V10M12 20V4M6 20v-6"/></svg>
      <span>Analytics</span>
    </button>
    <button class="dock-item-btn" id="dock-btn-bills" onclick="handleMobileDockClick('bills')">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
      <span>Bills Passed</span>
    </button>
    <button class="dock-item-btn" id="dock-btn-details" onclick="handleMobileDockClick('details')">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M15 3v18"/></svg>
      <span>Details</span>
    </button>
  </nav>
    """

