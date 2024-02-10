from rembg import remove
import easygui
from PIL import Image

imputPath = easygui.fileopenbox(title='select image file')
outputPath = easygui.filesavebox(title='save file to...')

input = Image.open(imputPath)
output = remove(input)
output.save(outputPath)

