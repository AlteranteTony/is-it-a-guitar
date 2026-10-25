# is-it-a-guitar
it plays music looks like guitar but isn't 
it is basically a guitar shaped musical messenger that tells your computer what notes to play . 

# what does is-it-a-guitar-do
so it is basically a guitar shaped musical messenger that tells your computer what notes to play. it uses EC11 Rotary Encoders , Bourns Slide Potentiometers , 
Kailh Choc Low-Profile Switches , xiao eps32-s3 and capacitive touch. the capacative touche uses electrical signals from our body to send signals to paly a different note.



# what is in the repo 
the repo contains "code.py" which is the firmware , "PCB&SCHEMATIC-editable file" which like it's name contains pcb and other editable files , "capacitive keys.kicad_mod" is footnote for custom shaped capacitive keys . 

# Tech Stack
- kicad
- python
- arduino ide 

## how to setup
first you will need to install circuit python copy the firmware and paste it hten connect the keyboard and open a midi compatible software and voila youve got yourself a synth.

# controls

| Control | Function |
|---|---|
| Touch Pad 1 (D0) | Plays MIDI note 60 (C4) |
| Touch Pad 2 (D1) | Plays MIDI note 62 (D4) |
| Touch Pad 3 (D2) | Plays MIDI note 64 (E4) |
| Touch Pad 4 (D3) | Plays MIDI note 65 (F4) |
| Touch Pad 5 (D4) | Plays MIDI note 67 (G4) |
| Button 1 (D7) | Triggers MIDI note 36 |
| Button 2 (D6) | Triggers MIDI note 38 |
| Button 3 (D5) | Triggers MIDI note 42 |
| Slider (D8) | Sends MIDI Control Change 1, commonly used for modulation |
| Rotary Encoder (D9, D10) | Sends MIDI Control Change 7, commonly used for volume |

# Parts list
EC11 Rotary Encoders , Bourns Slide Potentiometers , 
Kailh Choc Low-Profile Switches , xiao eps32-s3 and capacitive touc




# Some warnings and my thoughts

YOU MAY CUSTOMIZE THIS PROJECT IN ANY WAY YOU LIKE

PCB WAS CHECKED FOR ERRORS USING KI CAD'S DRC. CHECK PCB FOR ERROR BEFORE MANUFACTURING THE PCB
