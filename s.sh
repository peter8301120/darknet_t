time1=$(date +"%H")
time2=$time1
time3=$time1
time_m=$(date +"%M")
a=1
while true
do
	date +"%Y/%m/%d-%H"
	time1=$(date +"%H")
	time_m=$(date +"%M")
	#echo $time1
	#echo $time2

	#5分下載前一小時資料
	if [ "$time1" = "$time2" ] && [ "$time_m" = 05 ]
	then
		echo download files at `date -d '1 hours ago' +"%Y%m%d%H"`
		sh download.sh
		time2=$(date -d '1 hours' +"%H")
		#echo $time2
	else 
		if [ "$time1" = "$time3" ] && [ "$time_m" = 55 ]
			then
			echo Upload files to `date +"%Y%m%d"`
			sh upload01.sh
			sh upload02.sh
			echo "Upload finished ..."
			time3=$(date -d '1 hours' +"%H")
		else
			echo "Wait for 3 seconds ..."
			sleep 3
			echo $time_m
		fi
	fi
done
