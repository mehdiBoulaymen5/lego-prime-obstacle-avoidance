# Testing and Calibration Guide

This guide will help you test and calibrate your LEGO Spike Prime obstacle avoidance robot for optimal performance.

## 🧪 Pre-Testing Checklist

Before running the robot, verify:

- [ ] All motors are securely connected to Ports A and B
- [ ] Ultrasonic sensor is connected to Port C and facing forward
- [ ] Wheels are properly attached and rotate freely
- [ ] Hub battery is charged (at least 50%)
- [ ] Robot is placed on a flat, stable surface
- [ ] Testing area is clear of fragile objects
- [ ] You have a safe way to stop the robot (hub button or Ctrl+C)

## 📊 Testing Phases

### Phase 1: Component Testing

Test each component individually before running the full program.

#### Test 1: Motor Functionality
```python
# Simple motor test program
from spike import Motor
from spike.control import wait_for_seconds

left_motor = Motor('A')
right_motor = Motor('B')

# Test left motor
print("Testing left motor...")
left_motor.run_for_seconds(2, 50)
wait_for_seconds(1)

# Test right motor
print("Testing right motor...")
right_motor.run_for_seconds(2, 50)
wait_for_seconds(1)

print("Motor test complete!")
```

**Expected Results:**
- Left wheel should rotate forward for 2 seconds
- Right wheel should rotate forward for 2 seconds
- Both should run at similar speeds

**If motors don't work:**
- Check port connections
- Verify motor orientation
- Try swapping motors to isolate the issue

#### Test 2: Ultrasonic Sensor
```python
# Simple sensor test program
from spike import DistanceSensor
from spike.control import wait_for_seconds

distance_sensor = DistanceSensor('C')

print("Testing ultrasonic sensor...")
print("Move your hand in front of the sensor")

for i in range(20):
    distance = distance_sensor.get_distance_cm()
    if distance is not None:
        print(f"Distance: {distance} cm")
    else:
        print("No reading")
    wait_for_seconds(0.5)

print("Sensor test complete!")
```

**Expected Results:**
- Distance readings should change as you move your hand
- Readings should be between 4-200 cm
- Values should be relatively stable when hand is stationary

**If sensor doesn't work:**
- Check Port C connection
- Ensure sensor is not blocked
- Clean the sensor lenses
- Try a different port to test the sensor

### Phase 2: Basic Movement Testing

#### Test 3: Straight Line Movement
1. Place robot on a flat surface with at least 2 meters of clear space
2. Mark the starting position
3. Run the robot for 5 seconds moving forward
4. Measure if the robot traveled in a straight line

**Calibration if robot veers:**
- If veers left: Left motor is faster than right
- If veers right: Right motor is faster than left
- Adjust `FORWARD_SPEED` for individual motors if needed

#### Test 4: Turning Accuracy
1. Place robot facing a wall or marker
2. Trigger a turn (manually or via obstacle)
3. Measure the turning angle

**Calibration for turning:**
- Current setting: `TURN_DURATION = 0.5` seconds
- For 90° turn: Adjust duration as needed
- For sharper turns: Increase duration
- For gentler turns: Decrease duration

**Turning Calibration Table:**
| Duration (seconds) | Approximate Angle |
|-------------------|-------------------|
| 0.3 | ~50-60° |
| 0.4 | ~70-80° |
| 0.5 | ~90° |
| 0.6 | ~100-110° |
| 0.7 | ~120-130° |

*Note: Actual angles depend on wheel size, motor speed, and surface friction*

### Phase 3: Obstacle Detection Testing

#### Test 5: Detection Distance Calibration

**Setup:**
1. Place robot on flat surface
2. Position a flat obstacle (book, box) in front
3. Measure distance from robot to obstacle

**Test Procedure:**
1. Start with obstacle at 30cm
2. Run the program
3. Observe when robot stops
4. Measure actual stopping distance
5. Repeat at 20cm, 15cm, 10cm

**Recording Results:**
| Obstacle Distance | Robot Stopped? | Actual Stop Distance |
|------------------|----------------|---------------------|
| 30 cm | | |
| 20 cm | | |
| 15 cm | | |
| 10 cm | | |

**Calibration:**
- If robot stops too early: Decrease `OBSTACLE_THRESHOLD`
- If robot stops too late: Increase `OBSTACLE_THRESHOLD`
- Recommended range: 15-25 cm

#### Test 6: Different Obstacle Types

Test with various obstacles to ensure reliable detection:

**Obstacle Types to Test:**
- [ ] Flat wall or board (best case)
- [ ] Cardboard box
- [ ] Cylindrical object (bottle, can)
- [ ] Irregular shaped object
- [ ] Dark colored object
- [ ] Reflective surface
- [ ] Thin object (pole, stick)

**Notes:**
- Ultrasonic sensors work best with flat, solid surfaces
- Very thin objects may not be detected reliably
- Soft materials (fabric, foam) may absorb ultrasonic waves

### Phase 4: Full System Testing

#### Test 7: Obstacle Course

