import smbus

bus = smbus.SMBus(1)

DEVICE_ADDRESS = 0x48

temp_reg_12bit = bus.read_word_data(DEVICE_ADDRESS , 0)
temp_low = (temp_reg_12bit & 0xff00) >> 8
temp_high = (temp_reg_12bit & 0x00ff)

temp = (((temp_high * 256) + temp_low) >> 4)

temp_C = float(temp) * 0.0625

print("TEMP:",temp_C,"C")