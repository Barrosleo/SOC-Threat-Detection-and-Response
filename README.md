# SOC-Threat-Detection-and-Response

## 1. Project Goal & Overview

**SOC-Threat-Detection-and-Response** is a GitHub repository showcasing expertise in Microsoft Defender XDR, Sentinel, Purview, and threat hunting techniques. This project serves both as:

- **An Educational Resource:** It provides pre-built KQL queries for Microsoft Sentinel, incident response playbooks, and detailed guides on using Defender XDR and Purview.
- **A Practical Tool:** It offers Python scripts that automate SOC workflows—including log ingestion, alert prioritization, and threat detection—along with custom dashboards visualizing security insights.

**Target Audience:**  
SOC Level 1 analysts, threat intelligence engineers, and cybersecurity professionals looking to enhance their incident response and threat detection capabilities.

### Repository Structure

SOC-Threat-Detection-and-Response/
├── README.md
├── .gitignore
├── requirements.txt
├── CONTRIBUTING.md
├── LICENSE
├── docs/
│   ├── Microsoft_Sentinel_KQL.md
│   ├── Defender_XDR_UseCases.md
│   ├── Threat_Hunting_Playbook.md
│   ├── Incident_Response_Guide.md
│   ├── Microsoft_Purview_Data_Security.md
│   ├── SOC_Automation_Overview.md
│   └── SIEM_Log_Ingestion.md
├── scripts/
│   ├── create_sentinel_queries.py
│   ├── automate_defender_remediation.py
│   ├── detect_threats_sentinel.py
│   ├── threat_hunting_KQL_queries.py
│   ├── purview_data_security.py
│   ├── ingest_siEM_logs.py
│   ├── soc_alert_prioritization.py
│   ├── incident_response_playbooks.py
│   └── generate_incident_reports.py
├── dashboards/
│   ├── Microsoft_Defender_Dashboard.json
│   ├── Sentinel_Threat_Hunting_Dashboard.json
│   ├── SOC_Incident_Response_Dashboard.json
│   ├── Insider_Threat_Analysis_Dashboard.json
│   └── Attack_Path_Visualization_Dashboard.json
├── examples/
│   ├── simulated_incident_data.json
│   ├── threat_hunting_scenarios.md
│   ├── remediation_case_study.md
│   ├── attack_path_simulation.json
│   ├── soc_alert_triage_example.json
│   └── insider_threat_identification.json
└── notebooks/
    ├── Sentinel_KQL_Query_Tutorial.ipynb
    ├── Defender_XDR_Threat_Hunting.ipynb
    ├── SOC_Incident_Response_Workflows.ipynb
    ├── Purview_Data_Security_Insights.ipynb
    └── Automated_Threat_Detection_Using_AI.ipynb

---

## 2. Core Components & Functionality

- **Defender XDR & Endpoint Automation:**  
  `automate_defender_remediation.py` automates remediation tasks such as isolating endpoints and blocking IPs.
- **Sentinel Log Ingestion & Threat Detection:**  
  Scripts like `create_sentinel_queries.py` and `detect_threats_sentinel.py` ingest logs into Microsoft Sentinel and generate KQL-based detections.
- **Threat Hunting:**  
  `threat_hunting_KQL_queries.py` implements advanced KQL queries to hunt for lateral movement and persistence.
- **Incident Response Playbooks:**  
  Documentation in `docs/Incident_Response_Guide.md` provides step-by-step instructions for investigating and remediating alerts.
- **Purview Data Security:**  
  `purview_data_security.py` monitors for data exfiltration attempts and integrates Data Classification best practices.
- **SOC Dashboards:**  
  Custom JSON dashboards (e.g., `Microsoft_Defender_Dashboard.json`) visualize key security metrics for enhanced situational awareness.

---

## 3. Getting Started & Installation

### Prerequisites:
- Python 3.8+
- Git
- Access to Microsoft Defender, Sentinel, and Purview (or simulated data)
- (Optional) Docker for container-based deployment

### Installation:
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Barrosleo/SOC-Threat-Detection-and-Response.git
   cd SOC-Threat-Detection-and-Response
   ```
2. **Create a virtual environment and install dependencies:**
   ```
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

---

## 4. Usage Examples

### Running a Sentinel Query Script:
   ```
   python scripts/create_sentinel_queries.py --option value
   ```
### Executing a Defender Remediation Workflow:
   ```
   python scripts/automate_defender_remediation.py --option value
   ```
### Launching a SOC Dashboard (JSON is used by your SIEM tool):
(Dashboard configurations are in the dashboards folder.)
### Running a Jupyter Notebook for Incident Response:
   ```
   jupyter notebook notebooks/SOC_Incident_Response_Workflows.ipynb
   ```

---

## 5. Supporting Resources & Documentation
- **Microsoft Sentinel KQL Guide:** `docs/Microsoft_Sentinel_KQL.md`

- **Defender XDR Use Cases:** `docs/Defender_XDR_UseCases.md`

- **Threat Hunting Playbook:** `docs/Threat_Hunting_Playbook.md`

- **Incident Response Guide:** `docs/Incident_Response_Guide.md`

- **Purview Data Security Practices:** `docs/Microsoft_Purview_Data_Security.md`

- **SOC Automation Overview:** `docs/SOC_Automation_Overview.md`

- **SIEM Log Ingestion:** `docs/SIEM_Log_Ingestion.md`

---

## 6. Technical Considerations
- **Programming Languages:** Python

- **Frameworks/Libraries:** Flask, Requests, Pandas, JSON

- **Data Sources:** Public APIs, SIEM logs, simulated incident JSON files

- **Deployment Environment:** Local machine (Docker optional)

- **Version Control:** Git/GitHub

---

## 7. Desired Outcomes/Impact
- **Improve SOC Efficiency:** Automate threat detection, alert prioritization, and incident response.

- **Enhance Operational Insights:** Provide real-time dashboards and detailed playbooks.

- **Enable Hands-on Learning:** Equip analysts with practical tools and guided exercises.

---

## 8. Contributing
We welcome contributions! Please see `CONTRIBUTING.md` for contribution guidelines.

---

## 9. License
This project is licensed under the MIT License – see the `LICENSE` file for details.

---

## 10. Acknowledgements
Special thanks to the Microsoft Security community and open-source contributions that inspire continuous improvement in SOC operations.




























