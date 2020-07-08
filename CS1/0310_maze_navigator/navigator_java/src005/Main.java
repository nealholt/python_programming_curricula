
public class Main
{	//The JPanel that the game runs in
	private GameFrame game_frame;
	public static ImageManager image_manager = new ImageManager();
	private Board board;
	private int game_delay = 300;
	
	public Main()
	{	//Create the game frame and board within it
		//TODO: Change the map here.
		game_frame = new GameFrame("maps/starting_map.txt");
		board = game_frame.getBoard();
	}

	//Starts a new thread and runs the game loop in it.
	public void runGameLoop()
	{
		Thread loop = new Thread()
		{
			public void run()
			{
				actionLoop();
			}
		};
		loop.start();
	}

	public void actionLoop()
	{	/* Your functions include:
		 * move() - moves the boat ahead 1 is the way is clear
		 * isClearAhead() - returns true if there is no obstacle ahead
		 * isClearLeft() - returns true if there is no obstacle left
		 * isClearRight() - returns true if there is no obstacle right
		 * turnClockwise() - turns the boat clockwise
		 * turnCounterClockwise() - turns the boat counterclockwise
		 * getGoalX() - returns the x coordinate of the goal
		 * getGoalY() - returns the y coordinate of the goal
		 * getBoatX() - returns the x coordinate of the boat
		 * getBoatY() - returns the y coordinate of the boat
		 * getBoatHeading() - returns the heading of the boat as a
		 * 					String: north, south, east, or west.
		 * 
		 * If you would like to speed up or slow down the game,
		 * change the integer variable game_delay. For example:
		 * game_delay = 100; //faster
		 * game_delay = 800; //slower
		 */
		//TODO Write your code here.
		String heading = getBoatHeading();
		while(true)
		{
			//Turn east and head toward destination
			while(!heading.equals("east"))
			{
				turnClockwise();
				heading = getBoatHeading();
			}
			while(getGoalX()>getBoatX() && isClearAhead())
			{
				move();
			}
			//Turn west and head toward destination
			while(!heading.equals("west"))
			{
				turnClockwise();
				heading = getBoatHeading();
			}
			while(getGoalX()<getBoatX() && isClearAhead())
			{
				move();
			}
			//Turn south and head toward destination
			while(!heading.equals("south"))
			{
				turnClockwise();
				heading = getBoatHeading();
			}
			while(getGoalY()>getBoatY() && isClearAhead())
			{
				move();
			}
			//Turn north and head toward destination
			while(!heading.equals("north"))
			{
				turnClockwise();
				heading = getBoatHeading();
			}
			while(getGoalY()<getBoatY() && isClearAhead())
			{
				move();
			}
			//I'm headed north check if the way is blocked
			//or if I'm even with goal.
			if(!isClearAhead() || getGoalY()==getBoatY())
			{
				//Follow along the edge of the obstacle 
				//until my y value is less then what it was 
				//when I started.
				int distance = Math.abs(getBoatY()-getGoalY()) + Math.abs(getBoatX()-getGoalX());
				while(distance <= Math.abs(getBoatY()-getGoalY()) + Math.abs(getBoatX()-getGoalX()))
				{
					if(isClearAhead())
					{
						move();
					}
					else if(isClearRight())
					{
						turnClockwise();
					}
					else
					{
						turnCounterClockwise();
					}
				}
			}
		}
		
	} //public void actionLoop()

	

	private boolean isClearAhead()
	{
		return board.clearAhead();
	}

	private boolean isClearLeft()
	{
		return board.clearLeft();
	}
	
	private boolean isClearRight()
	{
		return board.clearRight();
	}

	private void turnClockwise()
	{
		this.board.turnClockwise();
		game_frame.updateGraphics();
		delay(game_delay);
	}
	
	private void turnCounterClockwise()
	{
		this.board.turnCounterClockwise();
		game_frame.updateGraphics();
		delay(game_delay);
	}

	private int getGoalX(){ return board.getGoalX(); }
	private int getGoalY(){ return board.getGoalY(); }
	private int getBoatX(){ return board.getBoatX(); }
	private int getBoatY(){ return board.getBoatY(); }
	private String getBoatHeading(){ return board.getBoatHeading(); }

	private void delay(int milliseconds)
	{
		Thread.yield();
		try {Thread.sleep(milliseconds);} catch(Exception e){}			
	}

	public static void main(String[] args) 
	{	//https://docs.oracle.com/javase/tutorial/essential/concurrency/runthread.html
		Main m = new Main();
		m.runGameLoop();
	}

	private void move()
	{
		board.move();
		game_frame.updateGraphics();
		delay(game_delay);
		if(board.success())
		{
			board.spawnRockets();
			for(int i=0; i<80; i++)
			{
				board.update(50.0/1000.0);
				game_frame.updateGraphics();
				delay(50);
			}
			System.exit(0);
		}
	}	
}