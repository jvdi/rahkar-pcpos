# -*- coding: utf-8 -*-

from db.db_con import *
from pos_sadad import sadad
from pos_pec import pec
from gui_for_tray_icon import TrayIcon
from gui_for_message import tk_gui
import os, time
from dotenv import load_dotenv
import json as jsn
import clr, re

# Load asanpardakht dll
clr.AddReference("module/PosInterface")
from PosInterface import PCPos
from System import DateTime

load_dotenv()

# Wait for load sql - or check to load
time.sleep(int(os.getenv('DB_WAIT_TIME')))

# Run tray-icon GUI
gui_tray = TrayIcon()
gui_tray.run_detached()

# Flag for process Control - For Stop app
run_flag = True

# run_flag is set in db_con file
# Main process of app
while run_flag:
    time.sleep(int(os.getenv('CHECK_TIME')))  # Witing time for check ms-db to get new TransAction

    # Start a connection to mssql server
    ms_cur = MsSql()

    # Get Row from mssql
    # Exist Column: RowID, Fix_Acc1_ID, Fix_Acc2Type_ID, BedPrice, RowDesc, ...
    ms_cur.execute('''
    SELECT * 
    FROM DocD
    WHERE Fix_Acc1_ID=5 AND Fix_Acc2Type_ID=2 AND (Acc2RowID='''+os.getenv('SADAD_ACC_ID')+''' OR Acc2RowID='''+os.getenv('PEC_ACC_ID')+''' OR Acc2RowID='''+os.getenv('ASAN-P_ACC_ID')+''')
    ORDER BY RowID DESC;
    ''')

    # Get price and document id from mssql and save to Gloabal var
    for row in ms_cur.fetch():
        global price_to_send, doch_id, acc_number
        price_to_send = (int(row['BedPrice']) * int(os.getenv('PRICE_FACTOR')))
        doch_id = row['DocH_ID']
        acc_number = row['Acc2RowID']
        break

    # Close connection of mssql
    ms_cur.close()

    # Do Sadad transAction
    if (str(os.getenv('SADAD_RUN')) == 'YES') and acc_number == int(os.getenv('SADAD_ACC_ID')) and price_to_send != 0:
        # Send to sadad and get result
        sadad(price_to_send, doch_id, gui_tray)
    # Pec transAction
    elif (str(os.getenv('PEC_RUN')) == 'YES') and acc_number == int(os.getenv('PEC_ACC_ID')) and price_to_send != 0:
        # Send price to PEC
        pec(doch_id, price_to_send, gui_tray)
    # Asan-P transAction
    elif (str(os.getenv('ASAN-P_RUN')) == 'YES') and acc_number == int(os.getenv('ASAN-P_ACC_ID')) and price_to_send != 0:
        pcpos = PCPos(int(os.getenv('ASAN-P_DEVICE_PORT')))
        pcpos.InitLAN(os.getenv('ASAN-P_DEVICE_IP'))

        # Get last sent-pay
        sqlite = SqliteDb()
        sqlite.execute('''
        SELECT * FROM pay ORDER BY rowid DESC;
        ''')
        last_pay_record_id = sqlite.fetchone()

        # Remove TransAction - if removed
        if last_pay_record_id[0] > doch_id:
            sqlite.execute('''
            DELETE FROM Pay WHERE id='{}';
            '''.format(last_pay_record_id[0]))
            sqlite.commit()
            # Close sqlite connection
            sqlite.close()
        # Do a new TransAction if it's a new
        elif last_pay_record_id[0] < doch_id:
            def do_trans_action():
                # price, empty, doc_id, time
                send_request = pcpos.DoSyncPayment(str(price_to_send), "", str(doch_id), DateTime.Now)
                response = str(send_request)
                end_result = re.split('= |;', response)
                return end_result

            # For cancell TransAction 
            not_done = True

            def abort_pay():
                global not_done
                not_done = False

            result = do_trans_action()
            while not_done:
                print(result)
                print(result[1])
                if result[1] == '0':
                    print(result[0]+': '+result[1])
                    print(result[3])
                    abort_pay()
                else:
                    # Create Json Result
                    json_text = '{ "PcPosStatusCode":"'+result[1]+'", "PcPosStatus":"' + \
                    'فعال'+'", "ResponseCodeMessage":"' + \
                    result[3]+'"}'
                    AsanP_json = jsn.loads(json_text)
                    
                    # Show Message
                    AsanP_gui = tk_gui()
                    AsanP_gui.show_message(do_trans_action, abort_pay, AsanP_json, 'آپ')
            
            # Save result in sqlite pay table
            sqlite.execute('''
            INSERT INTO pay(
                id, price, status
            )VALUES(
                {}, {}, {}
            )
            '''.format(doch_id, price_to_send, result[1]))
            sqlite.commit()

            # Close sqlite connection
            sqlite.close()