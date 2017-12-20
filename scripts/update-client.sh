#!/bin/bash

# Copyright 2015 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Script to fetch latest swagger spec.
# Puts the updated spec at api/swagger-spec/

set -o errexit
set -o nounset
set -o pipefail

SCRIPT_ROOT=$(dirname "${BASH_SOURCE}")

pushd "${SCRIPT_ROOT}" > /dev/null
SCRIPT_ROOT=`pwd`
popd > /dev/null

export KUBERNETES_BRANCH="release-1.8"

export CLIENT_ROOT="${SCRIPT_ROOT}/../kubernetes/client"

export CLIENT_LANGUAGE="python-tornado"

export CLIENT_VERSION="4.0.0-snapshot"

export CLEANUP_DIRS=(client/apis client/models docs test)

pushd "${CLIENT_ROOT}" > /dev/null
CLIENT_ROOT=`pwd`
popd > /dev/null

TEMP_FOLDER=$(mktemp -d) 
trap "rm -rf ${TEMP_FOLDER}" EXIT SIGINT

if [[ -z ${GEN_ROOT:-} ]]; then
    GEN_ROOT="${TEMP_FOLDER}/gen"
    echo ">>> Cloning gen repo"
    git clone --recursive https://github.com/kubernetes-client/gen.git "${GEN_ROOT}"
    echo ">>> Done"
else
    echo ">>> Reusing gen repo at ${GEN_ROOT}"
fi

export GEN_OUTPUT="${SCRIPT_ROOT}/output"
mkdir -p ${GEN_OUTPUT}

pushd "${GEN_OUTPUT}" > /dev/null
GEN_OUTPUT=`pwd`
popd > /dev/null

source "${GEN_ROOT}/openapi/client-generator.sh"
PACKAGE_NAME="kubernetes.client" kubeclient::generator::generate_client "${GEN_OUTPUT}"

echo ">>> Patching generated code..."
# fix imports
#find "${CLIENT_ROOT}" -type f -name \*.py -exec gsed -i 's/from client/from kubernetes.client/g' {} +
#find "${CLIENT_ROOT}" -type f -name \*.py -exec gsed -i 's/import client/import kubernetes.client/g' {} +
#find "${CLIENT_ROOT}" -type f -name \*.md -exec gsed -i 's/\bclient/kubernetes.client/g' {} +
#find "${CLIENT_ROOT}" -type f -name \*.md -exec gsed -i 's/kubernetes.client-python/client-python/g' {} +
echo ">>> Done"

# sadly, swagger-codegen is not smart enough to make nested packages, oh well.
cp -r ${GEN_OUTPUT}/kubernetes/client/* ${CLIENT_ROOT}/
cp -r ${GEN_OUTPUT}/kubernetes.client/* ${CLIENT_ROOT}/
cp -r ${GEN_OUTPUT}/test ${CLIENT_ROOT}/../
cp -r ${GEN_OUTPUT}/docs ${CLIENT_ROOT}/../

echo ">>> Updating version information..."
gsed -i "s/^__version__ = .*/__version__ = \\\"${CLIENT_VERSION}\\\"/g" "${CLIENT_ROOT}/../../setup.py"
echo ">>> Done"

# This is a terrible hack:
# first, this must be in gen repo not here
# second, this should be ported to swagger-codegen
#echo ">>> patching client..."
#git apply "${SCRIPT_ROOT}/rest_client_patch.diff"
#echo ">>> Done."
