import logging
import sys
import threading
import time

import can as can
import pythonping.executor
from can import BusABC
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS, ASYNCHRONOUS

import data
import data.data_types
from data.sensor import Sensor
from data.sensor_ids import SensorId
from data.sensor_manager import SensorManager
from pythonping import ping

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
LOGGER = logging.getLogger("app")

CAN_BITRATE = 500e3


def build_sensor_array():
    LOGGER.info("registering sensors")

    SensorManager.add_sensor(
        Sensor(
            SensorId.THROTTLE_POSITION.value,
            data.data_types.THROTTLE_POSITION,
            "throttle_position",
            100,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.SWITCH_POSITIONS.value,
            data.data_types.SWITCH_POSITION,
            "switch_positions",
            10,
        )
    )
    SensorManager.add_sensor(
        Sensor(SensorId.MOTOR_RPM.value, data.data_types.RPM, "motor_rpm", 10)
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.BATTERY_VOLTAGE.value,
            data.data_types.VOLTAGE,
            "battery_voltage",
            10,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.BATTERY_TEMPERATURE_1_2_3.value,
            data.data_types.TEMPERATURE,
            "battery_temperature_1_2_3",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.MOTOR_TEMPERATURE.value,
            data.data_types.TEMPERATURE,
            "motor_temperature",
            10,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.MOTOR_CONTROLLER_TEMPERATURE.value,
            data.data_types.TEMPERATURE,
            "motor_controller_temperature",
            10,
        )
    )
    SensorManager.add_sensor(
        Sensor(SensorId.BATTERY_SOC.value, data.data_types.SOC, "battery_soc", 1)
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.MPPT_TEMPERATURE_1.value,
            data.data_types.TEMPERATURE,
            "mppt_temperature_1",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.MPPT_TEMPERATURE_2.value,
            data.data_types.TEMPERATURE,
            "mppt_temperature_2",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.MPPT_TEMPERATURE_3.value,
            data.data_types.TEMPERATURE,
            "mppt_temperature_3",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.MPPT_TEMPERATURE_4.value,
            data.data_types.TEMPERATURE,
            "mppt_temperature_4",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.MPPT_TEMPERATURE_5.value,
            data.data_types.TEMPERATURE,
            "mppt_temperature_5",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.MPPT_TEMPERATURE_6.value,
            data.data_types.TEMPERATURE,
            "mppt_temperature_6",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.COOLANT_TEMP.value, data.data_types.TEMPERATURE, "coolant_temp", 1
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.FOIL_1_POSITION.value,
            data.data_types.ROLL_PITCH_DEGREE,
            "foil_1_position",
            100,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.FOIL_2_POSITION.value,
            data.data_types.ROLL_PITCH_DEGREE,
            "foil_2_position",
            100,
        )
    )
    SensorManager.add_sensor(
        Sensor(SensorId.HEIGHT.value, data.data_types.DISTANCE, "height", 100)
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.BATTERY_CURRENT.value,
            data.data_types.CURRENT,
            "battery_current",
            10,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.MPPT_CHARGER_VOLTAGE_1.value,
            data.data_types.VOLTAGE,
            "mppt_charger_voltage_1",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.MPPT_CHARGER_VOLTAGE_2.value,
            data.data_types.VOLTAGE,
            "mppt_charger_voltage_2",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.MPPT_CHARGER_VOLTAGE_3.value,
            data.data_types.VOLTAGE,
            "mppt_charger_voltage_3",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.MPPT_CHARGER_VOLTAGE_4.value,
            data.data_types.VOLTAGE,
            "mppt_charger_voltage_4",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.MPPT_CHARGER_VOLTAGE_5.value,
            data.data_types.VOLTAGE,
            "mppt_charger_voltage_5",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.MPPT_CHARGER_VOLTAGE_6.value,
            data.data_types.VOLTAGE,
            "mppt_charger_voltage_6",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.MPPT_CHARGER_CURRENT_1.value,
            data.data_types.CURRENT,
            "mppt_charger_current_1",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.MPPT_CHARGER_CURRENT_2.value,
            data.data_types.CURRENT,
            "mppt_charger_current_2",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.MPPT_CHARGER_CURRENT_3.value,
            data.data_types.CURRENT,
            "mppt_charger_current_3",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.MPPT_CHARGER_CURRENT_4.value,
            data.data_types.CURRENT,
            "mppt_charger_current_4",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.MPPT_CHARGER_CURRENT_5.value,
            data.data_types.CURRENT,
            "mppt_charger_current_5",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.MPPT_CHARGER_CURRENT_6.value,
            data.data_types.CURRENT,
            "mppt_charger_current_6",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.MOTOR_CONTROLLER_CURRENT.value,
            data.data_types.CURRENT,
            "motor_controller_current",
            10,
        )
    )
    SensorManager.add_sensor(
        Sensor(SensorId.GEARBOX_RPM.value, data.data_types.RPM, "gearbox_rpm", 10)
    )
    SensorManager.add_sensor(
        Sensor(SensorId.MOTOR_POWER.value, data.data_types.POWER, "motor_power", 10)
    )
    SensorManager.add_sensor(
        Sensor(SensorId.COOLANT_LEVEL.value, data.data_types.LEVEL, "coolant_level", 1)
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.ACCUBOX_AIR_TEMPERATURE.value,
            data.data_types.TEMPERATURE,
            "accubox_air_temperature",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.SOLARBOX_AIR_TEMPERATURE.value,
            data.data_types.TEMPERATURE,
            "solarbox_air_temperature",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.MOTORBOX_AIR_TEMPERATURE.value,
            data.data_types.TEMPERATURE,
            "motorbox_air_temperature",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.TELEMETRYBOX_AIR_TEMPERATURE.value,
            data.data_types.TEMPERATURE,
            "telemetrybox_air_temperature",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.AMBIENT_TEMPERATURE.value,
            data.data_types.TEMPERATURE,
            "ambient_temperature",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(SensorId.GPS_TIME.value, data.data_types.ABSOLUTTIME, "gps_time", 1)
    )
    SensorManager.add_sensor(
        Sensor(SensorId.RTC_TIME.value, data.data_types.ABSOLUTTIME, "rtc_time", 1)
    )
    SensorManager.add_sensor(
        Sensor(SensorId.COOLANT_FLOW.value, data.data_types.FLOW, "coolant_flow", 1)
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.MOTOR_VIBRATION.value,
            data.data_types.ACCELERATION,
            "motor_vibration",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(SensorId.GPS_SPEED.value, data.data_types.SPEED, "gps_speed", 10)
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.GPS_POSITION.value, data.data_types.GPS_POSITION, "gps_position", 1
        )
    )
    SensorManager.add_sensor(
        Sensor(SensorId.ROLL.value, data.data_types.ROLL_PITCH_DEGREE, "roll", 10)
    )
    SensorManager.add_sensor(
        Sensor(SensorId.PITCH.value, data.data_types.ROLL_PITCH_DEGREE, "pitch", 10)
    )
    SensorManager.add_sensor(
        Sensor(SensorId.GPS_HEDING.value, data.data_types.HEADING, "gps_heading", 1)
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.MAGNETIC_HEDING.value,
            data.data_types.HEADING,
            "magnetic_heading",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.WIND_DIRECTION.value, data.data_types.HEADING, "wind_direction", 1
        )
    )
    SensorManager.add_sensor(
        Sensor(SensorId.WIND_SPEED.value, data.data_types.SPEED, "wind_speed", 1)
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.ACCUBOX_FAN_RPM.value, data.data_types.RPM, "accubox_fan_rpm", 1
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.MOTORBOX_FAN_RPM.value, data.data_types.RPM, "motorbox_fan_rpm", 1
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.MOTORBOX_FAN_RPM.value, data.data_types.RPM, "solarbox_fan_rpm", 1
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.TELEMETRYBOX_FAN_RPM.value,
            data.data_types.RPM,
            "telemetrybox_fan_rpm",
            1,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.ERROR_THROTTLE_POSITION.value,
            data.data_types.THROTTLE_POSITION,
            "error_throttle_position",
            100,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.ERROR_DEAD_MANS_SWITCH_POSITION.value,
            data.data_types.SWITCH_POSITION,
            "error_dead_mans_switch_position",
            10,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.ERROR_MOTOR_SWITCH_POSITION.value,
            data.data_types.SWITCH_POSITION,
            "error_motor_switch_position",
            10,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.LOWEST_CELL_VOLTAGE.value,
            data.data_types.VOLTAGE_MV,
            "lowest_cell_voltage",
            10,
        )
    )
    SensorManager.add_sensor(
        Sensor(
            SensorId.HIGHEST_CELL_VOLTAGE.value,
            data.data_types.VOLTAGE_MV,
            "highest_cell_voltage",
            10,
        )
    )


