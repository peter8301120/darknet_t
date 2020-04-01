HOST=192.168.24.152
USERNAME=asv
PASSWORD=1234
lftp asv:1234@192.168.24.152 <<EOF  
	lcd ./ftp-download
	cd /image/download01
	cd `date +"%Y%m%d%H"`
	mget *.jpg
	mget *.JPG
	cd ..
	cd ..
	cd ./download02
	cd `date +"%Y%m%d%H"`
	mget *.jpg
	mget *.JPG
	bye
EOF




		  


