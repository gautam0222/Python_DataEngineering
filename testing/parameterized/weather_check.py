def weather_check(temp:float)->str:
    if temp < 0:
        return "It's freezing outside!"
    elif temp < 15:
        return "It's a bit chilly."
    elif temp < 25:
        return "The weather is pleasant."
    else:
        return "It's hot outside!"
    
if __name__ == "__main__":
    print(weather_check(10))
