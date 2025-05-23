# import serial
import time
import smbus
bus = smbus.SMBus(1)
from flask import Flask, request, jsonify
import subprocess
import struct
app = Flask(__name__)
# ------------------------------------------------------
IN_Engi_RPM_ID = 1

IN_CK_Gap_ID = 2
IN_CK_Bate_ID = 3

IN_Teeth_different_CMIN_ID = 4;
IN_Teeth_different_CMOUT_ID = 130;

# ------------------------------------------------------

IN_CK_Generate_ID = 150
IN_CAM_HALL_Generate_ID = 151
IN_CAM_INDUCT_Generate_ID = 152

# ------------------------------------------------------

IN_NUM_CAM_Teeth_ID = 5
IN_CAM_Teeth_1_ID = 6
IN_CAM_Gap_1_ID = 8

IN_CAM_Teeth_2_ID = 9
IN_CAM_Gap_2_ID = 11

IN_CAM_Teeth_3_ID = 10
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

# ------------------------------------------------------

IN_NUM_CAM_INDUCT_Teeth_ID = 25
IN_CAM_INDUCT_Teeth_1_ID = 26
IN_CAM_INDUCT_Teeth_2_ID = 28
IN_CAM_INDUCT_Teeth_3_ID = 29
IN_CAM_INDUCT_Teeth_4_ID = 31
IN_CAM_INDUCT_Teeth_5_ID = 30
IN_CAM_INDUCT_Teeth_6_ID = 32
IN_CAM_INDUCT_Teeth_7_ID = 33
IN_CAM_INDUCT_Teeth_8_ID = 35

IN_CAM_INDUCT_Gap_1_ID = 120
IN_CAM_INDUCT_Gap_2_ID = 121
IN_CAM_INDUCT_Gap_3_ID = 122
IN_CAM_INDUCT_Gap_4_ID = 123
IN_CAM_INDUCT_Gap_5_ID = 124
IN_CAM_INDUCT_Gap_6_ID = 125
IN_CAM_INDUCT_Gap_7_ID = 126
IN_CAM_INDUCT_Gap_8_ID = 127

# ------------------------------------------------------

# IN_H2O1_FRE_ID = 37
# IN_H2O1_OFFSET_ID = 38
# IN_H2O1_VOL_PEAK_ID = 40
IN_AC_HV_1_FRE_ID = 41
IN_AC_HV_1_DUTY_ID = 43
IN_AC_HV_2_DUTY_ID = 44
IN_AC_HV_3_DUTY_ID = 59
IN_AC_HV_4_DUTY_ID = 60
IN_AC_SCV_DUTY_ID = 47
IN_AC_PUS_DUTY_ID = 48

# ------------------------------------------------------

IN_ABS_Bate_ID = 128
IN_ABS_1_Speed_ID = 129
IN_ABS_2_Speed_ID = 130
IN_ABS_3_Speed_ID = 131
IN_ABS_4_Speed_ID = 132

IN_ABS_Generate_ID = 150

# ------------------------------------------------------
IN_MIL_LIGHT_ID  = 1;
IN_BAT_LAMP_STAT_ID = 2;
IN_TPMS_W_LAMP_ID = 3;
IN_ABS_W_LAMP_ID = 4;
IN_EBD_W_LAMP_ID = 5;
IN_xSG_TCS_OFF_LAMP_ID = 6;
IN_CF_Mdps_WLmp = 7;

#----------------------------------------------------------- from open dpc - lights
IN_CF_Gway_TurnSigRh_ID = 50;
IN_CF_Gway_TurnSigLh_ID = 51;
IN_SEATBELT_ID = 52;

#// ----------------------------------------------------------- from kia_picato_dbc

IN_SPEED_MOTOR_ID = 100;
IN_TEMP_ENG_ID = 101;
IN_WHEEL_SPD_ID = 102;


# ------------------------------------------------------

startid_sending = 165

# Nhập 4 byte header 1 lần
startid = 165 # var to start read (startid)
pageid = 195 # =195 to send data if indexid = 5
# typeid = int(input("typid (0-255): ")) #chose what num send?
indexid = 5 
typeid = 0
value = 0
address = 0
data = 0
#a = 165, b = 192, c = 1, d = 5

# num_send = int(input("number of packets to send: "))
bit_5_to_8 = [0, 0, 0, 0]
sending=0
addr = 0
# ser = serial.Serial('/dev/serial0', 115200, timeout=1) #open uart port


#function to read data from app

# @app.route('/send', methods=['POST'])
# def receive_data():
#     try:
#         data = request.get_json()
#         field = data.get('field')
#         value = data.get('value')
#         addr = data.get('addr')
#         field_map = {
#             "rpm": IN_Engi_RPM_ID,
#             "gap": IN_CK_Gap_ID,
#             "bate": IN_CK_Bate_ID,
#             "MIL" : IN_MIL_LIGHT_ID,
#         }
#         typeid = field_map.get(field.lower())
#         address = int(addr)
#         data = int(value)
#         if field is None or data is None:
#             return jsonify({"error": "Thiếu 'field' hoặc 'value'"}), 400
        
#     except Exception as e:
#         return jsonify({"error": f"An error occurred: {str(e)}"}), 500



# if __name__ == '__main__':
#     app.run(host = '0.0.0.0',port =8000)
#     # print(f"{typeid}, {value}")``
#     receive_data()
    

