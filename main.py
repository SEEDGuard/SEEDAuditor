import argparse

from core.defender import SpectralSignature, ActivationClustering, AFRAIDoor


def get_defender(defense_identifier):
    # We need to validate here if the input defender name exists or not
    if defense_identifier.lower() == 'spectralsignature':
        print("Returning Spectral Signature Instance")
        return SpectralSignature()
    elif defense_identifier.lower() == 'activationclustering':
        print("Returning Activation Clustering Instance")
        return ActivationClustering()
        elif defense_identifier.lower() == 'afraidoor':
        print("Returning AFRAIDoor Instance")
        return AFRAIDoor()
    else:
        raise ValueError(f"Invalid Defense name: {defense_identifier}")


def main():
    parser = argparse.ArgumentParser(description='Provide defense to a dataset with a specified methods.')
    parser.add_argument('--input_dir', type=str, default='',
                        help='Path to the input dataset')
    parser.add_argument('--output_dir', type=str, default='',
                        help='Path to the output directory')
    parser.add_argument('--method', type=str, default='spectralsignature',
                        help='Name of the method to use (e.g., "spectralsignature")')

    args = parser.parse_args()

    defender = get_defender(defense_identifier=args.method)

    defender.run_defense(data_dir=args.input_dir, dest_dir=args.output_dir)


if __name__ == "__main__":
    main()
