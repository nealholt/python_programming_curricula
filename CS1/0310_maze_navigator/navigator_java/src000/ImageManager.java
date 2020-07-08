import java.awt.Transparency;
import java.awt.image.BufferedImage;
import java.io.File;
import java.util.Hashtable;
import javax.imageio.ImageIO;

public class ImageManager
{	//Store all the images that have ever been loaded.
	private Hashtable<String, BufferedImage> images = new Hashtable<String, BufferedImage>();

	public ImageManager()
	{	//load the sprite sheet
		//roguelike_images/Spritesheet/roguelikeSheet_transparent.png
		//There are 1767 tiles
		BufferedImage image_sheet = loadImage("roguelike_images/Spritesheet/roguelikeSheet_transparent.png");
		//The tiles are 16 x 16px and have a 1px margin between them.
		for(int x=0; x*17<image_sheet.getWidth(); x++)
		{
			for(int y=0; y*17<image_sheet.getHeight(); y++)
			{
				//Get an empty and transparent buffered image
				//of the size of the image to cut out
				BufferedImage result = new BufferedImage(
						16, 16, Transparency.TRANSLUCENT);
				result = copySrcIntoDstAt(
						image_sheet,
						result,
						x*17, y*17, x*17+16, y*17+16);
				//Save the image in the hashtable
				this.images.put(Integer.toString(x)+","+Integer.toString(y), result);
				System.out.println(Integer.toString(x)+","+Integer.toString(y));
			}//for(int y=0; y<image_sheet.getHeight(); y+=17)
		}//for(int x=0; x<image_sheet.getWidth(); x+=17)
	}//public ImageManager()


	/* Retrieve a copy of the image from the hashtable.
	 * If the image is not yet in the hashtable, create it. */
	public BufferedImage getImage(String image_id)
	{
		if(!this.images.containsKey(image_id))
		{	//Load the image
			BufferedImage bi = this.loadImage(image_id);
			//Put the image in the hashtable
			this.images.put(image_id, bi);
		}
		return this.images.get(image_id);
	}

	//Load a buffered image
	private BufferedImage loadImage(String image_file)
	{
		BufferedImage img = null;
		try
		{
			img = ImageIO.read(new File(image_file));
		}
		catch (Exception e) 
		{
			System.out.println("Error loading image: '"+image_file+"'.");
			e.printStackTrace();
			System.exit(0);
		}
		return img;
	}

	/* http://stackoverflow.com/questions/2825837/java-how-to-do-fast-copy-of-a-bufferedimages-pixels-unit-test-included
	 * This is used for cutting out images from the spritesheet. */
	private BufferedImage copySrcIntoDstAt(
			BufferedImage src,
			BufferedImage dst,
			int x1, int y1,
			int x2, int y2)
	{
		if(x2 < x1 || y2 < y1)
		{
			System.out.println("WARNING in ImageManager.copySrcIntoDstAt. Negative dx or dy. Continuing without drawing attachment.");
			return dst;
		}
		boolean transparent_pixel = false;
		for (int x = x1; x < x2; x++)
		{
			for (int y = y1; y < y2; y++)
			{
				try{
					transparent_pixel = isTransparent(x, y, src);
				}catch(ArrayIndexOutOfBoundsException e){
					e.printStackTrace();
					System.out.println("\n\nCaught checking transparent pixel in src.");
					System.out.println("x: "+Integer.toString(x));
					System.out.println("y: "+Integer.toString(y));
					System.out.println("src width: "+Integer.toString(src.getWidth()));
					System.out.println("src height: "+Integer.toString(src.getHeight()));
					System.out.println("dst width: "+Integer.toString(dst.getWidth()));
					System.out.println("dst height: "+Integer.toString(dst.getHeight()));
					System.exit(0);	
				}
				if(!transparent_pixel)
				{
					try{
						dst.setRGB( x-x1, y-y1, src.getRGB(x,y) );
					}catch(ArrayIndexOutOfBoundsException e){
						e.printStackTrace();
						System.out.println("\n\nx: "+Integer.toString(x));
						System.out.println("y: "+Integer.toString(y));
						System.out.println("src width: "+Integer.toString(src.getWidth()));
						System.out.println("src height: "+Integer.toString(src.getHeight()));
						System.out.println("dst width: "+Integer.toString(dst.getWidth()));
						System.out.println("dst height: "+Integer.toString(dst.getHeight()));
						System.exit(0);
					}
				}
			}
		}
		return dst;
	}

	/* Detect if requested pixel is transparent */
	private boolean isTransparent(int x, int y, BufferedImage img)
	{
		//http://stackoverflow.com/questions/8978228/java-bufferedimage-how-to-know-if-a-pixel-is-transparent
		//The first byte is the alpha value.
		return (img.getRGB(x,y)>>24) == 0x00;
	}
}