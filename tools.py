# Setup a dask cluster
from dask.distributed import Client
from dask_kubernetes import KubeCluster

def init_cluster(n_workers=10):
    cluster = KubeCluster(n_workers=n_workers)
    client = Client(cluster)
    return cluster, client
