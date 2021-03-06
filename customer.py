from database import *
from def_customers import *
from utility import clear_console, print_name, get_current_time, pause


def intro():
    username = os.getenv('loggedin')
    all_accounts = list_all_account(username)
    account = None
    flag = True
    if all_accounts:
        for i in all_accounts:
            print(i[1])
        while flag:
            choice = input("Which account would you like to login to? ")
            for i in all_accounts:
                if choice == i[1]:
                    account = choice
                    flag = False
                    break
                else:
                    print("Enter a valid account number")
        try:
            main_menu = ['1. Deposit', '2. Transact', '3. Transfer to another account',
                         '4. View your Balance/Transaction details', '5. Register a new account', '6. Logout',
                         'Press Ctrl + C to Force Exit']
            login_time = get_current_time()
            while True:
                clear_console()
                print_name()
                print(Figlet('small').renderText('Customer Menu'))
                print(colored('Hello ' + retrieve_customer(username)[0], 'blue'))
                print('Login time: ' + login_time + '\n')
                print("Account number:" + account)
                print('Choose an option: \n')
                for i in main_menu:
                    print('\t' + i)
                print()
                inp = input('Command: ')
                print()
                if inp == '1':
                    result = retrieve_customer(username)
                    if result[16] is None:
                        print("Please register your account at one of our branches.")
                        print(
                            198 * '-' + '\n' + '| {:^13s} | {:^10s} | {:^15s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} |'.format(
                                'Branch Code',
                                'Branch Name',
                                'Building',
                                'Street Name',
                                'Locality',
                                'Landmark',
                                'City',
                                'State',
                                'Country',
                                'Zip Code'))
                        all_branches = retrieve_all_branches()
                        if all_branches:
                            for i in all_branches:
                                print(
                                    198 * '-' + '\n' + '| {:^13s} | {:^10s} | {:^15s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} |'.format(
                                        str(i[0]), i[1],
                                        str(i[2]), i[3],
                                        i[4], i[5],
                                        i[6], i[7],
                                        i[8], str(i[9])))
                            print(198 * '-')
                            pause()
                        else:
                            print('No registered branches found!')
                            pause()
                        break
                    else:
                        print("Maximum amount: 10000")
                        while True:
                            deposit_amount = int(input("Deposit Amount: "))
                            if 0 < deposit_amount <= 10000:
                                break
                            else:
                                print("Enter a Valid Number")
                        print(deposit_amount)
                        deposit(deposit_amount, account, username)

                elif inp == '2':
                    result = retrieve_customer(username)
                    if result[16] is None:
                        print("Please register your account at one of our branches.")
                        print(
                            198 * '-' + '\n' + '| {:^13s} | {:^10s} | {:^15s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} |'.format(
                                'Branch Code',
                                'Branch Name',
                                'Building',
                                'Street Name',
                                'Locality',
                                'Landmark',
                                'City',
                                'State',
                                'Country',
                                'Zip Code'))
                        all_branches = retrieve_all_branches()
                        if all_branches:
                            for i in all_branches:
                                print(
                                    198 * '-' + '\n' + '| {:^13s} | {:^10s} | {:^15s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} |'.format(
                                        str(i[0]), i[1],
                                        str(i[2]), i[3],
                                        i[4], i[5],
                                        i[6], i[7],
                                        i[8], str(i[9])))
                            print(198 * '-')
                            pause()
                        else:
                            print('No registered branches found!')
                            pause()
                        break
                    else:
                        print("Maximum amount: 10000")
                        while True:
                            transact_amount = int(input("Transaction Amount: "))
                            if 0 < transact_amount <= 10000:
                                break
                            else:
                                print("Enter a Valid Number")
                        transact(transact_amount, account, username)

                elif inp == '3':
                    result = retrieve_customer(username)
                    if result[16] is None:
                        print("Please register your account at one of our branches.")
                        print(
                            198 * '-' + '\n' + '| {:^13s} | {:^10s} | {:^15s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} |'.format(
                                'Branch Code',
                                'Branch Name',
                                'Building',
                                'Street Name',
                                'Locality',
                                'Landmark',
                                'City',
                                'State',
                                'Country',
                                'Zip Code'))
                        all_branches = retrieve_all_branches()
                        if all_branches:
                            for i in all_branches:
                                print(
                                    198 * '-' + '\n' + '| {:^13s} | {:^10s} | {:^15s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} |'.format(
                                        str(i[0]), i[1],
                                        str(i[2]), i[3],
                                        i[4], i[5],
                                        i[6], i[7],
                                        i[8], str(i[9])))
                            print(198 * '-')
                            pause()
                        else:
                            print('No registered branches found!')
                            pause()
                        break
                    else:
                        acc = input("Target Account: ")
                        print("Maximum amount: 10000")
                        while True:
                            transfer_amount = int(input("Transfer Amount: "))
                            if 0 < transfer_amount <= 10000:
                                break
                            else:
                                print("Enter a Valid Number")
                        transfer(transfer_amount, username, (acc,), account)

                elif inp == '4':
                    sub_menu = ['1: View Transaction Details', '2. View Balance']
                    for i in sub_menu:
                        print('\t' + i)
                    print()
                    choice = input("Command: ")
                    if choice == '1':
                        result = retrieve_accounts_customer(account)
                        if len(result) != 0:
                            print(
                                165 * '-' + '\n' + '| {:^13s} | {:^15s} | {:^15s} | {:^20s} | {:^10s} | {:^10s} | {:^20s} | {:^20s} | {:^15s} |'.format(
                                    'Customer ID',
                                    'Account Number',
                                    'Branch ID',
                                    'Date',
                                    'Time',
                                    'Amount',
                                    'Opening Balance',
                                    'Closing Balance',
                                    'Remarks'))
                            for i in result:
                                if i[2] is not None:
                                    print(
                                        165 * '-' + '\n' + '| {:^13s} | {:^15s} | {:^15s} | {:^20s} | {:^10s} | {:^10s} | {:^20s} | {:^20s} | {:^15s} |'.format(
                                            str(i[0]), str(i[1]),
                                            str(i[4]), i[2],
                                            i[3], str(i[5]),
                                            str(i[6]), str(i[7]),
                                            str(i[8])))
                            print(165 * '-')
                        else:
                            print('No records found!')
                    elif choice == '2':
                        result = str(view_accbalance(account))
                        print("Your account balance is: $" + result)
                elif inp == '5':
                    register_account_1(username)
                elif inp == '6':
                    print('Goodbye!\nLogout time: ', get_current_time())
                    break
                else:
                    print("Invalid entry!")
                pause()
        except KeyboardInterrupt:
            print('\nForce exit encountered!')
    else:
        print("Please register at one of our branches")

    if __name__ == '__main__':
        print('Log in first\nAbort!')
