# To sort lists by one item in the list
from operator import itemgetter

donors = {'Phil Harmonic': [70.02, 33.1, 12.00],
          'Dick Tator': [13.23, 12.12, 10.56],
          'May Flower': [66.6, 99.9], 'Perd Haply': [46, 12, 1],
          'Count von Fizzbuzz': [1000, 120, .01]}


# Thank you function
def ty():
    """Generates thank you notes and adds donors to the donor list"""
    while True:
        # Intro message
        print("If you want to know who donated, type 'list'. If you want to",
              " quit, type 'quit' Otherwise, who",
              " are we thanking today?")
        response = input('-> ')
        if(response == 'quit' or response == 'q'):
            break
        elif(response == 'list' or response == 'l'):
            for key in donors.keys():
                print(donors[key])
        elif(response == ''):
            print('Instead of nothing, try typing something.')
        else:
            name = response
            if(name in donors):
                print("How much did they donate?")
                amount = float(input('-> '))
                donors[name].append(amount)
                print(note(name, amount))
            else:
                donors[name] = []
                print("How much did they donate?")
                amount = float(input('-> '))
                donors[name].append(amount)
                print(note(name, amount))


def note(name, amount):
    """returns thank you note"""
    print("Thank you {0} for your donation of ${1}.".format(name, str(amount)),
          " These funds will in",
          " no way be misappropriated in an extravigant manner. ",
          "We only have an overhead of about 95%.")


# Report generator
def report():
    """Creates a report of all donors and the amount of their donations"""
    total_donated = 0
    average_donation = 0
    number_donations = 0

    for key in donors:
        total_donated = 0
        average_donation = 0
        number_donations = 0
        for donation in range(len(donors[key])):
            total_donated = total_donated + donors[key][donation]
            number_donations = number_donations + 1
        # Calculate average
        average_donation = float(total_donated / number_donations)
        donors[key].append(total_donated)
        donors[key].append(average_donation)
        donors[key].append(number_donations)
    
    print('Donor Name \t\tTotal Donated \t\tNumber of Donations \t\t'
          'Average donation')
    for key in donors:
        print('{key} \t\t{1} \t\t{3} \t\t{2}'.format(*donors[key]))


# Main program loop
while True:
    # Intro message
    print('Welcome to the mailroom, beautiful! Would you like to do?')
    print('-Write a thank you (ty)')
    print('-Veiw a report (report)')
    print('-Quit the program (quit)')

    # User input stored
    answer = input("-> ")

    if(answer == 'quit' or answer == 'q'):
        break
    elif(answer == 'thank you' or answer == 'ty'):
        ty()
    elif(answer == 'report' or answer == 'r'):
        report()
    else:
        print('That was not an option, clown!')
