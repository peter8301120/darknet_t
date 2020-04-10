HOST=192.168.2.102
USERNAME=myuser
PASSWORD=abvc123456
lftp myuser:abvc123456@192.168.2.102 <<EOF  
	lcd ./ftp-download01
	cd /Image/Download01
	cd `date +"%Y%m%d%H"`
	mget *.jpg
	mget *.JPG
	cd ..
	cd ..
	cd ./Download02
	cd `date +"%Y%m%d%H"`
	lcd ./ftp-download02
	mget *.jpg
	mget *.JPG
	bye
EOF




		  


