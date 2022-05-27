import json
from pprint import pprint
from response_model import Response
from generate_events import generate_event

import requests


def generate():
    results = []
    for i in range(10):
        results.append(generate_event())
    with open("events.json", "w") as file:
        file.write(json.dumps(results))


def check_risk_level(file):
    if file["risk_level"] == -1:
        with open("generated_events/{}".format(file["hash"]), "rb") as f:
            res = requests.post(
                "http://localhost:8001/scan-file", files={"file": f.read()}
            )
            pprint(res.json())


def main():
    events = []
    with open("events.json", "r") as file:
        data = file.read()
        events = json.loads(data)
    for event in events[:2]:
        res = requests.post("http://localhost:8000/events", json=event)
        verdict = res.json()  # type: Response
        check_risk_level(verdict["file"])
        check_risk_level(verdict["process"])


main()
