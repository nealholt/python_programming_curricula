public class KeyManager 
{
	public boolean[] ascii_input;
	private double mouse_x;
	private double mouse_y;
	private boolean mouse_pressed;

	//Check what keys have been released with this array.
	private boolean[] ascii_release;

	public KeyManager() 
	{
		ascii_input = new boolean[526];
		ascii_release = new boolean[526];
    }
	
	public void keyPressed(int key)
	{
		//System.out.println(key);
		ascii_input[key] = true;
	}
	
	public void keyReleased(int key)
	{
		ascii_input[key] = false;
		ascii_release[key] = true;
	}
	
	//Check that a key was released and set its
	//released indicator back to false
	public boolean checkKeyReleased(int key)
	{
		boolean temp = ascii_release[key];
		ascii_release[key] = false;
		return temp;
	}
	
	public void mousePressed()
	{
		this.mouse_pressed = true;
	}

	public void mouseReleased()
	{
		this.mouse_pressed = false;
	}
	
	public boolean getMousePressed()
	{
		return this.mouse_pressed;
	}
	
	public void mouseMoved(int x, int y)
	{
		this.mouse_x = (double)x;
		this.mouse_y = (double)y;
	}
	
	public double getMouseX()
	{
		return this.mouse_x;
	}
	
	public double getMouseY()
	{
		return this.mouse_y;
	}
}