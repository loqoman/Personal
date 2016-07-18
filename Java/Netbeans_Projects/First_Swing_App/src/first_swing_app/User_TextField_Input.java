/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package first_swing_app;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.UIManager;

/**
 *
 * @author Darwin
 */
public class User_TextField_Input extends JFrame {
    boolean status = true;

                                            //Must define varibles in the class
    JButton Hello,Disable;                  //Button that welcomes the user
    JTextField  textBox;                 //Button to disable the other button
    public User_TextField_Input(){
        super("User");              //Title of the window
        setSize(300,300);           //Setting the size of the window
                                    //JButtons
        Hello = new JButton("Hello!"); 
        Disable = new JButton("Toggle Other Button");
        textBox = new JTextField( 20 );

   
        JPanel pane = new JPanel();
        pane.add(Hello);    //Adding the hello button to the panel
        pane.add(Disable);  //Adding the disable button to the pane
        pane.add( textBox );
        add(pane);          //Adding this pane to the window(JPanel)
        
        pack();                                         //In order to handle multiple objects
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //setting exit method on the window
        setLookAndFeel();                               //Basic setup methods 
        setVisible(true);
                                                        //In the form of...Class.Handler <Name> = new Class.Handler
        User_TextField_Input.ButtonHandler button_wait = new User_TextField_Input.ButtonHandler();
        User_TextField_Input.ButtonDisableHandler button_disable = new User_TextField_Input.ButtonDisableHandler();
        Hello.addActionListener(button_wait);
        Disable.addActionListener(button_disable);
        

    }
    private static void setLookAndFeel(){
        try{
            UIManager.setLookAndFeel(
                    "com.sun.java.swing.plaf.nimbus.NimbusLookAndFeel"
            );
        }catch (Exception exc){
            System.out.println("Oh Noes! Somethig whent wrong :(");
        }
    }
    public static void main(String[] args){
        setLookAndFeel();
        User_TextField_Input WiNdOw = new User_TextField_Input();
    }
    
    public class ButtonHandler  implements ActionListener
    //handler to tell the user a message when the button is pressed
    {
        public void actionPerformed( ActionEvent event )
        {
            /* Used to print hello when the user presses the button
            */
            //JTextField textBox = (JTextField)event.getSource();
            String message = "You wrote: " + textBox.getText();
            JOptionPane.showMessageDialog( null, message );
        }
    }
    public class ButtonDisableHandler implements ActionListener{
      
        public void actionPerformed(ActionEvent event){
            
            if (status){
                status = false;
            }else{
                status = true;
            }
                       
            
            System.out.println(status); //Debugging
            Hello.setEnabled(status);
        }
              



    }

}
