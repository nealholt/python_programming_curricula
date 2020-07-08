import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.MouseInfo;
import java.awt.Point;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.MouseEvent;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

import javax.imageio.ImageIO;
import javax.swing.JPanel;
import javax.swing.event.MouseInputListener;

public class Board extends JPanel 
{	//Original code came largely from this tutorial:
	//http://zetcode.com/tutorials/javagamestutorial/movingsprites/
	private static final long serialVersionUID = 1L;
	private KeyManager key_setter = new KeyManager();
	private BufferedImage[][] image_grid;
	private char[][] ascii_grid;
	private int border_x = 100;
	private int border_y = 100;
	private final String[] water_tiles = {
			"0,0","1,0","2,0","3,0","4,0",
			"0,1","1,1","2,1","3,1","4,1",
			"0,2","1,2","2,2","3,2","4,2",
			"0,3","1,3","2,3","3,3","4,3",
			"0,4","1,4","2,4","3,4","4,4",
						"2,5","3,5","4,5",
			"54,23","55,23","56,23",
			"54,24","55,24","56,24"};
	private Boat boat;

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
		//System.out.println(water_tiles.length);
		//TODO
		boat = new Boat(2, 14);
		List<String> lines;
		try{
			lines = this.readSmallTextFile("maps/map1.txt");
			image_grid = new BufferedImage[lines.size()][lines.get(0).length()];
			ascii_grid = new char[lines.size()][lines.get(0).length()];
			for(int y=0; y<image_grid.length; y++)
			{
				for(int x=0; x<image_grid[y].length; x++)
				{
					ascii_grid[y][x] = lines.get(y).charAt(x);
					int index = (int)ascii_grid[y][x];
					//System.out.print((char)index +" ");
					//System.out.println((int)index);
					if(index<(int)'a'){
						//System.out.println((int)index);
						index -= (int)'0';
						//System.out.println((int)index);
						index += (int)'z' - (int)'a';
						//System.out.println((int)index);
					}else{
						index -= (int)'a';
					}
					//System.out.println(" "+index);
					image_grid[y][x] = Main.image_manager.getImage(
							water_tiles[index], 0);
				}
			}
		}catch(IOException e){
			e.printStackTrace(); System.exit(0);
		}
	}

	private List<String> readSmallTextFile(String aFileName) throws IOException
	{
	    Path path = Paths.get(aFileName);
	    return Files.readAllLines(path);
	}
	
	public void update()
	{
		if(this.key_setter.checkKeyReleased(38)) //up key
		{
			move();
		}
		//if(this.key_setter.checkKeyReleased(40)) //down key
		if(this.key_setter.checkKeyReleased(37)) //left key
		{
			this.boat.turnCounterClockwise();
		}
		if(this.key_setter.checkKeyReleased(39)) //right key
		{
			this.boat.turnClockwise();
		}
		//if(this.key_setter.checkKeyReleased(32)]) //space key
	}
	
	private boolean clearAhead()
	{
		Point p = boat.getCoordinatesAhead();
		return ascii_grid[(int)p.getY()][(int)p.getX()]=='i' || 
				ascii_grid[(int)p.getY()][(int)p.getX()]=='f' ||
				ascii_grid[(int)p.getY()][(int)p.getX()]=='g' ||
				ascii_grid[(int)p.getY()][(int)p.getX()]=='k' ||
				ascii_grid[(int)p.getY()][(int)p.getX()]=='l';
	}
	
	private void move(){
		if(clearAhead()){ this.boat.move(); }
	}
	
	@Override
	public void paintComponent(Graphics g)
	{
		Graphics2D g2d = (Graphics2D) g;
		int tile_size = 16;
		for(int y=0; y<image_grid.length; y++)
		{
			for(int x=0; x<image_grid[y].length; x++)
			{
				g2d.drawImage(image_grid[y][x], tile_size*x+border_x, tile_size*y+border_y, this);
			}
		}
		g2d.drawImage(boat.getImage(), tile_size*boat.getX()+border_x, tile_size*boat.getY()+border_y, this);
	}

	/*TODO public void setImage(String image_file)
	{
		image = loadImage(image_file);
	}*/

	private class TAdapter extends KeyAdapter
	{
		@Override
		public void keyReleased(KeyEvent e) 
		{
			//System.out.println(e.getKeyCode());
			key_setter.keyReleased(e.getKeyCode());
			//Escape key closes the window
			if(e.getKeyCode()==27){ System.exit(0); }
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
			//System.out.println("\nx:"+MouseInfo.getPointerInfo().getLocation().x);
			//System.out.println("y:"+MouseInfo.getPointerInfo().getLocation().y);
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