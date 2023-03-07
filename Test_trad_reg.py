#!/usr/bin/env python3

import sys
import time
from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.exceptions import ConnectionException

ip = sys.argv[1]
client = ModbusClient(ip, port=502)
client.connect()

start_address = 1
num_registers = 20

while True:
    rr = client.read_holding_registers(start_address, num_registers)
    decoder = BinaryPayloadDecoder.fromRegisters(rr.registers)
    print(f"Response: {rr}")
    for i in range(num_registers):
        print(f"Register {start_address+i}: {decoder.decode_16bit_int()}")
    time.sleep(1)
