import time
current_light = "red = stop"
traffic_lights = ["red = stop", "amber = wait", "green = go"]
while True:
    if current_light == "red = stop":
        print(traffic_lights[0])
        time.sleep(5)
        current_light = "amber = wait"
    elif current_light == "amber = wait":
        print(traffic_lights[1])
        time.sleep(2)
        current_light = "green = go"
    elif current_light == "green = go":
        print(traffic_lights[2])
        time.sleep(3)

        


