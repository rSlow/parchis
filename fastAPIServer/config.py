from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATABASE_FILE_URL = BASE_DIR / "ORM" / "db.db"
DB_ENV_FILE_PATH = BASE_DIR.parent / "env" / "pg_dev.env"

SERVER_DIR = BASE_DIR / "server.bin"
