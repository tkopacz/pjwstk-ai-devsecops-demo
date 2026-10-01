import json
import sys
from pathlib import Path


def findings(folder: str) -> list[str]:
    files = list(Path(folder).glob("*.sarif"))
    if not files:
        raise ValueError("CodeQL produced no SARIF; fail closed")
    failures = []
    for filename in files:
        for run in json.loads(filename.read_text(encoding="utf-8"))["runs"]:
            rules = {rule["id"]: rule for rule in run["tool"]["driver"]["rules"]}
            for result in run.get("results", []):
                rule = rules.get(result["ruleId"], {})
                severity = float(rule.get("properties", {}).get("security-severity", 0))
                if severity >= 4 or result.get("level") == "error":
                    failures.append(result["ruleId"])
    return failures


if __name__ == "__main__":
    violations = findings(sys.argv[1])
    print(json.dumps({"codeql_findings": violations}))
    raise SystemExit(bool(violations))