#!/bin/bash

TMP_DIR_NAME=/tmp/tnaudc-$(date +%s)
mkdir -p "${TMP_DIR_NAME}"
echo "Created temporary directory ${TMP_DIR_NAME}"

cp -r web/static/* "${TMP_DIR_NAME}"
echo "Copied static files to ${TMP_DIR_NAME}"

mkdir -p "${TMP_DIR_NAME}/css/_/$(cat version.txt)" || true
mv "${TMP_DIR_NAME}/css/style.css" "${TMP_DIR_NAME}/css/_/$(cat version.txt)/style.css" || true
echo "Moved style.css to ${TMP_DIR_NAME}/css/_/$(cat version.txt)/style.css" || true

mkdir -p "${TMP_DIR_NAME}/javascript/_/$(cat version.txt)" || true
mv "${TMP_DIR_NAME}/javascript/ipd.js" "${TMP_DIR_NAME}/javascript/_/$(cat version.txt)/ipd.js" || true
echo "Moved ipd.js to ${TMP_DIR_NAME}/javascript/_/$(cat version.txt)/ipd.js" || true

find "${TMP_DIR_NAME}" -name "*.css" -exec uglifycss --output "{}.min" "{}" \;
while IFS= read -r -d "" file; do
	mv "${file}" "${file/.css.min/}.min.css"
done < <(find "${TMP_DIR_NAME}" -name "*.css.min" -print0) || true
echo "Minified CSS files"

find "${TMP_DIR_NAME}" -name "*.js" -exec uglifyjs --compress --mangle --output "{}.min" "{}" \;
while IFS= read -r -d "" file; do
	mv "${file}" "${file/.js.min/}.min.js"
done < <(find "${TMP_DIR_NAME}" -name "*.js.min" -print0) || true
echo "Minified JS files"

wget https://gl.vprw.ru/tnaudc/thats_a_nice_argument_unfortunately_dot_com-website/-/raw/main/web/static/video/caterpillar-linus-tnaudc-meme-recreation-1080p60fps.mp4 -O "${TMP_DIR_NAME}/video/caterpillar-linus-tnaudc-meme-recreation-1080p60fps.mp4"
wget https://gl.vprw.ru/tnaudc/thats_a_nice_argument_unfortunately_dot_com-website/-/raw/main/web/static/images/backgrounds/iomp/ivobl-ph-il-5.jpeg -O "${TMP_DIR_NAME}/images/backgrounds/iomp/ivobl-ph-il-5.jpeg"
wget https://gl.vprw.ru/tnaudc/thats_a_nice_argument_unfortunately_dot_com-website/-/raw/main/web/static/images/backgrounds/iomp/ivobl-ph-il-6.jpeg -O "${TMP_DIR_NAME}/images/backgrounds/iomp/ivobl-ph-il-6.jpeg"
wget https://gl.vprw.ru/tnaudc/thats_a_nice_argument_unfortunately_dot_com-website/-/raw/main/web/static/images/backgrounds/iomp/ivobl-ph-il-7.jpeg -O "${TMP_DIR_NAME}/images/backgrounds/iomp/ivobl-ph-il-7.jpeg"
wget https://gl.vprw.ru/tnaudc/thats_a_nice_argument_unfortunately_dot_com-website/-/raw/main/web/static/images/backgrounds/mksdnr-water-mantaflow-tst/mtlqbp-mntflw-tt-6.jpeg -O "${TMP_DIR_NAME}/images/backgrounds/mksdnr-water-mantaflow-tst/mtlqbp-mntflw-tt-6.jpeg"
echo "Downloaded large videos and images"

rclone --config rclone.conf copy "${TMP_DIR_NAME}/" slctl-sttctnaudc:static_thatsaniceargumentunfortunately_com-7e358dffde76
echo "Pushed to Selectel Storage"

rm -rf "${TMP_DIR_NAME}"
echo "Deleted temporary directory ${TMP_DIR_NAME}"
