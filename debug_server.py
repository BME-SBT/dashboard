import time
from app import CAN_BITRATE

import can
import sys
from data import data_types
from can.message import Message

if __name__ == "__main__":
    bus = None
    try:
        bus = can.Bus('ws://localhost:54701/',
                      bustype='remote',
                      bitrate=CAN_BITRATE)

        # do CAN things
        rpm = data_types.RPM
        value = 1
        step = 1
        while True:
            message = Message(arbitration_id=1112,
                              is_extended_id=False, data=rpm.to_raw(value))
            bus.send(message)

            value += step
            if value > 5000:
                step = -1
            elif value < 1:
                step = 1
            time.sleep(1/10)

    except Exception as e:
        print(e)
        print(
            f"make sure that the server is running: python3 -m can_remote --interface=virtual --channel=0 --bitrate={int(CAN_BITRATE)}")
        raise e
