#!/usr/bin/python
import smbus
import binascii

bus = smbus.SMBus(1)    # 1 = /dev/i2c-1 (port I2C1)

DEVICE_ADDRESS = 0x03  #7 bit address (will be left shifted to add the read write bit)
DEVICE_REG_MODE1 = 0x00
DEVICE_REG_LEDOUT0 = 0x1d

f = open('data', 'rb')

#format e convert
ledout_values = ['{:02}'.format(b) for b in f.read()]
ledout_values = [int(i) for i in ledout_values]

#print (ledout_values)
#print (f.read())
#Write a single register
#bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, 0x86)

#Write an array of registers
#ledout_values = [0x1f, 0x4f, 0x7f, 0x08, 0x11, 0x9f]
#print(ledout_values)
bus.write_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT0, ledout_values)


#r = bus.read_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT0, 6)

#print (r)
