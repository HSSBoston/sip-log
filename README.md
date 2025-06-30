<p align="center">
  <img src="images/logo.jpg" width="750" />
</p>

Sip Log is a mobile device that computerizes a water bottle to monitor water intake during physical activity. Attached to the bottom of a bottle, it keeps track of how many times you drank water, estimates how much water you drank in total, records intake log in the cloud, and reminds you to hydrate via smartphone notification. It aims to aid athletes be more aware of their water intake, along with preventing dehydration from affecting their performance. Sip Log uses a battery-operated ESP32 microcontroller (M5StickC PLUS2) that runs CircuitPython code to detect water intake by sensing the tilt of a bottle with a 3-axis accelerometer. 

This project was presented at [PhysTech 2025](https://phystech2025.devpost.com/). It won a [3rd place](https://phystech2025.devpost.com/project-gallery) award.

### Key Features:

- Tilt sensing: Continuously sensing the tilt of a water bottle with an accelerometer
- Water intake detection: Detecting water intake when the tilt of the bottle is greater than 45 degrees. 
- Water intake logging: Recording water intake log in a cloud database (Kintone).
- Analyzing water intake log: Graphing intake log and estimating hourly/daily intake.
- Hydration reminder: Sending reminders to a phone.


https://github.com/user-attachments/assets/a5976171-7105-413c-b124-96ba7348cdee

