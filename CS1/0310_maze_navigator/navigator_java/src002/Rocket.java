import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.util.Random;

public class Rocket
{	//Coordinates
	private double x;
	private double y;
	//velocity of the sprite
	private double dx = 0;
	private double dy = 0;
	//Radius of the circular rocket
	private double radius;
	//How long until the explosion
	private double fuse; //seconds
	//Number of sub-rockets to spawn
	private int bomblets = 10;
	//Strength of gravity
	private double gravity = 250; //px / sec / sec
	//Reference to the board for adding more rockets
	private Board board_reference;
	//Color of this Rocket
	private Color color;
	
	private Random rand_gen = new Random();

	//Constructor
	public Rocket(double x, double y, 
			double dx,
			double dy,
			double radius,
			double fuse,
			Board board_reference)
	{
		this.x = x;
		this.y = y;
		this.dx = dx;
		this.dy = dy;
		this.radius = radius;
		this.fuse = fuse;
		this.board_reference = board_reference;
		color = new Color(rand_gen.nextInt(255),
				rand_gen.nextInt(255),
				rand_gen.nextInt(255));
	}
	
	public double getX()
	{
		return x;
	}

	public double getY()
	{
		return y;
	}

	public double getRadius()
	{
		return radius;
	}

	public void move(double elapsed_seconds) 
	{
		this.x += this.dx * elapsed_seconds;
		this.y += this.dy * elapsed_seconds;
	}
	
	/* Draw this sprite. */
	public void draw(Board b, Graphics g)
	{
		//Draw this sprite's image
		Graphics2D g2d = (Graphics2D) g;
		g2d.setColor(color);
		g2d.fillOval((int)this.x,
					 (int)this.y,
					 (int)this.radius*2, (int)this.radius*2);
	}

	/* This method is intended to be called once per frame and 
	 * will update this sprite.
	 * double elapsed_seconds is the number of seconds that
	 * elapsed since the previous update.
	 */
	public void update(double elapsed_seconds)
	{
		this.move(elapsed_seconds);
		fuse -= elapsed_seconds;
		if(fuse < 0)
		{
			fuse = Double.MAX_VALUE;
			for(int i=0; i<bomblets; i++)
			{
				board_reference.addRocket(
						new Rocket(this.getX(), //x
								this.getY(), //y
								this.dx+rand_gen.nextInt(200)-100,//dx
								this.dy+rand_gen.nextInt(200)-100, //dy
								5, //radius
								Double.MAX_VALUE, //fuse
								board_reference)
						);
			}
		}
		this.dy += gravity*elapsed_seconds;
	}
}