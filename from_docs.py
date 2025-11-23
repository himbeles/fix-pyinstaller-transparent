from nicegui import native, ui


def root():
    ui.label('Hello from PyInstaller')

ui.run(root, reload=False, port=native.find_open_port())