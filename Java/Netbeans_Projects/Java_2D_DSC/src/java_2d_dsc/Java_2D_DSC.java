/*
 * 2D application that is ment to include the pre-made UI and some new rectangles
 * 
 *
 */


package java_2d_dsc;

import java.awt.BorderLayout;
import java.awt.Color;
import javax.swing.*;//Importing packages
import java.awt.Graphics;

/*Simple application to controll a square within a pane 
 *With 4 buttons on the left. 
 * @author Darwin   
 */
public class Java_2D_DSC extends JFrame {
    public static JFrame Window;
        public final int window_X = 600;
        public final int window_Y = 300;
        
    public static void main(String[] args){
        Java_2D_DSC foobar = new Java_2D_DSC();
        foobar.DisplayGUI();
        //Rectangle_Setup rect = new Rectangle_Setup();
    }
    public void DisplayGUI(){
        Window = new JFrame("Move that square");
        Window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Window.setLayout(null);
        
        Button_Setup.Button_init();//can be found in:  java_2d_dsc/Button_setup.java
        
        Rectangle_init foo = new Rectangle_init();//ONLY DONE so that I dont have to deal with all this static and not staic 
        foo.Rect_Setup();                         //bullshit
        
        Window.setSize(window_X, window_Y);
        Window.setLocation(300,300);
        Window.setResizable(false);
        Window.setVisible(true);
        


       
    }

}
