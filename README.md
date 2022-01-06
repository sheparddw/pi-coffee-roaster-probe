# pi-coffee-roaster-probe
This repo connects a MAX6675 thermocouple up to a Raspberry Pi for tracking Coffee Roasting temperatures through the iOS app Roastmaster over wifi. 
Alter it however you like for your own use!

Here are the pins on the Pi the thermocouple should be plugged into:
cs_pin = 24 #(CS)
clock_pin = 23 #(SCLK/SCK)
data_pin = 22 #(SO/MOSI)

You will need:
- MAX6675 thermocouple with a K style probe and double female jumper cables.
- Raspberry Pi with male GPIO pins
- A wifi adapter unless the pi has built in wifi
- To install Raspian or a similar OS on the pi (make sure it has the pi GPIO Python library installed which is built into Raspian)
- Wifi for your iPad or phone and the pi to both connect to
- Roastmaster iOS app installed on your phone or iPad with data logging in app purchase
- Create new RDP probe in Roastmaster with port 5050 channel 1 and the following serial: kaldidrum  

I am not affiliated with Roastmaster, just a hobby coffee roaster and software developer. 
See the RDP protocol docs here: https://rainfroginc.com/wordpress/wp-content/uploads/2017/03/RDP-Datasheet.pdf
