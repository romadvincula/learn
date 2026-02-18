#!/bin/bash

for i in {0..23}
do
	curl -O -L https://data.gharchive.org/2021-01-16-$i.json.gz
done

