def add(num1, num2):
    return num1 + num2


def multiply_by_10(df):
    for col in df.columns:

        df[col] *= 10
    return df