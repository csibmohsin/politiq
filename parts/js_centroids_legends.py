# parts/js_centroids_legends.py

def get_centroids_legends_js():
    return """
    /* =====================================================================
       8. CENTROIDS, ZOOM TIERS & FLOATING LEGENDS
       ===================================================================== */
    function handleZoomChange() {
      if (!leafletMap || !geojsonLayer) return;
      const zoom = leafletMap.getZoom();

      if (currentMapMode === 'election') {
        if (zoom <= 5) {
          renderNationalCentroids();
        } else {
          renderConstituencyView();
        }
      } else if (currentMapMode === 'voters') {
        renderVoterStateCentroids();
      } else {
        renderElectorStateCentroids();
      }
    }

    /* =====================================================================
       HIGH-CONTRAST TEXT HELPER
       ===================================================================== */
    function getContrastColor(hexColor) {
      if (!hexColor) return '#0f172a';
      const hex = hexColor.replace('#', '');
      const r = parseInt(hex.substr(0, 2), 16) || 0;
      const g = parseInt(hex.substr(2, 2), 16) || 0;
      const b = parseInt(hex.substr(4, 2), 16) || 0;
      const yiq = ((r * 299) + (g * 587) + (b * 114)) / 1000;
      return yiq >= 160 ? '#0f172a' : '#ffffff';
    }

    function toggleLabelsButton() {
      showMapLabels = !showMapLabels;
      const btn = document.getElementById('btn-toggle-labels');
      if (btn) btn.classList.toggle('active', showMapLabels);
      const chk1 = document.getElementById('toggle-map-labels');
      if (chk1) chk1.checked = showMapLabels;
      const chk2 = document.getElementById('toggle-voter-labels');
      if (chk2) chk2.checked = showMapLabels;
      const chk3 = document.getElementById('toggle-elector-labels');
      if (chk3) chk3.checked = showMapLabels;
      handleZoomChange();
    }

    function toggleMapLabels(checked) {
      showMapLabels = checked;
      const btn = document.getElementById('btn-toggle-labels');
      if (btn) btn.classList.toggle('active', checked);
      const chk1 = document.getElementById('toggle-map-labels');
      if (chk1) chk1.checked = checked;
      const chk2 = document.getElementById('toggle-voter-labels');
      if (chk2) chk2.checked = checked;
      const chk3 = document.getElementById('toggle-elector-labels');
      if (chk3) chk3.checked = checked;
      handleZoomChange();
    }

    function toggleMapLegend() {
      const card = document.getElementById('map-legend-card');
      if (card) {
        card.style.display = card.style.display === 'none' ? 'block' : 'none';
      }
    }

    // State Centroid Calculations
    function calculateStateCentroids() {
      const stateMap = new Map();

      geojsonLayer.eachLayer(layer => {
        if (!layer.feature || !layer.feature.electionData) return;
        const d = layer.feature.electionData;
        if (!isFeatureFilteredIn(d)) return;

        const st = d.state;
        if (!stateMap.has(st)) {
          stateMap.set(st, {
            state: st,
            partyCounts: {},
            totalSeats: 0,
            bounds: L.latLngBounds()
          });
        }
        const sObj = stateMap.get(st);
        sObj.totalSeats++;
        sObj.partyCounts[d.winner.party] = (sObj.partyCounts[d.winner.party] || 0) + 1;
        sObj.bounds.extend(layer.getBounds());
      });

      return Array.from(stateMap.values());
    }

    function renderNationalCentroids() {
      nationalCentroidLayer.clearLayers();
      stateRegionalMarkerLayer.clearLayers();
      constituencyFlagLayer.clearLayers();

      if (!showMapLabels) return;

      const stateCentroids = calculateStateCentroids();

      stateCentroids.forEach(st => {
        if (st.totalSeats === 0) return;
        const sortedParties = Object.entries(st.partyCounts).sort((a, b) => b[1] - a[1]);
        const center = st.bounds.getCenter();
        const abbr = getStateAbbr(st.state);

        let badgesHtml = '';
        sortedParties.slice(0, 2).forEach(([party, count]) => {
          const pMeta = getPartyMeta(party);
          badgesHtml += `
            <span style="background:${pMeta.color}; color:#ffffff; padding:2px 5px; border-radius:3px; font-weight:800; font-size:10px; margin-left:2px;">
              ${party} ${count}
            </span>
          `;
        });

        const iconHtml = `
          <div style="background:rgba(255,255,255,0.92); border:1px solid #0f172a; border-radius:12px; padding:2px 6px; box-shadow:0 2px 5px rgba(0,0,0,0.2); font-family:sans-serif; display:inline-flex; align-items:center; white-space:nowrap; pointer-events:auto; cursor:pointer;">
            <span style="font-weight:800; font-size:10px; color:#0f172a; margin-right:3px;">${abbr}</span>
            ${badgesHtml}
          </div>
        `;

        const customIcon = L.divIcon({
          html: iconHtml,
          className: 'national-centroid-marker',
          iconSize: [80, 24],
          iconAnchor: [40, 12]
        });

        const marker = L.marker(center, { icon: customIcon });
        marker.on('click', () => zoomToStateByName(st.state));
        nationalCentroidLayer.addLayer(marker);
      });
    }

    function renderStateView() {
      nationalCentroidLayer.clearLayers();
      stateRegionalMarkerLayer.clearLayers();
      constituencyFlagLayer.clearLayers();

      if (!showMapLabels) return;

      const stateCentroids = calculateStateCentroids();

      stateCentroids.forEach(st => {
        if (st.totalSeats === 0) return;
        const sortedParties = Object.entries(st.partyCounts).sort((a, b) => b[1] - a[1]);
        const center = st.bounds.getCenter();
        const abbr = getStateAbbr(st.state);

        let chipsHtml = '';
        sortedParties.slice(0, 3).forEach(([party, count]) => {
          const pMeta = getPartyMeta(party);
          chipsHtml += `<span style="background:${pMeta.color}; color:#fff; padding:1px 4px; border-radius:2px; font-size:9.5px; font-weight:700;">${party} ${count}</span>`;
        });

        const iconHtml = `
          <div style="background:rgba(255,255,255,0.95); border:1px solid #334155; border-radius:8px; padding:3px 6px; box-shadow:0 3px 6px rgba(0,0,0,0.15); font-family:sans-serif; display:flex; flex-direction:column; align-items:center; gap:2px; cursor:pointer;">
            <span style="font-weight:800; font-size:10px; color:#0f172a;">${abbr} (${st.totalSeats})</span>
            <div style="display:flex; gap:3px;">${chipsHtml}</div>
          </div>
        `;

        const customIcon = L.divIcon({
          html: iconHtml,
          className: 'state-regional-marker',
          iconSize: [85, 34],
          iconAnchor: [42, 17]
        });

        const marker = L.marker(center, { icon: customIcon });
        marker.on('click', () => zoomToStateByName(st.state));
        stateRegionalMarkerLayer.addLayer(marker);
      });
    }

    function renderConstituencyView() {
      nationalCentroidLayer.clearLayers();
      stateRegionalMarkerLayer.clearLayers();
      constituencyFlagLayer.clearLayers();

      if (!showMapLabels) return;
      const zoom = leafletMap.getZoom();

      geojsonLayer.eachLayer(layer => {
        if (!layer.feature || !layer.feature.electionData) return;
        const d = layer.feature.electionData;
        if (!isFeatureFilteredIn(d)) return;

        const bounds = layer.getBounds();
        const center = bounds.getCenter();
        const pMeta = getPartyMeta(d.winner.party);
        const textColor = getContrastColor(pMeta.color);
        const displayText = zoom >= 8 ? `${d.constituency} · ${d.winner.party}` : d.winner.party;

        const iconHtml = `
          <div style="background:${pMeta.color}; color:${textColor}; font-size:9.5px; font-weight:800; padding:2px 5px; border-radius:3px; border:1px solid rgba(0,0,0,0.25); box-shadow:0 1px 3px rgba(0,0,0,0.25); white-space:nowrap; text-align:center; cursor:pointer;" title="${d.constituency} (${d.state}): ${d.winner.name} · ${d.winner.party}">
            ${displayText}
          </div>
        `;

        const customIcon = L.divIcon({
          html: iconHtml,
          className: 'pc-flag-marker',
          iconSize: zoom >= 8 ? [90, 20] : [36, 18],
          iconAnchor: zoom >= 8 ? [45, 10] : [18, 9]
        });

        const marker = L.marker(center, { icon: customIcon });
        marker.on('click', () => selectConstituencyByRecord(d.state, d.constituency));
        constituencyFlagLayer.addLayer(marker);
      });
    }

    // Voter Mode Centroids (Turnout %)
    function renderVoterStateCentroids() {
      nationalCentroidLayer.clearLayers();
      stateRegionalMarkerLayer.clearLayers();
      constituencyFlagLayer.clearLayers();

      if (!showMapLabels) return;

      const stateBounds = new Map();
      geojsonLayer.eachLayer(layer => {
        if (!layer.feature || !layer.feature.voterData) return;
        const v = layer.feature.voterData;
        if (!stateBounds.has(v.state)) {
          stateBounds.set(v.state, { data: v, bounds: L.latLngBounds() });
        }
        stateBounds.get(v.state).bounds.extend(layer.getBounds());
      });

      stateBounds.forEach((stObj, stName) => {
        const v = stObj.data;
        const center = stObj.bounds.getCenter();
        const abbr = getStateAbbr(stName);
        const color = getTurnoutColor(v.pollPct);
        const textColor = getContrastColor(color);

        const iconHtml = `
          <div style="background:#ffffff; border:1.5px solid #0f172a; border-radius:6px; padding:2px 6px; box-shadow:0 2px 6px rgba(0,0,0,0.25); font-family:Inter,sans-serif; display:inline-flex; align-items:center; gap:5px; cursor:pointer;">
            <span style="font-weight:800; font-size:10px; color:#0f172a;">${abbr}</span>
            <span style="background:${color}; color:${textColor}; font-weight:800; font-size:10.5px; padding:2px 6px; border-radius:4px; border:1px solid rgba(0,0,0,0.15);">
              ${v.pollPct}%
            </span>
          </div>
        `;

        const customIcon = L.divIcon({
          html: iconHtml,
          className: 'voter-centroid-marker',
          iconSize: [85, 26],
          iconAnchor: [42, 13]
        });

        const marker = L.marker(center, { icon: customIcon });
        marker.on('click', () => selectStateVoterInfo(stName));
        nationalCentroidLayer.addLayer(marker);
      });
    }

    // Elector Mode Centroids (Grand Total)
    function renderElectorStateCentroids() {
      nationalCentroidLayer.clearLayers();
      stateRegionalMarkerLayer.clearLayers();
      constituencyFlagLayer.clearLayers();

      if (!showMapLabels) return;

      const stateBounds = new Map();
      geojsonLayer.eachLayer(layer => {
        if (!layer.feature || !layer.feature.electorData) return;
        const e = layer.feature.electorData;
        if (!stateBounds.has(e.state)) {
          stateBounds.set(e.state, { data: e, bounds: L.latLngBounds() });
        }
        stateBounds.get(e.state).bounds.extend(layer.getBounds());
      });

      stateBounds.forEach((stObj, stName) => {
        const e = stObj.data;
        const center = stObj.bounds.getCenter();
        const abbr = getStateAbbr(stName);
        const crVal = (e.grandTotal / 10000000).toFixed(1);
        const label = e.grandTotal >= 10000000 ? `${crVal} Cr` : `${(e.grandTotal / 100000).toFixed(1)} L`;
        const color = getElectorColor(e.grandTotal);
        const textColor = getContrastColor(color);

        const iconHtml = `
          <div style="background:#ffffff; border:1.5px solid #0f172a; border-radius:6px; padding:2px 6px; box-shadow:0 2px 6px rgba(0,0,0,0.25); font-family:Inter,sans-serif; display:inline-flex; align-items:center; gap:5px; cursor:pointer;">
            <span style="font-weight:800; font-size:10px; color:#0f172a;">${abbr}</span>
            <span style="background:${color}; color:${textColor}; font-weight:800; font-size:10.5px; padding:2px 6px; border-radius:4px; border:1px solid rgba(0,0,0,0.15);">
              ${label}
            </span>
          </div>
        `;

        const customIcon = L.divIcon({
          html: iconHtml,
          className: 'elector-centroid-marker',
          iconSize: [95, 26],
          iconAnchor: [47, 13]
        });

        const marker = L.marker(center, { icon: customIcon });
        marker.on('click', () => selectStateElectorInfo(stName));
        nationalCentroidLayer.addLayer(marker);
      });
    }

    /* =====================================================================
       FLOATING MAP LEGEND MANAGER (UPDATES PER MODE)
       ===================================================================== */
    function updateMapLegend() {
      const titleBox = document.getElementById('legend-title-text');
      const subBox = document.getElementById('legend-subtitle-text');
      const content = document.getElementById('legend-content-box');
      if (!titleBox || !content) return;

      if (currentMapMode === 'election') {
        titleBox.textContent = 'Winning Parties';
        subBox.textContent = '2024';

        const topParties = ['BJP', 'INC', 'SP', 'AITC', 'DMK', 'TDP', 'JD(U)', 'SHSUBT', 'NCPSP', 'IND'];
        let gridHtml = '<div class="legend-grid">';
        topParties.forEach(p => {
          const pMeta = getPartyMeta(p);
          gridHtml += `
            <div class="legend-item">
              <span class="legend-color-dot" style="background:${pMeta.color};"></span>
              <span><b>${p}</b></span>
            </div>
          `;
        });
        gridHtml += '</div>';
        content.innerHTML = gridHtml;
      } else if (currentMapMode === 'voters') {
        titleBox.textContent = 'Voter Turnout (Poll %)';
        subBox.textContent = 'ECI Table 10';

        content.innerHTML = `
          <div class="legend-scale-bar">
            <span style="background:#fef08a; flex:1;"></span>
            <span style="background:#a7f3d0; flex:1;"></span>
            <span style="background:#34d399; flex:1;"></span>
            <span style="background:#059669; flex:1;"></span>
            <span style="background:#064e3b; flex:1;"></span>
          </div>
          <div class="legend-scale-labels">
            <span>&lt; 60%</span>
            <span>60–66%</span>
            <span>66–72%</span>
            <span>72–78%</span>
            <span>&gt; 78%</span>
          </div>
          <div style="font-size:10px; color:#64748b; margin-top:6px; line-height:1.3;">
            National Average: <b>66.10%</b> (Highest: Lakshadweep 85.0%, Lowest: Bihar 56.3%)
          </div>
        `;
      } else {
        titleBox.textContent = 'Elector Population';
        subBox.textContent = 'ECI Table 9';

        content.innerHTML = `
          <div class="legend-scale-bar">
            <span style="background:#e0f2fe; flex:1;"></span>
            <span style="background:#7dd3fc; flex:1;"></span>
            <span style="background:#38bdf8; flex:1;"></span>
            <span style="background:#2563eb; flex:1;"></span>
            <span style="background:#1e1b4b; flex:1;"></span>
          </div>
          <div class="legend-scale-labels">
            <span>&lt; 20L</span>
            <span>20L–1Cr</span>
            <span>1Cr–4Cr</span>
            <span>4Cr–8Cr</span>
            <span>&gt; 8Cr</span>
          </div>
          <div style="font-size:10px; color:#64748b; margin-top:6px; line-height:1.3;">
            Total Electorate: <b>97.80 Crore</b> (Highest: UP 15.4 Cr, Lowest: Lakshadweep 57k)
          </div>
        `;
      }
    }
    """

