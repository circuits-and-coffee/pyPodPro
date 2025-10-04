# Hardware and Platform
This section will contain resources for PCB design (in case you want to dive into the world of custom capes and hats), wiring schematics, and whatnot.

(TODO: Clean this section up so it's not just a link dump)


## CM4 Route (Likely what I'll end up using)
[Tutorial for carrier board creation](https://www.youtube.com/watch?v=ypcPJC_umPQ)

https://github.com/ShawnHymel/rpi-cm4-demo-carrier

## PocketBeagle 2 Route
https://www.digikey.com/en/product-highlight/b/beagleboard/pocketbeagle-2
https://www.armbian.com/pocketbeagle-2/


## Display
[E24RB-FW360-N TFT Display Module](https://focuslcds.com/product/e24rb-fw360-n/)

- Uses ST7789V controller
- Transflective polarizer (should have high viewing angles)
- Supports 8/9/16/18-Bit MCU, 16/18-Bit RGB, 3/4-wire Serial, 3/4-wire SPI interface
- [Specs Sheet](https://focuslcds.com/wp-content/uploads/Specs/E24RB-FW360-N_Spec.pdf)

## Power Management
- [BQ25895 I2C Fast Charger](https://www.ti.com/lit/ds/symlink/bq25895.pdf)
- [TPS61165 LED Driver](https://www.ti.com/lit/ds/symlink/tps61165.pdf)

### Minimal BOM (seed list)
 - Charger/Power‑path: BQ25895 (QFN‑24), or MP2639B (QFN‑26) + their app‑note passives.
 - 5 V boost (if separate): TPS61236P (+ inductor 22–47 µH; size per load).
 - Backlight driver: TPS61165 (+ 10 Ω RSET, diode, inductor/caps per “typical app”).
 - Panel switches: TPS22918 ×2 (panel logic & any aux 5 V to display accessories).
 - RTC (optional but nice for alarms): e.g., RV‑3028
 - JST‑PH‑2 battery, ESD/TVS at USB‑C VBUS, bulk ceramics near CM4 5 V pins.

[Example](https://github.com/electricimp/BQ25895/blob/master/Examples/README.md)