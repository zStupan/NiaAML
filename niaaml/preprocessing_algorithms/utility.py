from niaaml.utilities import Factory
from niaaml import preprocessing_algorithms

__all__ = [
	'PreprocessingAlgorithmUtility'
]

class PreprocessingAlgorithmUtility(Factory):
	r"""Class with string mappings to preprocessing algorithms.

	Attributes:
		_entities (Dict[str, PreprocessingAlgorithm]): Mapping from strings to preprocessing algorithms.
	"""

	def _set_parameters(self, **kwargs):
		r"""Set the parameters/arguments of the factory.

		See Also:
			* :func:`niaaml.utilities.Factory._set_parameters`
		"""
		self._entities = {
			'Normalizer': preprocessing_algorithms.Normalizer,
			'StandardScaler': preprocessing_algorithms.StandardScaler
		}