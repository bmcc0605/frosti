#sample driver process used to test sms_demo.py

import alert

#alert.send("Warning: temperature out of bounds for freezer 1!", "freezer")
#alert.send("Warning: Primary Pi has gone down, backup is in effect. Please replace as soon as possible.", "all")
hue = alert.send("Warning: Rodent rebellion imminent in vivarium 4!", "vivarium")
print hue