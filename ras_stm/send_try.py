import serial
import time

ser = serial.Serial('/dev/serial0', 115200, timeout=1)

IN_Engi_RPM_ID = 1
IN_CK_Gap_ID = 2
IN_CK_Bate_ID = 3
IN_Teeth_different_HALL_ID = 4
IN_NUM_CAM_Teeth_ID = 5
IN_CAM_Teeth_1_ID = 6
IN_CAM_Gap_1_ID = 8
IN_CAM_Teeth_2_ID = 9
IN_CAM_Teeth_3_ID = 10
IN_CAM_Gap_2_ID = 11
IN_CAM_Gap_3_ID = 12
IN_CAM_Teeth_4_ID = 13
IN_CAM_Gap_4_ID = 15
IN_CAM_Teeth_5_ID = 14
IN_CAM_Gap_5_ID = 16
IN_CAM_Teeth_6_ID = 17
IN_CAM_Gap_6_ID = 19
IN_CAM_Teeth_7_ID = 18
IN_CAM_Gap_7_ID = 20
IN_CAM_Teeth_8_ID = 21
IN_CAM_Gap_8_ID = 23
IN_NUM_CAM_INDUCT_Teeth_ID = 25
IN_CAM_INDUCT_Teeth_1_ID = 26
IN_CAM_INDUCT_Teeth_2_ID = 28
IN_CAM_INDUCT_Teeth_3_ID = 29
IN_CAM_INDUCT_Teeth_4_ID = 31
IN_CAM_INDUCT_Teeth_5_ID = 30
IN_CAM_INDUCT_Teeth_6_ID = 32
IN_CAM_INDUCT_Teeth_7_ID = 33
IN_CAM_INDUCT_Teeth_8_ID = 35
IN_H2O1_FRE_ID = 37
IN_H2O1_OFFSET_ID = 38
IN_H2O1_VOL_PEAK_ID = 40
IN_AC_HV_1_FRE_ID = 41
IN_AC_HV_1_DUTY_ID = 43
IN_AC_HV_2_DUTY_ID = 44
IN_AC_HV_3_DUTY_ID = 59
IN_AC_HV_4_DUTY_ID = 60
IN_AC_SCV_DUTY_ID = 47
IN_AC_PUS_DUTY_ID = 45

startid_sending = 165

# Nhập 4 byte header 1 lần
startid = 165 # var to start read (startid)
pageid = 195 # =195 to send data if indexid = 5
typeid = int(input("typid (0-255): ")) #chose what num send?
indexid = 5 

#a = 165, b = 192, c = 1, d = 5

num_send = int(input("number of packets to send: "))
bit_5_to_8 = bytes([0, 0, 0, 0])
sending=0

# viet ham nhan tin hieu o day

try:
    while True:
        if sending == 1:
            data_bytes = num_send.to_bytes(4, byteorder='little') + bit_5_to_8
            packet = bytes([startid, pageid, typeid, indexid]) + data_bytes
            ser.write(packet)
            sending = 0

            if typeid == IN_Engi_RPM_ID:
                print("Send IN_Engi_RPM", data_bytes)

            if typeid == IN_CK_Gap_ID:
                print("Send IIN_CK_Gap", data_bytes)
            
            if typeid == IN_CK_Bate_ID:
                print("Send IN_Engi_RPM", data_bytes)

        if sending == 0:
            print("STOP SENDING")
        

except KeyboardInterrupt:
    print("\n⏹️ STOPPED")
