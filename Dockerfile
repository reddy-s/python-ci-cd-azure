FROM python:3.6-alpine

LABEL maintainer="Sangram Reddy"
LABEL email="reddy.horcrux@gmail.com"
LABEL name="Python-CI-CD-Azure"
LABEL version=1.0.0

COPY ./IntegrationPackage/dist/Integration-*3*.whl /workspace/
COPY ./WrapperPackage/dist/Wrapper-*3*.whl /workspace/
COPY ./WrapperPackage/run.py /workspace/run.py

RUN pip install --no-cache-dir /workspace/Integration-*3*.whl && \
    pip install --no-cache-dir /workspace/Wrapper-*3*.whl && \
    chmod +x /workspace/run.py && \
    echo -e '#!/bin/sh\npython /workspace/run.py "$@"' >> /usr/bin/python_ci_cd_azure && \
    chmod +x /usr/bin/python_ci_cd_azure && \
    rm -rf /workspace/*.whl

CMD ["python_ci_cd_azure", "inner"]
