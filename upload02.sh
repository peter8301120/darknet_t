HOST=223.200.97.241
USERNAME=upload02
PASSWORD=upload02
echo $filename
lftp upload02:upload02@223.200.97.241 << EOF
  lcd ./ftp-upload02
  lcd ./empty
  mirror -R
  bye 
EOF

echo "upload02 finish!"
echo "Remove txt and .jpg!"
rm -r ./ftp-upload02
echo "finish Remove txt and .jpg!"
