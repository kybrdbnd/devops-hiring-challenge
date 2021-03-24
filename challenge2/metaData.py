"""EC2 metaData has been retrieved using v1 meta-data call"""

import requests

IP = 'http://169.254.169.254'
PATH = 'latest/meta-data'


def get_meta_data():
    """get EC2 instance meta data"""
    metaDataObjects = []
    try:
        res = requests.get(f"{IP}/{PATH}")
        res = res.content
        metaDataObjects = res.split('\n')
        print("ec2 meta data objects retrieved successfully")
    except Exception as err:
        print(err)
    return metaDataObjects


def make_children_calls(parent, childObjs):
    for child in childObjs:
        res = requests.get(f"{IP}/{PATH}/{parent}/{child}")
        res = res.content
        print(res)


def print_meta_data(metaDataObjects):
    """prints ec2 meta data"""
    for obj in metaDataObjects:
        try:
            res = requests.get(f"{IP}/{PATH}/{obj}")
            res = res.content
            if '/' in obj:
                childObjs = res.split('\n')
                print("got nested objects")
                make_children_calls(obj, childObjs)
            else:
                print(f'{obj} : {res}')
        except Exception as err:
            print(err)


if __name__ == '__main__':
    ec2metaDataObs = get_meta_data()
    print_meta_data(ec2metaDataObs)
