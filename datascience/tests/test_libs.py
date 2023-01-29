import unittest

# Write test case for method from libs.py
class TestLibs(unittest.TestCase):
    def test_generate_data(self):
        from libs import generate_data
        # Write test case for generate_data
        df = generate_data(10,2)
        self.assertEqual(df.shape, (10, 3))

    def test_print_generated_data(self):
        from libs import generate_data, print_generated_data
        # Write test case for print_generated_data, validate use print inside
        df = generate_data(10,2)
        print_generated_data(df)
        self.assertEqual(df.shape, (10, 3))

    def test_create_models(self):
        from libs import create_models
        # Write test case for create_models, validate the models is list and length is 5 and they are different
        models = create_models()
        self.assertEqual(len(models), 5)
        self.assertEqual(type(models), list)
        self.assertEqual(
            models[0] != models[1] != models[2] != models[3] != models[4], True
        )

    def test_train_test_split(self):
        from libs import generate_data, train_test_split
        # Write test case for train_test_split, validate the train and test is different
        df = generate_data(500)
        train, test = train_test_split(df)
        self.assertEqual(train.shape[0] != test.shape[1], True)

    def test_train_models_and_return_aucs(self):
        from libs import generate_data, create_models, train_test_split, train_models_and_return_aucs
        # Write test case for train_models_and_return_aucs, validate the aucs is list and length is 5
        df = generate_data(500)
        models = create_models()
        train, test = train_test_split(df)
        _, aucs = train_models_and_return_aucs(train, test, models)
        self.assertEqual(len(aucs), 5)
        self.assertEqual(type(aucs), list)

    def test_mean_auc(self):
        from libs import generate_data, create_models, train_test_split, train_models_and_return_aucs, mean_auc
        import numpy as np
        # Write test case for mean_auc, validate the mean_auc is float
        df = generate_data(500)
        models = create_models()
        train, test = train_test_split(df)
        _, aucs = train_models_and_return_aucs(train, test, models)
        auc = mean_auc(aucs)
        self.assertEqual(type(auc), np.float64)
        self.assertGreater(auc, 0.45)
