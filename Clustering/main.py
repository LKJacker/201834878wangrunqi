import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import normalized_mutual_info_score
from sklearn.cluster import AffinityPropagation
from sklearn.cluster import MeanShift
from sklearn.cluster import SpectralClustering
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
from sklearn.mixture import GaussianMixture


def load_data():
    dir = 'data/Tweets.txt'
    text, labels = [], []
    with open(dir, 'r', encoding='utf-8',errors="errors") as f:
        for line in f:
            js = json.loads(line.strip())
            text.append(js['text'])
            labels.append(js['cluster'])
    return text, labels
def Kmeans(text, labels):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(text)

    kmeans = KMeans(n_clusters=89, max_iter=50, n_init=10, init='k-means++')
    result_kmeans = kmeans.fit_predict(X.toarray())
    print('K-means acc:', normalized_mutual_info_score(result_kmeans, labels))


def AffinityPropagation_(text, labels):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(text)

    affinity_propagation = AffinityPropagation(damping=0.5, max_iter=50, convergence_iter=10, copy=False)
    result_affinity_propagation = affinity_propagation.fit_predict(X.toarray())
    print('AffinityPropagation acc:', normalized_mutual_info_score(result_affinity_propagation, labels))



def Mean_shift(text, labels):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(text)

    mean_shift = MeanShift(bandwidth=0.65, bin_seeding=True)
    result_mean_shift = mean_shift.fit_predict(X.toarray())
    print('MeanShift acc:', normalized_mutual_info_score(result_mean_shift, labels))


def SpectralClustering_(text, labels):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(text)

    spectral_clustering = SpectralClustering(n_clusters=89, n_init=10)
    result_spectral_clustering = spectral_clustering.fit_predict(X.toarray())
    print('SpectralClustering acc:', normalized_mutual_info_score(result_spectral_clustering, labels))

def AgglomerativeClustering_(text, labels):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(text)

    agglomerative_clustering = AgglomerativeClustering(n_clusters=89)
    result_agglomerative_clustering = agglomerative_clustering.fit_predict(X.toarray())
    print('AgglomerativeClustering acc:', normalized_mutual_info_score(result_agglomerative_clustering, labels))
    # AgglomerativeClustering accuracy: 0.7800394104591923


def DBSCAN_(text, labels):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(text)

    dbscan = DBSCAN(eps=0.5, min_samples=1, leaf_size=30)
    result_dbscan = dbscan.fit_predict(X.toarray())
    print('DBSCAN acc:', normalized_mutual_info_score(result_dbscan, labels))


def GaussianMixture_(text, labels):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(text)

    gaussian_mixture = GaussianMixture(n_components=89)
    result_gaussian_mixture = gaussian_mixture.fit_predict(X.toarray())
    print('GaussianMixture accuracy:', normalized_mutual_info_score(result_gaussian_mixture, labels))
    # GaussianMixture accuracy: 0.792451745546511


if __name__ == '__main__':
    text, labels = load_data()
    Kmeans(text, labels)
    AffinityPropagation_(text, labels)
    Mean_shift(text, labels)
    SpectralClustering_(text, labels)
    AgglomerativeClustering_(text, labels)
    DBSCAN_(text, labels)
    GaussianMixture_(text, labels)