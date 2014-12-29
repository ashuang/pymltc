#!/bin/sh
# Script to scrub 277 CA data files of personally identifiable information
# Files are modified in-place

sed -i 's/NM1\*\(..\)\*2\*[A-Za-z ]\+/NM1*\1*2*ORG NAME/g' $*
sed -i 's/NM1\*\(..\)\*1\*[A-Za-z ]\+\*[a-Za-z ]\+/NM1*\1*1*LAST*FIRST/g' $*
sed -i 's/\*[A-Za-z0-9]\+\~TRN/\*1234567890\~TRN/g' $*
