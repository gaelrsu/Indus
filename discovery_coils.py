#!/usr/bin/env python3

import sys
import time
from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.exceptions import ConnectionException

ip = sys.argv[1]
client = ModbusClient(ip, port=502)
client.connect()

while True:
    rr = client.read_coils(0, 20)
    values = [int(bit) for bit in rr.bits]  # conversion booléen -> entier (0 ou 1)
    print(values)
    time.sleep(1)
