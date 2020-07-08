import java.awt.Point;
import java.awt.image.BufferedImage;

public class Boat
{
	private final String[] headings = {"east","north","west","south"};
	private BufferedImage image;
	private int x,y;
	private int heading = 0;
	
	public Boat(int x, int y)
	{
		this.image = Main.image_manager.getImage("53,15", 0);
		this.x = x;
		this.y = y;
	}
	
	public BufferedImage getImage(){ return image; }
	public int getX(){return x;}
	public int getY(){return y;}
	private void moveNorth(){this.y--;}
	private void moveSouth(){this.y++;}
	private void moveEast(){this.x++;}
	private void moveWest(){this.x--;}
	public Point getCoordinatesAhead(){
		if(headings[heading].equals("east")){
			return new Point(x+1, y);
		}
		else if(headings[heading].equals("west")){
			return new Point(x-1, y);
		}
		else if(headings[heading].equals("north")){
			return new Point(x, y-1);
		}
		else{
			return new Point(x, y+1);
		}
	}
	public void move(){
		if(headings[heading].equals("east")){moveEast();}
		else if(headings[heading].equals("west")){moveWest();}
		else if(headings[heading].equals("north")){moveNorth();}
		else{moveSouth();}
	}
	public void turnClockwise(){
		heading--;
		if(heading<0){ heading+=headings.length; }
		updateImage();
	}
	public void turnCounterClockwise(){
		heading = (heading+1)%headings.length;
		updateImage();
	}
	private void updateImage(){
		if(headings[heading].equals("east")){
			this.image = Main.image_manager.getImage("53,15", 0);
		}
		else if(headings[heading].equals("west")){
			this.image = Main.image_manager.getImage("53,18", 0);
		}
		else if(headings[heading].equals("north")){
			this.image = Main.image_manager.getImage("53,15", -Math.PI/2);
		}
		else{
			this.image = Main.image_manager.getImage("53,18", -Math.PI/2);
		}
	}
}