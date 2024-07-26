from netmiko import ConnectHandler
import time
import schedule
import pandas as pd
import datetime
import os

report = pd.DataFrame({
    "timestamp": [],
    "hostname": [],
    "result": []
})

def job():

    mikrotik = {
    'device_type': '',
    'host':   'input your ip address',
    'username': 'input your user',
    'password': 'input your pass',
    'port': 'the default port ssh 22/but you can input custom port ssh'
    }
    
    try:
        # Login to Mikrotik
        mikrotik_connection = ConnectHandler(**mikrotik)
        print(f"login to Mikrotik")
        
        # Push Command ke Mikrotik
        output = mikrotik_connection.send_command('/ip/ipsec/active-peers/kill-connections', cmd_verify=False)
        
        # Kondisi Hasil Push Command ke Mikrotik
        if output.strip() == "":
            result_status = "DONE"
            print("success")
        else:
            result_status = "FAILED"
            print("failed")
        
        # Data ROW CSV
        new_row = {
            "nomer": len(report) + 1,  # add a new column for row number
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "hostname": "input your up",
            "hasil_flush": result_status
        }
        report.loc[len(report)] = new_row
        report.index = range(1, len(report) + 1)  # reset index to start from 1
    except Exception as err:
        print(err) 
    
    # Directory File
    file_path = os.path.join(os.getcwd(), 'result_status.csv')
    
    # Ketika ada data yang sama di File "Hasil_Flush" akan ditambahkan kebawah 
    report.to_csv(file_path, mode='w', header=False, index=False)
    print(os.getcwd())

# Script otomatis berjalan setiap 8 jam sekali
schedule.every(8).hours.do(job)

# Loop untuk menjalankan script secara terus-menerus
while True:
    schedule.run_pending()
    time.sleep(1)