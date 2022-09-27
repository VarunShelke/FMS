import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
result_list = []
def data_read(iplist):
    input_list = iplist
    df = pd.read_excel('datasets/khadakwasala.xlsx').dropna()
    f1 = df['today_rain'].values
    X = np.array(list(zip(f1)))
    result_list = clustering(3, X, input_list)
    return result_list
    
def clustering(n, data, input_list):
    kmeans = KMeans(n_clusters = n)
    kmeans = kmeans.fit(data)

    centroids = sorted(kmeans.cluster_centers_)
    cluster_0 = centroids[0]
    cluster_1 = centroids[1]
    cluster_2 = centroids[2]
    result_list = prediction(cluster_0, cluster_1, cluster_2, input_list)
    return result_list

def prediction(cluster_0, cluster_1, cluster_2, input_list):
    for i in range(0, len(input_list)):
        x = int(input_list[i])
        result_list.append(perform_prediction(cluster_0, cluster_1, cluster_2, x))
    
    return result_list
    
def perform_prediction(cluster_0, cluster_1, cluster_2, x):    
    y1_1 = abs(x - cluster_0[0])
    y1_2 = abs(x - cluster_1[0])
    y1_3 = abs(x - cluster_2[0])

    y1 = min(y1_1, y1_2, y1_3)

    match = []
    if(y1 == y1_1):
        match.append(0)
    elif(y1 == y1_2):
        match.append(1)
    elif(y1 == y1_3):
        match.append(2)

    c1_count = 0
    c2_count = 0
    c3_count = 0

    for number in match:
        if(number == 0):
            c1_count+= 1
        elif(number == 1):
            c2_count+= 1
        elif(number == 2):
            c3_count+= 1

    max_matches = max(c1_count, c2_count, c3_count)
    if(max_matches == c1_count):
        ans = 1
    elif(max_matches == c2_count):
        ans = 2
    elif(max_matches == c3_count):
        ans = 3
        
    return ans

def labelling():
    df_for_labelling = pd.read_excel('datasets/khadakwasala.xlsx').dropna()
    value_list = df_for_labelling['today_rain'].values.tolist()
    final_list = data_read(value_list)
    df_for_labelling['severity'] = final_list
    df_for_labelling.to_excel("final.xlsx", sheet_name = "labelled_data", index = False)
    
labelling()