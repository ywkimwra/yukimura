def main():
    a = convert(time)
    if 7 <= a <= 8:
        print("breakfast time")
    elif 12 <= a <= 13:
        print("lunch time")
    elif 18 <= a <= 19:
        print("dinner time")
def convert(time):
    hour, minute = time.split(":")
    hour = float(hour)
    minute = float(minute)
    time_converted = hour + (minute / 60)
    return time_converted

if __name__ == "__main__":
    time = input("What time is it? ")
    main()

