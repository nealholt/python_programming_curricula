
public class Main
{	//The JPanel that the game runs in
	private GameFrame game_frame;

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
	{
		//Add your code here.
		String[] image_list = {"images/right000.png",
				"images/right001.png",
				"images/right002.png",
				"images/right003.png"};
		int x=0;
		while(true)
		{
			for(int i=0; i<image_list.length; i++)
			{
				//game_frame.setImage(image_list[i]);
				//game_frame.setImageXY(x,300);
				x+=5;
				game_frame.updateGraphics();
				delay(150);
			}
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