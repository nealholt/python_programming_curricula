import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.MouseInfo;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.MouseEvent;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import javax.swing.JPanel;
import javax.swing.event.MouseInputListener;

public class Board extends JPanel 
{	//Original code came largely from this tutorial:
	//http://zetcode.com/tutorials/javagamestutorial/movingsprites/
	private static final long serialVersionUID = 1L;
	private BufferedImage image;
	private int image_x = 0;
	private int image_y = 0;
	
	public Board()
	{
		addKeyListener(new TAdapter());
		MAdapter myMouseEventListener = new MAdapter();
		this.addMouseListener(myMouseEventListener);
		this.addMouseMotionListener(myMouseEventListener);
		setFocusable(true);
		setBackground(Color.BLACK);
		//Double buffer gives efficiency gains. See here:
		//http://docs.oracle.com/javase/tutorial/extra/fullscreen/doublebuf.html
		setDoubleBuffered(true);
	}

	//Load a buffered image
	private BufferedImage loadImage(String image_file)
	{
		BufferedImage img = null;
		try
		{
			img = ImageIO.read(new File(image_file));
		}
		catch (IOException e) 
		{
			System.out.println("Error loading image: '"+image_file+"'.");
			e.printStackTrace();
			System.exit(0);
		}
		return img;
	}

	@Override
	public void paintComponent(Graphics g)
	{
		Graphics2D g2d = (Graphics2D) g;
		g2d.drawImage(image, image_x, image_y, this);
	}
	
	public void setImage(String image_file)
	{
		image = loadImage(image_file);
	}
	
	public void setImageXY(int x, int y)
	{
		this.image_x = x;
		this.image_y = y;
	}

	private class TAdapter extends KeyAdapter 
	{
		@Override
		public void keyReleased(KeyEvent e) 
		{
			//System.out.println(e.getKeyCode());
			//Any button closes the window
			System.exit(0);
		}

		@Override
		public void keyPressed(KeyEvent e) 
		{
		}
	}

	private class MAdapter implements MouseInputListener
	{
		public MAdapter() 
		{
			super();
		}

		@Override
		public void mouseClicked(MouseEvent arg0)
		{
			System.out.println("\nx:"+MouseInfo.getPointerInfo().getLocation().x);
			System.out.println("y:"+MouseInfo.getPointerInfo().getLocation().y);
		}

		@Override
		public void mousePressed(MouseEvent arg0)
		{
		}

		@Override
		public void mouseReleased(MouseEvent arg0)
		{
		}

		@Override
		public void mouseDragged(MouseEvent arg0)
		{
		}

		@Override
		public void mouseMoved(MouseEvent arg0)
		{
		}

		@Override
		public void mouseEntered(MouseEvent e)
		{
		}

		@Override
		public void mouseExited(MouseEvent e)
		{
		}
	}

}