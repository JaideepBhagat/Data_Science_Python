import matplotlib.pyplot as plt

# Reading a binary file (image)
with open("python.png", 'rb') as img:
    content = img.read()

with open("python_copy.png", 'wb') as img:
    img.write(content)

img = plt.imread("python_copy.png")

plt.imshow(img)
plt.show()