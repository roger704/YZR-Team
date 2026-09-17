# Reviewed deployment preflight

The deployment job now requires an authoritative Nexus review decision for its
exact source SHA before publication, using ephemeral GitHub Actions OIDC. Existing
build/test and publication steps remain in place. Configure the Nexus preflight
repository/workflow/environment policy before deploying; unavailable or unreviewed
source fails closed. This entry describes the change, not a completed deployment.
