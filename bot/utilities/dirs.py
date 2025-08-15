from pathlib import Path

WORK_DIR = Path(__file__).parent.parent.parent
LOCALES_DIR = WORK_DIR.joinpath('locales')
ENV_PATH = WORK_DIR.joinpath('.env')