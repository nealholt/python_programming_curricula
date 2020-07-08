import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.Toolkit;
import java.awt.image.BufferStrategy;
import javax.swing.JFrame;

public class GameFrame extends JFrame 
{
	private static final long serialVersionUID = 1L;
	private Board board;

	public GameFrame(String map) 
	{
		board = new Board(map);
		add(board);
        //Add the minimize, maximize, and close buttons only
		//in the not-fullscreen version
		setUndecorated(false);
        setVisible(true);
        setSize(1000,600);
		setResizable(true);
		setTitle("My Java Game");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        toFront();
		//This is a finnicky little annoying method.
		//It has to be called after the frame is visible and board has been
		//added and other stuff.
		this.createBufferStrategy(2);
	}

	/* Calls render with Graphics2D context and takes care 
	 * of double buffering.
	 * I took this from here:
	 * http://www.java-gaming.org/index.php?topic=24220.0 */
	public void updateGraphics()
	{
		BufferStrategy bf = this.getBufferStrategy();
		Graphics2D g = null;
		try 
		{
			g = (Graphics2D) bf.getDrawGraphics();
			g.setBackground(Color.BLACK);
			g.clearRect(0, 0, getWidth(), getHeight());
			this.board.paintComponent(g);
		} 
		finally 
		{
			g.dispose();
		}
		// Shows the contents of the backbuffer on the screen.
		bf.show();
		//Tell the System to do the Drawing now, otherwise it can take a few extra ms until 
		//Drawing is done which looks very jerky
		Toolkit.getDefaultToolkit().sync();
	} //public void updateGraphics()
	
	public Board getBoard()
	{
		return this.board;
	}

}