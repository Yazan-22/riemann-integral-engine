class IntegrationError(Exception):
    """Base class for integration-related errors."""
    pass


class UnknownMethodError(IntegrationError):
    """Raised when the requested integration method is not supported."""
    pass


class InvalidStepError(IntegrationError):
    """Raised when the number of subintervals (n) is invalid."""
    pass


class InvalidEngineInputError(IntegrationError):
    """Raised when engine input (func, a, b) is invalid."""
    pass
