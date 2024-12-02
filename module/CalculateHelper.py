def calculate(a, b):
    try:
        print("Process calculating...")
        result = a * b
        print(result)
    except Exception as e:
        print(f"Catch exception: {e}")
        raise TypeError("New error")
    else:
        print("No exception")
    finally:
        print("Finally")
