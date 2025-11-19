# macOS packaging support
from multiprocessing import freeze_support

freeze_support()  # noqa

from nicegui import app, native, ui

app.native.window_args['transparent'] = True
app.native.window_args['frameless'] = True

def root():
    ui.label('Hello from PyInstaller')

ui.run(root, reload=False, native=True, port=native.find_open_port())
