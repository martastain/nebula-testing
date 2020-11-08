#!/bin/bash

base_dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

URL="http://elastic:9200"
IDX=assets

echo
echo "Deleting old index"
echo

# delete index (will print an error if 'my_index' doesn't exist, you can safely ignore it)
curl -XDELETE "$URL/$IDX"

echo
echo "Creating index"
echo

curl -XPUT -H "Content-Type: application/json" "$URL/$IDX" -d @/data/settings/elastic-assets.json

$base_dir/data_import.py /data/import/assets.json
