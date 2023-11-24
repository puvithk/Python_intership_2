import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as anime
import random




def update_bar(bars,colors):
    for bar , col in zip(bars ,colors):
        bar.set_color(col)
    return bar


def bubble_sort(x,draw ,delay):
    for i in range(len(x)):
        for j in range(0,len(x)-1-i):
            if(x[j]>x[j+1]):
                x[j],x[j+1] = x[j+1] , x[j]
                draw(x ,[ 'green' if x==j or x==j+1 else 'blue' for x in range(len(x)) ])
                plt.pause(delay)
def generate_data(size):
    return [random.randint(1,100) for _ in range(size) ]
def main():
    size = 30
    data = generate_data(size)
    fig, ax = plt.subplots()
    bars =ax.bar(range(size),data,color='blue')
    ax.set_xlim(0, size)
    ax.set_ylim(0, max(data)+10)
    def draw(data , colors):
        for bar,var,color in zip(bars,data,colors):
            bar.set_height(var)
            bar.set_color(color)
    try:
        anime.Animation(fig, update_bar(bars,['blue' ] * len(data)),frames=bubble_sort(data.copy(),draw ,0.01),repeat=False , save_count = len(data))
        plt.show()
    except Exception as e:
        print(e)
        
    

    
if __name__ =="__main__":
    main()