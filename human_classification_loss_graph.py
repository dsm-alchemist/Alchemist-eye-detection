import matplotlib.pyplot as plt

def g_show(train, test, title, file_name):
    plt.plot(train, label='Train Loss')
    plt.plot(test, label='Test Loss')
    plt.legend()
    plt.title(title)
    plt.xlabel('epoch')
    plt.savefig('/result/' + file_name + '.png', dpi=300, facecolor='white')