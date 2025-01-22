class MatrixError(Exception):

    def __init__(self, message="A matrix definition error occurred", details=None):
        self.message = message
        self.details = details
        super().__init__(self.message)

    def __str__(self):
        if self.details:
            return f"{self.message}\n{self.details}"
        return self.message

class MatrixDefinitionError(MatrixError):

    def __init__(self, message="A matrix definition error occurred", details=None):
        super().__init__(message, details)

    
class MatrixOperationError(MatrixError):
    def __init__(self, message="A matrix operation error occurred", details=None):
        super().__init__(message, details)
