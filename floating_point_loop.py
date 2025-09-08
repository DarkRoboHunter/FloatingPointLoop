def main():
    values = []
    count = 0

    while count < 5:
        try:
            num = float(input(f"Enter floating-point value #{count + 1}: "))
            values.append(num)
            count += 1
        except ValueError:
            print("Invalid input. Please enter a number.")

    total = sum(values)
    average = total / len(values)
    maximum = max(values)
    minimum = min(values)
    interest = total * 0.20

    print("\n--- Results ---")
    print(f"Total: {total:.2f}")
    print(f"Average: {average:.2f}")
    print(f"Maximum: {maximum:.2f}")
    print(f"Minimum: {minimum:.2f}")
    print(f"Interest on total at 20%: {interest:.2f}")


if __name__ == "__main__":
    main()