**Setup:**
Create a simple obstacle course:
```
Start → [2m clear] → [Obstacle 1] → [Turn] → [1m clear] → [Obstacle 2] → [Turn]
```

**Test Procedure:**
1. Place robot at start position
2. Run the program
3. Observe robot behavior
4. Record any issues

**Success Criteria:**
- [ ] Robot moves forward smoothly
- [ ] Detects all obstacles
- [ ] Stops before hitting obstacles
- [ ] Turns successfully
- [ ] Continues after turning
- [ ] No crashes or collisions

#### Test 8: Extended Runtime Test

**Purpose:** Verify stability over longer periods

**Test Procedure:**
1. Run robot in open area for 5 minutes
2. Monitor for any issues
3. Check battery level after test

**Observations to Record:**
- Any unexpected stops
- Sensor reading failures
- Motor performance degradation
- Battery consumption rate

## 🔧 Calibration Parameters

### Recommended Starting Values
```python
FORWARD_SPEED = 50          # Good balance of speed and control
TURN_SPEED = 40             # Slightly slower for precise turns
OBSTACLE_THRESHOLD = 20     # Safe detection distance
TURN_DURATION = 0.5         # Approximately 90 degrees
```

### Calibration for Different Scenarios

#### For Tight Spaces
```python
FORWARD_SPEED = 30          # Slower for better control
OBSTACLE_THRESHOLD = 25     # Detect obstacles earlier
TURN_DURATION = 0.6         # Larger turns to clear obstacles
```

#### For Open Areas
```python
FORWARD_SPEED = 70          # Faster movement
OBSTACLE_THRESHOLD = 15     # Can detect closer
TURN_DURATION = 0.4         # Quicker turns
```

#### For Precise Navigation
```python
FORWARD_SPEED = 40          # Moderate speed
TURN_SPEED = 30             # Slower, more controlled turns
OBSTACLE_THRESHOLD = 22     # Balanced detection
TURN_DURATION = 0.5         # Standard 90° turn
```

## 📝 Testing Log Template

Use this template to record your testing results:

```
Date: _______________
Battery Level: ______%
Surface Type: _______________

Test Results:
-------------
Motor Test:
- Left Motor: [ ] Pass [ ] Fail
- Right Motor: [ ] Pass [ ] Fail

Sensor Test:
- Distance Readings: [ ] Pass [ ] Fail
- Detection Range: _____ cm

Movement Test:
- Straight Line: [ ] Pass [ ] Fail
- Turning Angle: _____ degrees

Obstacle Detection:
- Detection Distance: _____ cm
- Response Time: [ ] Fast [ ] Slow

Full System:
- Obstacle Course: [ ] Pass [ ] Fail
- Extended Runtime: [ ] Pass [ ] Fail

Issues Found:
_________________________________
_________________________________

Calibration Changes Made:
_________________________________
_________________________________

Notes:
_________________________________
_________________________________
```

## 🎯 Performance Optimization Tips

### Improving Detection Accuracy
1. Mount sensor at consistent height (10-15cm)
2. Ensure sensor is level and facing forward
3. Keep sensor lenses clean
4. Test in consistent lighting conditions

### Improving Movement Precision
1. Use wheels of equal size
2. Ensure motors are aligned parallel
3. Check that wheels spin freely
4. Test on consistent surface types

### Improving Battery Life
1. Reduce motor speeds if possible
2. Minimize unnecessary sensor polling
3. Optimize turn durations
4. Use efficient movement patterns

## ⚠️ Common Issues and Solutions

### Issue: Robot veers to one side
**Solution:** 
- Check wheel alignment
- Verify both motors run at same speed
- Adjust individual motor speeds if needed

### Issue: Inconsistent obstacle detection
**Solution:**
- Clean sensor lenses
- Check sensor mounting stability
- Increase detection threshold
- Add sensor reading validation

### Issue: Robot turns too much/too little
**Solution:**
- Calibrate `TURN_DURATION` parameter
- Check surface friction
- Verify wheel sizes are equal
- Test on different surfaces

### Issue: Robot stops randomly
**Solution:**
- Check battery level
- Verify all connections are secure
- Look for sensor reading errors
- Check for motor overheating

## ✅ Final Validation Checklist

Before considering testing complete:

- [ ] All components tested individually
- [ ] Straight line movement verified
- [ ] Turning angle calibrated
- [ ] Obstacle detection working reliably
- [ ] Full obstacle course completed successfully
- [ ] Extended runtime test passed
- [ ] All parameters documented
- [ ] Testing log completed

## 📊 Expected Performance Metrics

After proper calibration, your robot should achieve:

- **Detection Range:** 15-25 cm
- **Detection Accuracy:** >95% for flat obstacles
- **Turning Accuracy:** ±10° from target angle
- **Straight Line Deviation:** <5 cm per meter
- **Response Time:** <0.2 seconds from detection to stop
- **Runtime:** 30+ minutes on full charge

---

**Remember:** Every robot is slightly different due to building variations. Take time to calibrate your specific robot for best results!