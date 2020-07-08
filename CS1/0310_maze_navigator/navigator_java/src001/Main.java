
public class Main
{	//The JPanel that the game runs in
	private GameFrame game_frame;
	public static ImageManager image_manager = new ImageManager();
	
	public Main()
	{	//Create the game frame and board within it
		game_frame = new GameFrame();
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
		while(true)
		{
			game_frame.update();
			game_frame.updateGraphics();
			delay(200);
		}
	} //public void animationLoop()
	
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