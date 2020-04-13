HOST=192.168.2.102
USERNAME=02
PASSWORD=04580682
filename=echo date +"%Y%m%d%H".txt
echo $filename
lftp 02:04580682@192.168.2.102 << EOF
  lcd ./ftp-upload02
  mkdir ./Ftp-upload02
  cd ./Ftp-upload02
  mkdir `date +"%Y%m%d"`
  cd `date +"%Y%m%d"`
  mput *.txt
  mput *.jpg
  mput *.JPG
  bye 
EOF

echo "upload02 finish!"
sleep 3
echo "Remove txt and .jpg!"
cd ./ftp-upload02
rm *.txt
rm *.jpg
rm *.JPG
echo "finish Remove txt and .jpg!"
