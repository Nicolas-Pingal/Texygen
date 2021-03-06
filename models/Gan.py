from abc import abstractmethod

from utils.utils import init_sess


class Gan:
    def __init__(self):
        self.oracle = None
        self.generator = None
        self.discriminator = None
        self.gen_data_loader = None
        self.dis_data_loader = None
        self.oracle_data_loader = None
        self.sess = init_sess()
        self.metrics = list()
        self.epoch = 0
        self.pre_epoch_num = 80
        self.adversarial_epoch_num = 100
        self.log = None
        self.reward = None
        self.oracle_file = 'save/oracle.txt'
        self.generator_file = 'save/generator.txt'
        self.test_file = 'save/test_file.txt'
        self.csv_file = 'type_experiment_log.csv'

    def set_oracle(self, oracle):
        self.oracle = oracle

    def set_output_file(self, test_file):
        self.test_file = test_file

    def set_pre_epoch_num(self, pre_epoch_num):
        self.pre_epoch_num = pre_epoch_num

    def set_adversarial_epoch_num(self, adversarial_epoch_num):
        self.adversarial_epoch_num = adversarial_epoch_num

    def set_generator(self, generator):
        self.generator = generator

    def set_csv_file(self, csv_file):
        self.csv_file = csv_file

    def set_discriminator(self, discriminator):
        self.discriminator = discriminator

    def set_data_loader(self, gen_loader, dis_loader, oracle_loader):
        self.gen_data_loader = gen_loader
        self.dis_data_loader = dis_loader
        self.oracle_data_loader = oracle_loader

    def set_sess(self, sess):
        self.sess = sess

    def add_metric(self, metric):
        self.metrics.append(metric)

    def add_epoch(self):
        self.epoch += 1

    def reset_epoch(self):
        # current not in use
        self.epoch = 0
        return


    def evaluate(self):
        from time import time
        log = "epoch:" + str(self.epoch) + '\t'
        scores = list()
        scores.append(self.epoch)
        for metric in self.metrics:
            tic = time()
            score = metric.get_score()
            log += metric.get_name() + ":" + str(score) + '\t'
            toc = time()
            print('time elapsed of ' + metric.get_name() + ': ' + str(toc - tic))
            scores.append(score)
        print(log)
        return scores

    def check_valid(self):
        # TODO
        pass

    @abstractmethod
    def train_oracle(self):
        pass

    def train_cfg(self):
        pass

    def train_real(self):
        pass
