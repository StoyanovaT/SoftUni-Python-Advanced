from collections import deque

green_duration = int(input())
free_window = int(input())
cars_line = deque()
cars_counter = 0
crash = False
while True:
    current_green_status = green_duration
    current_free_status = free_window
    info = input()
    if info == "END":
        break

    if info == "green":
        while cars_line:
            if current_green_status >= 1:
                current_car = cars_line.popleft()
                if len(current_car) <= current_green_status:
                    cars_counter += 1
                    current_green_status -= len(current_car)

                else:
                    if len(current_car) <= current_green_status + free_window:
                        free_window = (current_green_status + free_window) - len(current_car)
                        current_green_status = 0
                        cars_counter += 1
                    else:
                        crashed_letter = current_car[current_green_status + free_window]
                        crash = True
                        print("A crash happened!")
                        print(f"{current_car} was hit at {crashed_letter}.")
                        break
            else:
                break
    if crash:
        break

    else:
        cars_line.append(info)

if not crash:
    print("Everyone is safe.")
    print(f"{cars_counter} total cars passed the crossroads.")

