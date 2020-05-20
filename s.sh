time_m=$(date +"%M")

while true
do 
	time_m=$(date +"%M")

	#5分下載前一小時資料
	if [ "$time_m" = 21 ]
	then
		python3 ftp_download01.py
		python3 ftp_download01.py
		sleep 60
	else 
		if [ "$time_m" = 55 ]
			then
			echo Upload files to `date +"%Y%m%d"`
			sh upload01.sh
			sh upload02.sh
			echo "Upload finished ..."
			#time3=$(date -d '1 hours' +"%H")
			sleep 60
		else
			echo "Wait for 3 seconds ..."
			sleep 3
			echo $time_m
		fi
	fi
done
