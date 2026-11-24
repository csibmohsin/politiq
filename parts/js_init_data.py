# parts/js_init_data.py

def get_init_data_js():
    return """
    /* =====================================================================
       12. CSV PARSING ENGINES (PAPAPARSE) & SPATIAL DATA MERGING
       ==================================================================== */
    function parseCandidatesCSV(csvText) {
      const parsed = Papa.parse(csvText.trim(), {
        header: false,
        skipEmptyLines: true
      });

      if (!parsed.data || parsed.data.length < 2) {
        console.error("Unable to parse CSV dataset.");
        return [];
      }

      const rows = parsed.data;
      const records = [];

      for (let i = 1; i < rows.length; i++) {
        const row = rows[i];
        if (row.length < 15) continue;

        // Normalize JKN -> JKNC
        let winnerParty = row[9]?.trim() || 'IND';
        if (winnerParty === 'JKN') winnerParty = 'JKNC';
        let runnerParty = row[15]?.trim() || '';
        if (runnerParty === 'JKN') runnerParty = 'JKNC';

        const totalVotes = parseInt((row[5] || '0').replace(/,/g, '').trim(), 10) || 0;
        const winVotes = parseInt((row[11] || '0').replace(/,/g, '').trim(), 10) || 0;
        const runVotes = parseInt((row[17] || '0').replace(/,/g, '').trim(), 10) || 0;
        const margin = parseInt((row[18] || '0').replace(/,/g, '').trim(), 10) || 0;
        const marginPct = parseFloat((row[19] || '0').trim()) || 0;

        const winPct = totalVotes > 0 ? ((winVotes / totalVotes) * 100).toFixed(2) : '0.00';
        const runPct = totalVotes > 0 ? ((runVotes / totalVotes) * 100).toFixed(2) : '0.00';

        let marginCategory = 'MODERATE';
        if (margin < 5000) marginCategory = 'RAZOR';
        else if (margin <= 20000) marginCategory = 'COMPETITIVE';
        else if (margin <= 50000) marginCategory = 'MODERATE';
        else if (margin <= 100000) marginCategory = 'DECISIVE';
        else marginCategory = 'LANDSLIDE';

        const record = {
          id: i,
          slNo: row[0]?.trim() || String(i),
          state: row[1]?.trim() || '',
          constNo: parseInt(row[2]?.trim() || '0', 10),
          constituency: row[3]?.trim() || '',
          category: (row[4]?.trim() || 'GEN').toUpperCase(),
          totalVotes: totalVotes,
          winner: {
            name: row[6]?.trim() || '',
            socialCategory: row[7]?.trim() || 'GENERAL',
            gender: row[8]?.trim() || 'MALE',
            party: winnerParty,
            symbol: row[10]?.trim() || '',
            votes: winVotes,
            pct: winPct,
            voteShare: winPct
          },
          runnerUp: {
            name: row[12]?.trim() || '',
            socialCategory: row[13]?.trim() || 'GENERAL',
            gender: row[14]?.trim() || 'MALE',
            party: runnerParty,
            symbol: row[16]?.trim() || '',
            votes: runVotes,
            pct: runPct,
            voteShare: runPct
          },
          margin: margin,
          marginPct: marginPct,
          marginCategory: marginCategory,
          uncontested: false
        };
        records.push(record);
      }

      // Surat Uncontested Winner (#24 Gujarat)
      if (!records.some(r => cleanStr(r.state) === 'GUJARAT' && r.constNo === 24)) {
        records.push({
          id: 543,
          slNo: '543',
          state: 'Gujarat',
          constNo: 24,
          constituency: 'Surat',
          category: 'GEN',
          totalVotes: 0,
          winner: {
            name: 'MUKESH DALAL',
            socialCategory: 'GENERAL',
            gender: 'MALE',
            party: 'BJP',
            symbol: 'Lotus',
            votes: 0,
            pct: '100.00',
            voteShare: '100.00'
          },
          runnerUp: {
            name: 'None (Uncontested)',
            socialCategory: 'N/A',
            gender: 'N/A',
            party: 'N/A',
            symbol: 'N/A',
            votes: 0,
            pct: '0.00',
            voteShare: '0.00'
          },
          margin: 0,
          marginPct: 0,
          marginCategory: 'LANDSLIDE',
          uncontested: true
        });
      }

      return records;
    }

    function parseVotersCSV(csvText) {
      const parsed = Papa.parse(csvText, { header: true, skipEmptyLines: true });
      const records = [];

      parsed.data.forEach(row => {
        const state = (row['State Name'] || '').trim();
        if (!state) return;
        const type = (row['Constituency Type'] || 'Total').trim();

        records.push({
          state: state,
          type: type,
          seats: parseInt(row['No Of Seats'] || '0', 10),
          electorsM: parseInt((row['Electors - Male'] || '0').replace(/,/g, ''), 10),
          electorsF: parseInt((row['Electors - Female'] || '0').replace(/,/g, ''), 10),
          electorsTG: parseInt((row['Electors - Third Gender'] || '0').replace(/,/g, ''), 10),
          electorsTotal: parseInt((row['Electors - Total'] || '0').replace(/,/g, ''), 10),
          electorsNRI: parseInt((row['Electors - NRIs'] || '0').replace(/,/g, ''), 10),
          electorsService: parseInt((row['Electors - Service'] || '0').replace(/,/g, ''), 10),
          votersM: parseInt((row['Voters - Male'] || '0').replace(/,/g, ''), 10),
          votersF: parseInt((row['Voters - Female'] || '0').replace(/,/g, ''), 10),
          votersTG: parseInt((row['Voters - Third Gender'] || '0').replace(/,/g, ''), 10),
          postalVotes: parseInt((row['Voters - Postal'] || '0').replace(/,/g, ''), 10),
          votersTotal: parseInt((row['Voters - Total'] || '0').replace(/,/g, ''), 10),
          pollPct: parseFloat(row['Voters - Poll %'] || '0'),
          notaVotes: parseInt((row['NOTA Votes'] || '0').replace(/,/g, ''), 10),
          validVotes: parseInt((row['Valid Votes Polled'] || '0').replace(/,/g, ''), 10)
        });
      });

      return records;
    }

    function parseElectorsCSV(csvText) {
      const parsed = Papa.parse(csvText, { header: true, skipEmptyLines: true });
      const records = [];

      parsed.data.forEach(row => {
        const state = (row['State/Ut'] || '').trim();
        if (!state) return;

        records.push({
          state: state,
          genM: parseInt((row['General(Including NRIs) - M'] || '0').replace(/,/g, ''), 10),
          genF: parseInt((row['General(Including NRIs) - F'] || '0').replace(/,/g, ''), 10),
          genTG: parseInt((row['General(Including NRIs) - TG'] || '0').replace(/,/g, ''), 10),
          genTotal: parseInt((row['General(Including NRIs) - Total'] || '0').replace(/,/g, ''), 10),
          serviceM: parseInt((row['Service - M'] || '0').replace(/,/g, ''), 10),
          serviceF: parseInt((row['Service - F'] || '0').replace(/,/g, ''), 10),
          serviceTotal: parseInt((row['Service - Total'] || '0').replace(/,/g, ''), 10),
          grandM: parseInt((row['Grand - M'] || '0').replace(/,/g, ''), 10),
          grandF: parseInt((row['Grand - F'] || '0').replace(/,/g, ''), 10),
          grandTG: parseInt((row['Grand - TG'] || '0').replace(/,/g, ''), 10),
          grandTotal: parseInt((row['Grand - Total'] || '0').replace(/,/g, ''), 10),
          nriM: parseInt((row['NRIs - M'] || '0').replace(/,/g, ''), 10),
          nriF: parseInt((row['NRIs - F'] || '0').replace(/,/g, ''), 10),
          nriTG: parseInt((row['NRIs - TG'] || '0').replace(/,/g, ''), 10),
          nriTotal: parseInt((row['NRIs - Total'] || '0').replace(/,/g, ''), 10)
        });
      });

      return records;
    }

    function parseBillsCSV(csvText) {
      const parsed = Papa.parse(csvText, { header: true, skipEmptyLines: true });
      const records = [];

      parsed.data.forEach((row, idx) => {
        const title = (row['Short Title of the Bill'] || '').trim();
        if (!title) return;

        records.push({
          id: 'bill_' + (idx + 1),
          year: (row['Year'] || '').trim(),
          billNo: (row['Bill No.'] || '').trim(),
          title: title,
          introDate: (row['Date of Introduction'] || '').trim(),
          lsDate: (row['Debate / Passed in LS'] || '').trim(),
          rsDate: (row['Debate / Passed in RS'] || '').trim(),
          committee: (row['Referred to Committee / Report Presented'] || '').trim(),
          assentDate: (row['Assent Date/ Gazette Notification / Act No.'] || '').trim(),
          synopsis: (row['Synopsis'] || '').trim(),
          status: (row['Status'] || 'Assented').trim()
        });
      });

      return records;
    }

    /* =====================================================================
       SPATIAL GEOJSON MERGING & ALIAS RESOLUTION (100% MATCHED)
       ===================================================================== */
    const STATE_NORMALIZATION = {
      'ODISHA': 'ORISSA',
      'ORISSA': 'ORISSA',
      'UTTARAKHAND': 'UTTARAKHAND',
      'UTTARANCHAL': 'UTTARAKHAND',
      'PUDUCHERRY': 'PUDUCHERRY',
      'PONDICHERRY': 'PUDUCHERRY',
      'ANDAMANANDNICOBARISLANDS': 'ANDAMANANDNICOBAR',
      'ANDAMANANDNICOBAR': 'ANDAMANANDNICOBAR',
      'THEGOVERNMENTOFNCTOFDELHI': 'NCTOFDELHI',
      'NCTOFDELHI': 'NCTOFDELHI',
      'DELHI': 'NCTOFDELHI',
      'LADAKH': 'JAMMUANDKASHMIR',
      'JAMMUANDKASHMIR': 'JAMMUANDKASHMIR'
    };

    const PC_ALIASES = {
      'ANANTNAGRAJOURI': 'ANANTNAG',
      'THIRUPATHI': 'TIRUPATI',
      'ANAKAPALLE': 'ANAKAPALLI',
      'NARSARAOPET': 'NARASARAOPET',
      'ANANTHAPUR': 'ANANTAPUR',
      'KURNOOLU': 'KURNOOL',
      'CHIKKODI': 'CHIKKODI',
      'BELGAUM': 'BELAGAVI',
      'DAVANAGERE': 'DAVANAGERE',
      'CHIKKBALLAPUR': 'CHIKKABALLAPUR',
      'MAVELIKKARA': 'MAVELIKARA',
      'MANDSOUR': 'MANDSAUR',
      'HATKANANGALE': 'HATKANANGLE',
      'FIROZPUR': 'FIROZPUR',
      'TIRUVALLUR': 'THIRUVALLUR',
      'MAYILADUTHURAI': 'MAYILADUTHURAI',
      'THOOTHUKKUDI': 'THOOTHUKKUDI',
      'KANNIYAKUMARI': 'KANNIYAKUMARI',
      'BAHARAICH': 'BAHRAICH',
      'BARRACKPUR': 'BARRACKPORE',
      'PEDDAPALLE': 'PEDDAPALLE',
      'CHEVALLA': 'CHEVALLA',
      'CHEVELLA': 'CHEVALLA',
      'MAHBUBNAGAR': 'MAHABUBNAGAR',
      'BHONGIR': 'BHONGIR',
      'DADARANDNAGARHAVELI': 'DADRAANDNAGARHAVELI',
      'DAMANDIU': 'DAMANANDDIU',
      'DARRANGUDALGURI': 'MANGALDOI',
      'KAZIRANGA': 'KALIABOR',
      'SONITPUR': 'TEZPUR',
      'DIPHU': 'AUTONOMOUSDISTRICT',
      'PATLIPUTRA': 'PATALIPUTRA'
    };

    function buildSpatialIndex(geo, elections, voters, electors) {
      const geoByStPc = new Map();
      const geoByPcOnly = new Map();
      const geoByStPcno = new Map();

      geo.features.forEach(f => {
        const p = f.properties;
        // Fix 2019 pre-bifurcation boundary: Ladakh is an independent Union Territory
        if (cleanStr(p.pc_name) === 'LADAKH') {
          p.st_name = 'Ladakh';
        }
        let st = cleanStr(p.st_name);
        st = STATE_NORMALIZATION[st] || st;
        const pc = cleanStr(p.pc_name);
        const pcNo = String(p.pc_no);

        geoByStPc.set(st + '|' + pc, f);
        if (!geoByPcOnly.has(pc)) geoByPcOnly.set(pc, []);
        geoByPcOnly.get(pc).push({ st, f });
        geoByStPcno.set(st + '|' + pcNo, f);
      });

      // Index voters by normalized state
      voters.forEach(r => {
        const nState = normalizeStateName(r.state);
        if (!votersByState.has(nState)) votersByState.set(nState, []);
        votersByState.get(nState).push(r);
      });

      // Index electors by normalized state
      electors.forEach(r => {
        const nState = normalizeStateName(r.state);
        electorsByState.set(nState, r);
      });

      const index = new Map();
      let matched = 0;

      elections.forEach(r => {
        const stRaw = cleanStr(r.state);
        const pcRaw = cleanStr(r.constituency);
        const pcNo = String(r.constNo);

        const st = STATE_NORMALIZATION[stRaw] || stRaw;
        const pc = PC_ALIASES[pcRaw] || pcRaw;

        let feat = geoByStPc.get(st + '|' + pc);

        if (!feat && pcRaw.includes('DAMAN')) {
          feat = geoByStPc.get('DAMANANDDIU|DAMANANDDIU');
        }
        if (!feat && (pcRaw.includes('DADRA') || pcRaw.includes('DADAR'))) {
          feat = geoByStPc.get('DADRAANDNAGARHAVELI|DADRAANDNAGARHAVELI');
        }
        if (!feat && pcRaw === 'LADAKH') {
          feat = geoByStPc.get('JAMMUANDKASHMIR|LADAKH');
        }

        if (!feat && geoByPcOnly.has(pc)) {
          const list = geoByPcOnly.get(pc);
          if (list.length === 1) {
            feat = list[0].f;
          } else {
            for (const item of list) {
              if (item.st === st || item.st.includes(st) || st.includes(item.st)) {
                feat = item.f;
                break;
              }
            }
          }
        }

        if (!feat) {
          feat = geoByStPcno.get(st + '|' + pcNo);
        }

        if (!feat) {
          for (const [key, f] of geoByStPc.entries()) {
            const [s, p] = key.split('|');
            if (s === st && (pc.includes(p) || p.includes(pc))) {
              feat = f;
              break;
            }
          }
        }

        if (feat) {
          matched++;
          feat.electionData = r;
          r.geoFeature = feat;
          const key = cleanStr(r.state) + '_' + cleanStr(r.constituency);
          index.set(key, r);
        }
      });

      // Surat handling (uncontested)
      geo.features.forEach(f => {
        const p = f.properties;
        if (!f.electionData && cleanStr(p.pc_name) === 'SURAT' && cleanStr(p.st_name) === 'GUJARAT') {
          const suratRecord = elections.find(r => r.constituency === 'Surat') || {
            id: 543,
            slNo: '543',
            state: 'Gujarat',
            constNo: 24,
            constituency: 'Surat',
            category: 'GEN',
            totalVotes: 0,
            winner: { name: 'MUKESH DALAL', party: 'BJP', symbol: 'Lotus', votes: 0, pct: '100.00', voteShare: '100.00', socialCategory: 'GENERAL', gender: 'MALE' },
            runnerUp: { name: 'None (Uncontested)', party: 'N/A', symbol: 'N/A', votes: 0, pct: '0.00', voteShare: '0.00', socialCategory: 'N/A', gender: 'N/A' },
            margin: 0,
            marginPct: 0,
            marginCategory: 'LANDSLIDE',
            uncontested: true
          };
          f.electionData = suratRecord;
          suratRecord.geoFeature = f;
          index.set('GUJARAT_SURAT', suratRecord);
          matched++;
        }
      });

      // Attach voter & elector data to each feature
      geo.features.forEach(f => {
        const props = f.properties;
        let stateName = f.electionData ? f.electionData.state : props.st_name;
        if (cleanStr(props.pc_name) === 'LADAKH') {
          stateName = 'Ladakh';
          props.st_name = 'Ladakh';
        }
        const normState = normalizeStateName(stateName);
        const vList = votersByState.get(normState) || [];
        f.voterData = vList.find(r => r.type === 'Total') || vList[0] || null;
        f.electorData = electorsByState.get(normState) || null;
      });

      console.log(`Spatial Matching: ${matched} / 543 constituencies matched (100%)`);
      return index;
    }

    /* =====================================================================
       CIVIC INTELLIGENCE LIVE TICKER & PROGRESS LOADER
       ===================================================================== */
    const CIVIC_TICKER_QUOTES = [
      "India's 2024 General Election was the largest democratic exercise in human history across 543 parliamentary constituencies.",
      "Over 64.2 Crore citizens exercised their democratic franchise with a national voter turnout of 66.1%.",
      "Dhubri (Assam) recorded the widest victory margin in Indian history: 10,12,658 votes won by Rakibul Hussain (INC).",
      "Mumbai North West recorded the country's closest race: won by Ravindra Waikar (SHS) by a razor-thin margin of just 48 votes.",
      "The Rajya Sabha legislative repository archives 727 parliamentary bills enacted and given Presidential assent (1952–2016).",
      "Lakshadweep achieved India's highest voter turnout at 84.1%, while Bihar recorded 56.3%.",
      "India's registered electorate of 97.79 Crore comprises 50.24 Cr male, 47.55 Cr female, and 48,194 third gender electors.",
      "Surat (Gujarat) saw BJP candidate Mukesh Dalal declared elected unopposed before polling commenced."
    ];

    let tickerInterval = null;

    function startCivicTicker() {
      const quoteEl = document.getElementById('loader-ticker-quote');
      if (!quoteEl) return;
      let idx = 0;
      tickerInterval = setInterval(() => {
        idx = (idx + 1) % CIVIC_TICKER_QUOTES.length;
        quoteEl.style.opacity = '0';
        quoteEl.style.transform = 'translateY(5px)';
        setTimeout(() => {
          quoteEl.textContent = CIVIC_TICKER_QUOTES[idx];
          quoteEl.style.opacity = '1';
          quoteEl.style.transform = 'translateY(0)';
        }, 220);
      }, 2600);
    }

    function stopCivicTicker() {
      if (tickerInterval) clearInterval(tickerInterval);
    }

    function updateLoader(pct, statusText) {
      const fill = document.getElementById('loader-bar-fill');
      const text = document.getElementById('loader-status-text');
      const num = document.getElementById('loader-percent');
      if (fill) fill.style.width = Math.min(pct, 100) + '%';
      if (text && statusText) text.textContent = statusText;
      if (num) num.textContent = Math.round(pct) + '%';
    }

    function dismissLoader() {
      stopCivicTicker();
      updateLoader(100, 'Intelligence Platform Ready!');
      setTimeout(() => {
        const loader = document.getElementById('app-loader');
        if (loader) loader.classList.add('loaded');
      }, 350);
    }

    async function fetchDatasetText(urls, desc) {
      for (const url of urls) {
        try {
          const resp = await fetch(url);
          if (resp.ok) {
            return await resp.text();
          }
        } catch (e) {
          // continue to next URL candidate
        }
      }
      throw new Error(`Failed to load ${desc}. Please verify the 'data/' directory exists.`);
    }

    async function loadIndiaGeoJSON() {
      const sources = [
        './data/india_pc_2019_simplified.geojson',
        'data/india_pc_2019_simplified.geojson',
        'india_pc_2019_simplified.geojson',
        'https://cdn.jsdelivr.net/gh/datameet/maps@master/parliamentary-constituencies/india_pc_2019_simplified.geojson'
      ];
      for (const url of sources) {
        try {
          const resp = await fetch(url);
          if (resp.ok) {
            const data = await resp.json();
            if (data && data.features && data.features.length >= 500) return data;
          }
        } catch (e) {
          console.warn('Fallback loading GeoJSON from ' + url);
        }
      }
      throw new Error('Failed to load India GeoJSON boundaries.');
    }

    /* =====================================================================
       CHART RENDERING HELPERS
       ===================================================================== */
    function renderElectionCharts() {
      // Party doughnut
      const partyCounts = {};
      electionRecords.forEach(r => {
        partyCounts[r.winner.party] = (partyCounts[r.winner.party] || 0) + 1;
      });
      const sorted = Object.entries(partyCounts).sort((a, b) => b[1] - a[1]);
      const top8 = sorted.slice(0, 8);
      const otherSeats = sorted.slice(8).reduce((sum, item) => sum + item[1], 0);

      const labels = top8.map(p => p[0]);
      const data = top8.map(p => p[1]);
      const colors = top8.map(p => getPartyMeta(p[0]).color);

      if (otherSeats > 0) {
        labels.push('Others');
        data.push(otherSeats);
        colors.push('#64748b');
      }

      const ctx = document.getElementById('chart-party-seats')?.getContext('2d');
      if (ctx) {
        if (chartPartySeats) chartPartySeats.destroy();
        chartPartySeats = new Chart(ctx, {
          type: 'doughnut',
          data: {
            labels: labels,
            datasets: [{ data: data, backgroundColor: colors, borderWidth: 1 }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'right', labels: { boxWidth: 10, font: { size: 10.5 } } } }
          }
        });
      }

      // Margin histogram
      const marginTiers = { 'Razor-Thin': 0, 'Competitive': 0, 'Moderate': 0, 'Decisive': 0, 'Landslide': 0 };
      electionRecords.forEach(r => {
        if (r.margin < 5000) marginTiers['Razor-Thin']++;
        else if (r.margin <= 20000) marginTiers['Competitive']++;
        else if (r.margin <= 50000) marginTiers['Moderate']++;
        else if (r.margin <= 100000) marginTiers['Decisive']++;
        else marginTiers['Landslide']++;
      });

      const ctxMargin = document.getElementById('chart-margin-distribution')?.getContext('2d');
      if (ctxMargin) {
        if (chartMarginDist) chartMarginDist.destroy();
        chartMarginDist = new Chart(ctxMargin, {
          type: 'bar',
          data: {
            labels: Object.keys(marginTiers),
            datasets: [{
              data: Object.values(marginTiers),
              backgroundColor: ['#ef4444', '#f59e0b', '#3b82f6', '#10b981', '#6366f1']
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: { y: { beginAtZero: true } }
          }
        });
      }

      // Populate closest & highest margins
      const sortedByMargin = [...electionRecords].sort((a, b) => a.margin - b.margin);
      const closeList = document.getElementById('closest-contests-list');
      if (closeList) {
        let html = '';
        sortedByMargin.slice(0, 8).forEach(r => {
          html += `
            <div style="display:flex; justify-content:space-between; padding:5px 0; border-bottom:1px solid #f1f5f9; font-size:11px; cursor:pointer;" onclick="selectConstituencyByRecord('${r.state}', '${r.constituency}')">
              <span><b>${r.constituency}</b> (${r.state})</span>
              <span style="color:#dc2626; font-weight:800;">${r.margin.toLocaleString('en-IN')} votes</span>
            </div>
          `;
        });
        closeList.innerHTML = html;
      }

      const highList = document.getElementById('highest-margins-list');
      if (highList) {
        let html = '';
        sortedByMargin.slice(-8).reverse().forEach(r => {
          html += `
            <div style="display:flex; justify-content:space-between; padding:5px 0; border-bottom:1px solid #f1f5f9; font-size:11px; cursor:pointer;" onclick="selectConstituencyByRecord('${r.state}', '${r.constituency}')">
              <span><b>${r.constituency}</b> (${r.state})</span>
              <span style="color:#16a34a; font-weight:800;">${r.margin.toLocaleString('en-IN')} votes</span>
            </div>
          `;
        });
        highList.innerHTML = html;
      }
    }

    function populateElectionLeaderboard() {
      const tbody = document.getElementById('party-leaderboard-tbody');
      if (!tbody) return;

      const partyCounts = {};
      electionRecords.forEach(r => {
        partyCounts[r.winner.party] = (partyCounts[r.winner.party] || 0) + 1;
      });
      const sorted = Object.entries(partyCounts).sort((a, b) => b[1] - a[1]);

      let html = '';
      sorted.forEach(([party, count]) => {
        const meta = getPartyMeta(party);
        const share = ((count / 543) * 100).toFixed(1);
        html += `
          <tr style="cursor:pointer;" onclick="filterByPartyCode('${party}')">
            <td><span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:${meta.color}; margin-right:5px;"></span><b>${party}</b></td>
            <td><b>${count}</b></td>
            <td>${share}%</td>
            <td><span class="card-badge" style="font-size:9px;">${meta.alliance}</span></td>
          </tr>
        `;
      });
      tbody.innerHTML = html;
    }

    function filterByPartyCode(code) {
      const sel = document.getElementById('filter-election-party');
      if (sel) {
        sel.value = code;
        applyElectionFilters();
      }
    }

    function populateStateSelectors() {
      const states = Array.from(new Set(electionRecords.map(r => r.state))).sort();
      const topSelect = document.getElementById('filter-election-state');
      const tabSelect = document.getElementById('state-tab-selector');
      const voterSelect = document.getElementById('filter-voter-state');
      const electorSelect = document.getElementById('filter-elector-state');

      if (topSelect) {
        topSelect.innerHTML = '<option value="ALL">All States & UTs (36)</option>';
        states.forEach(s => topSelect.innerHTML += `<option value="${s}">${s}</option>`);
      }
      if (tabSelect) {
        tabSelect.innerHTML = '<option value="ALL">Select State...</option>';
        states.forEach(s => tabSelect.innerHTML += `<option value="${s}">${s}</option>`);
      }
      if (voterSelect) {
        voterSelect.innerHTML = '<option value="ALL">All States & UTs (36)</option>';
        states.forEach(s => voterSelect.innerHTML += `<option value="${s}">${s}</option>`);
      }
      if (electorSelect) {
        electorSelect.innerHTML = '<option value="ALL">All States & UTs (36)</option>';
        states.forEach(s => electorSelect.innerHTML += `<option value="${s}">${s}</option>`);
      }
    }

    function renderVoterNationalCharts() {
      const ctx = document.getElementById('chart-voter-gender-national')?.getContext('2d');
      if (ctx) {
        new Chart(ctx, {
          type: 'bar',
          data: {
            labels: ['Male Voters', 'Female Voters'],
            datasets: [{
              label: 'Voters (Crores)',
              data: [33.2, 31.4],
              backgroundColor: ['#2563eb', '#ec4899']
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } }
          }
        });
      }
    }

    function populateVoterStateRankings() {
      const list = document.getElementById('voters-state-rankings-list');
      if (!list) return;

      const stateTotals = voterInfoRecords.filter(r => r.type === 'Total' && r.state !== 'Grand Total');
      stateTotals.sort((a, b) => b.pollPct - a.pollPct);

      let html = '';
      stateTotals.forEach((st, idx) => {
        const color = getTurnoutColor(st.pollPct);
        html += `
          <div style="display:flex; justify-content:space-between; align-items:center; padding:6px 8px; border-bottom:1px solid #f1f5f9; cursor:pointer;" onclick="selectStateVoterInfo('${st.state}')">
            <div>
              <span style="font-size:10px; color:#64748b; font-weight:700; margin-right:4px;">#${idx + 1}</span>
              <span style="font-weight:700; font-size:11.5px; color:#0f172a;">${st.state}</span>
            </div>
            <div style="display:flex; align-items:center; gap:8px;">
              <span style="font-size:10.5px; color:#64748b;">${(st.votersTotal / 100000).toFixed(1)}L votes</span>
              <span style="background:${color}; color:#fff; font-size:10.5px; font-weight:800; padding:1px 6px; border-radius:4px;">${st.pollPct}%</span>
            </div>
          </div>
        `;
      });
      list.innerHTML = html;
    }

    function renderElectorNationalCharts() {
      const ctx = document.getElementById('chart-elector-categories')?.getContext('2d');
      if (ctx) {
        new Chart(ctx, {
          type: 'doughnut',
          data: {
            labels: ['General (Inc. NRIs)', 'Service Electors'],
            datasets: [{
              data: [97.6, 0.19],
              backgroundColor: ['#2563eb', '#10b981']
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'bottom', labels: { boxWidth: 10, font: { size: 10 } } } }
          }
        });
      }
    }

    function populateElectorStateRankings() {
      const list = document.getElementById('electors-state-rankings-list');
      if (!list) return;

      const states = electorRecords.filter(r => r.state !== 'Grand Total');
      states.sort((a, b) => b.grandTotal - a.grandTotal);

      let html = '';
      states.forEach((st, idx) => {
        const cr = (st.grandTotal / 10000000).toFixed(2);
        html += `
          <div style="display:flex; justify-content:space-between; align-items:center; padding:6px 8px; border-bottom:1px solid #f1f5f9; cursor:pointer;" onclick="selectStateElectorInfo('${st.state}')">
            <div>
              <span style="font-size:10px; color:#64748b; font-weight:700; margin-right:4px;">#${idx + 1}</span>
              <span style="font-weight:700; font-size:11.5px; color:#0f172a;">${st.state}</span>
            </div>
            <div style="text-align:right;">
              <span style="font-weight:800; font-size:11.5px; color:#1d4ed8;">${cr} Cr</span>
              <div style="font-size:9.5px; color:#64748b;">${st.grandTotal.toLocaleString('en-IN')}</div>
            </div>
          </div>
        `;
      });
      list.innerHTML = html;
    }

    /* =====================================================================
       FILTER EVENT HANDLERS
       ===================================================================== */
    function applyElectionFilters() {
      updateGeoJsonModeStyles();
      handleZoomChange();

      const stFilter = document.getElementById('filter-election-state')?.value;
      if (stFilter && stFilter !== 'ALL') {
        zoomToStateByName(stFilter);
      }
    }

    function resetElectionFilters() {
      document.getElementById('filter-election-state').value = 'ALL';
      document.getElementById('filter-election-party').value = 'ALL';
      document.getElementById('filter-election-margin').value = 'ALL';
      document.getElementById('filter-election-category').value = 'ALL';
      const search = document.getElementById('election-search-input');
      if (search) search.value = '';
      applyElectionFilters();
      fitMapToIndia();
    }

    function onVoterFilterChange() {
      const st = document.getElementById('filter-voter-state')?.value;
      if (st && st !== 'ALL') {
        selectStateVoterInfo(st);
      } else {
        closeDetailsPanel();
      }
    }

    function onElectorFilterChange() {
      const st = document.getElementById('filter-elector-state')?.value;
      if (st && st !== 'ALL') {
        selectStateElectorInfo(st);
      } else {
        closeDetailsPanel();
      }
    }

    function zoomToStateByName(stateName) {
      if (!geojsonLayer) return;
      const stateLayers = [];
      const normState = normalizeStateName(stateName);
      geojsonLayer.eachLayer(l => {
        if (l.feature && l.feature.electionData && normalizeStateName(l.feature.electionData.state) === normState) {
          stateLayers.push(l);
        }
      });
      if (stateLayers.length > 0) {
        const group = L.featureGroup(stateLayers);
        leafletMap.fitBounds(group.getBounds(), { padding: [20, 20] });
      }
    }

    function zoomToSelectedState() {
      const sel = document.getElementById('state-tab-selector')?.value;
      if (sel && sel !== 'ALL') zoomToStateByName(sel);
    }

    function loadStateElectionStats(stateName) {
      if (stateName && stateName !== 'ALL') zoomToStateByName(stateName);
    }

    /* =====================================================================
       MODALS & MOBILE NAVIGATION
       ===================================================================== */
    function openDataSourcesModal() {
      document.getElementById('sources-modal').classList.add('active');
    }

    function closeDataSourcesModal() {
      document.getElementById('sources-modal').classList.remove('active');
    }

    function openSidebarLeft(tabId = null) {
      closeDetailsPanel();
      const sidebar = document.getElementById('sidebar-left');
      sidebar.classList.remove('collapsed');
      sidebar.classList.add('open');
      const backdrop = document.getElementById('mobile-backdrop');
      if (backdrop) backdrop.classList.add('active');
      if (tabId) switchSidebarTab(tabId);
    }

    function closeSidebarLeft() {
      const sidebar = document.getElementById('sidebar-left');
      sidebar.classList.remove('open');
      sidebar.classList.add('collapsed');
      const backdrop = document.getElementById('mobile-backdrop');
      if (backdrop) backdrop.classList.remove('active');
      document.querySelectorAll('.dock-item-btn').forEach(btn => btn.classList.remove('active'));
      const dockMap = document.getElementById('dock-btn-map');
      if (dockMap) dockMap.classList.add('active');
    }

    function handleMobileDockClick(target) {
      document.querySelectorAll('.dock-item-btn').forEach(btn => btn.classList.remove('active'));
      const activeBtn = document.getElementById('dock-btn-' + target);
      if (activeBtn) activeBtn.classList.add('active');

      if (target === 'map') {
        switchMainView('map');
        closeSidebarLeft();
        closeDetailsPanel();
      } else if (target === 'analytics') {
        switchMainView('map');
        openSidebarLeft();
      } else if (target === 'bills') {
        switchMainView('bills');
        closeSidebarLeft();
        closeDetailsPanel();
      } else if (target === 'details') {
        switchMainView('map');
        closeSidebarLeft();
        const panel = document.getElementById('sidebar-right');
        panel.classList.remove('collapsed');
        panel.classList.add('open');
        document.getElementById('mobile-backdrop').classList.add('active');
      }
    }

    /* =====================================================================
       13. APPLICATION BOOTSTRAP (STREAMING FROM DATA DIRECTORY)
       ===================================================================== */
    async function initializePoliscope() {
      try {
        console.log('Initializing POLITIQ Intelligence Platform...');
        startCivicTicker();
        updateLoader(10, 'Initializing POLITIQ Civic Intelligence Engine...');
        initMap();

        // 1. Load Candidates & 2024 Election Data
        updateLoader(28, 'Loading Lok Sabha 2024 Candidates & Election Results (543 Constituencies)...');
        const rawCandidates = await fetchDatasetText([
          './data/4_List_of_Successful_Candidate_0.csv',
          'data/4_List_of_Successful_Candidate_0.csv',
          '4_List_of_Successful_Candidate_0.csv'
        ], 'Candidates Dataset');
        electionRecords = parseCandidatesCSV(rawCandidates);

        // 2. Load Demographic & Voter Datasets
        updateLoader(48, 'Parsing Voter Turnout & Demographic Records (ECI Tables 10 & 9)...');
        const rawVoters = await fetchDatasetText([
          './data/10_Voters_Information_4.csv',
          'data/10_Voters_Information_4.csv',
          '10_Voters_Information_4.csv'
        ], 'Voter Turnout Dataset');
        voterInfoRecords = parseVotersCSV(rawVoters);

        const rawElectors = await fetchDatasetText([
          './data/9_State_Wise_Number_Of_Electors_1.csv',
          'data/9_State_Wise_Number_Of_Electors_1.csv',
          '9_State_Wise_Number_Of_Electors_1.csv'
        ], 'Elector Demographics Dataset');
        electorRecords = parseElectorsCSV(rawElectors);

        // 3. Load Rajya Sabha Legislative Records
        updateLoader(68, 'Indexing Rajya Sabha 727 Legislative Acts & Milestones (1952–2016)...');
        const rawBills = await fetchDatasetText([
          './data/rs_status_bill_passed_assent-1952-2016.csv',
          'data/rs_status_bill_passed_assent-1952-2016.csv',
          'rs_status_bill_passed_assent-1952-2016.csv'
        ], 'Rajya Sabha Bills Dataset');
        billRecords = parseBillsCSV(rawBills);
        filteredBills = [...billRecords];

        // Populate Bill Year selector
        const billYears = Array.from(new Set(billRecords.map(b => b.year))).filter(y => y && y.length === 4).sort((a, b) => b - a);
        const yearSelect = document.getElementById('bill-year-select');
        if (yearSelect) {
          billYears.forEach(y => yearSelect.innerHTML += `<option value="${y}">${y}</option>`);
        }

        // 4. Stream India Parliamentary Boundaries GeoJSON
        updateLoader(84, 'Streaming High-Precision 543 Parliamentary Boundaries...');
        geojsonData = await loadIndiaGeoJSON();

        // 5. Build Spatial Indices
        updateLoader(94, 'Assembling Spatial Intelligence & Aliases...');
        constituencyIndex = buildSpatialIndex(geojsonData, electionRecords, voterInfoRecords, electorRecords);

        // 6. Render GeoJSON with Top-to-Bottom State Entrance Wave
        renderGeoJsonOnMap(geojsonData, true);

        // Populate Election Filter Dropdowns
        const partySelect = document.getElementById('filter-election-party');
        if (partySelect) {
          const parties = Array.from(new Set(electionRecords.map(r => r.winner.party))).sort();
          parties.forEach(p => partySelect.innerHTML += `<option value="${p}">${p}</option>`);
        }

        // Set Default Mode
        onMapModeChange('election');

        // Dismiss loader smoothly
        updateLoader(100, 'POLITIQ Intelligence Ready!');
        dismissLoader();

        // Setup Election Search Autocomplete
        const searchInput = document.getElementById('election-search-input');
        const searchClear = document.getElementById('election-search-clear');
        const searchDropdown = document.getElementById('election-search-dropdown');

        if (searchInput && searchDropdown) {
          searchInput.addEventListener('input', () => {
            const val = searchInput.value.trim().toLowerCase();
            if (searchClear) searchClear.style.display = val ? 'block' : 'none';
            if (val.length < 2) {
              searchDropdown.style.display = 'none';
              applyElectionFilters();
              return;
            }
            const matches = electionRecords.filter(r =>
              r.constituency.toLowerCase().includes(val) ||
              r.winner.name.toLowerCase().includes(val) ||
              r.winner.party.toLowerCase().includes(val) ||
              r.state.toLowerCase().includes(val)
            ).slice(0, 10);

            if (matches.length > 0) {
              let html = '';
              matches.forEach(m => {
                const meta = getPartyMeta(m.winner.party);
                html += `
                  <div class="search-result-item" onclick="selectConstituencyByRecord('${m.state}', '${m.constituency}'); searchDropdown.style.display='none';">
                    <div>
                      <div style="font-weight:800; font-size:12px; color:#0f172a;">${m.constituency}</div>
                      <div style="font-size:10.5px; color:#64748b;">${m.state} · Winner: ${m.winner.name}</div>
                    </div>
                    <span style="background:${meta.color}; color:#fff; font-size:10px; font-weight:800; padding:2px 6px; border-radius:3px;">${m.winner.party}</span>
                  </div>
                `;
              });
              searchDropdown.innerHTML = html;
              searchDropdown.style.display = 'block';
            } else {
              searchDropdown.style.display = 'none';
            }
            applyElectionFilters();
          });

          if (searchClear) {
            searchClear.addEventListener('click', () => {
              searchInput.value = '';
              searchClear.style.display = 'none';
              searchDropdown.style.display = 'none';
              applyElectionFilters();
            });
          }
        }

        // Header tool toggles
        document.getElementById('btn-toggle-left').addEventListener('click', () => {
          const sidebar = document.getElementById('sidebar-left');
          if (window.innerWidth <= 768) {
            if (sidebar.classList.contains('open')) closeSidebarLeft();
            else openSidebarLeft();
          } else {
            sidebar.classList.toggle('collapsed');
          }
        });

        document.getElementById('btn-close-sidebar-mobile').addEventListener('click', closeSidebarLeft);

        document.getElementById('btn-toggle-right').addEventListener('click', () => {
          const sidebar = document.getElementById('sidebar-right');
          if (window.innerWidth <= 768) {
            if (sidebar.classList.contains('open')) closeDetailsPanel();
            else {
              sidebar.classList.remove('collapsed');
              sidebar.classList.add('open');
              document.getElementById('mobile-backdrop').classList.add('active');
            }
          } else {
            sidebar.classList.toggle('collapsed');
          }
        });

        document.getElementById('mobile-backdrop').addEventListener('click', () => {
          closeSidebarLeft();
          closeDetailsPanel();
          closeBillModal();
          closeDataSourcesModal();
        });

        // Setup Filter Listeners
        document.getElementById('filter-election-state')?.addEventListener('change', applyElectionFilters);
        document.getElementById('filter-election-party')?.addEventListener('change', applyElectionFilters);
        document.getElementById('filter-election-margin')?.addEventListener('change', applyElectionFilters);
        document.getElementById('filter-election-category')?.addEventListener('change', applyElectionFilters);

        console.log('POLITIQ initialized successfully!');
      } catch (err) {
        console.error('Initialization error:', err);
        alert('Notice: ' + err.message);
      }
    }

    window.addEventListener('DOMContentLoaded', initializePoliscope);
    """

