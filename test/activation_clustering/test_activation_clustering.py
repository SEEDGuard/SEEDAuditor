from core.defender import ActivationClustering


def main():
    input_dir = "test/spectral_signature/data/input/rb_function.txt"  # DRIVE LINK ADDED IN THE README
    output_dir = "test/spectral_signature/data/output"  # OUTPUT CONTENTS DRIVE LINK ADDED IN README

    ac: ActivationClustering = ActivationClustering()
    # ac.load_input_file(data_dir=input_dir, dataset="")
    ac.run_defense(data_dir=input_dir, dest_dir=output_dir)


if __name__ == "__main__":
    main()
