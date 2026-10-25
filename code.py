
import time
import board
import digitalio
import analogio
import touchio
import rotaryio
import usb_midi




MIDI_CHANNEL = 0
VELOCITY = 110

# Five touch pads: D0-D4
TOUCH_PINS = [
    board.D0,
    board.D1,
    board.D2,
    board.D3,
    board.D4,
]

TOUCH_NOTES = [60, 62, 64, 65, 67]

BUTTON_PINS = [
    board.D7,
    board.D6,
    board.D5,
]

# MIDI notes assigned to the buttons
BUTTON_NOTES = [36, 38, 42]

# Slider: D8
SLIDER_PIN = board.D8

# Rotary encoder: D9 and D10
ENCODER_A = board.D9
ENCODER_B = board.D10

# MIDI control numbers
SLIDER_CC = 1
ENCODER_CC = 7

# ---------------- MIDI SETUP ----------------

# USB MIDI must be enabled by the board firmware.
# On supported CircuitPython builds, the output port
# is normally usb_midi.ports[1].

if len(usb_midi.ports) < 2:
    raise RuntimeError(
        "USB MIDI output unavailable. Check boot.py."
    )

midi_out = usb_midi.ports[1]

def send_note_on(note):
    """Tell the computer to start a MIDI note."""
    midi_out.write(bytes([
        0x09,
        0x90 | MIDI_CHANNEL,
        note,
        VELOCITY
    ]))

def send_note_off(note):
    """Tell the computer to stop a MIDI note."""
    midi_out.write(bytes([
        0x08,
        0x80 | MIDI_CHANNEL,
        note,
        0
    ]))

def send_control_change(controller, value):
    """Send a MIDI control value from 0 to 127."""
    value = max(0, min(127, value))

    midi_out.write(bytes([
        0x0B,
        0xB0 | MIDI_CHANNEL,
        controller,
        value
    ]))

# ---------------- TOUCH PADS ----------------

touch_sensors = []

for pin in TOUCH_PINS:
    sensor = touchio.TouchIn(pin)
    touch_sensors.append(sensor)

touch_states = [False] * len(touch_sensors)

# ---------------- BUTTONS ----------------

buttons = []

for pin in BUTTON_PINS:
    button = digitalio.DigitalInOut(pin)
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP
    buttons.append(button)

button_states = [False] * len(buttons)

# ---------------- SLIDER ----------------

slider = analogio.AnalogIn(SLIDER_PIN)
last_slider_value = -1

# ---------------- ENCODER ----------------

encoder = rotaryio.IncrementalEncoder(
    ENCODER_A,
    ENCODER_B
)

last_encoder_position = encoder.position
encoder_value = 64

# ---------------- MAIN LOOP ----------------

print("Half Life MIDI Keyboard started")

while True:

    # Check the five touch pads
    for i, sensor in enumerate(touch_sensors):
        pressed = sensor.value

        if pressed and not touch_states[i]:
            send_note_on(TOUCH_NOTES[i])

        elif not pressed and touch_states[i]:
            send_note_off(TOUCH_NOTES[i])

        touch_states[i] = pressed

    # Check the three physical buttons
    for i, button in enumerate(buttons):
        # Pull-up means a pressed button reads False
        pressed = not button.value

        if pressed and not button_states[i]:
            send_note_on(BUTTON_NOTES[i])

        elif not pressed and button_states[i]:
            send_note_off(BUTTON_NOTES[i])

        button_states[i] = pressed

    # Read slider and convert its reading to 0-127
    slider_reading = slider.value
    slider_cc_value = slider_reading * 127 // 65536

    # Send only when the slider's MIDI value changes
    if slider_cc_value != last_slider_value:
        send_control_change(SLIDER_CC, slider_cc_value)
        last_slider_value = slider_cc_value

    # Read rotary encoder
    position = encoder.position

    if position != last_encoder_position:
        difference = position - last_encoder_position

        encoder_value = max(
            0,
            min(127, encoder_value + difference)
        )

        send_control_change(ENCODER_CC, encoder_value)
        last_encoder_position = position

    # Small pause before checking again
    time.sleep(0.005)
