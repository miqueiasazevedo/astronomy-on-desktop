#!/bin/sh
PICTURE_DIR=$1
echo $PICTURE_DIR
/usr/bin/osascript<<END
tell application "System Events" to set picture of every desktop to ("$PICTURE_DIR" as POSIX file as alias)
END