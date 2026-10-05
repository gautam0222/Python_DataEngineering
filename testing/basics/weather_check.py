def weather_check(temp:float):
    if temp > 30:
        return "It's hot outside!"
    elif temp < 10:
        return "It's cold outside!"
    elif temp < 20:
        return "It's a bit chilly outside."
    else:
        return "The weather is moderate."

if __name__ == "__main__":
    print(weather_check(25))
    
