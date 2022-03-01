def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs1()
    print("All tests passed!")

aaa = '12345'
print(globals())

print("Imported from:", __name__)

#python test_abs_project.py
#pytest --tb=line test_abs_project.py
#pytest --tb=line -v test_abs_project.py
#pytest -v --tb=short test_abs_project.py
#pytest --tb=no test_abs_project.py
#pytest test_abs_project.py
#pytest test_abs_project.py
#pytest --collect-only test_abs_project.py