from itertools import cycle
from PIL import Image,ImageTk
import time
import tkinter as tk        #Tkinter is a GUI library which helps in creating  graphical elements like windows,buttons,lables.

root = tk.Tk()
root.title("Image Slideshow Viewer")

#List of Image Path
image_paths = [
    r"C:\Users\Lenovo\Pictures\Saved Pictures\WhatsApp Image 2025-03-18 at 11.32.51_d4dcfb9d.jpg", #r is raw string jo backslash ko escape character ni smjhega
    r"C:\Users\Lenovo\Pictures\Saved Pictures\WhatsApp Image 2025-03-18 at 11.32.52_b79737e2.jpg", # escape character for ex \n
    r"C:\Users\Lenovo\Pictures\Saved Pictures\WhatsApp Image 2025-03-18 at 11.32.53_4a028a46.jpg",
    r"C:\Users\Lenovo\Pictures\Saved Pictures\WhatsApp Image 2025-03-18 at 11.32.53_18b96530.jpg",
    r"C:\Users\Lenovo\Pictures\Saved Pictures\WhatsApp Image 2025-03-18 at 11.32.53_b03bef7b.jpg" ]
#Resize the images to 1080x1080
image_size=(1080,1080)
images=[Image.open(path).resize(image_size)for path in image_paths]
photo_images=[ImageTk.PhotoImage(image) for image in images]
label = tk.Label(root)
label.pack()
def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)           #config method helps in changing the attributes of label like image font etc.
        label.update()
        time.sleep(3)
slideshow = cycle(photo_images)
def start_slideshow():
    for _ in range (len(image_paths)):
        update_image()
play_button = tk.Button(root,text='Play',command = start_slideshow)
play_button.pack()

root.mainloop() #for infinite iteration
