#!/bin/bash
set -eo pipefail

function build-docs () {
    echo "Building the documentation"
    mkdir /tmp/site
    cd /tmp/site
    git clone https://$GITHUB_USER:$GITHUB_TOKEN%40$GITHUB_EMAIL@github.com/absa-subatomic/subatomic-documentation.git .
    git checkout gh-pages
    cd -
    mkdocs build --strict -d /tmp/site
}

function publish-docs () {
    echo "Publishing the documentation"
    cd /tmp/site
    echo "subatomic.bison.ninja" > CNAME
    git add .
    git commit -a -m "Built from ${TRAVIS_COMMIT}"
    git push
}

function main () {
    build-docs || return 1

    if [[ "$TRAVIS_BRANCH" == "master" ]] && [[ "$TRAVIS_PULL_REQUEST" == false ]]; then
        # build docs on each commit but only from master
        publish-docs || return 1
    fi
}

main "$@" || exit 1
exit 0
