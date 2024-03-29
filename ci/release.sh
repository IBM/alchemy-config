#!/usr/bin/env bash

# Run from the project root
cd $(dirname ${BASH_SOURCE[0]})/..

# Get the tag for this release
tag=$(echo $REF | cut -d'/' -f3-)

# We explicitly don't want to run with buildkit so that the docker builds happen
# in a linear fashion since our `release_test` stages intentionally don't
# inherit from the stages where the publication happens.
export DOCKER_BUILDKIT=0

# Build the docker phase that will release and then test it
docker build . \
    --target=release_test \
    --build-arg RELEASE_VERSION=$tag \
    --build-arg PYPI_TOKEN=${PYPI_TOKEN:-""} \
    --build-arg RELEASE_DRY_RUN=${RELEASE_DRY_RUN:-"false"}
