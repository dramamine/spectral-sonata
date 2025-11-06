

# Spectral Sonata

Spectral Sonata is an interactive art piece. A MIDI keyboard controls visuals on an LED cube.

The LED cube is made of HUB75 panels. Panels are controlled by a Teensy 4.1 with the Smartmatrix Shield adaptor.

LED data is sent via USB cable to the cube.

## Setup

Flash the Teensy 4.1 with smartmatrix-serial-5panel.ino

## How To Run - Interactive Mode

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

Make sure Advanced Output is set to the "Smartmatrix cube map"

### Troubleshooting

#### Q. Cube not working / paused

Is the Bridge running and logging that it's working every couple of seconds? If not, reset the bridge script.

Try unplugging and replugging the Teensy USB connection.

Close any Arduino IDE instances as they might be using the Teensy comms port.

#### Q. MIDI controller not doing anything

Make sure MIDI controller is mapped in TouchDesigner. Check the MIDI Mapper menu and check the device ID in the sketch.


## How To Run - Show Mode

Record 80 universes of data from Lightjams.

From lightdream-pocket
```
cd artnet-to-sd-card
video2sdcard.py --sequence_path "./170x80-smartled-matrix-content.mp4"
```

SD card needs output.bin on it.

Flash the Teensy 4.1 with videosdcard-smartmatrix-5panel.ino
