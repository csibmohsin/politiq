# parts/styles.py

def get_css():
    return """
    /* =====================================================================
       CSS DESIGN SYSTEM - BHARAT CIVICLENS GOVERNMENT-GRADE INTELLIGENCE UI
       ===================================================================== */
    :root {
      --bg-canvas: #f8fafc;
      --bg-panel: #ffffff;
      --bg-subtle: #f1f5f9;
      --border-subtle: #e2e8f0;
      --border-focus: #94a3b8;
      --text-navy: #0f172a;
      --text-body: #334155;
      --text-muted: #64748b;
      --accent-saffron: #f97316;
      --accent-blue: #2563eb;
      --accent-green: #16a34a;
      --accent-emerald: #10b981;
      --accent-indigo: #4f46e5;
      --accent-red: #dc2626;
      --shadow-sm: 0 1px 2px 0 rgba(15, 23, 42, 0.05);
      --shadow-md: 0 4px 6px -1px rgba(15, 23, 42, 0.07), 0 2px 4px -2px rgba(15, 23, 42, 0.05);
      --shadow-lg: 0 10px 15px -3px rgba(15, 23, 42, 0.08), 0 4px 6px -4px rgba(15, 23, 42, 0.04);
      --shadow-bottom-sheet: 0 -10px 25px -5px rgba(15, 23, 42, 0.15), 0 -5px 10px -5px rgba(15, 23, 42, 0.08);
      --radius-sm: 6px;
      --radius-md: 8px;
      --radius-lg: 14px;
      --radius-full: 9999px;
      --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Inter", Helvetica, Arial, sans-serif;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }

    body {
      font-family: var(--font-sans);
      background-color: var(--bg-canvas);
      color: var(--text-body);
      height: 100vh;
      height: 100dvh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      -webkit-font-smoothing: antialiased;
    }

    ::-webkit-scrollbar { width: 5px; height: 5px; }
    ::-webkit-scrollbar-track { background: var(--bg-subtle); }
    ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: #94a3b8; }

    /* =====================================================================
       TOP HEADER & NAVIGATION
       ===================================================================== */
    .top-header {
      height: 58px;
      background: var(--bg-panel);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 16px;
      z-index: 1100;
      box-shadow: var(--shadow-sm);
      flex-shrink: 0;
      gap: 12px;
    }

    .brand-group {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-shrink: 0;
    }

    .brand-emblem {
      width: 34px;
      height: 34px;
      background: linear-gradient(135deg, #ff9933 0%, #ffffff 50%, #138808 100%);
      border: 1px solid #cbd5e1;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
      flex-shrink: 0;
    }

    .brand-emblem svg { width: 22px; height: 22px; }

    .brand-titles { display: flex; flex-direction: column; }
    .brand-name {
      font-size: 15px;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: var(--text-navy);
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .brand-name .badge-gov {
      font-size: 9px;
      font-weight: 800;
      padding: 1px 6px;
      background: #eff6ff;
      color: var(--accent-blue);
      border: 1px solid #bfdbfe;
      border-radius: var(--radius-full);
      letter-spacing: 0.05em;
    }
    .brand-subtitle {
      font-size: 10.5px;
      font-weight: 500;
      color: var(--text-muted);
      letter-spacing: -0.01em;
    }

    /* Navigation Tabs */
    .header-nav-tabs {
      display: flex;
      align-items: center;
      gap: 4px;
      background: var(--bg-subtle);
      padding: 3px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-subtle);
    }
    .header-nav-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      font-size: 12.5px;
      font-weight: 600;
      color: var(--text-body);
      background: none;
      border: none;
      border-radius: var(--radius-sm);
      cursor: pointer;
      transition: all 0.15s ease;
      white-space: nowrap;
    }
    .header-nav-btn:hover { color: var(--text-navy); background: rgba(255,255,255,0.7); }
    .header-nav-btn.active {
      background: #ffffff;
      color: var(--accent-blue);
      box-shadow: 0 1px 3px rgba(15,23,42,0.08);
      font-weight: 700;
    }
    .header-nav-badge {
      font-size: 10px;
      padding: 1px 5px;
      background: #eff6ff;
      color: var(--accent-blue);
      border-radius: var(--radius-full);
      font-weight: 700;
    }

    /* National KPI Bar */
    .national-kpis {
      display: flex;
      align-items: center;
      gap: 8px;
      overflow-x: auto;
    }
    .kpi-chip {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      background: var(--bg-subtle);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-full);
      padding: 3px 10px;
      font-size: 11px;
      font-weight: 600;
      white-space: nowrap;
      color: var(--text-navy);
    }
    .kpi-chip .kpi-label { color: var(--text-muted); font-size: 10px; text-transform: uppercase; letter-spacing: 0.04em; }
    .kpi-chip .kpi-val { font-weight: 800; }
    .kpi-chip.nda { background: #fff7ed; border-color: #fed7aa; color: #c2410c; }
    .kpi-chip.india { background: #eff6ff; border-color: #bfdbfe; color: #1d4ed8; }
    .kpi-chip.others { background: #f8fafc; border-color: #cbd5e1; color: #475569; }
    .kpi-chip.turnout { background: #f0fdf4; border-color: #bbf7d0; color: #15803d; }
    .kpi-chip.bills { background: #faf5ff; border-color: #e9d5ff; color: #7e22ce; }

    /* Header Actions */
    .header-actions {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-shrink: 0;
    }
    .btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 12px;
      font-size: 12px;
      font-weight: 600;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-subtle);
      background: var(--bg-panel);
      color: var(--text-navy);
      cursor: pointer;
      transition: all 0.15s ease;
      white-space: nowrap;
    }
    .btn:hover { background: var(--bg-subtle); border-color: #cbd5e1; }
    .btn-primary { background: var(--accent-blue); color: #ffffff; border-color: var(--accent-blue); }
    .btn-primary:hover { background: #1d4ed8; border-color: #1d4ed8; }

    /* =====================================================================
       MAP VIEW SUBHEADER & MODE CONTROLS (COMPACT & SLEEK)
       ===================================================================== */
    .map-subheader {
      background: var(--bg-panel);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 5px 12px;
      z-index: 1000;
      flex-shrink: 0;
      overflow-x: auto;
      white-space: nowrap;
      -webkit-overflow-scrolling: touch;
    }

    .map-mode-selector-wrapper {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-shrink: 0;
    }

    .map-mode-label {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-size: 10px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--accent-blue);
    }

    .map-mode-dropdown {
      height: 28px;
      padding: 0 8px;
      border-radius: var(--radius-sm);
      border: 1.5px solid var(--accent-blue);
      font-size: 11px;
      font-weight: 700;
      font-family: inherit;
      color: var(--text-navy);
      background: #eff6ff;
      outline: none;
      cursor: pointer;
      max-width: 220px;
    }
    .map-mode-dropdown:focus { box-shadow: 0 0 0 2px rgba(37,99,235,0.25); }

    .map-mode-desc-pill {
      font-size: 10px;
      color: var(--text-muted);
      background: var(--bg-subtle);
      padding: 2px 8px;
      border-radius: var(--radius-full);
      border: 1px solid var(--border-subtle);
      white-space: nowrap;
    }

    /* Filter trays inside subheader */
    .filter-tray {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-shrink: 0;
    }
    .filter-tray.hidden { display: none !important; }

    .search-wrapper {
      position: relative;
      width: 170px;
      min-width: 120px;
      flex-shrink: 0;
    }
    .search-input {
      width: 100%;
      height: 28px;
      padding: 0 24px 0 26px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-subtle);
      font-size: 11px;
      font-family: inherit;
      color: var(--text-navy);
      background: var(--bg-canvas);
      outline: none;
      transition: border-color 0.15s, box-shadow 0.15s;
    }
    .search-input:focus { border-color: var(--accent-blue); box-shadow: 0 0 0 2px rgba(37,99,235,0.15); background:#fff; }
    .search-icon { position: absolute; left: 8px; top: 7px; color: var(--text-muted); pointer-events: none; }
    .search-clear { position: absolute; right: 6px; top: 6px; background: none; border: none; color: var(--text-muted); cursor: pointer; display: none; font-size: 13px; }
    .search-clear:hover { color: var(--text-navy); }

    .search-results-dropdown {
      position: absolute;
      top: 32px;
      left: 0;
      width: 280px;
      max-height: 320px;
      overflow-y: auto;
      background: #ffffff;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-lg);
      z-index: 2100;
      display: none;
    }
    .search-result-item {
      padding: 7px 10px;
      border-bottom: 1px solid #f1f5f9;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .search-result-item:hover { background: #f8fafc; }

    .filter-select {
      height: 28px;
      padding: 0 8px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-subtle);
      font-size: 11px;
      font-weight: 600;
      font-family: inherit;
      color: var(--text-navy);
      background: var(--bg-canvas);
      outline: none;
      cursor: pointer;
      flex-shrink: 0;
    }
    .filter-select:focus { border-color: var(--accent-blue); }

    .toggle-labels-container {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      background: var(--bg-canvas);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 0 8px;
      height: 28px;
      cursor: pointer;
      user-select: none;
      flex-shrink: 0;
      font-size: 11px;
      font-weight: 700;
      color: var(--text-navy);
    }
    .toggle-labels-container:hover { border-color: #cbd5e1; background: #ffffff; }

    .btn-reset-filters {
      height: 28px;
      padding: 0 8px;
      background: none;
      border: 1px solid transparent;
      color: var(--accent-red);
      font-size: 11px;
      font-weight: 600;
      cursor: pointer;
      border-radius: var(--radius-sm);
      white-space: nowrap;
      display: inline-flex;
      align-items: center;
      gap: 3px;
    }
    .btn-reset-filters:hover { background: #fef2f2; border-color: #fecaca; }

    /* Segmented Mode Hub in Sidebar */
    .sidebar-mobile-mode-hub {
      padding: 8px 12px;
      background: #f8fafc;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      flex-direction: column;
      gap: 5px;
      flex-shrink: 0;
    }
    .mobile-mode-hub-header {
      font-size: 9px;
      font-weight: 800;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.06em;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .mode-hub-badge {
      font-size: 8px;
      font-weight: 800;
      background: #e2e8f0;
      color: #475569;
      padding: 1px 5px;
      border-radius: 4px;
    }
    .mobile-mode-btn-group {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 3px;
      background: #e2e8f0;
      padding: 3px;
      border-radius: 7px;
    }
    .mobile-mode-btn {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 5px;
      padding: 6px 4px;
      border-radius: 5px;
      border: none;
      background: transparent;
      color: #475569;
      font-size: 11px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.15s ease;
      white-space: nowrap;
    }
    .mobile-mode-btn:hover {
      color: var(--text-navy);
      background: rgba(255, 255, 255, 0.6);
    }
    .mobile-mode-btn.active {
      background: #ffffff;
      color: var(--accent-blue);
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
      font-weight: 800;
    }
    .mobile-mode-btn.active svg {
      stroke: var(--accent-blue);
    }

    /* =====================================================================
       MAIN WORKSPACES (MAP VIEW & LEGISLATIVE VIEW)
       ===================================================================== */
    .app-workspace {
      flex: 1;
      display: flex;
      position: relative;
      overflow: hidden;
      min-height: 0;
    }
    .view-container {
      width: 100%;
      height: 100%;
      display: flex;
      position: relative;
    }
    .view-container.hidden { display: none !important; }

    /* LEFT SIDEBAR - ANALYTICS ENGINE */
    .sidebar-left {
      width: 380px;
      min-width: 380px;
      background: var(--bg-panel);
      border-right: 1px solid var(--border-subtle);
      display: flex;
      flex-direction: column;
      z-index: 500;
      transition: transform 0.25s ease, margin-left 0.25s ease;
      box-shadow: var(--shadow-sm);
    }
    .sidebar-left.collapsed { margin-left: -380px; }

    .sidebar-header-mobile {
      display: none;
      padding: 12px 16px;
      border-bottom: 1px solid var(--border-subtle);
      align-items: center;
      justify-content: space-between;
      background: #ffffff;
    }
    .sidebar-header-mobile-title { font-size: 13.5px; font-weight: 700; color: var(--text-navy); }

    .sidebar-tabs {
      display: flex;
      background: var(--bg-subtle);
      border-bottom: 1px solid var(--border-subtle);
      padding: 4px 8px 0;
      gap: 4px;
      flex-shrink: 0;
      overflow-x: auto;
    }
    .sidebar-tab-btn {
      flex: 1;
      padding: 8px 10px;
      border: none;
      background: none;
      font-size: 11.5px;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      border-radius: var(--radius-sm) var(--radius-sm) 0 0;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      white-space: nowrap;
      transition: all 0.15s ease;
    }
    .sidebar-tab-btn:hover { color: var(--text-navy); background: rgba(255,255,255,0.6); }
    .sidebar-tab-btn.active {
      color: var(--accent-blue);
      background: var(--bg-panel);
      font-weight: 800;
      border-top: 2px solid var(--accent-blue);
    }

    .sidebar-content {
      flex: 1;
      overflow-y: auto;
      overflow-x: hidden;
      padding: 12px 14px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      box-sizing: border-box;
    }

    .sidebar-tab-pane {
      display: flex;
      flex-direction: column !important;
      gap: 12px;
      width: 100%;
      min-width: 0;
      box-sizing: border-box;
    }

    /* Analytics Cards */
    .analytics-card {
      background: #ffffff;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 12px 14px;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
      width: 100%;
      box-sizing: border-box;
      min-width: 0;
      overflow: hidden;
    }
    .card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 10px;
    }
    .card-title { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.03em; color: var(--text-navy); }
    .card-badge { font-size: 10px; font-weight: 700; padding: 2px 7px; background: var(--bg-subtle); color: var(--text-muted); border-radius: var(--radius-full); }

    /* Majority Meter */
    .majority-meter-container { display: flex; flex-direction: column; gap: 6px; }
    .majority-scale-header { display: flex; justify-content: space-between; font-size: 11px; font-weight: 700; }
    .majority-track {
      position: relative;
      height: 18px;
      background: #e2e8f0;
      border-radius: var(--radius-full);
      display: flex;
      overflow: hidden;
    }
    .majority-segment { height: 100%; transition: width 0.3s ease; }
    .majority-target-line {
      position: absolute;
      top: -2px;
      bottom: -2px;
      left: 50.09%;
      width: 2px;
      background: #0f172a;
      z-index: 10;
    }
    .majority-target-label {
      position: absolute;
      top: -18px;
      left: 50.09%;
      transform: translateX(-50%);
      font-size: 9px;
      font-weight: 800;
      color: #0f172a;
    }

    /* Analytics Table */
    .analytics-table { width: 100%; border-collapse: collapse; font-size: 11px; }
    .analytics-table th { text-align: left; padding: 6px 8px; font-weight: 700; color: var(--text-muted); border-bottom: 1px solid var(--border-subtle); }
    .analytics-table td { padding: 6px 8px; border-bottom: 1px solid #f8fafc; color: var(--text-body); }
    .analytics-table tr:hover { background: #f8fafc; }

    /* CENTER MAP CANVAS */
    .map-container {
      flex: 1;
      display: flex;
      flex-direction: column;
      position: relative;
      background: #f1f5f9;
      overflow: hidden;
      min-height: 0;
      height: 100%;
    }
    #india-map {
      flex: 1;
      width: 100%;
      height: 100%;
      min-height: 0;
      background: #f1f5f9;
    }

    /* Map Tool Buttons */
    .map-tools-top {
      position: absolute;
      top: 48px;
      right: 12px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      z-index: 800;
    }
    .map-tool-btn {
      width: 34px;
      height: 34px;
      background: rgba(255, 255, 255, 0.95);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      color: var(--text-navy);
      box-shadow: var(--shadow-md);
      transition: all 0.15s ease;
    }
    .map-tool-btn:hover { background: #ffffff; color: var(--accent-blue); }
    .map-tool-btn.active { background: #eff6ff; color: var(--accent-blue); border-color: var(--accent-blue); }

    /* Floating Legend Card */
    .map-legend-card {
      position: absolute;
      bottom: 24px;
      left: 16px;
      background: rgba(255, 255, 255, 0.95);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 10px 14px;
      z-index: 800;
      box-shadow: var(--shadow-lg);
      max-width: 250px;
    }
    .legend-title {
      font-size: 11px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: var(--text-navy);
      margin-bottom: 6px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .legend-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 4px 10px;
      font-size: 10.5px;
    }
    .legend-item { display: flex; align-items: center; gap: 6px; }
    .legend-color-dot { width: 10px; height: 10px; border-radius: 2px; flex-shrink: 0; }
    .legend-scale-bar {
      display: flex;
      height: 10px;
      border-radius: 4px;
      overflow: hidden;
      margin: 6px 0 4px;
    }
    .legend-scale-labels {
      display: flex;
      justify-content: space-between;
      font-size: 9.5px;
      font-weight: 600;
      color: var(--text-muted);
    }

    /* Attribution Bar */
    .bottom-credit-container {
      position: absolute;
      bottom: 10px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 800;
      pointer-events: auto;
    }
    .bottom-credit-pill {
      background: rgba(255, 255, 255, 0.92);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-full);
      padding: 4px 14px;
      font-size: 11px;
      font-weight: 500;
      color: var(--text-muted);
      box-shadow: var(--shadow-sm);
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .dev-link { color: var(--text-navy); text-decoration: none; font-weight: 700; display: inline-flex; align-items: center; gap: 4px; }
    .dev-link:hover { color: #e1306c; }
    .source-short { display: none; }
    .source-full { display: inline; }

    /* RIGHT CONTEXTUAL DETAILS PANEL */
    .sidebar-right {
      width: 380px;
      min-width: 380px;
      background: var(--bg-panel);
      border-left: 1px solid var(--border-subtle);
      display: flex;
      flex-direction: column;
      z-index: 500;
      transition: transform 0.25s ease, margin-right 0.25s ease;
      box-shadow: var(--shadow-sm);
      overflow-y: auto;
    }
    .sidebar-right.collapsed { margin-right: -380px; }

    .details-body { padding: 16px; display: flex; flex-direction: column; gap: 14px; }
    .details-header {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 10px;
    }
    .details-title-group { display: flex; flex-direction: column; gap: 2px; }
    .details-badge-row { display: flex; align-items: center; gap: 6px; }
    .details-pc-name { font-size: 17px; font-weight: 800; color: var(--text-navy); }
    .btn-close-details { background: none; border: none; font-size: 20px; color: var(--text-muted); cursor: pointer; padding: 2px 6px; }
    .btn-close-details:hover { color: var(--text-navy); }

    .details-empty-state {
      padding: 40px 20px;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 12px;
      color: var(--text-muted);
    }
    .details-empty-icon { width: 44px; height: 44px; stroke: #94a3b8; }
    .details-empty-title { font-size: 14px; font-weight: 700; color: var(--text-navy); }
    .details-empty-desc { font-size: 12px; line-height: 1.5; }

    /* Candidate cards in details */
    .candidate-card {
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 12px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      position: relative;
    }
    .candidate-card.winner { background: #fafafa; border-left: 4px solid var(--accent-saffron); }
    .candidate-card.runner { background: #ffffff; border-left: 4px solid #94a3b8; }

    .verdict-banner {
      padding: 8px 12px;
      border-radius: var(--radius-sm);
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 12px;
      font-weight: 700;
    }
    .verdict-banner.comfortable { background: #f0fdf4; color: #166534; border: 1px solid #bbf7d0; }
    .verdict-banner.landslide { background: #ecfdf5; color: #065f46; border: 1px solid #a7f3d0; }
    .verdict-banner.narrow { background: #fef2f2; color: #991b1b; border: 1px solid #fecaca; }

    .btn-bills-mobile-toggle { display: none; }
    
    .sidebar-bills-link-banner {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 9px 12px;
      background: linear-gradient(135deg, #1e1b4b 0%, #1e293b 100%);
      color: #ffffff;
      cursor: pointer;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      transition: background 0.15s ease;
      flex-shrink: 0;
    }
    .sidebar-bills-link-banner:hover {
      background: linear-gradient(135deg, #312e81 0%, #334155 100%);
    }
    .bills-banner-icon {
      width: 26px;
      height: 26px;
      border-radius: 6px;
      background: rgba(255, 255, 255, 0.15);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      color: #60a5fa;
    }
    .bills-banner-text {
      flex: 1;
      min-width: 0;
    }
    .bills-banner-title {
      font-size: 11px;
      font-weight: 800;
      color: #ffffff;
      line-height: 1.2;
    }
    .bills-banner-sub {
      font-size: 9.5px;
      color: #94a3b8;
      line-height: 1.2;
    }
    .bills-banner-action {
      font-size: 9.5px;
      font-weight: 800;
      color: #60a5fa;
      background: rgba(96, 165, 250, 0.15);
      padding: 2px 6px;
      border-radius: 4px;
      white-space: nowrap;
    }

    /* =====================================================================
       LEGISLATIVE INTELLIGENCE VIEW (DEDICATED BILLS EXPLORER)
       ===================================================================== */
    .view-bills-workspace {
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      background: var(--bg-canvas);
      overflow: hidden;
    }

    .bills-header-banner {
      background: linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%);
      color: #ffffff;
      padding: 20px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-shrink: 0;
      gap: 20px;
    }
    .bills-header-title { font-size: 20px; font-weight: 800; letter-spacing: -0.02em; }
    .bills-header-subtitle { font-size: 12px; color: #cbd5e1; margin-top: 3px; }
    .bills-header-kpis { display: flex; align-items: center; gap: 14px; }
    .bills-header-kpi-box {
      background: rgba(255,255,255,0.1);
      border: 1px solid rgba(255,255,255,0.15);
      border-radius: var(--radius-md);
      padding: 8px 14px;
      text-align: center;
    }
    .bills-header-kpi-val { font-size: 16px; font-weight: 800; color: #f8fafc; }
    .bills-header-kpi-label { font-size: 10px; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.05em; }

    .bills-controls-bar {
      background: #ffffff;
      border-bottom: 1px solid var(--border-subtle);
      padding: 10px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-shrink: 0;
      flex-wrap: wrap;
    }
    .bills-filter-group { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }
    .decade-pills { display: flex; align-items: center; gap: 4px; overflow-x: auto; }
    .decade-pill-btn {
      padding: 4px 10px;
      font-size: 11px;
      font-weight: 600;
      border: 1px solid var(--border-subtle);
      background: var(--bg-canvas);
      border-radius: var(--radius-full);
      cursor: pointer;
      color: var(--text-body);
      transition: all 0.15s;
    }
    .decade-pill-btn:hover { background: #ffffff; border-color: #cbd5e1; }
    .decade-pill-btn.active { background: var(--accent-blue); color: #ffffff; border-color: var(--accent-blue); }

    .bills-grid-container {
      flex: 1;
      overflow-y: auto;
      padding: 20px 24px;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
      gap: 16px;
      align-content: start;
    }

    /* Bill Card */
    .bill-card {
      background: #ffffff;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 16px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 12px;
      box-shadow: var(--shadow-sm);
      transition: transform 0.15s, box-shadow 0.15s, border-color 0.15s;
      cursor: pointer;
    }
    .bill-card:hover {
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
      border-color: #cbd5e1;
    }
    .bill-card-top { display: flex; justify-content: space-between; align-items: flex-start; gap: 8px; }
    .bill-badge-group { display: flex; align-items: center; gap: 6px; flex-wrap: wrap; }
    .badge-year { font-size: 10.5px; font-weight: 800; padding: 2px 8px; background: #eff6ff; color: var(--accent-blue); border-radius: var(--radius-full); }
    .badge-billno { font-size: 10.5px; font-weight: 700; padding: 2px 7px; background: #f1f5f9; color: var(--text-navy); border-radius: 4px; }
    .badge-status { font-size: 10.5px; font-weight: 700; padding: 2px 8px; background: #f0fdf4; color: #15803d; border-radius: var(--radius-full); }

    .bill-title {
      font-size: 13.5px;
      font-weight: 800;
      color: var(--text-navy);
      line-height: 1.4;
    }
    .bill-dates-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      padding-top: 8px;
      border-top: 1px dashed var(--border-subtle);
      font-size: 11px;
    }
    .bill-date-box { display: flex; flex-direction: column; gap: 2px; }
    .bill-date-label { font-size: 9.5px; color: var(--text-muted); text-transform: uppercase; font-weight: 600; }
    .bill-date-val { font-weight: 700; color: var(--text-navy); }

    .bill-action-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-top: 8px;
      border-top: 1px solid var(--border-subtle);
    }
    .btn-track-bill {
      font-size: 11px;
      font-weight: 700;
      color: var(--accent-blue);
      background: none;
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }
    .btn-track-bill:hover { text-decoration: underline; }

    /* =====================================================================
       ANIMATED LEGISLATIVE BILL TIMELINE MODAL
       ===================================================================== */
    .modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.65);
      backdrop-filter: blur(4px);
      z-index: 3000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 16px;
    }
    .modal-overlay.active { display: flex; }

    .modal-card {
      background: #ffffff;
      border-radius: var(--radius-lg);
      width: 100%;
      max-width: 780px;
      max-height: 90vh;
      display: flex;
      flex-direction: column;
      box-shadow: 0 25px 50px -12px rgba(15, 23, 42, 0.25);
      overflow: hidden;
      animation: modalPop 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    @keyframes modalPop {
      from { transform: scale(0.95); opacity: 0; }
      to { transform: scale(1); opacity: 1; }
    }

    .modal-header {
      padding: 18px 22px;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 12px;
      background: #fafafa;
    }
    .modal-body {
      padding: 22px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    /* Animated Timeline Container */
    .timeline-container {
      background: #f8fafc;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 20px 16px;
      position: relative;
    }
    .timeline-title {
      font-size: 11px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      margin-bottom: 20px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .timeline-stepper {
      display: flex;
      justify-content: space-between;
      position: relative;
    }
    .timeline-track-bg {
      position: absolute;
      top: 18px;
      left: 30px;
      right: 30px;
      height: 4px;
      background: #e2e8f0;
      z-index: 1;
    }
    .timeline-track-fill {
      position: absolute;
      top: 18px;
      left: 30px;
      height: 4px;
      background: linear-gradient(90deg, #10b981 0%, #059669 100%);
      z-index: 2;
      width: 0;
      animation: fillTimelineTrack 0.8s ease-out forwards;
    }
    @keyframes fillTimelineTrack {
      to { width: calc(100% - 60px); }
    }

    .timeline-step {
      position: relative;
      z-index: 5;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      width: 18%;
      cursor: pointer;
    }
    .timeline-node {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: #ffffff;
      border: 3px solid #cbd5e1;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--text-muted);
      font-weight: 700;
      transition: all 0.2s ease;
      box-shadow: 0 2px 4px rgba(0,0,0,0.06);
    }
    .timeline-step.completed .timeline-node {
      background: #10b981;
      border-color: #059669;
      color: #ffffff;
      box-shadow: 0 0 0 4px rgba(16, 185, 129, 0.2);
    }
    .timeline-step.bypassed .timeline-node {
      background: #f1f5f9;
      border-color: #cbd5e1;
      color: #94a3b8;
    }
    .timeline-step-label {
      font-size: 11px;
      font-weight: 700;
      color: var(--text-navy);
      margin-top: 8px;
      line-height: 1.3;
    }
    .timeline-step-date {
      font-size: 10px;
      color: var(--text-muted);
      margin-top: 3px;
      font-weight: 600;
    }
    .timeline-step-status {
      font-size: 9.5px;
      padding: 1px 6px;
      border-radius: 4px;
      margin-top: 4px;
      font-weight: 700;
    }
    .timeline-step.completed .timeline-step-status { background: #dcfce7; color: #15803d; }
    .timeline-step.bypassed .timeline-step-status { background: #f1f5f9; color: #64748b; }

    /* Google Search Box inside Bill Detail */
    .google-search-section {
      background: linear-gradient(135deg, #eff6ff 0%, #f8fafc 100%);
      border: 1px solid #bfdbfe;
      border-radius: var(--radius-md);
      padding: 14px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }
    .google-search-info { display: flex; flex-direction: column; gap: 3px; }
    .google-search-bill-title { font-size: 12.5px; font-weight: 800; color: var(--text-navy); }
    .google-search-desc { font-size: 11px; color: var(--text-muted); }
    .btn-google-search {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 16px;
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: var(--radius-md);
      color: #1e293b;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      box-shadow: var(--shadow-sm);
      transition: all 0.15s ease;
      white-space: nowrap;
    }
    .btn-google-search:hover {
      background: #2563eb;
      color: #ffffff;
      border-color: #2563eb;
      box-shadow: 0 4px 12px rgba(37,99,235,0.25);
    }

    /* Bill Full Details Table */
    .bill-full-table { width: 100%; border-collapse: collapse; font-size: 11.5px; }
    .bill-full-table td { padding: 8px 10px; border-bottom: 1px solid var(--border-subtle); vertical-align: top; }
    .bill-full-table td:first-child { width: 35%; font-weight: 700; color: var(--text-muted); }
    .bill-full-table td:last-child { font-weight: 600; color: var(--text-navy); }

    /* =====================================================================
       MOBILE NAVIGATION & BOTTOM DOCK
       ===================================================================== */
    .mobile-bottom-dock {
      display: none;
      height: 52px;
      background: #ffffff;
      border-top: 1px solid var(--border-subtle);
      align-items: center;
      justify-content: space-around;
      z-index: 1500;
      box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.05);
      flex-shrink: 0;
    }
    .dock-item-btn {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 3px;
      background: none;
      border: none;
      color: var(--text-muted);
      font-size: 10px;
      font-weight: 600;
      cursor: pointer;
      flex: 1;
      height: 100%;
    }
    .dock-item-btn.active { color: var(--accent-blue); font-weight: 700; }
    .dock-item-btn svg { width: 20px; height: 20px; }

    .mobile-backdrop {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.55);
      backdrop-filter: blur(2px);
      z-index: 2200;
    }
    .mobile-backdrop.active { display: block; }
    .mobile-handle-bar {
      display: none;
      width: 40px;
      height: 5px;
      background: #cbd5e1;
      border-radius: 3px;
      margin: 8px auto 4px;
      cursor: pointer;
    }

    /* =====================================================================
       RESPONSIVE BREAKPOINTS
       ===================================================================== */
    @media (max-width: 1024px) {
      .sidebar-left, .sidebar-right { width: 320px; min-width: 320px; }
      .sidebar-left.collapsed { margin-left: -320px; }
      .sidebar-right.collapsed { margin-right: -320px; }
    }

    @media (max-width: 768px) {
      .top-header {
        height: 48px;
        min-height: 48px;
        padding: 0 10px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 8px;
        flex-wrap: nowrap;
      }
      .brand-group {
        gap: 8px;
        flex: 1;
        min-width: 0;
      }
      .brand-titles { min-width: 0; }
      .brand-name {
        font-size: 13.5px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }
      .brand-name .badge-gov {
        font-size: 8px;
        padding: 1px 4px;
      }
      .brand-subtitle { display: none !important; }

      /* In mobile header: nav tabs and top KPIs are accessible via mobile dock & hamburger menu */
      .header-nav-tabs { display: none !important; }
      .national-kpis { display: none !important; }
      .header-actions #btn-data-audit { display: none !important; }
      .header-actions #btn-toggle-right {
        padding: 4px 8px;
        font-size: 11px;
      }

      /* Mobile subheader: sleek horizontal scrollable bar, never hidden! */
      .map-subheader {
        padding: 4px 6px;
        gap: 5px;
        height: 36px;
        max-height: 36px;
        overflow-x: auto;
        overflow-y: hidden;
        white-space: nowrap;
        flex-wrap: nowrap;
        align-items: center;
        background: #ffffff;
        -webkit-overflow-scrolling: touch;
      }
      .map-mode-selector-wrapper { flex-direction: row; align-items: center; gap: 3px; }
      .map-mode-label { display: none !important; }
      .map-mode-dropdown { max-width: 112px !important; font-size: 10px; height: 26px; padding: 0 4px; font-weight: 700; }
      .map-mode-desc-pill { display: none !important; }

      /* Make search bar compact on mobile so States dropdown is immediately visible */
      .search-wrapper {
        width: 88px !important;
        min-width: 80px !important;
        flex-shrink: 0;
        transition: width 0.2s ease;
      }
      .search-wrapper:focus-within {
        width: 125px !important;
      }
      .search-input {
        height: 26px;
        font-size: 10px;
        padding: 0 14px 0 20px;
      }
      .search-icon {
        left: 5px;
        width: 10px;
        height: 10px;
      }

      /* Compact, visible States dropdown on mobile */
      .filter-select {
        height: 26px;
        padding: 0 4px;
        font-size: 10px;
        max-width: 105px;
        flex-shrink: 0;
      }
      #filter-election-state, #filter-voter-state, #filter-elector-state {
        max-width: 110px !important;
        font-weight: 700;
        border-color: #93c5fd;
        background-color: #ffffff;
        color: #1e3a8a;
      }

      .map-tools-top {
        top: 46px;
        right: 8px;
        gap: 5px;
      }
      .map-tool-btn {
        width: 30px;
        height: 30px;
      }
      .map-tool-btn svg {
        width: 15px;
        height: 15px;
      }

      /* Bottom credit bar docked cleanly on the bottom right above mobile dock */
      .bottom-credit-container {
        bottom: 6px;
        right: 6px;
        left: auto;
        transform: none;
        width: auto;
        max-width: 220px;
        pointer-events: none;
        z-index: 800;
      }
      .bottom-credit-pill {
        font-size: 8px;
        padding: 2px 6px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        background: rgba(255, 255, 255, 0.95);
        border: 1px solid rgba(15, 23, 42, 0.15);
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12);
        display: inline-flex;
        align-items: center;
        gap: 3px;
        border-radius: 4px;
      }
      .bottom-credit-pill .credit-sep { margin: 0 1px; }
      .bottom-credit-pill .credit-brand-name,
      .bottom-credit-pill .credit-sep-brand {
        display: none !important;
      }
      .bottom-credit-pill .source-full { display: none !important; }
      .bottom-credit-pill .source-short { display: inline !important; font-size: 8px; }
      .bottom-credit-pill .dev-link {
        pointer-events: auto;
        font-size: 8px;
        gap: 2px;
      }
      .bottom-credit-pill .dev-link svg {
        width: 9px;
        height: 9px;
      }

      /* Mobile legend: bottom-left as requested, right above dock */
      .map-legend-card {
        top: auto;
        bottom: 6px;
        left: 6px;
        max-width: 130px;
        max-height: 145px;
        padding: 5px 7px;
        font-size: 9px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.18);
        background: rgba(255, 255, 255, 0.96);
        border: 1px solid var(--border-subtle);
        border-radius: var(--radius-sm);
        z-index: 850;
      }
      .legend-title { font-size: 9.5px; margin-bottom: 3px; }
      .legend-items-grid {
        grid-template-columns: 1fr;
        gap: 2px;
        max-height: 105px;
        overflow-y: auto;
      }

      /* Mobile drawers */
      .sidebar-left {
        position: fixed;
        top: 0;
        left: 0;
        width: 85%;
        max-width: 340px;
        height: 100%;
        height: 100dvh;
        z-index: 2500 !important;
        margin-left: 0 !important;
        transform: translateX(-100%) !important;
        box-shadow: 10px 0 25px rgba(0, 0, 0, 0.25);
        transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        visibility: hidden;
      }
      .sidebar-left.open { transform: translateX(0) !important; visibility: visible !important; }
      .sidebar-left.collapsed { transform: translateX(-100%) !important; visibility: hidden !important; }
      .sidebar-header-mobile { display: flex; }

      .sidebar-right {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        width: 100%;
        min-width: 100%;
        max-height: 80vh;
        max-height: 80dvh;
        z-index: 2500 !important;
        margin-right: 0 !important;
        transform: translateY(105%) !important;
        border-left: none;
        border-top: 1px solid var(--border-subtle);
        border-radius: 18px 18px 0 0;
        box-shadow: var(--shadow-bottom-sheet);
        transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        visibility: hidden;
      }
      .sidebar-right.open { transform: translateY(0) !important; visibility: visible !important; }
      .sidebar-right.collapsed { transform: translateY(105%) !important; visibility: hidden !important; }
      .mobile-handle-bar { display: block; }

      .mobile-bottom-dock { display: flex; }
      .timeline-stepper { flex-direction: column; gap: 14px; align-items: flex-start; }
      .timeline-track-bg, .timeline-track-fill { display: none; }
      .timeline-step { width: 100%; flex-direction: row; gap: 12px; text-align: left; }

      /* Mobile Header Bills Quick Button */
      .btn-bills-mobile-toggle {
        display: inline-flex !important;
        align-items: center;
        gap: 4px;
        padding: 4px 8px;
        background: #eff6ff;
        border: 1px solid #bfdbfe;
        color: #1d4ed8;
        border-radius: var(--radius-sm);
        font-size: 10.5px;
        font-weight: 700;
        cursor: pointer;
        white-space: nowrap;
        flex-shrink: 0;
      }
      .btn-bills-mobile-toggle:hover {
        background: #dbeafe;
      }
      .btn-bills-mobile-toggle.active-view {
        background: #2563eb;
        color: #ffffff;
        border-color: #2563eb;
      }

      /* Mobile optimization for Rajya Sabha Bills Passed view */
      .view-bills-workspace {
        overflow-y: auto;
        -webkit-overflow-scrolling: touch;
      }
      .bills-header-banner {
        padding: 12px 14px;
        flex-direction: column;
        align-items: flex-start;
        gap: 10px;
      }
      .bills-header-title { font-size: 15px; }
      .bills-header-subtitle { font-size: 11px; }
      .bills-header-kpis {
        width: 100%;
        display: flex;
        gap: 6px;
      }
      .bills-header-kpi-box {
        flex: 1;
        padding: 5px 6px;
      }
      .bills-header-kpi-val { font-size: 13px; }
      .bills-header-kpi-label { font-size: 8px; }
      .bills-controls-bar {
        padding: 8px 12px;
        gap: 8px;
        flex-direction: column;
        align-items: stretch;
      }
      .bills-filter-group {
        width: 100%;
        gap: 6px;
      }
      .bills-filter-group .search-wrapper {
        width: 100% !important;
      }
      .decade-pills {
        width: 100%;
        overflow-x: auto;
        white-space: nowrap;
        -webkit-overflow-scrolling: touch;
        padding-bottom: 4px;
      }
      .bills-grid-container {
        padding: 12px;
        grid-template-columns: 1fr;
        gap: 12px;
        padding-bottom: 75px;
      }
    }

    /* =====================================================================
       PREMIUM CIVIC INTELLIGENCE LOADING SCREEN & ENTRANCE ANIMATION
       Responsive on PC & Mobile with Radar Pulse & Civic Insights
       ===================================================================== */
    .app-loader {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      height: 100dvh;
      z-index: 99999;
      display: flex;
      align-items: center;
      justify-content: center;
      background: radial-gradient(circle at 50% 35%, #0f172a 0%, #090d16 100%);
      color: #ffffff;
      opacity: 1;
      visibility: visible;
      transition: opacity 0.65s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.65s ease;
      user-select: none;
    }

    .app-loader.loaded {
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
    }

    .loader-backdrop {
      position: absolute;
      inset: 0;
      background-image: 
        radial-gradient(rgba(56, 189, 248, 0.08) 1px, transparent 1px),
        radial-gradient(rgba(245, 158, 11, 0.05) 1px, transparent 1px);
      background-size: 32px 32px;
      background-position: 0 0, 16px 16px;
      opacity: 0.6;
    }

    .loader-content {
      position: relative;
      z-index: 2;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      max-width: 480px;
      width: 90%;
      padding: 24px 20px;
    }

    /* Radar / Chakra Pulse Emblem */
    .loader-emblem-wrap {
      position: relative;
      width: 80px;
      height: 80px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 16px;
    }

    .loader-radar-pulse {
      position: absolute;
      inset: 0;
      border-radius: 50%;
      border: 2px solid rgba(56, 189, 248, 0.4);
      animation: pulseRadar 2.2s cubic-bezier(0.25, 1, 0.5, 1) infinite;
    }

    .loader-radar-pulse-2 {
      position: absolute;
      inset: 0;
      border-radius: 50%;
      border: 1.5px solid rgba(245, 158, 11, 0.3);
      animation: pulseRadar 2.2s cubic-bezier(0.25, 1, 0.5, 1) infinite;
      animation-delay: 0.9s;
    }

    .loader-radar-sweep {
      position: absolute;
      width: 100%;
      height: 100%;
      border-radius: 50%;
      background: conic-gradient(from 0deg, transparent 0deg, rgba(56, 189, 248, 0.25) 60deg, transparent 75deg);
      animation: spinRadar 2.8s linear infinite;
    }

    .loader-chakra-emblem {
      position: relative;
      z-index: 3;
      width: 50px;
      height: 50px;
      border-radius: 50%;
      background: #0f172a;
      box-shadow: 0 0 25px rgba(56, 189, 248, 0.45), inset 0 0 10px rgba(15, 23, 42, 0.8);
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1.5px solid rgba(56, 189, 248, 0.6);
    }

    @keyframes pulseRadar {
      0% { transform: scale(0.65); opacity: 1; }
      100% { transform: scale(1.65); opacity: 0; }
    }

    @keyframes spinRadar {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }

    .loader-brand-title {
      font-size: 25px;
      font-weight: 800;
      letter-spacing: -0.5px;
      display: flex;
      align-items: center;
      gap: 8px;
      color: #f8fafc;
      margin-bottom: 4px;
    }

    .loader-brand-title .badge-gov {
      background: linear-gradient(135deg, #f59e0b, #ea580c);
      color: #ffffff;
      font-size: 11px;
      padding: 2px 7px;
      border-radius: 4px;
      font-weight: 800;
      letter-spacing: 0.5px;
    }

    .loader-brand-sub {
      font-size: 11.5px;
      color: #94a3b8;
      font-weight: 500;
      margin-bottom: 22px;
      letter-spacing: 0.2px;
    }

    /* Progress section */
    .loader-progress-box {
      width: 100%;
      margin-bottom: 18px;
    }

    .loader-status-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 11px;
      margin-bottom: 7px;
      font-weight: 600;
    }

    .loader-status-text {
      color: #38bdf8;
      text-align: left;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      max-width: 80%;
    }

    .loader-percent {
      color: #f59e0b;
      font-family: "JetBrains Mono", monospace;
      font-size: 11.5px;
    }

    .loader-bar-track {
      width: 100%;
      height: 6px;
      background: rgba(255, 255, 255, 0.08);
      border-radius: 999px;
      overflow: hidden;
      position: relative;
    }

    .loader-bar-fill {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #38bdf8, #818cf8, #f59e0b);
      border-radius: 999px;
      transition: width 0.3s ease;
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.5);
    }

    /* Civic Intelligence Live Ticker */
    .loader-ticker-card {
      width: 100%;
      background: rgba(30, 41, 59, 0.7);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 10px;
      padding: 12px 14px;
      margin-bottom: 16px;
      text-align: left;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
    }

    .ticker-header {
      display: flex;
      align-items: center;
      gap: 6px;
      margin-bottom: 6px;
    }

    .ticker-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 8px #10b981;
      animation: pulseDot 1.5s infinite;
    }

    @keyframes pulseDot {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.3; transform: scale(0.8); }
    }

    .ticker-tag {
      font-size: 9.5px;
      font-weight: 800;
      color: #cbd5e1;
      letter-spacing: 0.8px;
      text-transform: uppercase;
    }

    .ticker-quote {
      font-size: 11.5px;
      line-height: 1.45;
      color: #f1f5f9;
      font-weight: 500;
      min-height: 34px;
      transition: opacity 0.25s ease, transform 0.25s ease;
    }

    .loader-footer-note {
      font-size: 10px;
      color: #64748b;
      letter-spacing: 0.2px;
    }

    /* Map polygon entrance wave (Top to Bottom) */
    .leaflet-interactive.pc-wave-in {
      animation: waveInPolygon 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    @keyframes waveInPolygon {
      0% {
        opacity: 0.1;
        stroke-width: 0.2;
      }
      50% {
        stroke-width: 1.8;
      }
      100% {
        opacity: 1;
        stroke-width: 1;
      }
    }
    """

