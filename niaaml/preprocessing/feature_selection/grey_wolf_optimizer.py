import sys
from NiaPy.algorithms.basic import GreyWolfOptimizer
from NiaPy.task import StoppingTask
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from niaaml.preprocessing.feature_selection.feature_selection_algorithm import FeatureSelectionAlgorithm
from niaaml.utilities import ParameterDefinition, MinMax
from niaaml.preprocessing.feature_selection.utility import _FeatureSelectionThresholdBenchmark

__all__ = [
    'GWOFeatureSelection'
]

class GWOFeatureSelection(FeatureSelectionAlgorithm):
    r"""Implementation of feature selection using GWO algorithm.

    Date:
        2020
    
    Author:
        Luka Pečnik  

    License:
        MIT

    See Also:
        * :class:`niaaml.preprocessing.feature_selection.feature_selection_algorithm.FeatureSelectionAlgorithm`
    """
    Name = 'Grey Wolf Optimizer'

    def __init__(self, **kwargs):
        r"""Initialize GWO feature selection algorithm.
        """
        self.__gwo = GreyWolfOptimizer(NP=10)

    def __final_output(self, sol):
        r"""Calculate final array of features.

        Arguments:
            sol (numpy.ndarray[float]): Individual of population/ possible solution.

        Returns:
            numpy.ndarray[bool]: Mask of selected features.
        """
        selected = numpy.ones(sol.shape[0] - 1, dtype=bool)
        threshold = sol[sol.shape[0] - 1]
        for i in range(sol.shape[0] - 1):
            if sol[i] < threshold:
                selected[i] = False
        return selected
    
    def select_features(self, x, y, **kwargs):
        r"""Perform the feature selection process.

        Arguments:
            x (numpy.ndarray[float]): Array of original features.
            y (Iterable[any]) Expected classifier results.

        Returns:
            numpy.ndarray[bool]: Mask of selected features.
        """
        num_features = x.shape[1]
        benchmark = _FeatureSelectionThresholdBenchmark(x, y)
        task = StoppingTask(D=num_features+1, nFES=1000, benchmark=benchmark)
        best = self.__gwo.run(task)
        return self.__final_output(benchmark.get_best_solution())
    
    def to_string(self):
        r"""User friendly representation of the object.

        Returns:
            str: User friendly representation of the object.
        """
        return FeatureSelectionAlgorithm.to_string(self).format(name=self.Name, args=self._parameters_to_string(self.__gwo.getParameters()))
