# is-it-a-guitar
it plays music looks like guitar but isn't 
it is basically a guitar shaped musical messenger that tells your computer what notes to play . 
![image alt](https://github.com/AlteranteTony/is-it-a-guitar/blob/421be2a1fafb23048688aab4dfc987cbc930d15e/pictures/final%20look.png)

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
Kailh Choc Low-Profile Switches , xiao eps32-s3 and capacitive touch

# PCB AND SCHEMATIC 

![image alt](https://github.com/AlteranteTony/is-it-a-guitar/blob/09f79e7851ce0f7fd1af5018fc3a9e7f574d6849/pictures/final%20pcb.png)
![iamge alt](https://github.com/AlteranteTony/is-it-a-guitar/blob/5848bc873acebdd3b811dd7e3a02014f0acbfcfc/pictures/final-finalschematic.png)



# Some warnings and my thoughts

YOU MAY CUSTOMIZE THIS PROJECT IN ANY WAY YOU LIKE

PCB WAS CHECKED FOR ERRORS USING KI CAD'S DRC. CHECK PCB FOR ERROR BEFORE MANUFACTURING THE PCB

# BOM (bill of materials)
|Item                    |Qty|Supplier   |Cost/item|Total Cost|link                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------------|---|-----------|---------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|xiao esp32 s3           |1  |robu       |$12.00   |$12.00    |https://robu.in/product/seeed-studio-xiao-esp32s3-2-4ghz-wifi-ble-5-0/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|rotary encoder          |1  |robu       |$1.04    |$1.04     |https://robu.in/product/EC11%20Rotary%20Encoder%20Module%20with%20Knob%20Cap%20for%20Development%20Boards/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|slide potentiometer     |1  |robu       |$2.61    |$2.61     |https://robu.in/product/pta2043-2010cib254-bourns/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|switches                |3  |ali express|$1.49    |$4.47     |https://www.aliexpress.com/item/1005008089864080.html?spm=a2g0o.productlist.main.2.4d5244ccwm26RT&algo_pvid=ea52910f-184c-41a4-8cc4-522562df4f65&algo_exp_id=ea52910f-184c-41a4-8cc4-522562df4f65-1&pdp_ext_f={%22order%22%3A%22232%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22}&pdp_npi=6%40dis!INR!141.86!141.86!!!9.51!9.51!%40210159d417929564002281166e0d7c!12000045838677521!sea!IN!0!ABX!1!0!n_tag%3A-29910%3Bd%3A191bbc36%3Bm03_new_user%3A-29895&curPageLogUid=jFN2G4yYkuO7&utparam-url=scene%3Asearch&#124;query_from%3A&#124;x_object_id%3A1005008089864080&#124;_p_origin_prod%3A|
|pcb                     |1  |jlcpcb     |$9.83    |$9.83     |https://cart.jlcpcb.com/shopcart/cart/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|Estimated total shipping|1  |           |         |$3.00     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

