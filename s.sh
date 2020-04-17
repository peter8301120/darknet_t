time1=$(date +"%H")
#time2=$(date -d '1 hours' +"%H")
#if [ ("$time_m" > 05) ]
#	then
#	time2=$(date -d '1 hours' +"%H")
#fi
#time3=$time1
time_m=$(date +"%M")

while true
do 
	date +"%Y/%m/%d-%H"
	time1=$(date +"%H")
	time_m=$(date +"%M")
	echo $time1
	#echo $time2
	#echo $time3

	#5分下載前一小時資料
	if [ "$time_m" = 05 ]
	then
		echo download files at `date -d '1 hours ago' +"%Y%m%d%H"`
		sh download.sh
		#time2=$(date -d '1 hours' +"%H")
		#echo $time2
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
