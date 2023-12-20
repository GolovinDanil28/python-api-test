class TestExample:
    def test_check_math(self):
        a = 5
        b = 6
        expected_sum = 11
        assert a + b == 11, f"Sum of variables a and b is not equel to {expected_sum}"

    def test_check_math2(self):
        a = 51
        b = 6
        expected_sum = 14

        assert a + b == expected_sum, f"Sum of variables a and b is not equel to {expected_sum}"