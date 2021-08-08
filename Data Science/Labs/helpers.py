import matplotlib.pyplot as plt

def draw_vector(v0, v1):
    ax = plt.gca()
    ax.annotate('', v1, v0, 
                arrowprops={'arrowstyle': '->', 'linewidth': 4})