def start_can_listening():
    LOGGER.info("CAN listening started")

    for sensor in SensorManager.get_sensors():
        sensor.add_valuechange_handler(lambda v, name: upload_messages(v, name))

    while True:
        try:
            with create_bus() as bus:
                while True:
                    message: can.message.Message = bus.recv()
                    SensorManager.receive_message(message)
        except Exception as e:
            print(e)
            LOGGER.warning("restarting bus after error")
            time.sleep(1)


def start_networkstatus_worker():
    LOGGER.info("starting networkstatus monitoring")
    while True:
        try:
            with create_bus() as bus:
                while True:
                    # ping 1.1.1.1 using pythonping
                    results: pythonping.executor.ResponseList = ping(
                        "1.1.1.1", timeout=2, count=1
                    )
                    if results.success():
                        bus.send(
                            can.Message(
                                arbitration_id=SensorId.TELEMETRY_NETWORK_STATUS.value,
                                data=[0x1],
                            )
                        )
                    else:
                        bus.send(
                            can.Message(
                                arbitration_id=SensorId.TELEMETRY_NETWORK_STATUS.value,
                                data=[0x0],
                            )
                        )
                    time.sleep(5)
        except Exception as e:
            print(e)
            LOGGER.warning("restarting networkstatus monitor after error")
            time.sleep(1)


def create_bus() -> BusABC:
    return can.Bus(interface="socketcan", channel="can0", bitrate=CAN_BITRATE)


bucket_name = "lana_data"
client = InfluxDBClient(
    url="http://influx.solarboatteam.hu:8086",
    token="8WjcfKiq7otthk5XjhFokcI8Ll37ni_GyGBJ4KjYZt2LE34NDsfm_wRqdBKnexFcYSXkk2d28Xr2p0PZk-1quA==",
    org="sbt",
)
write_api = client.write_api(write_options=ASYNCHRONOUS)

last_upload = {}


def upload_messages(val, name):
    if name not in last_upload or last_upload[name] + 1 < time.time():
        p = Point("data").field(name, val)
        write_api.write(bucket=bucket_name, record=p)
        print("sent")
        last_upload[name] = time.time()
        print(name, val, last_upload[name])


def main():
    build_sensor_array()
    networkstatus_worker = threading.Thread(
        target=start_networkstatus_worker, daemon=True
    )
    networkstatus_worker.start()
    start_can_listening()


if __name__ == "__main__":
    main()
