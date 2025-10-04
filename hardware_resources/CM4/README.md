## Overview

This section will contain details specific to the Raspberry Pi CM4

### Display

While the Raspberry Pi CM4 has the GPIO bandwidth to support DPI displays, it uses far too many GPIO lanes than is allowed for this design.

In my opinion, you have to go with SPI or DSI displays if you want to also include other features like an I2C-interfaced click wheel, expandable Micro-SD storage, among other things.


### SD Card

