"""
LEGO Spike Prime - Obstacle Avoidance Robot
============================================

This program controls a mobile robot that navigates autonomously and avoids obstacles
using an ultrasonic distance sensor.

Hardware Configuration:
- Left Motor: Port A
- Right Motor: Port B
- Ultrasonic Sensor: Port C (front-facing)
- Color Sensor: Port D (optional, for future enhancements)

Author: LEGO Spike Prime Project
Date: 2026-02-22
"""

from spike import PrimeHub, Motor, DistanceSensor
from spike.control import wait_for_seconds
import time

# ============================================================================
# CONFIGURATION PARAMETERS
# ============================================================================

# Motor ports
LEFT_MOTOR_PORT = 'A'
RIGHT_MOTOR_PORT = 'B'

# Sensor ports
DISTANCE_SENSOR_PORT = 'C'
COLOR_SENSOR_PORT = 'D'  # Optional, for future use

# Movement parameters
FORWARD_SPEED = 50          # Speed for forward movement (0-100)
TURN_SPEED = 40             # Speed for turning (0-100)
OBSTACLE_THRESHOLD = 20     # Distance threshold in cm to detect obstacles
TURN_DURATION = 0.5         # Duration of turn in seconds (adjust for ~90 degrees)

# Safety parameters
MIN_DISTANCE = 10           # Minimum safe distance in cm
MAX_DISTANCE = 200          # Maximum sensor range in cm

# ============================================================================
# INITIALIZE HARDWARE COMPONENTS
# ============================================================================

print("Initializing LEGO Spike Prime Obstacle Avoidance Robot...")

# Initialize the hub
hub = PrimeHub()

# Initialize motors
left_motor = Motor(LEFT_MOTOR_PORT)
right_motor = Motor(RIGHT_MOTOR_PORT)

# Initialize distance sensor
distance_sensor = DistanceSensor(DISTANCE_SENSOR_PORT)

print("Hardware initialized successfully!")
print(f"Obstacle detection threshold: {OBSTACLE_THRESHOLD} cm")
print("Starting obstacle avoidance program...\n")

# Display ready status on hub
hub.light_matrix.write("GO")
wait_for_seconds(1)
hub.light_matrix.off()

# ============================================================================
# MOVEMENT FUNCTIONS
# ============================================================================

def move_forward():
    """
    Move the robot forward by running both motors at the same speed.
    """
    left_motor.start(FORWARD_SPEED)
    right_motor.start(FORWARD_SPEED)


def stop():
    """
    Stop both motors immediately.
    """
    left_motor.stop()
    right_motor.stop()


def turn_right():
    """
    Turn the robot right approximately 90 degrees.
    This is achieved by running the left motor forward and right motor backward.
    """
    # Stop first to ensure clean turn
    stop()
    wait_for_seconds(0.1)
    
    # Turn right by running motors in opposite directions
    left_motor.start(TURN_SPEED)
    right_motor.start(-TURN_SPEED)
    
    # Wait for turn duration
    wait_for_seconds(TURN_DURATION)
    
    # Stop after turn
    stop()
    wait_for_seconds(0.1)


def turn_left():
    """
    Turn the robot left approximately 90 degrees.
    This is achieved by running the right motor forward and left motor backward.
    (Optional function for future enhancements)
    """
    # Stop first to ensure clean turn
    stop()
    wait_for_seconds(0.1)
    
    # Turn left by running motors in opposite directions
    left_motor.start(-TURN_SPEED)
    right_motor.start(TURN_SPEED)
    
    # Wait for turn duration
    wait_for_seconds(TURN_DURATION)
    
    # Stop after turn
    stop()
    wait_for_seconds(0.1)


# ============================================================================
# SENSOR FUNCTIONS
# ============================================================================

def get_distance():
    """
    Get the distance reading from the ultrasonic sensor.
    
    Returns:
        int: Distance in centimeters, or None if reading fails
    """
    try:
        distance = distance_sensor.get_distance_cm()
        
        # Validate reading is within sensor range
        if distance is not None and MIN_DISTANCE <= distance <= MAX_DISTANCE:
            return distance
        else:
            return None
    except:
        # Return None if sensor reading fails
        return None


def is_obstacle_detected():
    """
    Check if an obstacle is detected within the threshold distance.
    
    Returns:
        bool: True if obstacle detected, False otherwise
    """
    distance = get_distance()
    
    if distance is not None:
        return distance <= OBSTACLE_THRESHOLD
    else:
        # If sensor fails, assume obstacle for safety
        return True


# ============================================================================
# MAIN PROGRAM LOOP
# ============================================================================

def main():
    """
    Main program loop for obstacle avoidance behavior.
    The robot moves forward until an obstacle is detected, then stops and turns right.
    """
    print("Robot is now running. Press Ctrl+C to stop.\n")
    
    try:
        while True:
            # Get current distance reading
            distance = get_distance()
            
            # Display distance on console for debugging
            if distance is not None:
                print(f"Distance: {distance} cm", end="\r")
            
            # Check for obstacles
            if is_obstacle_detected():
                # Obstacle detected - execute avoidance behavior
                print("\n⚠️  Obstacle detected! Stopping and turning...")
                
                # Visual feedback on hub
                hub.light_matrix.write("!")
                
                # Stop the robot
                stop()
                wait_for_seconds(0.2)
                
                # Turn right to avoid obstacle
                turn_right()
                
                # Clear hub display
                hub.light_matrix.off()
                
                print("✓ Turn complete. Resuming forward movement.\n")
                
            else:
                # No obstacle - continue moving forward
                move_forward()
            
            # Small delay to prevent excessive sensor polling
            wait_for_seconds(0.05)
    
    except KeyboardInterrupt:
        # Handle program termination gracefully
        print("\n\nProgram stopped by user.")
        stop()
        hub.light_matrix.write("END")
        wait_for_seconds(2)
        hub.light_matrix.off()
    
    except Exception as e:
        # Handle any unexpected errors
        print(f"\n\nError occurred: {e}")
        stop()
        hub.light_matrix.write("ERR")
        wait_for_seconds(2)
        hub.light_matrix.off()


# ============================================================================
# PROGRAM ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    main()

# Made with Bob
