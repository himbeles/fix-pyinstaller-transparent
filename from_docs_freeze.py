# macOS packaging support
from multiprocessing import freeze_support

freeze_support()  # noqa

from nicegui import native, ui


def root():
    ui.label('Hello from PyInstaller')

ui.run(root, reload=False, native=False, port=native.find_open_port())