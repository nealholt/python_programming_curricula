
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
		 * Maybe also an "is successful" check. Make this automatic with surprise fireworks?!
		 * 
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
		while(true)
		{
			move();
		}
	} //public void animationLoop()

	
	
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
	
/*	private boolean isClearAhead()
	{
		
	}

	private boolean isClearLeft()
	{
		
	}
	
	private boolean isClearRight()
	{
		
	}

	private void turnClockwise()
	{
		
	}
	
	private void turnCounterClockwise()
	{
		
	}
	
	getGoalX
	getGoalY
	getBoatX
	getBoatY
	getBoatHeading
*/
	
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
}