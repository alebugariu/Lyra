
from collections import defaultdict
from typing import Set

from lyra.abstract_domains.assumption.assumption_domain import InputMixin
from lyra.abstract_domains.basis import Basis
from lyra.abstract_domains.state import State
from lyra.abstract_domains.lattice import BottomMixin
from lyra.abstract_domains.numerical.interval_domain import Input, Literal

from lyra.core.expressions import VariableIdentifier, Expression, Subscription, SetDisplay, ListDisplay, \
    BinaryComparisonOperation, Keys, DictDisplay, Values, UnaryBooleanOperation, Slicing, TupleDisplay
from lyra.core.types import LyraType, ListLyraType
from lyra.core.utils import copy_docstring


class ContainerLattice(BottomMixin):
    """Container lattice.

    The default abstraction is ``(∅, ∅)`` (empty set of keys, empty set of values), representing that
    no keys and no values must be in the container.

    The bottom element of the lattice is ``⊥``.

    .. document private methods
    .. automethod:: ContainerLattice._less_equal
    .. automethod:: ContainerLattice._meet
    .. automethod:: ContainerLattice._join
    .. automethod:: ContainerLattice._widening
    """

    def __init__(self, keys: Set[LyraType] = None, values: Set[LyraType] = None):
        super().__init__()
        if keys is not None and values is not None:
            self._keys = keys
            self._values = values
        else:
            self.top()

    @property
    def keys(self):
        """Current set of keys that must be in the container.
        For lists, this represents the current set of indices.

        :return: the current set of keys
        """
        return self._keys

    @property
    def values(self):
        """Current set of values that must be in the container.

        :return: the current set of values
        """
        return self._values

    def __repr__(self):
        if self.is_bottom():
            return "⊥"
        if not self.keys:
            keys = "∅"
        else:
            keys = ", ".join("{}".format(key) for key in sorted(self.keys, key=lambda key: str(key)))
            keys = "{" + keys + "}"
        if not self.values:
            values = "∅"
        else:
            values = ", ".join("{}".format(value) for value in sorted(self.values, key=lambda key: str(value)))
            values = "{" + values + "}"
        return "(" + keys + ", " + values + ")"

    def top(self):
        """The top lattice element is the pair ``(∅, ∅)``."""
        return self._replace(type(self)(set(), set()))

    def is_top(self) -> bool:
        return not self.is_bottom() and not self.keys and not self.values

    def _less_equal(self, other: 'ContainerLattice') -> bool:
        return other.keys.issubset(self.keys) and other.values.issubset(self.values)

    def _join(self, other: 'ContainerLattice') -> 'ContainerLattice':
        keys = self.keys.intersection(other.keys)
        values = self.values.intersection(other.values)
        return self._replace(type(self)(keys, values))

    def _meet(self, other: 'ContainerLattice') -> 'ContainerLattice':
        keys = self.keys.union(other.keys)
        values = self.values.union(other.values)
        return self._replace(type(self)(keys, values))

    def _widening(self, other: 'ContainerLattice') -> 'ContainerLattice':
        return self.join(other)


