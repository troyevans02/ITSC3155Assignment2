import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = #####
cashier_instance = ######




def main():
    is_on = True

    while is_on:
        choice = input("What size sandwich do you want? (small/medium/large): ").lower()

        if choice in recipes:
            sandwich = recipes[choice]
            if sandwich_maker_instance.check_resources(sandwich['ingredients']):
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, sandwich['cost']):
                    sandwich_maker_instance.make_sandwich(choice, sandwich['ingredients'])
        elif choice == 'off':
            is_on = False
            print("Powering off machine")
        elif choice == 'report':
            print(resources)
        else:
            print("Invalid option. Choose again")

if __name__=="__main__":
    main()
