import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def kNN_algorithm(rainFall, damPercent):
    train_df = pd.read_excel('final.xlsx')
    test_df = pd.DataFrame({'rainfall': rainFall, 'available_percent': damPercent}, index=[0])
    X = train_df.drop(columns = ['date', 'severity'])
    y = train_df['severity'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 4)
    knn = KNeighborsClassifier(n_neighbors = 48)
    knn.fit(X_train,y_train)
    X_test = test_df
    return int(knn.predict(X_test)[0])