# kuka-robot-as-camera-guy

## Artificial Camera Guy
---
### Base Goals:

- Camera must detect face within a reasonable range (left/right, down/up, far/near).
Movement must be smoothed using any (one) method.
- Prepare two setups, run experiments and compare them in a scientific manner. 
- **Pick one of these:**
    1. **Network**: Communication via OpenShowVar (KUKA VAR PROXY) vs. XML via TCP/IP (KRLethernet)
    2. **Camera**: Mounted on the robot wrist vs. located in a fixed location.

### Extended Goals:

- Try various methods for smoothing movement (e.g. n frames fixed average, n frames moving average, n frames moving median,...), compare them in a scientific manner.
- Use a depth-sensor (lidar or structured light, available in the Lab) or infer from the detected face size. Move the robot accordingly.
- Compare both setups mentioned in the base goals.


Document for safety workspace:
in PDF, KUKA System Software
KUKA System Software 8.3
Operating and Programming Instructions for System Integrators
6.11 Configuring workspaces