
class Command():

    COMMAND_TYPES=[
        "ASSIGNMENT",
        "CREDITS",
        "HOW_MUCH",
        "HOW_MANY",
        "NO_IDEA"
    ]

    def __init__(self):
        pass


    def process_command(self, cmd_type):

        if cmd_type == "ASSIGNMENT":
            self._process_assignment()

        elif cmd_type == "CREDITS":
            self._process_credits()

        elif cmd_type == "HOW_MUCH":
            self._process_how_much()

        elif cmd_type == "HOW_MANY":
            self._process_how_many()

        else:
            self._process_no_idea()
      
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
