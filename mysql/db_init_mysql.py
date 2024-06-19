""" 初始化數據庫 """
# ----------------------------- Standard Imports ----------------------------- #
# ------------------------------ 3-Praty Imports ----------------------------- #
from sqlalchemy import (
    create_engine
)
# -------------------------------- App Imports ------------------------------- #
from config import ConfigClass
# ----------------------------- Global Variables ----------------------------- #


def create_db(db_name: str) -> None:
    """ 創建數據庫 """

    engine = create_engine(f"mysql+pymysql://{ConfigClass.RDBUSER}:{ConfigClass.RDBPWD}@{ConfigClass.RDBHOST}")
    with engine.connect() as conn:
        conn.execute(f"DROP DATABASE IF EXISTS {db_name}")
        conn.execute(
            f"CREATE DATABASE IF NOT EXISTS {db_name} DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
