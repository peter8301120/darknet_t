HOST=223.200.97.241
USERNAME=upload01
PASSWORD=upload01
echo $filename
lftp upload01:upload01@223.200.97.241 << EOF
  lcd ./ftp-upload01
  mirror -R
  bye 
EOF

echo "upload01 finish!"
echo "Remove txt and .jpg!"
rm -r ./ftp-upload01
echo "finish Remove txt and .jpg!"
