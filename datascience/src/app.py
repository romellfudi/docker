from libs import generate_data, print_generated_data

if __name__ == '__main__':
    df = generate_data(10)
    print_generated_data(df)