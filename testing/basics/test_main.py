from .weather_check import weather_check

#Test cases for the weather_check function
def test_weather_check_hot():
    assert weather_check(35) == "It's hot outside!"
    assert weather_check(31) == "It's hot outside!"
    assert weather_check(30.1) == "It's hot outside!"
    assert weather_check(30) == "The weather is moderate."
    assert weather_check(29.9) == "The weather is moderate."
    assert weather_check(20.1) == "It's a bit chilly outside."
    assert weather_check(20) == "The weather is moderate."
    assert weather_check(19.9) == "It's a bit chilly outside."

def test_weather_check_cold():
    assert weather_check(5) == "It's cold outside!"
    assert weather_check(9.9) == "It's cold outside!"
    assert weather_check(10) == "The weather is moderate."
    assert weather_check(10.1) == "The weather is moderate."
    assert weather_check(15) == "It's a bit chilly outside."
    assert weather_check(19.9) == "It's a bit chilly outside."
    assert weather_check(20) == "The weather is moderate."

def test_weather_check_moderate():
    assert weather_check(20) == "The weather is moderate."
    assert weather_check(25) == "The weather is moderate."
    assert weather_check(30) == "The weather is moderate."
    assert weather_check(30.1) == "It's hot outside!"
    assert weather_check(19.9) == "It's a bit chilly outside."
    assert weather_check(10) == "The weather is moderate."
    assert weather_check(9.9) == "It's cold outside!"

def test_weather_check_edge_cases():
    assert weather_check(30) == "The weather is moderate."
    assert weather_check(10) == "The weather is moderate."
    assert weather_check(20) == "The weather is moderate."
    assert weather_check(0) == "It's cold outside!"
    assert weather_check(-5) == "It's cold outside!"
    assert weather_check(100) == "It's hot outside!"

if __name__ == "__main__":
    test_weather_check_hot()
    test_weather_check_cold()
    test_weather_check_moderate()
    test_weather_check_edge_cases()
    print("All tests passed!")