class ContainerState(Basis, InputMixin):

    def __init__(self, variables: Set[VariableIdentifier], precursory: State = None):
        lattices = defaultdict(lambda: ContainerLattice)
        super().__init__(variables, lattices, precursory=precursory)
        InputMixin.__init__(self, precursory)

    @copy_docstring(Basis._assume_variable)
    def _assume_variable(self, condition: VariableIdentifier, neg: bool = False) -> 'ContainerState':
        return self

    @copy_docstring(Basis._assume_eq_comparison)
    def _assume_eq_comparison(self, condition: BinaryComparisonOperation, bwd: bool = False) -> 'ContainerState':
        return self

    @copy_docstring(Basis._assume_noteq_comparison)
    def _assume_noteq_comparison(self, condition: BinaryComparisonOperation, bwd: bool = False) -> 'ContainerState':
        return self

    @copy_docstring(Basis._assume_lt_comparison)
    def _assume_lt_comparison(self, condition: BinaryComparisonOperation, bwd: bool = False) -> 'ContainerState':
        return self

    @copy_docstring(Basis._assume_lte_comparison)
    def _assume_lte_comparison(self, condition: BinaryComparisonOperation, bwd: bool = False) -> 'ContainerState':
        return self

    @copy_docstring(Basis._assume_gt_comparison)
    def _assume_gt_comparison(self, condition: BinaryComparisonOperation, bwd: bool = False) -> 'ContainerState':
        return self

    @copy_docstring(Basis._assume_gte_comparison)
    def _assume_gte_comparison(self, condition: BinaryComparisonOperation, bwd: bool = False) -> 'ContainerState':
        return self

    @copy_docstring(Basis._assume_is_comparison)
    def _assume_is_comparison(self, condition: BinaryComparisonOperation, bwd: bool = False) -> 'ContainerState':
        return self

    @copy_docstring(Basis._assume_isnot_comparison)
    def _assume_isnot_comparison(self, condition: BinaryComparisonOperation, bwd: bool = False) -> 'ContainerState':
        return self

    @copy_docstring(Basis._assume_in_comparison)
    def _assume_in_comparison(self, condition: BinaryComparisonOperation, bwd: bool = False) -> 'ContainerState':
        return self

    @copy_docstring(Basis._assume_notin_comparison)
    def _assume_notin_comparison(self, condition: BinaryComparisonOperation, bwd: bool = False) -> 'ContainerState':
        return self

    @copy_docstring(Basis._assume)
    def _assume(self, condition: Expression, bwd: bool = False) -> 'ContainerState':
        if isinstance(condition, BinaryComparisonOperation):
            left = condition.left
            right = condition.right
            operator = condition.operator
            if isinstance(right, Values) or (isinstance(right, VariableIdentifier) and
                                             isinstance(right.typ, ListLyraType)):
                if isinstance(right, VariableIdentifier):  # the target is the list itself
                    target = right
                else:  # the target is the dictionary
                    target = right.target_dict
                current_state = self.store[target]
                if operator is BinaryComparisonOperation.Operator.NotIn:
                    self.store[target] = ContainerLattice(current_state.keys, current_state.values.discard(left))
                    return self
                if operator is BinaryComparisonOperation.Operator.In:
                    self.store[target] = ContainerLattice(current_state.keys, current_state.values.union({left}))
                    return self
            if isinstance(right, Keys):
                target = right.target_dict
                current_state = self.store[target]
                if operator is BinaryComparisonOperation.Operator.NotIn:
                    self.store[target] = ContainerLattice(current_state.keys.discard(left), current_state.values)
                    return self
                if operator is BinaryComparisonOperation.Operator.In:
                    self.store[target] = ContainerLattice(current_state.keys.union({left}), current_state.values)
                    return self
        elif isinstance(condition, UnaryBooleanOperation):  # not
            expression = condition.expression
            if isinstance(expression, BinaryComparisonOperation):
                reverse_operator = expression.operator.reverse_operator()
                left = expression.left
                right = expression.right
                rewritten_expression = BinaryComparisonOperation(expression.typ, left, reverse_operator, right)
                return self._assume(rewritten_expression, bwd)
        return self

    @copy_docstring(Basis._substitute)
    def _substitute(self, left: Expression, right: Expression) -> 'ContainerState':
        if isinstance(right, Subscription):
            target = right.target
            key = right.key
            while isinstance(target, (Subscription, Slicing)):
                target = target.target
            current_state = self.store[target]
            keys = set(self._evaluation.visit(key, self, dict()))
            self.store[target] = ContainerLattice(current_state.keys.union(keys), current_state.values)
        if isinstance(right, (SetDisplay, ListDisplay, DictDisplay)):
            # constant, so the dictionary/list becomes top
            keys = set()
            values = set()
            self.store[left] = ContainerLattice(keys, values)
        if isinstance(left, Subscription):
            # nothing changes, as we don't know if the key was there before or not
            return self
        self.substitute_keys_and_values(left, right)
        super()._substitute(left, right)
        return self

    def substitute_keys_and_values(self, left, right):
        for (variable, container_lattice) in self.store.items():
            keys = container_lattice.keys
            values = container_lattice.values
            key = next((key for key in keys if not isinstance(key, Literal) and key == left), None)
            current_state = self.store[variable]
            if key is not None:
                # substitute the key, if it is a constant, otherwise remove it
                # TODO: make this more precise
                other_keys = current_state.keys.difference({key})
                if isinstance(right, Literal):
                    self.store[variable] = ContainerLattice(other_keys.union({right}), current_state.values)
                else:
                    self.store[variable] = ContainerLattice(other_keys, current_state.values)
            value = next((value for value in values if not isinstance(value, Literal) and value == left), None)
            if value is not None:
                # substitute the value, if it is a constant, otherwise remove it
                # TODO: make this more precise
                other_values = current_state.values.difference({value})
                if isinstance(right, Literal):
                    self.store[variable] = ContainerLattice(current_state.keys, other_values.union({right}))
                else:
                    self.store[variable] = ContainerLattice(current_state.keys, other_values)

    @copy_docstring(Basis._output)
    def _output(self, output: Expression) -> 'ContainerState':
        if isinstance(output, Subscription):
            target = output.target
            key = output.key
            current_state = self.store[target]
            keys = set(self._evaluation.visit(key, self, dict()))
            self.store[target] = ContainerLattice(current_state.keys.union(keys), current_state.values)
        return self

    def _assign_any(self, left: Expression, right: Expression) -> 'ContainerState':
        raise RuntimeError("Unexpected assignment in a backward analysis!")

    @copy_docstring(State._assign_subscription)
    def _assign_subscription(self, left: Subscription, right: Expression) -> 'ContainerState':
        return self._assign_any(left, right)

    @copy_docstring(State._assign_slicing)
    def _assign_slicing(self, left: Slicing, right: Expression) -> 'ContainerState':
        return self._assign_any(left, right)

    @copy_docstring(State._substitute_subscription)
    def _substitute_subscription(self, left: Subscription, right: Expression) -> 'ContainerState':
        return self._substitute(left, right)

    @copy_docstring(State._substitute_slicing)
    def _substitute_slicing(self, left: Slicing, right: Expression) -> 'ContainerState':
        return self  # nothing changes

    @copy_docstring(InputMixin.replace)
    def replace(self, variable: VariableIdentifier, expression: Expression) -> 'ContainerState':
        # collect the new variables appearing in the replacing expression
        variables: Set[VariableIdentifier] = set()
        for identifier in expression.ids():
            if isinstance(identifier, VariableIdentifier):
                variables.add(identifier)
        variables: Set[VariableIdentifier] = variables.difference(set(self.variables))
        if variables:  # if there are new variables appearing in the replacing expression...
            # add the new variables to the current state
            for var in variables:
                self.variables.append(var)
                self.store[var] = self.lattices[type(var.typ)](**self.arguments[type(var.typ)])
            # replace the given variable with the given expression
            self._substitute(variable, expression)
        return self

    @copy_docstring(InputMixin.unify)
    def unify(self, other: 'ContainerState') -> 'ContainerState':
        # collect the variables that differ in the current and other state
        mine = sorted(set(self.variables).difference(set(other.variables)), key=lambda x: x.name)
        theirs = sorted(set(other.variables).difference(set(self.variables)), key=lambda x: x.name)
        # replace the variables in the current state that match those in the other state
        for my_var, their_var in zip(mine, theirs):
            # the replacement only occurs when the matching variables in the other state
            # depend on a program point that is smaller than the program point on which
            # the variables in the current state depend
            if their_var.name < my_var.name:
                self.variables[self.variables.index(my_var)] = their_var
                self.store[their_var] = self.store.pop(my_var)
        # add variables only present in the other state
        for var in theirs[len(mine):]:
            self.variables.append(var)
            self.store[var] = self.lattices[type(var.typ)](**self.arguments[type(var.typ)])
        return self

    class ExpressionEvaluation(Basis.ExpressionEvaluation):
        """Visitor that performs the evaluation of an expression in the container lattice."""

        def visit_ListDisplay(self, expr: ListDisplay, state=None, evaluation=None):
            if expr in evaluation:
                return evaluation  # nothing to be done
            evaluated = evaluation
            value = state.lattices[expr.typ](**state.arguments[expr.typ]).bottom()
            for item in expr.items:
                evaluated = self.visit(item, state, evaluated)
                value = value.join(evaluated[item])
            evaluation[expr] = value
            return evaluation

        def visit_TupleDisplay(self, expr: TupleDisplay, state=None, evaluation=None):
            if expr in evaluation:
                return evaluation  # nothing to be done
            evaluated = evaluation
            value = state.lattices[expr.typ](**state.arguments[expr.typ]).bottom()
            for item in expr.items:
                evaluated = self.visit(item, state, evaluated)
                value = value.join(evaluated[item])
            evaluation[expr] = value
            return evaluation

        def visit_SetDisplay(self, expr: SetDisplay, state=None, evaluation=None):
            if expr in evaluation:
                return evaluation  # nothing to be done
            evaluated = evaluation
            value = state.lattices[expr.typ](**state.arguments[expr.typ]).bottom()
            for item in expr.items:
                evaluated = self.visit(item, state, evaluated)
                value = value.join(evaluated[item])
            evaluation[expr] = value
            return evaluation

        def visit_DictDisplay(self, expr: DictDisplay, state=None, evaluation=None):
            if expr in evaluation:
                return evaluation  # nothing to be done
            evaluated = evaluation
            value = state.lattices[expr.typ](**state.arguments[expr.typ]).bottom()
            for key in expr.keys:
                evaluated = self.visit(key, state, evaluated)
                value = value.join(evaluated[key])
            for val in expr.values:
                evaluated = self.visit(val, state, evaluated)
                value = value.join(evaluated[val])
            evaluation[expr] = value
            return evaluation

        def visit_Subscription(self, expr: Subscription, state=None, evaluation=None):
            if expr in evaluation:
                return evaluation  # nothing to be done
            evaluated = self.visit(expr.target, state, evaluation)
            evaluation[expr] = evaluated[expr.target]
            return evaluation

        def visit_Slicing(self, expr: Slicing, state=None, evaluation=None):
            if expr in evaluation:
                return evaluation  # nothing to be done
            evaluated = self.visit(expr.target, state, evaluation)
            evaluation[expr] = evaluated[expr.target]
            return evaluation

    _evaluation = ExpressionEvaluation()  # static class member shared between all instances

    # expression refinement

    class ExpressionRefinement(Basis.ExpressionRefinement):

        @copy_docstring(Basis.ExpressionRefinement.visit_Input)
        def visit_Input(self, expr: Input, evaluation=None, value=None, state=None):
            state.record(value)
            return state  # nothing to be done

        @copy_docstring(Basis.ExpressionRefinement.visit_BinaryArithmeticOperation)
        def visit_BinaryArithmeticOperation(self, expr, evaluation=None, value=None, state=None):
            if isinstance(expr.left, Subscription):
                self.subscription_refinement(expr.left, state)
            if isinstance(expr.right, Subscription):
                self.subscription_refinement(expr.right, state)
            return state

        def subscription_refinement(self, expr, state):
            target = expr.target
            key = expr.key
            while isinstance(target, (Subscription, Slicing)):
                target = target.target
            current_state = state.store[target]
            keys = {key}
            state.store[target] = ContainerLattice(current_state.keys.union(keys), current_state.values)

        @copy_docstring(Basis.ExpressionRefinement.visit_ListDisplay)
        def visit_ListDisplay(self, expr: ListDisplay, evaluation=None, value=None, state=None):
            refined = evaluation[expr].meet(value)
            updated = state
            for item in expr.items:
                updated = self.visit(item, evaluation, refined, updated)
            return updated

        @copy_docstring(Basis.ExpressionRefinement.visit_TupleDisplay)
        def visit_TupleDisplay(self, expr: TupleDisplay, evaluation=None, value=None, state=None):
            refined = evaluation[expr].meet(value)
            updated = state
            for item in expr.items:
                updated = self.visit(item, evaluation, refined, updated)
            return updated

        @copy_docstring(Basis.ExpressionRefinement.visit_SetDisplay)
        def visit_SetDisplay(self, expr: SetDisplay, evaluation=None, value=None, state=None):
            refined = evaluation[expr].meet(value)
            updated = state
            for item in expr.items:
                updated = self.visit(item, evaluation, refined, updated)
            return updated

        @copy_docstring(Basis.ExpressionRefinement.visit_DictDisplay)
        def visit_DictDisplay(self, expr: DictDisplay, evaluation=None, value=None, state=None):
            refined = evaluation[expr].meet(value)
            updated = state
            for key in expr.keys:
                updated = self.visit(key, evaluation, refined, updated)
            for val in expr.values:
                updated = self.visit(val, evaluation, refined, updated)
            return updated

        @copy_docstring(Basis.ExpressionRefinement.visit_Subscription)
        def visit_Subscription(self, expr: Subscription, evaluation=None, value=None, state=None):
            self.subscription_refinement(expr, state)
            return state

        @copy_docstring(Basis.ExpressionRefinement.visit_Slicing)
        def visit_Slicing(self, expr: Slicing, evaluation=None, value=None, state=None):
            refined = evaluation[expr]  # weak update
            state.store[expr.target] = refined
            return state

    _refinement = ExpressionRefinement()  # static class member shared between instances

