time1=$(date +"%H")
time2=$time1
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
		sh download.sh
		time2=$((time1+1))
		echo $time2
	else
		echo "Wait for 3 seconds..."
		sleep 3
		echo $time_m
	fi
	#55分上傳成果txt檔
	if [ "$time_m" = 55 ]
	then
		sh upload.sh
		echo $time_m
	fi

done
