from etl.execution.contexts.batch import BatchExecutionContext


class Concurreny:
    """
    Base class for execution strategies.

    """
    pass

    # BatchExecutionContextType = BatchExecutionContext
    #
    # def __init__(self, BatchExecutionContextType=None):
    #     self.GraphExecutionContextType = BatchExecutionContextType or self.BatchExecutionContextType
    #
    # def create_graph_execution_context(self, graph, *args, BatchExecutionContext=None, **kwargs):
    #     return (BatchExecutionContext or self.GraphExecutionContextType)(graph, *args, **kwargs)
    #
    # def execute(self, graph, *args, **kwargs):
    #     raise NotImplementedError
