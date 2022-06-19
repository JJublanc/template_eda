import pathlib
import matplotlib.pyplot as plt
from PIL import Image
from numpy import asarray

data_dir = pathlib.Path("data/pangolins")

if __name__ == '__main__':
    data_dir = pathlib.Path("./data/pangolins")
    pangolins = list(data_dir.glob('*.jpg'))

    plt.figure(figsize=(20, 20))
    nb_sample = 10

    for i in range(nb_sample):
        ax = plt.subplot(nb_sample, 4, i * 4 + 1)
        img = Image.open(pangolins[i])
        plt.imshow(img)
        plt.title("size = {}".format(img.size))
        plt.axis('off')

        # Red, Green, Blue
        numpydata = asarray(img)
        ax = plt.subplot(nb_sample, 4, i * 4 + 2)
        plt.hist(numpydata[:, :, 0].flatten(), bins=50, color='r')

        ax = plt.subplot(nb_sample, 4, i * 4 + 3)
        plt.hist(numpydata[:, :, 1].flatten(), bins=50, color='g')

        ax = plt.subplot(nb_sample, 4, i * 4 + 4)
        plt.hist(numpydata[:, :, 2].flatten(), bins=50, color='b')


    plt.savefig('./reports/pangolins_custom.png')

