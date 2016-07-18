/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package java_2d_dsc;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Graphics;
import static java_2d_dsc.Java_2D_DSC.Window;
import javax.swing.JPanel;

/**
 *
 * @author psp504ap001
 */
public class Rectangle_init extends JPanel {
    //Position of square
    final private int oneX = 300;
    final private int oneY = 200;
    DrawPanel drawPanel;
    
    public void Rect_Setup(){
        //rect_pane.setBounds(Java_2D_DSC.window_X + 400,Java_2D_DSC.window_Y);
        drawPanel = new DrawPanel();
        Button_Setup.contentPane.add(drawPanel);

                                           //Fun fact, if I just add the rect directly to the window it only draws the rect
                                           //and that sucks.
    }
    class DrawPanel extends JPanel {       // class to hold the drawpanel, which holds the rectangles
        public void paintComponent(Graphics g) {
            g.setColor(Color.BLACK);
            g.fillRect(oneX, oneY, 6, 6);
        }
    }
}
