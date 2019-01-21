import glob
from PIL import Image
import pathlib

input_dir = "/Users/kieranbristow/Workspace/Subatomic/subatomic-documentation/docs/images/user-guide/"
exclude = ["devops-env-created.png", "bitbucket-url.png", "openshift-environments.png"]

max_width = 0
max_image = ""
for filename in glob.iglob(f'{input_dir}/**/*.png', recursive=True):
    image_name = filename.split("/")[-1]
    if image_name in exclude:
        continue

    img = Image.open(filename)
    img_w, img_h = img.size
    if img_w > max_width:
        max_image = filename
    max_width = max(max_width, img_w)

print (max_image)

for filename in glob.iglob(f'{input_dir}/**/*.png', recursive=True):

    image_name = filename.split("/")[-1]
    if image_name in exclude:
        continue

    img = Image.open(filename)
    img_w, img_h = img.size
    background = Image.new('RGBA', (max_width, img_h), (255, 255, 255, 255))
    background.paste(img, (0, 0))

    new_file_name = filename.replace(input_dir, "./output/")

    path = "/".join(new_file_name.split("/")[:-1])

    pathlib.Path(path).mkdir(parents=True, exist_ok=True)

    background.save(new_file_name)
