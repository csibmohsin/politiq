# parts/js_code.py

def get_javascript():
    return """
    /* =====================================================================
       POLITIQ - JAVASCRIPT INTELLIGENCE ENGINE
       ===================================================================== */
    
    // Core Application State
    let currentMainView = 'map'; // 'map' | 'bills'
    let currentMapMode = 'election'; // 'election' | 'voters' | 'electors'
    let leafletMap = null;
    let geojsonLayer = null;
    let geojsonData = null;

    // Layer groups for markers
    let nationalCentroidLayer = null;
    let stateRegionalMarkerLayer = null;
    let constituencyFlagLayer = null;

    // Datasets
    let electionRecords = [];
    let voterInfoRecords = [];
    let electorRecords = [];
    let billRecords = [];

    // Indices and mappings
    let constituencyIndex = new Map();
    let votersByState = new Map();
    let electorsByState = new Map();

    // Selection states
    let selectedPolygonLayer = null;
    let selectedStateLayers = [];
    let selectedStateName = null;
    let selectedConstituencyKey = null;
    let showMapLabels = true;

    // Chart instances
    let chartPartySeats = null;
    let chartMarginDist = null;
    let chartStateSeats = null;
    let chartVoterGender = null;
    let chartVoterCategory = null;
    let chartElectorDemog = null;

    // Bills state
    let filteredBills = [];
    let billsPage = 1;
    const BILLS_PER_PAGE = 30;
    let activeDecade = 'ALL';
    let currentSelectedBill = null;

    /* =====================================================================
       1. DATA CLEANING & STRING NORMALIZATION
       ===================================================================== */
    function cleanStr(s) {
      if (!s) return '';
      return String(s).toUpperCase().trim().replace(/&/g, 'AND').replace(/[^A-Z0-9]/g, '');
    }

    const STATE_ALIASES = {
      'ANDAMANANDNICOBAR': 'ANDAMANANDNICOBARISLANDS',
      'ANDAMANANDNICOBARISLAND': 'ANDAMANANDNICOBARISLANDS',
      'DELHI': 'NCTOFDELHI',
      'ORISSA': 'ODISHA',
      'DADRAANDNAGARHAVELI': 'DADRAANDNAGARHAVELIANDDAMANANDDIU',
      'DAMANANDDIU': 'DADRAANDNAGARHAVELIANDDAMANANDDIU',
      'THEGOVERNMENTOFNCTOFDELHI': 'NCTOFDELHI'
    };

    function normalizeStateName(s) {
      const c = cleanStr(s);
      return STATE_ALIASES[c] || c;
    }

    const STATE_ABBR = {
      'Andhra Pradesh': 'AP', 'Arunachal Pradesh': 'AR', 'Assam': 'AS', 'Bihar': 'BR',
      'Chhattisgarh': 'CG', 'Goa': 'GA', 'Gujarat': 'GJ', 'Haryana': 'HR',
      'Himachal Pradesh': 'HP', 'Jharkhand': 'JH', 'Karnataka': 'KA', 'Kerala': 'KL',
      'Madhya Pradesh': 'MP', 'Maharashtra': 'MH', 'Manipur': 'MN', 'Meghalaya': 'ML',
      'Mizoram': 'MZ', 'Nagaland': 'NL', 'Odisha': 'OD', 'Punjab': 'PB',
      'Rajasthan': 'RJ', 'Sikkim': 'SK', 'Tamil Nadu': 'TN', 'Telangana': 'TG',
      'Tripura': 'TR', 'Uttar Pradesh': 'UP', 'Uttarakhand': 'UK', 'West Bengal': 'WB',
      'Andaman & Nicobar Islands': 'AN', 'Andaman & Nicobar': 'AN', 'Chandigarh': 'CH',
      'Dadra & Nagar Haveli and Daman & Diu': 'DD', 'Dadra & Nagar Haveli': 'DD', 'Daman & Diu': 'DD',
      'Delhi': 'NCT', 'NCT OF Delhi': 'NCT', 'Jammu & Kashmir': 'JK', 'Jammu and Kashmir': 'JK',
      'Jammu & Kashmir (UT)': 'JK', 'Jammu and Kashmir (UT)': 'JK',
      'Ladakh': 'LA', 'Ladakh (UT)': 'LA', 'Lakshadweep': 'LAK', 'Puducherry': 'PY'
    };

    function getStateAbbr(st) {
      if (!st) return '';
      if (STATE_ABBR[st]) return STATE_ABBR[st];
      const clean = cleanStr(st);
      if (clean === 'JAMMUANDKASHMIR' || clean.includes('JAMMU')) return 'JK';
      if (clean === 'LADAKH') return 'LA';
      for (const [key, val] of Object.entries(STATE_ABBR)) {
        if (cleanStr(key) === clean) return val;
      }
      return st.substring(0, 3).toUpperCase();
    }

    /* =====================================================================
       2. OFFICIAL PARTY METADATA & COLORS
       ===================================================================== */
    const PARTY_META = {
      'BJP': { name: 'Bharatiya Janata Party', color: '#ff9933', symbol: 'Lotus', alliance: 'NDA' },
      'INC': { name: 'Indian National Congress', color: '#19aaed', symbol: 'Hand', alliance: 'INDIA' },
      'SP': { name: 'Samajwadi Party', color: '#e11d48', symbol: 'Bicycle', alliance: 'INDIA' },
      'AITC': { name: 'All India Trinamool Congress', color: '#0d9488', symbol: 'Flowers & Grass', alliance: 'INDIA' },
      'DMK': { name: 'Dravida Munnetra Kazhagam', color: '#b91c1c', symbol: 'Rising Sun', alliance: 'INDIA' },
      'TDP': { name: 'Telugu Desam Party', color: '#eab308', symbol: 'Bicycle', alliance: 'NDA' },
      'JD(U)': { name: 'Janata Dal (United)', color: '#15803d', symbol: 'Arrow', alliance: 'NDA' },
      'SHSUBT': { name: 'Shiv Sena (Uddhav Balasaheb Thackeray)', color: '#ea580c', symbol: 'Flaming Torch', alliance: 'INDIA' },
      'NCPSP': { name: 'Nationalist Congress Party (Sharadchandra Pawar)', color: '#0284c7', symbol: 'Man Blowing Turha', alliance: 'INDIA' },
      'SHS': { name: 'Shiv Sena', color: '#f97316', symbol: 'Bow and Arrow', alliance: 'NDA' },
      'LJPRV': { name: 'Lok Janshakti Party (Ram Vilas)', color: '#38bdf8', symbol: 'Helicopter', alliance: 'NDA' },
      'YSRCP': { name: 'YSR Congress Party', color: '#0369a1', symbol: 'Ceiling Fan', alliance: 'OTH' },
      'RJD': { name: 'Rashtriya Janata Dal', color: '#166534', symbol: 'Hurricane Lamp', alliance: 'INDIA' },
      'CPI(M)': { name: 'Communist Party of India (Marxist)', color: '#dc2626', symbol: 'Hammer, Sickle and Star', alliance: 'INDIA' },
      'IUML': { name: 'Indian Union Muslim League', color: '#047857', symbol: 'Ladder', alliance: 'INDIA' },
      'AAP': { name: 'Aam Aadmi Party', color: '#0ea5e9', symbol: 'Broom', alliance: 'INDIA' },
      'JKNC': { name: 'Jammu & Kashmir National Conference', color: '#881337', symbol: 'Plough', alliance: 'INDIA' },
      'JMM': { name: 'Jharkhand Mukti Morcha', color: '#1e3a8a', symbol: 'Bow and Arrow', alliance: 'INDIA' },
      'JNP': { name: 'Jana Sena Party', color: '#be123c', symbol: 'Glass Tumbler', alliance: 'NDA' },
      'CPI(ML)(L)': { name: 'Communist Party of India (Marxist-Leninist) (Liberation)', color: '#ef4444', symbol: 'Three Stars', alliance: 'INDIA' },
      'JD(S)': { name: 'Janata Dal (Secular)', color: '#15803d', symbol: 'A Lady Farmer Carrying Paddy', alliance: 'NDA' },
      'VCK': { name: 'Viduthalai Chiruthaigal Katchi', color: '#4338ca', symbol: 'Pot', alliance: 'INDIA' },
      'CPI': { name: 'Communist Party of India', color: '#b91c1c', symbol: 'Ears of Corn and Sickle', alliance: 'INDIA' },
      'RLD': { name: 'Rashtriya Lok Dal', color: '#16a34a', symbol: 'Hand Pump', alliance: 'NDA' },
      'RSP': { name: 'Revolutionary Socialist Party', color: '#991b1b', symbol: 'Spade and Stoker', alliance: 'INDIA' },
      'UPPL': { name: 'United People Party, Liberal', color: '#f59e0b', symbol: 'Tractor Chalata Kisan', alliance: 'NDA' },
      'AGP': { name: 'Asom Gana Parishad', color: '#0284c7', symbol: 'Elephant', alliance: 'NDA' },
      'HAM(S)': { name: 'Hindustani Awam Morcha (Secular)', color: '#d97706', symbol: 'Wok', alliance: 'NDA' },
      'KEC': { name: 'Kerala Congress', color: '#047857', symbol: 'Two Leaves', alliance: 'INDIA' },
      'NCP': { name: 'Nationalist Congress Party', color: '#0369a1', symbol: 'Clock', alliance: 'NDA' },
      'ADAL': { name: 'Apna Dal (Soneylal)', color: '#ea580c', symbol: 'Cup and Saucer', alliance: 'NDA' },
      'AJSUP': { name: 'AJSU Party', color: '#4f46e5', symbol: 'Banana', alliance: 'NDA' },
      'AIMIM': { name: 'All India Majlis-E-Ittehadul Muslimeen', color: '#065f46', symbol: 'Kite', alliance: 'OTH' },
      'RD': { name: 'Rashtriya Loktantrik Party', color: '#ca8a04', symbol: 'Tyre', alliance: 'INDIA' },
      'SAD': { name: 'Shiromani Akali Dal', color: '#eab308', symbol: 'Scales', alliance: 'OTH' },
      'SKM': { name: 'Sikkim Krantikari Morcha', color: '#be185d', symbol: 'Table Lamp', alliance: 'NDA' },
      'ZPM': { name: 'Zoram People’s Movement', color: '#f97316', symbol: 'Hat', alliance: 'OTH' },
      'BAP': { name: 'Bharat Adivasi Party', color: '#15803d', symbol: 'Hockey Stick & Ball', alliance: 'INDIA' },
      'ASPKR': { name: 'Azad Samaj Party (Kanshi Ram)', color: '#1e40af', symbol: 'Kettle', alliance: 'OTH' },
      'VOTPP': { name: 'Voice of the People Party', color: '#0284c7', symbol: 'Winnowing Fan', alliance: 'OTH' },
      'MDMK': { name: 'Marumalarchi Dravida Munnetra Kazhagam', color: '#dc2626', symbol: 'Top', alliance: 'INDIA' },
      'IND': { name: 'Independent Candidate', color: '#64748b', symbol: 'Free Symbol', alliance: 'OTH' }
    };

    function getPartyMeta(p) {
      if (!p) return { name: 'Other', color: '#64748b', symbol: 'Unknown', alliance: 'OTH' };
      const code = String(p).trim().toUpperCase();
      if (code === 'JKN') return PARTY_META['JKNC'];
      return PARTY_META[code] || { name: code, color: '#475569', symbol: 'Party Symbol', alliance: 'OTH' };
    }

    /* =====================================================================
       3. TOP NAVIGATION & VIEW SWITCHING
       ===================================================================== */
    function switchMainView(view) {
      currentMainView = view;

      document.querySelectorAll('.header-nav-btn').forEach(btn => btn.classList.remove('active'));
      const activeNavBtn = document.getElementById(view === 'map' ? 'nav-btn-map' : 'nav-btn-bills');
      if (activeNavBtn) activeNavBtn.classList.add('active');

      const mapContainer = document.getElementById('view-map');
      const billsContainer = document.getElementById('view-bills');

      if (view === 'map') {
        mapContainer.classList.remove('hidden');
        billsContainer.classList.add('hidden');
        if (leafletMap) {
          setTimeout(() => leafletMap.invalidateSize(), 100);
        }
      } else {
        mapContainer.classList.add('hidden');
        billsContainer.classList.remove('hidden');
        renderBillsList();
      }

      // Update mobile dock
      document.querySelectorAll('.dock-item-btn').forEach(btn => btn.classList.remove('active'));
      const dockBtn = document.getElementById(view === 'map' ? 'dock-btn-map' : 'dock-btn-bills');
      if (dockBtn) dockBtn.classList.add('active');

      // Update mobile header toggle button
      const mobileHeaderBtn = document.getElementById('btn-bills-mobile-header');
      const mobileHeaderText = document.getElementById('mobile-header-bills-text');
      if (mobileHeaderBtn && mobileHeaderText) {
        if (view === 'bills') {
          mobileHeaderBtn.classList.add('active-view');
          mobileHeaderText.textContent = 'Map View';
        } else {
          mobileHeaderBtn.classList.remove('active-view');
          mobileHeaderText.textContent = 'Bills Passed';
        }
      }
    }

    /* =====================================================================
       4. MAP VISUALIZATION MODE SWITCHING (SAME MAP INSTANCE)
       ===================================================================== */
    function onMapModeChange(mode) {
      currentMapMode = mode;

      const descPill = document.getElementById('map-mode-desc-pill');
      if (descPill) {
        if (mode === 'election') {
          descPill.textContent = 'Constituency-Level Party Dominance & Margin Analysis';
        } else if (mode === 'voters') {
          descPill.textContent = 'State-Level Polling Turnout %, Electors vs Voters & NOTA Statistics';
        } else {
          descPill.textContent = 'State-Level Elector Population, NRI & Armed Forces Demographics';
        }
      }

      // Sync select dropdown if changed externally
      const select = document.getElementById('map-mode-select');
      if (select && select.value !== mode) select.value = mode;

      // Sync mobile drawer buttons
      document.querySelectorAll('.mobile-mode-btn').forEach(b => b.classList.remove('active'));
      const activeBtn = document.getElementById('mobile-mode-btn-' + mode);
      if (activeBtn) activeBtn.classList.add('active');

      // Toggle Filter Trays
      document.getElementById('filter-tray-election')?.classList.toggle('hidden', mode !== 'election');
      document.getElementById('filter-tray-voters')?.classList.toggle('hidden', mode !== 'voters');
      document.getElementById('filter-tray-electors')?.classList.toggle('hidden', mode !== 'electors');

      // Update Top KPIs
      updateTopKpis();

      // Update Map Polygons & Centroids
      updateGeoJsonModeStyles();
      handleZoomChange();

      // Update Floating Legend
      updateMapLegend();

      // Update Left Analytics Sidebar
      updateSidebarAnalytics();

      // Reset Details Panel
      closeDetailsPanel();
    }

    function setMapModeFromMobile(mode) {
      onMapModeChange(mode);
      if (window.innerWidth <= 768) {
        closeSidebarLeft();
      }
    }

    function updateTopKpis() {
      const container = document.getElementById('top-national-kpis');
      if (!container) return;

      if (currentMapMode === 'election') {
        container.innerHTML = `
          <div class="kpi-chip"><span class="kpi-label">Total Seats</span><span class="kpi-val">543</span></div>
          <div class="kpi-chip"><span class="kpi-label">Majority</span><span class="kpi-val">272</span></div>
          <div class="kpi-chip nda"><span class="kpi-label">NDA</span><span class="kpi-val">293</span></div>
          <div class="kpi-chip india"><span class="kpi-label">INDIA</span><span class="kpi-val">234</span></div>
          <div class="kpi-chip others"><span class="kpi-label">Others</span><span class="kpi-val">16</span></div>
        `;
      } else if (currentMapMode === 'voters') {
        container.innerHTML = `
          <div class="kpi-chip turnout"><span class="kpi-label">National Turnout</span><span class="kpi-val">66.10%</span></div>
          <div class="kpi-chip"><span class="kpi-label">Total Electors</span><span class="kpi-val">97.80 Cr</span></div>
          <div class="kpi-chip"><span class="kpi-label">Voters Polled</span><span class="kpi-val">64.64 Cr</span></div>
          <div class="kpi-chip others"><span class="kpi-label">Total NOTA</span><span class="kpi-val">63.72 Lakh</span></div>
        `;
      } else {
        container.innerHTML = `
          <div class="kpi-chip nda"><span class="kpi-label">Grand Electors</span><span class="kpi-val">97.80 Cr</span></div>
          <div class="kpi-chip india"><span class="kpi-label">Male</span><span class="kpi-val">50.24 Cr</span></div>
          <div class="kpi-chip turnout"><span class="kpi-label">Female</span><span class="kpi-val">47.55 Cr</span></div>
          <div class="kpi-chip bills"><span class="kpi-label">Third Gender</span><span class="kpi-val">48,194</span></div>
          <div class="kpi-chip others"><span class="kpi-label">Service/NRI</span><span class="kpi-val">20.36 Lakh</span></div>
        `;
      }
    }
    """

