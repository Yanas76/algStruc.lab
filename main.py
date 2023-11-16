import input_managers

print("Options:")
print("1 - Eiler function")
print("2 - Moebius function")
print("3 - Smallest common multiple")
print("4 - Chinese remainder theorem")
print("5 - Legendre symbol")
print("6 - Jacobi symbol")
print("7 - Pollards rho factorisation")
print("8 - Baby step-giant step")
print("9 - Chippola square root")
print("10 - Miller-Rabin primality test:")
print("11 - RSA crypto-system")
print("12 - Ecliptic curves crypto-system")
print("0 - Exit")

while True:

    print("What do you want to do? Enter the corresponding option number or '0' to exit.")
    inp = input()

    if inp == '1':
        input_managers.eiler_function_input()
    elif inp == '2':
        input_managers.moebius_function_input()
    elif inp == '3':
        input_managers.smallest_common_multiple_input()
    elif inp == '4':
        input_managers.chinese_remainder_theorem_input()
    elif inp == '5':
        input_managers.legendre_symbol_input()
    elif inp == '6':
        input_managers.jacobi_symbol_input()
    elif inp == '7':
        input_managers.pollards_rho_factorisation_input()
    elif inp == '8':
        input_managers.baby_step_giant_step_input()
    elif inp == '9':
        input_managers.chipolla_algorithm_input()
    elif inp == '10':
        input_managers.miller_rabin_input()
    elif inp == '11':
        input_managers.rsa_cryptosystem_input()
    elif inp == '12':
        input_managers.ecliptic_curves_input()
    elif inp == '0':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid option. Please select a valid option or '0' to exit.")



