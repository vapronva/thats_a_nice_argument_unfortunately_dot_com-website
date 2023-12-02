#!/bin/bash

TMP_DIR_NAME=/tmp/tnaudc-$(date +%s)
mkdir -p "${TMP_DIR_NAME}"
echo "Created temporary directory ${TMP_DIR_NAME}"

cp -r web/static/* "${TMP_DIR_NAME}"
echo "Copied static files to ${TMP_DIR_NAME}"

VERSION=$(<version.txt)

CSS_VERSIONED_DIR="${TMP_DIR_NAME}/css/_/${VERSION}"
JS_VERSIONED_DIR="${TMP_DIR_NAME}/javascript/_/${VERSION}"

mkdir -p "${CSS_VERSIONED_DIR}" "${JS_VERSIONED_DIR}"

mv "${TMP_DIR_NAME}/css/style.css" "${CSS_VERSIONED_DIR}/style.css" 2>/dev/null
echo "Moved style.css to ${CSS_VERSIONED_DIR}/style.css"

mv "${TMP_DIR_NAME}/javascript/ipd.js" "${JS_VERSIONED_DIR}/ipd.js" 2>/dev/null
echo "Moved ipd.js to ${JS_VERSIONED_DIR}/ipd.js"

# Minify CSS and JS files
find "${TMP_DIR_NAME}" \( -name "*.css" -not -name "*.min.css" \) -exec sh -c 'minify "$1" > "${1%.*}.min.css"' _ {} \;
echo "Minified CSS files"

find "${TMP_DIR_NAME}" \( -name "*.js" -not -name "*.min.js" \) -exec sh -c 'minify "$1" > "${1%.*}.min.js"' _ {} \;
echo "Minified JS files"

# BASE_URL="https://gl.vprw.ru/tnaudc/thats_a_nice_argument_unfortunately_dot_com-website/-/raw/main/web/static"
#
# wget "${BASE_URL}/video/caterpillar-linus-tnaudc-meme-recreation-1080p60fps.mp4" -P "${TMP_DIR_NAME}/video/"
# wget "${BASE_URL}/images/backgrounds/iomp/ivobl-ph-il-5.jpeg" -P "${TMP_DIR_NAME}/images/backgrounds/iomp/"
# wget "${BASE_URL}/images/backgrounds/iomp/ivobl-ph-il-6.jpeg" -P "${TMP_DIR_NAME}/images/backgrounds/iomp/"
# wget "${BASE_URL}/images/backgrounds/iomp/ivobl-ph-il-7.jpeg" -P "${TMP_DIR_NAME}/images/backgrounds/iomp/"
# wget "${BASE_URL}/images/backgrounds/mksdnr-water-mantaflow-tst/mtlqbp-mntflw-tt-6.jpeg" -P "${TMP_DIR_NAME}/images/backgrounds/mksdnr-water-mantaflow-tst/"
# echo "Downloaded large videos and images"

rclone --config rclone.conf copy "${TMP_DIR_NAME}/" slctl-sttctnaudc:static_thatsaniceargumentunfortunately_com-7e358dffde76
echo "Pushed to Selectel Storage"

rm -rf "${TMP_DIR_NAME}"
echo "Deleted temporary directory ${TMP_DIR_NAME}"
