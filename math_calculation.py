import math

def area_of_rectangle():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width
    print(f"Area of Rectangle = {area:.2f}")

def circumference_of_circle():
    r = float(input("Enter radius (r): "))
    circumference = 2 * math.pi * r
    print(f"Circumference = {circumference:.2f}")

def simple_interest():
    principal = float(input("Enter Principal: "))
    rate = float(input("Enter Rate of interest (in %): "))
    time = float(input("Enter Time (in years): "))
    si = (principal * rate * time) / 100
    print(f"Simple Interest = {si:.2f}")

def speed_of_object():
    distance = float(input("Enter Distance: "))
    time = float(input("Enter Time: "))
    if time == 0:
        print("Error: Time cannot be zero.")
    else:
        speed = distance / time
        print(f"Speed = {speed:.2f}")

def bmi_calculator():
    weight = float(input("Enter Weight (in kg): "))
    height = float(input("Enter Height (in meters): "))
    if height == 0:
        print("Error: Height cannot be zero.")
    else:
        bmi = weight / (height ** 2)
        print(f"BMI = {bmi:.2f}")

def force_newton():
    m = float(input("Enter mass (in kg): "))
    a = float(input("Enter acceleration (in m/s²): "))
    f = m * a
    print(f"Force (F) = {f:.2f} N")

def compound_interest():
    p = float(input("Enter principal amount (P): "))
    r = float(input("Enter annual interest rate (as a decimal): "))
    n = int(input("Enter number of times interest is compounded per year (n): "))
    t = float(input("Enter time in years (t): "))
    a = p * ((1 + r/n) ** (n * t))
    print(f"Total Amount (A) = {a:.2f}")

def perimeter_of_triangle():
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))
    perimeter = a + b + c
    print(f"Perimeter = {perimeter:.2f}")

def volume_of_sphere():
    r = float(input("Enter radius (r): "))
    volume = (4/3) * math.pi * (r ** 3)
    print(f"Volume of Sphere = {volume:.2f}")

def kinetic_energy():
    m = float(input("Enter mass (in kg): "))
    v = float(input("Enter velocity (in m/s): "))
    ke = 0.5 * m * (v ** 2)
    print(f"Kinetic Energy (KE) = {ke:.2f} J")

def quadratic_roots():
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    if a == 0:
        print("Error: 'a' cannot be zero in a quadratic equation.")
        return
    discriminant = (b ** 2) - (4 * a * c)
    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"Roots are real: Root 1 = {root1:.2f}, Root 2 = {root2:.2f}")
    else:
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-discriminant) / (2 * a)
        print(f"Roots are complex: {real_part:.2f} + {imag_part:.2f}i and {real_part:.2f} - {imag_part:.2f}i")

def temp_conversion():
    c = float(input("Enter temperature in Celsius: "))
    f = (9/5) * c + 32
    print(f"Temperature in Fahrenheit = {f:.2f}°F")

def gravitational_force():
    g = 6.6743e-11
    m1 = float(input("Enter mass of object 1 (m1 in kg): "))
    m2 = float(input("Enter mass of object 2 (m2 in kg): "))
    r = float(input("Enter distance between centers (r in meters): "))
    if r == 0:
        print("Error: Distance cannot be zero.")
    else:
        force = g * (m1 * m2) / (r ** 2)
        print(f"Gravitational Force = {force:.2e} N")

def volume_of_cylinder():
    r = float(input("Enter radius (r): "))
    h = float(input("Enter height (h): "))
    volume = math.pi * (r ** 2) * h
    print(f"Volume of Cylinder = {volume:.2f}")

def pressure_calculator():
    f = float(input("Enter Force (F): "))
    a = float(input("Enter Area (A): "))
    if a == 0:
        print("Error: Area cannot be zero.")
    else:
        p = f / a
        print(f"Pressure (P) = {p:.2f} Pa")

def electric_power():
    v = float(input("Enter Voltage (V): "))
    i = float(input("Enter Current (I): "))
    p = v * i
    print(f"Electric Power (P) = {p:.2f} W")

def perimeter_of_circle():
    r = float(input("Enter radius (r): "))
    p = 2 * math.pi * r
    print(f"Perimeter (Circumference) = {p:.2f}")

def future_value():
    pv = float(input("Enter present value (PV): "))
    r = float(input("Enter annual interest rate (as a decimal): "))
    t = float(input("Enter time in years (t): "))
    fv = pv * ((1 + r) ** t)
    print(f"Future Value (FV) = {fv:.2f}")

def work_done():
    f = float(input("Enter force (f): "))
    d = float(input("Enter distance (d): "))
    theta = float(input("Enter angle theta (in degrees): "))
    work = f * d * math.cos(math.radians(theta))
    print(f"Work Done (W) = {work:.2f} J")

def heat_transfer():
    m = float(input("Enter mass (m): "))
    c = float(input("Enter specific heat capacity (c): "))
    delta_t = float(input("Enter temperature change (ΔT): "))
    q = m * c * delta_t
    print(f"Heat Transferred (Q) = {q:.2f} J")

def main_menu():
    while True:
        print("\n" + "="*40)
        print("            MAIN PROGRAM MENU            ")
        print("="*40)
        print("1. Area of a Rectangle")
        print("2. Circumference of a Circle")
        print("3. Simple Interest")
        print("4. Speed of an Object")
        print("5. BMI Calculator")
        print("6. Force Using Newton's Second Law")
        print("7. Compound Interest")
        print("8. Perimeter of a Triangle")
        print("9. Volume of a Sphere")
        print("10. Kinetic Energy")
        print("11. Quadratic Equation Roots")
        print("12. Temperature Conversion")
        print("13. Gravitational Force")
        print("14. Volume of a Cylinder")
        print("15. Pressure")
        print("16. Electric Power")
        print("17. Perimeter of a Circle")
        print("18. Future Value in Savings")
        print("19. Work Done by a Force")
        print("20. Heat Transfer")
        print("0. Exit Program")
        print("="*40)
        
        choice = input("Enter your choice (0-20): ").strip()
        print("-" * 40)
        
        if choice == '1': area_of_rectangle()
        elif choice == '2': circumference_of_circle()
        elif choice == '3': simple_interest()
        elif choice == '4': speed_of_object()
        elif choice == '5': bmi_calculator()
        elif choice == '6': force_newton()
        elif choice == '7': compound_interest()
        elif choice == '8': perimeter_of_triangle()
        elif choice == '9': volume_of_sphere()
        elif choice == '10': kinetic_energy()
        elif choice == '11': quadratic_roots()
        elif choice == '12': temp_conversion()
        elif choice == '13': gravitational_force()
        elif choice == '14': volume_of_cylinder()
        elif choice == '15': pressure_calculator()
        elif choice == '16': electric_power()
        elif choice == '17': perimeter_of_circle()
        elif choice == '18': future_value()
        elif choice == '19': work_done()
        elif choice == '20': heat_transfer()
        elif choice == '0':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid input! Please enter a number between 0 and 20.")

if __name__ == "__main__":
    main_menu()
