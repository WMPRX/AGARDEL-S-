import json


def generate_json_report(metrics: dict, trades: list[dict]) -> str:
    return json.dumps({"metrics": metrics, "trades": trades}, indent=2)
