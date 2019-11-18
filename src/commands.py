import roman
class Command():

    COMMAND_TYPES=[
        "ASSIGNMENT",
        "CREDITS",
        "HOW_MUCH",
        "HOW_MANY",
        "NO_IDEA"
    ]

    def __init__(self, symbol):
        self.symbol= symbol


    def process_command(self,cmd_type):

        if cmd_type == "ASSIGNMENT":
            pass

        elif cmd_type == "CREDITS":
            pass

        elif cmd_type == "HOW_MUCH":
            pass

        elif cmd_type == "HOW_MANY":
            pass

        else:
            pass
      
    def _process_assignment(self):
        pass
    def _process_credits(self):
        pass
    def _process_how_much(self):
        pass
    def _process_how_many(self):
        pass
    def _process_no_idea(self):
        pass
