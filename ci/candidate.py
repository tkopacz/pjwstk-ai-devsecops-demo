import json
import os
import urllib.request


def github(path: str):
    request = urllib.request.Request(
        f"https://api.github.com/repos/{os.environ['GITHUB_REPOSITORY']}/{path}",
        headers={"Authorization": f"Bearer {os.environ['GH_TOKEN']}",
                 "Accept": "application/vnd.github+json", "User-Agent": "pjwstk-gate"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


if __name__ == "__main__":
    candidate = github(f"pulls/{int(os.environ['CANDIDATE_PR'])}")
    assert candidate["base"]["ref"] == "main"
    assert candidate["head"]["repo"]["full_name"] == os.environ["GITHUB_REPOSITORY"]
    checks = github(f"commits/{candidate['head']['sha']}/check-runs?per_page=100")["check_runs"]
    for name in ("tests-eval", "codeql", "dependency-review"):
        matches = [check for check in checks if check["name"] == name and check["app"]["slug"] == "github-actions"]
        assert matches, f"Missing {name}"
        latest = max(matches, key=lambda check: check["id"])
        assert latest["conclusion"] == "success", f"Failed {name}"
    if os.environ.get("REQUIRE_MERGED") == "true":
        assert candidate["merged"], "A human must review and merge the PR; approval is not a merge bypass"
    print(json.dumps({"pr": candidate["number"], "sha": candidate["head"]["sha"], "merged": candidate["merged"]}))