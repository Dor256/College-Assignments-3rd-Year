import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def prepare_univar_func(f: staticmethod, x_min: int, x_max: int, title: str):
    plt.title(title)
    x_values = [x for x in range(x_min, x_max)]
    y_values = [f(x) for x in x_values]
    plt.plot(x_values, y_values)


def prepare_bivar_func(f: staticmethod, title: str, alpha: float = 1) -> Axes3D:
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X = np.arange(-2, 2.+0.05, 0.05)
    Y = np.arange(-2, 2.+0.05, 0.05)
    X, Y = np.meshgrid(X, Y)
    Z = np.array([f(np.array([x, y])) for x, y in zip(X, Y)])
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False, alpha=alpha)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.title(title)
    return ax


def plot_bivar_func(f: staticmethod, title: str, alpha: float = 1):
    prepare_bivar_func(f, title)
    plt.show()


def plot_univar_func(f: staticmethod, x_min: int, x_max: int, title: str):
    prepare_univar_func(f, x_min, x_max, title)
    plt.show()


def plot_gradient_descent_path(f: staticmethod, path: list, title: str):
    ax = prepare_bivar_func(f, title, alpha=0.3)
    X = [x[0] for x in path]
    Y = [y[1] for y in path]
    Z = np.array([f(np.array([x, y])) for x, y in zip (X, Y)])
    ax.scatter(X, Y, Z, color='black', label='Gradient Descent Path')
    ax.legend(loc='upper center', bbox_to_anchor=(1.1, 0))
    plt.show()


def plot_roc_curve(fpr, tpr):
    plt.figure()
    lw = 2
    plt.plot(fpr, tpr, label='ROC Curve')
    plt.show()


def plot_confusion_matrix(matrix, classes, thresh, title: str = 'Confusion Matrix', cmap=cm.Blues):
    plt.imshow(matrix, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(-0.5, len(classes) + 0.5)
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    for i, j in product(range(matrix.shape[0]), range(matrix.shape[1])):
        plt.text(j, i, matrix[i, j], horizontalalignment="center", color="white" if matrix[i, j] > thresh else "black")
    plt.show()