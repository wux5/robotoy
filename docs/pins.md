# Yahboom board pins mapping

## 40 Pins
```text
   3V3  (1) (2)  5V    
 GPIO2  (3) (4)  5V    
 GPIO3  (5) (6)  GND   
 GPIO4  (7) (8)  GPIO14
   GND  (9) (10) GPIO15
GPIO17 (11) (12) GPIO18
GPIO27 (13) (14) GND   
GPIO22 (15) (16) GPIO23
   3V3 (17) (18) GPIO24
GPIO10 (19) (20) GND   
 GPIO9 (21) (22) GPIO25
GPIO11 (23) (24) GPIO8 
   GND (25) (26) GPIO7 
 GPIO0 (27) (28) GPIO1 
 GPIO5 (29) (30) GND   
 GPIO6 (31) (32) GPIO12
GPIO13 (33) (34) GND   
GPIO19 (35) (36) GPIO16
GPIO26 (37) (38) GPIO20
   GND (39) (40) GPIO21
```
## Yahboom Board to GPIO Mapping
|  classification | Features | Schematic number | Arduino | STM32 | 51 | raspberry pie | Remarks |
| --- | --- | --- | --- | --- | :---: | --- | --- |
|  Car sports | Left motor front | AIN2 | **8** | **pb9** | **P2.1** | **IO20** |  |
|   | After the left motor | AIN1 | **7** | **PB8** | **P2.2** | **IO21** |  |
|   | Right motor front | BIN2 | **2** | **PB4** | **P2.4** | **IO19** |  |
|   | After the right motor | BIN1 | **4** | **PB5** | **P2.3** | **IO26** |  |
|   | Left motor PWM | PWMA | **6** | **PB7** | **P2.0** | **IO16** |  |
|   | Right motor PWM | PWMB | **5** | **PB6** | **P2.5** | **IO13** |  |
|  Track sensor | Left 1 | IN2 | **A2** | **PC14** | **P1.1** | **IO3** | **Arduino needs jumpers, others don't need jumpers** |
|   | Left 2 | IN1 | **A1** | **PC13** | **P1.0** | **IO5** |  |
|   | Right 1 | IN3 | **A3** | **PC15** | **P1.2** | **IO4** |  |
|   | Right 2 | IN4 | **A4** | **PB12** | **P1.3** | **IO18** |  |
|  Infrared obstacle avoidance | left | IN7 | **A3** | **PA6** | **P1.6** | **IO12** | **Arduino needs jumpers, others don't need jumpers** |
|   | right | IN5 | **A1** | **PA4** | **P1.4** | **IO17** |  |
|  Light seek sensor | left | IN8 | **A4** | **PB3** | **P1.7** | **IO7** |  |
|   | right | IN6 | **A2** | **PA5** | **P1.5** | **IO6** |  |
|  Grayscale sensor | Grayscale sensor | GS | **A5** | **PA1** | **no** | **no** |  |
|  button | button | K2 | **A0** | **PA0** | **P2.7** | **IO8** |  |
|  buzzer | buzzer | FM | **A0** | **PA0** | **P2.7** | **IO8** |  |
|  fan | fan | MOTOR | **A5** | **PA1** | **P0.0** | **IO2** |  |
|  Colorful searchlight | red | LED_R | **11** | **PB1** | **P3.2 / INT0** | **IO22** |  |
|   | green | LED_G | **10** | **PB0** | **P3.3 / INT1** | **IO27** |  |
|   | blue | LED_B | **9** | **PA7** | **P3.4 / T0** | **IO24** |  |
|  Yuntai | Yuntai | J1 | **3** | **PA11** | **P0.5** | **IO23** |  |
|  Ultrasonic | send | SCL_C | **13** | **PA15** | **P3.7 / RD** | **ID_SC** |  |
|   | receive | SDA_C | **12** | **PA12** | **P3.6 / WR** | **ID_SD** |  |
|  Infrared remote control | Infrared remote control | IRN | **A5** | **PA1** | **P3.5/T1** | **IO2** | Need jumpers |
|  Voltage detection | Voltage detection | POWERC | **A0** | **PA0** | **no** | **no** | Need jumpers |
|  PS2 | DAWDLE | MOS | **A3** | **PB15** | **P0.2** | **IO10** |  |
|   | MISO | WHO | **A2** | **PB14** | **P0.3** | **IO9** |  |
|   | GND | GND | **GND** | **GND** | **GND** | **GND** |  |
|   | VCC | VCC | **VCC** | **VCC** | **VCC** | **VCC** |  |
|   | CS | CS | **A4** | **PA8** | **P0.1** | **IO25** |  |
|   | SCK | SCK | **A1** | **PB13** | **P0.4** | **IO11** |  |
|  MPU6050 | clock | SCL | **SCL** | **PB10** | **P0.7** | **no** |  |
|   | data | SDA | **SDA** | **PB11** | **P0.6** | **no** |  |
|  Robot | Degree of freedom 1 | J1 | **3** | **PA11** | **P0.5** | **IO23** |  |
|   | Degree of freedom 2 | J2 | **A1** | **PB13** | **P0.4** | **IO11** |  |
|   | Degree of freedom 3 | J3 | **A2** | **PB14** | **P0.3** | **IO9** |  |
|   | Degree of freedom 4 | J4 | **A3** | **PB15** | **P0.2** | **IO10** |  |
|   | Degree of freedom 5 | J5 | **A4** | **PA8** | **P0.1** | **IO25** |  |
|   | Degree of freedom 6 | J6 | **A5** | **PA1** | **P0.0** | **IO2** |  |
|  24L01 wireless | RST | RST | **A5** | **PA1** | **P0.0** | no |  |
|   | SCK | SCK | **A1** | **PB13** | **P0.4** | no |  |
|   | MISSION | MISSION | **A2** | **PB14** | **P0.3** | no |  |
|   | DAWDLE | DAWDLE | **A3** | **PB15** | **P0.2** | no |  |
|   | CS | CS | **A4** | **PA8** | **P0.1** | no |  |
|  Linear CCD camera | A0 | A0 | **A1** | **PB13** | **no** | no |  |
|   | CLK | CLK | **A3** | **PB15** | **no** | no |  |
|   | AND | AND | **A2** | **PB14** | **no** | no |  |