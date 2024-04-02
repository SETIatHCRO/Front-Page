# Automatically crops all the VNA screenshots
SCRIPT_DIR="./"
files=$SCRIPT_DIR/*
for f in $files
do
	convert -crop -155+72 $f $f
	convert -crop -0-35 $f $f
done
