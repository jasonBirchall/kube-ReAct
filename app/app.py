import logging

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from flask import Flask

from app.config.app_config import app_config
from app.config.logging_config import configure_logging
from app.config.routes_config import configure_routes

logger = logging.getLogger(__name__)


def create_app() -> Flask:
    configure_logging(app_config.logging_level)

    logger.info("Starting app...")

    server = Flask(__name__)

    configure_routes(server)

    app = Dash(__name__, server=server, url_base_pathname="/dashboard/")
    app.title = "⚙️ SRE Dashboard"
    app.layout = create_dashboard()

    logger.info("Running app...")

    return app.server


def create_dashboard():
    def dashboard():
        return html.Div(
            children=[
                # Header Section
                html.Div(
                    children=[
                        html.H1(
                            "☸️ Agent-Based RCA Dashboard for Kubernetes",
                            style={"text-align": "center", "margin-bottom": "20px"},
                        ),
                        html.Div(
                            "Cluster Status: Healthy",
                            style={
                                "text-align": "center",
                                "color": "green",
                                "font-weight": "bold",
                                "margin-bottom": "20px",
                            },
                        ),
                    ],
                    style={"margin-bottom": "20px"},
                ),
                # System Overview
                html.Div(
                    children=[
                        html.H2("System Overview"),
                        dcc.Graph(
                            figure=px.bar(
                                get_cluster_overview(),
                                x="Node",
                                y=["CPU Usage (%)", "Memory Usage (%)"],
                                barmode="group",
                                title="Cluster Resource Utilisation",
                                template="plotly_dark",
                            )
                        ),
                    ],
                    style={"margin-bottom": "20px"},
                ),
                # Diagnostic Workflow
                html.Div(
                    children=[
                        html.H2("Diagnostic Workflow"),
                        dcc.Graph(
                            figure=px.timeline(
                                get_diagnostic_workflow(),
                                x_start="x_start",
                                x_end="x_end",
                                y="Step",
                                color="Step",
                                title="RCA Workflow Progress",
                                hover_name="Details",
                                template="plotly_dark",
                            ),
                        ),
                    ],
                    style={"margin-bottom": "20px"},
                ),
                # RCA Results
                html.Div(
                    children=[
                        html.H2("Root Cause Analysis Results"),
                        html.Div(
                            children=[
                                html.Div(
                                    children=[
                                        html.H4("Identified Issue: High CPU Usage"),
                                        html.P(
                                            "Recommendation: Increase CPU limits for pod 'example-pod'."
                                        ),
                                    ],
                                    style={
                                        "border": "1px solid white",
                                        "padding": "10px",
                                        "margin-bottom": "10px",
                                    },
                                ),
                                html.Div(
                                    children=[
                                        html.H4("Identified Issue: CrashLoopBackOff"),
                                        html.P(
                                            "Recommendation: Restart 'service-a' to resolve CrashLoopBackOff."
                                        ),
                                    ],
                                    style={
                                        "border": "1px solid white",
                                        "padding": "10px",
                                    },
                                ),
                            ]
                        ),
                    ],
                    style={"margin-bottom": "20px"},
                ),
            ],
            style={
                "padding": "20px",
                "background-color": "black",
                "color": "white",
                "font-family": "Arial, sans-serif",
            },
        )

    return dashboard


# Placeholder Data
def get_cluster_overview():
    data = {
        "Node": ["node1", "node2", "node3"],
        "CPU Usage (%)": [45, 60, 80],
        "Memory Usage (%)": [50, 70, 85],
    }
    return pd.DataFrame(data)


def get_diagnostic_workflow():
    data = {
        "Step": ["Fetch Logs", "Check CPU", "Inspect Config"],
        "x_start": [
            "2024-12-10 10:00:00",
            "2024-12-10 10:05:00",
            "2024-12-10 10:10:00",
        ],
        "x_end": ["2024-12-10 10:05:00", "2024-12-10 10:10:00", "2024-12-10 10:15:00"],
        "Details": [
            "Fetched logs for pod 'example-pod'",
            "High CPU usage detected on 'node1'",
            "Configuration issue found in Service A",
        ],
    }
    return pd.DataFrame(data)


def get_recommendations():
    data = {
        "Action": [
            "Increase memory limit for 'example-pod'",
            "Restart 'service-a' to resolve CrashLoopBackOff",
        ],
        "Justification": [
            "Memory usage exceeded current limits",
            "Persistent failure detected in service restarts",
        ],
    }
    return pd.DataFrame(data)
