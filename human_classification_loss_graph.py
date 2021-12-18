import matplotlib.pyplot as plt

def g_show(value, title, file_name):
    plt.plot(value)
    plt.title(title)
    plt.xlabel('epoch')
    plt.savefig('/result/' + file_name + '.png', dpi=300, facecolor='white')