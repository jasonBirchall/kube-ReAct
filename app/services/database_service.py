import datetime
import logging
from typing import Any

import psycopg2

from app.config.app_config import app_config

logger = logging.getLogger(__name__)


class DatabaseService:
    def __execute_query(self, sql: str, values=None):
        with psycopg2.connect(
            dbname=app_config.postgres.db,
            user=app_config.postgres.user,
            password=app_config.postgres.password,
            host=app_config.postgres.host,
            port=app_config.postgres.port,
        ) as conn:
            logging.info("Executing query...")
            cur = conn.cursor()
            cur.execute(sql, values)
            data = None
            if cur.description is not None:
                try:
                    data = cur.fetchall()
                except Exception as e:
                    logging.error(e)

            conn.commit()
            return data

    def get_indicator(self, indicator: str) -> list[tuple[Any, Any]]:
        return self.__execute_query(
            sql="SELECT timestamp, count FROM indicators WHERE indicator = %s;",
            values=[indicator],
        )

    def create_indicators_table(self) -> None:
        self.__execute_query(
            sql="""
                    CREATE TABLE IF NOT EXISTS indicators (
                        id SERIAL PRIMARY KEY,
                        indicator varchar,
                        timestamp timestamp,
                        count integer
                    );
                """
        )

    def clean_stubbed_indicators_table(self) -> None:
        self.__execute_query(
            sql="DELETE FROM indicators WHERE indicator LIKE 'STUBBED%'"
        )

    def add_indicator(self, indicator, count) -> None:
        self.__execute_query(
            "INSERT INTO indicators (indicator,timestamp, count) VALUES (%s, %s, %s);",
            values=[indicator, datetime.datetime.now(), count],
        )
