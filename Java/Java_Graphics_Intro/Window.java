import java.awt.*;
public class Window extends java.applet.Applet {
	
	
	public void init () {
		setBackground (Color.red);
	}
	public void paint (Graphics g) {
		g.setColor (Color.green);
		g.setXORMode (Color.blue);
		g.fillRect (10, 10, 100, 100);
		g.fillRect (10, 60, 100, 100);
	}
}