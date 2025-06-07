from lerobot.common.robot_devices.motors.feetech import FeetechMotorsBus, FeetechMotorsBusConfig


def main():
    config = FeetechMotorsBusConfig(
    port="/dev/ttyACM1",
    motors={
        "shoulder_pan": [5, "sts3215"],
        "shoulder_lift": [6, "sts3215"],
        "elbow_flex": [4, "sts3215"],
        "wrist_flex": [3, "sts3215"],
        "wrist_roll": [2, "sts3215"],
        "gripper": [1, "sts3215"],
    },
)
    config_follower = FeetechMotorsBusConfig(
    port="/dev/ttyACM0",
    motors={
        "shoulder_pan": [1, "sts3215"],
        "shoulder_lift": [2, "sts3215"],
        "elbow_flex": [3, "sts3215"],
        "wrist_flex": [4, "sts3215"],
        "wrist_roll": [6, "sts3215"],
        "gripper": [5, "sts3215"],
    },
)
    
    motors_bus_master = FeetechMotorsBus(config)
    motors_bus_master.connect()
    motors_bus_follower = FeetechMotorsBus(config_follower)
    motors_bus_follower.connect()

    while (keypress := input("Press Enter to read positions or type 'exit' to quit: ")) != "exit":
        
        position = motors_bus_master.read("Present_Position")
        position_follower = motors_bus_follower.read("Present_Position")
        print("Current positions master:", position)
        print("Current positions follower:", position_follower)

    motors_bus_master.disconnect()
    motors_bus_follower.disconnect()
    return motors_bus_master

if main() == "__main__":
    main()
    pass
