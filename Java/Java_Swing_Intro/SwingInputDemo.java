/* Most of the code immediately below is just copied from SwingHelloWorld.java */ import javax.swing.*;

/* This is new; we need stuff from the awt packages so that we can process
 * user input.
*/
import java.awt.*;
import java.awt.event.*;

public class SwingInputDemo implements Runnable
{
    public static void main( String[] args )
    {
        SwingInputDemo demo = new SwingInputDemo();
        SwingUtilities.invokeLater( demo );
    }
    
    public void run()
    {
        createGUI();
    }
    
    private void createGUI()
    {
        JFrame frame = new JFrame( "Swing Input Demo" );
        frame.setDefaultCloseOperation( JFrame.EXIT_ON_CLOSE );     
        JLabel label = new JLabel( "Swing Input Demo" );
        frame.getContentPane().add( label );
        
        /* With the exception of two lines below, the code from here forward is
           unique to SwingInputDemo.java.
        */
        
        /* Most of the work we need to do requires manipulation of the container
         * component of the frame.
        */
        Container container = frame.getContentPane();
        
        /* This tells the container to arrange its components in a grid, from 
         * left to right and top to bottom.
        */
        container.setLayout( new FlowLayout() );
        
        /* This is a box for the user to type text. Only one line of text is allowed. */
        JTextField  textBox = new JTextField( 20 );
        container.add( textBox );
        
        /* This is how we are able to get input from the text field.  We create an
         *  object (in this case from a private class, below) that "listens" for things
         * happening ("events") in the text box. Every time the user types enter
         * in the text field the listener is notified and given an opportunity to
         * respond.
         */
         TextHandler textListener = new TextHandler();
         textBox.addActionListener( textListener );
         
         /* Set the width and height of the frame (that is, the dialog). */
         frame.setSize( 325, 100 );
        
        /* These two lines were copied from SwingHelloWorld.java */
        frame.pack();
        frame.setVisible( true );
    }
    
    /* We need an object of this type to "listen" for events that occur in a text
     * box. Every time the user types enter this object will be notified and
     * given an opportunity to respond. The phrase "implements action listener"
     * is a promise to the compiler that this class will have a method named
     * "public void actionPerformed( ActionEvent event )."
    */
    private class TextHandler implements ActionListener
    {
        public void actionPerformed( ActionEvent event )
        {
            /* The ActionEvent object can tell us all sorts of things about
             * what happened, including the in which object (the "source")
             * that the event occurred. Unfortunately, the ActionEvent object
             * only knows that the source was type Object; to tell the compiler
             * that the source is specifically a JTextField object we use
             * "(JTextField)" (this is know as a "cast").
            */
            JTextField textBox = (JTextField)event.getSource();
            String msg = "text: " + textBox.getText();
            JOptionPane.showMessageDialog( null, msg );
        }
    }
}
