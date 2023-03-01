class EmailValidationError(ValueError):
    def __init__(self, address):
        super().__init__(f"failed email validation - <{address}>")
