from enum import Enum


class SensorId(Enum):
    THROTTLE_POSITION = 0b00000010101
    SWITCH_POSITIONS = 0b00000110101
    MOTOR_RPM = 0b00001010010
    BATTERY_VOLTAGE = 0b00001110000
    BATTERY_TEMPERATURE_1_2_3 = 0b00010010000
    MOTOR_TEMPERATURE = 0b00010110010
    MOTOR_CONTROLLER_TEMPERATURE = 0b00011010010
    BATTERY_SOC = 0b00011110000
    MPPT_TEMPERATURE_1 = 0b00100010001
    MPPT_TEMPERATURE_2 = 0b00100110001
    MPPT_TEMPERATURE_3 = 0b00101010001
    MPPT_TEMPERATURE_4 = 0b00101110001
    MPPT_TEMPERATURE_5 = 0b00110010001
    MPPT_TEMPERATURE_6 = 0b00110110001
    COOLANT_TEMP = 0b00111010100
    FOIL_1_POSITION = 0b00111111011
    FOIL_2_POSITION = 0b01000011100
    HEIGHT = 0b01000111011
    BATTERY_CURRENT = 0b01001010000
    MPPT_CHARGER_VOLTAGE_1 = 0b01001110001
    MPPT_CHARGER_VOLTAGE_2 = 0b01010010001
    MPPT_CHARGER_VOLTAGE_3 = 0b01010110001
    MPPT_CHARGER_VOLTAGE_4 = 0b01011010001
    MPPT_CHARGER_VOLTAGE_5 = 0b01011110001
    MPPT_CHARGER_VOLTAGE_6 = 0b01100010001
    MPPT_CHARGER_CURRENT_1 = 0b01100110001
    MPPT_CHARGER_CURRENT_2 = 0b01101010001
    MPPT_CHARGER_CURRENT_3 = 0b01101110001
    MPPT_CHARGER_CURRENT_4 = 0b01110010001
    MPPT_CHARGER_CURRENT_5 = 0b01110110001
    MPPT_CHARGER_CURRENT_6 = 0b01111010001
    MOTOR_CONTROLLER_CURRENT = 0b01111110010
    GEARBOX_RPM = 0b10000010010
    MOTOR_POWER = 0b10000110010
    COOLANT_LEVEL = 0b10001010100
    ACCUBOX_AIR_TEMPERATURE = 0b10001110011
    SOLARBOX_AIR_TEMPERATURE = 0b10010010110
    MOTORBOX_AIR_TEMPERATURE = 0b10010110010
    TELEMETRYBOX_AIR_TEMPERATURE = 0b10011010111
    AMBIENT_TEMPERATURE = 0b10011110100
    GPS_TIME = 0b10100010100
    RTC_TIME = 0b10100111001
    COOLANT_FLOW = 0b10101010100
    MOTOR_VIBRATION = 0b10101110010
    GPS_SPEED = 0b10110010100
    GPS_POSITION = 0b10110110100
    ROLL = 0b10111010100
    PITCH = 0b10111110100
    GPS_HEDING = 0b11000010100
    MAGNETIC_HEDING = 0b11000110100
    WIND_DIRECTION = 0b11001010100
    WIND_SPEED = 0b11001110100
    ACCUBOX_FAN_RPM = 0b11010010011
    MOTORBOX_FAN_RPM = 0b11010110010
    SOLARBOX_FAN_RPM = 0b11011010110
    TELEMETRYBOX_FAN_RPM = 0b11011110111
    ERROR_THROTTLE_POSITION = 0b00000000010
    ERROR_DEAD_MANS_SWITCH_POSITION = 0b00000100010
    ERROR_MOTOR_SWITCH_POSITION = 0b00001000010
    LOWEST_CELL_VOLTAGE = 0b11100010000
    HIGHEST_CELL_VOLTAGE = 0b11100110000

    TELEMETRY_NETWORK_STATUS = 0b11100011101
    MOTOR_TELEMETRY_HEARTBEAT = 0b11100110010
