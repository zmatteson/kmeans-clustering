import argparse
import random
import math

def find_center(cluster):
    x = 0
    y = 0
    for point in cluster:
        x += point[0]
        y += point[1]
    x = x / len(cluster)
    y = y / len(cluster)
    return (x , y)

def recalculate_centroids(clusters, data):
    centroids = []
    for cluster in clusters:
        centroids.append(find_center(cluster))
    clusters = get_clusters(data, centroids)
    return (centroids, clusters)

def get_distance(a,b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    return math.sqrt(x**2 + y**2)

def find_closest_center(x, centroids):
    minDistance = float('inf')
    index = 0
    for i, center in enumerate(centroids):
        distance = get_distance(x, center)
        if minDistance >= distance:
            index = i
            minDistance = distance
    return index

def initialize_centroids(data, k):
    centroids = []
    points = random.sample(range(len(data)), k)
    for i in points:
        centroids.append(data[i])
    return centroids

def get_clusters(data, centroids):
    clusters = []
    for _ in range(len(centroids)):
        clusters.append([])
    for x in data:
        index = find_closest_center(x, centroids)
        clusters[index].append(x)
    return clusters


def output_clusters(clusters):
    f = open('values-output.txt', 'w+')
    for i, cluster in enumerate(clusters):
        for point in cluster:
            string = []
            string.append(str(int(point[0])))
            string.append(str(int(point[1])))
            string.append(str(i))
            string.append('\n')
            line = ' '.join(string)
            f.write(line)
    f.close()

def process_data(filename):
    f = open(filename, 'r')
    data= []
    for line in f:
        a = line.strip('\n')
        b = a.split(' ')
        data.append((float(b[0]), float(b[1])))
    f.close()
    return data

def main():
    parser = argparse.ArgumentParser(description='Create a decision tree from a CSV file.')
    parser.add_argument('file', help='the data file to be processed')
    parser.add_argument('k', help='the number of clusters to find')
    args = parser.parse_args()
    data = process_data(args.file)
    centroids = initialize_centroids(data, int(args.k))
    clusters = get_clusters(data, centroids)

    centroids, clusters = recalculate_centroids(clusters, data)[0], recalculate_centroids(clusters, data)[1]
    while centroids != recalculate_centroids(clusters,data)[0]:
        centroids, clusters = recalculate_centroids(clusters, data)[0], recalculate_centroids(clusters, data)[1]
    output_clusters(clusters) 

main()