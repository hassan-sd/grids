import os
import glob
from PIL import Image

def create_grid(input_folder, dimensions):
    width, height = map(int, dimensions.split('x'))
    os.makedirs('grids', exist_ok=True)

    images = sorted(glob.glob(f'{input_folder}/*'))
    for i in range(0, len(images), 4):
        grid_image = Image.new('RGB', (width * 2, height * 2))

        for j in range(4):
            if i + j < len(images):
                img = Image.open(images[i+j])
                grid_image.paste(img, ((j % 2) * width, (j // 2) * height))

        grid_image.save(f'grids/grid_{i//4+1}.png')


def separate_grid(input_folder, dimensions, aspect):
    width, height = map(int, dimensions.split('x'))
    os.makedirs('output', exist_ok=True)

    split_width, split_height = (width // 2, height // 2) if aspect == 'square' else map(int, aspect.split('x'))

    grid_images = sorted(glob.glob(f'{input_folder}/*'))
    for i, grid_image_path in enumerate(grid_images):
        grid_image = Image.open(grid_image_path)

        for j in range(4):
            left = (j % 2) * split_width
            top = (j // 2) * split_height
            right = left + split_width
            bottom = top + split_height
            image = grid_image.crop((left, top, right, bottom))
            image.save(f'output/image_{i*4+j+1}.png')


def main():
    option = input('Are you A) creating a grid or B) separating a grid? ')
    dimensions = input('Enter the image dimensions (e.g., 512x512): ')

    if option.lower() == 'a':
        folder = input('Enter the folder containing the images: ')
        create_grid(folder, dimensions)
    elif option.lower() == 'b':
        aspect = input('Is the aspect ratio square, portrait or landscape? If it\'s portrait or landscape, enter dimensions (widthxheight): ')
        folder = input('Enter the folder containing the grid images: ')
        separate_grid(folder, dimensions, aspect)


if __name__ == '__main__':
    main()
