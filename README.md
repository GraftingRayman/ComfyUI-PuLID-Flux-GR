### update Jan.09 2025
Due to multiple issues, this repo has been renamed and moved 

Should no longer cause conflicts with existing versions

Added cleanup and destruction codes to free up resources

### update Jan.07 2025
###
face_select has two new options

smallest_face and most_prominent

they do what the names suggest

### update Jan.01 2025
#### face number
if face_select option is set to normal

you can now select different faces from an image, this applies when you have a single image with multiple faces in it, like a group photo

#### center_face and largest_face

changed the default to not select center face, this will need selecting normal in the face_select option

you can also select largest face in the picture by selecting largest_face

if normal is selected in face_select, you can use the blur settings to ignore blurred faces (this only applies to batches of faces)

normal usually selects the face to the far right of the image, but don't count on that to happen, did not delve into the mathematics of what gets chosen

![image](https://github.com/user-attachments/assets/7c668c17-5f60-477c-93d5-91d88889dc5f)

# Installation:
Goto your custom_nodes folder and type the following in terminal/command prompt:

<code>git clone https://github.com/GraftingRayman/ComfyUI-PuLID-Flux-GR</code>

Then install the requirements by entering the following in terminal/command prompt:

<code>pip install -r requirements.txt</code>

If you are using a portable version of ComfyUI, you need to run the following in terminal/command prompt:

<code>h:\ComfyUI_windows_portable\ComfyUI\python_embeded\python.exe -m pip install -r h:\ComfyUI_windows_portable\ComfyUI\custom_nodes\ComfyUI-PuLID-Flux-GR\requirements.txt</code>

You will need to fix the path in the above command to match the location of your ComfyUI



