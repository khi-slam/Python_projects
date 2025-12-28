import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


def on_activate(app):
    # Create a window
    window = Gtk.ApplicationWindow(application=app)
    window.set_title("Fedora Python App")
    window.set_default_size(300, 200)

    # Create a button
    button = Gtk.Button(label="her")

    # Connect the "clicked" signal to close the window
    button.connect("clicked", lambda btn: window.destroy())

    # Add button to window and show everything
    window.set_child(button)
    window.present()


# Create the application
app = Gtk.Application(application_id="org.example.pythonapp")
app.connect('activate', on_activate)

# Run the loop
app.run(None)