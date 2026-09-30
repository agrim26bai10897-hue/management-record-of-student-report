from academic_engine import calculate_academic_performance

def run_tests():
    print("Running system validation tests...")
    
    # Test 1: Passing Marks
    sample_marks_pass = {"Math": 80, "Physics": 70, "CS": 90}
    total, pct, result = calculate_academic_performance(sample_marks_pass)
    assert total == 240, "Test 1 Failed: Total incorrect"
    assert pct == 80.0, "Test 1 Failed: Percentage incorrect"
    assert result == "Pass", "Test 1 Failed: Result should be Pass"
    print("Test 1 (Pass Calculation): PASSED")

    # Test 2: Failing Marks
    sample_marks_fail = {"Math": 30, "Physics": 70, "CS": 80}
    total, pct, result = calculate_academic_performance(sample_marks_fail)
    assert result == "Fail", "Test 2 Failed: Result should be Fail"
    print("Test 2 (Fail Calculation): PASSED")
    
    print("\nAll validation tests completed successfully!")

if __name__ == "__main__":
    run_tests()