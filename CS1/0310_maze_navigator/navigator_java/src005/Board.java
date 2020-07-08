import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Point;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.MouseEvent;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import javax.swing.JPanel;
import javax.swing.event.MouseInputListener;

public class Board extends JPanel 
{	//Original code came largely from this tutorial:
	//http://zetcode.com/tutorials/javagamestutorial/movingsprites/
	private static final long serialVersionUID = 1L;
	private ArrayList<Rocket> rockets = new ArrayList<Rocket>();
	private KeyManager key_setter = new KeyManager();
	private BufferedImage[][] image_grid;
	private char[][] ascii_grid;
	private int border_x = 10;
	private int border_y = 40;
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
	private int goal_x, goal_y;

	public Board(String map)
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
		//Create the grid of images and ascii grid
		List<String> lines;
		try{
			lines = this.readSmallTextFile(map);
			image_grid = new BufferedImage[lines.size()][lines.get(0).length()];
			ascii_grid = new char[lines.size()][lines.get(0).length()];
			for(int y=0; y<image_grid.length; y++)
			{
				for(int x=0; x<image_grid[y].length; x++)
				{
					ascii_grid[y][x] = lines.get(y).charAt(x);
					//set goal
					if(ascii_grid[y][x] == 'k')
					{
						goal_x = x; goal_y = y;
					}
					//set player start location
					if(ascii_grid[y][x] == 'q')
					{
						//Create the boat
						boat = new Boat(x, y);
					}
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
	
	private boolean locationIsClear(int x, int y)
	{
		return 	ascii_grid[y][x]=='i' ||
				ascii_grid[y][x]=='f' ||
				ascii_grid[y][x]=='g' ||
				ascii_grid[y][x]=='k' ||
				ascii_grid[y][x]=='l';
	}
	
	//Is the path ahead of the boat clear?
	public boolean clearAhead()
	{
		Point p = boat.getCoordinatesAhead();
		return locationIsClear((int)p.getX(), (int)p.getY());
	}
	
	//Is the path left of the boat clear?
	public boolean clearLeft()
	{
		Point p = boat.getCoordinatesLeft();
		return locationIsClear((int)p.getX(), (int)p.getY());
	}
	
	//Is the path right of the boat clear?
	public boolean clearRight()
	{
		Point p = boat.getCoordinatesRight();
		return locationIsClear((int)p.getX(), (int)p.getY());
	}

	public void turnClockwise()
	{
		this.boat.turnClockwise();
	}
	
	public void turnCounterClockwise()
	{
		this.boat.turnCounterClockwise();
	}
	
	//Is the boat successful in reaching its destination?
	public boolean success()
	{
		int x = boat.getX();
		int y = boat.getY();
		return 	ascii_grid[y][x]=='k';
	}
	
	public int getGoalX(){ return goal_x; }
	public int getGoalY(){ return goal_y; }
	public int getBoatX(){ return boat.getX(); }
	public int getBoatY(){ return boat.getY(); }
	public String getBoatHeading(){ return boat.getHeading(); }
	
	//Spawn rockets as a surprise celebration for success
	public void spawnRockets()
	{
		Random r = new Random();
		for(int i=0; i<15; i++)
		{
			rockets.add(
					new Rocket(200, //x
							250, //y
							(r.nextDouble()*400)-200,//dx
							-150-r.nextInt(300),//dy
							5, //radius
							1.0, //fuse in seconds
							this)
					);
		}
	}

	//Add one rocket. This is needed for secondary explosions.
	public void addRocket(Rocket r)
	{
		rockets.add(r);
	}
	
	//Move the boat if the path is clear.
	public void move(){
		if(clearAhead()){ this.boat.move(); }
	}
	
	@Override
	public void paintComponent(Graphics g)
	{
		//Draw the world
		Graphics2D g2d = (Graphics2D) g;
		g2d.scale(2.5, 2.5);
		int tile_size = 16;
		for(int y=0; y<image_grid.length; y++)
		{
			for(int x=0; x<image_grid[y].length; x++)
			{
				g2d.drawImage(image_grid[y][x], tile_size*x+border_x, tile_size*y+border_y, this);
			}
		}
		//Draw the boat
		g2d.drawImage(boat.getImage(), tile_size*boat.getX()+border_x, tile_size*boat.getY()+border_y, this);
		//Draw rockets
		Rocket r;
		for(int i=0; i<rockets.size(); i++)
		{
			r = rockets.get(i);
			r.draw(this, g);
		}
	}
	
	///Update teh rockets
	public void update(double elapsed_seconds)
	{
		for(int i=0; i<rockets.size(); i++)
		{
			rockets.get(i).update(elapsed_seconds);
		}
	}

	private class TAdapter extends KeyAdapter
	{
		@Override
		public void keyReleased(KeyEvent e) 
		{
			//System.out.println(e.getKeyCode());
			key_setter.keyReleased(e.getKeyCode());
			//Escape key closes the window
			if(e.getKeyCode()==27){ System.exit(0); }
			
			//For now, every key ends the game:
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