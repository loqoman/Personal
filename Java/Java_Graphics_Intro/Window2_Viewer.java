//Current working build
//Creates a window with a square on it
/*
Current qustions:
-----------------
Why does in all the swing demos they dont respond ().setsize(x,y)?


*/
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Window2_Viewer {
	public static void main(String[] args){
		JFrame f = new JFrame("Test Title 1"); //Our JFrame is called F for some reason 
		
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		Window2 rect = new Window2();
		f.add(rect);
		//Adding the textbox
		/*
		TextField  textBox = new JTextField( 20 );
        f.add( textBox );
		*/
		f.setSize(1000,500); // In the form of X,Y Sets the size of the window
		f.setVisible(true);
		//JOptionPane.showMessageDialog( null, "Make America Great Again" ); //Test message in a pop up window

	}
}