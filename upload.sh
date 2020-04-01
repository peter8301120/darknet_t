HOST=192.168.24.152
USERNAME=asv
PASSWORD=1234
filename=echo date +"%Y%m%d%H".txt
echo $filename
lftp asv:1234@192.168.24.152 << EOF
  lcd ./ftp-upload
  mkdir txt
  cd txt
  mput *.txt
  bye 
EOF
echo "upload finish!"
sleep 3
echo "Remove txt!"
cd ./ftp-upload
rm *.txt
