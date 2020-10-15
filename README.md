# Botnet deection on IoT Devices
![IoT Botnet](https://i.imgur.com/xsRFm2I.png)
### Introduction:
Internet of Things (IoT) devices are widely used in modern homes and every part of our lives, because they are not that sophisticated, it becomes an easy target for Denial of service attack. IoT devices can be used as bots to launch a distributed DOS attack.

The rapid growth of IoT devices which can be more easily compromised than desktop computers has led to an increase in the occurrences of IoT based botnet attacks. Botnet attack is a type of DDOS attack, where the attacker uses a large number of IoT devices to participate in the DOS to overwhelm a specific target. THis type of attack is hard to detect, since the device keeps functioning normally, and the user or the owner of the device will not notice if his device is a part of an attack, in some cases the device may suffer from delay of its functionality.

Botnets such as Mirai are typically constructed in several distinct operational steps
- propagation
- infection
- C&C communication
- execution of attacks.



### Dataset:
[Download](https://archive.ics.uci.edu/ml/datasets/detection_of_IoT_botnet_attacks_N_BaIoT)
The N-BaIoT dataset was collected from a real network traffic of nine IoT devices. The data contains both benign and attack traffic. The dataset is separated where each device has its files, each file contains a type of traffic such as normal traffic or attacks. There are ten classes of attacks that were generated using two families of botnet attack codes from the github (Mirai, Bashlite). N-BaIoT dataset has 115 features, all of these features are statistical analysis, which is extracted from the packet traffic for various periods.

The dataset contains the following nine device normal & attack traffic.
- Danmini - Doorbell
- Ennio  - Doorbell
- Ecobee - Thermostat
- Philips B120N/10 - Baby Monitor
- Provision PT-737E - Security Camera
- Provision PT-838 - Security Camera
- Simple Home XCS7-1002-WHT - Security Camera
- Simple Home XCS7-1003-WHT - Security Camera
- Samsung SNH 1011 N - Web cam

#### Feature information:
##### Stream aggregation:
- H: ("Source IP" in N-BaIoT paper) Stats summarizing the recent traffic from this packet's host (IP)
- MI: ("Source MAC-IP" in N-BaIoT paper) Stats summarizing the recent traffic from this packet's host (IP + MAC)
- HH: ("Channel" in N-BaIoT paper) Stats summarizing the recent traffic going from this packet's host (IP) to the packet's destination host.
- HH_jit: ("Channel jitter" in N-BaIoT paper) Stats summarizing the jitter of the traffic going from this packet's host (IP) to the packet's destination host.
- HpHp: ("Socket" in N-BaIoT paper) Stats summarizing the recent traffic going from this packet's host+port (IP) to the packet's destination host+port. Example 192.168.4.2:1242 -> 192.168.4.12:80

- Time-frame (The decay factor Lambda used in the damped window):
    - How much recent history of the stream is capture in these statistics
    - L5, L3, L1, L0.1 and L0.01

- The statistics extracted from the packet stream:
   - weight: The weight of the stream (can be viewed as the number of items observed in recent history)
   - mean: …
   - std: …
   - radius: The root squared sum of the two streams' variances
   - magnitude: The root squared sum of the two streams' means
   - cov: An approximated covariance between two streams
   - pcc: An approximated correlation coefficient between two streams
   
### EDA

| Device | Chart |
| --- | --- |
| Ennio Door bell | ![Door bell](https://i.imgur.com/d17INis.png)
| Danmin Door bell | ![Door bell 2](https://i.imgur.com/h7dk8RY.png)
| Ecobee Thermostat | ![Thermo stat](https://i.imgur.com/cnF53Fs.png)
| Ennio Door bell | ![Door bell](https://i.imgur.com/gssflL9.png)
| Danmin Door bell | ![Door bell 2](https://i.imgur.com/KXThLsS.png)
| Ecobee Thermostat | ![Thermo stat](https://i.imgur.com/JbCMTsc.png)
| Ennio Door bell | ![Door bell](https://i.imgur.com/Htgp7hq.png)
| Danmin Door bell | ![Door bell 2](https://i.imgur.com/C1J98PJ.png)
| Ecobee Thermostat | ![Thermo stat](https://i.imgur.com/Sxpbefe.png)

### Pre processing & Training

### Modeling

### Deploymnet

### Future works

### Credits & Links

