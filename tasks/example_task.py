import csv
from functools import reduce
from fractions import gcd
import random

import luigi


class RandomNumbers(luigi.Task):
    date = luigi.DateParameter()

    def run(self):
        with self.output().open('w') as output_file:
            csv_writer = csv.writer(output_file)

            for i in range(1000):
                csv_writer.writerow([
                    random.randint(1, 100),
                    random.randint(1, 1000),
                    random.randint(1, 10000)
                 ])

    def output(self):
        return luigi.LocalTarget(
            self.date.strftime('data/random_%Y_%m_%d.csv')
        )


class LeastCommonMultiple(luigi.Task):
    date_interval = luigi.DateIntervalParameter()

    def output(self):
        return luigi.LocalTarget("data/lcf_{}.csv".format(self.date_interval))

    def requires(self):
        """ Returns all the RandomNumbers.output w/in the date interval """
        return [RandomNumbers(date) for date in self.date_interval]

    def run(self):
        with self.output().open('w') as output_file:
            output_csv = csv.writer(output_file)

            for input_task in self.input():
                with input_task.open('r') as input_file:
                    input_csv = csv.reader(input_file)
                    for row in input_csv:
                        input_csv = csv.reader(input_file)

                        output_csv.writerow([
                            self.lcm(*[int(i) for i in row]),
                            *row
                        ])

    @staticmethod
    def lcm(*numbers):
        def lcm(a, b):
            return (a * b) // gcd(a, b)
        return reduce(lcm, numbers, 1)


if __name__ == "__main__":
    luigi.run()
