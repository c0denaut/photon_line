import matplotlib.pyplot as plt
import random


class PhotonLine:

    def __init__(self, num_channels, n_photons):
        """
        Инициализация параметров класса
        """
        self.num_channels = num_channels
        self.n_photons = n_photons
        raw_chance = [random.random() for _ in range(num_channels)]
        sum_chances = sum(raw_chance)
        self.probabilities = [p / sum_chances for p in raw_chance]

        self.energies = [round(random.uniform(0.5, 2), 1) for _ in range(num_channels)]

        if sum(self.probabilities) == 0:
            raise ValueError(f"Ошибка нормировки! Сумма вероятностей = {sum(self.probabilities)}")

    def monte_karlo_photon(self):
        """
        Метод Монте-Карло для распределения фотонов по каналам

        Выходные данные:
        self.counts:- массив с количеством фотонов в каждом канале
        """
        self.counts = [0] * self.num_channels

        for _ in range(self.n_photons):

            G = random.uniform(0, 1)

            cumulative_prob = 0
            for i, prob in enumerate(self.probabilities):
                cumulative_prob += prob
                if G < cumulative_prob:
                    self.counts[i] += 1
                    break

    def histogram(self):
        """
        Функция, принимающая в себя массивы данных и выводящая гистограмму с распределением фотонов по уровням.
        """
        if not hasattr(self, 'counts'):
            print("Сначала выполните моделирование")
            return

        plt.figure(figsize=(15, 6))

        step = max(1, self.num_channels // 20)

        plt.bar(range(self.num_channels), self.counts)
        plt.xlabel('Номер канала')
        plt.ylabel('Количество фотонов')
        plt.title(f'Распределение фотонов по каналам (n={self.n_photons})')

        plt.xticks(range(0, self.num_channels, step),
                   [f'{i + 1}' for i in range(0, self.num_channels, step)],
                   rotation=45)

        plt.tight_layout()
        plt.show()

    # def histogram_distributed_true(self):
    #     """
    #     Гистограмма с максимумом в центре.
    #     """
    #     if not hasattr(self, 'counts'):
    #         print("Сначала выполните моделирование")
    #         return
    #
    #     # Создаем список кортежей (номер_канала, количество, вероятность, энергия)
    #     channels = list(enumerate(zip(self.counts, self.probabilities, self.energies)))
    #     # channels[i] = (index, (count, prob, energy))
    #
    #     # Сортируем по количеству фотонов (по убыванию)
    #     sorted_channels = sorted(channels, key=lambda x: x[1][0], reverse=True)
    #
    #     n = len(sorted_channels)
    #     hill_indices = [0] * n  # здесь будем хранить исходные номера каналов
    #     hill_counts = [0] * n
    #     hill_probs = [0] * n
    #     hill_energies = [0] * n
    #
    #     mid = n // 2
    #
    #     # Центральный элемент (самый большой)
    #     hill_indices[mid] = sorted_channels[0][0]
    #     hill_counts[mid] = sorted_channels[0][1][0]
    #     hill_probs[mid] = sorted_channels[0][1][1]
    #     hill_energies[mid] = sorted_channels[0][1][2]
    #
    #     # Распределяем остальные по бокам
    #     left = mid - 1
    #     right = mid + 1 if n % 2 == 1 else mid
    #
    #     for i in range(1, n):
    #         if i % 2 == 1 and left >= 0:  # нечетные - влево
    #             hill_indices[left] = sorted_channels[i][0]
    #             hill_counts[left] = sorted_channels[i][1][0]
    #             hill_probs[left] = sorted_channels[i][1][1]
    #             hill_energies[left] = sorted_channels[i][1][2]
    #             left -= 1
    #         elif right < n:  # четные - вправо
    #             hill_indices[right] = sorted_channels[i][0]
    #             hill_counts[right] = sorted_channels[i][1][0]
    #             hill_probs[right] = sorted_channels[i][1][1]
    #             hill_energies[right] = sorted_channels[i][1][2]
    #             right += 1
    #
    #     plt.figure(figsize=(14, 6))
    #
    #     # Построение гистограммы
    #     bars = plt.bar(range(n), hill_counts)
    #
    #     # Раскрашиваем в зависимости от количества (чем больше, тем темнее)
    #     max_count = max(hill_counts)
    #     for bar, count in zip(bars, hill_counts):
    #         intensity = count / max_count
    #         bar.set_color((0.2, 0.2, 1, intensity))  # синий с прозрачностью
    #
    #     plt.xlabel('Номер канала (исходный)')
    #     plt.ylabel('Количество фотонов')
    #     plt.title(f'Распределение фотонов по каналам (n={self.n_photons})')
    #
    #     # Подписи с исходными номерами каналов
    #     step = max(1, n // 20)
    #     visible_positions = range(0, n, step)
    #     plt.xticks(visible_positions,
    #                [str(hill_indices[i] + 1) for i in visible_positions],  # +1 для отображения с 1
    #                rotation=45)
    #
    #     # Добавляем информацию о топ-3 каналах
    #     top_indices = sorted(range(n), key=lambda i: hill_counts[i], reverse=True)[:3]
    #     info_text = "Топ каналы:\n"
    #     for idx in top_indices:
    #         info_text += f"Канал {hill_indices[idx] + 1}: {hill_counts[idx]} фотонов (P={hill_probs[idx]:.3f})\n"
    #
    #     plt.text(0.02, 0.98, info_text, transform=plt.gca().transAxes,
    #              bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.7),
    #              verticalalignment='top', fontsize=9)
    #
    #     plt.tight_layout()

    #     plt.show()
