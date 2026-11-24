# build_civiclens.py
# Compiles the clean, modular POLITIQ platform
import os
import sys

import parts.styles
import parts.html_layout
import parts.js_code
import parts.js_map_engine
import parts.js_centroids_legends
import parts.js_sidebars_details
import parts.js_bills_engine
import parts.js_init_data

def compile_civiclens():
    print("Compiling POLITIQ Platform...")
    css_content = parts.styles.get_css()
    html_body = parts.html_layout.get_html_body()

    js_parts = [
        parts.js_code.get_javascript(),
        parts.js_map_engine.get_map_engine_js(),
        parts.js_centroids_legends.get_centroids_legends_js(),
        parts.js_sidebars_details.get_sidebars_details_js(),
        parts.js_bills_engine.get_bills_engine_js(),
        parts.js_init_data.get_init_data_js()
    ]
    full_js = "\n\n".join(js_parts)

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>POLITIQ — Political Intelligence &amp; Information Quotient | Understand Politics Through Data.</title>
  
  <!-- Favicon / Brand styling -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  
  <!-- FontAwesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  
  <!-- Leaflet CSS -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin=""/>
  
  <!-- Leaflet JS -->
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
  
  <!-- PapaParse for high-speed client-side CSV processing -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.4.1/papaparse.min.js"></script>
  
  <!-- Chart.js for data visualization analytics -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>

  <style>
{css_content}
  </style>
</head>
<body>
{html_body}

  <!-- =========================================================================
       POLITIQ CORE INTELLIGENCE PLATFORM ENGINE
       Loads datasets asynchronously from ./data/ repository with live progress.
       ========================================================================= -->
  <script>
{full_js}
  </script>
</body>
</html>
"""

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_template)

    print(f"Successfully compiled index.html ({len(html_template)} bytes, ~{len(html_template)//1024} KB)")

if __name__ == '__main__':
    compile_civiclens()
