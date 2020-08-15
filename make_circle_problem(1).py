import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("Agg")
from celluloid import Camera
import random 

# def quicksort(array,)
    


# def q_partition(array,p,r):
#     x = array[r]
#     i = p-1
#     for elements in range(p,r):


def colors(array,color):
    colors = []
    for i in range(len(array)):
        colors.append(color)
    return(colors)


def bubblesort(array):
    n = len(array)
    color_array = colors(array,"blue")    
    for i in range(n):
        #Prints every 10 iterations, only for debugging purposes
        if i%10 == 0:
            print(i)
        swapped=False
        for j in range(n-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                swapped=True
                color_array[j],color_array[j+1]="red","red"
                plt.bar(names,array,color=color_array)
                camera.snap()
                color_array[j],color_array[j+1]="blue","blue"
            
        # color_array[-(i+1)]="green"
        color_array[-(i+1)] ="green"
        plt.bar(names,array,color=color_array)
        camera.snap()
        if swapped== False:
                break
    color_array = colors(array,"green")
    plt.bar(names,array,color=color_array)
    camera.snap()
        
                
fig = plt.figure()
camera = Camera(fig)

#Initialize array with given size
size = 100
array = list(range(1,size+1))
names = list(range(1,size+1))
random.seed(1)
random.shuffle(array)
    
bubblesort(array)

animation = camera.animate()
animation.save('animation.mp4',fps=60)
print("Animation is done!")
plt.close('all')