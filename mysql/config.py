""" 環境變數的設定 """
# ----------------------------- Standard Imports ----------------------------- #
import os
from pathlib import Path


class ConfigClass:
    """ 環境變數的設定 """

    # 獲取環境變數
    ENV = os.environ.get('ENV', 'dev').lower()

    # 使用 pathlib 處理路徑，更現代的做法
    PROJECTROOT = Path(__file__).parent
    PROJECTROOTRELATIVE = Path("./")
    ALEMBICDIR = PROJECTROOT / "service_alembic"

    # 從環境變數中讀取設定，並提供預設值
    PROJECT_NAME = os.getenv("PROJECT_NAME")
    RDBUSER = os.getenv("RDBUSER")
    RDBPWD = os.getenv("RDBPWD")
    RDBHOST = os.getenv("RDBHOST")
    RDBPORT = os.getenv("RDBPORT")

    # 簡化前綴生成
    ENV_PREFIX = f'{ENV}_' if ENV else ''
    ENV_PREFIX += f'{PROJECT_NAME}_'

    # 數據庫配置
    DB = ENV_PREFIX + "rdb"

    # 生成數據庫連接字符串
    SQLALCHEMY_MYSQL_URL: str = (
        f"mysql+pymysql://{RDBUSER}:{RDBPWD}@{RDBHOST}:{RDBPORT}/{DB}?charset=utf8mb4"
    )

    # 定義 alembic 資料夾名稱、資料庫名稱
    target_db_dict = {
        "alembic": DB
    }


# 實例化配置類
Config = ConfigClass()
