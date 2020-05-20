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
        ftp.login('download01', 'download01')
        
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
                if folderName.find('gpu')>=0:
                    continue
                if folderName.find('done')<0:
                    continue
                D=ftp.nlst(folderName)
                ftp.cwd(folderName)
                saveFolder = 'ftp-download01_temp'
                finishFolder = 'ftp-download01'
                if not os.path.exists(saveFolder):
                    os.makedirs(saveFolder)
                for d in D:
                    try:
                        tmp=d.split('/')
                        filename=tmp[1]
                        print(filename)
                        # download the file
                        local_filename = os.path.join(saveFolder, filename)
                        print(local_filename)
                        lf = open(local_filename, "wb")
                        #print('download count:%d'%(downloadCnt,))
                        #print('save ftp file strart')
                        ftp.retrbinary("RETR " + filename, lf.write, 8*1024)
                        #print('save ftp file end')
                        lf.close()
                        downloadCnt += 1
                    except Exception as e:
                        print('file save error')
                        print(e)
                        ftp.close()
                        break
                ftp.cwd('..')
                ftp.rename(folderName,folderName+'_gpu')
                try:
                    if not os.path.exists(finishFolder):
                        os.rename(saveFolder,finishFolder)
                except Exception as e:
                    print(e)
                    ftp.close()
                    break
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
        print('開始FTP下載，現在時間%s'%(datetime.now().strftime("%H:%M:%S"),))
        run_ftp_download()
    except Exception as e:
        print(e) 

if __name__ == '__main__':
    func()
