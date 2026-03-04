from Photon41k import PhotonLine


def main():
    num_channels = int(input("Введите количество каналов: "))
    n = int(input("Введите количество фотонов: "))
    photon_line = PhotonLine(num_channels, n)

    for i in range(num_channels):
        print(f"Канал {i + 1}: E={photon_line.energies[i]:.1f}, P={photon_line.probabilities[i]:.3f}")

    photon_line.monte_karlo_photon()

    for i in range(num_channels):
        print(f"Канал {i + 1}: {photon_line.counts[i]} фотонов")

    photon_line.histogram()
    # photon_line.histogram_distributed_true()


if __name__ == "__main__":
    main()