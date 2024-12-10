import logging

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from flask import Flask

from app.config.app_config import app_config
from app.config.logging_config import configure_logging
from app.config.routes_config import configure_routes
from app.services.database_service import DatabaseService
from app.services.figure_service import FigureService

logger = logging.getLogger(__name__)


def create_app() -> Flask:
    configure_logging(app_config.logging_level)

    logger.info("Starting app...")

    server = Flask(__name__)

    server.database_service = DatabaseService()
    server.figure_service = FigureService(server.database_service)

    configure_routes(server)

    app = Dash(__name__, server=server, url_base_pathname="/dashboard/")
    app.title = "⚙️ SRE Dashboard"
    app.layout = create_dashboard(server.figure_service)

    logger.info("Running app...")

    return app.server


def create_dashboard(figure_service: FigureService):
    """
    Creates a standard SRE dashboard layout with the Four Golden Signals:
    Latency, Traffic, Errors, and Saturation.
    """

    def dashboard():
        return html.Div(
            children=[
                html.H1("☸️ Agent-Based RCA Dashboard for Kubernetes"),
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
                # Actionable Recommendations
                html.Div(
                    children=[
                        html.H2("Actionable Recommendations"),
                        dcc.Graph(
                            figure=px.bar(
                                get_recommendations(),
                                x="Action",
                                y="Justification",
                                title="Recommended Actions",
                                template="plotly_dark",
                            )
                        ),
                    ],
                    style={"margin-bottom": "20px"},
                ),
                # Incident History (Stub)
                html.Div(
                    children=[
                        html.H2("Incident History"),
                        html.P(
                            "No incidents to display yet. RCA results will appear here."
                        ),
                    ],
                    style={"margin-bottom": "20px"},
                ),
                # System Dependencies (Stub)
                html.Div(
                    children=[
                        html.H2("System Dependencies"),
                        html.P(
                            "Visualisation of service-to-pod and pod-to-database relationships."
                        ),
                    ],
                ),
                html.Div(
                    children=[
                        html.H2("Latency"),
                        dcc.Graph(
                            figure=figure_service.get_latency_data(),  # Placeholder function
                            style={
                                "width": "100%",
                                "height": "500px",
                                "display": "inline-block",
                            },
                        ),
                    ],
                    style={"margin-bottom": "20px"},
                ),
                # Traffic
                html.Div(
                    children=[
                        html.H2("Traffic"),
                        dcc.Graph(
                            figure=figure_service.get_traffic_data(),  # Placeholder function
                            style={
                                "width": "100%",
                                "height": "500px",
                                "display": "inline-block",
                            },
                        ),
                    ],
                    style={"margin-bottom": "20px"},
                ),
                # Errors
                html.Div(
                    children=[
                        html.H2("Errors"),
                        dcc.Graph(
                            figure=figure_service.get_error_data(),  # Placeholder function
                            style={
                                "width": "100%",
                                "height": "500px",
                                "display": "inline-block",
                            },
                        ),
                    ],
                    style={"margin-bottom": "20px"},
                ),
                # Saturation
                html.Div(
                    children=[
                        html.H2("Saturation"),
                        dcc.Graph(
                            figure=figure_service.get_saturation_data(),  # Placeholder function
                            style={
                                "width": "100%",
                                "height": "500px",
                                "display": "inline-block",
                            },
                        ),
                    ],
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
    # Replace details with proper timestamps for x_start and x_end
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
