# Author - Akansha Verma
# This project build a complete simulator for a smart home monitoring system.

import random
from datetime import datetime

event_log = []

# ======================================================
# STEP 2 - Dictionary Implementation
# ======================================================
def initialize_sensor():
    sensors = [
        {
            "id": 1,
            "location": "Front door",
            "type" : "motion",
            "current_value": "closed"
        },
        {
            "id": 2,
            "location": "Kitchen",
            "type" : "temperature",
            "current_value": random.randint(20, 100)
        },
        {
            "id": 3,
            "location": "Living Room",
            "type": "motion",
            "current_value": False
        }
    ]
    return sensors

def create_alert(sensor_id, msg):
    alert = {
            "sensor_id": sensor_id,
            "message": msg,
            "timestamp": datetime.now()
        }
    return alert

sensors = initialize_sensor()
print(sensors)

# ======================================================
# STEP 3 - If/Else Logic
# ======================================================

# following function return alerts for abnormal sensor readings
def check_sensor_reading(sensor, house_mode):
    sensor_type = sensor["type"]
    value = sensor["current_value"]
    
    # Security Alerts:
    if sensor_type == "motion":
        if value and house_mode == "away":
            return create_alert(sensor["id"], "Motion detected while away " + sensor["location"])
    elif sensor_type == "door":
        if value == "open" and house_mode == "away":
            return create_alert(sensor["id"], "Door opened while away " + sensor["location"])
    # Safety Alerts:
    if sensor_type == "temperature":
        if value > 95:
            return create_alert(sensor["id"], "Equiment failure" + sensor["location"])
        elif value < 35:
            return create_alert(sensor["id"], "Frozen pipe risk " + sensor["location"])
        elif house_mode == "home" and (value > 65 and value < 75):
            return create_alert(sensor["id"], "Temperature outside comfort zone " + sensor["location"])
    
    elif sensor_type == "smoke":
        if value:
            return create_alert(sensor["id"], "Smoke detected " + sensor["location"])
        
    return "Reading is normal"

# sample data to test the above if/else logic
motion_sensor = {
    "id": 1,
    "type": "motion",
    "location": "Living Room",
    "current_value": random.choice([True, False])
}

door_sensor = {
    "id": 2,
    "type": "door",
    "location": "Front Door",
    "current_value": random.choice(["open", "closed"])
}

temperature_sensor = {
    "id": 3,
    "type": "temperature",
    "location": "Kitchen",
    "current_value": random.randint(20, 100)
}

smoke_sensor = {
    "id": 4,
    "type": "smoke",
    "location": "Hallway",
    "current_value": random.choice([True, False])
}

house_mode = "away"

print("check motion sensor:", check_sensor_reading(motion_sensor, house_mode))
print("check door sensor:", check_sensor_reading(door_sensor, house_mode))
print("check temperature sensor:", check_sensor_reading(temperature_sensor, house_mode))
print("check smoke sensor:", check_sensor_reading(smoke_sensor, house_mode))

# ======================================================
# STEP 4 - Functions
# ======================================================

# generate sensor readings
def generate_sensor_readings(sensor):
    if sensor["type"] == "motion":
        sensor["current_value"] = random.choice([True, False])
    elif sensor["type"] == "door":
        sensor["current_value"] = random.choice(["open", "closed"])
    elif sensor["type"] == "temperature":
        sensor["current_value"] = random.randint(20, 100)
    elif sensor["type"] == "smoke":
        sensor["current_value"] = random.choice([True, False])
       
    return sensor

# function to display alerts
def trigger_alert(alert):
    print("ALERT: ", alert["message"], "Timestamp: ", alert["timestamp"])

# logging function to records all events
def log_event(event):
    event_log.append(event)
    print("Event logged: ", event)
   
# function to process readings and determine if alerts are needed 
def process_readings(sensor, house_mode):
    alert = check_sensor_reading(sensor, house_mode)
    if alert != "Reading is normal":
        trigger_alert(alert)
        log_event(alert)
    
    return alert

# check if the above written functions are working as expected
sensors = initialize_sensor()
for sensor in sensors:
    sensor = generate_sensor_readings(sensor)
    process_readings(sensor, house_mode)
    
# ======================================================
# STEP 5 - Object-Oriented Version (Sensor Class)
# ======================================================

class Sensor_HomeGuard:
    def __init__(self, sensor_id, location, sensor_type):
        self.id = sensor_id
        self.location = location
        self.type = sensor_type
        self.current_value = None

    print("********* Inside class ***********")
    # this function simulates reading so no longer need to use generate_sensor_readings function, instead we can use this method to read the sensor value
    def read(self):
        if self.type == "motion":
            self.current_value = random.choice([True, False])
        elif self.type == "door":
            self.current_value = random.choice(["open", "closed"])
        elif self.type == "temperature":
            self.current_value = random.randint(20, 100)
        elif self.type == "smoke":
            self.current_value = random.choice([True, False])
        return self.current_value
    
    # this function replaces check_sensor_reading() and checks for abnormal sensor readings
    def isAbnormal(self, house_mode):
        if self.type == "motion":
            return self.current_value and house_mode == "away"
        elif self.type == "door":
            return self.current_value == "open" and house_mode == "away"
        elif self.type == "temperature":
            if self.current_value < 35:
                return True
            elif self.current_value > 95:
                return True
            elif house_mode == "home" and (self.current_value > 65 and self.current_value < 75):
                return True
        elif self.type == "smoke":
            return self.current_value
        
        return False
    
    # it resets the sensor value to default
    def reset(self):
        if self.type == "temperature":
            self.current_value = 70
        elif self.type == "door":
            self.current_value = "closed"
        elif self.type == "motion":
            self.current_value = False
        elif self.type == "smoke":
            self.current_value = False
            