# # function to send i2c
# try:
#     if (address == 1):
#         while True:
#             bus.write_i2c_block_data(0X12, 0x00, [0, typeid, data])
            

# #            
        

# except KeyboardInterrupt:
#     print("\n⏹️ STOPPED")
@app.route('/send', methods=['POST'])
def receive_data():
    try:
        # Lấy dữ liệu từ Flutter
        data = request.get_json(force=True)
        field = data.get('field')
        value = data.get('value')
        addr = data.get('addr')
        field_map = {
            "rpm": IN_Engi_RPM_ID,
            "gap": IN_CK_Gap_ID,
            "bate": IN_CK_Bate_ID,

            "difin": IN_Teeth_different_CMIN_ID,
            "difout": IN_Teeth_different_CMOUT_ID,

            "crksend": IN_CK_Generate_ID,
            "camhallsend": IN_CAM_HALL_Generate_ID,
            "caminductsend": IN_CAM_INDUCT_Generate_ID,

            "numcaminduct": IN_NUM_CAM_INDUCT_Teeth_ID,
            "camteeth1": IN_CAM_INDUCT_Teeth_1_ID,
            "camteeth2": IN_CAM_INDUCT_Teeth_2_ID,
            "camteeth3": IN_CAM_INDUCT_Teeth_3_ID,
            "camteeth4": IN_CAM_INDUCT_Teeth_4_ID,
            "camteeth5": IN_CAM_INDUCT_Teeth_5_ID,
            "camteeth6": IN_CAM_INDUCT_Teeth_6_ID,
            "camteeth7": IN_CAM_INDUCT_Teeth_7_ID,
            "camteeth8": IN_CAM_INDUCT_Teeth_8_ID,
            "camgap1": IN_CAM_INDUCT_Gap_1_ID,
            "camgap2": IN_CAM_INDUCT_Gap_2_ID,
            "camgap3": IN_CAM_INDUCT_Gap_3_ID,
            "camgap4": IN_CAM_INDUCT_Gap_4_ID,
            "camgap5": IN_CAM_INDUCT_Gap_5_ID,
            "camgap6": IN_CAM_INDUCT_Gap_6_ID,
            "camgap7": IN_CAM_INDUCT_Gap_7_ID,
            "camgap8": IN_CAM_INDUCT_Gap_8_ID,

            "absbate": IN_ABS_Bate_ID,
            "abs1speed": IN_ABS_1_Speed_ID,
            "abs2speed": IN_ABS_2_Speed_ID,
            "abs3speed": IN_ABS_3_Speed_ID,
            "abs4speed": IN_ABS_4_Speed_ID,

            "abssend": IN_ABS_Generate_ID,

            "ana1": IN_AC_HV_1_DUTY_ID,
            "ana2": IN_AC_HV_2_DUTY_ID,
            "ana3": IN_AC_HV_3_DUTY_ID,
            "ana4": IN_AC_HV_4_DUTY_ID,
            "ana5": IN_AC_SCV_DUTY_ID,
            "ana6": IN_AC_PUS_DUTY_ID,

            "act" : IN_AC_HV_1_FRE_ID,

            "kia_mil" : IN_MIL_LIGHT_ID,
            "kia_tpms" : IN_TPMS_W_LAMP_ID,
            "kia_abs" : IN_ABS_W_LAMP_ID,
            "kia_sbelt" : IN_SEATBELT_ID,
            "kia_mdps" : IN_CF_Mdps_WLmp,
            "kia_ebd" : IN_EBD_W_LAMP_ID ,
            "kia_engine_spd" : IN_SPEED_MOTOR_ID,
            "kia_veh_spd" : IN_WHEEL_SPD_ID ,
        }
        if not field or value is None or addr is None:
            return jsonify({"error": "Thiếu 'field', 'value', hoặc 'addr'"}), 400

        field = field.lower()
        typeid = field_map.get(field)

        if typeid is None:
            return jsonify({"error": f"Trường '{field}' không hợp lệ"}), 400

        # Ép kiểu
        address = int(addr)
        value = int(value)
        if address == 1:
            print(1)
            low_byte  = value & 0xFF
            high_byte = (value >> 8) & 0xFF
        # Gửi dữ liệu qua I2C
            if typeid == 100:
                print(2)
                # high_byte = (value >> 8) & 0xFF  # Lấy 8 bit cao = 0x0B = 11
                print(value)
                print(low_byte)
                print(high_byte)       
                # value_bytes = list(packed)        # [0x00, 0x00, 0x0B, 0xB8]
                bus.write_i2c_block_data(0x12, 0x00, [typeid, high_byte, low_byte])
            else:
                print(3)
                bus.write_i2c_block_data(0x12, 0x00, [typeid, high_byte, low_byte])
            time.sleep(0.05)
        if address == 2:
            value_bytes = list(value.to_bytes(4, 'little'))
            datasend = [165, 192, typeid, 5] + value_bytes + bit_5_to_8
            bus.write_i2c_block_data(0x10, 0x00, datasend)
            time.sleep(0.05)

        if address == 3:
            value_bytes = list(value.to_bytes(4, 'little'))
            datasend = [165, 192, typeid, 5] + value_bytes + bit_5_to_8
            bus.write_i2c_block_data(0x20, 0x00, datasend)
            time.sleep(0.05)

        return jsonify({
            "status": "ok",
            "sent": {"addr": address, "typeid": typeid, "value": value}
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)