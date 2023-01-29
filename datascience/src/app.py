from libs import (
    generate_data,
    print_generated_data,
    create_models,
    train_test_split,
    train_models_and_return_aucs,
    mean_auc,
)

if __name__ == "__main__":
    df = generate_data(1000)
    # print_generated_data(df)
    models = create_models()
    train, test = train_test_split(df)
    print("train: ", train.shape[0], "test: ", test.shape[0])
    _, aucs = train_models_and_return_aucs(train, test, models)
    print("aucs: ", aucs)
    print(mean_auc(aucs))
