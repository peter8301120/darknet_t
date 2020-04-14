HOST=192.168.2.102
USERNAME=01
PASSWORD=04580682
filename=echo date +"%Y%m%d%H".txt
echo $filename
lftp 01:04580682@192.168.2.102 << EOF
  lcd ./ftp-upload01
  mkdir ./Ftp-upload01
  cd ./Ftp-upload01
  mkdir `date +"%Y%m%d"`
  cd `date +"%Y%m%d"`
  mput *.txt
  mput *.jpg
  mput *.JPG
  bye 
EOF

echo "upload01 finish!"
echo "Remove txt and .jpg!"
cd ./ftp-upload01
rm *.txt
rm *.jpg
rm *.JPG
echo "finish Remove txt and .jpg!"
