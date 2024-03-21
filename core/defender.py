import subprocess
from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
from core.defense.spectral_signature.spectral_signature import init_spectral_signature
from core.defense.activation_clustering.activation_clustering import init_activation_clustering

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
        init_spectral_signature(input_dir=data_dir, output_dir=dest_dir)


class ActivationClustering(Defender):

    def load_input_file(self, data_dir: str, dataset):  # dataset should support txt, jsonl and pd.Dataframe
        print("Loading the poisoned or un-poisoned dataset")

    def run_defense(self, data_dir: str, dest_dir: str):
        init_activation_clustering(input_dir=data_dir, output_dir=dest_dir)


