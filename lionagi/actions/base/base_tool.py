from typing import Any
from pydantic import field_serializer

from lionagi.schema.base_schema import BaseNode

# To-Do: manual integration with tools


class BaseTool(BaseNode):
    """
    A class representing a tool with a function, content, parser, and schema.

    Attributes:
        func (Callable): The function associated with the tool.
        content (Any, optional): The content to be processed by the tool. Defaults to None.
        parser (Any, optional): The parser to be used with the tool. Defaults to None.
        schema_ (Dict): The schema definition for the tool.

    Examples:
        >>> tool = Tool(func=my_function, schema_={'type': 'string'})
        >>> serialized_func = tool.serialize_func()
        >>> print(serialized_func)
        'my_function'
    """

    func: Any
    manual: Any
    parser: Any = None
    schema_: dict

    @field_serializer('func')
    def serialize_func(self, func):
        """
        Serialize the function to its name.

        Args:
            func (Callable): The function to serialize.

        Returns:
            str: The name of the function.

        Examples:
            >>> def my_function():
            ...     pass
            >>> Tool.serialize_func(my_function)
            'my_function'
        """
        return func.__name__
    