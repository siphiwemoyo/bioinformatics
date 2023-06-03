from matplotlib import pyplot 
from matplotlib.animation import FuncAnimation
from PIL import Image

seq = 'AGCTCGCTCGCTGCGTATAAAATCGCATCGCGCGCAGCAAAATCGATCGCGC'

def GC_content(seq, window_size=15):
    GC_values = []

    for i in range(len(seq)-window_size):
        sub_Sequence = seq[i:i+window_size]
        num_GC = sub_Sequence.count('G')+sub_Sequence.count('C')
        value = num_GC/float(window_size)
        GC_values.append(value)
    return GC_values

GC_results = GC_content(seq)

# This bar chart can display the GC content percentages for different DNA sequences or regions.
def update(frame):
    pyplot.cla()
    pyplot.bar(range(frame+1), GC_results[:frame+1])
    pyplot.xlabel('Sequence Position')
    pyplot.ylabel('GC Content')
    pyplot.title('GC Content Variation')
    pyplot.ylim(0, 1)  # Set the y-axis limits between 0 and 1

fig = pyplot.figure()
ani = FuncAnimation(fig, update, frames=len(GC_results), interval=500, repeat=False)
ani.running=True

images = []
for i in range(len(GC_results)):
    update(i)
    fig.canvas.draw()
    image = Image.frombytes('RGB', fig.canvas.get_width_height(), fig.canvas.tostring_rgb())
    images.append(image)
    
images[0].save('animation.gif', save_all=True, append_images=images[1:], optimize=False, duration=500, loop=0)
pyplot.show()