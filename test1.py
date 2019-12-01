from day1 import calculate_fuel, calculate_all_fuel


class TestFuel:
    def test_fuel(self):
        assert calculate_fuel(3) == 0
        assert calculate_fuel(12) == 2
        assert calculate_fuel(14) == 2
        assert calculate_fuel(1969) == 654
        assert calculate_fuel(100756) == 33583


    def test_fuel_all(self):
        assert calculate_all_fuel(14) == 2
        assert calculate_all_fuel(1969) == 966
        assert calculate_all_fuel(100756) == 50346
