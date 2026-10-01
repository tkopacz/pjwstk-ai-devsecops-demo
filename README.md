# Synthetic PR Security Gates

Public classroom repository. All tickets and sources are synthetic. No customer data, credentials or production runtime.

Required checks: tests-eval, native CodeQL (GitHub Advanced Security publisher), dependency-review. Native secret scanning and push protection are enabled. Dependabot opens reviewable update PRs; no automatic merge.

Python application uses only the standard library: `python -m unittest -v test_app` and `python evaluate.py`. Never install dependencies under scan-only and never execute inert_fixture.py on a negative branch.

Main requires a human code-owner review and passing checks, also for administrators. PRE-PROD requires a human environment decision. release.yml can reach waiting approval for a green open PR, but actual Azure login requires that a human has already reviewed and merged that PR. Approval cannot bypass merge protection.

OIDC uses UAMI with no client secret, exact repository_id/environment/workflow_ref/ref subject, and own-RG-only release writer. The release deploys a synthetic reviewed-SHA tag, not a hosted application. No approval or merge is automated.

Only the owner currently has reviewer access. Own PR cannot be self-approved; add a second human collaborator before merging. Environment self-review prevention is unavailable in this single-reviewer setup and is explicitly not claimed.