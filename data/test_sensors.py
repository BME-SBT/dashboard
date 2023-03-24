import struct
import unittest
import data_types


class TestDatatypes(unittest.TestCase):
    def test_rpm(self):
        raw_val = 2400
        raw_data = struct.pack('>h', raw_val)
        data_type = data_types.RPM
        self.assertEqual(data_type.get_value(raw_data), raw_val)
        self.assertEqual(data_type.get_text_value(
            raw_data), f"{raw_val}.0 1/min")


if __name__ == '__main__':
    unittest.main()
