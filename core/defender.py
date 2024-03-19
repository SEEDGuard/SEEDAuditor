import subprocess
from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Defender(ABC):

    @abstractmethod
    def load_input_file(self, data_dir: str, dest_dir: str):
        """Abstract method for dataset preprocessing."""
        raise NotImplementedError

    @abstractmethod
    def run_defense(self, data_dir: str, dest_dir: str):
        """Abstract method for dataset preprocessing."""
        raise NotImplementedError


class SpectralSignature(Defender):

    def load_input_file(self, data_dir: str, dest_dir: str):
        print("Loading the poisoned or un-poisoned dataset")

    def run_defense(self, data_dir: str, dest_dir: str):
        print("Running Spectral Signature")


class ActivationClustering(Defender):

    def load_input_file(self, data_dir: str, dest_dir: str):
        print("Loading the poisoned or un-poisoned dataset")

    def run_defense(self, data_dir: str, dest_dir: str):
        print("Running Activation Clustering")


