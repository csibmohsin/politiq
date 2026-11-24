# POLITIQ — Political Intelligence & Information Quotient

<p align="center">
  <strong>Understand Politics Through Data.</strong><br>
  <em>India's Premier National Public Data & Legislative Intelligence Platform</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-POLITIQ-0f172a?style=for-the-badge&logo=shield" alt="Platform">
  <img src="https://img.shields.io/badge/Status-Production_Ready-10b981?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/Data-ECI_&_Rajya_Sabha-38bdf8?style=for-the-badge" alt="Data Source">
  <a href="https://csibmohsin.github.io/politiq/"><img src="https://img.shields.io/badge/Live_Demo-csibmohsin.github.io%2Fpolitiq-f59e0b?style=for-the-badge&logo=github" alt="Live Demo"></a>
</p>

---

## 🌐 Live Website

Access the live platform hosted on GitHub Pages:
🔗 **[https://csibmohsin.github.io/politiq/](https://csibmohsin.github.io/politiq/)**

---

## 🌟 Overview

**POLITIQ** is a government-grade, client-side political intelligence platform designed for researchers, journalists, policymakers, and citizens. It delivers a unified, zero-fabrication visualization of India's democratic landscape using four official public datasets:

1. **2024 Lok Sabha Election Results:** 543 Parliamentary Constituencies with winning parties, runner-ups, vote shares, and margin classifications.
2. **Voter Information & Turnout (ECI Table 10):** 109 state-level aggregate records across General, SC, and ST seats, postal votes, and NOTA.
3. **State-Wise Registered Electors (ECI Table 9):** Demographic distribution across Male, Female, Third Gender, NRI, and Service voters.
4. **Rajya Sabha Legislative Intelligence:** 727 historical bills enacted into law with presidential assent from 1952 to 2016.

---

## 🚀 Key Features

- **One Map, Three Visual Modes:** Seamlessly switch between Election Results, Voter Turnout, and Elector Demographics on a single unified Leaflet map instance without page reloads.
- **Top-to-Bottom State Entrance Wave:** Cascading geographical illumination from Ladakh & Kashmir down to Kanyakumari & Kerala.
- **Civic Intelligence Loading Screen:** Animated radar pulse, live progress bar, and rotating civic insights ticker featuring historical milestones.
- **Dynamic Zoom Resolution:** National overview at low zoom; immediate solo constituency party badges upon the first zoom notch (`zoom > 5`), expanding to detailed constituency names at closer zoom (`zoom >= 8`).
- **Legislative Explorer & Interactive Timeline:** Search 727 enacted bills by title, year, or status. Click any bill to view its animated milestone timeline (Introduction → Lok Sabha → Rajya Sabha → Committee → Presidential Assent) with one-click Google Search integration.
- **100% Mobile & Desktop Responsive:** Adaptive bottom navigation bar, sliding sidebars, high-contrast badges, and touch-friendly controls.

---

## 📂 Repository Structure

```
POLITIQ/
│
├── index.html                    # Lightweight client-side application (~210 KB)
│
├── data/                         # Official raw public datasets
│   ├── 4_List_of_Successful_Candidate_0.csv      # Lok Sabha 2024 Winners & Runners-up
│   ├── 10_Voters_Information_4.csv              # ECI Table 10 Turnout & Postal Votes
│   ├── 9_State_Wise_Number_Of_Electors_1.csv     # ECI Table 9 Demographic Electors
│   ├── rs_status_bill_passed_assent-1952-2016.csv # 727 Rajya Sabha Acts (1952-2016)
│   └── india_pc_2019_simplified.geojson          # 543 Parliamentary Constituency Polygons
│
├── parts/                        # Modular Python build components
│   ├── html_layout.py
│   ├── styles.py
│   ├── js_map_engine.py
│   ├── js_centroids_legends.py
│   ├── js_sidebars_details.py
│   ├── js_bills_engine.py
│   └── js_init_data.py
│
├── build_civiclens.py            # Automated build script
├── .gitignore                    # Clean Git configuration
└── README.md                     # Platform documentation
```

---

## 💻 Local Quickstart

Run a local HTTP server from the project directory:

```bash
# Python 3
python -m http.server 8080
```

Open your browser at:
```
http://localhost:8080/
```

---

## 🌐 Deploying to GitHub Pages (`POLITIQ.github.io`)

### Option A: As Your Primary User Site (`username.github.io`)

If you want the URL to be `https://<your-username>.github.io/`:

1. On GitHub, create a new repository named exactly:
   ```
   <your-username>.github.io
   ```
   *(For example, if your username is `csib-mohsin`, name the repo `csib-mohsin.github.io`)*.

2. Run these commands in your project folder:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: POLITIQ Intelligence Platform"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-username>.github.io.git
   git push -u origin main
   ```

3. Your website will be live at `https://<your-username>.github.io/` within 60 seconds!

---

### Option B: As a Project Site (`username.github.io/politiq`)

If you want the repository to be named `politiq`:

1. On GitHub, create a new public repository named:
   ```
   politiq
   ```

2. Run these commands in your project folder:
   ```bash
   git init
   git add .
   git commit -m "Initial release: POLITIQ Intelligence Platform"
   git branch -M main
   git remote add origin https://github.com/<your-username>/politiq.git
   git push -u origin main
   ```

3. Enable GitHub Pages:
   - Go to your repository on GitHub.
   - Click **Settings** > **Pages** (in the left sidebar).
   - Under **Build and deployment > Branch**, select `main` branch and `/ (root)` folder.
   - Click **Save**.
   - Your site will be live at `https://<your-username>.github.io/politiq/`!

---

## 🔒 Data Transparency & Integrity

All data presented in POLITIQ is sourced directly from verified public records:
- **Election Commission of India (ECI):** General Election 2024 results, Table 9 (Electors), and Table 10 (Voters).
- **Rajya Sabha Secretariat:** Status of Government Bills Passed by Parliament and Assented to by the President (1952–2016).
- **DataMeet:** Simplified 2019/2024 Parliamentary Constituency Boundaries GeoJSON.

Zero synthetic data fabrication or altered voting counts.

---

## 👤 Author & Credits

- **Platform:** POLITIQ
- **Developer:** **Mohsin Khawaja** ([@csib.mohsin](https://instagram.com/csib.mohsin))
- **License:** Open for educational, academic, and non-commercial public research.

