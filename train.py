import numpy as np
from sklearn.model_selection import train_test_split

def get_dataset():
    '''df = pd.read_csv('Data/dataset.csv')
    Y = df['winner']
    X = df.drop('winner', axis=1)'''
    X = np.loadtxt('Data/dataset.csv', delimiter=',')
    Y = X[:, -1]
    X = X[:, :-1]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=42)
    return X_train, X_test, Y_train, Y_test


def train_model(model, X_train, X_test, Y_train, Y_test):
    model.fit(X_train, Y_train, validation_data=(X_test, Y_test), shuffle=True, epochs=10, batch_size=200)
    return model


def main():
    X_train, X_test, Y_train, Y_test = get_dataset()
    from get_model import get_model, save_model
    model = get_model()
    model = train_model(model, X_train, X_test, Y_train, Y_test)
    save_model(model)
    return model


if __name__ == '__main__':
    main()