/* Most of the code immediately below is just copied from SwingHelloWorld.java */
import javax.swing.*;

/* This is new; we need stuff from the awt packages so that we can process
 * user input.
 */
import java.awt.*;
import java.awt.event.*;

public class SwingInputDemo2 implements Runnable
{
    /* This is new; instance variables to hold JTextBox and JButton components */
    private JTextField  textBox_;
    private JButton     okButton_;

    public static void main( String[] args )
    {
        SwingInputDemo2 demo = new SwingInputDemo2();
        SwingUtilities.invokeLater( demo );
    }
    
    public void run()
    {
        createGUI();
    }
    
    private void createGUI()
    {
        JFrame frame = new JFrame( "Swing Input Demo 2" );
        frame.setDefaultCloseOperation( JFrame.EXIT_ON_CLOSE );

        /* I chose to do the layout in a separate method so that it will be
         * easier to see the logic that is used to set up the OK button to
         * tell us when it is clicked. The doLayout method will create all
         * the components and arrange them within the JFrame.
         */
        doLayout( frame );

        /* This is how we set up the OK button so that we will know when it
         * is clicked. "ButtonListener" is a private class that we define
         * below.
         */
        ButtonListener listener = new ButtonListener();
        okButton_.addActionListener( listener );
        
        /* This time we won't bother to add a listener to the text box. We 
         * will just wait until the OK button is clicked, then we will 
         * display whatever was typed into the text box in a JOptionPane.
         */
        
        /* Show the dialog. */
        frame.setVisible( true );
    }

    /**************************************************************************
     * The doLayout Method
     * ===================
     * This method uses a GridBagLayout to position the frame's components.
     * It divides the frame into a grid of two rows and two columns. A label
     * ("Swing Input Demo 2") goes in the cell (0,0); a text box goes in 
     * cell (1,0). An OK button occupies both cells (1,0) and (1,1). Each cell
     * will be separated from the inside of the frame and each other (that is,
     * they will be "inset") by a margin of 5 pixels.
     *
     *                 +-----------------------------------+
     *                 |                 |                 |
     *                 |                 |                 |
     *                 |     label       |    text box     |
     *                 |                 |                 |
     *                 |                 |                 |
     *                 |-----------------+-----------------|
     *                 |                 |                 |
     *                 |            +---------+            |
     *                 |            |   O K   |            |
     *                 |            +---------+            |
     *                 |                 |                 |
     *                 +-----------------------------------+
     **************************************************************************/

    private void doLayout( JFrame frame )
    {
        JLabel  label   = new JLabel( "Swing Input Demo 2" );
        textBox_ = new JTextField( 20 );
        okButton_ = new JButton( "OK" );

        /* Most of the work we need to do requires manipulation of the
         * container component of the frame.
         */
        Container container = frame.getContentPane();
        
        /* Create and set the GridBagLayout manager. */
        container.setLayout( new GridBagLayout() );

        /* A GridBagConstraints object is used to determine the cell position
         * of the label, text box and OK button.
         */
        GridBagConstraints gbc = new GridBagConstraints();

        /* The fill constraint determines how a component is resized if it is
         * too small to fit in its cell. We don't want the component resized
         * at all.
         */
        gbc.fill = GridBagConstraints.NONE;

        /* The insets constraint determines the margins. */
        gbc.insets = new Insets( 5, 5, 5, 5 );
        
        /* The label goes in cell (0,0). */
        gbc.gridx = 0;
        gbc.gridy = 0;
        container.add( label, gbc );
        
        /* The text box goes in cell (1,0). */
        gbc.gridx = 1;
        gbc.gridy = 0;
        container.add( textBox_, gbc );

        /* The OK Button starts in cell (0,1), and spans two cells. */
        gbc.gridx = 0;
        gbc.gridy = 1;
        gbc.gridwidth = 2;
        container.add( okButton_, gbc );

        /* Tell the layout manager to perform the layout. */
        frame.pack();
    }
    
    /**************************************************************************
     * The ButtonListener Class
     * ========================
     * We need an object of this type to "listen" for events that occur in
     * the OK button. The "implements ActionListener" is a promise to the
     * compiler to have a "public void actionPerformed( ActionEvent )"
     * method.
     */
    private class ButtonListener implements ActionListener
    {
        /* This method is called when the OK button is clicked. */
        public void actionPerformed( ActionEvent event )
        {
            String msg = "text: " + textBox_.getText();
            JOptionPane.showMessageDialog( null, msg );
        }
    }
}
