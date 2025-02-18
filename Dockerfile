# Container image that runs your code
FROM --platform=$BUILDPLATFORM debian:stable-slim AS base

RUN apt-get update
RUN apt-get install wget -y
RUN wget -q https://github.com/CycloneDX/sbom-utility/releases/download/v0.17.0/sbom-utility-v0.17.0-linux-amd64.tar.gz
RUN tar -xvzf sbom-utility-v0.17.0-linux-amd64.tar.gz


FROM debian:stable-slim

COPY analyze_and_check_sbom.sh check_usage_policy.py /
RUN chmod +x /analyze_and_check_sbom.sh
COPY --from=base /sbom-utility /license.json /
RUN chmod +x ./sbom-utility
RUN ls -la
RUN apt-get update
RUN apt-get install python3 -y
ENTRYPOINT [ "sh", "-c", "/analyze_and_check_sbom.sh"]
