import csv

import luigi

import lib


class RandomNumbers(luigi.Task):
    date = luigi.DateParameter()

    def run(self):
        with self.output().open('w') as output_file:
            csv_writer = csv.writer(output_file)

            for row in lib.rows_of_random_numbers():
                csv_writer.writerow(row)

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
                    for row in lib.generate_lcm_rows(input_csv):
                        output_csv.writerow(row)


if __name__ == "__main__":
    luigi.run()
