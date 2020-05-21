import os
from ftplib import FTP
import time
from datetime import datetime
import glob
import shutil

def run_ftp_download():
    try:
        ftp =  FTP()
        #ftp.set_debuglevel(2)
        ftp.connect('223.200.97.241', 21)
        ftp.login('upload02', 'upload02')
        
        listing = []
        ftp.retrlines("LIST", listing.append)

        totalNum= len(listing)

        count=1
        downloadCnt=0

        for val in listing:
            print('interval 進度: %d/%d'%(count,totalNum))
            try:
                #print(val)
                words = val.split(None, 8)
                #print(words)
                folderName = words[-1].lstrip()
                #print(words[-1])
                print('foldername:%s'%(folderName,))
                if "gpu" in folderName or "done" in folderName:
                    continue
                ftp.rename(folderName,folderName + "_done")

            except Exception as e:
                print('error')
                print(e)
                ftp.close()
                break
            count+=1
        ftp.close()
    except:
        ftp.close()

def func(): 
    try:
        print('開始修改FTP檔案名稱，現在時間%s'%(datetime.now().strftime("%H:%M:%S"),))
        run_ftp_download()
    except Exception as e:
        print(e) 

if __name__ == '__main__':
    func()
