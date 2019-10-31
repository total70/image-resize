from os import listdir, mkdir
from PIL import Image

def check_if_dir_exists():
	try: 
		mkdir('resize')
	except:
		pass


check_if_dir_exists()

def get_images_in_folder():
	try:
		files = []
		for file in listdir('.'):
			splits = file.split('.')

			for idx, split in enumerate(splits):
				if split != 'jpg':
					files.append(f'{split}.jpg')
		return files	
	except:
		pass	

files = get_images_in_folder()

def get_image_size(image, reducer):
	return round(image.size[0] / reducer), round(image.size[1]/ reducer)

for file in files:
	try:
		size = 6
		image = Image.open(file)
		width, height = get_image_size(image, reducer=size)
		print("------ Image size ------")
		print(f'width: {width} height: {height}')
		image = image.resize(size=(width,height), resample=Image.LANCZOS)
		image.save(f'resize/{file}')
	except:
		pass	
