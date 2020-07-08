
public class Main
{	//The JPanel that the game runs in
	private GameFrame game_frame;
	public static ImageManager image_manager = new ImageManager();
	private Board board;
	
	public Main()
	{	//Create the game frame and board within it
		game_frame = new GameFrame();
		board = game_frame.getBoard();
	}

	//Starts a new thread and runs the game loop in it.
	public void runGameLoop()
	{
		Thread loop = new Thread()
		{
			public void run()
			{
				animationLoop();
			}
		};
		loop.start();
	}

	public void animationLoop()
	{	//TODO
		/* I want move, turn, clearAhead, xy, goal xy, heading, 
		 * clear left, clear right, all in main.
		 * Then I want an easy map and a challenge map.
		 * And my own solution to each.
	move
	isClearAhead
	isClearLeft
	isClearRight
	turnClockwise
	turnCounterClockwise
	getGoalX
	getGoalY
	getBoatX
	getBoatY
	getBoatHeading
		 * */
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
		}
	} //public void animationLoop()

	

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
		delay(300);
	}
	
	private void turnCounterClockwise()
	{
		this.board.turnCounterClockwise();
		game_frame.updateGraphics();
		delay(300);
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
		delay(300);
		if(board.success())
		{
			board.spawnRockets();
			for(int i=0; i<100; i++)
			{
				board.update(50.0/1000.0);
				game_frame.updateGraphics();
				delay(50);
			}
			System.exit(0);
		}
	}	
}