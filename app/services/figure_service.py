import pandas as pd
import plotly.express as px


class FigureService:
    def __init__(self, database_service):
        self.database_service = database_service

    def get_latency_data(self):
        # Stub data for latency
        data = {
            "Time": ["10:00", "10:05", "10:10", "10:15", "10:20"],
            "Latency (ms)": [120, 150, 100, 200, 170],
        }
        df = pd.DataFrame(data)

        # Create a line graph
        fig = px.line(
            df,
            x="Time",
            y="Latency (ms)",
            title="Latency Over Time",
            markers=True,
            template="plotly_dark",
        )
        fig.add_hline(
            y=200, line_dash="dash", line_color="red", annotation_text="Threshold"
        )

        return fig

    def get_traffic_data(self):
        # Stub data for traffic
        data = {
            "Time": ["10:00", "10:05", "10:10", "10:15", "10:20"],
            "Requests per Second": [50, 60, 45, 70, 65],
        }
        df = pd.DataFrame(data)

        # Create a bar chart
        fig = px.bar(
            df,
            x="Time",
            y="Requests per Second",
            title="Traffic Over Time",
            template="plotly_dark",
        )

        return fig

    def get_error_data(self):
        # Stub data for errors
        data = {
            "Time": ["10:00", "10:05", "10:10", "10:15", "10:20"],
            "Error Rate (%)": [1.5, 2.0, 0.5, 3.0, 2.5],
        }
        df = pd.DataFrame(data)

        # Create an area chart
        fig = px.area(
            df,
            x="Time",
            y="Error Rate (%)",
            title="Error Rate Over Time",
            template="plotly_dark",
        )
        fig.add_hline(
            y=2.5, line_dash="dash", line_color="orange", annotation_text="Alert Level"
        )

        return fig

    def get_saturation_data(self):
        # Stub data for saturation
        data = {
            "Time": ["10:00", "10:05", "10:10", "10:15", "10:20"],
            "CPU Utilization (%)": [50, 70, 60, 80, 75],
        }
        df = pd.DataFrame(data)

        # Create a line graph with markers
        fig = px.line(
            df,
            x="Time",
            y="CPU Utilization (%)",
            title="CPU Saturation Over Time",
            markers=True,
            template="plotly_dark",
        )
        fig.add_hline(
            y=80,
            line_dash="dash",
            line_color="red",
            annotation_text="Critical Threshold",
        )

        return fig
