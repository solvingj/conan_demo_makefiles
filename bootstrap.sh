#!/bin/bash

repos="libA libB libC libD App App2"

for repo in `echo $repos`; do

    pushd $repo
    echo "--- creating $repo locally"
    git init 
    git add . 
    git commit -m "initial commit"
    echo "--- running conan create locally"
    conan create . mycompany/demo
    popd
done

