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
            for i in range(len(donors)):
                if(name == donors[i][0]):
                    print("How much did they donate?")
                    amount = float(input('-> '))
                    donors[i][1].append(amount)
                    print(note(name, amount))
            else:
                donors.append([name, []])
                print("How much did they donate?")
                amount = float(input('-> '))
                donors[-1][1].append(amount)
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
    complete_donation_info = list(donors)

    # Average out the donations
    for contributer in range(len(donors)):
        total_donated = 0
        average_donation = 0
        number_donations = 0
        for donation in range(len(donors[contributer][1])):
            total_donated = total_donated + donors[contributer][1][donation]
            number_donations = number_donations + 1
        # Calculate average
        average_donation = float(total_donated / number_donations)
        complete_donation_info[contributer].append(total_donated)
        complete_donation_info[contributer].append(average_donation)
        complete_donation_info[contributer].append(number_donations)
    # the total donated should be the third item of each sub list
    complete_donation_info.sort(key=itemgetter(2), reverse=True)
    # Convert to tuples for easy printing
    [(x,) for x in complete_donation_info]
    print('Donor Name \t\tTotal Donated \t\tNumber of Donations \t\t'
          'Average donation')
    for i in range(len(complete_donation_info)):
        print('{0} \t\t{2} \t\t{4} \t\t{3}'.format(*complete_donation_info[i]))


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
