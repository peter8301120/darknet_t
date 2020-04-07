HOST=192.168.2.102
USERNAME=myuser
PASSWORD=abvc123456
filename=echo date +"%Y%m%d%H".txt
echo $filename
lftp myuser:abvc123456@192.168.2.102 << EOF
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
