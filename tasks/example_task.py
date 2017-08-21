import csv

import luigi

import lib


class RandomNumbers(luigi.Task):
    number = luigi.IntParameter()

    def run(self):
        with self.output().open('w') as output_file:
            csv_writer = csv.writer(output_file)

            for row in lib.rows_of_random_numbers(rows=10000):
                csv_writer.writerow(row)

    def output(self):
        return luigi.LocalTarget('data/random_{}.csv'.format(self.number))


class LeastCommonMultiple(luigi.Task):
    count = luigi.IntParameter()

    def output(self):
        return luigi.LocalTarget("data/lcf_{}.csv".format(self.count))

    def requires(self):
        """ Returns all the RandomNumbers.output w/in the date interval """
        return [RandomNumbers(i) for i in range(self.count)]

    def run(self):
        with self.output().open('w') as output_file:
            output_csv = csv.writer(output_file)

            for input_task in self.input():
                with input_task.open('r') as input_file:
                    input_csv = csv.reader(input_file)
                    for row in lib.generate_lcm_rows(input_csv):
                        output_csv.writerow(row)


if __name__ == "__main__":
    luigi.run()
