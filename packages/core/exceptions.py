class SpeculativeDecodingException(Exception):
    pass

class WorkerAllocationException(SpeculativeDecodingException):
    pass

class ValidationException(SpeculativeDecodingException):
    pass

class AgentCoordinationException(SpeculativeDecodingException):
    pass

