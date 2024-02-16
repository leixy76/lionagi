import operator
import ast

class BaseEvaluator:
    """
    Safely evaluates expressions using AST parsing to prevent unsafe operations.
    """
    def __init__(self):
        self.allowed_operators = {
            ast.Eq: operator.eq, ast.NotEq: operator.ne,
            ast.Lt: operator.lt, ast.LtE: operator.le,
            ast.Gt: operator.gt, ast.GtE: operator.ge,
            # Add other operators as necessary
        }

    def evaluate(self, expression, context):
        """
        Evaluate a condition expression within a given context.
        """
        try:
            tree = ast.parse(expression, mode='eval')
            return self._evaluate_node(tree.body, context)
        except Exception as e:
            raise ValueError(f"Failed to evaluate expression: {expression}. Error: {e}")

    def _evaluate_node(self, node, context):
        if isinstance(node, ast.Compare):
            left = self._evaluate_node(node.left, context)
            for operation, comparator in zip(node.ops, node.comparators):
                op_func = self.allowed_operators[type(operation)]
                right = self._evaluate_node(comparator, context)
                if not op_func(left, right):
                    return False
            return True
        elif isinstance(node, ast.Name):
            return context.get(node.id)
        elif isinstance(node, ast.Num):
            return node.n
        # Implement additional AST node types as needed
        else:
            raise ValueError("Unsupported operation in condition.")