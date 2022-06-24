# EV3-OpenMV-Stuff
An OpenMV software, hardware example for LEGO Mindstroms EV3 (support SPIKE/RI).

## How it works
Team ceeoinnovations created a MicroPython library for the LEGO UART Protocol that can be used with OpenMV, and we wrote a sample program to let OpenMV detect objects by color and mark them with IDs on the screen (OpenMV IDE view) and send the largest object information to EV3.

## Hardware
![](https://github.com/ofdl-robotics-tw/EV3-OpenMV-Stuff/blob/main/Adapter%20PCB/EV3OpenMV_PCB_rev1.PNG?raw=true)

We designed a simple PCB that can combine OpenMV Board and EV3 Port, and Lego holes can be used to fasten the board to Lego brick.

## Software
Using OpenMV python, open "FindBlobEx_LMS.py" and copy the "LPF2.py" to OpenMV disk drive, then Download the program to OpenMV, connect OpenMV to EV3, and OpenMV IDE screen will show the object ID with square, EV3 will receive the largest object information(You can change the code to send diffrent information to EV3). 

Go to release page to download EV3-G blocks, the block will return following info:
  * For a block:
    * `Connection status` see **Connection Status Code** below
    * `ID` ID of Block
    * `X` X Center of Block
    * `Y` Y Center of Block
    * `W` Width of Block
    * `H` Height of Block

## Documents used
 - [PyBricks - LEGO Powered Up UART Protocol](https://github.com/pybricks/technical-info/blob/master/uart-protocol.md)
 - [ceeoinnovations/SPIKEPrimeBackpacks](https://github.com/ceeoinnovations/SPIKEPrimeBackpacks)
 - [EV3 Hardware Developer Kit](https://education.lego.com/en-us/support/mindstorms-ev3/developer-kits)

## Disclaimer
LEGO® is a trademark of the LEGO Group of companies which does not sponsor, authorize or endorse this software.
The LEGO Group and contributors to this repo are not liable for any loss, injury or damage arising from the use or misuse of the provided code or hardware.
