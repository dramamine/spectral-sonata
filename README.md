

# Spectral Sonata

Spectral Sonata is an interactive art piece. A MIDI keyboard controls visuals on an LED cube.

The LED cube is made of HUB75 panels. Panels are controlled by a Teensy 4.1 with the Smartmatrix Shield adaptor.

LED data is sent via USB cable to the cube.

## Setup

Flash the Teensy 4.1 with smartmatrix-serial.ino [@TODO link to lightdream-pocket]

## How To Run

@TODO autohotkey script or something?




### 1. TouchDesigner

Open td/Spectral Sonata.toe
"Attact Mode": generate random patterns on an interval
"Attract While Idle": If no MIDI input after some time, toggle Attract Mode. on MIDI input, disable Attract Mode.

### 2. ArtNet to Serial Bridge

Run bridge/artnet-to-serial-sender.py
Note that TouchDesigner can kick off this script.

### 3. Resolume

Open Resolume composition "Spectral Sonata"
Make sure DMX Output is being sent to Localhost.

### Troubleshooting

Q. Cube not working / paused
A. 
Is the Bridge running and logging that it's working every couple of seconds? If not, reset the bridge script.
Try unplugging and replugging the Teensy USB connection.
