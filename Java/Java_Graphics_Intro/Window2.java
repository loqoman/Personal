/*
* Currentley not a working build
* Looks like there is 2 differnent graphics modules that I
* Need to play around with
* ---------------------------
* Paint function used in Window2_Viewer
*
*/
import java.awt.*; //This means to import all classes from the awt package
import java.awt.Graphics2D;
import java.awt.event.*;
import javax.swing.*;
import java.util.Scanner; //Used to get keyboard input
import java.applet.Applet; // Used to do the applets
import java.awt.Graphics;

public class Window2 extends JPanel {
	//Making our graphics object

	//Our paint function
	
	
	public void paint (Graphics g) {
		super.paintComponent(g);
		this.setBackground(Color.WHITE);
		g.setColor(Color.BLACK);
		g.fillRect(25,25,100,30);

		
	}
	//Main loop
}
//If im curoius [- if ( width > 0.0 && height > 0.0 ) ]
//Is proper AND logic
//JFrame class
// :]
/*
class Graphics_Object extends javax.swing.JFrame
{
    private static final long serialVersionUID = 0x10L;

	private static final int EDGE = 3, TOP = 30;  // around the JFrame
	private Image itsPicture;
	private Graphics itsPage;

	public TurtleWorld (int width, int height)
	{	super ("Turtle Drawings");  // set the title for the frame
		setDefaultCloseOperation (EXIT_ON_CLOSE); // no WindowListener
		setSize (width + 2 * EDGE, height + TOP + EDGE);
		toFront();  // put this frame in front of the BlueJ window
		setVisible (true);  // cause a call to paint
		begin (width, height);
	}	//======================


	public void begin (int width, int height)
	{	itsPicture = new java.awt.image.BufferedImage (width, height,
			           java.awt.image.BufferedImage.TYPE_INT_RGB);
		itsPage = itsPicture.getGraphics();
		itsPage.setColor (Color.white);
		itsPage.fillRect (0, 0, width, height);
		itsPage.setColor (Color.black);
	}	//======================


	public Graphics getPage()
	{	return itsPage; // itsPicture.getGraphics(); => NO COLORS
	}	//======================


	public void paint (Graphics g)
	{	if (itsPicture != null)
			g.drawImage (itsPicture, EDGE, TOP, this);
		Turtlet.paintPaintmes();
	}	//======================

}
*/