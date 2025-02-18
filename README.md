# Analyze SBOMS

GitHub Action to analyze whether licenses of an SBOM are compliant.


# Usage
```yaml
- uses: MaibornWolff/compliance-pipelines-analyze-sboms@v1
  with:
    # The path to your SBOM in the repository. [Required]
    SBOM_PATH: ''
    # The path to the license policy in the repository
    # Default: /license.json
    LICENSE_POLICY_PATH: ''
    # Whether to break the pipeline, by exiting with an error,
    # in case of license non-compliance
    BREAK_ENABLED: false
```