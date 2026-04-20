# Submission Checklist (Double-Blind Ready)

## Identity and Metadata

- [ ] No author names in README, notebooks, scripts, comments
- [ ] No institution, lab, or city references in project text
- [ ] No personal URLs, ORCID, or social links
- [ ] Git history rewritten/sanitized if necessary
- [ ] Notebook metadata checked for identity fields

## Code and Data Hygiene

- [ ] Remove private TODO notes and personal tags
- [ ] Replace sensitive identifiers in topologies and logs
- [ ] Validate dataset license compatibility
- [ ] Add synthetic fallback datasets in `data/`

## Reproducibility

- [ ] `requirements.txt` has pinned versions
- [ ] Docker image builds without local assumptions
- [ ] Quick-start command runs in < 5 minutes
- [ ] All RQ scripts produce outputs in `results/`

## Paper Alignment

- [ ] Script-to-figure mapping included in README
- [ ] Hyperparameters and random seeds documented
- [ ] Statistical summary format matches paper tables

## Pre-Release Validation

- [ ] Fresh clone tested in isolated environment
- [ ] Dry-run all experiment scripts
- [ ] Store heavy artifacts externally (Zenodo/Figshare)
- [ ] Verify archive or hosted snapshot is publicly accessible
