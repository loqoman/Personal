/* Use this program as a template for creating your own Java GUI. Substitute your
   class name for "HelloWorld."
*/

/* There are several places to look for Java GUI components, including the javax.swing 
 * and java.awt packages.
 */
import javax.swing.*;
//And the AWT packages
import java.awt.*;
import java.awt.event.*;

/* "implements runnable" is a promise to the compiler that your class will have
   have a method with the signature "public void run()."
 */
 //Good comment
public class SwingHelloWorld implements Runnable
{
    public static void main( String[] args )
    {
        /* Your main method should be this simple: create an object the same
           type as your class, then call SwingUtilities.invokeLater. After a bit
           of internal Swing processing, control of your program will pass to your
           run  method.
        */
        SwingHelloWorld hello = new SwingHelloWorld();
        SwingUtilities.invokeLater( hello );
    }
    
    /* This is where you fulfill your promise that you made with the "implements
       runnable" clause you added to your class declaration.
    */
    public void run()
    {
        /* Create the initial part of your GUI. I chose to put all the details in a
           private method called "createGUI." You can split your creation logic
           between several methods, or put it all right here in "run."
        */
        createGUI();
    }
    
    private void createGUI()
    {
        /* For the time being, assume that every Java GUI is started by 
           creating a frame; this creates a dialog that serves as the principal
           part of your GUI. The string that you pass to the JFrame constructor
           will be displayed in the title bar of your dialog.
        */
        JFrame frame = new JFrame( "Hello World" );
        /* This tells the frame what to do if the user picks the "x" in the title bar
           of your GUI. Note that everything you've done up to this point is what
           you should do for every GUI that you create (at least, until you become
           more comfortable with the way that Swing works).
        */
        frame.setDefaultCloseOperation( JFrame.EXIT_ON_CLOSE );
        frame.setSize(500,500);  //Sets the size of the frame
								 //Worth noting that this does not work if you frame.pack();
        /* This next bit will be different for every dialog. This is where you will
           create the components that populate the dialog. In this simple example
           all we are doing is adding a label.
        */
		
		/* A GridBagConstraints object is used to determine the cell position
         * of the label, text box and OK button.
         */
		 
		 Container container = frame.getContentPane();
		 
		 //--------------------------//
		GridBagConstraints gbc = new GridBagConstraints();
		
        /* The fill constraint determines how a component is resized if it is
         * too small to fit in its cell. We don't want the component resized
         * at all.
         */
		
        gbc.fill = GridBagConstraints.NONE;
		
		container.setLayout( new GridBagLayout() );

		/* The insets constraint determines the margins. */

		gbc.insets = new Insets( 5, 5, 5, 5 );

        JLabel label = new JLabel( "Hello World" );

        /* To add a component to a frame, create the component, then locate the
           frame's content pane, then add the component to the content pane.
		   This is basicelly a text box that you dont define the x,y for
        */
		gbc.gridx = 3;
        gbc.gridy = 3;
        frame.getContentPane().add( label, gbc );


        /* Here are two more bits that will be common to all your GUIs. The 
           frame's pack method tells the frame to create and arrange all the bits
           and pieces of the dialog. There are lots of ways to customize the 
           arrangement; in this simple example we are just using the default
           arrangement method, which is to position all the components in the
           upper left-hand corner of the dialog. To get more creative with your
           arrangement, see 
           http://java.sun.com/docs/books/tutorial/uiswing/components/toplevel.html
        */
		//Frame.pack() makes the window the size of the object
		//Not going to use it right now
        //frame.pack();
        /* This makes the dialog visible, and available for interaction with the user. */
        frame.setVisible( true );
    }
}
