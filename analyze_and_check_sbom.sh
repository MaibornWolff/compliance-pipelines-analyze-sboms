#!/bin/sh
/sbom-utility license list --input-file=$SBOM_PATH --format=txt --config-license=$LICENSE_POLICY_PATH -o=evaluated_sbom.txt
python3 /check_usage_policy.py --pipelinebreak $BREAK_ENABLED evaluated_sbom.txt