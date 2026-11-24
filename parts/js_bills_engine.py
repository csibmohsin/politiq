# parts/js_bills_engine.py

def get_bills_engine_js():
    return """
    /* =====================================================================
       11. LEGISLATIVE INTELLIGENCE & ANIMATED BILL TIMELINE ENGINE
       ===================================================================== */
    function filterBills() {
      const searchVal = document.getElementById('bill-search-input')?.value.trim().toLowerCase() || '';
      const yearVal = document.getElementById('bill-year-select')?.value || 'ALL';
      const sortVal = document.getElementById('bill-sort-select')?.value || 'newest';

      filteredBills = billRecords.filter(b => {
        // Search filter
        if (searchVal) {
          const matchTitle = b.title.toLowerCase().includes(searchVal);
          const matchNo = b.billNo.toLowerCase().includes(searchVal);
          const matchYear = b.year.includes(searchVal);
          const matchStatus = b.status.toLowerCase().includes(searchVal);
          if (!matchTitle && !matchNo && !matchYear && !matchStatus) return false;
        }

        // Year filter
        if (yearVal !== 'ALL' && b.year !== yearVal) return false;

        // Decade filter
        if (activeDecade !== 'ALL') {
          const bYear = parseInt(b.year, 10);
          const dStart = parseInt(activeDecade, 10);
          if (isNaN(bYear) || bYear < dStart || bYear > dStart + 9) return false;
        }

        return true;
      });

      // Sort
      if (sortVal === 'newest') {
        filteredBills.sort((a, b) => parseInt(b.year || '0', 10) - parseInt(a.year || '0', 10));
      } else if (sortVal === 'oldest') {
        filteredBills.sort((a, b) => parseInt(a.year || '0', 10) - parseInt(b.year || '0', 10));
      } else if (sortVal === 'title') {
        filteredBills.sort((a, b) => a.title.localeCompare(b.title));
      }

      billsPage = 1;
      renderBillsList();
    }

    function onBillFilterChange() {
      filterBills();
    }

    function selectDecade(decade) {
      activeDecade = decade;
      document.querySelectorAll('.decade-pill-btn').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('data-decade') === decade);
      });
      filterBills();
    }

    function renderBillsList() {
      const container = document.getElementById('bills-grid-container');
      const badge = document.getElementById('bills-count-badge');
      if (!container) return;

      if (badge) badge.textContent = `Showing ${filteredBills.length} of ${billRecords.length} Bills`;

      if (filteredBills.length === 0) {
        container.innerHTML = `
          <div style="grid-column: 1 / -1; padding: 60px 20px; text-align: center; color: var(--text-muted);">
            <div style="font-size: 16px; font-weight: 700; color: var(--text-navy); margin-bottom: 6px;">No Parliamentary Bills Found</div>
            <div style="font-size: 12px;">Try adjusting your search terms, year selector, or decade filters.</div>
          </div>
        `;
        return;
      }

      const displayBills = filteredBills.slice(0, billsPage * BILLS_PER_PAGE);

      let html = '';
      displayBills.forEach((b) => {
        const introDate = b.introDate && b.introDate !== 'NA' ? b.introDate : 'Recorded in RS';
        const assentDate = b.assentDate && b.assentDate !== 'NA' ? b.assentDate : 'Assented';

        html += `
          <div class="bill-card" onclick="openBillTimelineModal('${b.id}')">
            <div>
              <div class="bill-card-top">
                <div class="bill-badge-group">
                  <span class="badge-year">${b.year}</span>
                  <span class="badge-billno">Bill No. ${b.billNo}</span>
                  <span class="badge-status">${b.status}</span>
                </div>
              </div>
              <div class="bill-title" style="margin-top: 10px;">${b.title}</div>
            </div>

            <div>
              <div class="bill-dates-row">
                <div class="bill-date-box">
                  <span class="bill-date-label">Date Introduced</span>
                  <span class="bill-date-val">${introDate}</span>
                </div>
                <div class="bill-date-box">
                  <span class="bill-date-label">Assent Date</span>
                  <span class="bill-date-val">${assentDate}</span>
                </div>
              </div>

              <div class="bill-action-row">
                <span style="font-size: 10px; color: var(--text-muted);">Rajya Sabha Legislative Track</span>
                <button class="btn-track-bill">
                  <span>Track Timeline</span>
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
                </button>
              </div>
            </div>
          </div>
        `;
      });

      if (filteredBills.length > displayBills.length) {
        html += `
          <div style="grid-column: 1 / -1; text-align: center; padding: 16px;">
            <button class="btn btn-primary" onclick="loadMoreBills()">
              Load More Bills (${filteredBills.length - displayBills.length} remaining)
            </button>
          </div>
        `;
      }

      container.innerHTML = html;
    }

    function loadMoreBills() {
      billsPage++;
      renderBillsList();
    }

    /* =====================================================================
       ANIMATED BILL TIMELINE MODAL & GOOGLE SEARCH
       ===================================================================== */
    function openBillTimelineModal(billId) {
      const bill = billRecords.find(b => b.id === billId);
      if (!bill) return;
      currentSelectedBill = bill;

      document.getElementById('modal-bill-title').textContent = bill.title;
      document.getElementById('modal-bill-badges').innerHTML = `
        <span class="badge-year">${bill.year}</span>
        <span class="badge-billno">Bill No. ${bill.billNo}</span>
        <span class="badge-status">${bill.status}</span>
        <span class="badge-billno">Rajya Sabha</span>
      `;

      // Milestones Data
      const introDate = (bill.introDate && bill.introDate !== 'NA') ? bill.introDate : 'Not Available';
      const rsDate = (bill.rsDate && bill.rsDate !== 'NA') ? bill.rsDate : 'Passed in RS';
      const lsDate = (bill.lsDate && bill.lsDate !== 'NA') ? bill.lsDate : 'Passed in LS';
      const commDate = (bill.committee && bill.committee !== 'NA') ? bill.committee : 'Not Referred / NA';
      const assentDate = (bill.assentDate && bill.assentDate !== 'NA') ? bill.assentDate : 'Assented';

      document.getElementById('step-intro-date').textContent = introDate;
      document.getElementById('step-rs-date').textContent = rsDate;
      document.getElementById('step-ls-date').textContent = lsDate;
      document.getElementById('step-comm-date').textContent = commDate;
      document.getElementById('step-assent-date').textContent = assentDate;

      // Statuses
      const stepComm = document.getElementById('step-4');
      if (commDate === 'Not Referred / NA' || commDate === 'Not Available') {
        stepComm.className = 'timeline-step bypassed';
        document.getElementById('step-comm-status').textContent = 'Bypassed/NA';
      } else {
        stepComm.className = 'timeline-step completed';
        document.getElementById('step-comm-status').textContent = 'Report Presented';
      }

      // Reset and trigger track animation
      const fillBar = document.getElementById('timeline-fill-bar');
      fillBar.style.animation = 'none';
      setTimeout(() => fillBar.style.animation = '', 10);

      // Google Search button setup
      document.getElementById('google-search-title-display').textContent = bill.title;
      const searchBtn = document.getElementById('btn-google-search-action');
      searchBtn.onclick = () => searchBillOnGoogle(bill.title, bill.year);

      // Full table
      const table = document.getElementById('modal-bill-table');
      table.innerHTML = `
        <tbody>
          <tr><td>Complete Short Title</td><td><b>${bill.title}</b></td></tr>
          <tr><td>Year of Legislation</td><td>${bill.year}</td></tr>
          <tr><td>Parliamentary Bill Number</td><td>${bill.billNo}</td></tr>
          <tr><td>Date of Introduction</td><td>${introDate}</td></tr>
          <tr><td>Debate / Passed in Rajya Sabha</td><td>${rsDate}</td></tr>
          <tr><td>Debate / Passed in Lok Sabha</td><td>${lsDate}</td></tr>
          <tr><td>Referred to Committee</td><td>${commDate}</td></tr>
          <tr><td>Assent Date / Gazette Notification / Act No.</td><td>${assentDate}</td></tr>
          <tr><td>Official Synopsis</td><td>${bill.synopsis && bill.synopsis !== 'NA' ? bill.synopsis : 'Official parliamentary enactment text recorded under Rajya Sabha Gazette.'}</td></tr>
          <tr><td>Current Legislative Status</td><td><span class="badge-status">${bill.status}</span></td></tr>
        </tbody>
      `;

      document.getElementById('bill-timeline-modal').classList.add('active');
    }

    function closeBillModal() {
      document.getElementById('bill-timeline-modal').classList.remove('active');
      currentSelectedBill = null;
    }

    function searchBillOnGoogle(billTitle, year) {
      const query = `${billTitle} ${year} India Parliament Rajya Sabha`;
      window.open('https://www.google.com/search?q=' + encodeURIComponent(query), '_blank');
    }

    function showMilestoneDetail(stage) {
      if (!currentSelectedBill) return;
      const b = currentSelectedBill;
      let msg = '';
      if (stage === 'intro') {
        msg = `Bill was formally introduced on ${b.introDate || 'the recorded date'} in Parliament.`;
      } else if (stage === 'rs') {
        msg = `Debated and passed by the Rajya Sabha (Council of States) on ${b.rsDate || 'record'}.`;
      } else if (stage === 'ls') {
        msg = `Debated and passed by the Lok Sabha (House of the People) on ${b.lsDate || 'record'}.`;
      } else if (stage === 'committee') {
        msg = b.committee && b.committee !== 'NA' ? `Committee details: ${b.committee}` : `This bill was not referred to a parliamentary committee.`;
      } else {
        msg = `Received Presidential Assent and published in the Gazette of India on ${b.assentDate || 'record'}.`;
      }
      alert(msg);
    }
    """

