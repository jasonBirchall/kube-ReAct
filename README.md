# Kubernetes Root Cause Analysis Dashboard

## Overview

This project aims to provide a real-time **Site Reliability Engineering (SRE) Dashboard** for Kubernetes environments, focusing on the **Four Golden Signals** (Latency, Traffic, Errors, and Saturation). It integrates an **agent-based diagnostic workflow** powered by Python, Dash, and Kubernetes APIs to visualise system health, provide actionable recommendations, and assist in Root Cause Analysis (RCA).

The dashboard is designed with scalability and usability in mind, making it a valuable tool for Site Reliability Engineers (SREs), DevOps engineers, and organisations operating Kubernetes clusters.

---

## Features

- **Real-Time Visualisation**:

  - Displays metrics for Latency, Traffic, Errors, and Saturation.
  - Intuitive and interactive charts powered by Dash and Plotly.

- **Agent-Based Diagnostics**:

  - Iterative workflow for RCA, leveraging Kubernetes logs, metrics, and events.
  - Dynamic reasoning to provide actionable insights.

- **Customisable Recommendations**:

  - Automatically suggests fixes for common Kubernetes issues.
  - Tracks and displays incident history.

- **Privacy-Preserving Architecture**:
  - All data processing occurs within the Kubernetes cluster.

---

## Project Structure

```
.
├── app/                          # Application logic
│   ├── app.py                    # Flask and Dash app definition
│   ├── config/                   # Configuration files
│   │   ├── app_config.py         # Application-specific configuration
│   │   ├── logging_config.py     # Logging setup
│   │   └── routes_config.py      # Flask route configuration
│   ├── routes/                   # Flask routes
│   │   ├── api_route.py          # API endpoints
│   │   └── index_route.py        # Root route
│   ├── services/                 # Core services
│   │   ├── database_service.py   # Handles database interactions
│   │   ├── figure_service.py     # Generates data for dashboard visualisations
│   │   └── __init__.py
│   ├── run.py                    # Application entry point
│   ├── assets/                   # Static files (e.g., CSS)
│   │   └── main.css              # Dashboard styling
│   └── __init__.py
├── grafana/                      # Optional Grafana setup
│   ├── Dockerfile                # Dockerfile for Grafana
│   ├── dashboards/               # Pre-configured Grafana dashboards
│   └── provisioning/             # Provisioning files for Grafana
├── helm/                         # Helm chart for Kubernetes deployment
│   └── kubera/
│       ├── Chart.yaml            # Helm chart metadata
│       ├── values-prod.yaml      # Production values
│       └── templates/            # Kubernetes templates
├── Dockerfile                    # Dockerfile for the main app
├── docker-compose.yaml           # Local development environment setup
├── pyproject.toml                # Python project metadata
├── uv.lock                       # Dependency lock file
├── README.md                     # This file
└── .dockerignore                 # Docker build exclusions
```

---

## Getting Started

### Prerequisites

- Python 3.12+
- Docker & Docker Compose
- Kubernetes Cluster (optional for production deployment)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/kubernetes-rca-dashboard.git
   cd kubernetes-rca-dashboard
   ```

2. Build and run the application using Docker Compose:

   ```bash
   docker-compose up --build
   ```

3. Access the dashboard:
   - Open your browser and navigate to `http://localhost:4567/dashboard/`.

---

## Key Concepts

### Four Golden Signals

1. **Latency**: Tracks request/response times for applications.
2. **Traffic**: Measures the volume of requests handled by the system.
3. **Errors**: Captures failure rates for requests or system operations.
4. **Saturation**: Monitors resource utilisation (CPU, memory, etc.).

### Diagnostic Workflow

- Iterative reasoning and acting process for RCA:
  1. Fetch logs, metrics, or events.
  2. Formulate hypotheses.
  3. Validate hypotheses and refine analysis.
  4. Provide actionable recommendations.

### Privacy and Security

- All data remains within the Kubernetes cluster.
- No sensitive information is transmitted externally.

---

## Deployment

### Kubernetes Deployment

1. Package the application using Helm:

   ```bash
   helm package helm/kubera
   ```

2. Deploy to your cluster:

   ```bash
   helm install kubera helm/kubera -f helm/kubera/values-prod.yaml
   ```

3. Verify the deployment:

   ```bash
   kubectl get pods
   ```

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit changes: `git commit -m "Add feature-name"`.
4. Push to the branch: `git push origin feature-name`.
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgements

- [Dash](https://dash.plotly.com/) for interactive visualisations.
- [Kubernetes](https://kubernetes.io/) for cluster orchestration.
- [Helm](https://helm.sh/) for deployment management.
- Open-source contributors for inspiration and guidance.

```

```

