import time


class FreqMeasurer:
    def __init__(self, samples=5):
        self.samples_dict = {}
        self.samples = samples

    def _collect_data(self):
        samples_collected = 0
        while True:
            _ = input('')
            print('.')
            self.samples_dict.update(
                {
                    samples_collected: time.time()
                }
            )
            samples_collected += 1
            if samples_collected > self.samples:
                break

    def _generate_report(self):
        intervals_list = []

        for sample_number, timestamp in self.samples_dict.items():
            next_sample = self.samples_dict.get(sample_number + 1)
            if next_sample is not None:
                interval =  next_sample - timestamp
                intervals_list.append(interval)

        average_interval = sum(intervals_list)/len(intervals_list)
        frequency = 1/average_interval
        print(f'Average Interval is {round(average_interval, ndigits=2)} seconds')
        print(f'Events per minute is {round(frequency * 60, ndigits=2)}')
        print(f'Frequency of event is {round(frequency, ndigits=2)} Hz')

    def run(self):
        print('Press enter in time with the event')
        self._collect_data()
        self._generate_report()


def main():
    print('start measurement')
    freq = FreqMeasurer()
    freq.run()


if __name__ == '__main__':
    main()
