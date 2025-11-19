# macOS packaging support
from multiprocessing import freeze_support

freeze_support()  # noqa

from nicegui import app, ui

app.native.window_args['transparent'] = True
app.native.window_args['frameless'] = True


def main():
    with ui.card():
        ui.label('Hello, NiceGUI!')

    ui.run(
        reload=False,
        native=True,
    )


if __name__ in ('__main__', '__mp_main__'):
    main()
