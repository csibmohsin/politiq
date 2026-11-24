# parts/js_map_engine.py

def get_map_engine_js():
    return """
    /* =====================================================================
       5. CHOROPLETH COLOR SCALES & GRADUATED PALETTES
       ===================================================================== */
    function getTurnoutColor(pct) {
      if (pct === null || pct === undefined || isNaN(pct)) return '#cbd5e1';
      if (pct < 60) return '#fef08a';
      if (pct < 66) return '#a7f3d0';
      if (pct < 72) return '#34d399';
      if (pct < 78) return '#059669';
      return '#064e3b';
    }

    function getElectorColor(val) {
      if (!val || isNaN(val)) return '#cbd5e1';
      if (val < 2000000) return '#e0f2fe';
      if (val < 10000000) return '#7dd3fc';
      if (val < 40000000) return '#38bdf8';
      if (val < 80000000) return '#2563eb';
      return '#1e1b4b';
    }

    /* =====================================================================
       6. FILTER MATCHING & HOVER ISOLATION LOGIC
       ===================================================================== */
    function isFeatureFilteredIn(d) {
      if (!d) return false;
      if (currentMapMode === 'election') {
        const stateFilter = document.getElementById('filter-election-state')?.value || 'ALL';
        const partyFilter = document.getElementById('filter-election-party')?.value || 'ALL';
        const marginFilter = document.getElementById('filter-election-margin')?.value || 'ALL';
        const catFilter = document.getElementById('filter-election-category')?.value || 'ALL';
        const searchFilter = document.getElementById('election-search-input')?.value.trim().toLowerCase() || '';

        if (stateFilter !== 'ALL' && d.state !== stateFilter) return false;
        if (partyFilter !== 'ALL' && d.winner.party !== partyFilter) return false;
        if (catFilter !== 'ALL' && d.category !== catFilter) return false;
        if (marginFilter !== 'ALL' && d.marginCategory !== marginFilter) return false;
        if (searchFilter && !(
          d.constituency.toLowerCase().includes(searchFilter) ||
          d.winner.name.toLowerCase().includes(searchFilter) ||
          d.winner.party.toLowerCase().includes(searchFilter) ||
          d.state.toLowerCase().includes(searchFilter)
        )) return false;
        return true;
      } else if (currentMapMode === 'voters') {
        const stateFilter = document.getElementById('filter-voter-state')?.value || 'ALL';
        if (stateFilter !== 'ALL' && d.state !== stateFilter) return false;
        return true;
      } else {
        const stateFilter = document.getElementById('filter-elector-state')?.value || 'ALL';
        if (stateFilter !== 'ALL' && d.state !== stateFilter) return false;
        return true;
      }
    }

    function restoreFeatureStyle(layer) {
      if (!layer || !layer.feature) return;
      const f = layer.feature;
      const d = f.electionData;
      const pass = d ? isFeatureFilteredIn(d) : true;

      if (currentMapMode === 'election') {
        if (pass && d) {
          const pMeta = getPartyMeta(d.winner.party);
          layer.setStyle({
            fillColor: pMeta.color,
            fillOpacity: 0.75,
            weight: 1,
            color: '#334155',
            opacity: 1
          });
        } else {
          layer.setStyle({
            fillColor: '#94a3b8',
            fillOpacity: 0.10,
            weight: 0.4,
            color: '#cbd5e1',
            opacity: 0.25
          });
        }
      } else if (currentMapMode === 'voters') {
        const vData = f.voterData;
        if (pass && vData) {
          const color = getTurnoutColor(vData.pollPct);
          layer.setStyle({
            fillColor: color,
            fillOpacity: 0.82,
            weight: 1,
            color: '#1e293b',
            opacity: 1
          });
        } else {
          layer.setStyle({
            fillColor: '#94a3b8',
            fillOpacity: 0.10,
            weight: 0.4,
            color: '#cbd5e1',
            opacity: 0.25
          });
        }
      } else {
        const eData = f.electorData;
        if (pass && eData) {
          const color = getElectorColor(eData.grandTotal);
          layer.setStyle({
            fillColor: color,
            fillOpacity: 0.82,
            weight: 1,
            color: '#0f172a',
            opacity: 1
          });
        } else {
          layer.setStyle({
            fillColor: '#94a3b8',
            fillOpacity: 0.10,
            weight: 0.4,
            color: '#cbd5e1',
            opacity: 0.25
          });
        }
      }
    }

    function updateGeoJsonModeStyles() {
      if (!geojsonLayer) return;

      geojsonLayer.eachLayer(layer => {
        restoreFeatureStyle(layer);
      });
    }

    /* =====================================================================
       7. LEAFLET MAP INITIALIZATION & BOUNDARY RENDERING
       ===================================================================== */
    function initMap() {
      leafletMap = L.map('india-map', {
        center: [22.9734, 78.6569],
        zoom: 5,
        minZoom: 4,
        maxZoom: 12,
        zoomControl: true,
        attributionControl: false
      });

      nationalCentroidLayer = L.layerGroup().addTo(leafletMap);
      stateRegionalMarkerLayer = L.layerGroup().addTo(leafletMap);
      constituencyFlagLayer = L.layerGroup().addTo(leafletMap);

      leafletMap.on('zoomend', handleZoomChange);
    }

    function fitMapToIndia() {
      if (geojsonLayer) {
        leafletMap.fitBounds(geojsonLayer.getBounds(), { padding: [10, 10] });
      }
    }

    function triggerNorthToSouthEntranceAnimation() {
      if (!geojsonLayer) return;
      const layersWithLat = [];
      geojsonLayer.eachLayer(layer => {
        try {
          const bounds = layer.getBounds();
          if (bounds && bounds.isValid()) {
            const center = bounds.getCenter();
            layersWithLat.push({ layer: layer, lat: center.lat });
          }
        } catch(e) {}
      });

      if (layersWithLat.length === 0) {
        handleZoomChange();
        return;
      }

      // Sort from North (highest latitude, ~35° in Kashmir/Ladakh) to South (~8° in Kanyakumari/Kerala)
      layersWithLat.sort((a, b) => b.lat - a.lat);

      const maxLat = layersWithLat[0].lat;
      const minLat = layersWithLat[layersWithLat.length - 1].lat;
      const latRange = Math.max(maxLat - minLat, 1);

      // Initially dim polygons for entrance wave
      layersWithLat.forEach(item => {
        item.layer.setStyle({ fillOpacity: 0.08, opacity: 0.15, weight: 0.4 });
      });

      // Staggered top-to-bottom illumination wave
      const waveDuration = 700; // ms
      layersWithLat.forEach(item => {
        const fraction = (maxLat - item.lat) / latRange;
        const delay = fraction * waveDuration;
        setTimeout(() => {
          restoreFeatureStyle(item.layer);
          if (item.layer._path) {
            item.layer._path.classList.add('pc-wave-in');
          }
        }, delay);
      });

      // Pop in party badges / centroids once cascading wave finishes
      setTimeout(() => {
        handleZoomChange();
      }, waveDuration + 60);
    }

    function renderGeoJsonOnMap(geo, animateEntrance = true) {
      if (geojsonLayer) {
        leafletMap.removeLayer(geojsonLayer);
      }

      geojsonLayer = L.geoJSON(geo, {
        style: function(feature) {
          const d = feature.electionData;
          const pMeta = d ? getPartyMeta(d.winner.party) : { color: '#cbd5e1' };
          return {
            fillColor: pMeta.color,
            weight: 1,
            opacity: 1,
            color: '#334155',
            fillOpacity: 0.75
          };
        },
        onEachFeature: function(feature, layer) {
          bindFeatureInteractions(feature, layer);
        }
      }).addTo(leafletMap);

      fitMapToIndia();
      if (animateEntrance) {
        triggerNorthToSouthEntranceAnimation();
      } else {
        handleZoomChange();
      }
    }

    function bindFeatureInteractions(feature, layer) {
      const d = feature.electionData;
      const v = feature.voterData;
      const e = feature.electorData;

      // Tooltip generator function
      layer.bindTooltip(() => getTooltipHtml(feature), {
        className: 'leaflet-tooltip-election',
        sticky: true,
        direction: 'top',
        offset: [0, -10]
      });

      layer.on({
        mouseover: function(evt) {
          const l = evt.target;
          if (selectedPolygonLayer === l) return;

          const pass = d ? isFeatureFilteredIn(d) : true;
          if (pass) {
            l.setStyle({
              weight: 2.8,
              color: '#0f172a',
              fillOpacity: 0.92
            });
            l.bringToFront();
          } else {
            // Strictly preserve grey dimmed appearance on hover!
            l.setStyle({
              weight: 1.2,
              color: '#94a3b8',
              fillColor: '#94a3b8',
              fillOpacity: 0.20
            });
          }
        },
        mouseout: function(evt) {
          const l = evt.target;
          if (selectedPolygonLayer !== l) {
            restoreFeatureStyle(l);
          }
        },
        click: function(evt) {
          handleFeatureClick(feature, layer);
        }
      });
    }

    function getTooltipHtml(feature) {
      const d = feature.electionData;
      const v = feature.voterData;
      const e = feature.electorData;
      const stateName = feature.properties.st_name || (d ? d.state : '');

      if (currentMapMode === 'election') {
        if (!d) return `<b>${feature.properties.pc_name || 'Constituency'}</b><br>State: ${stateName}`;
        const pMeta = getPartyMeta(d.winner.party);
        return `
          <div style="font-size:12px; font-weight:800; color:#0f172a; margin-bottom:2px;">
            ${d.constituency} <span style="font-size:10px; font-weight:600; color:#64748b;">(${d.state})</span>
          </div>
          <div style="font-size:11.5px; font-weight:700; color:${pMeta.color}; margin-bottom:4px;">
            Winner: ${d.winner.name} (${d.winner.party})
          </div>
          <div style="font-size:10.5px; color:#475569;">
            Margin: <b>${d.margin.toLocaleString('en-IN')}</b> votes (${d.marginPct}%)
          </div>
        `;
      } else if (currentMapMode === 'voters') {
        if (!v) return `<b>${stateName}</b><br>Voter info data unavailable`;
        return `
          <div style="font-size:12.5px; font-weight:800; color:#0f172a; margin-bottom:3px;">
            ${v.state} <span style="font-size:10px; font-weight:700; color:#15803d; background:#dcfce7; padding:1px 5px; border-radius:4px;">${v.pollPct}% Turnout</span>
          </div>
          <div style="font-size:11px; color:#334155; margin-bottom:2px;">
            Total Electors: <b>${v.electorsTotal.toLocaleString('en-IN')}</b>
          </div>
          <div style="font-size:11px; color:#334155; margin-bottom:2px;">
            Voters Polled: <b>${v.votersTotal.toLocaleString('en-IN')}</b>
          </div>
          <div style="font-size:10.5px; color:#64748b;">
            NOTA Votes: <b>${v.notaVotes.toLocaleString('en-IN')}</b>
          </div>
          <div style="font-size:9.5px; color:#94a3b8; margin-top:3px; border-top:1px dashed #e2e8f0; padding-top:2px;">
            State-Level Aggregated Voter Intelligence (ECI Table 10)
          </div>
        `;
      } else {
        if (!e) return `<b>${stateName}</b><br>Elector demographics data unavailable`;
        return `
          <div style="font-size:12.5px; font-weight:800; color:#0f172a; margin-bottom:3px;">
            ${e.state} <span style="font-size:10px; font-weight:700; color:#1d4ed8; background:#eff6ff; padding:1px 5px; border-radius:4px;">${(e.grandTotal / 10000000).toFixed(2)} Cr Electors</span>
          </div>
          <div style="font-size:11px; color:#334155; margin-bottom:2px;">
            Grand Total: <b>${e.grandTotal.toLocaleString('en-IN')}</b>
          </div>
          <div style="font-size:10.5px; color:#475569;">
            Male: ${e.grandM.toLocaleString('en-IN')} · Female: ${e.grandF.toLocaleString('en-IN')}
          </div>
          <div style="font-size:10.5px; color:#64748b; margin-top:2px;">
            Service: <b>${e.serviceTotal.toLocaleString('en-IN')}</b> · Overseas NRIs: <b>${e.nriTotal.toLocaleString('en-IN')}</b>
          </div>
        `;
      }
    }

    function handleFeatureClick(feature, layer) {
      if (currentMapMode === 'election') {
        const d = feature.electionData;
        if (d) selectConstituencyByRecord(d.state, d.constituency);
      } else if (currentMapMode === 'voters') {
        const v = feature.voterData;
        const stateName = v ? v.state : (feature.properties.st_name || '');
        selectStateVoterInfo(stateName);
      } else {
        const e = feature.electorData;
        const stateName = e ? e.state : (feature.properties.st_name || '');
        selectStateElectorInfo(stateName);
      }
    }
    """

