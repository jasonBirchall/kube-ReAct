import logging

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

    logger.info("Populating stub data...")
    server.database_service.create_indicators_table()
    server.database_service.clean_stubbed_indicators_table()

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
                html.H1("SRE Dashboard - Four Golden Signals"),
                # Latency
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
