/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package first_swing_app;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.Container;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import javax.swing.JFrame;
import javax.swing.JLabel;

/**
 *
 * @author Darwin
 */

public class Disable_That_Button extends JFrame {
    public String msg = "Hello World!";     //The message that the use gets when they press the button
    boolean status = true;

                                            //Must define varibles in the class
    JButton Hello,Disable;                  //Button that welcomes the user
                                            //Button to disable the other button
    public Disable_That_Button(){
        super("Button Disabling");  //Title of the window
        setSize(300,300);           //Setting the size of the window
                                    //JButtons
        Hello = new JButton("Hello!"); 
        Disable = new JButton("Toggle Other Button");
        JPanel pane = new JPanel();
        pane.add(Hello);    //Adding the hello button to the panel
        pane.add(Disable);  //Adding the disable button to the pane
        add(pane);          //Adding this pane to the window(JPanel)
        
        //pack();                                       //In order to handle multiple objects
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //setting exit method on the window
        setLookAndFeel();                               //Basic setup methods 
        setVisible(true);
                                                        //In the form of...Class.Handler <Name> = new Class.Handler
        Disable_That_Button.ButtonHandler button_wait = new Disable_That_Button.ButtonHandler();
        Disable_That_Button.ButtonDisableHandler button_disable = new Disable_That_Button.ButtonDisableHandler();
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
        Disable_That_Button WiNdOw = new Disable_That_Button();
    }
    
    public class ButtonHandler  implements ActionListener
    //handler to tell the user hello when the button is pressed
    {
        public void actionPerformed( ActionEvent event )
        {
            /* Used to print hello when the user presses the button
            */
            JOptionPane.showMessageDialog( null, msg );
        }
    }
    public class ButtonDisableHandler implements ActionListener{
      
        public void actionPerformed(ActionEvent event){
            
            if (status){
                status = false;
            }else{
                status = true;
            }
                       
            Hello.setEnabled(status);
        }
              



    }

}
