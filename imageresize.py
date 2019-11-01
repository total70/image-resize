from os import listdir, mkdir
from PIL import Image

class ImageResize():
	def __init__(self, size=1, inputPath='./input', outputPath='./output'):
		self.size = size
		self.inputPath = inputPath
		self.outputPath = outputPath
		self.files = self.get_images_in_folder()
		self.boot()

	def boot(self):
		self.check_if_dir_exists()
		self.create_image()

	def check_if_dir_exists(self):
		try: 
			mkdir(f'{self.outputPath}')
		except:
			pass

	def get_images_in_folder(self):
		try:
			files = []
			for file in listdir(self.inputPath):
				splits = file.split('.')
				for idx, split in enumerate(splits):
					if split != 'jpg':
						files.append(f'{split}.jpg')
			return files	
		except:
			pass
		
	def get_image_size(self, image, reducer):
		return round(image.size[0] / reducer), round(image.size[1]/ reducer)

	def create_image(self):
		for file in self.files:
			try:
				size = self.size
				image = Image.open(f'{self.inputPath}/{file}')
				width, height = self.get_image_size(image, reducer=size)
				print("------ Image size ------")
				print(f'width: {width} height: {height}') 
				image = image.resize(size=(width,height), resample=Image.LANCZOS)
				image.save(f'{self.outputPath}/{file}')				
			except:
				pass	

if __name__ == "__main__":
	imageResize = ImageResize(size=0.1, inputPath='./input', outputPath='./output')