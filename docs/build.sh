#!/usr/bin/env bash

# this scripts needs to be called from the Project's root dir


DOCS_DIR=docs
DOCS_BUILD_DIR=$DOCS_DIR/_build
DOCS_BUILD_DOCTREES_DIR=$DOCS_BUILD_DIR/.doctrees
DOCS_BUILD_IMAGES_DIR=$DOCS_BUILD_DIR/_images
DOCS_BUILD_SOURCES_DIR=$DOCS_BUILD_DIR/_sources


rm $DOCS_DIR/*.rst
rm $DOCS_BUILD_DIR/*.html
rm $DOCS_BUILD_DOCTREES_DIR/*.doctree
rm $DOCS_BUILD_IMAGES_DIR/*
rm $DOCS_BUILD_SOURCES_DIR/*.txt


sh $DOCS_DIR/parse-docstr.sh


sphinx-autobuild $DOCS_DIR $DOCS_BUILD_DIR