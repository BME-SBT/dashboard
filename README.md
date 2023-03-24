## Requirements

PySide6
python-can
python-can-remote

## Usage

Start virtual can server: `python3 -m can_remote --interface=virtual --channel=0 --bitrate=500000`  
Start dashboard: `python3 app.py`

## Send debug messages

Edit `debug_server.py` to send whatever you want. You can use the data_types module from the dashboard.
Start debug_server: `python3 debug_server.py`
