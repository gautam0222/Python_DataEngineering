from main import weather

def test_weather_check():
    w=weather()
    assert w.weather_check(35) == "It's hot outside!"
    assert w.weather_check(31) == "It's hot outside!"
    assert w.weather_check(30.1) == "It's hot outside!"
    assert w.weather_check(30) == "The weather is moderate."
    assert w.weather_check(29.9) == "The weather is moderate."
    assert w.weather_check(20.1) == "It's a bit chilly outside."
    assert w.weather_check(20) == "The weather is moderate."
    assert w.weather_check(19.9) == "The weather is moderate."

def test_rain_check():
    w=weather()
    assert w.rain_check(0.8) == "It's likely to rain. Don't forget your umbrella!"
    assert w.rain_check(0.5) == "There's a chance of rain. You might want to carry an umbrella."
    assert w.rain_check(0.2) == "It's unlikely to rain today."
    assert w.rain_check(0.7) == "There's a chance of rain. You might want to carry an umbrella."
    assert w.rain_check(0.3) == "It's unlikely to rain today."