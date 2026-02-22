# LEGO Spike Prime - Obstacle Avoidance Robot

A simple autonomous mobile robot that navigates and avoids obstacles using the LEGO Spike Prime robotics kit.

## 📋 Table of Contents
- [Features](#features)
- [Hardware Requirements](#hardware-requirements)
- [Assembly Instructions](#assembly-instructions)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)

## ✨ Features

- **Autonomous Navigation**: Robot moves forward continuously
- **Obstacle Detection**: Uses ultrasonic sensor to detect obstacles up to 20cm away
- **Automatic Avoidance**: Stops and turns right when obstacles are detected
- **Visual Feedback**: Hub display shows status messages
- **Safety Features**: Validates sensor readings and handles errors gracefully
- **Well-Documented Code**: Comprehensive comments for easy understanding and modification

## 🔧 Hardware Requirements

### Required Components
- 1x LEGO Spike Prime Hub
- 2x Large Motors (for wheels)
- 1x Ultrasonic Distance Sensor
- 1x Color Sensor (optional, for future enhancements)
- LEGO building pieces for chassis construction
- 2x Wheels (compatible with large motors)

### Port Configuration
```
Port A: Left Motor
Port B: Right Motor
Port C: Ultrasonic Distance Sensor (front-facing)
Port D: Color Sensor (optional, bottom-facing)
```

## 🏗️ Assembly Instructions

### Step 1: Build the Chassis
1. Create a stable base platform using LEGO bricks
2. Mount the Spike Prime Hub in the center of the chassis
3. Ensure the hub is securely attached and balanced

### Step 2: Attach the Motors
1. Mount the left motor on Port A to the left side of the chassis
2. Mount the right motor on Port B to the right side of the chassis
3. Ensure motors are at the same height and aligned parallel
4. Attach wheels to both motors

### Step 3: Mount the Ultrasonic Sensor
1. Attach the ultrasonic sensor to Port C
2. Mount it at the front of the robot, facing forward
3. Position it approximately 10-15cm above the ground
4. Ensure it has a clear view ahead without obstructions

### Step 4: Optional Color Sensor
1. If using the color sensor, attach it to Port D
2. Mount it at the bottom of the chassis, facing downward
3. Position it close to the ground (1-2cm clearance)

### Step 5: Final Checks
- Verify all connections are secure
- Check that wheels rotate freely
- Ensure the robot is balanced and stable
- Test that the hub powers on correctly

## 💻 Installation

### Prerequisites
- LEGO Spike Prime Hub with latest firmware
- LEGO Education Spike App or Python development environment
- USB cable or Bluetooth connection to the hub

### Loading the Program

#### Method 1: Using LEGO Spike App
1. Open the LEGO Education Spike App
2. Connect to your Spike Prime Hub
3. Create a new Python project
4. Copy the contents of `obstacle_avoidance_robot.py`
5. Paste into the Python editor
6. Upload the program to the hub

#### Method 2: Using VS Code with LEGO Extension
1. Install the LEGO Education Spike Prime extension for VS Code
2. Connect to your Spike Prime Hub
3. Open `obstacle_avoidance_robot.py`
4. Click "Download to Hub" or press F5

## 🚀 Usage

### Running the Program

1. **Place the robot** in an open area with obstacles to avoid
2. **Power on** the Spike Prime Hub
3. **Run the program** from the hub menu or your development environment
4. The hub display will show "GO" briefly, then the robot will start moving
5. **Observe** the robot as it navigates and avoids obstacles

### Expected Behavior

1. Robot moves forward at constant speed
2. When an obstacle is detected within 20cm:
   - Robot stops immediately
   - Hub display shows "!" symbol
   - Robot turns right approximately 90 degrees
   - Robot resumes forward movement
3. This cycle repeats continuously

### Stopping the Program

- **From Hub**: Press the center button on the hub
- **From Computer**: Press Ctrl+C in the terminal/console
- The robot will stop motors and display "END" on the hub

## ⚙️ Configuration

You can customize the robot's behavior by modifying these parameters in `obstacle_avoidance_robot.py`:

### Movement Parameters
```python
FORWARD_SPEED = 50          # Speed for forward movement (0-100)
TURN_SPEED = 40             # Speed for turning (0-100)
OBSTACLE_THRESHOLD = 20     # Distance in cm to detect obstacles
TURN_DURATION = 0.5         # Duration of turn in seconds
```

### Tuning Guide

**To make the robot move faster:**
- Increase `FORWARD_SPEED` (max: 100)

**To detect obstacles earlier:**
- Increase `OBSTACLE_THRESHOLD` (e.g., 30cm)

**To detect obstacles later:**
- Decrease `OBSTACLE_THRESHOLD` (e.g., 15cm)

**To adjust turning angle:**
- Increase `TURN_DURATION` for larger turns (e.g., 0.7 for ~120°)
- Decrease `TURN_DURATION` for smaller turns (e.g., 0.3 for ~60°)

**To make turns sharper:**
- Increase `TURN_SPEED`

## 🔍 Troubleshooting

### Robot doesn't move forward
- **Check**: Motor connections on Ports A and B
- **Check**: Motors are not blocked or jammed
- **Check**: Battery level is sufficient
- **Try**: Increase `FORWARD_SPEED` value

### Robot doesn't detect obstacles
- **Check**: Ultrasonic sensor is connected to Port C
- **Check**: Sensor is facing forward without obstructions
- **Check**: Obstacle is within sensor range (4-200cm)
- **Try**: Increase `OBSTACLE_THRESHOLD` value

### Robot turns too much/too little
- **Adjust**: `TURN_DURATION` parameter
- **Check**: Motors are running at equal speeds
- **Check**: Wheels are the same size
- **Try**: Calibrate by testing different duration values

### Robot moves in circles
- **Check**: Both motors are properly connected
- **Check**: Wheels are securely attached
- **Check**: Motors are aligned parallel to each other
- **Try**: Swap motor ports to test individual motors

### Sensor readings are inconsistent
- **Check**: Sensor is mounted securely
- **Check**: No loose connections
- **Check**: Sensor lens is clean
- **Try**: Add a small delay between readings

### Program crashes or freezes
- **Check**: Hub firmware is up to date
- **Check**: All imports are correct
- **Try**: Restart the hub
- **Try**: Re-upload the program

## 🎯 Future Enhancements

Here are some ideas to extend the robot's capabilities:

### Easy Enhancements
1. **Alternate Turning**: Make the robot turn left and right alternately
2. **Speed Control**: Slow down as the robot approaches obstacles
3. **Sound Effects**: Add beeps when obstacles are detected
4. **LED Indicators**: Use hub lights to show different states

### Intermediate Enhancements
1. **Color Detection**: Stop on specific floor colors using the color sensor
2. **Random Exploration**: Add randomness to turning direction
3. **Distance Display**: Show distance readings on the hub display
4. **Multiple Speeds**: Different speeds for different situations

### Advanced Enhancements
1. **Wall Following**: Keep a constant distance from walls
2. **Room Mapping**: Create a simple map of the environment
3. **Return to Start**: Navigate back to starting position
4. **Multi-Sensor Fusion**: Combine ultrasonic and color sensor data

## 📚 Additional Resources

- [LEGO Spike Prime Python API Documentation](https://education.lego.com/en-us/product-resources/spike-prime/downloads/python-api)
- [LEGO Education Support](https://education.lego.com/en-us/support)
- [Python Programming Basics](https://www.python.org/about/gettingstarted/)

## 📝 Notes

- The import errors shown in the editor are normal - the `spike` library is only available on the LEGO Spike Prime Hub
- Always test in a safe environment away from edges and fragile objects
- Keep the hub firmware updated for best performance
- Battery level affects motor performance - recharge when needed

## 🤝 Contributing

Feel free to modify and improve this project! Some suggestions:
- Optimize the obstacle detection algorithm
- Add new sensor integrations
- Improve the turning logic
- Create alternative navigation strategies

## 📧 Contact

For questions, feedback, or collaboration opportunities, please contact:
- **Email**: mehdi.boulaymen@ibm.com

---

**Happy Building and Coding! 🤖**