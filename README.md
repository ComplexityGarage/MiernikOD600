# Title of the project
OD600-Meter
# Authors 
- Mikołaj Włochowicz and Kamil Adach
# Description of the project 
The aim of this project was to create a simple but powerfull device commonly used in biology laboratories - OD600 meter. Thanks to this, one can measure the optical density of bacteria or yeast culture in 600 nm wavelength peak. It is commonly known that even such simple machines are sometimes overpriced and because of that we decided to make functional, on budget small device.
# Science and tech used 
Lambert-Beer's law is used to measure it. Even thought this formula refers specifically to absorption, it is also used in case of dispersal. It measures first the BLANK (usually the growing medium without microrganisms - more on that later) which is the background also refered as I0, and the SAMPLE containing the microrganisms (noted as In). There's visible, linear corelation between OD600 and the number of microrganisms in the solution in some range (from 0.1 to 1.0 OD).
Growing medium: Luria-Broth (also referred as 'LB') is a mixture of highly nutritious compounds which let bacteria and yeasts multiply in artifitial environment - it will be used as BLANK and also SAMPLE (containing baker's yeast in this experiment).
For this experiment we cultured baker's yeast in LB medium overnight in shaking conditions of 250 rpm in 37°C. In order to check how our device corelates with others we did multiple dilutions of the overnight culture and ended up with such set: BLANK; 0X; 2X; 5X; 10X; 50X; 100X; 1000X. We measured OD600 on our device and it gave quite consistent data with commercial machines in some range.

**Electronics used in this project:**
• Phototransistor TEPT4400;
• Yellow LED diode (close to 600 nm);
• Resistor 4.7k;
• Resistor 0.33k;
• Raspberry Pi Pico H;
# Connections 
**Connections of the electronics:**
GPIO 15: LED terminal to 0.33K resistor to GND;
GPIO 16: Tact switch button (BLANK BUTTON);
GPIO 17: Tact switch button (MEASUREMENT BUTTON)
ADCO(GP26): TEPT4400 to 4.7K resistor to GND;
3V3(OUT): plus(+) terminal;

  
# State of the art 
We managed to assamble and write a python code for our device. It is able to run on it's own - just from the phone charger or USB charging port of our computer. We decided to compare it to commercial device such as NanoDrop.
# What next?
The results we got showed us what should be made better:
• creating the 'calibration curve' - growing yeasts for certain time, conducting several dilutions as before but also growing a small amount of this solution on petri dish in order to assess how much of the colony forming unit we have in certain volume of our culture. This will let us create more precise device
• increasing the sensitivity of our device by use of transimpedance amplifier 
• making proper case for the whole machine
# Sources 
- [Writing on GitHub] ( https://docs.github.com/en/get-started/writing-on-github ) 
