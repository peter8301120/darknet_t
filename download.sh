HOST=192.168.2.102
USERNAME=myuser
PASSWORD=abvc123456
lftp myuser:abvc123456@192.168.2.102 <<EOF 
	lcd ./ftp-download01
	cd ./Download01
	cd `date -d '1 hours ago' +"%Y%m%d%H"`
	mget *.jpg
	mget *.JPG
        cd ..
        mv `date -d '1 hours ago' +"%Y%m%d%H"` `date -d '1 hours ago' +"%Y%m%d%H"_gpu`
	bye
EOF

lftp myuser:abvc123456@192.168.2.102 <<EOF 
	lcd ./ftp-download02
	cd ./Download02
	cd `date -d '1 hours ago' +"%Y%m%d%H"`
	mget *.jpg
	mget *.JPG
        cd ..
        mv `date -d '1 hours ago' +"%Y%m%d%H"` `date -d '1 hours ago' +"%Y%m%d%H"_gpu`
	bye
EOF


		 


