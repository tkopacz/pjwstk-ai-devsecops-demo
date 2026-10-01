import json

from app import classify


CASES = [
    ("Reset password", "SYNTHETIC-1", "IT", "PASS"),
    ("Opening hours", "SYNTHETIC-2", "GENERAL", "PASS"),
    ("Reset password", "", "REVIEW", "BLOCK"),
    ("", "SYNTHETIC-1", "REVIEW", "BLOCK"),
    ("PASSWORD reset", "SYNTHETIC-3", "IT", "PASS"),
]


def evaluate() -> list[dict]:
    return [
        {"case": index, "expected": {"queue": queue, "decision": decision},
         "actual": classify(text, source),
         "passed": classify(text, source) == {"queue": queue, "decision": decision}}
        for index, (text, source, queue, decision) in enumerate(CASES, 1)
    ]


if __name__ == "__main__":
    results = evaluate()
    print(json.dumps(results, indent=2))
    raise SystemExit(0 if all(result["passed"] for result in results) else 1)