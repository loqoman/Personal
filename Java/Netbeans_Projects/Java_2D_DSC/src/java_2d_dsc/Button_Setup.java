/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package java_2d_dsc;

import javax.swing.*;
import java.awt.*;
/**
 *
 * @author Darwin
 */
public class Button_Setup extends JFrame {
    public static int buttonY = 30;
    static Dimension button_size = new Dimension(200,30);
    static JPanel contentPane;
    public static void Button_init() {
        contentPane = new JPanel();//Setting up the window to work with absolute positinos 
        contentPane.setLayout(null);
        //Controls initilization
        JLabel title = new JLabel("Use these buttons to move around!"); 
        title.setLocation(10,buttonY);
        title.setSize(300,20);
        //All the buttons and their positions reletive to each other
        JButton left = new JButton("Left");
        left.setLocation(10,buttonY + 30);
        left.setSize(button_size);
        
        JButton right = new JButton("right");
        right.setLocation(10,buttonY + 60);
        right.setSize(button_size);
      
        JButton up = new JButton("up");
        up.setLocation(10,buttonY + 90);
        up.setSize(button_size);
        
        JButton down = new JButton("down");
        down.setLocation(10,buttonY + 120);
        down.setSize(button_size);

        contentPane.add(title);
        //Buttons \/
        contentPane.add(left);
        contentPane.add(right);
        contentPane.add(up);
        contentPane.add(down );
        
        Java_2D_DSC.Window.add(contentPane);
    }
    public static void main(String... args){
    }
    
}
