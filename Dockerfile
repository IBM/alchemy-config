## Base ########################################################################
#
# This phase sets up dependencies for the other phases
##
FROM python:3.6-slim as base

# This image is only for building, so we run as root
WORKDIR /src

# Install build, test, andn publish dependencies
COPY requirements*.txt /src/
RUN true && \
    pip install pip --upgrade && \
    pip install twine && \
    pip install -r /src/requirements.txt && \
    pip install -r /src/requirements_test.txt && \
    true

## Test ########################################################################
#
# This phase runs the unit tests for the library
##
FROM base as test
COPY . /src
RUN true && \
    ./ci/run-tests.sh && \
    RELEASE_DRY_RUN=true RELEASE_VERSION=0.0.0 \
        ./ci/publish.sh && \
    true

## Release #####################################################################
#
# This phase builds the release and publishes it to pypi
##
FROM test as release
ARG PYPI_TOKEN
ARG RELEASE_VERSION
ARG RELEASE_DRY_RUN
RUN ./ci/publish.sh

## Release Test ################################################################
#
# This phase installs the indicated version from PyPi and runs the unit tests
# against the installed version.
##
FROM base as release_test
ARG RELEASE_VERSION
ARG RELEASE_DRY_RUN
COPY ./test /src/test
COPY ./ci/run-tests.sh /src/ci/run-tests.sh
RUN true && \
    ([ "$RELEASE_DRY_RUN" != "true" ] && sleep 30 || true) && \
    pip cache purge && \
    pip install alchemy-config==${RELEASE_VERSION} && \
    ./ci/run-tests.sh && \
    true
