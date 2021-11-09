# model_view_controller.py
class View:
    # def __init__(self, message):
    #     self.message = message

    def ask_for_values_to_add(self, entity):
        value = input(f"Enter new {entity}'s values: ")
        return value

    def added_message(self, entity):
        print(f"+++ {entity} is added +++")

    def ask_for_values_to_update(self, entity):
        value = input(f"Enter updated {entity}'s values: ")
        return value

    def updated_message(self, entity):
        print(f"*** {entity} is updated ***")

    def ask_for_values_to_delete(self, entity):
        value = input(f"Enter {entity}'s id: ")
        return value

    def deleted_message(self, entity):
        print(f"--- {entity} is deleted ---")

    def ask_for_values_to_generate(self, entity):
        value = input(f"Enter number of random {entity}s")
        return value

    def generated_message(self, entity):
        print(f"@@@ {entity}s are generated")

    def ask_for_values_to_search(self, message):
        value = input(f"Enter {message}: ")
        return value

    def before_and_after_search(self, message):
        print(f"_____search {message}_____")

    def incorrect_input_message(self, entity):
        print(f"!!! incorrect values for {entity} were entered, try again !!!")

