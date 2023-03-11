import json
from pathlib import Path

from config import BASE_DIR


def json_parse(config_path: Path):
    with open(config_path) as file:
        return json.load(file)


class Configurator:
    def __init__(self):
        self.player_moves = self.load_players_moves()
        self.field_config = self.load_field_config()

    @staticmethod
    def load_players_moves():
        config_path = BASE_DIR / "configs" / "moves.json"
        return json_parse(config_path)

    @staticmethod
    def load_field_config():
        config_path = BASE_DIR / "configs" / "field_config.json"
        return json_parse(config_path)