# to test the class, need to create an instance of the class and call its methods
sensors = [
    Sensor_HomeGuard(1, "Living Room", "motion"),
    Sensor_HomeGuard(2, "Front Door", "door"),
    Sensor_HomeGuard(3, "Kitchen", "temperature"),
    Sensor_HomeGuard(4, "Hallway", "smoke")
]
    
house_mode = "away"

for sensor in sensors:
    sensor.read()

    print(sensor.location, sensor.current_value)

    if sensor.isAbnormal(house_mode):
        alert = create_alert(sensor.id, f"Abnormal reading from {sensor.location}")
        trigger_alert(alert)
        log_event(alert)
        
# ======================================================
# STEP 6 - Complete HomeGuard Simulation
# ======================================================
def format_time():
    return datetime.now().strftime("%H:%M:%S")

def display_reading(sensor):
    if sensor.type == "motion":
        status = "Activity detected" if sensor.current_value else "No activity"
        print(f"[READING] {sensor.location} Motion: {status}")

    elif sensor.type == "door":
        status = "OPENED" if sensor.current_value == "open" else "CLOSED"
        print(f"[READING] {sensor.location}: {status}")

    elif sensor.type == "temperature":
        if sensor.current_value > 95:
            condition = "Critical"
        elif sensor.current_value < 35:
            condition = "Warning"
        else:
            condition = "Normal"

        print(
            f"[READING] {sensor.location} Temperature: "
            f"{sensor.current_value}°F ({condition})"
        )

    elif sensor.type == "smoke":
        status = "SMOKE DETECTED" if sensor.current_value else "CLEAR"
        print(f"[READING] {sensor.location} Smoke: {status}")

def generate_alert_message(sensor, house_mode):
    if sensor.type == "motion" and house_mode == "away":
        return "SECURITY: Motion detected while in AWAY mode!"

    elif sensor.type == "door" and house_mode == "away":
        return "SECURITY: Front Door opened while in AWAY mode!"

    elif sensor.type == "temperature":
        if sensor.current_value > 95:
            return "SAFETY: High temperature detected!"
        elif sensor.current_value < 35:
            return "SAFETY: Freezing temperature risk!"

    elif sensor.type == "smoke" and sensor.current_value:
        return "SAFETY: Smoke detected!"

    return None

def run_homeguard():

    sensors = [
        Sensor_HomeGuard(1, "Living Room", "motion"),
        Sensor_HomeGuard(2, "Front Door", "door"),
        Sensor_HomeGuard(3, "Kitchen", "temperature"),
        Sensor_HomeGuard(4, "Bedroom", "smoke")
    ]

    house_mode = "away"

    print("=== HomeGuard Security System ===")
    print(f"Time: {format_time()}")
    print(f"Mode: {house_mode.upper()}\n")


    # Run multiple monitoring cycles
    for cycle in range(3):
        print(f"Time: {format_time()}")
        for sensor in sensors:
            sensor.read()
            display_reading(sensor)
            message = generate_alert_message(sensor, house_mode)

            if message:
                alert = create_alert(sensor.id,message)
                print(f"[ALERT!] " f"{alert['message']}")
                print(f"[LOG] [{format_time()}]" "Sending notification to homeowner...")
                log_event(alert)
        print()

run_homeguard()

# ======================================================
# STEP 7 - Testing HomeGuard System
# ======================================================
def run_test(system_mode):
    print("=== Test Mode ===", system_mode.upper())
    sensors = [
        Sensor_HomeGuard(1, "Living Room", "motion"),
        Sensor_HomeGuard(2, "Front Door", "door"),
        Sensor_HomeGuard(3, "Kitchen", "temperature"),
        Sensor_HomeGuard(4, "Bedroom", "smoke")
    ]
    for sensor in sensors:
        sensor.read()
        display_reading(sensor)
        message = generate_alert_message(sensor, system_mode)
        if message:
            alert = create_alert(sensor.id, message)
            print(f"[ALERT!] {alert['message']}")
            print(f"[LOG] [{format_time()}] Sending notification to homeowner...")
            log_event(alert)
        else:
            print(f"[STATUS] {sensor.location}: Normal")
    

print("Test completed.")

# ======================================================
# Run Required Test Scenarios
# ======================================================
# Security Test
run_test("away")
# Safety Test
run_test("away")
# Comfort Test
run_test("home")