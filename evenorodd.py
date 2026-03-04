def check_number(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

if __name__ == "__main__":
    num = 7
    result = check_number(num)
    print(f"The number {num} is {result}")
